"""경량 폭발 감지 스캐너 · S+A 54채널 (GitHub Actions 버전)

Level 1: 폭발 임계 초과 시 텔레그램 알림 (기존)
Level 2: 조기 시그널 (VPH 채널 평균 3배 이상) 알림 (NEW)

주기: 15분마다
상태: state/monitor_lite_state.json (Actions Artifact로 승계)

Emoji 위계:
  🔥🔥  임계 × 2 초과 (초대형 폭발)
  🔥    임계 초과 (폭발)
  ⚡    조기 시그널 (VPH 3배 · 폭발 갈 조짐)
  👀    관찰 (신규 감지지만 지표 미달)
"""
from __future__ import annotations
import argparse, json, re, sys, requests
from pathlib import Path
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

# 로컬 import (common.py)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (
    ROOT, STATE_DIR, get_yt_bearer, send_telegram,
    load_json, save_json,
)


WATCHLIST = ROOT / 'monitor_scripts/watchlist_economy.json'
STATE = STATE_DIR / 'monitor_lite_state.json'
ALERT_LAST = STATE_DIR / 'alert_last.json'
ALERT_HISTORY = STATE_DIR / 'alert_history.jsonl'


def load_state() -> dict:
    return load_json(STATE, {'channels': {}, 'last_run': None})


def save_state(state: dict):
    state['last_run'] = datetime.now(timezone.utc).isoformat()
    save_json(STATE, state)


def fetch_rss_vids(cid: str, n: int = 5) -> list[dict]:
    try:
        r = requests.get(
            f'https://www.youtube.com/feeds/videos.xml?channel_id={cid}',
            headers={'User-Agent': 'Mozilla/5.0'}, timeout=15,
        )
        if r.status_code != 200:
            return []
        vids = []
        for m in re.finditer(r'<entry>(.*?)</entry>', r.text, re.DOTALL):
            block = m.group(1)
            vm = re.search(r'<yt:videoId>([^<]+)</yt:videoId>', block)
            tm = re.search(r'<title>([^<]+)</title>', block)
            pm = re.search(r'<published>([^<]+)</published>', block)
            if vm:
                vids.append({
                    'vid': vm.group(1),
                    'title': (tm.group(1) if tm else '').strip(),
                    'published': pm.group(1) if pm else '',
                })
            if len(vids) >= n:
                break
        return vids
    except Exception:
        return []


def fetch_video_stats(video_ids: list[str], token: str) -> dict:
    result = {}
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        try:
            r = requests.get(
                'https://www.googleapis.com/youtube/v3/videos',
                params={
                    'part': 'statistics,snippet',
                    'id': ','.join(batch), 'maxResults': 50,
                },
                headers={'Authorization': f'Bearer {token}'}, timeout=30,
            )
            for item in r.json().get('items', []):
                st = item.get('statistics', {})
                sn = item.get('snippet', {})
                result[item['id']] = {
                    'views': int(st.get('viewCount', 0)),
                    'comments': int(st.get('commentCount', 0)),
                    'likes': int(st.get('likeCount', 0)),
                    'title': sn.get('title', ''),
                    'published': sn.get('publishedAt', ''),
                    'channel': sn.get('channelTitle', ''),
                }
        except Exception as e:
            print(f'  WARN API failure: {e}')
    return result


def is_due(cid: str, interval_min: int, state: dict) -> bool:
    last = state['channels'].get(cid, {}).get('last_polled')
    if not last:
        return True
    last_dt = datetime.fromisoformat(last)
    return (datetime.now(timezone.utc) - last_dt) >= timedelta(minutes=interval_min)


def compute_baseline_vph(w: dict) -> float:
    """채널 평균 VPH 근사값.

    우선순위:
      1. avg_vph_baseline (있으면 사용)
      2. avg_views / 24 (하루당 조회수 → 시간당 근사)
      3. explosion_threshold / 24 (fallback)
    """
    v = w.get('avg_vph_baseline', 0)
    if v > 0:
        return v
    v = w.get('avg_views', 0)
    if v > 0:
        return v / 24
    return w.get('explosion_threshold', 10000) / 24


