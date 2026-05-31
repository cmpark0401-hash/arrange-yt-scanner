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
try:
    from channel_repetition import ngrams, jaccard, vocab as _vocab_set
except ImportError:
    ngrams = jaccard = _vocab_set = None

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


def fetch_video_meta(vid: str) -> dict:
    """영상 메타: title, channel, subscribers, views, upload_date, duration. 시간 효율 계산 재료."""
    import subprocess
    venv_yt = ROOT / ".venv" / "bin" / "yt-dlp"
    yt = str(venv_yt) if venv_yt.exists() else "yt-dlp"
    fields = "%(title)s|||%(channel)s|||%(channel_follower_count)s|||%(view_count)s|||%(upload_date)s|||%(duration)s|||%(like_count)s|||%(comment_count)s"
    try:
        r = subprocess.run([yt, f"https://www.youtube.com/watch?v={vid}", "--skip-download",
                            "--print", fields, "--no-warnings",
                            "--extractor-args", "youtube:player_client=web,android,ios"],
                           capture_output=True, text=True, timeout=60)
        parts = (r.stdout or "").strip().split("|||")
        if len(parts) >= 6:
            def to_int(s):
                try: return int(s) if s and s != "NA" else 0
                except: return 0
            return {
                "title": parts[0],
                "channel": parts[1] if parts[1] != "NA" else "",
                "subscribers": to_int(parts[2]),
                "views": to_int(parts[3]),
                "upload_date": parts[4] if len(parts[4]) == 8 else "",
                "duration_sec": to_int(parts[5]),
                "likes": to_int(parts[6]) if len(parts) > 6 else 0,
                "comments": to_int(parts[7]) if len(parts) > 7 else 0,
            }
    except subprocess.TimeoutExpired:
        pass
    return {}


def compute_time_efficiency(meta: dict) -> dict:
    """발행 시점부터 시간 경과별 효율 추정."""
    if not meta.get("upload_date") or len(meta["upload_date"]) != 8:
        return {}
    from datetime import datetime as _dt
    try:
        up = _dt.strptime(meta["upload_date"], "%Y%m%d")
    except ValueError:
        return {}
    now = _dt.now()
    hours_since = max(1, (now - up).total_seconds() / 3600)
    days_since = round(hours_since / 24, 1)
    views = meta.get("views", 0)
    subs = meta.get("subscribers", 0)
    velocity_per_hour = round(views / hours_since, 1)
    efficiency = round(views / subs, 3) if subs > 0 else 0
    # 효율 등급
    if efficiency >= 2.0:
        tier = "🚀 메가폭발 (efficiency 2배+)"
    elif efficiency >= 1.0:
        tier = "🔥 폭발 (구독 초과)"
    elif efficiency >= 0.3:
        tier = "📈 양호"
    elif efficiency >= 0.1:
        tier = "🟡 평범"
    else:
        tier = "❄️ 저조"
    # 시청자 반응 비율
    like_ratio = round(meta.get("likes", 0) / views, 4) if views else 0
    comment_ratio = round(meta.get("comments", 0) / views, 4) if views else 0
    return {
        "hours_since_upload": round(hours_since, 1),
        "days_since_upload": days_since,
        "views": views, "subscribers": subs,
        "efficiency": efficiency,  # views / subs
        "velocity_per_hour": velocity_per_hour,
        "tier": tier,
        "like_ratio": like_ratio,
        "comment_ratio": comment_ratio,
        "likes": meta.get("likes", 0),
        "comments": meta.get("comments", 0),
    }


