# 📖 TubeHacker 사용 가이드

**유튜브 알고리즘 해킹의 모든 것** — 발견 → 검증 → 청사진 → 제작까지 한 사이클.

<div class="tldr">
<div class="tldr-title">⚡ 한 줄 요약 (3가지)</div>
<div class="tldr-body">
✅ <b>오늘 만들 영상 주제·구조·어휘</b>를 데이터 기반으로 추천<br>
✅ <b>YouTube URL을 던지면</b> 자막 분해 → Hook/구조/단조도 자동 분석<br>
✅ 분석 결과 → <b>Claude Code에 한 번에 전달</b> → 대본 자동 생성
</div>
</div>

---

## 🚀 처음 사용자를 위한 3분 가이드

<div class="steps">
  <div class="step hot">
    <span class="step-num">STEP 1</span>
    <div class="step-title">🏠 대시보드 홈 보기</div>
    <div class="step-body">상단 칩 3개로 오늘 분위기 파악 — 🚨 시그널 · 🔥 폭발 · 🆕 24h</div>
  </div>
  <div class="step">
    <span class="step-num">STEP 2</span>
    <div class="step-title">📂 우리 카테고리 찾기</div>
    <div class="step-body">카테고리 탭 클릭 → 👑 1·2·3위 채널 카드의 인기 영상 확인</div>
  </div>
  <div class="step warn">
    <span class="step-num">STEP 3</span>
    <div class="step-title">🎯 만들 주제 정하기</div>
    <div class="step-body">오늘의 주제 탭에서 🔥 재편집 재폭발 카드 → 주제 선택</div>
  </div>
</div>

---

<details class="auto-guide">
<summary>🤖 클코 자동화 가이드</summary>
<div class="auto-body">

<div class="tldr">
<div class="tldr-title">⚡ 한 줄 요약</div>
<div class="tldr-body">
Claude Code에 <code>"OOO 채널 주제 찾아서 대본 만들어줘"</code> 한마디 → <b>TubeHacker 데이터 자동 분석 → 주제 추천 → 사용자 선택 → 대본 작업</b>까지 자동.
</div>
</div>

<h3>🎬 시나리오 1: 채널이 이미 있을 때</h3>

<div class="action-flow">

<div class="action-row">
<div class="action-actor user"><span class="who">👤 사용자</span>명령</div>
<div class="action-arrow">→</div>
<div class="action-body">
<span class="step-name">한 줄 명령</span>
<code>"잘듣네 채널 주제 찾아서 대본 만들어줘"</code>
</div>
</div>

<div class="action-row">
<div class="action-actor claude"><span class="who">🤖 Claude</span>자동</div>
<div class="action-arrow">⤵</div>
<div class="action-body">
<span class="step-name">📂 채널 컨텍스트 파악</span>
<ul>
<li><code>channels/jaldeunne/config/profile.md</code> — 채널 톤·카테고리</li>
<li><code>channels/jaldeunne/config/thumbnail-strategy.json</code> — 썸네일 전략</li>
</ul>
</div>
</div>

<div class="action-row">
<div class="action-actor claude"><span class="who">🤖 Claude</span>자동</div>
<div class="action-arrow">⤵</div>
<div class="action-body">
<span class="step-name">📊 TubeHacker 데이터 조회</span>
<ul>
<li>검증 주제 아카이브 (오래 검증된 주제)</li>
<li>오늘 폭발 주제 + 재편집 시그널</li>
<li>패턴 라이브러리 (제목 공식·Hook 풀)</li>
<li>시니어랩 corpus (해당 카테고리면)</li>
</ul>
</div>
</div>

<div class="action-row">
<div class="action-actor claude"><span class="who">🤖 Claude</span>제안</div>
<div class="action-arrow">⤵</div>
<div class="action-body">
<span class="step-name">🎯 주제 3~5개 추천 + 학습 영상</span>
<ul>
<li>1. 효·가족: "어머니 시한부..." (효율 6.2x · 학습 영상 3편)</li>
<li>2. 권선징악: "사기당한 노부부..." (효율 5.8x)</li>
<li>3. 혼인·치정: "신혼 첫날밤..." (효율 5.5x)</li>
</ul>
</div>
</div>

<div class="action-row">
<div class="action-actor user"><span class="who">👤 사용자</span>선택</div>
<div class="action-arrow">→</div>
<div class="action-body">
<span class="step-name">주제 선택</span>
<code>"2번으로 가자"</code>
</div>
</div>

<div class="action-row">
<div class="action-actor claude"><span class="who">🤖 Claude</span>자동</div>
<div class="action-arrow">⤵</div>
<div class="action-body">
<span class="step-name">📝 script-pd 스킬 자동 진입</span>
<ul>
<li>레퍼런스 영상 자동 수집 + 분석</li>
<li>패턴 라이브러리 인사이트 자동 주입</li>
<li>전략·아우트라인·드래프트 작성</li>
</ul>
</div>
</div>

<div class="action-row">
<div class="action-actor user"><span class="who">👤 사용자</span>결정</div>
<div class="action-arrow">→</div>
<div class="action-body">
<span class="step-name">중간 결정 2~3회</span>
<ul>
<li>Hook 3후보 중 선택</li>
<li>컨셉 확정</li>
<li>최종 검토 OK</li>
</ul>
</div>
</div>

<div class="action-row">
<div class="action-actor system"><span class="who">📄 산출</span>완료</div>
<div class="action-arrow">✅</div>
<div class="action-body">
<span class="step-name">최종 산출물</span>
<ul>
<li><code>{project}_script.txt</code> — TTS·영상 제작 가능</li>
<li><code>youtube.md</code> — 제목·설명·태그</li>
<li><code>thumbnails/prompts.json</code> — 썸네일 AI 프롬프트</li>
<li><code>sources.md</code> — 출처 타임라인</li>
</ul>
</div>
</div>

</div>

<h3>🆕 시나리오 2: 채널이 아직 없을 때 (예: 새 야담 채널)</h3>

<div class="action-flow">

<div class="action-row">
<div class="action-actor user"><span class="who">👤 사용자</span>명령</div>
<div class="action-arrow">→</div>
<div class="action-body">
<code>"새 야담 채널 만들어서 첫 영상 대본 만들어줘"</code>
</div>
</div>

<div class="action-row">
<div class="action-actor claude"><span class="who">🤖 Claude</span>자동</div>
<div class="action-arrow">⤵</div>
<div class="action-body">
<span class="step-name">🔧 channel-setup 스킬 진입</span>
<ul>
<li><code>channels/_shared_corpus/yadam/BRIEF.md</code> 자동 로드</li>
<li>벤치마크 분석 단계 자동 스킵 (이미 28편 corpus 있음)</li>
</ul>
</div>
</div>

<div class="action-row">
<div class="action-actor claude"><span class="who">🤖 Claude</span>질문</div>
<div class="action-arrow">⤵</div>
<div class="action-body">
<span class="step-name">최소 질문 2~3개</span>
<ul>
<li>채널 이름 (예: 야담의 향기)</li>
<li>세부 톤 (낭독 톤 OR 대화 톤)</li>
<li>발행 빈도</li>
</ul>
</div>
</div>

<div class="action-row">
<div class="action-actor claude"><span class="who">🤖 Claude</span>자동</div>
<div class="action-arrow">⤵</div>
<div class="action-body">
<span class="step-name">📁 채널 폴더·설정 자동 생성</span>
<ul>
<li><code>profile.md</code> (조선야담처녀 톤 자동 반영)</li>
<li><code>settings.json</code> · <code>workflow.json</code></li>
<li><code>thumbnail-strategy.json</code> (어두운 흙색·인물 클로즈업·노란 굵은 텍스트 등 패턴 라이브러리 반영)</li>
</ul>
</div>
</div>

