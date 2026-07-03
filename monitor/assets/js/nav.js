/**
 * 튜브해커 공통 네비게이션
 * 각 페이지에서 <div id="nav"></div> 삽입 후 자동 렌더링
 *
 * arrange-yt-scanner.pages.dev/monitor/ 하위에 배포됨
 */
(function() {
  // 상대 경로 사용 (base 무관하게 동작)
  const NAV_ITEMS = [
    { path: 'index.html', name: '홈', emoji: '🏠' },
    { path: 'channels.html', name: '채널 감시', emoji: '📺' },
    { path: 'alerts.html', name: '폭발 알림', emoji: '🔥' },
    { path: 'topics.html', name: '주제 파이', emoji: '📊' },
    { path: 'reports.html', name: '리포트', emoji: '📋' },
  ];

  function renderNav() {
    const container = document.getElementById('nav');
    if (!container) return;

    // 현재 파일명만 추출
    const parts = location.pathname.split('/').filter(Boolean);
    const currentFile = parts[parts.length - 1] || 'index.html';

    container.innerHTML = `
      <nav class="nav-bar">
        <a href="index.html" class="nav-logo">
          <span class="logo-emoji">🎬</span>
          <span>튜브해커</span>
        </a>
        <div class="nav-links">
          ${NAV_ITEMS.map(item => {
            const isActive = currentFile === item.path ||
                             (currentFile === '' && item.path === 'index.html') ||
                             (currentFile === 'monitor' && item.path === 'index.html');
            return `<a href="${item.path}" class="nav-link ${isActive ? 'active' : ''}">
              <span>${item.emoji}</span> ${item.name}
            </a>`;
          }).join('')}
          <a href="../index.html" class="nav-link" style="margin-left: 12px; opacity: 0.6;" title="arrange-yt-scanner 메인">
            <span>↩</span> 메인 대시보드
          </a>
        </div>
        <div class="nav-meta" id="nav-meta"></div>
      </nav>
    `;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderNav);
  } else {
    renderNav();
  }
})();
