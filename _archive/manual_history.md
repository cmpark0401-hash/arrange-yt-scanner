## 📜 튜브해커 개발 히스토리

<details style="margin:16px 0;border:1px solid var(--border);border-radius:10px;padding:14px 18px;background:var(--surface);">
<summary style="cursor:pointer;font-weight:700;color:var(--primary-hi);font-size:14px;">▶ 펼쳐서 보기 — 2주간의 빌드 여정</summary>

<div style="margin-top:18px;color:var(--text2);font-size:13px;line-height:1.6;">

거의 빈 화면에서 시작해 매일 새 페이지/기능이 쌓였습니다. 클코(Claude Code)와 함께 만든 2주간의 흔적.

<div style="display:grid;gap:14px;margin-top:18px;">

<div style="border-left:3px solid var(--text3);padding-left:14px;">
<div style="font-size:11px;color:var(--text3);font-weight:700;">2026-05-27 (수요일) · 시작</div>
<div style="font-weight:700;color:var(--text);margin-top:2px;">🌱 초기 빌드 — Day 0</div>
<ul style="margin:6px 0;padding-left:20px;">
<li>대시보드 첫 빌드 — "어레인지 유튜브 스캐너"</li>
<li>카테고리·형식(롱폼/쇼츠) 분류 시작</li>
<li>7일 트렌드 차트</li>
</ul>
<div class="mock">
  <div class="mock-header">
    <span class="mock-brand">어레인지 유튜브 스캐너</span>
    <span class="mock-slogan">· v0.1 초기 빌드</span>
  </div>
  <div class="mock-tabs">
    <span class="mock-tab on">📊 대시보드</span>
  </div>
  <div class="mock-card">
    <span class="mock-ch-name">채널A</span>
    <div class="mock-meta-line">구독 100만 · 카테고리: 지식 · 형식: 롱폼</div>
    <div style="font-size:10px;color:var(--text3);margin-top:6px;">📈 7일 트렌드 차트 영역</div>
  </div>
</div>
</div>

<div style="border-left:3px solid var(--text3);padding-left:14px;">
<div style="font-size:11px;color:var(--text3);font-weight:700;">2026-05-28 (목요일)</div>
<div style="font-weight:700;color:var(--text);margin-top:2px;">🎨 UI 정비 — Pint급 대시보드</div>
<ul style="margin:6px 0;padding-left:20px;">
<li>채널 카드 UI 본격화 — 👑 1·2·3위 / ▲ 등락</li>
<li>형식 토글 + 대형 제외 + 검색 박스</li>
<li>🔬 과학 트렌드 페이지 신설</li>
</ul>
<div class="mock">
  <div class="mock-header">
    <span class="mock-brand">어레인지 유튜브 스캐너</span>
    <span class="mock-slogan">· Pint급 UI</span>
  </div>
  <div class="mock-tabs">
    <span class="mock-tab on">📊 대시보드</span>
    <span class="mock-tab">🔬 과학 트렌드</span>
  </div>
  <div style="font-size:10px;color:var(--text3);margin:6px 0;">[🔘 롱폼] [🔘 쇼츠] [☑ 대형 제외] [🔍 검색...]</div>
  <div class="mock-card crown">
    <span class="mock-rank-badge">👑 #1</span>
    <span class="mock-ch-name">채널A</span>
    <span class="mock-delta">▲3</span>
    <div class="mock-meta-line">구독 384만 · 지식</div>
  </div>
  <div class="mock-card">
    <span class="mock-rank-badge" style="background:#c0c0c0;">#2</span>
    <span class="mock-ch-name">채널B</span>
    <span class="mock-delta" style="color:var(--down);">▼1</span>
  </div>
</div>
</div>

<div style="border-left:3px solid var(--warn);padding-left:14px;">
<div style="font-size:11px;color:var(--warn);font-weight:700;">2026-05-29 (금요일) · 폭발적 확장</div>
<div style="font-weight:700;color:var(--text);margin-top:2px;">🚀 검증 주제 엔진 + 일본 확장 + SPA</div>
<ul style="margin:6px 0;padding-left:20px;">
<li>🎯 <b>오늘 만들 주제</b> 추천 보드 신설 (채널별 + 카테고리별)</li>
<li>🔥 <b>Hot키워드</b> — 검증 주제 누적 아카이브 + 씨앗 검색</li>
<li>🇯🇵 <b>일본 대시보드 /jp/</b> — Gemini 한국어 번역 병기</li>
<li>📰 카테고리별 뉴스 헤드라인 (구글 뉴스 RSS)</li>
<li>📅 일일 리포트 클린 테이블</li>
<li>SPA 셸(핀트식) — 헤더+탭 고정, 탭별 lazy fetch</li>
</ul>
<div class="mock">
  <div class="mock-header">
    <span style="font-size:18px;">🇰🇷</span>
    <span class="mock-brand">TubeHacker</span>
    <span class="mock-slogan">· by arrange · SPA 셸 도입</span>
    <div class="mock-chips">
      <span class="mock-chip warn">🚨 <b>9</b></span>
      <span class="mock-chip hot">🔥 <b>150</b></span>
      <span class="mock-chip">🆕 65</span>
      <span class="mock-chip" style="background:#fff;color:#000;">🇯🇵 JP</span>
    </div>
  </div>
  <div class="mock-tabs">
    <span class="mock-tab on">🏠 대시보드</span>
    <span class="mock-tab">🎯 오늘의 주제</span>
    <span class="mock-tab">🔥 Hot키워드</span>
    <span class="mock-tab">🔬 과학</span>
    <span class="mock-tab">📰 뉴스</span>
    <span class="mock-tab">📅 일별</span>
  </div>
  <div style="font-size:10px;color:var(--text3);margin-top:6px;">⚡ SPA — 탭 클릭 = lazy fetch (페이지 새로고침 X)</div>
