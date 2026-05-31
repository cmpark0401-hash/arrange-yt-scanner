# 📖 TubeHacker 사용 가이드

**유튜브 알고리즘 해킹의 모든 것** — 발견 → 검증 → 청사진 → 제작까지 한 사이클.

<div class="tldr">
<div class="tldr-title">⚡ TL;DR — 3줄 요약</div>
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

## 🖼️ 사이트 한눈에 보기

<div class="mock">
  <div class="mock-header">
    <span style="font-size:18px;">🇰🇷</span>
    <span class="mock-brand">TubeHacker</span>
    <span class="mock-slogan">· 유튜브 알고리즘 해킹의 모든 것</span>
    <div class="mock-chips">
      <span class="mock-chip warn">🚨 시그널 <b>9</b></span>
      <span class="mock-chip hot">🔥 폭발 <b>150</b></span>
      <span class="mock-chip">🆕 24h <b>65</b></span>
      <span class="mock-chip">🇯🇵 JP</span>
    </div>
  </div>
  <div class="mock-tabs">
    <span class="mock-tab on">🏠 대시보드 홈</span>
    <span class="mock-tab">🎯 오늘의 주제</span>
    <span class="mock-tab">🔥 Hot키워드</span>
    <span class="mock-tab">🔬 과학 트렌드</span>
    <span class="mock-tab">🎙️ 시니어랩</span>
    <span class="mock-tab">🔥 왜 이 영상은 터졌는가?</span>
    <span class="mock-tab">🏆 패턴 라이브러리</span>
    <span class="mock-tab">📖 가이드</span>
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

**언제 보나**: 매일 아침 30초 확인용.

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