<div class="action-row">
<div class="action-actor claude"><span class="who">🤖 Claude</span>제안</div>
<div class="action-arrow">⤵</div>
<div class="action-body">
<span class="step-name">시니어랩 추천 TOP3로 주제 자동 제안</span>
<ul>
<li>1. 효·가족 (점수 11,804)</li>
<li>2. 권선징악·사이다 (11,176)</li>
<li>3. 혼인·치정 (10,704)</li>
</ul>
</div>
</div>

<div class="action-row">
<div class="action-actor user"><span class="who">👤 사용자</span>선택</div>
<div class="action-arrow">→</div>
<div class="action-body">
주제 선택 → 시나리오 1의 <b>script-pd 진입</b> 흐름으로 합류
</div>
</div>

</div>

<h3>📋 추천 명령어 패턴</h3>

<div class="cmd-card">
<div class="cmd-input">"잘듣네 채널 주제 5개 추천해줘"</div>
<span class="cmd-arrow">→</span>
<div class="cmd-result">추천만 (대본 X)</div>
</div>

<div class="cmd-card">
<div class="cmd-input">"잘듣네 채널 주제 찾아서 대본 만들어줘"</div>
<span class="cmd-arrow">→</span>
<div class="cmd-result">추천 + 사용자 선택 + 대본 풀세트</div>
</div>

<div class="cmd-card">
<div class="cmd-input">"잘듣네 채널 효·가족 주제로 대본 만들어줘"</div>
<span class="cmd-arrow">→</span>
<div class="cmd-result">주제 명시 → 바로 대본 작업</div>
</div>

<div class="cmd-card">
<div class="cmd-input">"이 영상 분석하고 잘듣네 톤으로 대본 만들어줘: URL"</div>
<span class="cmd-arrow">→</span>
<div class="cmd-result">autopsy + script-pd 한 흐름</div>
</div>

<div class="cmd-card">
<div class="cmd-input">"오늘 가장 잘 나갈 만한 잘듣네 영상 1편 만들어줘"</div>
<span class="cmd-arrow">→</span>
<div class="cmd-result">추천 자동 선택 + 대본 (사용자 결정 최소)</div>
</div>

<h3>⚠️ 한계 (정직하게)</h3>

<div class="compare">
  <div class="compare-box good">
    <div class="head">✅ 자동화되는 것</div>
    <ul>
      <li>TubeHacker 데이터 분석</li>
      <li>채널 컨텍스트·corpus·패턴 자동 로드</li>
      <li>주제 추천 + 학습 영상 매칭</li>
      <li>script-pd 스킬 자동 진입</li>
      <li>레퍼런스 수집·분석·전략·아웃라인·드래프트</li>
      <li>썸네일 프롬프트 자동 생성</li>
    </ul>
  </div>
  <div class="compare-box bad">
    <div class="head">⚠️ 사용자가 결정해야 하는 것</div>
    <ul>
      <li>주제 선택 (3~5개 중 1)</li>
      <li>Hook 3후보 중 1 선택</li>
      <li>컨셉 확정·검토</li>
      <li>발행 OK</li>
      <li>채널이 없으면 채널명·톤 (질문 2~3회)</li>
    </ul>
  </div>
</div>

<div class="insight">
  <div class="insight-tag">💡 핵심 포인트</div>
  <div class="insight-section">완전 무인 자동화 X — <b>의도된 설계</b></div>
  <div class="insight-section">script-pd가 사용자 결정 단계를 두는 이유: <b>채널 톤·주제 방향성은 사람만 알 수 있기 때문</b></div>
  <div class="insight-section">총 소요 시간: <b>30분~1시간</b> (데이터 분석 자동 + 사용자 결정 2~3회)</div>
</div>

<h3>🎯 지금 바로 시도해보기</h3>

<div class="cmd-card" style="border-color:var(--primary-bd);background:var(--primary-bg);">
<div class="cmd-input" style="background:var(--bg);color:var(--text);">"새 야담 채널 만들어서 첫 영상 대본 만들어줘"</div>
<span class="cmd-arrow">→</span>
<div class="cmd-result"><b style="color:var(--primary-hi);">현재 가장 데이터 풍부 (시니어랩 28편 corpus + 72편 야담)</b></div>
</div>

</div>
</details>

---

## 🖼️ 사이트 한눈에 보기

<div class="mock">
  <div class="mock-header">
    <span style="font-size:18px;">🇰🇷</span>
    <span class="mock-brand">TubeHacker</span>
    <span class="mock-slogan">· 유튜브 알고리즘 해킹의 모든 것</span>
    <div class="mock-chips">
      <span class="mock-chip warn">🚨 <b>9</b></span>
      <span class="mock-chip hot">🔥 <b>150</b></span>
      <span class="mock-chip">🆕 <b>65</b></span>
      <span class="mock-chip" style="background:rgba(34,197,94,.13);color:#22c55e;border-color:rgba(34,197,94,.55);font-weight:700;">📡 <b style="color:#22c55e;">264</b></span>
      <span class="mock-chip" style="background:#fff;color:#000;">📖 가이드</span>
      <span class="mock-chip" style="background:#fff;color:#000;">📅 일별</span>
      <span class="mock-chip" style="background:linear-gradient(135deg,#fff,#fff5f5);color:#000;border:1.5px solid #ff4d4f;font-weight:800;">🇯🇵 JP</span>
    </div>
  </div>
  <div class="mock-tabs">
    <span class="mock-tab on" style="position:relative;">🎯 오늘의 주제 <span style="position:absolute;top:-4px;right:-4px;background:#ef4444;color:#fff;border-radius:50%;width:14px;height:14px;font-size:9px;line-height:14px;text-align:center;">7</span></span>
    <span class="mock-tab" style="position:relative;">📰 뉴스 모니터링 <span style="position:absolute;top:-4px;right:-4px;background:#ef4444;color:#fff;border-radius:50%;width:14px;height:14px;font-size:9px;line-height:14px;text-align:center;">3</span></span>
    <span class="mock-tab">🔥 Hot키워드</span>
    <span class="mock-tab">🔬 과학 트렌드</span>
    <span class="mock-tab">🎙️ 시니어랩</span>
    <span class="mock-tab">🔥 왜 이 영상은 터졌는가?</span>
    <span class="mock-tab">🏆 패턴 라이브러리</span>
    <span class="mock-tab">🔄 분석 업데이트</span>
  </div>
  <div class="mock-card crown">
    <span class="mock-rank-badge">👑 #1</span>
    <span class="mock-ch-name">지식인사이드</span>
    <span class="mock-delta">▲5</span>
    <div class="mock-meta-line">구독 384만 · 🎬 롱폼 · 📅 21년 8월 개설 · 4년 9개월차</div>
    <div class="mock-stats-row">
      <div class="mock-stat sig"><b>3</b>🚨 시그널</div>
      <div class="mock-stat hot"><b>5</b>🔥 폭발</div>
      <div class="mock-stat"><b>1</b>🆕 24h</div>
    </div>
    <div class="mock-vid-dual">
      <div class="mock-vid-mini">
        <div class="lbl pop">🔥 인기 영상</div>
        <div class="mock-vid-thumb">[썸네일]</div>
        <div class="title">조선 마지막 환관의 비밀</div>
      </div>
      <div class="mock-vid-mini">
        <div class="lbl latest">🆕 최신 영상</div>
        <div class="mock-vid-thumb">[썸네일]</div>
        <div class="title">광해군이 왜 폐위됐나</div>
      </div>
    </div>
  </div>
