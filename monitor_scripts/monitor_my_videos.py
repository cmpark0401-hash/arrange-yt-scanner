"""내 채널 신작 24시간 이내 노출 저하 감지 (썸네일 교체 알림)

로직 (매뉴얼 기준):
  1. 지식록·247·레드맨 3채널 최근 30편 조회
  2. 발행 후 24시간 이내 영상만 필터
  3. 임계 판정:
     - 발행 20h+ · 뷰 < 100 → 🔴 즉시 교체 알림
     - 발행 12h+ · 뷰 < 50 → 🟠 위험 (준비 알림)
     - 발행  6h+ · 뷰 < 30 → 🟡 관망 알림
  4. 알림 중복 방지 (state에 vid 기록)
  5. 텔레그램 발송

매시간 GitHub Actions로 실행.
"""
from __future__ import annotations
import argparse, json, sys, requests
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, STATE_DIR, get_credentials, send_telegram, load_json, save_json


ALERT_STATE = STATE_DIR / 'my_video_alerts.json'


CHANNELS = [
    {'slug': 'knowledge-archive', 'name': '지식록', 'emoji': '📈'},
    {'slug': 'economy-247', 'name': '247경제', 'emoji': '💹'},
    {'slug': 'redman-economy', 'name': '레드맨', 'emoji': '🇰🇷'},
]


def fetch_recent_videos(token: str, playlist_id: str, max_videos: int = 5) -> list[str]:
    vids = []
    r = requests.get(
        'https://www.googleapis.com/youtube/v3/playlistItems',
        params={'part': 'contentDetails', 'playlistId': playlist_id, 'maxResults': max_videos},
        headers={'Authorization': f'Bearer {token}'}, timeout=15,
    )
    for item in r.json().get('items', []):
        vids.append(item['contentDetails']['videoId'])
    return vids


def fetch_video_stats(token: str, vids: list[str]) -> dict:
    if not vids:
        return {}
    r = requests.get(
        'https://www.googleapis.com/youtube/v3/videos',
        params={'part': 'snippet,statistics', 'id': ','.join(vids)},
        headers={'Authorization': f'Bearer {token}'}, timeout=15,
    )
    result = {}
    for item in r.json().get('items', []):
        st = item.get('statistics', {})
        sn = item.get('snippet', {})
        result[item['id']] = {
            'title': sn.get('title', ''),
            'published': sn.get('publishedAt', ''),
            'views': int(st.get('viewCount', 0)),
        }
    return result


def get_channel_info(token: str) -> dict:
    r = requests.get(
        'https://www.googleapis.com/youtube/v3/channels',
        params={'part': 'contentDetails,snippet', 'mine': 'true'},
        headers={'Authorization': f'Bearer {token}'}, timeout=15,
    )
    items = r.json().get('items', [])
    if not items:
        return {}
    ch = items[0]
    return {
        'uploads': ch['contentDetails']['relatedPlaylists']['uploads'],
        'title': ch['snippet']['title'],
    }


def classify(views: int, hours: float) -> tuple[str, str, str]:
    """(level, emoji, message) 반환. level 'skip' = 알림 X"""
    if hours < 6:
        return 'skip', '', ''
    if hours >= 20 and views < 100:
        return 'red', '🔴', '20시간 · 뷰 100미만 · 즉시 썸네일 교체 필요'
    if hours >= 12 and views < 50:
        return 'orange', '🟠', '12시간 · 뷰 50미만 · 위험 · B안 준비'
    if hours >= 6 and views < 30:
        return 'yellow', '🟡', '6시간 · 뷰 30미만 · 관망 · 추이 지켜보세요'
    return 'skip', '', ''


def build_message(entries: list[dict]) -> str:
    entries.sort(key=lambda x: {'red': 0, 'orange': 1, 'yellow': 2}.get(x['level'], 9))
    header_emoji = entries[0]['emoji']
    lines = [
        f'{header_emoji} *썸네일 교체 알림 · {len(entries)}편*',
        f'_{datetime.now().strftime("%m/%d %H:%M")} · 매뉴얼 기준 감지_',
        '',
    ]
    for e in entries:
        lines.append(f'{e["emoji"]} *{e["channel_name"]}*')
        lines.append(f'📌 {e["title"][:60]}')
        lines.append(f'📊 발행 {e["hours"]:.0f}시간 · {e["views"]}뷰')
        lines.append(f'⚡ {e["msg"]}')
        lines.append(f'🔗 https://youtu.be/{e["vid"]}')
        lines.append('')
    lines.append('━━━━━━━━━━━━━━')
    lines.append('💡 매뉴얼 (24시간 스와프 전략):')
    lines.append('  1. output/thumbnails/prompts.json 확인')
    lines.append('  2. B안(변형) 준비 · 스튜디오 → 썸네일 교체')
    lines.append('  3. 알고리즘 재인식 유도')
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    alerted = load_json(ALERT_STATE, {'sent': []})
    already_sent = set(alerted.get('sent', []))
    now = datetime.now(timezone.utc)

    all_alerts = []
    for ch in CHANNELS:
        try:
            creds = get_credentials(ch['slug'])
            token = creds.token
            info = get_channel_info(token)
            if not info:
                print(f'⚠️ {ch["name"]}: 채널 정보 없음')
                continue
            vids = fetch_recent_videos(token, info['uploads'], max_videos=5)
            stats = fetch_video_stats(token, vids)

            for vid, s in stats.items():
                if not s.get('published'):
                    continue
                pub = datetime.fromisoformat(s['published'].replace('Z', '+00:00'))
                hours = (now - pub).total_seconds() / 3600
                # 24시간 이내만
                if hours >= 30:
                    continue
                level, emoji, msg = classify(s['views'], hours)
                if level == 'skip':
                    continue
                # 이미 red 알림 보낸 vid는 스킵 (중복 방지)
                key = f'{vid}:{level}'
                if key in already_sent:
                    continue
                all_alerts.append({
                    'level': level, 'emoji': emoji, 'msg': msg,
                    'vid': vid, 'title': s['title'],
                    'views': s['views'], 'hours': hours,
                    'channel_name': f'{ch["emoji"]} {ch["name"]}',
                })
                already_sent.add(key)
                print(f'  {emoji} {ch["name"]}: {s["title"][:40]} · {s["views"]}뷰 · {hours:.1f}h')
        except Exception as e:
            print(f'⚠️ {ch["name"]}: {e}')

    if not all_alerts:
        print('✅ 임계 도달 영상 없음 · 모든 신작 정상')
        return

    msg = build_message(all_alerts)
    print()
    print(msg)
    print()
    if not args.dry_run:
        ok = send_telegram(msg)
        print(f'📢 텔레그램 {"✅" if ok else "❌"}')
        # state 저장 (중복 방지)
        save_json(ALERT_STATE, {
            'sent': sorted(already_sent),
            'updated_at': now.isoformat(),
        })


if __name__ == '__main__':
    main()