</div>
</div>

<div style="border-left:3px solid var(--hot);padding-left:14px;">
<div style="font-size:11px;color:var(--hot);font-weight:700;">2026-05-30 (토요일)</div>
<div style="font-weight:700;color:var(--text);margin-top:2px;">🎙️ 시니어랩 (야담 워크플로)</div>
<ul style="margin:6px 0;padding-left:20px;">
<li>야담 카테고리 전용 watch list 10채널</li>
<li>5종 분석 (벤치마크·제목패턴·교차변환·신규채널·사료가이드)</li>
<li>활성도 필터 + 채널별 역대 TOP 분석</li>
</ul>
<div class="mock">
  <div class="mock-header">
    <span style="font-size:18px;">🇰🇷</span>
    <span class="mock-brand">TubeHacker</span>
    <div class="mock-chips">
      <span class="mock-chip warn">🚨 <b>9</b></span>
      <span class="mock-chip hot">🔥 <b>150</b></span>
      <span class="mock-chip">🆕 65</span>
      <span class="mock-chip" style="background:#fff;color:#000;">🇯🇵 JP</span>
    </div>
  </div>
  <div class="mock-tabs">
    <span class="mock-tab">🏠 대시보드</span>
    <span class="mock-tab">🎯 오늘의 주제</span>
    <span class="mock-tab">🔥 Hot키워드</span>
    <span class="mock-tab">🔬 과학</span>
    <span class="mock-tab on" style="background:#ff7a45;border-color:#ff7a45;">🎙️ 시니어랩 NEW</span>
    <span class="mock-tab">📰 뉴스</span>
    <span class="mock-tab">📅 일별</span>
  </div>
  <div class="mock-card">
    <div style="font-size:11px;font-weight:700;color:var(--hot);">🎙️ 야담 watch list · 10채널</div>
    <div style="font-size:10px;color:var(--text2);margin-top:4px;">[벤치마크] [제목패턴] [교차변환] [신규채널] [사료가이드]</div>
  </div>
</div>
</div>

<div style="border-left:3px solid var(--info);padding-left:14px;">
<div style="font-size:11px;color:var(--info);font-weight:700;">2026-05-31 (일요일)</div>
<div style="font-weight:700;color:var(--text);margin-top:2px;">🏆 패턴 라이브러리 + Autopsy + 가이드 1차</div>
<ul style="margin:6px 0;padding-left:20px;">
<li>🏆 <b>패턴 라이브러리</b> — 썸네일 60·제목 공식·Hook 풀 32</li>
<li>🔥 <b>왜 이 영상은 터졌는가?</b> (Autopsy) — URL 던지면 분해</li>
<li>📖 <b>사용 가이드 페이지</b> 1차 — 메트릭 사전 + FAQ</li>
<li>LLM 썸네일 분석 72편 (Claude API)</li>
<li>favicon (보라 T) + 페이지별 title</li>
</ul>
<div class="mock">
  <div class="mock-header">
    <span style="font-size:18px;">🇰🇷</span>
    <span class="mock-brand">TubeHacker</span>
    <span class="mock-slogan">· 알고리즘 해킹의 모든 것</span>
    <div class="mock-chips">
      <span class="mock-chip warn">🚨 <b>9</b></span>
      <span class="mock-chip hot">🔥 <b>150</b></span>
      <span class="mock-chip">🆕 65</span>
      <span class="mock-chip" style="background:#fff;color:#000;">🇯🇵 JP</span>
    </div>
  </div>
  <div class="mock-tabs">
    <span class="mock-tab on">🏠 대시보드</span>
    <span class="mock-tab">🎯 오늘의 주제</span>
    <span class="mock-tab">🔥 Hot</span>
    <span class="mock-tab">🔬 과학</span>
    <span class="mock-tab">🎙️ 시니어랩</span>
    <span class="mock-tab" style="background:#a855f7;color:#fff;border-color:#a855f7;">🔥 왜 터졌나? NEW</span>
    <span class="mock-tab" style="background:#a855f7;color:#fff;border-color:#a855f7;">🏆 패턴 NEW</span>
    <span class="mock-tab" style="background:#a855f7;color:#fff;border-color:#a855f7;">📖 가이드 NEW</span>
  </div>
  <div class="mock-card">
    <div style="font-size:11px;font-weight:700;color:var(--info);">🔥 Autopsy — URL 던지기 분석</div>
    <div style="font-size:10px;color:var(--text3);margin-top:4px;font-family:monospace;background:var(--bg);padding:5px;border-radius:4px;">https://youtube.com/watch?v=...</div>
    <div style="font-size:10px;color:var(--text2);margin-top:4px;">→ Hook 분해 · 구조 · 단조도 · 썸네일 OCR · Claude 대본</div>
  </div>
