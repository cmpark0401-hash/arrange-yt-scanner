"""야담 영상 자막 corpus → 표준 구조·어휘 패턴 추출.

corpus의 각 영상에서:
1. Hook 0~30초 텍스트 추출 → 첫 문장·평균 어휘 통계
2. 도입 30초~3분 → 인물·배경 소개 패턴
3. 중반 30~70% 지점 → 갈등 절정 (조회 그래프상 retention drop 직전)
4. 결말 마지막 60초 → 마무리 패턴
5. 전체 길이·분량·고빈도 어휘·발화 속도

출력: _yadam_structure_patterns.json
- structure_template: 표준 구조 (Hook 30초, Intro 3분, Body N분, Climax 5분, Outro 60초)
- hook_pool: 영상별 Hook 첫 문장 모음 (Hook 작성 시 풀)
- closing_pool: 결말 마지막 문장 모음
- vocab_signature: 야담 채널 공통 어휘 (검증 표현)
- per_video: 영상별 상세 구조
"""
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "channels" / "knowledge-archive" / "_monitor_logs"
CORPUS_DIR = LOG_DIR / "_yadam_corpus"

# 어휘 stopword (의미 없는 흔한 단어)
STOP = {"것이", "그러", "그래서", "그리고", "그러나", "하지만", "그런데", "그렇게", "이렇게",
        "그러면", "그러나", "이러", "저러", "어떤", "그것", "이것", "저것", "여기", "거기",
        "그날", "오늘", "어제", "이날", "다음", "그때", "당시", "정말", "진짜", "마지막",
        "사이", "이후", "결국", "단번"}


def text_in_range(segments: list, start_sec: float, end_sec: float) -> str:
    """주어진 시간 구간의 자막 텍스트 합치기."""
    out = []
    for s in segments:
        if s["start"] >= end_sec:
            break
        if s["end"] < start_sec:
            continue
        out.append(s["text"])
    return " ".join(out)


def first_sentence(text: str) -> str:
    """대략적인 첫 문장 추출 (마침표·물음표·느낌표 기준)."""
    text = text.strip()
    if not text:
        return ""
    m = re.search(r"[^\.\?\!。\n]{5,120}[\.\?\!。]", text)
    if m:
        return m.group(0).strip()
    return text[:80]


def extract_words(text: str) -> list:
    """한글 2글자+ 단어만 추출 (stopword 제외)."""
    words = re.findall(r"[가-힣]{2,}", text)
    return [w for w in words if w not in STOP and len(w) >= 2]


# Hook 패턴 분류 — 0~30초 첫 문장 키워드 기반
HOOK_PATTERNS = {
    "충격사건형": ["갑자기", "충격", "그날", "그밤", "어느날", "쓰러졌", "돌아가셨", "죽었", "사라졌", "벌어졌",
                  "쫓겨", "나가거라", "죽이", "당했", "내쫓", "끊어", "터졌"],
    "질문형": ["혹시", "왜", "어떻게", "무엇이", "당신은", "여러분", "아십니까", "들어보셨"],
    "회상형": ["기억", "그때", "옛날", "예전", "추억", "있었습니다", "있었지요", "옛적", "지난날"],
    "통계형": ["퍼센트", "%", "백명", "천명", "만명", "조사", "통계", "연구", "발표"],
    "대비형": ["하지만", "그러나", "오히려", "도리어", "반대로", "그런데"],
    "약속형": ["오늘 이야기", "이번에는", "지금부터", "오늘은", "이 이야기"],
}

# 첫 사건 (행동/이벤트) 발생 키워드 — 첫 3분 안에서 검출
EVENT_KEYWORDS = ["어느날", "그날", "그밤", "갑자기", "쓰러졌", "돌아가셨", "죽었", "사라졌",
                  "벌어졌", "왔습니다", "왔지요", "들어왔", "나타났", "달려왔", "들이닥",
                  "터졌", "쫓겨", "베어", "잡혔", "맞붙", "외쳤", "소리쳤", "쓰러"]


def classify_hook(text: str) -> tuple[str, dict]:
    """Hook 첫 문장 → 패턴 분류 + 매칭 키워드."""
    if not text:
        return "기타", {}
    head = text[:200]
    matches = {}
    for pat, words in HOOK_PATTERNS.items():
        hits = [w for w in words if w in head]
        if hits:
            matches[pat] = hits
    if not matches:
        return "기타", {}
    dominant = max(matches.items(), key=lambda x: len(x[1]))[0]
    return dominant, matches


