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

## 📺 매일 1편 만들기 — 워크보드 → 채팅창 → 발행 (5단계 자동화 흐름)

> **이 페이지를 화면 한쪽에 띄워두고, 클로의 채널별 채팅창은 다른 쪽에 띄워두세요.** 이 흐름대로 따라가면 매일 1편 발행 가능합니다.

### ⚡ 한 줄 요약

```
📋 워크보드에서 토픽 선정 → 📋 명령 복사 → 💬 채팅창 붙여넣기 → ✍️ 대본 자동 → 📤 발행
```

### 🎯 5단계 도식 (이대로만 따라하세요)

```
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 1.  📋 데일리 워크보드 열기                                      │
│          https://arrange-yt-scanner.pages.dev/workboard.html        │
│          → 4채널 × 7카테고리 = 약 20+ 토픽 한눈에 보기                │
│                                                                      │
│          🔥 단일폭발 🚨 시의성 📚 시리즈 ✨ evergreen                │
│          🔁 재편집  🔀 카테고리교차  💎 보유 대본                    │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 2.  🎯 오늘 만들 토픽 1개 결정                                  │
│          평가 기준: ⭐ rating + 카테고리 + 채널 컨디션                │
│          • 처음이면 → ✨ evergreen(검증된 안전) or 💎 보유 대본 추천  │
│          • 시간 있으면 → 🔥 단일폭발(시의성 골든타임)                │
│          • 시리즈 진행 중이면 → 📚 시리즈 다음 EP 우선                │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 3.  🚀 토픽 카드 → "새 채팅창 명령" 펼치기 → [📋 복사] 클릭     │
│          (보라색 박스 안에 자동 생성된 자연어 명령)                  │
│                                                                      │
│          예: "지식록 채널 워크보드 kn-... 작업 시작.                 │
│               카테고리: 단일폭발 · 주제: "..."                       │
│                · A 영상: ... · B 영상: ... · C 각도: ...             │
│               대본 만들어줘."                                        │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 4.  💬 해당 채널의 클로 채팅창 열기 → Cmd+V → Enter            │
│          채널별로 별도 채팅창 1개씩 유지 권장 (지식록·잘듣네·과만세·야담) │
│                                                                      │
│          → script-pd 스킬 자동 발동                                  │
│          → 워크보드 데이터 자동 로드 (A·B·C 소스)                    │
│          → 제우스 노하우 박스 (검증 영상 2개 합치기)                 │
│          → 사용자에게 활용 방법(시의성/알고리즘/교차) 1~5 선택 요청   │
│          → COLLECT → ANALYZE → STRATEGY → DRAFT → REVIEW 자동 진행   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 5.  ✅ 대본 완성 → 영상 제작 → 발행 → 결과 보고                 │
│          "지식록 워크보드 kn-... 발행됨 URL=https://youtu.be/xxx"   │
│          → 워크보드 status=published + video_url 자동 저장          │
│          → 다음날 모니터링으로 효율 자동 추적                        │
└─────────────────────────────────────────────────────────────────────┘
```

### ✅ 처음 시작하는 분 체크리스트

매일 작업 전 1회 점검:

- [ ] **클로(Claude Code) 설치 완료** — Mac/Windows 데스크탑 앱
- [ ] **autoworkers-script 프로젝트 폴더 열기** — VS Code or 터미널
- [ ] **4채널 폴더 존재 확인** — `channels/{knowledge-archive, nn-flix, science-world-life, yadam}/`
- [ ] **TubeHacker 대시보드 열어두기** — https://arrange-yt-scanner.pages.dev
- [ ] **채널별 채팅창 4개 준비** — 클로 사이드바에서 New Chat × 4 (지식록·잘듣네·과만세·야담)

### 🪟 화면 배치 권장

```
┌──────────────────────────┬──────────────────────────────────────────┐
│                          │                                          │
│  📋 TubeHacker 가이드/    │  💬 클로 채팅창 (해당 채널)              │
│     워크보드              │                                          │
│  (왼쪽 모니터 or 절반)   │  (오른쪽 모니터 or 절반)                 │
│                          │                                          │
│  - 토픽 보기              │  - 자연어 명령 입력                     │
│  - "📋 복사" 버튼         │  - script-pd 자동 진행                  │
│  - 진행 상태 확인         │  - 대본 검토·수정                       │
│                          │                                          │
└──────────────────────────┴──────────────────────────────────────────┘
```

### 🎬 채널별 채팅창 운영 권장

각 채널 1개 채팅창 유지 (영상별 X). 채팅창은 그 채널의 **연속된 작업 컨텍스트** 보관:

| 채널 | 채팅창 1개 → 누적 |
|---|---|
| 📈 지식록 | 경제·시사 톤 일관성 + 메인 시리즈 EP 누적 |
| 🌙 잘듣네 | 인물·교양 위로 톤 + 부모 세대 시리즈 EP 누적 |
| 🔬 과만세 | 과학·건강 시니어 톤 + AI 시대 모순 시리즈 |
| 📜 야담 | 지역 사료 + 조선 인물 시리즈 |

> 새 채팅창은 채널 메모리·이전 작업 흐름 잃어버림. **채널당 1개 채팅창 유지**가 효율 최대.

### 💡 시나리오별 빠른 답변

**Q: 워크보드에 단일폭발 카테고리가 비어있어요**
→ 단순 시점 문제. evergreen / 시리즈 / 보유 대본부터 진행. 다음 monitor 사이클(매일 9시·21시) 후 새 폭발 신호 들어옴.

**Q: 채팅창에 명령 붙여넣었는데 script-pd가 자동으로 안 발동돼요**
→ "지식록 채널 영상 만들어줘" / "대본 만들어줘" 추가하면 무조건 발동. 또는 워크보드 명령 박스의 마지막 줄 "대본 만들어줘" 확인.

**Q: 같은 채널에서 어제 작업 이어서 하려면?**
→ "이어서 해줘" / "지난번 프로젝트 상태 확인해줘" — script-pd가 마지막 상태 자동 감지.

**Q: 워크보드 토픽이 마음에 안 드는데 새 추천 받으려면?**
→ "오늘 데이터로 추천 다시 만들어줘" → 4채널 × 7카테고리 재분석 + 워크보드 갱신.

**Q: 워크보드를 안 거치고 그냥 만들고 싶어요**
→ 채팅창에서 "X 주제로 만들어줘" 직접 입력. script-pd가 워크보드 없이 기존 흐름으로 진행 (제우스 노하우 박스 표시).

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

### 🚨 4단계 — 자가진단 체크리스트 (REVIEW_FINALIZE 시점 강제)

> **출처**: 김히엉 트리거롱폼 강의 PDF p116. AI 양산 채널 수익 정지 회피의 핵심.
> 강사 명시: "**사람이 등장하는 대형 채널도 수익 정지된다 — AI/사람 무관, 가이드라인 준수가 핵심**"

