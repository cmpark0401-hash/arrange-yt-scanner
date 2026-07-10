"""YouTube 검색 · 주제 카피 확산 자동 스캐너"""
from __future__ import annotations
import argparse, json, sys, requests
from pathlib import Path
from datetime import datetime, timezone, timedelta

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, get_yt_bearer

WATCHLIST = ROOT / 'monitor_scripts/watchlist_economy.json'


def search_videos(token, query, days, max_results):
    published_after = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    r = requests.get(
        'https://www.googleapis.com/youtube/v3/search',
        params={
            'part': 'snippet', 'q': query, 'type': 'video',
            'maxResults': min(50, max_results),
            'publishedAfter': published_after,
            'order': 'relevance', 'regionCode': 'KR', 'relevanceLanguage': 'ko',
        },
        headers={'Authorization': f'Bearer {token}'}, timeout=20,
    )
    items = r.json().get('items', [])
    return [{
        'vid': it['id']['videoId'],
        'title': it['snippet']['title'],
        'channel': it['snippet']['channelTitle'],
        'cid': it['snippet']['channelId'],
        'published': it['snippet']['publishedAt'],
    } for it in items]


def fetch_stats(token, vids):
    result = {}
    for i in range(0, len(vids), 50):
        batch = vids[i:i+50]
        r = requests.get(
            'https://www.googleapis.com/youtube/v3/videos',
            params={'part': 'statistics', 'id': ','.join(batch), 'maxResults': 50},
            headers={'Authorization': f'Bearer {token}'}, timeout=30,
        )
        for item in r.json().get('items', []):
            st = item.get('statistics', {})
            result[item['id']] = {'views': int(st.get('viewCount', 0))}
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('query')
    ap.add_argument('--days', type=int, default=30)
    ap.add_argument('--max', type=int, default=30)
    args = ap.parse_args()

    watchlist = json.loads(WATCHLIST.read_text(encoding='utf-8'))
    watch_by_cid = {w['cid']: w for w in watchlist}

    token = get_yt_bearer('knowledge-archive')

    print(f'🔍 "{args.query}" · 최근 {args.days}일 검색 중...')
    videos = search_videos(token, args.query, args.days, args.max)
    print(f'  {len(videos)}편 찾음')

    if not videos:
        print('결과 없음')
        return

    stats = fetch_stats(token, [v['vid'] for v in videos])
    now = datetime.now(timezone.utc)
    for v in videos:
        s = stats.get(v['vid'], {})
        v['views'] = s.get('views', 0)
        try:
            pub_dt = datetime.fromisoformat(v['published'].replace('Z', '+00:00'))
            v['days_ago'] = (now - pub_dt).days
        except:
            v['days_ago'] = 99
        v['in_watchlist'] = v['cid'] in watch_by_cid
        v['tier'] = watch_by_cid.get(v['cid'], {}).get('tier', '')

    videos.sort(key=lambda x: -x['views'])

    print(f'\n=== "{args.query}" · 카피 확산 스캔 ===\n')
    watch_count = sum(1 for v in videos if v['in_watchlist'])
    total_views = sum(v['views'] for v in videos)
    max_views = max((v['views'] for v in videos), default=0)

    print(f'📊 {len(videos)}편 · 총 {total_views:,}뷰 · 최고 {max_views:,}')
    print(f'   감시: {watch_count} · 감시밖: {len(videos)-watch_count}\n')

    print(f'{"뷰":>10s} · {"D+":>3s} · {"티어":>4s} · {"채널":15s} · 제목')
    print('-' * 100)
    for v in videos[:20]:
        marker = '✅' if v['in_watchlist'] else '  '
        tier = f'[{v["tier"]}]' if v['tier'] else ''
        title = v['title'][:55]
        print(f'{marker} {v["views"]:>9,} · D+{v["days_ago"]:>2} · {tier:>4s} · {v["channel"][:14]:14s} · {title}')

    print(f'\n💡 판정: ', end='')
    if len(videos) <= 2:
        print(f'✅ 매우 신선 (진입 최적)')
    elif len(videos) <= 5:
        print(f'⚡ 확산 초기 (원조 성장 확인 필수)')
    elif len(videos) <= 10:
        print(f'⚠️  확산 중반 (새 각도 필요)')
    else:
        print(f'🚫 확산 포화 (스킵 or 완전 새 프레임)')


if __name__ == '__main__':
    main()
