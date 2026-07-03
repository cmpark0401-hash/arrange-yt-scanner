"""튜브해커 사이트 데이터 빌드 (GitHub Actions 버전)

입력:
  monitor_scripts/watchlist_economy_full.json  (refresh_watchlist 산출)
  state/alert_last.json                        (monitor_lite 산출)

출력:
  monitor/assets/data/channels.js
  monitor/assets/data/alerts.js
  monitor/assets/data/topics.js
  monitor/assets/data/summary.js
"""
from __future__ import annotations
import json, sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, STATE_DIR, write_js_var


SITE = ROOT / 'monitor'
DATA_OUT = SITE / 'assets/data'
WATCHLIST_FULL = ROOT / 'monitor_scripts/watchlist_economy_full.json'
ALERT_LAST = STATE_DIR / 'alert_last.json'
TOPICS_SRC = ROOT / 'monitor_scripts/topic_pie_expanded.json'
HOT_SRC = ROOT / 'monitor_scripts/hot_topics.json'


def build():
    DATA_OUT.mkdir(parents=True, exist_ok=True)
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    # 1) 채널 리스트
    if WATCHLIST_FULL.exists():
        channels = json.loads(WATCHLIST_FULL.read_text(encoding='utf-8'))
        write_js_var(DATA_OUT / 'channels.js', 'CHANNELS', channels)
        print(f'✅ channels.js · {len(channels)}채널')
    else:
        print('⚠️ watchlist_economy_full.json 없음 · refresh_watchlist 먼저')
        channels = []
        write_js_var(DATA_OUT / 'channels.js', 'CHANNELS', [])

    # 2) 알림 큐
    if ALERT_LAST.exists():
        alerts = json.loads(ALERT_LAST.read_text(encoding='utf-8'))
        recent_alerts = len(alerts.get('entries', []))
    else:
        alerts = {'entries': []}
        recent_alerts = 0
    write_js_var(DATA_OUT / 'alerts.js', 'ALERTS', alerts)
    print(f'✅ alerts.js · {recent_alerts}건')

    # 3) 주제 클러스터 (선택 · 없어도 OK)
    if TOPICS_SRC.exists():
        topics = json.loads(TOPICS_SRC.read_text(encoding='utf-8'))
    else:
        topics = {'clusters': []}
    write_js_var(DATA_OUT / 'topics.js', 'TOPICS', topics)
    print(f'✅ topics.js · {len(topics.get("clusters", []))}클러스터')

    # 4) hot topics (있으면)
    hot_count = 0
    if HOT_SRC.exists():
        hot = json.loads(HOT_SRC.read_text(encoding='utf-8'))
        hot_count = len(hot.get('candidates', []))

    # 5) summary
    summary = {
        'channels': len(channels),
        'hot_videos': hot_count,
        'recent_alerts': recent_alerts,
        'updated_at': now,
    }
    write_js_var(DATA_OUT / 'summary.js', 'SUMMARY', summary)
    print(f'✅ summary.js · 갱신 {now}')

    print(f'\n🎯 사이트 빌드 완료: {SITE}')


if __name__ == '__main__':
    build()