<div class="compare">
  <div class="compare-box good">
    <div class="head">✅ 4가지 다 OK 여야 통과</div>
    <ul>
      <li>□ 내 고유의 아이디어/관점이 담겨있나?</li>
      <li>□ 창작자의 해설·통찰이 있나?</li>
      <li>□ 시청자에게 정보·즐거움·위로를 주나?</li>
      <li>□ <b style="color:var(--danger);">템플릿으로 대량 복제 가능한 구조 X</b></li>
    </ul>
  </div>
  <div class="compare-box bad">
    <div class="head">🎬 대본 자동 적용 (DRAFT 단계)</div>
    <ul>
      <li>반어형 Hook 1순위 강제 ("X가 가장 빛났던 순간 무너졌습니다")</li>
      <li>3막 8장 구조 (1,300자 × 8장 ≒ 20분)</li>
      <li>시대 점프 패턴 ("옛날엔 → 결정적 계기가 → 지금은")</li>
      <li>공감 키워드 (체화된 경험: "월급 빼고 다 오른다")</li>
      <li>채널 페르소나·톤 시그니처 (description.md 참조)</li>
    </ul>
  </div>
</div>

<div class="insight">
  <div class="insight-tag">💎 정관장 비유 — 레드오션 진입 정당화 (PDF p99-101)</div>
  <div class="insight-section"><b>홍삼 시장 1조 3천억 · 정관장 75% 점유</b> · 2위 점유율 2~5% = 매출 587억</div>
  <div class="insight-section">→ "큰 시장일수록 일부만 점령해도 들어오는 수익 크다" · 0.3% = 50억</div>
  <div class="insight-section"><b>적용</b>: 야담·과만세도 레드오션 정당. 블루오션 1등 노리지 마라.</div>
</div>

### 📊 5단계 — 배포 후 모니터링

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

## 📋 데일리 워크보드 (NEW · 6/3)

> **위치**: 헤더 우측 `📋 데일리 워크보드` chip (보라 그라데이션 + 빨간 날짜 배지)

매일 채팅에서 묻고 흩어지던 4채널 주제 추천을 한 페이지에 정리·누적·히스토리화.

### 📂 7가지 분류 기준 (모든 채널 매일 분류)

<div class="steps">
  <div class="step">
    <span class="step-num">🔥</span>
    <div class="step-title">단일 폭발</div>
    <div class="step-body">타채널 <b>2일 이내</b> 조회수 폭발 (시의성 단발 검증)</div>
  </div>
  <div class="step">
    <span class="step-num">🚨</span>
    <div class="step-title">시의성</div>
    <div class="step-body">현재 트렌드·뉴스 기반 (오늘 만들면 골든타임)</div>
  </div>
  <div class="step">
    <span class="step-num">📚</span>
    <div class="step-title">시리즈 다음 회차</div>
    <div class="step-body">메인 시리즈 IP EP.N (AI 양산이 못 함)</div>
  </div>
  <div class="step">
    <span class="step-num">✨</span>
    <div class="step-title">검증 evergreen</div>
    <div class="step-body">Hot키워드 누적 검증 (시기 무관 잘 통함)</div>
  </div>
  <div class="step">
    <span class="step-num">🔁</span>
    <div class="step-title">재편집 재폭발</div>
    <div class="step-body">같은 주제 다시 신호 (변형 기회)</div>
  </div>
  <div class="step">
    <span class="step-num">🔀</span>
    <div class="step-title">카테고리 교차</div>
    <div class="step-body">다른 분야 폭발 → 우리 채널 톤으로 변환</div>
  </div>
  <div class="step">
    <span class="step-num">💎</span>
    <div class="step-title">보유 대본 우선</div>
    <div class="step-body">이미 작성된 미발행 대본</div>
  </div>
</div>

### 🎯 4채널 메인 시리즈 IP (AI 양산이 못 하는 차별화)

<div class="insight">
  <div class="insight-tag">💎 우리 시스템만 가능한 시리즈 (다른 채널 따라 못함)</div>
  <div class="insight-section"><b>📈 지식록</b>: "오늘 동시에 터진 영상 5편이 가리키는 한국" — TubeHacker 매일 데이터 → 통찰 (개인 못 봄)</div>
  <div class="insight-section"><b>🌙 잘듣네</b>: "당신 부모님이 살아냈던 그날" — 시청자 ↔ 부모 세대 ↔ 한 인물 3중 교차 (단순 위인 X)</div>
  <div class="insight-section"><b>🔬 과만세</b>: "AI도 못 푼 우리 몸/우주의 한 가지" — AI 시대 메타 모순 (AI가 못 만듦)</div>
  <div class="insight-section"><b>📜 야담</b>: "당신 고향에서 살았던 그 사람" — 지역 사료 (AI 학습 데이터 빈약, 전국 시·군 × 조선 500년)</div>
</div>

### 💬 클코 자연어 명령 (다음 같은 채팅창)

```
"오늘 데이터로 추천 다시 만들어줘"      → 4채널 × 7카테고리 재분석 + 워크보드 갱신
"지식록 단일폭발 시작"                  → status=in_progress + script-pd 진입 안내
"지식록 시리즈 드래프트 완료"           → checklist.draft=true + events 추가
"잘듣네 evergreen 발행 URL=..."         → status=published + video_url
"야담 보유대본 보류"                    → status=hold
```

→ 모든 변경 시 클코가 JSON 직접 편집 + 빌드 + git push 자동.

---

## 🌟 김히엉 트리거롱폼 강의 학습 결과 (NEW · 6/3)

> **출처**: 영상 8h49m + PDF 247p 종합 학습. 영상 70%는 자기 서사·세일즈, 실제 노하우 30%만 추출.

### ✅ 즉시 적용 (모든 채널 자동)

<div class="steps">
  <div class="step">
    <span class="step-num">1</span>
    <div class="step-title">🚨 자가진단 체크리스트</div>
    <div class="step-body">REVIEW_FINALIZE 강제. AI/사람 무관 가이드라인 준수가 모든 것을 결정 (PDF p118)</div>
  </div>
  <div class="step">
    <span class="step-num">2</span>
    <div class="step-title">🪝 반어형 Hook 1순위</div>
    <div class="step-body">"X가 가장 빛났던 순간 무너졌습니다" — Hook 3후보 중 1개 의무</div>
  </div>
  <div class="step">
    <span class="step-num">3</span>
    <div class="step-title">📐 3막 8장 구조</div>
    <div class="step-body">1,300자 × 8장 = 약 20분. 시대 배경 → 사건 → 변화 → 대체제 → 클로징</div>
  </div>
  <div class="step">
    <span class="step-num">4</span>
    <div class="step-title">⏳ 시대 점프 + 공감</div>
    <div class="step-body">"옛날엔 → 결정적 계기가 → 지금은" / 체화된 경험("월급 빼고 다 오른다")</div>
  </div>
  <div class="step">
    <span class="step-num">5</span>
    <div class="step-title">🎭 채널 페르소나</div>
    <div class="step-body">강사=쫄라맨 / 우리=음성. 나레이션 시그니처로 페르소나 (description.md)</div>
  </div>
  <div class="step">
    <span class="step-num">6</span>
    <div class="step-title">🎬 숏폼 낙수 효과</div>
    <div class="step-body">롱폼 1편 → 30~60초 하이라이트 1~3편 → 같은 채널 유입</div>
  </div>
