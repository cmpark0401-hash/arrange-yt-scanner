# 🎬 튜브해커

유튜브 폭발 감지 · 원조 추적 · 대본 작업 파이프라인.

## 페이지

- `/` — 홈 · 대시보드 요약
- `/channels.html` — 감시 채널 리스트 (S 12 + A 42)
- `/alerts.html` — 실시간 폭발 알림
- `/topics.html` — 주제 클러스터 (25개 파이)
- `/reports.html` — 일일 리포트

## 데이터 갱신

```bash
# 1. 채널 데이터 갱신
.venv/bin/python scripts/mece/refresh_watchlist.py

# 2. 사이트 빌드
.venv/bin/python scripts/mece/build_tubehacker_site.py

# 3. git push (Cloudflare Pages 자동 배포)
git add tubehacker-site/
git commit -m "data refresh"
git push
```

## Cloudflare Pages 설정

- Repository: `tubehacker-site/` 디렉토리
- Build command: (없음 · 정적 HTML)
- Build output directory: `/`
- Domain: `tubehacker.pages.dev` (기본) 또는 커스텀

## 로컬 미리보기

```bash
# 방법 1: 정적 서버
cd tubehacker-site
python3 -m http.server 8080
# → http://localhost:8080

# 방법 2: 파일 직접 열기
open tubehacker-site/index.html
```