</div>

<p style="text-align:center; color:var(--text2); font-size:12px;">↑ 실제 사이트 헤더 + 채널 카드 모양 (미니어처)</p>

<div class="insight">
  <div class="insight-tag">🆕 헤더 사용 팁</div>
  <div class="insight-section"><b>로고 클릭</b>: <code>TubeHacker</code> 텍스트 클릭하면 홈으로 이동 + 새로고침</div>
  <div class="insight-section"><b>알림 배지 (빨간 원)</b>: 🎯 오늘의 주제 · 📰 뉴스 모니터링 탭 옆에 새 데이터 개수 표시. 한번 보면 회색으로 변함</div>
  <div class="insight-section"><b>흰 chip (우측)</b>: 🇯🇵 JP / 📖 가이드 / 📅 일별 — 자주 안 쓰는 페이지는 우측 chip으로 정리</div>
</div>

---

## 🎯 TubeHacker가 답하는 5가지 질문

<div class="flow">
  <div class="flow-node primary">
    <span class="icon">🎯</span>
    <div class="title">오늘 만들 주제?</div>
    <div class="sub">→ 오늘의 주제</div>
  </div>
  <div class="flow-node">
    <span class="icon">🔥</span>
    <div class="title">영구 가치 주제?</div>
    <div class="sub">→ Hot키워드</div>
  </div>
  <div class="flow-node">
    <span class="icon">🔬</span>
    <div class="title">왜 터졌나?</div>
    <div class="sub">→ Autopsy</div>
  </div>
  <div class="flow-node">
    <span class="icon">🏆</span>
    <div class="title">검증 패턴?</div>
    <div class="sub">→ 패턴 라이브러리</div>
  </div>
  <div class="flow-node">
    <span class="icon">📊</span>
    <div class="title">경쟁 채널?</div>
    <div class="sub">→ 대시보드</div>
  </div>
</div>

---

## 📊 핵심 메트릭 (이거 모르면 안 됨)

<div class="metric-card">
  <div class="metric-icon">⚡</div>
  <div class="metric-body">
    <div class="name">효율 (Efficiency)</div>
    <div class="formula">= 조회수 ÷ 구독자수</div>
    <div class="meaning">알고리즘이 외부 추천한 정도. 구독자 작은 채널도 폭발 가능.</div>
    <div class="metric-grades">
      <span class="grade good">1.0+ 양호</span>
      <span class="grade good">5.0+ 폭발 🔥</span>
      <span class="grade good">10.0+ 메가폭발 🚀</span>
    </div>
  </div>
</div>

<div class="metric-card">
  <div class="metric-icon">🚀</div>
  <div class="metric-body">
    <div class="name">시속 (Velocity)</div>
    <div class="formula">= 조회수 ÷ 영상 나이(시간)</div>
    <div class="meaning">'지금 막' 폭발 중인 영상 발견. 이미 폭발한 영상이 아니라 진행 중.</div>
    <div class="metric-grades">
      <span class="grade mid">5,000+/h 시그널 🚨</span>
      <span class="grade good">50,000+/h 트렌딩</span>
    </div>
  </div>
</div>

<div class="metric-card">
  <div class="metric-icon">⏱️</div>
  <div class="metric-body">
    <div class="name">첫 사건 발생 시점</div>
    <div class="formula">영상 시작 → 첫 사건 키워드 등장 시점</div>
    <div class="meaning">시청자 머무름 결정. 늦으면 이탈.</div>
  </div>
</div>

<div class="ruler">
  <div class="ruler-track">
    <div class="ruler-marker" data-label="60s" style="left:33%;"></div>
    <div class="ruler-marker" data-label="120s" style="left:66%;"></div>
  </div>
  <div class="ruler-labels">
    <span>🟢 안전</span>
    <span>🟡 주의</span>
    <span>🔴 위험</span>
  </div>
  <div class="ruler-scale">
    <span>0s</span><span>60s</span><span>120s</span><span>180s</span>
  </div>
</div>

<div class="metric-card">
  <div class="metric-icon">♻️</div>
  <div class="metric-body">
    <div class="name">단조도 (Monotony)</div>
    <div class="formula">= N편 영상간 3-gram Jaccard × 100</div>
    <div class="meaning">같은 채널이 매번 같은 표현 쓰는 정도. 높으면 시청자 거부감.</div>
  </div>
</div>

<div class="gauge">
  <div class="gauge-title">단조도 점수 0~100</div>
  <div class="gauge-bar">
    <div class="gauge-pointer" style="left:25%;"></div>
  </div>
  <div class="gauge-labels">
    <span>🟢 0~10 다양</span>
    <span>🟡 10~20 적당</span>
    <span>🟠 20~30 반복</span>
    <span>🔴 30+ 거부</span>
  </div>
</div>

<div class="metric-card">
  <div class="metric-icon">🎯</div>
  <div class="metric-body">
    <div class="name">클릭베이트 점수</div>
    <div class="formula">LLM 1~10점</div>
    <div class="meaning">썸네일의 자극도. 카테고리 평균이 목표 — 너무 높으면 신뢰도 ↓ → retention ↓</div>
    <div class="metric-grades">
      <span class="grade good">5~7 적정</span>
      <span class="grade mid">8 강함</span>
      <span class="grade bad">9~10 과함 ⚠️</span>
    </div>
  </div>
</div>

---

## 🗂️ 탭별 상세 사용법

### 🏠 대시보드 홈

**언제 보나**: 매일 아침 30초 확인용. (로고 <code>TubeHacker</code> 클릭으로 진입)

<div class="steps">
  <div class="step">
    <span class="step-num">1</span>
    <div class="step-title">헤더 칩 확인</div>
    <div class="step-body">🚨 시그널 · 🔥 폭발 · 🆕 24h 숫자 클수록 = 만들기 좋은 날</div>
  </div>
  <div class="step">
    <span class="step-num">2</span>
    <div class="step-title">필터 활용</div>
    <div class="step-body">시간 토글 · 형식 토글 · 대형 제외 · 폭발/시그널만 · 검색</div>
  </div>
  <div class="step">
    <span class="step-num">3</span>
    <div class="step-title">채널 카드 읽기</div>
    <div class="step-body">👑 1·2·3위 · ▲ 등락 · 📅 연차 · 인기/최신 영상</div>
  </div>
</div>

<div class="compare">
  <div class="compare-box good">
    <div class="head">✅ 이렇게 보세요</div>
    <ul>
      <li>▲ 상승 화살표 있는 채널 우선</li>
      <li>대형 제외 체크해서 우리 사이즈 채널만</li>
      <li>인기 영상 + 최신 영상 모두 확인</li>
      <li>편/주 5+ 채널 = 활발한 채널</li>
    </ul>
  </div>
  <div class="compare-box bad">
    <div class="head">❌ 흔한 실수</div>
    <ul>
      <li>1위 채널만 보고 따라가기</li>
      <li>우리 카테고리 아닌 채널 분석</li>
      <li>구독자 수만 보고 판단</li>
      <li>매일 같은 채널만 확인</li>
    </ul>
  </div>
</div>