</div>

### 🧠 시청자 본능 8가지 변주 (소재 풀 확장)

강사의 "몰락"이 통한 이유 = **Schadenfreude** (남의 불행에 안도) + 사회적 비교 + 공정성 + 위협 회피. 같은 본능 다른 변주:

| 패턴 | 본능 | 우리 활용 (채널별) |
|---|---|---|
| 🔥 추락·몰락 | 안도감 | 지식록 시사 |
| ⚖️ 자업자득·사이다 | 공정성 | 야담 권선징악 |
| 🤫 금기·비밀 | 호기심 | 과만세 충격 사실 |
| 👤 숨은 영웅 | 소속감 | 잘듣네 인물·야담 |
| ⚔️ VS·대결 | 양극 비교 | 지식록 한국 vs 일본 |
| 🚨 위협·경고 | 생존 | 지식록·과만세 |
| 🎢 신분 역전 | 카타르시스 | 야담 7살 노비 |
| 🕰️ 시간 점프 | 결과론 | 잘듣네 100년 후 |

### 🚫 강사 명시 금지 13가지

1. 원본 그대로 카피 (저작권) · 2. AI 풀자동 딸각딸각 · 3. 이미지 슬라이드만 · 4. 자막만 바꿔서 다채널 · 5. 벤치마킹 스크립트 복붙 · 6. 블루오션 1등 노리기 · 7. RPM만 노리기 · 8. 회피 우선 · 9. 같은 영상 다채널 · 10. 클로징 요약 · 11. WAV 그대로 · 12. 단일 카테고리 · 13. "사람 등장이라 안전" 미신

### 💎 정관장 비유 — 레드오션 진입 정당화

홍삼 시장 1조 3천억의 **2위(2-5%) = 587억**. "큰 시장 0.3%만 먹어도 50억" → 블루오션 1등 노리지 마라.

---

## 💰 에드센스 운영 가이드 (월억남 학습 노트)

> **출처**: 월억남 "에드센스 끝판왕 + 현시점 유튜브 대처법" 학습. 원문 인용 없이 패턴·구조만 변형 정리. 회색지대 기법은 사용자 판단 영역으로 명시.

<details>
<summary><b>📖 펼쳐서 보기 — 에드센스 7가지 핵심 + 다채널 전략</b></summary>

### 1️⃣ 에드센스 = 유튜브용 은행 (개념)

`유튜브 채널 수익 발생 → 에드센스에 달러 입금(매월 10일) → 내 은행 계좌 입금(매월 21~26일)`. 채널과 에드센스는 분리된 시스템이고, 채널 단위가 아니라 **에드센스 계정 단위**로 수익이 합산됨.

### 2️⃣ 활성화된 에드센스를 만드는 2가지 경로

| 경로 | 조건 | 주의 |
|---|---|---|
| **자력 1차 수창** | 구독 500 + 영상 3개 + 롱폼 3000h or 숏폼 300만뷰 | 연결 반려 시 즉시 재시도 가능 |
| **수창 채널 "변경" 버튼** | 이미 수익화된 채널에서 다른 에센으로 연결 | **반려 시 32일 lock — 채널 수익 멈춤** |

> **에드센스 홈페이지에서 미리 가입 금지** — 구글 공식 문서에 "다른 사이트에서 만든 계정은 작동하지 않음" 명시. 반드시 YouTube Studio에서 시작.

### 3️⃣ 4단계 정산 준비 (순서가 중요)

```
① 본인인증     명의·전화번호·주소·주민 앞자리
② 주소인증     본인인증 주소로 핀번호 우편 (2~4주)
③ 미국 세금정보  W-8BEN (개인) / 사업자번호 (개인사업자)
④ 계좌 입력    SWIFT 코드 + 외화 입금 가능 계좌
```

- **개인**: 위 순서 그대로
- **개인사업자**: ③ 세금정보를 먼저 (TIN에 사업자번호 입력)
- **법인사업자**: 연결 시 계좌유형을 "조직/회사명"으로 (변경 불가)

### 4️⃣ 본인인증 단계 핵심 주의사항

- **45일 이내 본인인증** 미완료 시 에센 막힘
- 명의자 + 그 명의 핸드폰 + 요금제(알뜰폰/SKT 등) 정확히 선택 — 3회 틀리면 24시간 lock
- 본인인증 명의 = 세금정보 명의 일치 필수
- **본인인증 명의 = 진짜 에센 소유자**가 됨 (연결 시 입력한 명의가 자동 교체됨)

### 5️⃣ 주소인증(핀번호) 단계 — 러브레터를 기다리는 마음

- 본인인증 주소로 핀번호 우편 자동 발송 (2~4주 소요)
- **6자리를 추측하지 말 것** — 3회 틀리면 에센 닫힘
- 3주 후 "PIN 다시 보내기" 가능 (단, 핀번호는 동일)
- 핀번호가 늦게 와도 지난 달 수익은 입력 후 며칠 내 즉시 처리

### 6️⃣ 세금정보 입력 (W-8BEN)

- **TIN 번호에 주민번호 넣지 말 것** (개인의 경우) — 미국 시청자 비중 낮으면 차이 미미
- **개인사업자**: TIN = 사업자번호 → 영화·서비스·저작권 원천징수 10/0/10% 적용
- 입력 후 신분증(주민/여권/운전면허) 추가 제출 요구 자주 발생
- 이름은 영문 발음 그대로 (예: "Hong Gildong" → 발음 일치 시 신분증 인증 면제 케이스 多)

### 7️⃣ 계좌 입력 — 명의 분리 가능

- 에센 명의 ≠ 계좌 명의 OK (가족·법인 계좌로 받기 가능)
- **세금 처리는 계좌 명의자가 함** (돈 받는 사람이 세금 처리)
- 겸업 금지·연금 대상자 우려 → 가족 계좌로 분산

### 🚧 현시점 유튜브 억까 4종 + 대응 메뉴얼

| 케이스 | 위험도 | 대응 |
|---|---|---|
| 🔴 채널 삭제 (스팸/가이드) | 채널 자체 폐쇄 | 항소 대본으로 2~3주 간격 재항소 |
| 🟡 재사용 컨텐츠 (수창 정지) | 에센 연좌제 드뭄 | 항소 + 시도 |
| 🟠 관련 채널 (수창 정지) | 에센 연좌제 반반 | **묶인 다른 채널 즉시 다른 에센으로 대피** |
| 🔴 허위 컨텐츠 (수창 정지) | 에센 연좌제 多 | **항소 X, 즉시 다른 채널 대피만** |

