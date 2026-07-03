/**
 * 튜브해커 영상 북마크 시스템
 *
 * 저장 구조 (localStorage):
 * {
 *   "video_id_1": {
 *     "type": "interest",  // "interest" | "production"
 *     "production_channel": "247",  // "jisikrok" | "247" | "redman" (production일 때만)
 *     "video": { vid, title, views, comments, url, days_ago, date_str, channel_name },
 *     "added_at": "2026-07-03T..."
 *   }
 * }
 */
(function() {
  const KEY = 'tubehacker_bookmarks';
  const CHANNELS = {
    'jisikrok': { name: '지식록', emoji: '📈', color: '#3b82f6' },
    '247': { name: '247경제', emoji: '💹', color: '#dc2626' },
    'redman': { name: '레드맨', emoji: '🇰🇷', color: '#e11d48' },
  };

  function load() {
    try {
      return JSON.parse(localStorage.getItem(KEY) || '{}');
    } catch {
      return {};
    }
  }

  function save(data) {
    localStorage.setItem(KEY, JSON.stringify(data));
    // 커스텀 이벤트 (여러 페이지 동기화용)
    window.dispatchEvent(new Event('bookmarks-changed'));
  }

  function get(vid) {
    return load()[vid];
  }

  function toggleInterest(vid, videoMeta) {
    const data = load();
    const existing = data[vid];
    if (existing && existing.type === 'interest') {
      delete data[vid];
    } else {
      data[vid] = {
        type: 'interest',
        video: videoMeta,
        added_at: new Date().toISOString(),
      };
    }
    save(data);
    return data[vid];
  }

  function setProduction(vid, videoMeta, channel) {
    const data = load();
    if (channel === null || channel === undefined) {
      // 제거
      if (data[vid] && data[vid].type === 'production') {
        delete data[vid];
      }
    } else {
      data[vid] = {
        type: 'production',
        production_channel: channel,
        video: videoMeta,
        added_at: new Date().toISOString(),
      };
    }
    save(data);
    return data[vid];
  }

  function remove(vid) {
    const data = load();
    delete data[vid];
    save(data);
  }

  function getAll(type) {
    const data = load();
    let items = Object.entries(data).map(([vid, val]) => ({ vid, ...val }));
    if (type) items = items.filter(i => i.type === type);
    items.sort((a, b) => (b.added_at || '').localeCompare(a.added_at || ''));
    return items;
  }

  // 북마크 아이콘 렌더링 (video cell에 삽입)
  function renderIcons(video, channelName) {
    const bm = get(video.vid);
    const isInterest = bm && bm.type === 'interest';
    const isProduction = bm && bm.type === 'production';
    const prodChannel = isProduction ? bm.production_channel : null;

    const videoMetaJson = JSON.stringify({
      vid: video.vid,
      title: video.title,
      views: video.views || 0,
      comments: video.comments || 0,
      url: video.url,
      days_ago: video.days_ago,
      date_str: video.date_str,
      channel_name: channelName || '',
    }).replace(/"/g, '&quot;');

    const prodBadge = prodChannel && CHANNELS[prodChannel]
      ? `<span style="font-size: 9px; color: ${CHANNELS[prodChannel].color}; font-weight: 700;">${CHANNELS[prodChannel].emoji}${CHANNELS[prodChannel].name}</span>`
      : '';

    return `
      <div class="bookmark-icons" onclick="event.stopPropagation();" style="display: flex; gap: 4px; margin-top: 4px; align-items: center;">
        <button class="bm-btn ${isInterest ? 'active' : ''}"
                onclick="TubeHackerBookmarks.toggleInterestUI(this, '${video.vid}', '${videoMetaJson}')"
                title="관심주제">
          ${isInterest ? '⭐' : '☆'}
        </button>
        <div style="position: relative; display: inline-block;">
          <button class="bm-btn ${isProduction ? 'active' : ''}"
                  onclick="TubeHackerBookmarks.openProductionMenu(event, '${video.vid}', '${videoMetaJson}')"
                  title="영상제작">
            ${isProduction ? '🎬' : '🎥'}
          </button>
        </div>
        ${prodBadge}
      </div>
    `;
  }

  function toggleInterestUI(btn, vid, videoMetaEncoded) {
    const video = JSON.parse(videoMetaEncoded.replace(/&quot;/g, '"'));
    toggleInterest(vid, video);
    const isNow = !!get(vid);
    btn.textContent = isNow ? '⭐' : '☆';
    btn.classList.toggle('active', isNow);
  }

  function openProductionMenu(event, vid, videoMetaEncoded) {
    event.stopPropagation();
    // 기존 메뉴 닫기
    document.querySelectorAll('.production-menu').forEach(m => m.remove());

    const rect = event.target.getBoundingClientRect();
    const video = JSON.parse(videoMetaEncoded.replace(/&quot;/g, '"'));
    const currentProd = get(vid);
    const currentCh = currentProd?.production_channel;

    const menu = document.createElement('div');
    menu.className = 'production-menu';
    menu.style.cssText = `
      position: fixed;
      top: ${rect.bottom + 4}px;
      left: ${rect.left}px;
      background: #232732;
      border: 1px solid #2c3140;
      border-radius: 6px;
      padding: 6px;
      z-index: 1000;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
      min-width: 140px;
    `;
    menu.innerHTML = `
      <div style="font-size: 10px; color: #8a92a3; padding: 4px 8px; text-transform: uppercase;">영상제작 채널</div>
      ${Object.entries(CHANNELS).map(([key, ch]) => `
        <div class="prod-menu-item ${currentCh === key ? 'active' : ''}"
             data-channel="${key}"
             style="padding: 6px 10px; cursor: pointer; border-radius: 4px; font-size: 12px; color: #e4e6eb; display: flex; align-items: center; gap: 6px; ${currentCh === key ? `background: ${ch.color}; color: white;` : ''}">
          ${ch.emoji} ${ch.name} ${currentCh === key ? '✓' : ''}
        </div>
      `).join('')}
      ${currentProd ? `
        <div class="prod-menu-item" data-channel=""
             style="padding: 6px 10px; cursor: pointer; border-radius: 4px; font-size: 12px; color: #f87171; margin-top: 4px; border-top: 1px solid #2c3140; padding-top: 8px;">
          🗑 제거
        </div>
      ` : ''}
    `;
    document.body.appendChild(menu);

    menu.querySelectorAll('.prod-menu-item').forEach(item => {
      item.onclick = (e) => {
        e.stopPropagation();
        const ch = item.dataset.channel || null;
        setProduction(vid, video, ch);
        menu.remove();
        // 재렌더 트리거
        window.dispatchEvent(new Event('bookmarks-changed'));
        location.reload();
      };
      item.onmouseover = () => { if (!item.classList.contains('active')) item.style.background = '#2a2f3a'; };
      item.onmouseout = () => { if (!item.classList.contains('active')) item.style.background = ''; };
    });

    // 외부 클릭 시 닫기
    setTimeout(() => {
      document.addEventListener('click', function closeMenu() {
        menu.remove();
        document.removeEventListener('click', closeMenu);
      }, { once: true });
    }, 10);
  }

  window.TubeHackerBookmarks = {
    get, toggleInterest, setProduction, remove, getAll, load,
    renderIcons, toggleInterestUI, openProductionMenu,
    CHANNELS,
  };

  // 공용 CSS 주입
  const style = document.createElement('style');
  style.textContent = `
    .bm-btn {
      background: transparent;
      border: 1px solid #2c3140;
      color: #8a92a3;
      padding: 3px 6px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 12px;
      transition: all 0.1s;
    }
    .bm-btn:hover { background: #2a2f3a; border-color: #fbbf24; color: #fbbf24; }
    .bm-btn.active { background: #fbbf24; color: #78350f; border-color: #fbbf24; font-weight: 700; }
  `;
  document.head.appendChild(style);
})();
