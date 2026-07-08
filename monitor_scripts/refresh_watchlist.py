"""watchlist_economy_full.json 갱신 (GitHub Actions 버전)

각 채널의 최근 15편 stats + 기간별 TOP + avg_vph_baseline 계산
"""
from __future__ import annotations
import json, re, sys, requests
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, get_yt_bearer, save_json


WATCHLIST = ROOT / 'monitor_scripts/watchlist_economy.json'
OUT = ROOT / 'monitor_scripts/watchlist_economy_full.json'


def fetch_rss_vids(cid):
    try:
        r = requests.get(
            f'https://www.youtube.com/feeds/videos.xml?channel_id={cid}',
            headers={'User-Agent': 'Mozilla/5.0'}, timeout=15,
        )
        if r.status_code != 200:
            return []
        vids = []
        for m in re.finditer(r'<entry>(.*?)</entry>', r.text, re.DOTALL):
            b = m.group(1)
            vm = re.search(r'<yt:videoId>([^<]+)</yt:videoId>', b)
            if vm:
                vids.append(vm.group(1))
            if len(vids) >= 15:
                break
        return vids
    except Exception:
        return []


def fetch_video_stats(vids, token):
    out = {}
    for i in range(0, len(vids), 50):
        batch = vids[i:i+50]
        try:
            r = requests.get(
                'https://www.googleapis.com/youtube/v3/videos',
                params={'part': 'statistics,snippet',
                        'id': ','.join(batch), 'maxResults': 50},
                headers={'Authorization': f'Bearer {token}'}, timeout=30,
            )
            for item in r.json().get('items', []):
                st = item.get('statistics', {})
                sn = item.get('snippet', {})
                out[item['id']] = {
                    'title': sn.get('title', ''),
                    'views': int(st.get('viewCount', 0)),
                    'comments': int(st.get('commentCount', 0)),
                    'published': sn.get('publishedAt', ''),
                }
        except Exception as e:
            print(f'  WARN videos.list failed: {e}')
    return out


def main():
    watchlist = json.loads(WATCHLIST.read_text(encoding='utf-8'))
    print(f'📡 {len(watchlist)}채널 갱신 시작...')

    # 이전 데이터 로드 (RSS/API 실패 시 fallback)
    prev_data = {}
    if OUT.exists():
        try:
            prev_list = json.loads(OUT.read_text(encoding='utf-8'))
            prev_data = {c['cid']: c for c in prev_list}
        except Exception:
            pass

    token = get_yt_bearer('knowledge-archive')
    now = datetime.now(timezone.utc)

    # 1) RSS 병렬
    all_vids = []
    vid_by_ch = {}
    with ThreadPoolExecutor(max_workers=15) as ex:
        futs = {ex.submit(fetch_rss_vids, w['cid']): w['cid'] for w in watchlist}
        done = 0
        for fut in as_completed(futs):
            cid = futs[fut]
            vids = fut.result()
            vid_by_ch[cid] = vids
            all_vids.extend(vids)
            done += 1
            if done % 15 == 0:
                print(f'  RSS {done}/{len(watchlist)}')

    print(f'  총 {len(all_vids)}편 stats 조회...')
    stats = fetch_video_stats(all_vids, token)
    print(f'  {len(stats)}편 stats 수집')

    enriched = []
    fallback_count = 0
    for w in watchlist:
        cid = w['cid']
        ch_vids = []
        for vid in vid_by_ch.get(cid, []):
            s = stats.get(vid)
            if not s:
                continue
            try:
                pub = datetime.fromisoformat(s['published'].replace('Z', '+00:00'))
                days_ago = (now - pub).days
                hours_ago = (now - pub).total_seconds() / 3600
                date_str = pub.strftime('%m/%d')
            except Exception:
                continue
            ch_vids.append({
                'vid': vid, 'title': s['title'],
                'views': s['views'], 'comments': s['comments'],
                'days_ago': days_ago, 'hours_ago': hours_ago,
                'date_str': date_str,
                'url': f'https://youtu.be/{vid}',
            })

        # RSS/API 실패 시 이전 데이터 유지 (fallback)
        if not ch_vids:
            prev = prev_data.get(cid)
            if prev:
                merged = {**prev, **w, 'updated_at_fallback': now.isoformat()}
                enriched.append(merged)
                fallback_count += 1
                continue

        by_recent = sorted(ch_vids, key=lambda x: x['days_ago'])
        latest = by_recent[0] if by_recent else None

        v1 = [v for v in ch_vids if v['days_ago'] <= 1]
        v7 = [v for v in ch_vids if v['days_ago'] <= 7]
        v14 = [v for v in ch_vids if v['days_ago'] <= 14]
        v30 = [v for v in ch_vids if v['days_ago'] <= 30]

        top1 = max(v1, key=lambda x: x['views'], default=None)
        top7 = max(v7, key=lambda x: x['views'], default=None)
        top14 = max(v14, key=lambda x: x['views'], default=None)
        top30 = max(v30, key=lambda x: x['views'], default=None)

        def top5_avg(vs):
            if not vs:
                return 0
            sorted_views = sorted((v['views'] for v in vs), reverse=True)[:5]
            return int(sum(sorted_views) / len(sorted_views))

        # avg_vph_baseline: 최근 7일 성숙 영상 (24h 이상 지난 영상)의 median vph
        # 24h 이상 지난 영상은 대체로 초기 급등 지나서 안정 뷰
        mature = [v for v in v7 if v['hours_ago'] >= 24]
        if mature:
            vphs = sorted(v['views'] / v['hours_ago'] for v in mature)
            baseline_vph = int(vphs[len(vphs) // 2])
        else:
            # fallback: avg views over 24h
            baseline_vph = int(top5_avg(v7) / 24)

        enriched.append({
            **w,
            'latest_video': latest,
            'top1_video': top1, 'top7_video': top7,
            'top14_video': top14, 'top30_video': top30,
            'top5_1d': top5_avg(v1),
            'top5_7d': top5_avg(v7),
            'top5_14d': top5_avg(v14),
            'top5_30d': top5_avg(v30),
            'count_1d': len(v1),
            'count_7d': len(v7),
            'count_14d': len(v14),
            'count_30d': len(v30),
            'avg_vph_baseline': baseline_vph,
            'updated_at': now.isoformat(),
        })

    save_json(OUT, enriched)

    with_latest = sum(1 for e in enriched if e.get('latest_video'))
    with_top7 = sum(1 for e in enriched if e.get('top7_video'))
    print()
    print(f'✅ {OUT}')
    print(f'   {len(enriched)}채널 · 최근업로드 {with_latest} · '
          f'7일TOP {with_top7} · avg_vph 계산 완료')


if __name__ == '__main__':
    main()