> **핵심**: 항소·이유 찾기보다 **대응이 우선**. 통제 불가능한 상황에 감정 넣지 말고 기계적으로 1채널 1에센 분산 + 묶인 채널 대피.

### 💎 다카테 다채널 다에센 전략 (월억남 핵심 철학)

- **영원한 1황 카테고리는 없다** — 트렌드 따라 갈아탈 수 있는 분산 구조
- **1에센 1채널이 이상적** — 연좌제 리스크 최소화
- **방패채널** — ACCS Market·SWAPD에서 저품질 수창 채널 ($40~60) 사서 활성화 에센만 찍어내기
- **다카테 운영의 본질** — 리스크 분산 + 자동사냥(외주) + 채널 수확(판매) 3중 효과

### ⚠️ 회색지대 기법 (월억남 책 내용, 사용자 판단 영역)

월억남 책에는 1인 다에센 만드는 우회 기법(뻥데이터 연결·번호 변경 반복·듀얼넘버·알뜰폰 다개통 등)이 상세히 나옴. **이는 구글 정책 "1인 1에센" 위반 가능성이 있고, 적발 시 에센 일괄 정지·수익 몰수 리스크가 있음.** 합법 운영을 원하면:

- ✅ 본인 명의 1에센 + 다채널 연결
- ✅ 가족 명의 분리 (단, IP/주소/결제수단 겹치면 적발)
- ❌ 본인 명의 다에센 우회 → 회색지대, 위험 감수도는 본인 판단

### 💼 추천 도구 / 사이트

- **방패채널 구매**: [DealBaron (구 ACCS Market)](https://dealbaron.com/youtube), [SWAPD](https://swapd.co)
- **활성화 에센 구매**: [퀄리튜브](https://qualitube.site) (부자프로그램 운영)
- **단순 SMS 인증**: HERO SMS (해외 가상번호)
- **알뜰폰 비교**: [모요](https://www.moyoplan.com) (월 100원~3000원)
- **참고 도서**: 부자프로그램 "연좌제 방지 완벽 가이드"

</details>

---

## 🛒 채널 구매·소유권 이전 가이드 (영상 4편 + 웹리서치 + 시도남 강의 종합)

> **출처**: YouTube 영상 4편(P14CtfpbcYo, eZmLtGLlEQE, sIfW8U36JzU, I6jgyr4yixo) + **시도남 노멀쇼츠 1기 특강 PDF 392p** + 강의 녹취록 + 구글 공식문서 + brunch 실전 사례 + Creator Hero 가이드.
>
> **핵심 슬로건 (시도남)**: *"새로 만들지 마세요. 잘된 걸, 다시 굴리세요"* / *"0부터 만들지 않는다. **시간을 산다**"* / *"싸게 사기보다 안전하게 사기"*
>
> **핵심 숫자 3개**: **7일**(소유권 승격) · **32일**(에센 변경 lock) · **30일**(인수 후 침묵 권장)

<details>
<summary><b>📖 펼쳐서 보기 — 시세 → 4단계 워크플로우 → 7일 룰 → 30일 운영</b></summary>

### 🎯 시도남 4단계 워크플로우 (한눈에)

```
1단계. 채널 탐색       │ 수창 활성 + 가격대 20~30만원
2단계. 채널 검증       │ 노란딱지·저작권 이력 + 30일 노출 추이 + 에센 변경 가능 여부
3단계. 안전 거래       │ 에스크로 거래 + 소유권 이전 후 잔금
4단계. 7일 안정화      │ 위험영상 X + 템플릿 유지 + 1일 1영상
```

> 0부터 키우기 = 평균 **3~N개월**. 채널 구매 = **즉시 운영 가능** + 구독자 1,000명/시청시간 4,000h **이미 완료**. 20~30만원대로 시작 가능.

### 💰 시세 정보 (시도남 강의)

| 루트 | 가격 |
|---|---|
| 일반 시세 | 약 **50만원** |
| 검증된 직거래 루트 | 약 **20~30만원대** |

> **가격 격차 = 정보 격차** — 중간 마진 없는 직거래 + 검증된 셀러 풀 + 협상 가능 구조. 구독자당 단가 400~500원 상한 기준.

### 1️⃣ 채널 구매 전 체크리스트 (사기 예방)

판매자가 가장 흔히 속이는 3가지: **(a) 수익 인증 스샷 위조, (b) 정책 위반 은폐, (c) 실제 소유자 ≠ 판매자**.

> **🔥 시도남이 강조하는 "절대 확인할 3가지"** — 다른 건 다 양보해도 이 3개만은 무조건 확인:
> 1. **수익창출 활성 상태인가** (Studio 라이브 화면공유)
> 2. **노란딱지/저작권 이력 없는가**
> 3. **채널 소유권 이전 100% 가능한가** (Brand Account 상태)

| 점검 항목 | 확인 방법 | Red Flag |
|---|---|---|
| **진짜 수익 인증** | 판매자 **화면공유**로 Studio → 수익 → 최근 28일/365일 라이브 클릭 | "스샷만 드릴게요" |
| **커뮤니티 가이드 경고** | Studio → 설정 → 채널 → 기능 자격요건 라이브 확인 | "이전 운영 모른다" |
| **저작권 스트라이크** | Studio → 콘텐츠 → 제한사항 + 저작권 페이지 진입 | Content ID 클레임 多 |
| **수익화 정책 위반** | Studio 수익화 탭 "사용 설정됨"인지 ("검토 중/제한" 아닌지) | 노란 달러 영상 多 |
| **시청자층 일치** | 분석 → 잠재고객 → 국가/연령 매칭 여부 | 인도·동남아 비중 압도적 (저단가) |
| **구독자당 단가** | 1명당 **400~500원** 상한 | "10만 구독자에 1억" 호가 |
| **휴면 기간** | 최근 6개월 무업로드 = 알고리즘 휴면 (유튜브 6개월 법칙) | 장기 무업로드 후 수익만 강조 |
| **실제 소유자** | 거래 직전 **본인을 임시 관리자로 추가** 요청 | 거부 / "비번 드릴게요" |

- [ ] **에스크로 거래** (소셜러스·앵커딜 등) 또는 안전 거래 플랫폼 경유
- [ ] **계약서 작성**: 자산 명세 + 하자담보 + 비경쟁 + 진술보증
- [ ] **계정 ID/비번 직거래 절대 금지** — 약관 위반 + 사기 단골 경로

#### 💡 시도남 거래 꿀팁 (TIP 슬라이드)

- **판매자 순위 20위 안**에서 구매 (검증된 셀러 풀, 분쟁 시 평판 리스크가 셀러 측에 큼)
- **여러 개 묶음 구매 시 가격 조정** 요청 (1개 30만원 → 3개 묶음 70만원 등)
- **AS 미리 요구**: 계약서에 *"5편 업로드 시 조회수 100 미달이면 교체 요청"* 같은 조건 명시
- 문제 발생 시 **에스크로 중재자에 즉시 도움 요청** (이메일·증빙 정리 보관)

> **시도남 안전거래 원칙**: *"싸게 사기보다 안전하게 사기"* — 에스크로 + 소유권 이전 완료 후 잔금. 직거래 X.

### 2️⃣ 소유권 이전(Brand Account) 절차 — 7일 룰

> 핵심: 채널은 반드시 **브랜드 계정**이어야 함. 개인 계정은 이전 불가.

```
[판매자]                                          [구매자]
0. 개인→브랜드 계정 전환
   (설정→채널→고급설정→"브랜드 계정으로 이동")
        ↓
1. Studio→설정→권한관리
   → 사람+ 아이콘 → 구매자 이메일 입력
   → 역할 "소유자" 선택 → 초대
        ↓                                       2. 이메일 수신 → 초대 수락
                                                 → 공동 소유자(co-owner) 상태
        ↓
        ⏳ 7일 보안 대기 (구글 강제)
        ↓
3.                                              4. 7일 경과 후
                                                 → 권한 화면에서
                                                 본인을 **"주 소유자"**로 승격
        ↓
5. 판매자는 자동 "관리자" 강등
   → 구매자가 판매자 계정 제거 (권장)
```

> **7일 룰의 의의**: 사기 차단. 잔금은 7일 경과 + 주 소유자 승격 완료 후 마지막 조각만 남기는 **에스크로 구조**가 안전.

### 3️⃣ 구매 직후 즉시 (7개 보안 작업)

- [ ] **1) 구글 계정 비밀번호 변경** — 16자+ 영대소+숫자+특수, 재사용 금지
- [ ] **2) 2단계 인증(2SV) 활성화** — 패스키 or OTP 앱 (SMS만은 SIM 스와핑 위험)
- [ ] **3) 복구 이메일·전화 본인 것으로** 갱신
- [ ] **4) 결제 정보·세금 정보 초기화** (payments.google.com)
- [ ] **5) 채널 이름/핸들은 점진 변경** (전면 변경 시 알고리즘 노출 급락)
- [ ] **6) 본인인증** (15분+ 업로드·커스텀 썸네일은 채널별 재인증 필요)
- [ ] **7) 에드센스는 32일 룰 의식하고 마지막에** (§4 참조)