def detect_first_event(segments: list, limit_sec: float = 180) -> dict:
    """0~180초 안에서 첫 사건 키워드 등장 시점."""
    for s in segments:
        if s["start"] >= limit_sec:
            break
        for kw in EVENT_KEYWORDS:
            if kw in s["text"]:
                return {"at_sec": round(s["start"], 1), "keyword": kw, "snippet": s["text"][:120]}
    return {"at_sec": None, "keyword": "", "snippet": ""}


def emotion_signals(text: str) -> dict:
    """Hook 감정 강도 지표."""
    if not text:
        return {"exclaim": 0, "question": 0, "emphasis_words": 0, "intensity": 0.0}
    excl = text.count("!") + text.count("！")
    quest = text.count("?") + text.count("？")
    emphasis_terms = ["정말", "진짜", "절대", "완전", "전혀", "결코", "꼭", "반드시", "도무지"]
    emph = sum(1 for w in emphasis_terms if w in text)
    intensity = round((excl * 1.0 + quest * 0.7 + emph * 0.6) / max(1, len(text) / 100), 2)
    return {"exclaim": excl, "question": quest, "emphasis_words": emph, "intensity": intensity}


def analyze_one(record: dict) -> dict:
    """한 영상의 구조 분석. Hook을 0-3, 3-10, 10-30으로 세분화 + 첫 사건 시점."""
    segs = record.get("segments", [])
    if not segs:
        return {}
    duration = record.get("duration_sec", 0) or (segs[-1]["end"] if segs else 0)
    if duration < 60:
        return {"video_id": record["video_id"], "title": record.get("title", ""),
                "duration_sec": duration, "skipped": "too_short"}

    # Hook 세분화: 0-3 (pre-hook) / 3-10 (core) / 10-30 (promise)
    pre_hook = text_in_range(segs, 0, 3)
    hook_core = text_in_range(segs, 3, 10)
    hook_promise = text_in_range(segs, 10, 30)
    hook_all = text_in_range(segs, 0, 30)

    # 첫 3분 세분화: setup (30-90), first_plot (90-180)
    setup = text_in_range(segs, 30, 90)
    first_plot = text_in_range(segs, 90, 180)
    intro = text_in_range(segs, 30, 180)

    mid_start = duration * 0.4
    mid_end = duration * 0.7
    body_climax = text_in_range(segs, mid_start, mid_end)
    outro = text_in_range(segs, max(0, duration - 60), duration)

    full_text = " ".join(s["text"] for s in segs)
    words = extract_words(full_text)
    word_count = len(words)
    wpm = round(word_count / (duration / 60), 1) if duration > 0 else 0

    # Hook 패턴 분류 + 매칭 키워드
    hook_pattern, hook_matches = classify_hook(hook_all)
    # 첫 사건 발생 시점 (0~180s 안에서)
    first_event = detect_first_event(segs, 180)
    # Hook 감정 강도
    emotion = emotion_signals(hook_all)

    # Hook 발화 속도 vs 본문 속도 비교
    hook_words = len(extract_words(hook_all))
    hook_wpm = round(hook_words / 0.5, 1) if hook_words else 0  # 30초 = 0.5분
    body_words = word_count - hook_words - len(extract_words(intro))
    body_dur_min = max(0.1, (duration - 180) / 60)
    body_wpm = round(body_words / body_dur_min, 1) if body_words else 0

    return {
        "video_id": record["video_id"],
        "title": record.get("title", ""),
        "auto": record.get("auto", False),
        "duration_sec": int(duration),
        "duration_min": round(duration / 60, 1),
        "total_words": word_count,
        "wpm": wpm,
        "hook": {
            "text": hook_all[:600],
            "first_sentence": first_sentence(hook_all),
            "char_count": len(hook_all),
            "pattern": hook_pattern,
            "pattern_matches": hook_matches,
            "wpm": hook_wpm,
            "body_wpm": body_wpm,
            "wpm_diff": round(hook_wpm - body_wpm, 1),  # +면 Hook이 더 빠름
            "emotion": emotion,
            # 세분화
            "pre_hook_0_3s": {"text": pre_hook[:200], "char_count": len(pre_hook)},
            "core_3_10s": {"text": hook_core[:300], "char_count": len(hook_core)},
            "promise_10_30s": {"text": hook_promise[:400], "char_count": len(hook_promise)},
        },
        "first_event": first_event,  # 첫 사건 발생 시점
        "intro": {
            "text": intro[:800], "char_count": len(intro),
            "setup_30_90s": setup[:400],
            "first_plot_90_180s": first_plot[:400],
        },
        "climax": {"text": body_climax[:800], "char_count": len(body_climax)},
        "outro": {
            "text": outro[:600],
            "last_sentence": first_sentence(outro[::-1])[::-1] if outro else "",
            "char_count": len(outro),
        },
        "top_words": Counter(words).most_common(15),
    }


