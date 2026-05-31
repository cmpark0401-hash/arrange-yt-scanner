"""왜 이 영상은 터졌는가? — 사용자가 던진 URL N편 자막 corpus 분해 + 비교 분석.

흐름:
1. URL 파싱 (--url 또는 stdin)
2. 자막 다운로드 (transcribe_yadam.fetch_subtitle 재사용)
3. 영상별 구조 분해 (analyze_yadam_structure.analyze_one 재사용)
4. N편 공통 패턴 추출
5. result.json + result.md 저장 + 인덱스 갱신

산출:
  channels/_autopsy/{slug}/
  ├── result.json
  ├── result.md
  └── transcripts/{vid}.json
  channels/_autopsy/_index.json (전체 분석 카드 목록)
"""
import argparse
import json
import re
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from transcribe_yadam import fetch_subtitle  # 자막 다운로드 + dedup
from analyze_yadam_structure import analyze_one, STOP  # 구조 분해 + stopword

AUTOPSY_DIR = ROOT / "channels" / "_autopsy"
AUTOPSY_DIR.mkdir(parents=True, exist_ok=True)


def slugify(text: str, max_len: int = 50) -> str:
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"[^\w가-힣\-]+", "", text)
    return text[:max_len].strip("-") or "untitled"


def extract_video_id(url: str) -> str:
    """YouTube URL에서 video ID 추출."""
    m = re.search(r"(?:v=|youtu\.be/|/embed/|/shorts/)([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else url[:11]


def fetch_video_title(vid: str) -> str:
    import subprocess
    yt = str(ROOT / ".venv" / "bin" / "yt-dlp")
    try:
        r = subprocess.run([yt, f"https://www.youtube.com/watch?v={vid}", "--skip-download",
                            "--print", "%(title)s", "--no-warnings",
                            "--extractor-args", "youtube:player_client=web,android,ios"],
                           capture_output=True, text=True, timeout=40)
        return r.stdout.strip()
    except subprocess.TimeoutExpired:
        return ""


def classify_hook_pattern(text: str) -> str:
    """Hook 30s 첫 문장을 패턴으로 분류."""
    if not text:
        return "기타"
    triggers = {
        "충격사건형": ["갑자기", "충격", "그날", "그밤", "어느날", "쓰러졌", "돌아가셨", "죽었", "사라졌", "벌어졌"],
        "질문형": ["혹시", "왜", "어떻게", "무엇이", "당신은", "여러분"],
        "회상형": ["기억", "그때", "옛날", "예전", "추억"],
        "통계형": ["퍼센트", "%", "백명", "천명", "만명", "조사", "통계", "연구"],
        "대비형": ["하지만", "그러나", "오히려", "도리어", "반대로"],
        "직격형": ["오늘은", "지금", "바로", "이제"],
    }
    head = text[:120]
    for pat, words in triggers.items():
        if any(w in head for w in words):
            return pat
    return "기타"


def classify_outro_pattern(text: str) -> str:
    """Outro 마지막 60s를 패턴으로 분류."""
    if not text:
        return "기타"
    triggers = {
        "교훈형": ["입니다", "법입니다", "법이지요", "법이라", "교훈", "배웠", "깨달았"],
        "여운형": ["그렇게", "그저", "남았", "잊지", "기억", "마음에"],
        "요약형": ["다시", "정리하면", "결국은", "한 마디로"],
        "시그니처형": ["구독", "좋아요", "다음 영상", "감사합니다", "댓글", "알림"],
    }
    tail = text[-200:]
    for pat, words in triggers.items():
        if any(w in tail for w in words):
            return pat
    return "기타"


def common_patterns(analyses: list) -> dict:
    """N편 분석 결과 → 공통 패턴 + 차이점."""
    if not analyses:
        return {}
    durations = [a["duration_min"] for a in analyses if a.get("duration_min")]
    wpms = [a["wpm"] for a in analyses if a.get("wpm")]

    # 어휘 교집합 + 빈도 합
    word_sets = []
    all_words = Counter()
    for a in analyses:
        ws = {w: n for w, n in a.get("top_words", [])}
        word_sets.append(set(ws.keys()))
        for w, n in ws.items():
            all_words[w] += n
    common_words = set.intersection(*word_sets) if word_sets else set()
    common_top = [(w, all_words[w]) for w in common_words]
    common_top.sort(key=lambda x: -x[1])

    # Hook·Outro 유형 분류 비율
    hook_types = Counter(classify_hook_pattern(a.get("hook", {}).get("text", "")) for a in analyses)
    outro_types = Counter(classify_outro_pattern(a.get("outro", {}).get("text", "")) for a in analyses)

    return {
        "n_videos": len(analyses),
        "avg_duration_min": round(sum(durations) / len(durations), 1) if durations else 0,
        "median_duration_min": round(sorted(durations)[len(durations) // 2], 1) if durations else 0,
        "duration_range": [min(durations), max(durations)] if durations else [0, 0],
        "avg_wpm": round(sum(wpms) / len(wpms), 1) if wpms else 0,
        "common_words_top": common_top[:20],
        "all_words_top": all_words.most_common(25),
        "hook_types": dict(hook_types),
        "outro_types": dict(outro_types),
        "hook_dominant": hook_types.most_common(1)[0][0] if hook_types else "기타",
        "outro_dominant": outro_types.most_common(1)[0][0] if outro_types else "기타",
    }


def render_md(meta: dict, analyses: list, patterns: dict) -> str:
    lines = [
        f"# 🔥 왜 이 영상은 터졌는가? — {meta['label']}",
        "",
        f"_{meta['date']} · 영상 {len(analyses)}편 분석 · 태그: {', '.join(meta.get('tags',[])) or '—'}_",
        "",
    ]

    # 공통 패턴 (주인공)
    if patterns:
        lines += [
            "## 🎯 공통 패턴 (핵심 인사이트)",
            "",
            f"- **공통 후크 유형**: {patterns['hook_dominant']} ({patterns['hook_types']})",
            f"- **공통 결말 톤**: {patterns['outro_dominant']} ({patterns['outro_types']})",
            f"- **평균 분량**: {patterns['avg_duration_min']}분 (중앙 {patterns['median_duration_min']} · 범위 {patterns['duration_range'][0]:.1f}~{patterns['duration_range'][1]:.1f})",
            f"- **평균 발화 속도**: {patterns['avg_wpm']} 단어/분",
            "",
        ]
        cw = patterns.get("common_words_top", [])
        if cw:
            lines += [
                "### 📚 N편 공통 어휘 (교집합)",
                "",
                ", ".join(f"`{w}` ×{n}" for w, n in cw[:15]),
                "",
            ]
        aw = patterns.get("all_words_top", [])
        if aw:
            lines += [
                "### 📊 전체 빈출 어휘 합산",
                "",
                ", ".join(f"`{w}` ×{n}" for w, n in aw[:20]),
                "",
            ]

    # 영상별 분해
    lines += ["---", "", "## 🎬 영상별 분해", ""]
    for i, a in enumerate(analyses, 1):
        lines += [
            f"### {i}. {a['title'][:80]}",
            "",
            f"- YouTube: https://youtube.com/watch?v={a['video_id']}",
            f"- 분량: **{a['duration_min']}분** · 발화: **{a['wpm']} 단어/분** · 단어 {a['total_words']:,}",
            f"- 자막 종류: {'자동' if a.get('auto') else '수동'}",
            "",
            "**🪝 Hook (0~30s)** — `" + classify_hook_pattern(a["hook"]["text"]) + "`",
            "```",
            a["hook"]["text"][:600].strip() or "(텍스트 없음)",
            "```",
            "",
            "**📖 Intro (30~180s)**",
            "```",
            a["intro"]["text"][:800].strip() or "(텍스트 없음)",
            "```",
            "",
            "**🔥 Climax (40~70%)**",
            "```",
            a["climax"]["text"][:1200].strip() or "(텍스트 없음)",
            "```",
            "",
            "**🎯 Outro (마지막 60s)** — `" + classify_outro_pattern(a["outro"]["text"]) + "`",
            "```",
            a["outro"]["text"][:600].strip() or "(텍스트 없음)",
            "```",
            "",
            "**📚 빈출 어휘**: " + ", ".join(f"`{w}` ×{n}" for w, n in a.get("top_words", [])[:10]),
            "",
            "---",
            "",
        ]

    return "\n".join(lines)


def update_index(slug: str, meta: dict, patterns: dict):
    idx_path = AUTOPSY_DIR / "_index.json"
    idx = {"items": []}
    if idx_path.exists():
        try:
            idx = json.loads(idx_path.read_text())
        except Exception:
            pass
    # 같은 slug 있으면 업데이트, 없으면 추가
    items = [it for it in idx.get("items", []) if it["slug"] != slug]
    items.insert(0, {
        "slug": slug,
        "label": meta["label"],
        "date": meta["date"],
        "tags": meta.get("tags", []),
        "n_videos": meta["n_videos"],
        "hook_dominant": patterns.get("hook_dominant", "—"),
        "outro_dominant": patterns.get("outro_dominant", "—"),
        "avg_duration_min": patterns.get("avg_duration_min", 0),
        "common_words_top5": [w for w, n in patterns.get("common_words_top", [])[:5]],
    })
    idx_path.write_text(json.dumps({"items": items}, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="왜 이 영상은 터졌는가? — N편 영상 자막 분해 + 비교 분석")
    ap.add_argument("urls", nargs="*", help="YouTube URL들 (공백 구분)")
    ap.add_argument("--label", default="", help="이 분석에 붙일 라벨 (예: '잘듣네 신작 비교')")
    ap.add_argument("--tags", default="", help="태그 (콤마 구분)")
    ap.add_argument("--slug", default="", help="slug 직접 지정 (없으면 라벨 + 날짜로 자동)")
    args = ap.parse_args()

    urls = [u.strip() for u in args.urls if u.strip()]
    if not urls:
        print("❌ URL이 없습니다. 예: .venv/bin/python scripts/autopsy.py URL1 URL2 --label '...'")
        sys.exit(1)

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    label = args.label or f"분석 {date} {len(urls)}편"
    slug = args.slug or f"{date}-{slugify(label)}"
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    work_dir = AUTOPSY_DIR / slug
    work_dir.mkdir(parents=True, exist_ok=True)
    tr_dir = work_dir / "transcripts"
    tr_dir.mkdir(exist_ok=True)

    print(f"\n🔥 autopsy: {label} ({slug})")
    print(f"📥 {len(urls)}개 영상 자막 다운로드 + 분석\n")

    analyses = []
    failed = []
    for i, url in enumerate(urls, 1):
        vid = extract_video_id(url)
        print(f"  [{i:2}/{len(urls)}] {vid}", flush=True)
        title = fetch_video_title(vid)
        record = fetch_subtitle(vid)
        if not record or not record.get("segments"):
            print(f"          ❌ 자막 없음")
            failed.append({"url": url, "video_id": vid, "title": title, "reason": "자막 없음"})
            time.sleep(1)
            continue
        record["title"] = title
        record["url"] = url
        # 자막 저장
        (tr_dir / f"{vid}.json").write_text(
            json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        # 구조 분해
        analysis = analyze_one(record)
        if not analysis or analysis.get("skipped"):
            print(f"          ⏭️  너무 짧음")
            failed.append({"url": url, "video_id": vid, "title": title, "reason": "<60s"})
            time.sleep(1)
            continue
        analysis["title"] = title
        analyses.append(analysis)
        print(f"          ✅ {analysis['duration_min']}분 · {analysis['wpm']}wpm · {len(record['segments'])}세그")
        time.sleep(0.5)

    if not analyses:
        print("\n❌ 분석 가능한 영상이 없습니다. 다른 URL로 재시도하세요.")
        sys.exit(1)

    # 공통 패턴 추출
    patterns = common_patterns(analyses)

    # 태그 자동 추출 (지정 없을 때): 공통 어휘 상위 5개
    if not tags:
        tags = [w for w, _ in patterns.get("common_words_top", [])[:5]]

    meta = {
        "slug": slug, "label": label, "date": date, "tags": tags,
        "n_videos": len(analyses), "n_failed": len(failed),
        "generated_at": now.strftime("%Y-%m-%d %H:%M"),
    }

    # 저장
    (work_dir / "result.json").write_text(json.dumps({
        "meta": meta, "patterns": patterns, "analyses": analyses, "failed": failed,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    (work_dir / "result.md").write_text(render_md(meta, analyses, patterns), encoding="utf-8")
    update_index(slug, meta, patterns)

    # 사용자 출력
    print(f"\n✅ 분석 완료 — {label} ({len(analyses)}편 성공, {len(failed)} 실패)")
    print(f"   🪝 공통 후크 유형: {patterns['hook_dominant']} ({patterns['hook_types']})")
    print(f"   🎯 공통 결말 톤: {patterns['outro_dominant']} ({patterns['outro_types']})")
    print(f"   ⏱️  평균 분량: {patterns['avg_duration_min']}분 · 발화 {patterns['avg_wpm']}wpm")
    if patterns.get("common_words_top"):
        cw = ", ".join(f"{w}×{n}" for w, n in patterns["common_words_top"][:5])
        print(f"   📚 공통 어휘 TOP5: {cw}")
    print(f"\n📂 {work_dir}")
    print(f"📄 result.md · 📊 result.json")


if __name__ == "__main__":
    main()
