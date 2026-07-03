"""공통 유틸 · GitHub Actions 환경용

OAuth 자격증명은 GitHub Secrets에서 환경변수로 주입된 JSON을 파싱해서 사용.
로컬 파일 (~/.config/autoworkers/tokens/*.json) 미사용.
"""
from __future__ import annotations
import json, os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent  # 저장소 루트
STATE_DIR = ROOT / 'state'
STATE_DIR.mkdir(exist_ok=True)


CHANNEL_TOKENS = {
    'knowledge-archive': 'YT_TOKEN_KNOWLEDGE_ARCHIVE',
    'economy-247': 'YT_TOKEN_ECONOMY_247',
    'redman-politics': 'YT_TOKEN_REDMAN_POLITICS',
}


def get_credentials(slug: str = 'knowledge-archive'):
    """환경변수에서 OAuth JSON을 읽어 Credentials 생성."""
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request

    env_name = CHANNEL_TOKENS.get(slug)
    if not env_name:
        raise ValueError(f'Unknown channel slug: {slug}')

    token_json = os.getenv(env_name)
    if not token_json:
        raise ValueError(f'Missing environment variable: {env_name}')

    try:
        info = json.loads(token_json)
    except json.JSONDecodeError as e:
        raise ValueError(f'{env_name} is not valid JSON: {e}')

    creds = Credentials.from_authorized_user_info(info)
    if not creds.valid:
        creds.refresh(Request())
    return creds


def get_yt_bearer(slug: str = 'knowledge-archive') -> str:
    """API 호출용 access token만 반환."""
    return get_credentials(slug).token


def send_telegram(text: str) -> bool:
    """텔레그램 메시지 전송. Markdown 실패 시 plain 재시도."""
    import requests
    tg_token = os.getenv('TELEGRAM_BOT_TOKEN', '')
    tg_chat = os.getenv('TELEGRAM_CHAT_ID', '')
    if not tg_token or not tg_chat:
        print('WARN: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID missing')
        return False

    api_url = f'https://api.telegram.org/bot{tg_token}/sendMessage'

    def _send(payload):
        try:
            r = requests.post(api_url, json=payload, timeout=15)
            if r.status_code == 200:
                return True
            # 자세한 실패 원인 출력
            body = r.text[:500]
            print(f'  텔레그램 HTTP {r.status_code} · body={body}')
            return False
        except Exception as e:
            print(f'  텔레그램 예외: {e}')
            return False

    # 1) Markdown 시도
    ok = _send({
        'chat_id': tg_chat,
        'text': text,
        'parse_mode': 'Markdown',
        'disable_web_page_preview': False,
    })
    if ok:
        return True

    # 2) 실패 시 plain 재시도
    print('  → plain 텍스트로 재시도')
    return _send({
        'chat_id': tg_chat,
        'text': text,
        'disable_web_page_preview': False,
    })


def load_json(path: Path, default=None):
    if path.exists():
        return json.loads(path.read_text(encoding='utf-8'))
    return default if default is not None else {}


def save_json(path: Path, data, indent: int = 2):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=indent), encoding='utf-8')


def write_js_var(path: Path, name: str, obj) -> None:
    """window.__NAME__ = {...};"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f'window.__{name}__ = {json.dumps(obj, ensure_ascii=False)};\n',
        encoding='utf-8',
    )