def fetch_comments(vid: str, max_count: int = 80) -> list:
    """yt-dlp로 댓글 텍스트 가져오기 (top 댓글 위주)."""
    import subprocess, json as _json
    venv_yt = ROOT / ".venv" / "bin" / "yt-dlp"
    yt = str(venv_yt) if venv_yt.exists() else "yt-dlp"
    try:
        r = subprocess.run([yt, f"https://www.youtube.com/watch?v={vid}",
                            "--skip-download", "--write-comments",
                            "--extractor-args", f"youtube:comment_sort=top;max_comments={max_count},0,0,0",
                            "--print-json", "--no-warnings", "-q"],
                           capture_output=True, text=True, timeout=120)
        if not r.stdout:
            return []
        for line in r.stdout.strip().split("\n"):
            try:
                obj = _json.loads(line)
                cs = obj.get("comments", [])
                return [c.get("text", "") for c in cs if c.get("text")]
            except Exception:
                continue
    except subprocess.TimeoutExpired:
        return []
    return []


def extract_timestamps(comments: list) -> dict:
    """댓글에서 timestamp 패턴 (1:23, 1:23:45) 추출 + 시점별 빈도."""
    pat = re.compile(r"\b(\d{1,2}):(\d{2})(?::(\d{2}))?\b")
    counter = Counter()
    examples = {}
    for c in comments:
        for m in pat.finditer(c):
            h = int(m.group(3) and m.group(1) or 0)
            mm = int(m.group(3) and m.group(2) or m.group(1))
            ss = int(m.group(3) or m.group(2))
            total = h * 3600 + mm * 60 + ss
            if total < 5 or total > 7200:  # 5초~2시간 범위
                continue
            counter[total] += 1
            # 첫 등장 댓글 스니펫 저장
            if total not in examples:
                snippet = c.replace("\n", " ").strip()[:140]
                examples[total] = snippet
    # 가장 많이 언급된 시점 TOP
    top = []
    for sec, cnt in counter.most_common(15):
        top.append({"sec": sec, "mmss": f"{sec//60}:{sec%60:02d}",
                    "mentions": cnt, "example": examples.get(sec, "")})
    # 시점 구간별 분포 (0-30s, 30-180s, 180s-end)
    bucket = {"0-30s": 0, "30-180s": 0, "3-10m": 0, "10m+": 0}
    for sec, cnt in counter.items():
        if sec < 30: bucket["0-30s"] += cnt
        elif sec < 180: bucket["30-180s"] += cnt
        elif sec < 600: bucket["3-10m"] += cnt
        else: bucket["10m+"] += cnt
    return {
        "total_timestamps": sum(counter.values()),
        "unique_seconds": len(counter),
        "top_mentions": top,
        "bucket_distribution": bucket,
    }


