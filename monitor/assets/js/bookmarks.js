/**
 * 튜브해커 영상 북마크 시스템 v2
 *
 * 저장 구조 (localStorage):
 * {
 *   "video_id_1": {
 *     "type": "interest",  // "interest" | "production"
 *     "production_channel": "247",  // "jisikrok" | "247" | "redman" (production일 때만)
 *     "video": { vid, title, views, comments, url, days_ago, date_str, channel_name },
 *     "added_at": "..."
 *   }
 * }
 *
 * v2 변경: 영상 메타를 HTML 속성으로 인코딩하지 않고
 * 전역 레지스트리에 vid 키로 등록 (따옴표 escape 문제 해결)
 */
(function() {
  const KEY = 'tubehacker_bookmarks';
  const CHANNELS = {
    'jisikrok': { name: '지식록', emoji: '📈', color: '#3b82f6' },
    '247': { name: '247경제', emoji: '💹', color: '#dc2626' },
    'redman': { name: '레드맨', emoji: '🇰🇷', color: '#e11d48' },
  };

  // 전역 영상 레지스트리 (렌더링 시 등록)
  const videoRegistry = {};

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '{}'); }
    catch { return {}; }
  }

  function save(data) {
    localStorage.setItem(KEY, JSON.stringify(data));
    window.dispatchEvent(new Event('bookmarks-changed'));
  }

  function get(vid) { return load()[vid]; }

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
      if (data[vid] && data[vid].type === 'production') delete data[vid];
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

  // 영상 메타 등록 (렌더링 시 호출)
  function register(video, channelName) {
    videoRegistry[video.vid] = {
      vid: video.vid,
      title: video.title || '',
      views: video.views || 0,
      comments: video.comments || 0,
      url: video.url || `https://youtu.be/${video.vid}`,
      days_ago: video.days_ago,
      date_str: video.date_str || '',
      channel_name: channelName || '',
    };
  }

  // 북마크 아이콘 렌더링 (video cell에 삽입)
  function renderIcons(video, channelName) {
    // 레지스트리 등록
    register(video, channelName);

    const bm = get(video.vid);
    const isInterest = bm && bm.type === 'interest';
    const isProduction = bm && bm.type === 'production';
    const prodChannel = isProduction ? bm.production_channel : null;

    const prodBadge = prodChannel && CHANNELS[prodChannel]
      ? `<span style="font-size: 9px; color: ${CHANNELS[prodChannel].color}; font-weight: 700;">${CHANNELS[prodChannel].emoji}${CHANNELS[prodChannel].name}</span>`
      : '';

    return `
      <div class="bookmark-icons" onclick="event.stopPropagation();" style="display: flex; gap: 4px; margin-top: 4px; align-items: center;">
        <button class="bm-btn ${isInterest ? 'active' : ''}"
                onclick="TubeHackerBookmarks.toggleInterestUI(this, '${video.vid}')"
                title="관심주제">
          ${isInterest ? '⭐' : '☆'}
        </button>
        <button class="bm-btn ${isProduction ? 'active' : ''}"
                onclick="TubeHackerBookmarks.openProductionMenu(event, '${video.vid}')"
                title="영상제작">
          ${isProduction ? '🎬' : '🎥'}
        </button>
        ${prodBadge}
      </div>
    `;
  }

  function toggleInterestUI(btn, vid) {
    const video = videoRegistry[vid];
    if (!video) {
      console.warn('Video not in registry:', vid);
      return;
    }
    toggleInterest(vid, video);
    const isNow = !!get(vid);
    btn.textContent = isNow ? '⭐' : '☆';
    btn.classList.toggle('active', isNow);
  }

  function openProductionMenu(event, vid) {
    event.stopPropagation();
    document.querySelectorAll('.production-menu').forEach(m => m.remove());

    const video = videoRegistry[vid];
    if (!video) {
      console.warn('Video not in registry:', vid);
      return;
    }
    const rect = event.target.getBoundingClientRect();
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
             data-vid="${vid}"
             style="padding: 6px 10px; cursor: pointer; border-radius: 4px; font-size: 12px; color: #e4e6eb; display: flex; align-items: center; gap: 6px; ${currentCh === key ? `background: ${ch.color}; color: white;` : ''}">
          ${ch.emoji} ${ch.name} ${currentCh === key ? '✓' : ''}
        </div>
      `).join('')}
      ${currentProd ? `
        <div class="prod-menu-item" data-channel="" data-vid="${vid}"
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
        const itemVid = item.dataset.vid;
        const itemVideo = videoRegistry[itemVid];
        setProduction(itemVid, itemVideo, ch);
        menu.remove();
        window.dispatchEvent(new Event('bookmarks-changed'));
        // 페이지 리로드 대신 소프트 리렌더 시도
        if (typeof render === 'function') render();
        else location.reload();
      };
      item.onmouseover = () => { if (!item.classList.contains('active')) item.style.background = '#2a2f3a'; };
      item.onmouseout = () => { if (!item.classList.contains('active')) item.style.background = ''; };
    });

    setTimeout(() => {
      document.addEventListener('click', function closeMenu() {
        menu.remove();
        document.removeEventListener('click', closeMenu);
      }, { once: true });
    }, 10);
  }

  window.TubeHackerBookmarks = {
    get, toggleInterest, setProduction, remove, getAll, load,
    register, renderIcons, toggleInterestUI, openProductionMenu,
    CHANNELS,
    _registry: videoRegistry,  // debug용
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