<div class="insight">
  <div class="insight-tag">🎯 인사이트 도출 예시</div>
  <div class="insight-section"><b>상황</b>: 역사 카테고리 1위 ▲3 상승 + 인기 영상 "조선 마지막 환관의 비밀"</div>
  <div class="insight-section"><b>인사이트</b>: 역사 채널 지금 알고리즘 추천 + "비밀·정체" 클릭베이트 통함 + 조선 비주류 인물 콘텐츠 효율 좋음</div>
  <div class="insight-section"><b>액션</b>: 조선시대 비주류(궁녀/내시/상궁) 인물 콘텐츠 1개 만들기</div>
</div>

---

### 🎯 오늘의 주제

**언제 보나**: 매일 영상 만들기 전.

<div class="flow">
  <div class="flow-node primary">
    <span class="icon">🥇</span>
    <div class="title">🔥 재편집 재폭발</div>
    <div class="sub">최우선 — 가장 안전</div>
  </div>
  <div class="flow-node">
    <span class="icon">🥈</span>
    <div class="title">검증 주제</div>
    <div class="sub">영구 가치</div>
  </div>
  <div class="flow-node">
    <span class="icon">🥉</span>
    <div class="title">오늘 폭발</div>
    <div class="sub">단발 트렌드 주의</div>
  </div>
</div>

<div class="compare">
  <div class="compare-box good">
    <div class="head">✅ 우선순위</div>
    <ul>
      <li><b>🔥 재편집 재폭발</b> — 다른 채널이 *지금 같은 주제로 다시 만들어 잘 됨* → 우리도 만들면 효율 높음</li>
      <li><b>검증 주제</b> — 시간 검증 통과 → 안전</li>
      <li><b>오늘 폭발</b> — 단발일 수 있음 → 신중</li>
    </ul>
  </div>
  <div class="compare-box bad">
    <div class="head">❌ 흔한 실수</div>
    <ul>
      <li>"오늘 폭발 주제"만 따라가기 (단발 위험)</li>
      <li>주제만 가져가고 *왜 터졌는지* 분석 안 함</li>
      <li>autopsy 안 거치고 바로 대본 작업</li>
    </ul>
  </div>
</div>

---

### 🎙️ 시니어랩 (야담) — 풀세트 흐름

<div class="flow">
  <div class="flow-node primary">
    <span class="icon">1️⃣</span>
    <div class="title">추천 TOP3</div>
    <div class="sub">윈도우 가중 점수</div>
  </div>
  <div class="flow-node">
    <span class="icon">2️⃣</span>
    <div class="title">📚 벤치마크 학습</div>
    <div class="sub">1~5순위 채널 톤</div>
  </div>
  <div class="flow-node">
    <span class="icon">3️⃣</span>
    <div class="title">🎬 표준 구조</div>
    <div class="sub">6단계 시간 배분</div>
  </div>
  <div class="flow-node">
    <span class="icon">4️⃣</span>
    <div class="title">🪝 Hook 풀</div>
    <div class="sub">검증된 첫 문장</div>
  </div>
  <div class="flow-node primary">
    <span class="icon">5️⃣</span>
    <div class="title">🔥 분석 1클릭</div>
    <div class="sub">표 행 [🔥 분석]</div>
  </div>
</div>

<div class="tldr">
<div class="tldr-title">🎯 시니어랩 → 야담 채널 첫 영상 워크플로</div>
<div class="tldr-body">
시니어 탭 → 추천 TOP3 #1 선택 → 학습 영상 5편 [🔥 분석] → autopsy 결과 → [📝 대본 만들기] → Claude Code → 대본 완성 (총 ~50분)
</div>
</div>

---

### 🔥 왜 이 영상은 터졌는가? (Autopsy)

**언제 보나**: 특정 영상 성공 비결 분석 / 우리 영상 만들기 전 검증.

<div class="steps">
  <div class="step hot">
    <span class="step-num">1</span>
    <div class="step-title">📋 URL 준비 (3~5편 권장)</div>
    <div class="step-body">1편만 던지면 패턴 안 보임. 같은 카테고리·비슷한 효율의 영상 묶어서</div>
  </div>
  <div class="step">
    <span class="step-num">2</span>
    <div class="step-title">📥 폼 입력</div>
    <div class="step-body">URL · 라벨(선택) · 태그(선택) → [🔥 분석 시작]</div>
  </div>
  <div class="step warn">
    <span class="step-num">3</span>
    <div class="step-title">🤖 GitHub Issue 자동 작성</div>
    <div class="step-body">새 탭에서 [Create] 한 번 클릭. 5~10분 자동 처리</div>
  </div>
  <div class="step">
    <span class="step-num">4</span>
    <div class="step-title">📊 결과 카드 확인</div>
    <div class="step-body">Cmd+R 새로고침 → 새 카드 → 클릭해서 상세</div>
  </div>
</div>

#### 📊 결과 페이지에서 보는 것

<div class="mock">
  <div style="font-size:14px; font-weight:800; color:var(--text); margin-bottom:8px;">🎯 공통 패턴 (핵심 인사이트)</div>
  <div class="mock-stats-row">
    <div class="mock-stat"><b>회상형</b>🪝 후크</div>
    <div class="mock-stat"><b>교훈형</b>🎯 결말</div>
    <div class="mock-stat"><b>43.6분</b>⏱️ 평균</div>
    <div class="mock-stat"><b>247 wpm</b>🗣️ 발화</div>
  </div>
  <div style="margin-top:8px; padding-top:8px; border-top:1px solid var(--divider); font-size:12px; color:var(--text2);">
    공통 어휘: <code>잠시</code>×96 · <code>있었습니다</code>×85 · <code>있었지요</code>×72 · ...
  </div>
</div>

<div class="mock">
  <div style="font-size:14px; font-weight:800; color:var(--text); margin-bottom:8px;">🔬 Hook 0~30초 세분화</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;">
    <div style="background:var(--surface);padding:10px;border-radius:8px;font-size:11px;">
      <div style="font-weight:700;color:var(--warn);">⚡ 0~3s Pre-hook</div>
      <div style="color:var(--text2);margin-top:3px;">첫인상 (시각·청각 즉시 인지)</div>
    </div>
    <div style="background:var(--surface);padding:10px;border-radius:8px;font-size:11px;">
      <div style="font-weight:700;color:var(--hot);">⚡ 3~10s Core</div>
      <div style="color:var(--text2);margin-top:3px;">충격·질문·통계 패턴</div>
    </div>
    <div style="background:var(--surface);padding:10px;border-radius:8px;font-size:11px;">
      <div style="font-weight:700;color:var(--primary-hi);">⚡ 10~30s Promise</div>
      <div style="color:var(--text2);margin-top:3px;">"이 영상에서 보여줄 것" 약속</div>
    </div>
  </div>
</div>

<div class="insight">
  <div class="insight-tag">🎯 활용법</div>
  <div class="insight-section">분석 결과의 <b>첫 사건 평균 시점</b>이 우리 영상 만들 때 기준 — 같은 시점에 첫 사건 배치</div>
  <div class="insight-section"><b>댓글 timestamp 분포</b>의 spike 시점 = 영상의 *킬링 포인트* — 우리도 비슷한 시점에 강조 포인트 배치</div>
  <div class="insight-section"><b>단조도 30+</b>인 채널의 후속 영상이라면 우리는 <b>다른 표현</b>으로 만들어 차별화</div>
</div>

#### 📝 결정적 활용 — [📝 대본 만들기]