### 4️⃣ 에드센스 연결 변경 — 32일 lock-in 함정

> **가장 많은 사고 지점.** 잘못 누르면 32일 수익 0원.

**3대 원칙**:
1. **에드센스는 이전되지 않는다** — 판매자 에센은 판매자 것. 구매자는 자기 에센 새로 연결.
2. **연결 변경은 32일에 1회만 가능** — 잘못 끊으면 한 달간 못 붙임 = 수익 정산 보류.
3. **1인 1에드센스가 공식 정책** — 본인 명의 에센 우선.

**권장 순서**:
- [ ] A. **활성화된 에드센스 미리 준비** (본인 명의 미승인 시 블로그/다른 사이트로 우선 승인)
- [ ] B. **채널 소유권 이전 7일 완전 종료 확인** (주 소유자가 본인이어야 변경권 발생)
- [ ] C. **Studio → 수익 → 애드센스 계정 "변경"** (32일 카운터 시동)
- [ ] D. **본인 에드센스 연결** (24시간 내 반영)
- [ ] E. **세금정보(W-8BEN/W-9), 결제 수단, 주소 본인 명의로** 입력
- [ ] F. **본인인증** 요청 시 즉시 제출 (미제출 시 지급 보류)

> 휴면 에드센스 함정: "받기만 하고 안 쓰던" 에센은 연결 즉시 본인인증·세금정보 갱신 요청 多 → 거래일 D-7 이전에 미리 로그인 점검.

### 5️⃣ 강의 노트 (녹취록 + 시도남 PDF 기반) — 구매 후 30일 액션 플랜

| 시점 | 액션 | Why |
|---|---|---|
| **1주차** | 본인 에드센스 연결 시작 (승인 ~2주 소요) | 3주차 수익부터 본인 계좌 유입 |
| **즉시** | 기존 영상 "그대로 유지" | 삭제 시 수익 정지. 시도남: *"기존 영상 전부 삭제 = 수익창출 박탈 위험"* |
| **첫 7일** | 위험 요소 영상 X (아이·동물·피 등 sensitive) | 알고리즘이 정상 채널로 인식하는 안정화 구간 |
| **첫 7일** | 템플릿 유지 (폰트·자막·결·BGM 급변 X) | 시도남: *"카테고리·템플릿 급변경 = 노출 폭락"* |
| **초기 1~2주** | 하루 1개 업로드 → 점진 확장 | 채널이 "영상 받아주는 상태"(조회수 발생) 확인 후 4개/일까지 |
| **시점 무관** | 깔끔한 계정 우선 | 허위·재사용 오염된 채널 → 영상 다 지우고 키우기는 비추 (멘탈 관리) |
| **1~2채널 집중 시** | 쿠팡 파트너스 연동 | 유튜브 수익의 +10% 부가수익 (월 100만 → +10만) |
| **다채널 진입 시** | 각 채널 다른 명의 에센 | IP는 위험 적음, **명의 분리가 핵심 안전장치** |

#### ❌ 시도남이 명시한 초보 실수 2가지

| 실수 | 결과 |
|---|---|
| 기존 영상 **전부 삭제** | 수익창출 박탈 위험 |
| 템플릿·카테고리 **급변경** | 노출 폭락 |

#### 🌏 다채널 합산 1등 전략 (시도남 정규강의 3주차)

- 한 채널 1등 X → **다채널 합산 1등** 사고방식
- 채널당 **100~300만원 라인** 설계 (3채널 = 월 300~900만원)
- 한국 + 일본 = **시장 분산 = 안정성** (한 채널 무너져도 라인 전체 안전)
- "잘된 건 또 잘된다" — 변주 기준 5가지: **톤·컷 수·자막·결말·시작점**

#### 📊 운영 데이터 룰 (시도남 정규강의 2주차)

- **첫 48시간** 데이터로 다음 영상 결정
- **10편 완주** 강제 룰 — 데이터가 모이는 최소 단위
- 무엇을 보고 다음 영상을 결정할 것인가 = 채널 수명을 좌우

### 6️⃣ 일반 운영 노하우 (강의 외 보완)

- **기존 카테고리 분석**: 구매한 채널이 어떤 주제로 1차 수창 통과했는지 파악. 완전히 다른 주제 전환 시 **초기 3~5편은 알고리즘이 새 타깃 찾느라 조회수 낮음** → 낙담 X, 밀고 나가기
- **예약 발행 전략**: 한 달치 일괄 예약 ❌ → 시청자 분포 시간대(퇴근·주말 직전) 분석 후 **하루 2~3회 고정 시간대** 예약 루틴
- **자력 제작 능력 선행**: "편의점 갑자기 줘도 운영할 줄 알아야" — 캡컷 등으로 1분 미만 하이퀄 쇼츠 제작 숙련도 없이는 구매 비용만 손실

