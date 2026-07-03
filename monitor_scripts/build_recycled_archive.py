"""6개월~2년 전 폭발 영상 아카이브 · 재활용 후보 발굴 (GitHub Actions 버전)

주기: 매주 일요일
출력:
  monitor_scripts/recycled_archive.json  (전체)
  monitor/assets/data/recycled.js        (사이트 임베드)
"""
from __future__ import annotations
import json, sys, requests
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, get_yt_bearer, save_json, write_js_var


WATCHLIST = ROOT / 'monitor_scripts/watchlist_economy.json'
ARCHIVE = ROOT / 'monitor_scripts/recycled_archive.json'
JS_OUT = ROOT / 'monitor/assets/data/recycled.js'


def fetch_all_uploads(cid, token, max_videos=800):
    r = requests.get(
        'https://www.googleapis.com/youtube/v3/channels',
        params={'part': 'contentDetails', 'id': cid},
        headers={'Authorization': f'Bearer {token}'}, timeout=15,
    )
    items = r.json().get('items', [])
    if not items:
        return []
    playlist_id = items[0]['contentDetails']['relatedPlaylists']['uploads']

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
    return vids


def fetch_video_stats(vids, token):
    result = {}
    for i in range(0, len(vids), 50):
        batch = vids[i:i+50]
        r = requests.get(
            'https://www.googleapis.com/youtube/v3/videos',
            params={'part': 'snippet,statistics',
                    'id': ','.join(batch), 'maxResults': 50},
            headers={'Authorization': f'Bearer {token}'}, timeout=30,
        )
        for item in r.json().get('items', []):
            st = item.get('statistics', {})
            sn = item.get('snippet', {})
            result[item['id']] = {
                'title': sn.get('title', ''),
                'published': sn.get('publishedAt', ''),
                'views': int(st.get('viewCount', 0)),
                'likes': int(st.get('likeCount', 0)),
                'comments': int(st.get('commentCount', 0)),
            }
    return result


CATEGORIES = {
    '방송/미디어 몰락': ['방송국', '방송사', 'JTBC', 'MBC', 'KBS', 'SBS', '중앙그룹', '중앙일보'],
    '한일 역전': ['일본', '독점', '뒤집힌', '한국 대반격', '수출통제', '박살'],
    '한국 국산화': ['국산화', '독자 개발', '한국이 뚫은', '해저터널', '조선업', '원전'],
    '해외 인프라·수주': ['인도네시아', '고속철', '고속철도', '베트남', '사우디', '해외 수주', '수출', '해외 진출', '동남아'],
    '중국 몰락': ['중국 지하철', '중국 아파트', '중국 자본', '중국 몰락', '위안화'],
    '엔비디아·AI': ['엔비디아', 'HBM', '젠슨황', 'AI 반도체', '피지컬 AI'],
    '삼성 스토리': ['이재용', '삼성전자', '삼성 반도체', '삼성 카르텔'],
    'LG·현대·SK': ['현대차', 'SK하이닉스', 'LG', '구광모', '정의선'],
    '부동산·아파트': ['아파트', '부동산', '재건축', '엘시티', '한남더힐', '반포자이'],
    '자원·에너지': ['희토류', '텅스텐', '리튬', '광물'],
    '재벌·인물 몰락': ['정몽규', '재벌', '그룹 회장', '2세 3세', '몰락'],
    '경제 원리·구조': ['경제학', '금리', '환율', '통화', '인플레'],
    '트럼프·글로벌': ['트럼프', '관세', '무역전쟁', '미국 대선'],
}


def categorize(title):
    t = title.lower()
    for cat, kws in CATEGORIES.items():
        if any(kw.lower() in t for kw in kws):
            return cat
    return '(기타)'


def build_archive():
    watchlist = json.loads(WATCHLIST.read_text(encoding='utf-8'))
    token = get_yt_bearer('knowledge-archive')
    now = datetime.now(timezone.utc)

    MIN_AGE_DAYS = 180
    MAX_AGE_DAYS = 730

    print(f'📚 {len(watchlist)}채널의 6~24개월 전 폭발 영상 발굴')
    all_candidates = []

    def process_channel(w):
        cid = w['cid']
        avg_views = w.get('avg_views', 0)
        subs = w.get('subs', 0)

        vids = fetch_all_uploads(cid, token, max_videos=800)
        if not vids:
            return []
        stats = fetch_video_stats(vids, token)

        all_views = [s['views'] for s in stats.values() if s.get('views', 0) > 0]
        if not all_views:
            return []
        historical_median = sorted(all_views)[len(all_views) // 2] if all_views else 0
        baseline = max(avg_views, int(historical_median))

        if subs >= 100000:
            min_eff, min_views = 1.3, 200000
        elif subs >= 30000:
            min_eff, min_views = 2.0, 100000
        else:
            min_eff, min_views = 3.0, 30000

        candidates = []
        for vid, s in stats.items():
            try:
                pub = datetime.fromisoformat(s['published'].replace('Z', '+00:00'))
                days_ago = (now - pub).days
            except Exception:
                continue
            if days_ago < MIN_AGE_DAYS or days_ago > MAX_AGE_DAYS:
                continue
            views = s['views']
            eff = views / baseline if baseline else 0
            if eff < min_eff:
                continue
            if views < min_views:
                continue

            candidates.append({
                'vid': vid, 'title': s['title'],
                'channel_name': w['name'], 'channel_cid': cid,
                'channel_tier': w['tier'],
                'channel_subs': w.get('subs', 0),
                'channel_avg_views': avg_views,
                'views': views,
                'likes': s['likes'], 'comments': s['comments'],
                'comment_ratio_pct': round(s['comments']/views*100, 3) if views else 0,
                'published': s['published'][:10],
                'days_ago': days_ago,
                'months_ago': round(days_ago / 30, 1),
                'efficiency': round(eff, 1),
                'category': categorize(s['title']),
                'url': f'https://youtu.be/{vid}',
                'thumbnail': f'https://i.ytimg.com/vi/{vid}/mqdefault.jpg',
            })
        return candidates

    done = 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(process_channel, w): w['name'] for w in watchlist}
        for fut in as_completed(futs):
            name = futs[fut]
            try:
                cands = fut.result()
                all_candidates.extend(cands)
                done += 1
                if done % 5 == 0 or cands:
                    print(f'  [{done}/{len(watchlist)}] {name[:15]:15s} · {len(cands)}편 발굴')
            except Exception as e:
                print(f'  WARN {name}: {e}')

    payload = {
        'built_at': now.isoformat(),
        'built_local': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'total': len(all_candidates),
        'candidates': sorted(all_candidates, key=lambda x: -x['views']),
    }
    save_json(ARCHIVE, payload)
    write_js_var(JS_OUT, 'RECYCLED', payload)

    by_cat = Counter(c['category'] for c in all_candidates)
    print(f'\n✅ 총 {len(all_candidates)}편')
    for cat, n in by_cat.most_common():
        print(f'  {cat[:20]:20s} · {n:>3}편')


if __name__ == '__main__':
    build_archive()
