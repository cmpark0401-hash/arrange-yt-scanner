"""야담 velocity TOP20 영상의 자막 다운로드 → JSON corpus 저장.

각 영상에 대해:
1. yt-dlp로 자막 시도 (수동 ko → 자동 ko)
2. VTT 파싱 → segments [{start, end, text}]
3. 저장: _yadam_corpus/{video_id}.json
"""
import json
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YT_DLP = ROOT / ".venv" / "bin" / "yt-dlp"
LOG_DIR = ROOT / "channels" / "knowledge-archive" / "_monitor_logs"
CORPUS_DIR = LOG_DIR / "_yadam_corpus"
CORPUS_DIR.mkdir(parents=True, exist_ok=True)

TOP_N = 20  # velocity 상위 N편 자막 수집


def _yt():
    return str(YT_DLP) if YT_DLP.exists() else "yt-dlp"


def _clean_text(text: str) -> str:
    """VTT 텍스트에서 태그·엔티티·노이즈 마커 제거."""
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&").replace("&nbsp;", " ")
    text = re.sub(r"\[음악\]|\[Music\]|\[applause\]|\[laughter\]|\[박수\]|\[웃음\]", " ", text, flags=re.IGNORECASE)
    text = re.sub(r">>+\s*", "", text)  # >>> 화자 마커
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _collapse_word_repeats(text: str, max_window: int = 20) -> str:
    """연속 단어 chunk 반복 제거 — 자동자막의 rolling 누적 패턴 처리.

    예: "엄마가 죽었다 엄마가 죽었다" → "엄마가 죽었다"
        "a b c d a b c d" → "a b c d"
    """
    words = text.split()
    if len(words) < 4:
        return text
    out = []
    i = 0
    while i < len(words):
        skipped = False
        # 큰 chunk부터 시도: 직전 out의 마지막 N단어 == 현재 위치 N단어면 skip
        # 최대 chunk = min(out 길이, 남은 단어 수, max_window)
        max_n = min(len(out), len(words) - i, max_window)
        for n in range(max_n, 1, -1):
            if out[-n:] == words[i:i + n]:
                i += n
                skipped = True
                break
        if not skipped:
            out.append(words[i])
            i += 1
    return " ".join(out)


def parse_vtt(path: Path) -> list:
    """VTT 파일 파싱 → [{start, end, text}] + 누적 중복 제거."""
    try:
        raw = path.read_text(encoding="utf-8")
    except Exception:
        return []
    segments = []
    pattern = re.compile(r"(\d{2}:\d{2}:\d{2}[\.,]\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}[\.,]\d{3})")
    blocks = re.split(r"\n\n", raw)
    for blk in blocks:
        lines = [ln.strip() for ln in blk.strip().split("\n") if ln.strip()]
        if not lines:
            continue
        ts_line = next((ln for ln in lines if pattern.search(ln)), None)
        if not ts_line:
            continue
        m = pattern.search(ts_line)
        if not m:
            continue
        start = ts_to_sec(m.group(1))
        end = ts_to_sec(m.group(2))
        text_lines = [ln for ln in lines
                      if ln != ts_line and not pattern.search(ln)
                      and not ln.startswith("WEBVTT") and not ln.isdigit()]
        text = _clean_text(" ".join(text_lines))
        if not text:
            continue
        segments.append({"start": round(start, 2), "end": round(end, 2), "text": text})

    # 1단계: 동일 텍스트 인접 중복 제거
    dedup_eq, last = [], None
    for s in segments:
        if s["text"] == last:
            continue
        dedup_eq.append(s)
        last = s["text"]

    # 2단계: rolling 누적 패턴 처리 (이전 텍스트의 suffix를 prefix로 포함하면 새 부분만 보존)
    rolled = []
    prev_text = ""
    for s in dedup_eq:
        cur = s["text"]
        if prev_text and cur.startswith(prev_text):
            new_part = cur[len(prev_text):].strip()
            if new_part:
                rolled.append({**s, "text": new_part})
            prev_text = cur
            continue
        # 부분 overlap (이전 끝 = 현재 시작 N글자)
        overlap_len = 0
        max_check = min(len(prev_text), len(cur), 100)
        for n in range(max_check, 3, -1):
            if prev_text.endswith(cur[:n]):
                overlap_len = n; break
        if overlap_len > 0:
            new_part = cur[overlap_len:].strip()
            if new_part:
                rolled.append({**s, "text": new_part})
                prev_text = (prev_text + " " + new_part).strip()[-200:]
            continue
        rolled.append(s)
        prev_text = cur[-200:]  # prev_text 길이 제한

    # 3단계: 세그먼트 내 단어 chunk 반복 제거
    for s in rolled:
        s["text"] = _collapse_word_repeats(s["text"])

    return [s for s in rolled if s["text"]]