### 7️⃣ 구매 후 30일 — 위험 시기 7대 리스크

| 리스크 | 트리거 | 대응 |
|---|---|---|
| 갑작스러운 수익화 일시정지 | 채널 이력 급변 (주제·패턴·IP) | 첫 30일 기존 톤·포맷 **70% 유지** |
| "관련 채널" 묶음 발동 | 다른 채널과 IP·결제·기기 공유 | **분리된 브라우저 프로필 + 다른 결제수단** |
| 정책 검토 재트리거 | 일괄 비공개·삭제 | **영상 일괄 삭제 금지** (1주 5편 이하) |
| 구 운영자 억까/신고 | 분쟁·이중판매 | 거래 증빙(에스크로·계약서·이메일) 영구 보관 |
| 댓글·배지 손실 | 브랜드 이전 직후 일부 미이관 | 인증 배지 재신청, 댓글은 사전 백업 |
| 알고리즘 노출 급락 | 일관성 끊김 | **7일 내 1편 업로드**로 생존 신호 |
| 명의 노출 (겸업 위험) | 본인 명의로 결제·계좌 등록 | 가족 명의 계좌로 분산 |

### 📌 핵심 요약 (한 줄)

> **안전 소유권 이전(7일) → 1주차 에드센스 연결 → 기존 영상 방치 → 하루 1개씩 내 영상 업로드 → 30일 침묵·점진 변경**

### 🔗 출처