def fetch_thumbnail_meta(vid: str, work_dir: Path) -> dict:
    """썸네일 다운로드 + 메타. OCR/LLM은 옵션 (없으면 메타만)."""
    import subprocess
    venv_yt = ROOT / ".venv" / "bin" / "yt-dlp"
    yt = str(venv_yt) if venv_yt.exists() else "yt-dlp"
    work_dir.mkdir(parents=True, exist_ok=True)
    # mqdefault(320x180) 또는 maxresdefault(1280x720) — 우선 maxres
    thumb_url = f"https://i.ytimg.com/vi/{vid}/maxresdefault.jpg"
    out_path = work_dir / f"{vid}.jpg"
    try:
        import urllib.request
        req = urllib.request.Request(thumb_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
            out_path.write_bytes(data)
    except Exception:
        # fallback to hqdefault
        try:
            thumb_url = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
            with urllib.request.urlopen(thumb_url, timeout=20) as r:
                out_path.write_bytes(r.read())
        except Exception:
            return {}
    meta = {"thumbnail_url": thumb_url, "local_path": str(out_path.relative_to(ROOT)),
            "file_size_kb": round(out_path.stat().st_size / 1024, 1)}
    # OCR 시도 (tesseract 있으면)
    try:
        r = subprocess.run(["tesseract", str(out_path), "-", "-l", "kor+eng"],
                           capture_output=True, text=True, timeout=30)
        ocr_text = (r.stdout or "").strip()
        if ocr_text:
            meta["ocr_text"] = re.sub(r"\s+", " ", ocr_text)[:300]
    except (FileNotFoundError, subprocess.TimeoutExpired):
        meta["ocr_text"] = ""
    return meta


def fetch_video_title(vid: str) -> str:
    import subprocess
    venv_yt = ROOT / ".venv" / "bin" / "yt-dlp"
    yt = str(venv_yt) if venv_yt.exists() else "yt-dlp"
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
    """N편 분석 결과 → 공통 패턴 + 차이점. Hook 세분화 통계 포함."""
    if not analyses:
        return {}
    durations = [a["duration_min"] for a in analyses if a.get("duration_min")]
    wpms = [a["wpm"] for a in analyses if a.get("wpm")]

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

    hook_types = Counter(classify_hook_pattern(a.get("hook", {}).get("text", "")) for a in analyses)
    outro_types = Counter(classify_outro_pattern(a.get("outro", {}).get("text", "")) for a in analyses)

    # === B-1: Hook 세분화 통계 ===
    hook_pattern_types = Counter(a.get("hook", {}).get("pattern", "기타") for a in analyses)
    hook_wpms = [a.get("hook", {}).get("wpm", 0) for a in analyses if a.get("hook", {}).get("wpm")]
    body_wpms = [a.get("hook", {}).get("body_wpm", 0) for a in analyses if a.get("hook", {}).get("body_wpm")]
    intensities = [a.get("hook", {}).get("emotion", {}).get("intensity", 0) for a in analyses]

    # 첫 사건 발생 시점 통계
    event_times = [a.get("first_event", {}).get("at_sec") for a in analyses
                   if a.get("first_event", {}).get("at_sec") is not None]
    avg_event_sec = round(sum(event_times) / len(event_times), 1) if event_times else None

    # 0~3초 / 3~10초 / 10~30초 구간별 평균 길이
    pre_chars = [a.get("hook", {}).get("pre_hook_0_3s", {}).get("char_count", 0) for a in analyses]
    core_chars = [a.get("hook", {}).get("core_3_10s", {}).get("char_count", 0) for a in analyses]
    promise_chars = [a.get("hook", {}).get("promise_10_30s", {}).get("char_count", 0) for a in analyses]

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
        # B-1 세분화
        "hook_pattern_breakdown": dict(hook_pattern_types),
        "hook_pattern_dominant": hook_pattern_types.most_common(1)[0][0] if hook_pattern_types else "기타",
        "avg_hook_wpm": round(sum(hook_wpms) / len(hook_wpms), 1) if hook_wpms else 0,
        "avg_body_wpm": round(sum(body_wpms) / len(body_wpms), 1) if body_wpms else 0,
        "hook_speed_boost": round(sum(hook_wpms) / len(hook_wpms) - sum(body_wpms) / len(body_wpms), 1) if hook_wpms and body_wpms else 0,
        "avg_hook_intensity": round(sum(intensities) / len(intensities), 2) if intensities else 0,
        "first_event_avg_sec": avg_event_sec,
        "first_event_distribution": event_times,
        "hook_section_avg_chars": {
            "pre_0_3s": round(sum(pre_chars) / len(pre_chars), 1) if pre_chars else 0,
            "core_3_10s": round(sum(core_chars) / len(core_chars), 1) if core_chars else 0,
            "promise_10_30s": round(sum(promise_chars) / len(promise_chars), 1) if promise_chars else 0,
        },
        # B-2: N편 간 중복도 (autopsy 영상들끼리)
        "repetition": _calc_repetition(analyses) if ngrams else {},
    }


