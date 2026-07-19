"""지식록·247경제·레드맨 3채널의 최근 업로드 + 성과 수집 (GitHub Actions 버전)

3개 OAuth 토큰을 환경변수에서 읽음:
  YT_TOKEN_KNOWLEDGE_ARCHIVE
  YT_TOKEN_ECONOMY_247
  YT_TOKEN_REDMAN_POLITICS
"""
from __future__ import annotations
import json, re, requests, sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, get_credentials, write_js_var


OUT = ROOT / 'monitor/assets/data/my_channels.js'

MY_CHANNELS = [
    {'slug': 'knowledge-archive', 'name': '지식록', 'emoji': '📈', 'color': '#3b82f6'},
    {'slug': 'economy-247', 'name': '247경제', 'emoji': '💹', 'color': '#dc2626'},
    {'slug': 'redman-economy', 'name': '레드맨', 'emoji': '🇰🇷', 'color': '#e11d48'},
]


def fetch_channel_info(token):
    r = requests.get(
        'https://www.googleapis.com/youtube/v3/channels',
        params={'part': 'snippet,statistics,contentDetails', 'mine': 'true'},
        headers={'Authorization': f'Bearer {token}'}, timeout=15,
    )
    items = r.json().get('items', [])
    if not items:
        return None
    ch = items[0]
    return {
        'channel_id': ch['id'],
        'title': ch['snippet']['title'],
        'subs': int(ch['statistics'].get('subscriberCount', 0)),
        'total_views': int(ch['statistics'].get('viewCount', 0)),
        'video_count': int(ch['statistics'].get('videoCount', 0)),
        'uploads_playlist': ch['contentDetails']['relatedPlaylists']['uploads'],
    }


def fetch_recent_videos(token, playlist_id, max_videos=30):
    vids = []
    next_page = None
    while len(vids) < max_videos:
        params = {'part': 'contentDetails', 'playlistId': playlist_id,
                  'maxResults': min(50, max_videos - len(vids))}
        if next_page:
            params['pageToken'] = next_page
        r = requests.get(
            'https://www.googleapis.com/youtube/v3/playlistItems',
            params=params,
            headers={'Authorization': f'Bearer {token}'}, timeout=15,
        )
        data = r.json()
        for item in data.get('items', []):
            vids.append(item['contentDetails']['videoId'])
        next_page = data.get('nextPageToken')
        if not next_page:
            break
    return vids[:max_videos]


def fetch_video_details(token, video_ids):
    result = {}
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        r = requests.get(
            'https://www.googleapis.com/youtube/v3/videos',
            params={'part': 'snippet,statistics,contentDetails',
                    'id': ','.join(batch), 'maxResults': 50},
            headers={'Authorization': f'Bearer {token}'}, timeout=30,
        )
        for item in r.json().get('items', []):
            st = item.get('statistics', {})
            sn = item.get('snippet', {})
            cd = item.get('contentDetails', {})
            dur = cd.get('duration', 'PT0S')
            m = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', dur)
            hours = int(m.group(1) or 0) if m else 0
            mins = int(m.group(2) or 0) if m else 0
            secs = int(m.group(3) or 0) if m else 0
            duration_sec = hours * 3600 + mins * 60 + secs

            result[item['id']] = {
                'title': sn.get('title', ''),
                'published': sn.get('publishedAt', ''),
                'views': int(st.get('viewCount', 0)),
                'likes': int(st.get('likeCount', 0)),
                'comments': int(st.get('commentCount', 0)),
                'duration_sec': duration_sec,
            }
    return result


def fetch_analytics(token, days=30):
    end_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    start_date = (datetime.now(timezone.utc) - timedelta(days=days)).strftime('%Y-%m-%d')

    result = {'available': False}
    try:
        r = requests.get(
            'https://youtubeanalytics.googleapis.com/v2/reports',
            params={
                'ids': 'channel==MINE',
                'startDate': start_date,
                'endDate': end_date,
                'metrics': 'views,impressionClickThroughRate,'
                           'averageViewPercentage,averageViewDuration',
            },
            headers={'Authorization': f'Bearer {token}'}, timeout=15,
        )
        data = r.json()
        rows = data.get('rows', [])
        if rows:
            row = rows[0]
            result = {
                'channel_views_30d': row[0] if len(row) > 0 else 0,
                'channel_ctr': row[1] if len(row) > 1 else 0,
                'channel_avg_retention_pct': row[2] if len(row) > 2 else 0,
                'channel_avg_duration_sec': row[3] if len(row) > 3 else 0,
                'available': True,
            }
    except Exception as e:
        print(f'  WARN analytics: {e}')
    return result


def process_channel(cfg):
    print(f'\n🔐 {cfg["emoji"]} {cfg["name"]} ({cfg["slug"]})')
    try:
        creds = get_credentials(cfg['slug'])
    except Exception as e:
        print(f'   ERR token: {e}')
        return {**cfg, 'error': 'no_token', 'error_detail': str(e)}

    token = creds.token
    info = fetch_channel_info(token)
    if not info:
        return {**cfg, 'error': 'no_channel_info'}

    print(f'   채널: {info["title"]} · 구독 {info["subs"]:,} · 영상 {info["video_count"]}')

    vids = fetch_recent_videos(token, info['uploads_playlist'], max_videos=30)
    print(f'   최근 {len(vids)}편')

    details = fetch_video_details(token, vids)
    print(f'   상세 {len(details)}편')

    analytics = fetch_analytics(token)
    if analytics.get('available'):
        print(f'   Analytics CTR {analytics["channel_ctr"]:.2f}% · '
              f'지속률 {analytics["channel_avg_retention_pct"]:.1f}%')

    now = datetime.now(timezone.utc)
    videos = []
    for vid in vids:
        d = details.get(vid, {})
        if not d:
            continue
        try:
            pub = datetime.fromisoformat(d['published'].replace('Z', '+00:00'))
            days_ago = (now - pub).days
            date_str = pub.strftime('%Y-%m-%d %H:%M')
        except Exception:
            days_ago = 999
            date_str = ''
        videos.append({
            'vid': vid,
            'title': d.get('title', ''),
            'views': d.get('views', 0),
            'likes': d.get('likes', 0),
            'comments': d.get('comments', 0),
            'duration_sec': d.get('duration_sec', 0),
            'days_ago': days_ago,
            'date_str': date_str,
            'url': f'https://youtu.be/{vid}',
            'comment_ratio_pct': round(d.get('comments', 0) / d.get('views', 1) * 100, 3)
                                 if d.get('views') else 0,
        })
    videos.sort(key=lambda x: x['days_ago'])

    return {
        **cfg, **info,
        'analytics': analytics,
        'videos': videos,
        'updated_at': now.isoformat(),
    }


def main():
    results = [process_channel(cfg) for cfg in MY_CHANNELS]
    payload = {
        'channels': results,
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
    }
    write_js_var(OUT, 'MY_CHANNELS', payload)
    print(f'\n✅ 저장: {OUT}')
    for r in results:
        if r.get('error'):
            print(f'  ⚠️ {r["name"]}: {r["error"]}')
        else:
            print(f'  ✅ {r["name"]}: {len(r.get("videos", []))}편')


if __name__ == '__main__':
    main()