**YouTube 영상**: [eZmLtGLlEQE](https://www.youtube.com/watch?v=eZmLtGLlEQE) · [sIfW8U36JzU](https://www.youtube.com/watch?v=sIfW8U36JzU) · [I6jgyr4yixo](https://www.youtube.com/watch?v=I6jgyr4yixo) · [P14CtfpbcYo](https://www.youtube.com/watch?v=P14CtfpbcYo)

**구글 공식**: [에드센스 변경 32일 룰](https://support.google.com/youtube/answer/7367146?hl=ko) · [YouTube용 에드센스 설정](https://support.google.com/youtube/answer/9914702?hl=ko) · [채널 이전](https://support.google.com/youtube/answer/6351567?hl=ko) · [채널 보호](https://support.google.com/youtube/answer/9701986?hl=ko)

**참고**: [유튜브 채널 거래 안전성 (brunch)](https://brunch.co.kr/@wordcreater/27) · [Creator Hero 가이드](https://www.creator-hero.com/blog/how-to-transfer-your-youtube-account) · [유튜브 6개월 법칙 (나무위키)](https://namu.wiki/w/%EC%9C%A0%ED%8A%9C%EB%B8%8C%206%EA%B0%9C%EC%9B%94%20%EB%B2%95%EC%B9%99)

**강의 자료**: 디하클 시도남 노멀쇼츠 1기 특강 PDF 392p (채널 직구 메인 p.274~291 + 정규강의 모듈 p.340·341·384·385) + 녹음 6편 — 학습 노트 패턴만 변형, 원문 인용 X

</details>

---

## 🔬 20개 메트릭·엔진 정의 사전 (코드 근거 + 발견 알고리즘)

> **TubeHacker 시스템에서 다루는 모든 메트릭의 정의·임계값·발견 방법.** 헤더 chip 7개 외에 시스템 내부에서 작동하는 파생 엔진 13개까지 총 20개. 모든 숫자는 코드 인용 기반.

<details>
<summary><b>📖 펼쳐서 보기 — 헤더 chip 7개 + 파생 엔진 13개 = 총 20개</b></summary>

### 🎯 A. 헤더 chip 7개 (사용자 직접 접근)

#### 1. 🚨 알고리즘 시그널 (algorithm signal)

- **정의**: 시속 5,000회+ OR 측정 간격 내 조회 5만+ 증가, 발행 3일 이내
- **입력**: `monitor_channels.py`의 영상별 조회수 시계열 (channels/*/`_monitor_history/{video_id}.json`)
- **공식**: `VELOCITY_THRESHOLD = 5000` (monitor_channels.py:43), `SIGNAL_DELTA_THRESHOLD = 50000` · `velocity_per_hour = delta_views / interval_hours`
- **발견**: ① 시계열 로드 → ② 직전 vs 현재 측정 차이 계산 → ③ 시속 ≥5000 OR 절대증가 ≥50000 → ④ 업로드 3일 이내 → ⑤ 시속 내림차순
- **시각화**: `daily_{date}.html` 최상단 "🚨 알고리즘 시그널" 섹션
- **활용**: 재현 불가능한 현상 → 즉시 "왜 뜨는가" 분석 + 같은 톤 제작

#### 2. 🔥 소형 채널 폭발 (small explosion)

- **정의**: 구독 5만 이하 채널 + 효율 5배+ 또는 시속 1,000+ 또는 절대 2만+
- **입력**: 일일 채널 점검 결과 (`fetch_video_stats`)
- **공식** (monitor_channels.py:49~55): `SMALL_SUBS_LIMIT = 50_000` · `SMALL_EFF_THR = 5.0` · `SMALL_VEL_THR = 1000` · `SMALL_VIEWS_THR = 20_000`
- **발견**: 구독 ≤50K 채널 → efficiency = views/subscribers → 3조건 중 하나 만족 시 `is_hot=true, tier="small"`
- **시각화**: `daily_{date}.html` "🔬 소형 채널 폭발" 섹션 (Top 40)
- **활용**: 작은 채널의 "뉘앙스 있는 주제" 발견 → 재편집 후보

#### 3. 🐳 대형 채널 폭발 (large explosion)

- **정의**: 구독 5만 초과 + 시속 5,000+ 또는 절대 20만+
- **공식**: `LARGE_VEL_THR = 5000` · `LARGE_VIEWS_THR = 200_000`
- **발견**: 구독 >50K → tier="large" → 시속 내림차순 (효율보다 속도 중시)
- **시각화**: `daily_{date}.html` "🐳 대형 채널 폭발" (Top 40)
- **활용**: 플랫폼 전체 트렌드 반영 → 따라가면 성장 용이

#### 4. 🆕 신영상 (new video, 24h)

- **정의**: 모니터링 29개 채널의 24시간 이내 업로드
- **공식**: `is_new = upload_date >= one_day_ago` (monitor_channels.py:533)
- **시각화**: `daily_{date}.html` "🆕 신영상" (Top 40, 효율 표기)
- **활용**: 채널 현재 활동성 + 신선한 발행 트래킹

#### 5. 🎯 오늘의 주제 (today topics)

- **정의**: 검증 아카이브(proven) × 오늘 폭발 영상 교차 분석 → 카테고리별 추천
- **입력**: (a) `_proven_topics_archive.json`, (b) 오늘 모니터 결과
- **공식** (build_site.py:3420~3458): 키워드 길이 ≥2 + noisy 제외, 효율 + (시그널이면 +50) + 재업 보너스로 정렬
- **발견**: ① CATEGORIES(경제·역사·지식·심리·과학·시사·정치·인문) 순회 → ② 검증 주제 추출 (최대 8개) → ③ 오늘 폭발 제목과 substring 매칭 → ④ 스코어 정렬
- **시각화**: `recommendations.html` 카테고리별 "검증 금광" + "오늘 뜬 주제" 카드
- **활용**: 두 섹션 교집합 = "타이밍 좋은 주제"

#### 6. 🔥 Hot 키워드 (hot keywords)

- **정의**: 오늘 폭발 영상 제목 × proven 아카이브 키워드 substring 매칭
- **공식**: 키워드 길이 ≥2, `_topic_noise()` 제외 (build_site.py:3420)
- **발견**: 아카이브 키워드 풀 → 오늘 폭발 제목 substring 매칭 → 빈도 집계
- **활용**: "지금 알고리즘+사용자가 동시에 좋아하는" 정확한 신호

#### 7. 🧪 과학 트렌드 (science trends)

- **정의**: 과학 시드 키워드로 검색한 신규 채널 + 폭발 영상
- **공식** (explore_science.py:28~29): `EXPLOSION_VIEWS = 100_000` · `PER_KEYWORD = 15` · 롱폼 ≥60초
- **발견**: ① 과학 시드 로드 → ② ytsearch (키워드당 15편) → ③ 등록·블록 제외 → ④ hit_count ≥2 채널 = "반복 검색되는 채널" → ⑤ 조회 100K+ 영상만 폭발 분류
- **시각화**: `science_{date}.html` (상단 신규 채널 TOP, 하단 폭발 영상 TOP 30)
- **활용**: 새 시드 추가하면 미발견 채널 발굴 가능

---

### 🛠️ B. 파생 엔진 13개 (자동 백그라운드)

#### 8. ⚠️ 발행 중단·둔화 경고 (decline warning)

- **정의**: 평소(14일) 대비 최근(7일) 발행 빈도 20% 이하 급감 채널
- **공식** (monitor_channels.py:45~47): `DECLINE_THRESHOLD = 0.20` · `BASELINE_WINDOW = 14` · `RECENT_WINDOW = 7`
- **발견**: EMA(지수이동평균) 발행율 갱신 (0.7×기존 + 0.3×신규) → `recent_ratio = recent_weekly / baseline_weekly` → ≤0.20 → 경고
- **시각화**: `daily_{date}.html` "⚠️ 발행 중단 경고"
- **활용**: 채널 휴면 징후 즉시 감지

#### 9. 📺 외부 폭발 영상 (external explosion via news)

- **정의**: 오늘 뉴스 키워드로 검색한 등록 채널 外 폭발 영상
- **공식** (search_news_videos.py:29~33): `EXTERNAL_VIEWS_THR = 50_000` · `KEYWORDS_TOP = 8` · `PER_KEYWORD = 10`
- **발견**: ① 뉴스 RSS 로드 → ② 명사 빈도 상위 8 키워드 → ③ ytsearch × 10편 → ④ 등록·블록·5만 미달 제외 → ⑤ 상위 20편 stats
- **시각화**: `news_{date}.html` "📺 뉴스 키워드 外部 영상"
- **활용**: 뉴스 직결 타채널 폭발 = 같은 주제 제작 골든타임

#### 10. 🏷️ 자동 카테고리 분류 (auto categories)

- **정의**: 채널이 categories 명시 없으면 영상 제목 기반 자동 추정
- **공식**: 카테고리당 매칭 카운트 ≥2 → `auto_categories` 배열에 추가
- **발견**: 영상 제목 → 명사 tokenize → discover_classify_keywords.json 시드 매칭 → 카테고리 합산
- **시각화**: 채널 카드 "카테고리" 배지
- **활용**: 신규 채널 주제 영역 빠른 파악

#### 11. 👴 야담·시니어 탐사 (senior exploration)

- **정의**: 야담 시드 11개로 ytsearch → 시니어 관심층 폭발 영상 발굴
- **공식** (explore_senior.py:36~42): `CHANNEL_ACTIVE_DAYS = 60` · `VIDEO_RECENT_DAYS = 30` · `MIN_VIEWS = 5_000` (니치라 낮춤)
- **발견**: ① 야담 watch list 채널 → ② 최신 100편 → ③ 30일·5천뷰·롱폼 필터 → ④ velocity = views / age_hours
- **시각화**: `senior_{date}.html`
- **활용**: 야담 "조선야담처녀" 톤 학습 + 시니어 어휘 풀

#### 12. 🔁 재편집 재폭발 (reedit re-explosion)

- **정의**: 검증 키워드가 최근 7일 내 재업로드 → 다시 터지는 현상
- **공식** (detect_reedit_yt.py:25~29): `TOP_KEYWORDS = 120` · `PER_KW_SEARCH = 12` · `MIN_VIEWS = 50_000` · `RECENT_DAYS = 7` · `score = archive_score + (7-days) * 3 + views/100_000`
- **발견**: ① 아카이브 상위 120 키워드 → ② ytsearch × 12편 → ③ 5만뷰+ 필터 → ④ yt-dlp로 업로드일 풀추출 → ⑤ 7일 이내 = 점수 계산
- **시각화**: `daily_{date}.html` "🔥 지금 폭발 중"
- **활용**: "검증 주제 → 즉시 재업로드" 최강 ROI 전략

#### 13. 🏆 검증 주제 엔진 (proven topic engine)

- **정의**: 여러 채널·여러 영상이 같은 키워드로 반복 폭발 = "검증 금광"
- **공식** (detect_proven_topics.py:31~58): `RECENT_DAYS = 14` · `MIN_CHANNELS = 2` · `MIN_VIDEOS = 3` · `archive_score = sum(views) + channels_count * 50_000`
- **발견**: ① 14일 폭발 영상 + science + 후보 풀 + 시드 topics → ② 한글 명사 추출 + 별칭 정규화 → ③ 채널/영상/조회 집계 → ④ 채널 ≥2 & 영상 ≥3 필터 → ⑤ 아카이브 누적 병합
- **시각화**: `proven_{date}.html`
- **활용**: 4채널 IP 공통 발견 + 카테고리 교차 후보 발굴

#### 14. 🏷️ 채널 타입 분류 (channel type, 6종)

- **정의**: 채널명 키워드 + 구독자 기반 6가지 자동 분류
- **공식** (estimate_candidate_type.py:27~82):
  - `대형` (구독 1M+) / `일반,뉴스` (뉴스 키워드 + <1M) / `일반+AI` (AI 키워드 + 100K+) / `AI` (AI만) / `일반` (10K~1M) / `제외` (성인·키즈·도박)
- **발견**: NEWS_KW → AI_KW → 구독자 우선순위
- **시각화**: 후보·모니터링 리포트 "타입" 배지
- **활용**: 타입별 다른 폭발 임계 적용 (소형/대형 분리)

#### 15. 🔁 단조도 점수 (monotony score)

- **정의**: 채널 영상마다 반복되는 표현·Hook 중복도 (0~100, 낮을수록 다양)
- **공식** (channel_repetition.py): `jaccard(a,b) = |a∩b|/|a∪b|` · `monotony_score = 100 - vocab_renewal*50 - avg_jaccard_hook*50`
- **발견**: ① N편 자막 로드 → ② 영상 쌍별 3-gram Jaccard → ③ Hook 0:00~0:30 + 본문 텍스트 → ④ 어휘 갱신율
- **시각화**: `candidates.html` 채널 벤치마크
- **활용**: 같은 패턴 반복 = 거부감 → 다양화 체크리스트

#### 16. 📋 제목 공식 분석 (title formula)

- **정의**: 카테고리별 효율 TOP 제목의 구조·길이·클릭베이트 정량화
- **공식** (title_formula.py:30~76):
  - 구조: `has_question/exclaim/colon/dash/pipe/emoji/number/brackets/quote`
  - 클릭베이트 8종: 충격·비밀·반전·금기·VS·위협·신분역전·시간점프
  - n-gram: 2-gram, 3-gram 빈도 TOP 20
- **시각화**: `library.html` "📋 제목 공식"
- **활용**: 카테고리별 효율 제목 공통 구조 학습

#### 17. 🏆 패턴 라이브러리 (pattern library)

- **정의**: 모든 검증 데이터 통합 카탈로그 (autopsy + 시니어 + 모니터 + proven)
- **공식**: `hook_pool` + `outro_pool` + `title_formulas` + `thumbnail_index` + `vocab_signatures` + `first_event_norms` + `top_videos`
- **발견**: 모든 소스 JSON 로드 → 영상 ID 중복 제거 → 효율 정렬 → 항목별 추출
- **시각화**: `library.html` 전용 페이지
- **활용**: 신영상 제작 시 직접 참고 (Hook·제목·Outro 템플릿)

#### 18. 🖼️ 썸네일 LLM 시각 분석 (thumbnail visual)

- **정의**: Claude API로 썸네일 OCR·시각요소·클릭베이트 점수·제목 일치도 분석
- **공식** (analyze_thumbnails_llm.py): 클릭베이트 1~10점 + 제목 일치도 % + 카테고리 추정. Claude 3.5 Haiku 사용 (영상당 $0.005~0.01)
- **발견**: ① library.json 썸네일 URL → ② base64 인코딩 → ③ API vision 호출 → ④ JSON 응답 파싱
- **시각화**: `library.html` 썸네일 갤러리 + 시각 팝업
- **활용**: 효율 높은 썸네일 공통 시각 요소 학습 + 자체 디자인 참고

#### 19. 🔀 카테고리 교차 (cross-category transfer)

- **정의**: A 카테고리 폭발 주제를 B 채널 톤으로 재편집
- **발견**: proven_topics → 채널 category 매핑 → 다른 카테고리 폭발 추출 → 채널별 변환 제안
- **시각화**: `workboard.html` "🔀 카테고리 교차" (7카테고리 중 6번)
- **활용**: 한 주제 다채널 활용 → ROI 극대화

#### 20. 📚 메인 시리즈 IP + 💎 보유 대본 추적

- **정의**: 4채널의 메인 시리즈 EP.N 진행 + 미발행 대본 우선 추천
- **공식** (build_site.py:3090~3138): `series_ip` 필드(main·essence·ep_count) → `ep_next = ep_count + 1` · type "보유" = 강조색
- **시각화**: `workboard.html` 채널별 보라 박스 "📚 메인 시리즈 IP" + "💎 보유 대본 우선"
- **활용**: 다음 회차 자동 추천 + 시간 절감 (대본 있는 것부터 발행)

---

### 📊 메트릭 분류표 (한눈에)

| # | 메트릭 | 카테고리 | 핵심 임계값 | 시각화 |
|---|---|---|---|---|
| 1 | 🚨 알고리즘 시그널 | 등록채널 신호 | velocity ≥5,000/h | daily |
| 2 | 🔬 소형 폭발 | 등록채널 폭발 | eff ≥5x, vel ≥1,000 | daily |
| 3 | 🐳 대형 폭발 | 등록채널 폭발 | vel ≥5,000, views ≥200K | daily |
| 4 | 🆕 신영상 | 등록채널 이벤트 | upload ≤24h | daily |
| 5 | 🎯 오늘의 주제 | 추천 통합 | proven × 오늘 교차 | recommendations |
| 6 | 🔥 Hot 키워드 | 트렌딩 | substring 빈도 | recommendations |
| 7 | 🧪 과학 트렌드 | 전문 탐사 | views ≥100K | science |
| 8 | ⚠️ 발행 중단 | 채널 모니터 | recent/baseline ≤0.20 | daily |
| 9 | 📺 외부 폭발 | 뉴스 연계 | views ≥50K | news |
| 10 | 🏷️ 자동 카테고리 | 분류 엔진 | match ≥2 | candidates |
| 11 | 👴 야담·시니어 | 전문 탐사 | views ≥5K, ≤30일 | senior |
| 12 | 🔁 재편집 재폭발 | 검증 기반 | days ≤7 | daily |
| 13 | 🏆 검증 주제 | 크로스채널 | channels ≥2, videos ≥3 | proven |
| 14 | 🏷️ 채널 타입 | 후보 분석 | 6가지 타입 | candidates |
| 15 | 🔁 단조도 점수 | 채널 분석 | 0~100 (낮을수록 다양) | candidates |
| 16 | 📋 제목 공식 | 패턴 분석 | 구조 + 클릭베이트 8종 | library |
| 17 | 🏆 패턴 라이브러리 | 통합 카탈로그 | hook/outro/vocab | library |
| 18 | 🖼️ 썸네일 LLM | 시각 분석 | 클릭베이트 1~10점 | library |
| 19 | 🔀 카테고리 교차 | 전략 엔진 | 다카테 폭발 감지 | workboard |
| 20 | 📚 시리즈 IP + 💎 보유 | 채널 관리 | ep_count + type="보유" | workboard |

### 🌟 시스템 아키텍처 한 줄 요약

```
29개 채널 모니터링 → 시속·효율 계산 → 6가지 신호(폭발·시그널·신영상·중단·재편집·검증)
        ↓                                ↓
     뉴스 RSS 수집 → 외부 폭발 발굴    채널 분석(타입·단조도·제목공식)
        ↓                                ↓
     시드 ytsearch(과학·시니어) → 신규 채널 발견
        ↓                                ↓
     검증 주제 아카이브 누적 → 패턴 라이브러리 → 썸네일 LLM 분석
        ↓                                ↓
     Daily Workboard 7카테고리 통합 → 4채널 의사결정 → "오늘 만들 주제"
```

</details>

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