<div class="flow">
  <div class="flow-node">
    <span class="icon">📊</span>
    <div class="title">분석 결과</div>
    <div class="sub">상단 보라 박스</div>
  </div>
  <div class="flow-node primary">
    <span class="icon">📝</span>
    <div class="title">[대본 만들기]</div>
    <div class="sub">버튼 클릭</div>
  </div>
  <div class="flow-node">
    <span class="icon">📋</span>
    <div class="title">자동 복사</div>
    <div class="sub">클립보드 + 모달</div>
  </div>
  <div class="flow-node primary">
    <span class="icon">🤖</span>
    <div class="title">Claude Code</div>
    <div class="sub">붙여넣기 → 대본 시작</div>
  </div>
</div>

---

### 🏆 패턴 라이브러리

**언제 보나**: 새 영상의 *썸네일·제목·Hook 만들기 전* 필수 참고.

<div class="steps">
  <div class="step">
    <span class="step-num">1</span>
    <div class="step-title">⚡ 첫 사건 시점 표준</div>
    <div class="step-body">평균/중앙/P25/P75 → 우리 영상도 이 범위 안에</div>
  </div>
  <div class="step">
    <span class="step-num">2</span>
    <div class="step-title">📝 제목 공식</div>
    <div class="step-body">우리 카테고리 카드 — 글자수·구조·클릭베이트·2-gram</div>
  </div>
  <div class="step">
    <span class="step-num">3</span>
    <div class="step-title">🖼️ 썸네일 카탈로그</div>
    <div class="step-body">효율 TOP + LLM 시각 분석 (클릭베이트·전략 한 줄)</div>
  </div>
  <div class="step">
    <span class="step-num">4</span>
    <div class="step-title">🪝 Hook 풀</div>
    <div class="step-body">효율 정렬 첫 문장 30개 — 패턴 학습</div>
  </div>
</div>

<div class="insight">
  <div class="insight-tag">🎯 인사이트 도출 예시 — 야담 카테고리</div>
  <div class="insight-section"><b>데이터</b>: 평균 글자수 80자 · 파이프(ㅣ) 22% · 숫자 32% · "비밀_정체" 클릭베이트 우세</div>
  <div class="insight-section"><b>인사이트</b>: 야담 제목은 <b>길고 + 파이프 구분자 + 숫자 (인물 나이) + 비밀/정체 키워드</b> 패턴이 검증됨</div>
  <div class="insight-section"><b>액션</b>: "14살 종놈이 임금을 살린 비밀의 망치 ㅣ 임진왜란 야담 ㅣ 옛날이야기" (80자·파이프 2개·숫자·비밀)</div>
</div>

---

### 🔄 분석 업데이트 (NEW)

**언제 보나**: 주 1~2회, "추적 채널을 늘리거나 정리하고 싶을 때".

TubeHacker는 매일 자동으로 **신규 채널 후보**를 발견합니다(현재 264개 발견). 어떤 채널을 정식 추적 대상에 넣을지는 **사용자 선택**입니다. 이 페이지에서 한 번에 추가/해제할 수 있어요.

<div class="flow">
  <div class="flow-node">
    <span class="icon">🤖</span>
    <div class="title">매일 시스템</div>
    <div class="sub">신규 후보 자동 누적</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-node primary">
    <span class="icon">👤</span>
    <div class="title">사용자 (주 1~2회)</div>
    <div class="sub">체크박스 선택 → 일괄 추가</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-node">
    <span class="icon">📡</span>
    <div class="title">다음날부터 추적</div>
    <div class="sub">매일 21:00 데이터 수집</div>
  </div>
</div>

#### 📍 페이지 구조 — 두 가지 탭

<div class="steps">
  <div class="step">
    <span class="step-num">🆕</span>
    <div class="step-title">신규 후보 탭</div>
    <div class="step-body">시스템이 발견한 추가 후보 — 카테고리 필터 + 50개씩 페이지</div>
  </div>
  <div class="step">
    <span class="step-num">📡</span>
    <div class="step-title">추적 중 탭</div>
    <div class="step-body">현재 모니터링 중인 채널 — 시그널/폭발 활성도 순 정렬</div>
  </div>
</div>

#### 🎯 사용법 — 한 번에 추가하기

<div class="steps">
  <div class="step">
    <span class="step-num">1</span>
    <div class="step-title">카테고리 필터</div>
    <div class="step-body">"경제" "지식" "역사" 등 — 우리 채널과 같은 카테고리만 좁히기</div>
  </div>
  <div class="step">
    <span class="step-num">2</span>
    <div class="step-title">체크박스 선택</div>
    <div class="step-body">카드 클릭 = 체크. 좋아 보이는 채널 5~20개 선택</div>
  </div>
  <div class="step">
    <span class="step-num">3</span>
    <div class="step-title">⚡ 상위 10개 (선택)</div>
    <div class="step-body">하단 바의 [⚡ 상위 10개] 누르면 자동 선택</div>
  </div>
  <div class="step">
    <span class="step-num">4</span>
    <div class="step-title">[✓ N개 추적 추가]</div>
    <div class="step-body">하단 sticky bar 버튼 클릭 → GitHub Issue 자동 생성</div>
  </div>
  <div class="step">
    <span class="step-num">5</span>
    <div class="step-title">자동 처리 (3분 내)</div>
    <div class="step-body">로컬 봇이 Issue 감지 → 채널 목록에 추가 → 다음날부터 추적</div>
  </div>
</div>

#### 🗑️ 추적 해제 (정리)

추적 중 탭에서 → 안 보는 채널 체크박스 → 하단 빨간 [✗ 추적 해제] 버튼 → Issue 생성 → 봇이 blocklist에 추가.

<div class="compare">
  <div class="compare-box good">
    <div class="head">✅ 추가하면 좋은 채널</div>
    <ul>
      <li>30d 시그널/폭발 합계 ≥ 1 (활성)</li>
      <li>우리 카테고리와 겹침</li>
      <li>구독 1만 ~ 50만 (소형, 우리와 비교 가능)</li>
      <li>주 발행 빈도 1편/주 이상</li>
    </ul>
  </div>
  <div class="compare-box bad">
    <div class="head">❌ 안 추가해도 되는 것</div>
    <ul>
      <li>30d 신호 0개 (죽은 채널)</li>
      <li>구독 1000 미만 (데이터 부족)</li>
      <li>다른 카테고리 (참고 안 됨)</li>
      <li>이미 추적 중 (중복)</li>
    </ul>
  </div>
</div>

<div class="insight">
  <div class="insight-tag">💡 3-카운터 의미 (헤더에 보이는 숫자)</div>
  <div class="insight-section"><b>📺 분석영상</b>: 지금까지 분석한 모든 영상(추적 + Autopsy + 검증주제). 누적 수치 — 데이터 풀 크기</div>
  <div class="insight-section"><b>📊 분석채널</b>: 한 번이라도 분석에 포함된 채널(추적 + Autopsy 등). 추적보다 큼</div>
  <div class="insight-section"><b>📡 추적</b>: 매일 21:00에 자동 모니터링하는 채널 — 이 페이지에서 늘리거나 줄임</div>
</div>

---

## 💎 제우스 노하우 (오토워커 1기 1달 750만원 검증)

오토워커 1기 **제우스님**이 1달 만에 구독 3만 / 수익 750만원을 만든 핵심. 클코 + 튜브해커 + 튜브워커 조합으로 이 노하우를 매 영상 자동 적용한다.

<div class="tldr" style="border-color:#fbbf24;background:linear-gradient(135deg,rgba(245,158,11,.08),rgba(251,191,36,.05));">
<div class="tldr-title" style="color:#fbbf24;">⚡ 한 줄 요약 (2가지)</div>
<div class="tldr-body">
💎 <b>노하우 1 — 주제</b>: 조회수 검증된 영상 2개를 합쳐 새 각도 주제 만들기 → 두 시청자 풀 동시 흡수<br>
💎 <b>노하우 2 — 배포</b>: 영문 파일명·해시태그 위치·고정댓글·영상 끝 본인 의견 등 7가지 알고리즘 친화 세팅
</div>
</div>

