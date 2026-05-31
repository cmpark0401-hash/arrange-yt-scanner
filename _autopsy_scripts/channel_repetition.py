"""채널 내 N편 자막의 중복도 분석.

같은 채널이 영상마다 똑같은 표현·후크·시그너처 멘트를 반복하면 시청자 거부감이 큼.
정량 지표:
1. N-gram 매치율 — 영상 A의 3-gram 중 채널 다른 영상에 등장한 비율
2. Hook 첫 문장 유사도 — Jaccard 또는 cosine
3. 시그너처 멘트 빈도 — 영상당 평균 등장 횟수
4. 어휘 갱신율 — 새 영상에서 신규 어휘 비율
5. 단조도 점수 — 0~100 (낮을수록 다양)

사용:
  .venv/bin/python scripts/channel_repetition.py --channel "조선야담처녀"
  .venv/bin/python scripts/channel_repetition.py --corpus channels/_shared_corpus/yadam/transcripts/
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "channels" / "knowledge-archive" / "_monitor_logs"

STOP = {"것이", "그러", "그래서", "그리고", "그러나", "하지만", "그런데", "그렇게", "이렇게",
        "그러면", "이러", "저러", "어떤", "그것", "이것", "저것", "여기", "거기",
        "그날", "오늘", "어제", "이날", "다음", "그때", "당시", "정말", "진짜"}


def ngrams(text: str, n: int = 3) -> set:
    """한글 단어 n-gram set."""
    words = [w for w in re.findall(r"[가-힣]{2,}", text) if w not in STOP]
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return round(inter / union, 4) if union else 0.0


def vocab(text: str) -> set:
    return {w for w in re.findall(r"[가-힣]{2,}", text) if w not in STOP and len(w) >= 2}


def load_corpus(corpus_dir: Path, channel_filter: str = "") -> list:
    """corpus 디렉토리의 영상별 자막 JSON 로드. 채널 필터 가능."""
    out = []
    for p in sorted(corpus_dir.glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            rec = json.loads(p.read_text())
        except Exception:
            continue
        title = rec.get("title", "")
        ch = rec.get("channel", "") or rec.get("source", "")
        if channel_filter and channel_filter not in title and channel_filter not in ch:
            continue
        text = " ".join(s.get("text", "") for s in rec.get("segments", []))
        out.append({
            "video_id": rec.get("video_id", p.stem),
            "title": title, "text": text,
            "duration_sec": rec.get("duration_sec", 0),
            "hook_text": _hook_text(rec.get("segments", [])),
        })
    return out


def _hook_text(segs: list) -> str:
    out = []
    for s in segs:
        if s.get("start", 0) >= 30:
            break
        out.append(s.get("text", ""))
    return " ".join(out)


def analyze_channel(videos: list, signature_terms: list) -> dict:
    """채널 N편 → 중복도 종합."""
    if len(videos) < 2:
        return {"warning": "최소 2편 이상 필요"}

    # 1. 영상별 3-gram·4-gram
    grams3 = {v["video_id"]: ngrams(v["text"], 3) for v in videos}
    grams4 = {v["video_id"]: ngrams(v["text"], 4) for v in videos}
    vocabs = {v["video_id"]: vocab(v["text"]) for v in videos}
    hook_grams = {v["video_id"]: ngrams(v["hook_text"], 2) for v in videos}

    # 2. 영상간 pairwise Jaccard
    pairs_3gram, pairs_4gram, pairs_hook, pairs_vocab = [], [], [], []
    ids = [v["video_id"] for v in videos]
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            pairs_3gram.append({"a": a, "b": b, "jaccard": jaccard(grams3[a], grams3[b])})
            pairs_4gram.append({"a": a, "b": b, "jaccard": jaccard(grams4[a], grams4[b])})
            pairs_hook.append({"a": a, "b": b, "jaccard": jaccard(hook_grams[a], hook_grams[b])})
            pairs_vocab.append({"a": a, "b": b, "jaccard": jaccard(vocabs[a], vocabs[b])})

    avg = lambda L: round(sum(p["jaccard"] for p in L) / len(L), 4) if L else 0.0

    # 3. 시그너처 표현 빈도 (영상당 평균 등장 횟수)
    sig_per_video = defaultdict(list)
    for v in videos:
        for term in signature_terms:
            cnt = v["text"].count(term)
            sig_per_video[term].append(cnt)
    sig_stats = [{"term": t, "avg_per_video": round(sum(cs) / len(cs), 1),
                  "max": max(cs), "videos_with": sum(1 for c in cs if c > 0)}
                 for t, cs in sig_per_video.items()]
    sig_stats.sort(key=lambda x: -x["avg_per_video"])

    # 4. 어휘 갱신율 — 시간순으로 봤을 때 새 영상이 얼마나 신규 어휘를 가져오나
    cumulative = set()
    refresh_rates = []
    for v in videos:
        v_vocab = vocabs[v["video_id"]]
        new = v_vocab - cumulative
        refresh = round(len(new) / max(1, len(v_vocab)), 3) if v_vocab else 0
        refresh_rates.append({"video_id": v["video_id"], "title": v["title"][:50],
                              "new_vocab": len(new), "total_vocab": len(v_vocab), "refresh_rate": refresh})
        cumulative |= v_vocab

    # 5. 단조도 점수 (0~100, 낮을수록 다양)
    # 종합: 3-gram avg × 100 (0.0=완전 다양, 1.0=완전 동일)
    monotony = round(avg(pairs_3gram) * 100, 1)
    if monotony >= 30:
        verdict = "🔴 매우 반복적 (시청자 거부감 위험)"
    elif monotony >= 20:
        verdict = "🟠 반복 신호 — 다음 영상은 어휘 갱신 필요"
    elif monotony >= 10:
        verdict = "🟡 적당한 일관성"
    else:
        verdict = "🟢 다양성 양호"

    return {
        "n_videos": len(videos),
        "avg_jaccard_3gram": avg(pairs_3gram),
        "avg_jaccard_4gram": avg(pairs_4gram),
        "avg_jaccard_hook_2gram": avg(pairs_hook),
        "avg_jaccard_vocab": avg(pairs_vocab),
        "monotony_score": monotony,
        "verdict": verdict,
        "signature_stats": sig_stats[:15],
        "vocab_refresh": refresh_rates,
        "top_pairs_3gram": sorted(pairs_3gram, key=lambda x: -x["jaccard"])[:5],
        "top_pairs_hook": sorted(pairs_hook, key=lambda x: -x["jaccard"])[:5],
    }


# 야담 기본 시그너처 (시니어랩 데이터에서 검증된 표현)
DEFAULT_SIGNATURE_TERMS = [
    "있었습니다", "있었지요", "있었어요", "그랬지요",
    "권선징악", "조선판사이다", "옛날이야기",
    "박씨", "정인", "사또", "양반", "오랑캐", "호랑이",
    "어머니의", "아버지의", "그렇게", "이윽고",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default=str(ROOT / "channels" / "_shared_corpus" / "yadam" / "transcripts"),
                    help="corpus 디렉토리 (자막 JSON 모음)")
    ap.add_argument("--channel", default="", help="특정 채널만 필터 (제목/채널명 substring)")
    ap.add_argument("--signature", default=",".join(DEFAULT_SIGNATURE_TERMS),
                    help="시그너처 표현 (콤마구분)")
    ap.add_argument("--output", default="", help="결과 JSON 저장 경로 (없으면 stdout)")
    args = ap.parse_args()

    corpus_dir = Path(args.corpus)
    if not corpus_dir.exists():
        print(f"❌ {corpus_dir} 없음"); sys.exit(1)

    videos = load_corpus(corpus_dir, args.channel)
    label = args.channel or "전체"
    print(f"📂 {label} — corpus {len(videos)}편 로드\n")
    if len(videos) < 2:
        print("⚠️ 최소 2편 이상 필요"); sys.exit(0)

    sig_terms = [t.strip() for t in args.signature.split(",") if t.strip()]
    result = analyze_channel(videos, sig_terms)
    result["channel"] = label
    result["generated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"🔍 결과:")
    print(f"   영상간 평균 3-gram Jaccard:   {result['avg_jaccard_3gram']:.3f}")
    print(f"   영상간 평균 4-gram Jaccard:   {result['avg_jaccard_4gram']:.3f}")
    print(f"   Hook 2-gram Jaccard:          {result['avg_jaccard_hook_2gram']:.3f}")
    print(f"   어휘 set Jaccard:             {result['avg_jaccard_vocab']:.3f}")
    print(f"   단조도 점수:                    {result['monotony_score']}/100")
    print(f"   판정:                          {result['verdict']}")
    print(f"\n📚 시그너처 표현 TOP10 (영상당 평균):")
    for s in result["signature_stats"][:10]:
        print(f"   {s['term']:14}  평균 {s['avg_per_video']:>5.1f}회  최대 {s['max']:>3}  ({s['videos_with']}/{result['n_videos']}편)")

    out_path = Path(args.output) if args.output else (LOG_DIR / f"channel_repetition_{datetime.now():%Y-%m-%d}.json")
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n✅ → {out_path.name}")


if __name__ == "__main__":
    main()