def classify_alert(views: int, vph: float, hours_since: float, w: dict) -> tuple[str, str]:
    """감지 등급 판정.

    반환: (emoji, level)
      level ∈ {'super', 'explosion', 'early', 'watch'}
    """
    threshold = w.get('explosion_threshold', 10000)
    baseline_vph = compute_baseline_vph(w)

    # Level 1: 폭발
    if views >= threshold * 2:
        return '🔥🔥', 'super'
    if views >= threshold:
        return '🔥', 'explosion'
    # 급등 초기 (기존 로직 유지 · 시간당 임계/12 & 뷰 2000+)
    if hours_since and hours_since >= 0.5 and vph >= threshold / 12 and views >= 2000:
        return '🔥', 'explosion'

    # Level 2: 조기 시그널 (VPH 3배 이상 · 폭발 갈 조짐)
    # 발행 30분 이상 지났고, 뷰 300 이상 최소 확보
    if hours_since and hours_since >= 0.5 and vph >= baseline_vph * 3 and views >= 300:
        return '⚡', 'early'

    return '👀', 'watch'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true', help='알림 전송 안 함')
    ap.add_argument('--all', action='store_true', help='폴링 주기 무시 · 전 채널')
    ap.add_argument('--tier', choices=['S', 'A'], help='특정 티어만')
    args = ap.parse_args()

    watchlist = json.loads(WATCHLIST.read_text(encoding='utf-8'))
    state = load_state()

    targets = watchlist
    if args.tier:
        targets = [w for w in targets if w['tier'] == args.tier]
    if not args.all:
        targets = [w for w in targets if is_due(w['cid'], w['poll_interval_min'], state)]

    print(f'📡 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} · '
          f'대상 {len(targets)}/{len(watchlist)}채널')
    if not targets:
        print('  (도래한 채널 없음)')
        return

    # 1) RSS 병렬 폴링
    all_new_vids = []  # (channel_meta, video)
    now_iso = datetime.now(timezone.utc).isoformat()
    with ThreadPoolExecutor(max_workers=15) as ex:
        futs = {ex.submit(fetch_rss_vids, w['cid'], 5): w for w in targets}
        for fut in as_completed(futs):
            w = futs[fut]
            vids = fut.result()
            seen = set(state['channels'].get(w['cid'], {}).get('seen', []))
            new_vids = [v for v in vids if v['vid'] not in seen]
            if w['cid'] not in state['channels']:
                state['channels'][w['cid']] = {}
            state['channels'][w['cid']]['last_polled'] = now_iso
            combined = [v['vid'] for v in vids] + list(seen)
            new_seen = list(dict.fromkeys(combined))[:50]
            state['channels'][w['cid']]['seen'] = new_seen
            for v in new_vids:
                all_new_vids.append((w, v))

    print(f'  🆕 신규 감지: {len(all_new_vids)}편')

    is_first_run = state.get('last_run') is None
    if is_first_run:
        print('  ℹ️ 첫 실행 · state만 초기화 (알림 X)')
        save_state(state)
        return

    if not all_new_vids:
        save_state(state)
        return

    # 2) 신규 vid API 배치 조회
    print('  📊 API 배치 조회...')
    token = get_yt_bearer('knowledge-archive')
    vid_ids = [v['vid'] for _, v in all_new_vids]
    stats = fetch_video_stats(vid_ids, token)

    # 3) 등급 판정
    explosions = []
    earlies = []
    watches = []
    for w, v in all_new_vids:
        s = stats.get(v['vid'], {})
        views = s.get('views', 0)
        comments = s.get('comments', 0)

        pub = s.get('published') or v.get('published', '')
        hours_since = None
        if pub:
            try:
                pub_dt = datetime.fromisoformat(pub.replace('Z', '+00:00'))
                hours_since = round(
                    (datetime.now(timezone.utc) - pub_dt).total_seconds() / 3600, 1,
                )
            except Exception:
                pass

        vph = round(views / hours_since, 0) if hours_since and hours_since >= 0.5 else 0

        emoji, level = classify_alert(views, vph, hours_since, w)
        print(f'  {emoji} [{w["tier"]}] {s.get("title","")[:35]:35s} · {views:>7,}뷰 · {hours_since}시간')

        entry = {
            'w': w, 'v': v, 's': s, 'views': views, 'comments': comments,
            'hours': hours_since, 'vph': vph, 'level': level, 'emoji': emoji,
        }
        if level in ('super', 'explosion'):
            explosions.append(entry)
        elif level == 'early':
            earlies.append(entry)
        else:
            watches.append(entry)

    # 4) 텔레그램 알림 (폭발 + 조기 시그널 통합)
    alerts = explosions + earlies
    if alerts:
        alerts.sort(key=lambda x: (0 if x['level'] in ('super', 'explosion') else 1, -x['views']))

        header = '🔥 *경제 폭발 감지*' if explosions else '⚡ *조기 시그널 감지*'
        counts = []
        n_super = sum(1 for a in alerts if a['level'] == 'super')
        n_expl = sum(1 for a in alerts if a['level'] == 'explosion')
        n_early = sum(1 for a in alerts if a['level'] == 'early')
        if n_super: counts.append(f'🔥🔥 {n_super}')
        if n_expl: counts.append(f'🔥 {n_expl}')
        if n_early: counts.append(f'⚡ {n_early}')

        msg_lines = [
            f'{header} · {" · ".join(counts)}',
            f'_{datetime.now().strftime("%m/%d %H:%M")} · 대본 후보_',
            '',
        ]

        queue_entries = []
        for i, a in enumerate(alerts[:8], 1):
            w, s = a['w'], a['s']
            title = (s.get('title', '?')
                     .replace('*', '\\*').replace('_', '\\_')
                     .replace('[', '\\[').replace(']', '\\]'))
            threshold = w.get('explosion_threshold', 0)
            multiplier = round(a['views'] / threshold, 1) if threshold else 0
            fire = a['emoji']
            hrs = f'{a["hours"]}h' if a["hours"] else '?'
            comment_pct = f'{a["comments"] / a["views"] * 100:.2f}%' if a["views"] else '0%'

            msg_lines.append(f'{fire} *{i}. {w["name"]}* [{w["tier"]}]')
            msg_lines.append(f'📌 {title[:65]}')
            if a['level'] == 'early':
                baseline = compute_baseline_vph(w)
                vph_x = round(a['vph'] / baseline, 1) if baseline else 0
                msg_lines.append(f'📊 {a["views"]:,}뷰 · vph {int(a["vph"]):,} ({vph_x}x평균)')
            else:
                msg_lines.append(f'📊 {a["views"]:,}뷰 ({multiplier}x임계) · 💬 {comment_pct}')
            msg_lines.append(f'⏱ {hrs} · vph {int(a["vph"] or 0):,}')
            msg_lines.append(f'🔗 https://youtu.be/{a["v"]["vid"]}')
            msg_lines.append('')

            queue_entries.append({
                'idx': i, 'level': a['level'], 'emoji': a['emoji'],
                'tier': w['tier'],
                'channel_name': w['name'],
                'channel_cid': w['cid'],
                'channel_url': w['url'],
                'vid': a['v']['vid'],
                'video_url': f'https://youtu.be/{a["v"]["vid"]}',
                'title': s.get('title', ''),
                'views': a['views'],
                'comments': a['comments'],
                'comment_ratio_pct': round(a['comments'] / a['views'] * 100, 3) if a['views'] else 0,
                'hours_since_publish': a['hours'],
                'views_per_hour': int(a['vph'] or 0),
                'threshold': threshold,
                'multiplier': multiplier,
            })

        msg_lines.append('━━━━━━━━━━━━━━')
        msg_lines.append('💬 *대본 작업 지시 예시*')
        msg_lines.append('  · "#1 247경제 변형 대본"')
        msg_lines.append('  · "#1 지식록 변형 대본"')
        msg_lines.append('  · "#2 원조 추적"')

        msg = '\n'.join(msg_lines)

        payload = {
            'batch_ts': datetime.now(timezone.utc).isoformat(),
            'batch_local': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'entries': queue_entries,
        }
        save_json(ALERT_LAST, payload)
        with ALERT_HISTORY.open('a', encoding='utf-8') as f:
            f.write(json.dumps(payload, ensure_ascii=False) + '\n')

        if not args.dry_run:
            ok = send_telegram(msg)
            print(f'  📢 텔레그램 {"✅" if ok else "❌"} · '
                  f'폭발 {len(explosions)} · 조기 {len(earlies)}')
        else:
            print('\n[DRY RUN] 알림 미전송 · 미리보기:')
            print(msg)

    save_state(state)
    print('✅ 완료 · state 저장')


if __name__ == '__main__':
    main()
