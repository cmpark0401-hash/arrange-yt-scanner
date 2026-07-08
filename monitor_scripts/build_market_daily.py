"""시장 트렌드 일일 스냅샷 · 매일 실행

목적:
  54개 감시 채널의 조회수 크기가 매일 어떻게 변화하는지 추적
  = 경제 카테고리 시장 관심도 지수

저장:
  state/market_daily.json  (최근 60일 히스토리)
  docs/monitor/assets/data/market_trend.js  (대시보드 임베드)
"""
from __future__ import annotations
import json, sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, STATE_DIR, write_js_var, load_json, save_json


WATCHLIST_FULL = ROOT / 'monitor_scripts/watchlist_economy_full.json'
HISTORY = STATE_DIR / 'market_daily.json'
JS_OUT = ROOT / 'monitor/assets/data/market_trend.js'


def build_snapshot(channels: list) -> dict:
    today = datetime.now().strftime('%Y-%m-%d')
    by_tier = {'SS': [], 'S': [], 'A': []}
    all_7d = []
    all_30d = []
    top_video = None
    count_10k_7d = 0
    count_100k_7d = 0
    total_uploads_7d = 0
    total_uploads_30d = 0
    for c in channels:
        tier = c.get('tier', '')
        t7 = c.get('top5_7d', 0)
        t30 = c.get('top5_30d', 0)
        if tier in by_tier:
            by_tier[tier].append(t7)
        all_7d.append(t7)
        all_30d.append(t30)
        total_uploads_7d += c.get('count_7d', 0)
        total_uploads_30d += c.get('count_30d', 0)
        if t7 >= 10000: count_10k_7d += 1
        if t7 >= 100000: count_100k_7d += 1
        for f in ['top1_video', 'top7_video']:
            v = c.get(f)
            if v and (not top_video or v.get('views', 0) > top_video.get('views', 0)):
                top_video = {
                    'title': v.get('title', ''), 'views': v.get('views', 0),
                    'vid': v.get('vid', ''), 'channel': c['name'], 'tier': tier,
                }
    def avg(lst): return int(sum(lst)/len(lst)) if lst else 0
    return {
        'date': today,
        'total_channels': len(channels),
        'tier_ss_count': len(by_tier['SS']),
        'tier_s_count': len(by_tier['S']),
        'tier_a_count': len(by_tier['A']),
        'ss_top5_avg': avg(by_tier['SS']),
        's_top5_avg': avg(by_tier['S']),
        'a_top5_avg': avg(by_tier['A']),
        'all_top5_avg': avg(all_7d),
        'all_top5_30d_avg': avg(all_30d),
        'count_10k_7d': count_10k_7d,
        'count_100k_7d': count_100k_7d,
        'total_uploads_7d': total_uploads_7d,
        'total_uploads_30d': total_uploads_30d,
        'top_video': top_video,
    }


def main():
    if not WATCHLIST_FULL.exists():
        print('⚠️ watchlist_economy_full.json 없음. refresh_watchlist 먼저')
        return
    channels = json.loads(WATCHLIST_FULL.read_text(encoding='utf-8'))
    snapshot = build_snapshot(channels)

    history = load_json(HISTORY, {'snapshots': []})
    snapshots = history.get('snapshots', [])
    snapshots = [s for s in snapshots if s.get('date') != snapshot['date']]
    snapshots.append(snapshot)
    snapshots = sorted(snapshots, key=lambda x: x['date'])[-60:]
    history['snapshots'] = snapshots
    history['updated_at'] = datetime.now().isoformat()
    save_json(HISTORY, history)
    write_js_var(JS_OUT, 'MARKET_TREND', history)

    print(f'✅ {snapshot["date"]} · {snapshot["total_channels"]}채널')
    print(f'   상위5 평균: SS {snapshot["ss_top5_avg"]:,} · S {snapshot["s_top5_avg"]:,} · A {snapshot["a_top5_avg"]:,}')
    print(f'   폭발: 10K+ {snapshot["count_10k_7d"]}채널 · 100K+ {snapshot["count_100k_7d"]}채널')
    print(f'   발행: 7일 {snapshot["total_uploads_7d"]}편 · 30일 {snapshot["total_uploads_30d"]}편')

    if len(snapshots) >= 2:
        prev, cur = snapshots[-2], snapshots[-1]
        def d(k):
            v = cur.get(k, 0) - prev.get(k, 0)
            return f'({"+" if v>=0 else ""}{v:,})'
        print(f'\n📊 어제 대비:')
        print(f'   S 상위5: {cur["s_top5_avg"]:,} {d("s_top5_avg")}')
        print(f'   A 상위5: {cur["a_top5_avg"]:,} {d("a_top5_avg")}')
        print(f'   10K+ 채널: {cur["count_10k_7d"]} {d("count_10k_7d")}')


if __name__ == '__main__':
    main()
