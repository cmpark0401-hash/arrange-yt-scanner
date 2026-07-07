"""채널 풀 데이터 빌드 · 등록된 전체 168 채널 (감시 여부 태그)

출력: monitor/assets/data/channel_pool.js
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, write_js_var


POOL_SRC = ROOT / 'monitor_scripts/monitor_channels_economy.json'
WATCHLIST = ROOT / 'monitor_scripts/watchlist_economy.json'
JS_OUT = ROOT / 'monitor/assets/data/channel_pool.js'


def extract_cid(url: str) -> str:
    if '/channel/' in url:
        return url.split('/channel/')[1].split('/')[0]
    return ''


def build():
    pool = json.loads(POOL_SRC.read_text(encoding='utf-8'))
    watchlist = json.loads(WATCHLIST.read_text(encoding='utf-8'))
    watch_map = {w['cid']: w for w in watchlist}
    watch_cids = set(watch_map.keys())

    entries = []
    for p in pool:
        url = p.get('url', '')
        cid = extract_cid(url)
        is_watch = cid in watch_cids
        w = watch_map.get(cid, {})

        entries.append({
            'name': p.get('name', ''),
            'url': url,
            'cid': cid,
            'type': p.get('type', ''),
            'categories': p.get('categories', []),
            'is_watching': is_watch,
            'tier': w.get('tier', '') if is_watch else '',
            'subs': w.get('subs', 0) if is_watch else 0,
            'avg_views': w.get('avg_views', 0) if is_watch else 0,
            'poll_interval_min': w.get('poll_interval_min', 0) if is_watch else 0,
        })

    stats = {
        'total': len(entries),
        'watching': sum(1 for e in entries if e['is_watching']),
        'candidate': sum(1 for e in entries if not e['is_watching']),
        'by_type': {},
        'by_tier': {'SS': 0, 'S': 0, 'A': 0, '_none': 0},
    }
    for e in entries:
        t = e['type'] or '?'
        stats['by_type'][t] = stats['by_type'].get(t, 0) + 1
        if e['is_watching']:
            stats['by_tier'][e['tier'] or '_none'] = stats['by_tier'].get(e['tier'] or '_none', 0) + 1

    from datetime import datetime
    payload = {
        'entries': entries,
        'stats': stats,
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
    }
    write_js_var(JS_OUT, 'CHANNEL_POOL', payload)
    print(f'✅ channel_pool.js · 전체 {stats["total"]} · 감시 중 {stats["watching"]} · 후보 {stats["candidate"]}')


if __name__ == '__main__':
    build()