def main():
    if not CORPUS_DIR.exists():
        print(f"❌ {CORPUS_DIR} 없음 — transcribe_yadam.py 먼저 실행")
        return
    corpus_files = sorted(CORPUS_DIR.glob("*.json"))
    corpus_files = [p for p in corpus_files if not p.name.startswith("_")]
    if not corpus_files:
        print("❌ corpus 비어 있음")
        return
    print(f"📂 corpus {len(corpus_files)}편 분석\n")

    per_video, hook_pool, closing_pool, all_words = [], [], [], Counter()
    durations, wpms = [], []
    for p in corpus_files:
        try:
            rec = json.loads(p.read_text())
        except Exception:
            continue
        analysis = analyze_one(rec)
        if not analysis or analysis.get("skipped"):
            continue
        per_video.append(analysis)
        if analysis["hook"]["first_sentence"]:
            hook_pool.append({
                "video_id": analysis["video_id"],
                "title": analysis["title"][:60],
                "sentence": analysis["hook"]["first_sentence"],
                "full_30s": analysis["hook"]["text"][:200],
            })
        if analysis["outro"].get("last_sentence"):
            closing_pool.append({
                "video_id": analysis["video_id"],
                "title": analysis["title"][:60],
                "sentence": analysis["outro"]["last_sentence"],
                "full_60s": analysis["outro"]["text"][:200],
            })
        for w, n in analysis["top_words"]:
            all_words[w] += n
        durations.append(analysis["duration_min"])
        wpms.append(analysis["wpm"])

    # 표준 구조 템플릿 (평균 기반)
    if durations:
        avg_dur = sum(durations) / len(durations)
        avg_wpm = sum(wpms) / len(wpms) if wpms else 0
        template = {
            "avg_duration_min": round(avg_dur, 1),
            "median_duration_min": round(sorted(durations)[len(durations) // 2], 1),
            "avg_wpm": round(avg_wpm, 1),
            "estimated_word_count": int(avg_dur * avg_wpm),
            "structure": [
                {"phase": "Hook", "start_sec": 0, "end_sec": 30, "note": "충격 사건 + 시점 환기"},
                {"phase": "Intro", "start_sec": 30, "end_sec": 180, "note": "인물·배경·시대 소개"},
                {"phase": "Body", "start_sec": 180, "end_sec": int(avg_dur * 60 * 0.4),
                 "note": "갈등 전개·증폭"},
                {"phase": "Climax", "start_sec": int(avg_dur * 60 * 0.4),
                 "end_sec": int(avg_dur * 60 * 0.7), "note": "절정·반전"},
                {"phase": "Resolution", "start_sec": int(avg_dur * 60 * 0.7),
                 "end_sec": int(avg_dur * 60) - 60, "note": "결말·권선징악"},
                {"phase": "Outro", "start_sec": int(avg_dur * 60) - 60,
                 "end_sec": int(avg_dur * 60), "note": "여운·시그니처"},
            ],
        }
    else:
        template = {}

    out = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "corpus_size": len(per_video),
        "structure_template": template,
        "vocab_signature": [{"word": w, "n": n} for w, n in all_words.most_common(30) if n >= 3],
        "hook_pool": hook_pool,
        "closing_pool": closing_pool,
        "per_video": per_video,
    }
    path = LOG_DIR / f"senior_structure_{datetime.now():%Y-%m-%d}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 분석 완료 {len(per_video)}편 → {path.name}")
    if template:
        print(f"   평균 분량 {template['avg_duration_min']}분 · 평균 발화 {template['avg_wpm']}wpm")
        print(f"   대본 권장 분량 ≈ {template['estimated_word_count']:,}단어")
    print(f"   Hook 풀 {len(hook_pool)}개 · 결말 풀 {len(closing_pool)}개 · 어휘 시그너처 상위 10:")
    for w, n in all_words.most_common(10):
        print(f"     {w} ×{n}")


if __name__ == "__main__":
    main()