</div>
</div>

<div style="border-left:3px solid var(--primary);padding-left:14px;background:var(--primary-bg);padding:12px 14px;border-radius:8px;">
<div style="font-size:11px;color:var(--primary-hi);font-weight:700;">2026-06-01 (월요일) · 현재</div>
<div style="font-weight:700;color:var(--text);margin-top:2px;">✨ 시각화 + 반자동 채널 관리</div>
<ul style="margin:6px 0;padding-left:20px;">
<li>📖 <b>가이드 시각화</b> — 미니어처 UI · 인포카드 · 흐름 다이어그램 · 비교박스</li>
<li>🤖 <b>클코 자동화 가이드</b> 섹션</li>
<li>🔄 <b>분석 업데이트</b> 페이지 — 추적 87 + 신규 후보 264, 일괄 추가/해제</li>
<li>🔔 nav 알림 배지 (오늘의 주제 / 뉴스 모니터링 빨간 펄스)</li>
<li>🏠 로고 클릭 = 홈 + 새로고침</li>
<li>📂 카테고리 필터 + 50개 페이지네이션 (두 탭 모두)</li>
<li>헤더 chip 시그널/폭발/24h 클릭 = 대시보드</li>
<li>분석영상/분석채널/추적 3-카운터 정의</li>
</ul>
<div class="mock" style="border-color:var(--primary);">
  <div class="mock-header">
    <span style="font-size:18px;">🇰🇷</span>
    <span class="mock-brand">TubeHacker</span>
    <span class="mock-slogan">· 유튜브 알고리즘 해킹의 모든 것</span>
    <div class="mock-chips">
      <span class="mock-chip warn">🚨 <b>10</b></span>
      <span class="mock-chip hot">🔥 <b>159</b></span>
      <span class="mock-chip" style="background:var(--primary-bg);color:var(--primary-hi);border-color:var(--primary-bd);">🆕 <b>14</b></span>
      <span class="mock-chip" style="background:rgba(34,197,94,.13);color:#22c55e;border-color:rgba(34,197,94,.55);font-weight:700;">📡 <b style="color:#22c55e;">264</b></span>
      <span class="mock-chip" style="background:#fff;color:#000;">📖 가이드</span>
      <span class="mock-chip" style="background:#fff;color:#000;">📅 일별</span>
      <span class="mock-chip" style="background:linear-gradient(135deg,#fff,#fff5f5);color:#000;border:1.5px solid #ff4d4f;font-weight:800;">🇯🇵 JP</span>
    </div>
  </div>
  <div class="mock-tabs">
    <span class="mock-tab on" style="position:relative;">🎯 오늘의 주제 <span style="position:absolute;top:-5px;right:-5px;background:#ef4444;color:#fff;border-radius:50%;width:14px;height:14px;font-size:9px;line-height:14px;text-align:center;font-weight:800;">7</span></span>
    <span class="mock-tab" style="position:relative;">📰 뉴스 모니터링 <span style="position:absolute;top:-5px;right:-5px;background:#ef4444;color:#fff;border-radius:50%;width:14px;height:14px;font-size:9px;line-height:14px;text-align:center;font-weight:800;">3</span></span>
    <span class="mock-tab">🔥 Hot</span>
    <span class="mock-tab">🔬 과학</span>
    <span class="mock-tab">🎙️ 시니어랩</span>
    <span class="mock-tab">🔥 Autopsy</span>
    <span class="mock-tab">🏆 패턴</span>
  </div>
  <div class="mock-card crown">
    <span class="mock-rank-badge">👑 #1</span>
    <span class="mock-ch-name">지식인사이드</span>
    <span class="mock-delta">▲5</span>
    <div class="mock-meta-line">구독 384만 · 21년 8월 개설 · 4년 9개월차</div>
    <div class="mock-stats-row">
      <div class="mock-stat sig"><b>3</b>🚨 시그널</div>
      <div class="mock-stat hot"><b>5</b>🔥 폭발</div>
      <div class="mock-stat"><b>1</b>🆕 24h</div>
    </div>
  </div>
</div>
</div>

</div>

<div style="margin-top:20px;padding:12px;background:var(--surface);border:1px solid var(--border);border-radius:8px;font-size:12px;color:var(--text2);">
<b style="color:var(--text);">📊 2주 누적</b>: 페이지 9개 · 채널 추적 87 · 분석 영상 N편 · 일본 대시보드 별도 운영 · LLM 썸네일 분석 통합
</div>

</div>
</details>

---