### 💎 노하우 1: 검증 영상 2개 합쳐 새 각도 (★ 가장 중요)

**기본 패턴**:

<div style="background:var(--surface);border-left:3px solid #fbbf24;border-radius:0 8px 8px 0;padding:14px 18px;margin:14px 0;font-size:13px;line-height:1.7;">
공통 주제 X (같은 대상·인물·현상)<br>
&nbsp;+ <b>A</b>: X를 [관점1·지역1·시점1·측면1]에서 본 검증 영상 (30만뷰+)<br>
&nbsp;+ <b>B</b>: X를 [관점2·지역2·시점2·측면2]에서 본 검증 영상 (30만뷰+)<br>
─────────────<br>
= <b>C</b>: X를 [비교·통합·인과 연결]한 새 각도
</div>

**제우스님 원본 예시**:
- A: "미국 샌프란시스코에서 대박난 BTS의 인기" (40만뷰)
- B: "일본 방송을 장악한 BTS의 인기" (30만뷰)
- C: "미국 vs 일본, 세계 1·2위 시장이 동시에 BTS에 열광하는 진짜 이유" — 두 풀 동시 흡수 + 새로움 가산점

**왜 효과적인가** (알고리즘 관점):
1. A 시청자 + B 시청자 = **두 풀에 동시 노출** → 초기 추천 트래픽 2배
2. 단순 카피 아닌 비교·통합 → **독창성 가산점**
3. A·B 둘 다 이미 검증된 수요 → C도 수요 확률 ↑

### 🎬 활용 방법 5가지 (어떤 식으로 2개를 합칠 것인가)

<div class="steps">
  <div class="step">
    <span class="step-num">1</span>
    <div class="step-title">🕒 시의성 접목</div>
    <div class="step-body">현재 핫이슈 + 우리 채널의 검증 영상 = 시의성 가산</div>
  </div>
  <div class="step">
    <span class="step-num">2</span>
    <div class="step-title">🚀 알고리즘 트렌드 접목</div>
    <div class="step-body">TubeHacker Hot키워드·시그널의 폭발 주제 + 우리 채널 검증</div>
  </div>
  <div class="step">
    <span class="step-num">3</span>
    <div class="step-title">🔀 카테고리 교차</div>
    <div class="step-body">다른 카테고리 폭발 주제를 <b>우리 톤으로 변환</b> (예: 경제 → 역사)</div>
  </div>
  <div class="step">
    <span class="step-num">4</span>
    <div class="step-title">⏳ 시점 교차</div>
    <div class="step-body">같은 패턴의 과거 + 현재 (예: "광해군 폐위" + "현 정부 위기")</div>
  </div>
  <div class="step">
    <span class="step-num">5</span>
    <div class="step-title">👥 인물·사건 교차</div>
    <div class="step-body">두 인물/사건의 비교·공통점·인과 (예: "세종 vs 정조")</div>
  </div>
</div>

<div class="insight">
  <div class="insight-tag">🎯 채널별 샘플 — 제우스 노하우 1 적용</div>
  <div class="insight-section"><b>🌙 잘듣네 (위로형 인문)</b> · 시점 교차 — <i>A: "어머니 시한부 마지막 선택" (60만) + B: "60년 부부의 마지막 30일 일기" (45만) → C: "어머니의 시한부와 부부의 마지막 30일, 잠들기 전 한 자리에서"</i></div>
  <div class="insight-section"><b>📜 지식록 (시사·역사 시니어)</b> · 시점 교차 + 시의성 — <i>A: "현 정부 1년 만에 박살난 진짜 이유" (80만) + B: "광해군 9년 만에 폐위된 진짜 이유" (40만) → C: "광해군과 현 정부가 똑같이 놓친 단 하나 — 400년을 건너온 권력의 균열"</i></div>
  <div class="insight-section"><b>📚 야담 채널 (사료 인용)</b> · 인물 교차 — <i>A: "실록에 단 한 줄 적힌 노비의 충성" (45만) + B: "광해군일기 양반의 배신" (30만) → C: "실록 한 줄의 노비 vs 일기 한 줄의 양반, 누가 진짜 사람이었나"</i></div>
</div>

### ✅ 노하우 1 — 체크리스트 (클코가 매번 묻는 항목)

<div class="compare">
  <div class="compare-box good">
    <div class="head">✅ 좋은 A·B</div>
    <ul>
      <li>A, B 둘 다 조회수 30만+ (가능하면 50만+)</li>
      <li>같은 대상/현상을 다룸 (공통 X 명확)</li>
      <li>관점이 진짜 다름 (단순 같은 내용 ❌)</li>
      <li>최근 3~12개월 안의 검증 영상</li>
    </ul>
  </div>
  <div class="compare-box bad">
    <div class="head">❌ 잘못된 합치기</div>
    <ul>
      <li>A·B 모두 같은 채널 영상 (시청자 풀 겹침)</li>
      <li>공통 주제 X가 모호함</li>
      <li>C가 A or B 한쪽만으로도 만들 수 있음 (통합 의미 ❌)</li>
      <li>최신 트렌드와 동떨어진 영상</li>
    </ul>
  </div>
</div>

---

### 💎 노하우 2: 알고리즘 친화 업로드 세팅 7가지

배포 직전 자동 적용 (`prompts/upload-guide.md`에 자동화됨). 클코가 `output/youtube.md`에 같이 생성.

<div class="steps">
  <div class="step">
    <span class="step-num">1</span>
    <div class="step-title">영상 파일명 = 영문 검색어</div>
    <div class="step-body"><code>keyword1_keyword2_keyword3.mp4</code> — 알고리즘 분류 보조</div>
  </div>
  <div class="step">
    <span class="step-num">2</span>
    <div class="step-title">썸네일 파일명 = 영문 검색어</div>
    <div class="step-body"><code>keyword1_keyword2_keyword3.png</code> (썸네일 3개도 동일 룰)</div>
  </div>
  <div class="step">
    <span class="step-num">3</span>
    <div class="step-title">설명 최상단 #해시태그 5개</div>
    <div class="step-body">검색어 위주 — 첫 줄에 #키워드1 #키워드2 ... #키워드5</div>
  </div>
  <div class="step">
    <span class="step-num">4</span>
    <div class="step-title">설명 하단 timestamp (수동 챕터)</div>
    <div class="step-body">00:00·02:30·05:10... — 자동 챕터 오분류 방지 + 시청 지속률 ↑</div>
  </div>
  <div class="step">
    <span class="step-num">5</span>
    <div class="step-title">설명 맨 하단 #해시태그 15개 이하</div>
    <div class="step-body">검색 폭 확대 — 16개 이상은 역효과</div>
  </div>
  <div class="step">
    <span class="step-num">6</span>
    <div class="step-title">고정 댓글</div>
    <div class="step-body">영상 핵심 한 줄 + 시청자 액션 유도 (Claude 자동 생성)</div>
  </div>
  <div class="step">
    <span class="step-num">7</span>
    <div class="step-title">영상 끝 본인 의견</div>
    <div class="step-body">AI 양산 차단 회피 — 3~5문장의 개인 통찰 (Claude 자동)</div>
  </div>
</div>

