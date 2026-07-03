"""텔레그램 다이제스트 발송 (Level 3)

주기: 매 12/18/22시 KST
로직:
  - state/alert_history.jsonl 읽어서 최근 6h 이벤트 요약
  - state/monitor_lite_state.json 에서 채널별 최근 폴링 상태 확인
  - 텔레그램에 1개 메시지 발송

사용:
  python monitor_scripts/build_digest.py [--window-hours 6]
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import Counter, defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, STATE_DIR, send_telegram


ALERT_HISTORY = STATE_DIR / 'alert_history.jsonl'
STATE_FILE = STATE_DIR / 'monitor_lite_state.json'


def load_history_recent(hours: int) -> list[dict]:
    """지난 N시간 내 알림 배치만 반환."""
    if not ALERT_HISTORY.exists():
        return []
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    batches = []
    with ALERT_HISTORY.open(encoding='utf-8') as f:
        for line in f:
            try:
                batch = json.loads(line)
                ts = datetime.fromisoformat(batch['batch_ts'])
                if ts >= cutoff:
                    batches.append(batch)
            except Exception:
                continue
    return batches


def summarize(batches: list[dict]) -> dict:
    total_alerts = 0
    counts_by_level = Counter()
    top_entries = []
    by_channel = defaultdict(int)

    for batch in batches:
        for entry in batch.get('entries', []):
            total_alerts += 1
            counts_by_level[entry.get('level', 'unknown')] += 1
            by_channel[entry.get('channel_name', '?')] += 1
            top_entries.append(entry)

    top_entries.sort(key=lambda e: -e.get('views', 0))
    return {
        'total_alerts': total_alerts,
        'by_level': dict(counts_by_level),
        'top': top_entries[:5],
        'batches': len(batches),
        'active_channels': dict(sorted(by_channel.items(), key=lambda x: -x[1])[:5]),
    }


def build_message(summary: dict, window_hours: int) -> str:
    now = datetime.now().strftime('%m/%d %H:%M')
    lines = [
        f'📊 *다이제스트 · 지난 {window_hours}h*',
        f'_{now} 기준_',
        '',
    ]

    if summary['total_alerts'] == 0:
        lines.append('신호 없음 (조용한 구간)')
        lines.append('')
        lines.append('👀 관찰만 있고 폭발·조기 시그널 미발생')
    else:
        by = summary['by_level']
        parts = []
        if by.get('super'): parts.append(f'🔥🔥 {by["super"]}')
        if by.get('explosion'): parts.append(f'🔥 {by["explosion"]}')
        if by.get('early'): parts.append(f'⚡ {by["early"]}')
        lines.append(f'*알림 {summary["total_alerts"]}건* · {" · ".join(parts)}')
        lines.append(f'배치 {summary["batches"]}회 · 활성 채널 {len(summary["active_channels"])}개')
        lines.append('')

        if summary['top']:
            lines.append('*🏆 TOP 5*')
            for i, e in enumerate(summary['top'], 1):
                title = e.get('title', '?')[:45].replace('*', '').replace('_', '')
                emoji = e.get('emoji', '·')
                views = e.get('views', 0)
                ch = e.get('channel_name', '?')
                lines.append(f'{i}. {emoji} {ch} · {views:,}뷰')
                lines.append(f'   {title}')
                lines.append(f'   {e.get("video_url", "")}')
            lines.append('')

        if summary['active_channels']:
            active = ' · '.join(f'{n}({c})' for n, c in list(summary['active_channels'].items())[:5])
            lines.append(f'*활성 채널*: {active}')

    lines.append('')
    lines.append('━━━━━━━━━━━━━━')
    lines.append('🔗 대시보드: https://arrange-yt-scanner.pages.dev/monitor/')

    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--window-hours', type=int, default=6)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    batches = load_history_recent(args.window_hours)
    summary = summarize(batches)
    msg = build_message(summary, args.window_hours)

    print(msg)
    print()

    if args.dry_run:
        print('[DRY RUN] 미전송')
        return

    ok = send_telegram(msg)
    print(f'📢 텔레그램 {"✅" if ok else "❌"}')


if __name__ == '__main__':
    main()
