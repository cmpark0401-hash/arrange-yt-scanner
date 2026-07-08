"""주간 시장 리포트 · 매주 월요일 텔레그램 발송

내용:
  1. 최근 7일 vs 이전 7일 시장 크기 비교
  2. 이번 주 최고 폭발 TOP 5
  3. 급성장 채널 TOP 3
  4. 새 SS/S 티어 후보

사용:
  python monitor_scripts/build_weekly_digest.py
"""
from __future__ import annotations
import json, sys
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, STATE_DIR, send_telegram, load_json


HISTORY = STATE_DIR / 'market_daily.json'
WATCHLIST_FULL = ROOT / 'monitor_scripts/watchlist_economy_full.json'


def main():
    history = load_json(HISTORY, {'snapshots': []})
    snapshots = history.get('snapshots', [])

    if not WATCHLIST_FULL.exists():
        print('⚠️ watchlist 없음')
        return

    channels = json.loads(WATCHLIST_FULL.read_text(encoding='utf-8'))

    # 이번 주 최고 폭발 TOP 5
    all_videos = []
    for c in channels:
        for f in ['top7_video']:
            v = c.get(f)
            if v:
                all_videos.append({
                    'title': v.get('title', ''),
                    'views': v.get('views', 0),
                    'vid': v.get('vid', ''),
                    'channel': c['name'],
                    'tier': c.get('tier', ''),
                })
    all_videos.sort(key=lambda x: -x['views'])
    top_5 = all_videos[:5]

    # 이번 주 상위5 성장 TOP 3 (7d/30d 비율 높은 채널)
    growth = []
    for c in channels:
        t7 = c.get('top5_7d', 0)
        t30 = c.get('top5_30d', 0)
        if t30 > 0 and t7 > 0:
            ratio = t7 / t30
            growth.append((c['name'], c.get('tier', ''), t7, t30, ratio, c.get('subs', 0)))
    growth.sort(key=lambda x: -x[4])
    top_growth = [g for g in growth if g[4] >= 0.7 and g[2] >= 50000][:3]

    # 시장 크기 · 이번 주 vs 지난 주
    week_now = None
    week_ago = None
    if snapshots:
        week_now = snapshots[-1]
        # 7일 전 스냅샷
        target = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        for s in snapshots:
            if s['date'] <= target:
                week_ago = s

    # 메시지 조립
    now = datetime.now()
    lines = [
        f'📊 *주간 시장 리포트*',
        f'_{now.strftime("%Y-%m-%d")} · 감시 54채널_',
        '',
    ]

    if week_now and week_ago:
        def d(k):
            v = week_now.get(k, 0) - week_ago.get(k, 0)
            return f'({"+" if v>=0 else ""}{v:,})' if v != 0 else ''
        lines.append(f'*시장 크기 · 지난주 대비*')
        lines.append(f'  SS 상위5: {week_now["ss_top5_avg"]:,} {d("ss_top5_avg")}')
        lines.append(f'  S 상위5:  {week_now["s_top5_avg"]:,} {d("s_top5_avg")}')
        lines.append(f'  A 상위5:  {week_now["a_top5_avg"]:,} {d("a_top5_avg")}')
        lines.append(f'  10K+ 채널: {week_now["count_10k_7d"]} {d("count_10k_7d")}')
        lines.append('')
    elif week_now:
        lines.append(f'*이번 주 시장 크기*')
        lines.append(f'  SS 상위5: {week_now["ss_top5_avg"]:,}')
        lines.append(f'  S 상위5:  {week_now["s_top5_avg"]:,}')
        lines.append(f'  A 상위5:  {week_now["a_top5_avg"]:,}')
        lines.append(f'  10K+ 채널: {week_now["count_10k_7d"]}편')
        lines.append('_(다음 주부터 지난주 대비 표시)_')
        lines.append('')

    lines.append('🏆 *이번 주 최고 폭발 TOP 5*')
    for i, v in enumerate(top_5, 1):
        title = (v['title'][:35] + '…') if len(v['title']) > 35 else v['title']
        lines.append(f'{i}. [{v["tier"]}] {v["channel"][:12]} · {v["views"]:,}뷰')
        lines.append(f'   {title}')
        lines.append(f'   https://youtu.be/{v["vid"]}')
    lines.append('')

    if top_growth:
        lines.append('🚀 *급성장 채널 TOP 3* (7일 뷰 상위)')
        for i, (n, t, t7, t30, r, subs) in enumerate(top_growth, 1):
            lines.append(f'{i}. [{t}] {n[:15]} · 7일 {t7:,}뷰 · 구독 {subs:,}')
        lines.append('')

    lines.append('━━━━━━━━━━━━━━')
    lines.append('🔗 대시보드: https://arrange-yt-scanner.pages.dev/monitor/')

    msg = '\n'.join(lines)
    print(msg)
    print()

    ok = send_telegram(msg)
    print(f'📢 텔레그램 {"✅" if ok else "❌"}')


if __name__ == '__main__':
    main()