<div class="insight" style="background:linear-gradient(135deg,rgba(245,158,11,.06),rgba(251,191,36,.04));border-left:3px solid #fbbf24;">
  <div class="insight-tag" style="color:#fbbf24;">💡 보너스 (제우스님이 추가로 적용한 것)</div>
  <div class="insight-section"><b>로고 + 배경 경음악</b>: 채널 정체성 강화 + 시청 시간 ↑</div>
  <div class="insight-section"><b>본인 얼굴 AI 합성</b>: AI 양산 의심 회피 (선택)</div>
  <div class="insight-section"><b>발행 주기</b>: 2~3일에 1편 (꾸준함이 빈도보다 중요 — 알고리즘 신뢰)</div>
  <div class="insight-section"><b>포맷</b>: 롱폼 위주, 숏폼은 롱폼 변형으로 가끔</div>
</div>

---

## 🎨 제목·썸네일 제작 체크리스트 (버터떡 노하우)

> **출처**: 버터떡 강의 (SEO·썸네일·알고리즘 풀세트). **모든 채널·모든 영상**에 적용.
> 클코 대본 작업 시 STRATEGY 단계에서 자동으로 이 체크리스트를 띄움.

### 📌 핵심 원칙 (한 줄)

**제목 = SEO(검색용) / 썸네일 카피 = CTR(클릭용)** — 둘이 같으면 광고판 활용 0.

### ✅ 1단계 — 제목·썸네일 직접 제작 (사용자가 체크)

<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:18px 0;">

<div style="background:var(--surface);border:1px solid var(--primary-bd);border-radius:10px;padding:14px 16px;">
<div style="font-weight:800;color:var(--primary-hi);font-size:14px;margin-bottom:8px;">📌 제목 (SEO)</div>
<ul style="margin:0;padding-left:18px;font-size:12.5px;line-height:1.75;">
<li>□ 메인 키워드 <b>전진 배치</b> (앞쪽)</li>
<li>□ 연관 키워드 자연스럽게 조합</li>
<li>□ 잘리지 않는 길이 (40자 이내 권장)</li>
<li>□ 검색용 표현 (구글·유튜브 검색에 걸릴)</li>
</ul>
</div>

<div style="background:var(--surface);border:1px solid var(--hot-bd);border-radius:10px;padding:14px 16px;">
<div style="font-weight:800;color:var(--hot);font-size:14px;margin-bottom:8px;">🎨 썸네일 카피 (CTR)</div>
<ul style="margin:0;padding-left:18px;font-size:12.5px;line-height:1.75;">
<li>□ 대사형·임팩트 문장</li>
<li>□ 한눈에 들어오는 짧은 문구</li>
<li>□ 숫자·금액·기간(○○만원·○○년)은 여기</li>
<li>□ 검색용 문장 ❌ (감정·충격에 집중)</li>
</ul>
</div>

<div style="background:var(--surface);border:1px solid var(--info);border-radius:10px;padding:14px 16px;">
<div style="font-weight:800;color:var(--info);font-size:14px;margin-bottom:8px;">🔗 3단 일치</div>
<ul style="margin:0;padding-left:18px;font-size:12.5px;line-height:1.75;">
<li>□ 이미지 ↔ 썸네일 카피 ↔ 제목</li>
<li>□ 셋이 만나도 의미 통함</li>
</ul>
</div>

<div style="background:var(--surface);border:1px solid var(--danger);border-radius:10px;padding:14px 16px;">
<div style="font-weight:800;color:var(--danger);font-size:14px;margin-bottom:8px;">❌ 금지</div>
<ul style="margin:0;padding-left:18px;font-size:12.5px;line-height:1.75;">
<li>□ 썸네일 카피 = 제목 (거의 같음)</li>
<li>□ 유명인 옆 대사형 멘트 (허위사실)</li>
<li>□ 까만 박스 / AI 잘림 흔적</li>
</ul>
</div>

<div style="background:var(--surface);border:1px solid var(--warn);border-radius:10px;padding:14px 16px;grid-column:span 2;">
<div style="font-weight:800;color:var(--warn);font-size:14px;margin-bottom:8px;">📱 모바일 가독성 (썸네일 마지막 점검)</div>
<ul style="margin:0;padding-left:18px;font-size:12.5px;line-height:1.75;">
<li>□ 큰 글자 (모바일 폰 크기에서 잘 보임)</li>
<li>□ 텍스트 한쪽 치우치게 배치 (양쪽 텅 X)</li>
<li>□ 명확한 단색 (과한 그라데이션 X)</li>
</ul>
</div>

</div>

### ✅ 2단계 — 클코가 자동 제공 (제목·썸네일 후 알림)

대본 작업 마지막에 클코가 `output/youtube.md`에 자동 포함:

<div class="steps">
  <div class="step">
    <span class="step-num">1</span>
    <div class="step-title">📁 영문 파일명</div>
    <div class="step-body"><code>keyword1_keyword2_keyword3.mp4 / .png</code> — 알고리즘 분류 보조 (제우스 노하우 2)</div>
  </div>
  <div class="step">
    <span class="step-num">2</span>
    <div class="step-title">🏷️ 태그 10~15개</div>
    <div class="step-body">스튜디오 설정용 (시청자 X). 검색 알고리즘만 봄</div>
  </div>
  <div class="step">
    <span class="step-num">3</span>
    <div class="step-title">#️⃣ 해시태그</div>
    <div class="step-body">설명 상단 5개 (검색 강함) + 하단 15개 이하 (검색 폭)</div>
  </div>
  <div class="step">
    <span class="step-num">4</span>
    <div class="step-title">💬 고정 댓글 ⭐</div>
    <div class="step-body"><b>검색 인덱스 가장 강함</b>. 핵심 해시태그 3~5개 + 액션 유도 멘트</div>
  </div>
  <div class="step">
    <span class="step-num">5</span>
    <div class="step-title">📍 수동 챕터</div>
    <div class="step-body">자동 X — 정확한 타임스탬프 직접 입력. 알고리즘+지속률 ↑</div>
  </div>
  <div class="step">
    <span class="step-num">6</span>
    <div class="step-title">📊 객관 자료 위치</div>
    <div class="step-body">구글 트렌드 그래프·뉴스 캡처 시점 명시 → 양산 의심 회피</div>
  </div>
</div>

### ✅ 3단계 — 대본 자체에 자동 적용

<div class="insight">
  <div class="insight-tag">🎬 클코가 DRAFT 단계에서 자동 보장 (사용자 액션 불필요)</div>
  <div class="insight-section"><b>1. 첫 1분 후킹 필수</b> — 버터떡 강의 핵심. Hook 30s + Intro 30s = 1분 안에 시청자 결심 유도. 노잼이면 즉시 이탈</div>
  <div class="insight-section"><b>2. 엔딩 멘트 절대 금지</b> — "마무리하도록 하겠습니다" 같은 신호 X → 그 시점 즉시 이탈. 마지막까지 본문 연장 후 <b>자연스러운 뚝 끝</b></div>
  <div class="insight-section"><b>3. 영상 끝 본인 의견 3~5문장</b> — 제우스 노하우 2번 7번 항목. AI 양산 차단 회피 + 개인 통찰 (단순 요약 X)</div>
</div>

### 📊 4단계 — 배포 후 모니터링

| 시점 | 측정 | 기준 |
|---|---|---|
| 24~48h 후 | **CTR (클릭률)** | 8%+ 좋음 / 6% 최소 / 4% 미만 → 썸네일·제목 즉시 교체 |
| 1주 후 | **시청 지속률 그래프 첫 1분** | 50%+ 유지 (1분 이내 이탈 ↓) |
| 1주 후 | **댓글·재방문률** | 재방문 늘면 채널 정착 신호 |