def ts_to_sec(ts: str) -> float:
    ts = ts.replace(",", ".")
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def fetch_subtitle(vid: str) -> dict:
    """수동 → 자동 자막 다운로드 시도. dict 또는 빈 dict."""
    import os
    url = f"https://www.youtube.com/watch?v={vid}"
    debug = bool(os.environ.get("AUTOPSY_DEBUG"))
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        # 수동·자동 자막 모두 시도, ko 우선
        # IPv4 강제·UA 지정·extractor 다양화 — GitHub Actions IP 제약 우회
        cmd = [_yt(), url, "--skip-download",
               "--write-subs", "--write-auto-subs",
               "--sub-format", "vtt",
               "--sub-langs", "ko.*,ko",
               "-o", str(tmp_path / "%(id)s.%(ext)s"),
               "--no-warnings", "--force-ipv4",
               "--user-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
               "--extractor-args", "youtube:player_client=mweb,web,android,ios;player_skip=webpage"]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        except subprocess.TimeoutExpired:
            if debug: print(f"          ⚠️  timeout 180s")
            return {}
        # 다운된 vtt 찾기
        vtts = sorted(tmp_path.glob(f"{vid}.*.vtt"))
        if not vtts:
            stdout = r.stdout or ""
            stderr = r.stderr or ""
            # 명령행도 같이 출력 (yt-dlp 어떻게 호출했는지)
            print(f"          ⚠️  yt-dlp returncode={r.returncode}")
            print(f"          ⚠️  cmd[:3]={cmd[:3]}")
            if stdout: print(f"          ⚠️  stdout: {stdout[-600:]}")
            if stderr: print(f"          ⚠️  stderr: {stderr[-800:]}")
            if not stdout and not stderr:
                print(f"          ⚠️  (empty stdout/stderr — yt-dlp 명령 자체 실패 가능)")
            return {}
        # ko 수동 우선, 다음 ko-orig, 다음 첫 번째
        preferred = None
        for v in vtts:
            if ".ko.vtt" in v.name:
                preferred = v; break
        if not preferred:
            for v in vtts:
                if "ko" in v.name:
                    preferred = v; break
        if not preferred:
            preferred = vtts[0]
        segments = parse_vtt(preferred)
        return {
            "video_id": vid,
            "sub_file": preferred.name,
            "auto": ".auto" in preferred.name or "-orig" in preferred.name,
            "segments": segments,
            "total_segments": len(segments),
            "duration_sec": segments[-1]["end"] if segments else 0,
        }


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="기존 corpus json 무시하고 재다운로드")
    args = ap.parse_args()

    files = sorted(LOG_DIR.glob("senior_explore_*.json"), reverse=True)
    if not files:
        print("❌ senior_explore JSON 없음")
        return
    data = json.loads(files[0].read_text())
    videos = data.get("yadam", {}).get("videos", [])

    # velocity TOP N + 채널별 역대 TOP1도 같이 (대표 영상 학습)
    top_v = sorted(videos, key=lambda v: -v.get("velocity_per_hour", 0))[:TOP_N]
    alltime_reps = []
    for ch in data.get("yadam", {}).get("channel_alltime", []):
        if ch.get("top_videos"):
            alltime_reps.append(ch["top_videos"][0])

    targets = []
    seen = set()
    for v in top_v:
        if v["id"] not in seen:
            targets.append({"id": v["id"], "title": v["title"], "source": "velocity_top"})
            seen.add(v["id"])
    for v in alltime_reps:
        if v["id"] not in seen:
            targets.append({"id": v["id"], "title": v["title"], "source": "alltime_top"})
            seen.add(v["id"])
    print(f"📥 자막 수집 대상 {len(targets)}편 (velocity TOP{TOP_N} + 채널별 역대 1위)\n")

    ok, fail = 0, 0
    summary = []
    for i, t in enumerate(targets, 1):
        vid = t["id"]
        out_path = CORPUS_DIR / f"{vid}.json"
        if out_path.exists() and not args.force:
            print(f"  [{i:2}/{len(targets)}] ⏭️  {vid} 이미 있음 ({t['title'][:35]})")
            ok += 1
            try:
                summary.append({"video_id": vid, "title": t["title"], "source": t["source"],
                                "segments": json.loads(out_path.read_text())["total_segments"]})
            except Exception:
                pass
            continue
        print(f"  [{i:2}/{len(targets)}] 🎯 {vid} {t['title'][:35]}", flush=True)
        result = fetch_subtitle(vid)
        if result and result.get("segments"):
            result["title"] = t["title"]
            result["source"] = t["source"]
            out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"          ✅ {result['total_segments']}세그·{int(result['duration_sec'])}초{'·자동' if result['auto'] else '·수동'}")
            summary.append({"video_id": vid, "title": t["title"], "source": t["source"],
                            "segments": result["total_segments"]})
            ok += 1
        else:
            print("          ❌ 자막 없음/실패")
            fail += 1
        time.sleep(1)

    idx_path = CORPUS_DIR / f"_index_{data.get('date')}.json"
    idx_path.write_text(json.dumps({
        "date": data.get("date"),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "total_targets": len(targets),
        "succeeded": ok, "failed": fail,
        "corpus": summary,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✅ 완료 {ok}편 · 실패 {fail}편 → {CORPUS_DIR.name}/")


if __name__ == "__main__":
    main()