def _calc_repetition(analyses: list) -> dict:
    """N편 영상의 N-gram·Hook 유사도. (시청자 거부감 진단)"""
    if not ngrams or len(analyses) < 2:
        return {}
    texts = {}
    hook_texts = {}
    for a in analyses:
        vid = a.get("video_id", "")
        texts[vid] = " ".join([a.get("hook", {}).get("text", ""),
                                a.get("intro", {}).get("text", ""),
                                a.get("climax", {}).get("text", ""),
                                a.get("outro", {}).get("text", "")])
        hook_texts[vid] = a.get("hook", {}).get("text", "")
    g3 = {v: ngrams(t, 3) for v, t in texts.items()}
    h2 = {v: ngrams(t, 2) for v, t in hook_texts.items()}
    pairs_3gram, pairs_hook = [], []
    ids = list(texts.keys())
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            pairs_3gram.append({"a": a, "b": b, "jaccard": jaccard(g3[a], g3[b])})
            pairs_hook.append({"a": a, "b": b, "jaccard": jaccard(h2[a], h2[b])})
    avg_3 = round(sum(p["jaccard"] for p in pairs_3gram) / len(pairs_3gram), 4) if pairs_3gram else 0.0
    avg_h = round(sum(p["jaccard"] for p in pairs_hook) / len(pairs_hook), 4) if pairs_hook else 0.0
    monotony = round(avg_3 * 100, 1)
    if monotony >= 30:
        verdict = "🔴 매우 반복적"
    elif monotony >= 20:
        verdict = "🟠 반복 신호"
    elif monotony >= 10:
        verdict = "🟡 적당한 일관성"
    else:
        verdict = "🟢 다양성 양호"
    return {
        "avg_jaccard_3gram": avg_3, "avg_jaccard_hook_2gram": avg_h,
        "monotony_score": monotony, "verdict": verdict,
        "top_pairs_3gram": sorted(pairs_3gram, key=lambda x: -x["jaccard"])[:3],
        "top_pairs_hook": sorted(pairs_hook, key=lambda x: -x["jaccard"])[:3],
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
    th_dir = work_dir / "thumbnails"
    tr_dir.mkdir(exist_ok=True)

    print(f"\n🔥 autopsy: {label} ({slug})")
    print(f"📥 {len(urls)}개 영상 자막 다운로드 + 분석\n")

    analyses = []
    failed = []
    for i, url in enumerate(urls, 1):
        vid = extract_video_id(url)
        print(f"  [{i:2}/{len(urls)}] {vid}", flush=True)
        # 메타 (title + 구독·조회·발행일·좋아요·댓글) 1회 fetch
        meta = fetch_video_meta(vid)
        title = meta.get("title", "") if meta else ""
        record = fetch_subtitle(vid)
        if not record or not record.get("segments"):
            print(f"          ❌ 자막 없음")
            failed.append({"url": url, "video_id": vid, "title": title, "reason": "자막 없음"})
            time.sleep(1)
            continue
        record["title"] = title
        record["url"] = url
        (tr_dir / f"{vid}.json").write_text(
            json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        analysis = analyze_one(record)
        if not analysis or analysis.get("skipped"):
            print(f"          ⏭️  너무 짧음")
            failed.append({"url": url, "video_id": vid, "title": title, "reason": "<60s"})
            time.sleep(1)
            continue
        analysis["title"] = title
        analysis["channel"] = meta.get("channel", "")
        analysis["time_efficiency"] = compute_time_efficiency(meta)
        # C-4: 댓글 timestamp (retention spike 추정)
        try:
            comments = fetch_comments(vid, max_count=80)
            analysis["comment_timestamps"] = extract_timestamps(comments) if comments else {}
        except Exception:
            analysis["comment_timestamps"] = {}
        # C-5: 썸네일 메타 + OCR (tesseract 있을 때)
        try:
            analysis["thumbnail"] = fetch_thumbnail_meta(vid, th_dir)
        except Exception:
            analysis["thumbnail"] = {}
        analyses.append(analysis)
        eff = analysis["time_efficiency"]
        eff_str = f"eff {eff.get('efficiency', 0):.2f}x · {eff.get('tier', '')}" if eff else ""
        ts_cnt = (analysis.get("comment_timestamps") or {}).get("total_timestamps", 0)
        print(f"          ✅ {analysis['duration_min']}분 · {analysis['wpm']}wpm · {eff_str} · 댓글ts {ts_cnt}건")
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