### 🎯 채널별 톤 조정 (4채널 매트릭스)

| 항목 | 지식록 | 잘듣네 | 과만세 | 야담 |
|---|---|---|---|---|
| **제목 키워드** | 코스피·환율·삼성 등 시사·경제 SEO | 인물명·도시·시대 | 과학 용어·건강 키워드 | 조선시대 인물·사건 |
| **썸네일 카피** | 시의성 폭로형 (숫자·충격) | 라디오 결 인용문 | 호기심 질문 | 권선징악 결말 암시 |
| **1분 후킹** | 시의성 폭로 ("X가 지금 무너진다") | 부드러운 인트로 ("오늘 밤 한 사람의...") | 호기심 질문 ("우주의 끝에는?") | 권선징악 시작 ("조선시대 어느 노비가...") |
| **본인 의견 톤** | 시니어 우파 통찰 | 잠들기 전 위로 | 시니어 과학 깊이 | 사료 인용 + 통찰 |
| **객관 자료** | 그래프·뉴스 캡처 | 인물 사진·서신·일기 | 논문·통계 | 사료 인용 (실록·일기) |

---

## 🎯 영상 1편 만들 때 풀 워크플로우

<div class="steps" style="grid-template-columns:repeat(auto-fit,minmax(140px,1fr));">
  <div class="step hot">
    <span class="step-num">Phase 1</span>
    <div class="step-title">발견</div>
    <div class="step-body">🏠 대시보드 시그널·👑 1·2·3위</div>
  </div>
  <div class="step">
    <span class="step-num">Phase 2</span>
    <div class="step-title">주제 결정</div>
    <div class="step-body">🎯 오늘의 주제 → URL 복사</div>
  </div>
  <div class="step">
    <span class="step-num">Phase 3</span>
    <div class="step-title">분석</div>
    <div class="step-body">🔥 autopsy URL 3~5편</div>
  </div>
  <div class="step">
    <span class="step-num">Phase 4</span>
    <div class="step-title">패턴 학습</div>
    <div class="step-body">결과 + 🏆 라이브러리</div>
  </div>
  <div class="step warn">
    <span class="step-num">Phase 5</span>
    <div class="step-title">대본</div>
    <div class="step-body">[📝 대본 만들기] → Claude</div>
  </div>
  <div class="step">
    <span class="step-num">Phase 6</span>
    <div class="step-title">발행</div>
    <div class="step-body">대본 → 영상 → 업로드</div>
  </div>
  <div class="step hot">
    <span class="step-num">Phase 7</span>
    <div class="step-title">검증</div>
    <div class="step-body">24h 후 우리 영상도 autopsy</div>
  </div>
</div>

<div class="tldr">
<div class="tldr-title">⏱️ 총 소요 시간</div>
<div class="tldr-body">
Phase 1~5 = <b>45분</b> (의사결정·분석) + <b>대본 작성</b> (script-pd가 자동) + <b>영상 제작</b> (사용자)
</div>
</div>

---

## ❓ FAQ (초보자가 자주 묻는 것)

<details>
<summary><b>Q: 어디부터 봐야 하나요?</b></summary>
<p>🎯 <b>오늘의 주제 탭</b>. 우리 카테고리 카드의 🔥 재편집 재폭발 묶음 첫 번째 주제부터.</p>
</details>

<details>
<summary><b>Q: 분석 결과 너무 많아서 어떻게 봐야 할지 모르겠어요</b></summary>
<p>3개만 보세요:<br>
1. <b>공통 후크 유형</b> — 우리도 같은 유형으로<br>
2. <b>첫 사건 평균 시점</b> — 우리도 같은 시점에<br>
3. <b>시그너처 어휘</b> — 우리 본문에 박기</p>
</details>

<details>
<summary><b>Q: autopsy에 던지는 영상 어떻게 골라요?</b></summary>
<p><b>같은 카테고리 + 비슷한 효율 + 3~5편</b>. 1편만 던지면 패턴 안 나옴. 시니어랩의 [🔥 분석] 버튼 활용하면 자동.</p>
</details>

<details>
<summary><b>Q: 단조도가 25 나왔어요. 위험한가요?</b></summary>
<p>🟠 반복 신호 단계. 다음 영상은:<br>
1. 시그너처 어휘 줄이기 (영상당 5번 → 2번)<br>
2. Hook 패턴 변경 (충격사건형 → 회상형)<br>
3. 인물명·주제 갱신</p>
</details>

<details>
<summary><b>Q: 클릭베이트 점수가 7/10 나왔어요. 너무 자극적인가요?</b></summary>
<p>카테고리 평균이 6.5 정도면 7은 적정. 9+는 신뢰도 떨어져 retention ↓ — <b>카테고리 평균 ± 1 안에 두기</b>.</p>
</details>

<details>
<summary><b>Q: 매일 봐야 하나요?</b></summary>
<p>의무 X. 주 1~2회 충분. 매일 보면 같은 데이터 반복 — 효율 영상은 1~2주 단위 변경.</p>
</details>

<details>
<summary><b>Q: 우리 영상도 autopsy로 분석할 수 있나요?</b></summary>
<p>✅ 발행 24시간 후 던지세요. 다른 영상과 비교해서 차이점 찾고 다음 영상 개선.</p>
</details>

<details>
<summary><b>Q: LLM 썸네일 분석 비용은?</b></summary>
<p>영상당 ~$0.005 · 30편 ~$0.15 · 100편 ~$0.50. 한 번 분석한 영상은 영구 캐시.</p>
</details>

<details>
<summary><b>Q: 모바일에서도 보이나요?</b></summary>
<p>✅ 반응형. 다만 데스크탑이 정보 위계 명확.</p>
</details>

---

## 🆘 트러블슈팅

<div class="compare">
  <div class="compare-box bad">
    <div class="head">⚠️ 흔한 문제</div>
    <ul>
      <li>분석 시작 버튼 안 됨</li>
      <li>autopsy 실패 (자막 없음)</li>
      <li>[🔥 분석] URL prefill 안 됨</li>
      <li>Cloudflare 배포 늦음</li>
    </ul>
  </div>
  <div class="compare-box good">
    <div class="head">✅ 해결법</div>
    <ul>
      <li>Cmd+Shift+R 하드 새로고침</li>
      <li>다른 영상 시도 (자막 있는)</li>
      <li>콘솔(F12) sessionStorage 확인</li>
      <li>1~2분 대기 후 새로고침</li>
    </ul>
  </div>
</div>

---

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

## 🔗 외부 링크

- **사이트**: https://arrange-yt-scanner.pages.dev
- **GitHub**: https://github.com/cmpark0401-hash/arrange-yt-scanner
- **API 키 발급** (LLM 분석): https://console.anthropic.com/

---

## 📝 마지막 한 마디

<div class="tldr">
<div class="tldr-title">💡 데이터 + 직관 = 좋은 영상</div>
<div class="tldr-body">
TubeHacker는 <b>데이터를 보여주는 도구</b>. <b>결정은 사람이 합니다</b>.<br><br>
데이터가 보여주는 패턴 + 사용자의 카테고리 직관 + 채널 톤 = 최고의 영상.<br>
매번 7-Phase 따라하다 보면 본인만의 패턴이 보입니다. 그게 진짜 노하우입니다.
</div>
</div>

_TubeHacker · 유튜브 알고리즘 해킹의 모든 것_
