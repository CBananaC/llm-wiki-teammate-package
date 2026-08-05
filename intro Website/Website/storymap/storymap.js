
const settingsButton = document.getElementById('settings-button');

document.querySelectorAll('.sample-doc-panel, .source-flow-document').forEach((panel) => {
  const minButton = panel.querySelector('.ip-min');
  const closeButton = panel.querySelector('.ip-close');
  const filterButton = panel.querySelector('.ip-filterbtn');
  const settingsButton = panel.querySelector('.ip-settingsbtn');
  minButton?.addEventListener('click', () => {
    panel.classList.toggle('is-folded');
    minButton.setAttribute('aria-expanded', String(!panel.classList.contains('is-folded')));
  });
  closeButton?.addEventListener('click', () => {
    const wrapper = panel.closest('.comparison-review-panel, .acc-panel');
    wrapper?.setAttribute('hidden', '');
  });
  [filterButton, settingsButton].forEach((button) => {
    button?.addEventListener('click', () => {
      button.classList.toggle('is-active');
      button.setAttribute('aria-pressed', String(button.classList.contains('is-active')));
    });
  });
});
const settingsPanel = document.getElementById('site-settings-panel');
const settingsWrap = document.querySelector('.settings-wrap');
const fontSizeDecrease = document.getElementById('font-size-decrease');
const fontSizeIncrease = document.getElementById('font-size-increase');
const fontSizeValue = document.getElementById('font-size-value');
const FONT_SCALE_KEY = 'intro-website-font-scale';
const FONT_SCALE_MIN = 0.55;
const FONT_SCALE_MAX = 2.2;
const FONT_SCALE_STEP = 0.05;
const clampFontScale = (value) => Math.min(FONT_SCALE_MAX, Math.max(FONT_SCALE_MIN, value));
const readFontScale = () => {
  try {
    const saved = Number.parseFloat(localStorage.getItem(FONT_SCALE_KEY));
    return Number.isFinite(saved) ? clampFontScale(saved) : 1;
  } catch (error) {
    return 1;
  }
};
const applyFontScale = (value) => {
  const scale = clampFontScale(value);
  document.documentElement.style.setProperty('--font-scale', String(scale));
  fontSizeValue.value = `${Math.round(scale * 100)}%`;
  fontSizeValue.textContent = fontSizeValue.value;
  fontSizeDecrease.disabled = scale <= FONT_SCALE_MIN;
  fontSizeIncrease.disabled = scale >= FONT_SCALE_MAX;
  try {
    localStorage.setItem(FONT_SCALE_KEY, String(scale));
  } catch (error) {
    // Continue without persistence when storage is unavailable.
  }
};
const setSettingsOpen = (open) => {
  settingsPanel.hidden = !open;
  settingsButton.setAttribute('aria-expanded', String(open));
  settingsButton.setAttribute('aria-label', open ? '關閉網站設定' : '開啟網站設定');
};
let settingsCloseTimer;
const scheduleSettingsClose = () => {
  window.clearTimeout(settingsCloseTimer);
  settingsCloseTimer = window.setTimeout(() => {
    if (!settingsWrap.matches(':hover') && !settingsWrap.contains(document.activeElement)) setSettingsOpen(false);
  }, 100);
};
applyFontScale(readFontScale());
settingsWrap.addEventListener('mouseenter', () => setSettingsOpen(true));
settingsWrap.addEventListener('mouseleave', scheduleSettingsClose);
settingsWrap.addEventListener('focusin', () => setSettingsOpen(true));
settingsWrap.addEventListener('focusout', scheduleSettingsClose);
settingsButton.addEventListener('click', () => setSettingsOpen(settingsPanel.hidden || settingsWrap.matches(':hover')));
fontSizeDecrease.addEventListener('click', () => applyFontScale(readFontScale() - FONT_SCALE_STEP));
fontSizeIncrease.addEventListener('click', () => applyFontScale(readFontScale() + FONT_SCALE_STEP));
document.addEventListener('click', (event) => {
  if (!settingsPanel.hidden && !event.target.closest('.settings-wrap')) setSettingsOpen(false);
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !settingsPanel.hidden) {
    setSettingsOpen(false);
    settingsButton.focus();
  }
});

const tabs = [...document.querySelectorAll('.main-nav-link')];
const tabPanels = [...document.querySelectorAll('[data-tab-panel]')];
const introDropdown = document.querySelector('.nav-dropdown');
const introDropdownTrigger = introDropdown.querySelector('.nav-dropdown-trigger');
const introDropdownMenu = introDropdown.querySelector('.nav-dropdown-menu');
const workflowNodes = [...document.querySelectorAll('.workflow-node')];
let introDropdownCloseTimer;
const setIntroDropdownOpen = (open) => {
  window.clearTimeout(introDropdownCloseTimer);
  introDropdown.classList.toggle('open', open);
  introDropdownTrigger.setAttribute('aria-expanded', String(open));
};
introDropdown.addEventListener('mouseenter', () => setIntroDropdownOpen(true));
const scheduleIntroDropdownClose = () => {
  window.clearTimeout(introDropdownCloseTimer);
  introDropdownCloseTimer = window.setTimeout(() => {
    const pointerInside = introDropdown.matches(':hover') || introDropdownMenu.matches(':hover');
    const focusInside = introDropdown.contains(document.activeElement);
    if (!pointerInside && !focusInside) setIntroDropdownOpen(false);
  }, 80);
};
introDropdown.addEventListener('mouseleave', scheduleIntroDropdownClose);
introDropdownMenu.addEventListener('mouseenter', () => setIntroDropdownOpen(true));
introDropdownMenu.addEventListener('mouseleave', scheduleIntroDropdownClose);
introDropdown.addEventListener('focusin', () => setIntroDropdownOpen(true));
introDropdown.addEventListener('focusout', scheduleIntroDropdownClose);
const panelForHash = (hash) => {
  if (hash === '#intro' || hash.startsWith('#intro-')) return 'intro';
  if (hash === '#part-1') return 'part-1';
  if (hash === '#part-2') return 'part-2';
  if (hash === '#part-3' || hash.startsWith('#part-3-')) return 'part-3';
  return 'cover';
};
const setActiveTab = (tabName, { updateHash = true, scrollTarget = null } = {}) => {
  const panel = tabPanels.find((item) => item.dataset.tabPanel === tabName);
  if (!panel) return;
  tabPanels.forEach((item) => { item.hidden = item !== panel; });
  tabs.forEach((tab) => tab.classList.toggle('active', tab.dataset.navTarget === tabName));
  introDropdown.classList.toggle('active', tabName === 'intro');
  setIntroDropdownOpen(false);
  if (updateHash) history.pushState(null, '', scrollTarget || `#${tabName}`);
  if (scrollTarget) {
    window.requestAnimationFrame(() => document.querySelector(scrollTarget)?.scrollIntoView({ block: 'start' }));
  } else {
    window.scrollTo(0, 0);
  }
};
tabs.forEach((tab) => {
  tab.addEventListener('click', (event) => {
    event.preventDefault();
    setActiveTab(tab.dataset.navTarget);
  });
});
document.querySelector('[data-cover-target="intro"]')?.addEventListener('click', (event) => {
  event.preventDefault();
  setActiveTab('intro');
});
introDropdown.querySelectorAll('.nav-dropdown-menu a').forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const target = link.dataset.workflowTarget || link.getAttribute('href');
    const tabName = panelForHash(target);
    const scrollTarget = tabName === 'intro' && target.startsWith('#intro-') ? target : null;
    setActiveTab(tabName, { scrollTarget });
  });
});
workflowNodes.forEach((node) => {
  node.addEventListener('click', () => {
    workflowNodes.forEach((item) => item.classList.toggle('is-selected', item === node));
  });
});

/* 量測每一節文字欄的高度，寫入該節的 --text-h。
   storymap-cards.css 的 --visual-x（倍數）便以此為基準計算視覺元素高度。
   文字欄高度會隨字級設定、視窗寬度、小卡展開而改變，因此持續觀察。 */
const measureTextColumns = () => {
  const groups = [...document.querySelectorAll('.lay-split, .lay-acc')];
  if (!groups.length) return;
  const apply = () => {
    groups.forEach((group) => {
      const textColumn = group.querySelector('.lay-copy, .acc-track');
      if (!textColumn) return;
      const height = Math.round(textColumn.getBoundingClientRect().height);
      if (height > 0) group.style.setProperty('--text-h', `${height}px`);
    });
  };
  apply();
  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(apply);
    groups.forEach((group) => {
      const textColumn = group.querySelector('.lay-copy, .acc-track');
      if (textColumn) observer.observe(textColumn);
    });
  }
  window.addEventListener('resize', apply);
};
measureTextColumns();

/* 硃119消息來源標註：外置來源框跟隨原文引文位置，並在文件內捲動或
   視窗尺寸改變時重畫連線。這組標註是教學網站新增的視覺層，不修改審閱工具。 */
let sourceFlowRefreshFrame = 0;
const refreshSourceFlowConnectors = () => {
  sourceFlowRefreshFrame = 0;
  document.querySelectorAll('[data-source-flow]').forEach((visual) => {
    const svg = visual.querySelector('.source-connector-layer');
    if (!svg) return;
    const rootRect = visual.getBoundingClientRect();
    const width = Math.round(visual.clientWidth);
    const height = Math.round(visual.clientHeight);
    if (!width || !height) return;

    svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
    svg.innerHTML = '';
    const marks = new Map();
    visual.querySelectorAll('[data-source-highlight]').forEach((mark) => {
      const key = mark.dataset.sourceHighlight;
      if (key) marks.set(key, [...(marks.get(key) || []), mark]);
    });

    const scrollViewport = visual.querySelector('.ip-scroll')?.getBoundingClientRect();
    const pageViewport = { top: 0, bottom: window.innerHeight };
    const panelHeaderBottom = [
      visual.querySelector('.ip-head')?.getBoundingClientRect(),
      visual.querySelector('.ip-filterdock')?.getBoundingClientRect()
    ].filter(Boolean).reduce(
      (bottom, rect) => Math.max(bottom, rect.bottom),
      scrollViewport?.top ?? pageViewport.top
    );
    visual.querySelectorAll('.source-callouts').forEach((callouts) => {
      let previousBottom = 8;
      const isRight = callouts.classList.contains('source-callouts-right');
      callouts.querySelectorAll('[data-source-bubble]').forEach((bubble) => {
        const key = bubble.dataset.sourceBubble;
        const markList = marks.get(key) || [];
        if (!markList.length) return;
        const contentTop = Math.max(panelHeaderBottom, scrollViewport?.top ?? pageViewport.top);
        const contentBottom = Math.min(scrollViewport?.bottom ?? pageViewport.bottom, pageViewport.bottom);
        const visibleMarks = markList
          .map((mark) => ({ mark, rect: mark.getBoundingClientRect() }))
          .filter(({ rect }) => !scrollViewport
            || (rect.top >= contentTop
              && rect.bottom > contentTop
              && rect.top < contentBottom));
        const markIsVisible = visibleMarks.length > 0;
        bubble.hidden = !markIsVisible;
        bubble.setAttribute('aria-hidden', String(!markIsVisible));
        if (!markIsVisible) {
          bubble.style.removeProperty('top');
          return;
        }
        const markRect = visibleMarks[0].rect;
        const bubbleHeight = bubble.getBoundingClientRect().height;
        const targetY = markRect.top + markRect.height / 2 - rootRect.top;
        const maxBubbleTop = Math.max(8, height - bubbleHeight - 8);
        let bubbleTop = Math.max(8, Math.min(maxBubbleTop, targetY - bubbleHeight / 2));
        if (bubbleTop < previousBottom + 10) bubbleTop = Math.min(maxBubbleTop, previousBottom + 10);
        bubble.style.top = `${Math.round(bubbleTop)}px`;
        previousBottom = bubbleTop + bubbleHeight;

        const bubbleRect = bubble.getBoundingClientRect();
        const x1 = (isRight ? bubbleRect.left : bubbleRect.right) - rootRect.left;
        const y1 = bubbleRect.top + bubbleRect.height / 2 - rootRect.top;
        const x2 = Math.max(0, Math.min(width, (isRight ? markRect.right : markRect.left) - rootRect.left));
        const y2 = Math.max(8, Math.min(height - 8, targetY));
        const color = getComputedStyle(bubble).getPropertyValue('--source-color').trim();

        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.classList.add('source-connector-line');
        line.style.stroke = color;
        line.setAttribute('x1', String(Math.round(x1)));
        line.setAttribute('y1', String(Math.round(y1)));
        line.setAttribute('x2', String(Math.round(x2)));
        line.setAttribute('y2', String(Math.round(y2)));
        svg.appendChild(line);

        const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        dot.classList.add('source-connector-dot');
        dot.style.fill = color;
        dot.setAttribute('cx', String(Math.round(x2)));
        dot.setAttribute('cy', String(Math.round(y2)));
        dot.setAttribute('r', '3.5');
        svg.appendChild(dot);
      });
    });
  });
};
const scheduleSourceFlowConnectorRefresh = () => {
  if (sourceFlowRefreshFrame) return;
  sourceFlowRefreshFrame = window.requestAnimationFrame(refreshSourceFlowConnectors);
};
window.addEventListener('resize', scheduleSourceFlowConnectorRefresh);
window.addEventListener('scroll', scheduleSourceFlowConnectorRefresh, { passive: true });
document.querySelectorAll('[data-source-flow]').forEach((visual) => {
  visual.querySelector('.ip-scroll')?.addEventListener('scroll', scheduleSourceFlowConnectorRefresh, { passive: true });
  visual.querySelectorAll('.source-callout').forEach((callout) => {
    callout.addEventListener('pointerenter', scheduleSourceFlowConnectorRefresh);
    callout.addEventListener('pointerleave', scheduleSourceFlowConnectorRefresh);
    callout.addEventListener('focusin', scheduleSourceFlowConnectorRefresh);
    callout.addEventListener('focusout', scheduleSourceFlowConnectorRefresh);
  });
  if ('ResizeObserver' in window) new ResizeObserver(scheduleSourceFlowConnectorRefresh).observe(visual);
});
scheduleSourceFlowConnectorRefresh();

/* 小卡（點擊展開）＋對應視覺元素。
   行為：初始全部收合；點標題展開／收合，不影響其他已展開的卡；
   點已展開卡片的內文，只把右側畫面切換到該卡，不收合。 */
document.querySelectorAll('[data-acc]').forEach((group) => {
  const cards = [...group.querySelectorAll('[data-acc-card]')];
  const panels = [...group.querySelectorAll('[data-acc-panel]')];
  if (!cards.length) return;

  const showPanel = (id) => {
    panels.forEach((panel) => {
      const active = panel.dataset.accPanel === id;
      panel.classList.toggle('is-active', active);
      panel.hidden = !active;
    });
    cards.forEach((card) => card.classList.toggle('is-showing', card.dataset.accCard === id));
    scheduleSourceFlowConnectorRefresh();
  };

  cards.forEach((card) => {
    const heading = card.querySelector('[data-acc-target]');
    const body = card.querySelector('.acc-body');
    card.classList.remove('is-open');
    if (heading) heading.setAttribute('aria-expanded', 'false');

    /* 上半（標題）：展開／收合 */
    heading?.addEventListener('click', () => {
      const willOpen = !card.classList.contains('is-open');
      card.classList.toggle('is-open', willOpen);
      heading.setAttribute('aria-expanded', String(willOpen));
      if (willOpen) {
        showPanel(card.dataset.accCard);
      } else {
        const stillOpen = cards.filter((item) => item.classList.contains('is-open'));
        showPanel(stillOpen.length ? stillOpen[stillOpen.length - 1].dataset.accCard : cards[0].dataset.accCard);
      }
    });

    heading?.addEventListener('keydown', (event) => {
      if (!['ArrowDown', 'ArrowRight', 'ArrowUp', 'ArrowLeft'].includes(event.key)) return;
      event.preventDefault();
      const headings = cards.map((item) => item.querySelector('[data-acc-target]')).filter(Boolean);
      const index = headings.indexOf(heading);
      const step = event.key === 'ArrowDown' || event.key === 'ArrowRight' ? 1 : -1;
      headings[(index + step + headings.length) % headings.length].focus();
    });

    /* 下半（內文）：只切換右側畫面 */
    if (body) {
      body.setAttribute('role', 'button');
      body.setAttribute('tabindex', '0');
      body.setAttribute('aria-label', '顯示此項目的視覺元素');
      body.addEventListener('click', () => showPanel(card.dataset.accCard));
      body.addEventListener('keydown', (event) => {
        if (event.key !== 'Enter' && event.key !== ' ') return;
        event.preventDefault();
        showPanel(card.dataset.accCard);
      });
    }
  });

  showPanel(cards[0].dataset.accCard);
});
document.addEventListener('click', (event) => {
  if (!introDropdown.contains(event.target)) setIntroDropdownOpen(false);
});
const sections = [...document.querySelectorAll('.story[data-tab], [data-intro-card][data-tab]')];
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    const target = entry.target.dataset.nav || '#' + entry.target.id;
    const workflowTarget = entry.target.id ? '#' + entry.target.id : target;
    workflowNodes.forEach((node) => node.classList.toggle(
      'is-selected',
      node.dataset.workflowTarget === workflowTarget || node.dataset.workflowTarget === target
    ));
  });
}, { threshold: 0.35 });
sections.forEach((section) => observer.observe(section));

/* 圖片放大檢視：全站共用一個浮層。點圖片開啟，點 X 或點外部深色區域關閉，
   也支援 Esc 鍵關閉。 */
const photoLightbox = (() => {
  const overlay = document.createElement('div');
  overlay.className = 'photo-lightbox';
  overlay.innerHTML = `
    <figure class="photo-lightbox-figure">
      <button type="button" class="photo-lightbox-close" aria-label="關閉放大檢視">×</button>
      <img alt="">
      <figcaption class="photo-lightbox-caption" hidden></figcaption>
    </figure>
    <button type="button" class="photo-lightbox-nav prev" aria-label="上一頁">‹</button>
    <button type="button" class="photo-lightbox-nav next" aria-label="下一頁">›</button>
    <div class="photo-lightbox-counter" aria-live="polite" hidden></div>
  `;
  document.body.appendChild(overlay);
  const img = overlay.querySelector('img');
  const caption = overlay.querySelector('.photo-lightbox-caption');
  const closeBtn = overlay.querySelector('.photo-lightbox-close');
  const prevBtn = overlay.querySelector('.photo-lightbox-nav.prev');
  const nextBtn = overlay.querySelector('.photo-lightbox-nav.next');
  const counter = overlay.querySelector('.photo-lightbox-counter');
  let lastFocused = null;
  let pages = [];
  let pageIndex = 0;

  const close = () => {
    overlay.classList.remove('is-open');
    img.src = '';
    pages = [];
    pageIndex = 0;
    prevBtn.hidden = true;
    nextBtn.hidden = true;
    counter.hidden = true;
    if (lastFocused) lastFocused.focus();
  };
  const renderPage = () => {
    const page = pages[pageIndex];
    if (!page) return;
    img.src = page.src;
    img.alt = page.alt || '';
    if (page.captionHtml) { caption.innerHTML = page.captionHtml; caption.hidden = false; }
    else if (page.caption) { caption.textContent = page.caption; caption.hidden = false; }
    else { caption.textContent = ''; caption.hidden = true; }
    const hasNavigation = pages.length > 1;
    prevBtn.hidden = !hasNavigation;
    nextBtn.hidden = !hasNavigation;
    counter.hidden = !hasNavigation;
    counter.textContent = hasNavigation ? `頁 ${pageIndex + 1} / ${pages.length}` : '';
  };
  const open = (src, alt, captionText, triggerEl) => {
    lastFocused = triggerEl || null;
    pages = [{ src, alt, caption: captionText }];
    pageIndex = 0;
    renderPage();
    overlay.classList.add('is-open');
    closeBtn.focus();
  };
  const escapeCaptionHtml = (value) => String(value).replace(/[&<>"']/g, (char) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[char]));
  const openGallery = (galleryPages, startIndex, {
    title = '', captionTitle = title, showPageNumber = true, description = '', descriptionHtml = ''
  } = {}, triggerEl) => {
    const validPages = galleryPages.filter(Boolean);
    if (!validPages.length) return;
    lastFocused = triggerEl || null;
    pages = validPages.map((src, i) => {
      const pageLabel = showPageNumber ? `第 ${i + 1} 頁` : '';
      return {
        src,
        alt: `${title} ${pageLabel}`.trim(),
        caption: [captionTitle, pageLabel, description].filter(Boolean).join('｜'),
        captionHtml: descriptionHtml
          ? [captionTitle && escapeCaptionHtml(captionTitle), pageLabel, descriptionHtml].filter(Boolean).join('｜')
          : ''
      };
    });
    pageIndex = Math.max(0, Math.min(pages.length - 1, startIndex || 0));
    renderPage();
    overlay.classList.add('is-open');
    closeBtn.focus();
  };

  const showPage = (nextIndex) => {
    if (pages.length < 2) return;
    pageIndex = (nextIndex + pages.length) % pages.length;
    renderPage();
  };

  /* 點外部深色區域（不是圖片本身）即關閉 */
  overlay.addEventListener('click', (event) => {
    if (event.target === overlay || event.target === overlay.firstElementChild) close();
  });
  closeBtn.addEventListener('click', close);
  prevBtn.addEventListener('click', () => showPage(pageIndex - 1));
  nextBtn.addEventListener('click', () => showPage(pageIndex + 1));
  document.addEventListener('keydown', (event) => {
    if (!overlay.classList.contains('is-open')) return;
    if (event.key === 'Escape') close();
    if (event.key === 'ArrowLeft') showPage(pageIndex - 1);
    if (event.key === 'ArrowRight') showPage(pageIndex + 1);
  });

  prevBtn.hidden = true;
  nextBtn.hidden = true;
  counter.hidden = true;
  return { open, openGallery, close };
})();

/* 圖片畫廊：左右翻頁、乾淨圖片、下方說明（預設只顯示標題，滑鼠移入展開）。
   每個 [data-photo-gallery] 讀取自己的 <script type="application/json"
   data-photo-gallery-data> 作為圖片與說明來源。若只有來源而沒有段落，直接顯示完整引註；
   點擊圖片本身可開啟放大檢視。 */
document.querySelectorAll('[data-photo-gallery]').forEach((gallery) => {
  const dataScript = gallery.querySelector('[data-photo-gallery-data]');
  if (!dataScript) return;
  let pages = [];
  try {
    pages = JSON.parse(dataScript.textContent);
  } catch (error) {
    return;
  }
  if (!Array.isArray(pages) || !pages.length) return;

  const stage = gallery.querySelector('.photo-gallery-stage');
  const body = gallery.querySelector('.photo-gallery-body');
  if (!stage || !body) return;

  stage.innerHTML = '';
  pages.forEach((page, i) => {
    const frame = document.createElement('div');
    frame.className = 'photo-gallery-frame' + (i === 0 ? ' is-active' : '');
    frame.dataset.frame = String(i);
    const img = document.createElement('img');
    img.src = page.image;
    img.alt = page.alt || '';
    /* 每張圖片保留自己的顯示設定；切換圖片時不會沿用上一張的尺寸或裁切方式。 */
    if (page.fit) img.style.setProperty('--photo-fit', page.fit);
    if (page.position) img.style.setProperty('--photo-position', page.position);
    if (page.zoom) img.style.setProperty('--photo-zoom', String(page.zoom));
    /* 每張圖片的裁切／對齊／縮放一律在 storymap-cards.css 用
       :nth-of-type(N) 設定（N = 第幾張，從 1 開始），不在這裡處理，
       避免行內樣式蓋過 CSS 設定而難以調整。 */
    /* 點圖片本身開啟放大檢視：一律顯示完整原圖（不套用上面的裁切／縮放），
       說明文字帶標題與來源，方便在放大狀態下核對。 */
    img.addEventListener('click', () => {
      const captionParts = [page.title, page.source?.text].filter(Boolean);
      photoLightbox.open(page.image, page.alt || page.title, captionParts.join('｜'), img);
    });
    frame.appendChild(img);
    stage.appendChild(frame);
  });
  const frames = [...stage.querySelectorAll('.photo-gallery-frame')];

  if (pages.length > 1) {
    const prevBtn = document.createElement('button');
    prevBtn.type = 'button'; prevBtn.className = 'photo-gallery-nav prev'; prevBtn.setAttribute('aria-label', '上一張');
    prevBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>';
    const nextBtn = document.createElement('button');
    nextBtn.type = 'button'; nextBtn.className = 'photo-gallery-nav next'; nextBtn.setAttribute('aria-label', '下一張');
    nextBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>';
    const counter = document.createElement('div');
    counter.className = 'photo-gallery-counter';
    stage.append(prevBtn, nextBtn, counter);

    let index = 0;
    const show = (next) => {
      index = (next + frames.length) % frames.length;
      frames.forEach((frame, i) => {
        frame.classList.toggle('is-active', i === index);
        frame.hidden = i !== index;
      });
      counter.textContent = `圖 ${index + 1} / ${frames.length}`;
      /* A touch-expanded page must not leave its larger information area on
         the next page.  Reset the transient state before rendering the new
         page; a desktop hover can still expand it again naturally. */
      body.classList.remove('is-expanded');
      body.scrollTop = 0;
      if (pages[index].bodyMaxHeight) body.style.setProperty('--gallery-body-max-h', pages[index].bodyMaxHeight);
      else body.style.removeProperty('--gallery-body-max-h');
      renderBody(pages[index]);
    };
    prevBtn.addEventListener('click', () => show(index - 1));
    nextBtn.addEventListener('click', () => show(index + 1));
    gallery.setAttribute('tabindex', '0');
    gallery.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowLeft') show(index - 1);
      if (event.key === 'ArrowRight') show(index + 1);
    });
    show(0);
  } else {
    renderBody(pages[0]);
  }

  function renderBody(page) {
    /* Keep each page's optional layout override independent.  This also
       makes a page with a short description return to its own area after a
       previous page with a longer description was expanded. */
    body.classList.remove('is-expanded');
    body.scrollTop = 0;
    const paragraphs = (page.paragraphs || []).filter(Boolean);
    const hasDescription = paragraphs.length > 0;
    const hasSource = Boolean(page.source?.text);
    const paras = paragraphs.map((p) => `<p class="photo-gallery-desc">${p}</p>`).join('');
    const source = page.source
      ? `<p class="photo-gallery-source"><a href="${page.source.href}" target="_blank" rel="noopener noreferrer">${page.source.text} ↗</a></p>`
      : '';
    const title = page.titleHref
      ? `<a class="photo-gallery-title-link" href="${page.titleHref}" target="_blank" rel="noopener noreferrer">${page.title}</a>`
      : page.title;
    body.classList.toggle('is-source-only', !hasDescription && hasSource);
    body.innerHTML = `
      <h3 class="photo-gallery-title">${title}</h3>
      ${hasDescription ? `<div class="photo-gallery-more"><div>
        ${paras}
        ${source}
      </div></div>
      <p class="photo-gallery-hint">閱讀更多</p>` : source}
    `;
  }

  /* 觸控裝置：點擊說明區展開／收合 */
  body.addEventListener('click', (event) => {
    if (event.target.closest('a')) return;
    if (window.matchMedia('(hover: none)').matches) body.classList.toggle('is-expanded');
  });
});

/* OCR PDF page previews use one delegated listener so the click remains active
   while the animation replaces the visible page image. */
document.addEventListener('click', (event) => {
  const img = event.target;
  if (!img || img.getAttribute?.('data-ocr-page-img') === null) return;
  const fileStack = img.parentElement?.parentElement;
  const script = fileStack?.querySelector('script[data-ocr-pages]');
  if (!fileStack || !script) return;
  let pages = [];
  try {
    pages = JSON.parse(script.textContent).filter(Boolean);
  } catch (error) {
    return;
  }
  if (!pages.length) return;
  const currentSrc = String(img.getAttribute('src') || img.src || '');
  const currentIndex = pages.findIndex((src) => currentSrc.endsWith(String(src)));
  const documentMeta = fileStack.classList.contains('handwritten')
    ? {
        title: '為奏彰化失陷已調兵赴臺事｜黃仕簡｜1786/12/10 sent',
        descriptionHtml: '黃仕簡，〈為奏彰化失陷已調兵赴臺事〉（1786/12/10），〈奏聞臺灣彰化縣賊匪殺官陷城及奴才辦理赴剿緣由事〉，《宮中檔奏摺—乾隆朝》，乾隆51年12月10日，故宮075543號，件1。國立故宮博物院，<a href="https://qingarchives.npm.edu.tw/index.php?act=Display/image/8760364P-6I=Vw#08l" target="_blank" rel="noopener noreferrer">《清代檔案檢索系統》</a>（<a href="https://qingarchives.npm.edu.tw/index.php?act=Display/image/8760364P-6I=Vw/pdf#08l" target="_blank" rel="noopener noreferrer">PDF影像</a>），瀏覽日期：2026/08/04。'
      }
    : {
        title: '為奏彰化失陷已調兵赴臺事｜黃仕簡｜1786/12/10 sent',
        description: '黃仕簡，〈為奏彰化失陷已調兵赴臺事〉（1786/12/10），《明清台灣檔案匯編》，第30冊，頁80，硃25。'
      };
  photoLightbox.openGallery(pages, currentIndex < 0 ? 0 : currentIndex, {
    title: fileStack.getAttribute('data-ocr-document-title') || documentMeta.title,
    captionTitle: '',
    showPageNumber: false,
    description: fileStack.getAttribute('data-ocr-document-description') || documentMeta.description,
    descriptionHtml: documentMeta.descriptionHtml
  }, img);
});

const routeGalleryPages = [
  {
    image: '../Visual Material/印版平定台湾战图册6.png',
    alt: '《印版平定臺灣戰圖冊》的戰事圖像',
    title: '奏摺抵達御前',
    text: '柴大紀的奏摺經福建、江蘇、山東的驛站輾轉傳遞，歷時一個月，在一月二日始送達御前。乾隆帝硃批：「已有旨了。」',
    source: '柴大紀奏摺傳遞記錄'
  },
  {
    image: '../Visual Material/img2_4_2.jpg',
    alt: '清代軍事文獻的冊頁與裝幀',
    title: '軍機處登記同日軍情',
    text: '乾隆帝硃批後，奏摺交由軍機處登記和辦理。根據當日的《軍機處隨手登記檔》，乾隆帝當天不僅收到柴大紀的奏摺，還包括閩浙總督常青、福建巡撫徐嗣曾與福建水師提督黃仕簡所上的奏摺，同樣奏報臺灣的軍情。',
    source: '《軍機處隨手登記檔》'
  },
  {
    image: 'taiwan-route-source-page.png',
    alt: '《乾隆重要戰爭之軍需研究》〈台灣之役〉頁面',
    title: '諭旨廷寄與柴大紀',
    text: '據《登記檔》所載，乾隆帝當日下了兩道諭旨，其中一道〈諭閩浙總督常青等總須鎮定持重並俟兵丁到齊約期夾攻〉也廷寄給了柴大紀，嘉許了他嚴守臺灣府城，並命他迅速剿滅匪徒，收復失地。',
    source: '《登記檔》所載諭旨'
  }
];

const animateRouteLayer = (map, direction) => new Promise((resolve) => {
  const outbound = map.querySelector('.route-line-outbound');
  const returning = map.querySelector('.route-line-return');
  const layer = direction === 'return' ? returning : outbound;
  if (!layer) {
    resolve();
    return;
  }
  if (direction === 'return') {
    returning?.classList.remove('is-visible', 'is-running');
  } else {
    [outbound, returning].forEach((item) => item?.classList.remove('is-visible', 'is-running'));
  }
  window.requestAnimationFrame(() => {
    layer.classList.add('is-visible', 'is-running');
    const duration = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 1000;
    window.setTimeout(resolve, duration);
  });
});

const initRouteMap = (map) => {
  const taiwanPin = map.querySelector('[data-route-pin="taiwan"]');
  const beijingPin = map.querySelector('[data-route-pin="beijing"]');
  const taiwanInfo = map.querySelector('[data-route-info="taiwan"]');
  const beijingInfo = map.querySelector('[data-route-info="beijing"]');
  const line = map.querySelector('.route-line-svg');
  if (!taiwanPin || !beijingPin || !taiwanInfo || !beijingInfo || !line) return;

  const state = {
    page: 0,
    routeStarted: false,
    routeRunning: false
  };
  const galleryImage = beijingInfo.querySelector('[data-gallery-image]');
  const galleryPage = beijingInfo.querySelector('[data-gallery-page]');
  const galleryTitle = beijingInfo.querySelector('[data-gallery-title]');
  const galleryText = beijingInfo.querySelector('[data-gallery-text]');
  const gallerySource = beijingInfo.querySelector('[data-gallery-source]');
  const galleryPrevious = beijingInfo.querySelector('[data-gallery-prev]');
  const galleryNext = beijingInfo.querySelector('[data-gallery-next]');

  const renderGalleryPage = (pageIndex, { replayRoute = false } = {}) => {
    state.page = Math.max(0, Math.min(routeGalleryPages.length - 1, pageIndex));
    const page = routeGalleryPages[state.page];
    galleryImage.src = page.image;
    galleryImage.alt = page.alt;
    ['fit', 'position', 'zoom'].forEach((key) => galleryImage.style.removeProperty(`--route-photo-${key}`));
    if (page.fit) galleryImage.style.setProperty('--route-photo-fit', page.fit);
    if (page.position) galleryImage.style.setProperty('--route-photo-position', page.position);
    if (page.zoom) galleryImage.style.setProperty('--route-photo-zoom', String(page.zoom));
    galleryTitle.textContent = page.title;
    galleryText.textContent = page.text;
    gallerySource.textContent = page.source;
    galleryPage.textContent = `${state.page + 1} / ${routeGalleryPages.length}`;
    galleryPrevious.disabled = state.page === 0;
    galleryNext.textContent = state.page === routeGalleryPages.length - 1 ? '再次播放路線' : '下一頁';
    if (replayRoute && state.page === routeGalleryPages.length - 1) {
      window.setTimeout(() => animateRoute({ replay: true }), 120);
    }
  };

  const revealBeijing = () => {
    beijingPin.removeAttribute('hidden');
    beijingInfo.hidden = false;
  };

  const animateRoute = async ({ replay = false } = {}) => {
    if (state.routeRunning) return;
    state.routeRunning = true;
    await animateRouteLayer(map, replay ? 'return' : 'outbound');
    if (!replay) revealBeijing();
    state.routeRunning = false;
  };

  const revealTaiwan = () => {
    taiwanInfo.hidden = false;
    taiwanPin.classList.add('is-active');
    taiwanPin.setAttribute('aria-expanded', 'true');
    if (!state.routeStarted) {
      state.routeStarted = true;
      window.setTimeout(() => animateRoute(), 140);
    }
  };

  const activatePin = (pin) => {
    if (pin === taiwanPin) revealTaiwan();
    if (pin === beijingPin && !beijingPin.hasAttribute('hidden')) beijingInfo.hidden = false;
  };

  [taiwanPin, beijingPin].forEach((pin) => {
    pin.addEventListener('click', () => activatePin(pin));
    pin.addEventListener('keydown', (event) => {
      if (event.key !== 'Enter' && event.key !== ' ') return;
      event.preventDefault();
      activatePin(pin);
    });
  });

  taiwanInfo.querySelector('[data-route-close]').addEventListener('click', () => {
    taiwanInfo.hidden = true;
    taiwanPin.classList.remove('is-active');
    taiwanPin.setAttribute('aria-expanded', 'false');
  });
  beijingInfo.querySelector('[data-route-close]').addEventListener('click', () => { beijingInfo.hidden = true; });
  galleryImage.addEventListener('click', () => {
    const page = routeGalleryPages[state.page];
    photoLightbox.open(page.image, page.alt, `${page.title}｜${page.source}`, galleryImage);
  });
  galleryPrevious.addEventListener('click', () => renderGalleryPage(state.page - 1));
  galleryNext.addEventListener('click', () => {
    if (state.page < routeGalleryPages.length - 1) {
      renderGalleryPage(state.page + 1, { replayRoute: state.page + 1 === routeGalleryPages.length - 1 && state.routeStarted });
    } else {
      animateRoute({ replay: true });
    }
  });
  renderGalleryPage(0);
};
document.querySelectorAll('[data-route-map]').forEach(initRouteMap);

/* ---------------------------------------------------------------------------
   GIF 示範的浮動標註：把每張說明卡片連到 GIF 上對應的圓點。
   卡片與圓點的位置都由 storymap-cards.css 的變數決定，這裡只負責依照兩者
   當下的實際位置，計算連接線的角度與長度並畫出來；視窗縮放或版面變動時
   會自動重畫，因此不需要在 CSS 裡手動指定線的座標。
   --------------------------------------------------------------------------- */
const initGifAnnotations = (block) => {
  const layer = block.querySelector('[data-line-layer]');
  if (!layer) return;

  const draw = () => {
    layer.innerHTML = '';
    // 小螢幕已改為單欄排列並隱藏連接線，不需要計算。
    if (window.getComputedStyle(layer).display === 'none') return;

    const blockRect = block.getBoundingClientRect();

    block.querySelectorAll('[data-dot]').forEach((dot) => {
      const label = block.querySelector(`[data-label="${dot.getAttribute('data-dot')}"]`);
      if (!label) return;

      const dotRect = dot.getBoundingClientRect();
      const labelRect = label.getBoundingClientRect();
      const dotCx = dotRect.left + dotRect.width / 2;
      const dotCy = dotRect.top + dotRect.height / 2;

      // 自動計算的起點（圓點）與終點（卡片邊框上離圓點最近的一點，
      // 通常是卡片底邊，這樣線不會穿過卡片文字）。
      let dx = dotCx - blockRect.left;
      let dy = dotCy - blockRect.top;
      let lx = Math.max(labelRect.left, Math.min(dotCx, labelRect.right)) - blockRect.left;
      let ly = Math.max(labelRect.top, Math.min(dotCy, labelRect.bottom)) - blockRect.top;

      // 手動微調（全部可省略，省略時就是上面的自動結果）。
      // 數值寫在 storymap-cards.css：整組「圓點＋線」的設定寫在圓點的區塊，
      // 卡片端的微調寫在卡片的區塊；兩邊都會被讀取。
      const dotStyle = window.getComputedStyle(dot);
      const labelStyle = window.getComputedStyle(label);
      const num = (name) => {
        const raw = (dotStyle.getPropertyValue(name) || labelStyle.getPropertyValue(name)).trim();
        if (!raw) return null;
        const value = parseFloat(raw);
        return Number.isFinite(value) ? value : null;
      };

      // 註：--mark-x／--mark-y 由 CSS 直接位移圓點，圓點的實際座標已經含在
      // dotRect 裡，所以線的起點會自動跟著一起移動，這裡不必再加一次。

      // --line-from-x／--line-from-y：只移動線的起點，圓點不動
      dx += num('--line-from-x') || 0;
      dy += num('--line-from-y') || 0;
      // --line-to-x／--line-to-y：把線的「終點」（卡片端）平移幾 px
      lx += num('--line-to-x') || 0;
      ly += num('--line-to-y') || 0;

      // --line-angle：直接指定線的角度（度，0 = 向右、90 = 向下）
      // --line-length：直接指定線的長度（px）
      const autoAngle = Math.atan2(ly - dy, lx - dx) * 180 / Math.PI;
      const autoLength = Math.hypot(lx - dx, ly - dy);
      const angle = num('--line-angle');
      const length = num('--line-length');

      const line = document.createElement('span');
      line.className = 'annotation-line';
      line.style.left = `${dx}px`;
      line.style.top = `${dy}px`;
      line.style.width = `${length === null ? autoLength : length}px`;
      line.style.transform = `rotate(${angle === null ? autoAngle : angle}deg)`;
      layer.appendChild(line);
    });
  };

  const img = block.querySelector('img');
  if (img && !img.complete) img.addEventListener('load', draw);
  window.addEventListener('resize', draw);
  if (typeof ResizeObserver === 'function') new ResizeObserver(draw).observe(block);
  draw();
};
document.querySelectorAll('[data-gif-annotate]').forEach(initGifAnnotations);

/* ---------------------------------------------------------------------------
   第三部分互動標籤
   --------------------------------------------------------------------------- */
const initPart3OriginalCharts = () => {
  document.querySelectorAll('[data-part3-chart-toggle]').forEach((button) => {
    const group = button.closest('.part3-chart-frame, .part3-flow-frame');
    if (!group) return;
    button.addEventListener('click', () => {
      group.querySelectorAll('[data-part3-chart-toggle]').forEach((item) => {
        const active = item === button;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
    });
  });
};
initPart3OriginalCharts();

const initPart3ToolsChecklist = () => {
  document.querySelectorAll('[data-part3-tools-checklist]').forEach((workbench) => {
    const rows = [...workbench.querySelectorAll('[data-part3-tool-id]')];
    const views = [...workbench.querySelectorAll('[data-part3-tool-info]')];
    if (!rows.length || !views.length) return;

    const selectTool = (id) => {
      const row = rows.find((item) => item.dataset.part3ToolId === id);
      const view = views.find((item) => item.dataset.part3ToolInfo === id);
      if (!row || !view) return;
      rows.forEach((item) => item.classList.toggle('is-active', item === row));
      views.forEach((item) => { item.hidden = item !== view; });
    };

    rows.forEach((row) => {
      row.addEventListener('change', () => selectTool(row.dataset.part3ToolId));
      row.addEventListener('click', () => selectTool(row.dataset.part3ToolId));
    });
    selectTool(rows[0].dataset.part3ToolId);
  });
};
initPart3ToolsChecklist();

/* ---------------------------------------------------------------------------
   版面特徵探索器（7 辨識印刷字 / 8 辨識手寫字）
   左半是原件：印刷本為書冊翻頁，手寫本為風琴摺（每張掃描分三摺，
   固定兩摺一組展開）。點擊標籤會標示該特徵所在位置，右半同時逐字播出
   「AI 指示 → AI 生成的 Python 代碼 → OCR 的輸出結果」三個視窗。
   內容全部來自 storymap-example.html 的 data-part3-feature-data JSON。
   --------------------------------------------------------------------------- */
const initPart3FeatureExplorers = () => {
  const CHAT_ICONS = `
    <span class="part3-fx-chat-ic">+</span>
    <span class="part3-fx-chat-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9 10h.01M15 10h.01M9 15c1.5 1 4.5 1 6 0"/></svg></span>
    <span class="part3-fx-chat-model"><span class="spin"></span>5.6<span class="chev">▾</span></span>
    <span class="part3-fx-chat-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></span>
    <span class="part3-fx-chat-send">↑</span>`;

  const outMarkup = `
    <div class="part3-fx-feat">
      <span class="k">版面特徵</span>
      <h3 data-fx-title></h3>
      <p data-fx-desc></p>
    </div>
    <div class="part3-fx-arrow" aria-hidden="true">↓</div>
    <div class="part3-fx-chat">
      <div class="part3-fx-win-bar"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span><span class="ttl">AI Prompt</span></div>
      <div class="part3-fx-chat-body">
        <div class="part3-fx-chat-input">
          <div class="part3-fx-chat-text" data-fx-prompt></div>
          <div class="part3-fx-chat-row">${CHAT_ICONS}</div>
        </div>
      </div>
    </div>
    <div class="part3-fx-arrow" aria-hidden="true">↓</div>
    <div class="part3-fx-win">
      <div class="part3-fx-win-bar"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span><span class="ttl">AI 生成的 Python 代碼</span></div>
      <div class="part3-fx-win-body" data-fx-py></div>
    </div>
    <div class="part3-fx-arrow" aria-hidden="true">↓</div>
    <div class="part3-fx-win">
      <div class="part3-fx-win-bar"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span><span class="ttl">OCR 的輸出結果</span></div>
      <div class="part3-fx-win-body" data-fx-json></div>
    </div>`;

  document.querySelectorAll('[data-part3-explorer]').forEach((root) => {
    const data = parseJsonScript(root);
    const features = (data && data.features) || [];
    if (!features.length) return;

    /* 標籤與標示區的位置、大小、顏色全部走 CSS 變數。
       這裡把 JSON 內的數值寫成「低優先度」的預設樣式（選擇器只用屬性，
       不用 id），storymap-cards.css 便可以用 #id 選擇器覆寫任何一項，
       不必改動 HTML 或這支程式。 */
    const kind = root.dataset.part3Explorer;
    const injectDefaults = () => {
      const rules = features.map((f) => {
        const box = f.box || {};
        const tag = f.tag || {};
        const decls = [
          `--fx-color: ${f.colour || '#e6e0d4'}`,
          `--fx-left: ${box.left || '0%'}`,
          `--fx-top: ${box.top || '0%'}`,
          `--fx-width: ${box.width || '0%'}`,
          `--fx-height: ${box.height || '0%'}`,
          `--fx-tag-left: ${tag.left || 'auto'}`,
          `--fx-tag-right: ${tag.right || 'auto'}`,
          `--fx-tag-top: ${tag.top || 'auto'}`
        ].join('; ');
        return `[data-part3-explorer="${kind}"] [data-fx-feature="${f.key}"] { ${decls}; }`;
      });
      const style = document.createElement('style');
      style.dataset.part3FxDefaults = kind;
      style.textContent = rules.join('\n');
      document.head.appendChild(style);
    };
    injectDefaults();

    const out = root.querySelector('[data-part3-fx-out]');
    out.innerHTML = outMarkup;
    const elTitle = out.querySelector('[data-fx-title]');
    const elDesc = out.querySelector('[data-fx-desc]');
    const elPrompt = out.querySelector('[data-fx-prompt]');
    const elPy = out.querySelector('[data-fx-py]');
    const elJson = out.querySelector('[data-fx-json]');

    const tagHost = root.querySelector('[data-part3-fx-tags]');
    const indEl = root.querySelector('[data-part3-fx-ind]');
    const prevBtn = root.querySelector('[data-part3-fx-prev]');
    const nextBtn = root.querySelector('[data-part3-fx-next]');
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    let cur = 0;
    const timers = [];
    const stopTyping = () => { while (timers.length) window.clearTimeout(timers.pop()); };

    // 逐字播出：純文字（AI 指示）與含語法標色的 HTML（代碼／JSON）分開處理。
    const typeText = (host, text, speed, caretClass, perTick) => {
      let i = 0;
      const step = () => {
        i = Math.min(i + perTick, text.length);
        host.textContent = text.slice(0, i);
        if (i < text.length) {
          const caret = document.createElement('span');
          caret.className = caretClass;
          host.appendChild(caret);
          timers.push(window.setTimeout(step, speed));
        }
      };
      step();
    };
    // 含標色標籤的內容：先整段放進 DOM，再把文字節點清空後逐字補回，
    // 這樣顏色標籤不會被切斷（與 revealAgenticLine 相同做法）。
    const typeHtml = (host, html, speed, perTick) => {
      host.innerHTML = html;
      const walker = document.createTreeWalker(host, NodeFilter.SHOW_TEXT);
      const nodes = [];
      let node;
      while ((node = walker.nextNode())) { nodes.push({ node, full: node.textContent }); node.textContent = ''; }
      if (!nodes.length) return;
      let ni = 0;
      const step = () => {
        let budget = perTick;
        while (budget > 0 && ni < nodes.length) {
          const entry = nodes[ni];
          const shown = entry.node.textContent.length;
          if (shown >= entry.full.length) { ni += 1; continue; }
          const take = Math.min(budget, entry.full.length - shown);
          entry.node.textContent = entry.full.slice(0, shown + take);
          budget -= take;
        }
        if (ni < nodes.length) timers.push(window.setTimeout(step, speed));
      };
      step();
    };

    const showFeature = (index) => {
      const f = features[index];
      if (!f) return;
      cur = index;
      syncToCurrent();
      render();
      stopTyping();
      elTitle.textContent = f.title;
      elDesc.textContent = f.desc;
      if (reduceMotion) {
        elPrompt.textContent = f.prompt;
        elPy.innerHTML = f.py;
        elJson.innerHTML = f.json;
        return;
      }
      elPrompt.textContent = '';
      elPy.innerHTML = '';
      elJson.innerHTML = '';
      // 三個視窗同時開始，速度較快
      typeText(elPrompt, f.prompt, 18, 'part3-fx-caret part3-fx-caret-chat', 2);
      typeHtml(elPy, f.py, 14, 4);
      typeHtml(elJson, f.json, 14, 4);
    };

    const buildTags = (isOnScreen, positioned) => {
      tagHost.innerHTML = '';
      features.forEach((f, i) => {
        const tag = document.createElement('button');
        tag.type = 'button';
        const other = !isOnScreen(f);
        tag.className = 'part3-fx-tag'
          + (i === cur ? ' is-active' : ' is-dim')
          + (other ? ' is-other' : '');
        // 位置與顏色一律交由 CSS 變數決定（預設值見下方 injectDefaults()，
        // 實際微調請改 storymap-cards.css），這裡只標上是哪一個特徵。
        tag.dataset.fxFeature = f.key;
        if (positioned) tag.classList.add('is-floating');
        const label = f.title.split('：')[0].split('（')[0];
        tag.innerHTML = label;
        tag.addEventListener('click', () => showFeature(i));
        tagHost.appendChild(tag);
      });
    };

    let render = () => {};
    let syncToCurrent = () => {};

    /* ---------- 7 印刷字：書冊翻頁 ---------- */
    if (root.dataset.part3Explorer === 'printed') {
      const pages = data.pages || [];
      const img = root.querySelector('[data-part3-fx-img]');
      const hlHost = root.querySelector('[data-part3-fx-hl]');
      const pageEl = img.parentElement;
      let page = 0;
      let turning = false;
      features.forEach((f) => { f.badge = `p.${(f.page || 0) + 1}`; });

      const paintPage = () => {
        img.src = pages[page];
        indEl.textContent = `頁 ${page + 1} / ${pages.length}`;

        prevBtn.disabled = page === 0;
        nextBtn.disabled = page === pages.length - 1;
        hlHost.innerHTML = '';
        const f = features[cur];
        if (f && (f.page || 0) === page) {
          const hl = document.createElement('div');
          hl.className = 'part3-fx-hl is-active';
          hl.dataset.fxFeature = f.key;
          hlHost.appendChild(hl);
        }
        buildTags((f) => (f.page || 0) === page, true);
      };
      render = paintPage;

      // 翻頁：新的一頁自右滑入疊在舊頁之上，像翻動檔案夾裡的紙張。
      const turnTo = (next, dir) => {
        if (turning || next === page || next < 0 || next >= pages.length) return;
        if (reduceMotion) { page = next; paintPage(); return; }
        turning = true;
        const sheet = document.createElement('div');
        sheet.className = 'part3-fx-turn';
        const sImg = document.createElement('img');
        sheet.appendChild(sImg);
        if (dir > 0) {
          sImg.src = pages[next];
          sheet.style.transform = 'translateX(102%)';
          pageEl.appendChild(sheet);
          window.requestAnimationFrame(() => {
            sheet.style.transition = 'transform .5s cubic-bezier(.33,.9,.3,1)';
            sheet.style.transform = 'translateX(0)';
          });
        } else {
          sImg.src = pages[page];
          sheet.style.transform = 'translateX(0)';
          pageEl.appendChild(sheet);
          img.src = pages[next];
          window.requestAnimationFrame(() => {
            sheet.style.transition = 'transform .5s cubic-bezier(.33,.9,.3,1)';
            sheet.style.transform = 'translateX(102%)';
          });
        }
        window.setTimeout(() => { page = next; sheet.remove(); turning = false; paintPage(); }, 520);
      };
      prevBtn.addEventListener('click', () => turnTo(page - 1, -1));
      nextBtn.addEventListener('click', () => turnTo(page + 1, 1));
      // 選到其他頁的特徵時，先翻到該頁，翻頁動畫結束後再標示
      render = () => {
        const f = features[cur];
        const target = f ? (f.page || 0) : page;
        if (target !== page && !turning) { turnTo(target, target > page ? 1 : -1); return; }
        paintPage();
      };
      paintPage();
    }

    /* ---------- 8 手寫字：風琴摺 ---------- */
    if (root.dataset.part3Explorer === 'folded') {
      const strip = root.querySelector('[data-part3-fx-strip]');
      const sheets = data.sheets || [];
      const panels = [];
      sheets.forEach((src) => { [2, 1, 0].forEach((part) => panels.push({ src, part })); });
      const pairCount = Math.ceil(panels.length / 2);
      const pairOf = (i) => Math.floor(i / 2);
      let pair = 0;
      features.forEach((f) => { f.badge = `第 ${(f.panel || 0) + 1} 摺`; });

      panels.forEach((p, i) => {
        const el = document.createElement('div');
        el.className = 'part3-fx-panel';
        el.style.setProperty('--src', `url("${p.src}")`);
        el.style.setProperty('--posx', `${p.part * 50}%`);
        if (data.foldAspect) el.style.setProperty('--fold-aspect', data.foldAspect);
        el.addEventListener('click', () => { pair = pairOf(i); render(); });
        strip.appendChild(el);
      });

      // 只有「選取特徵」時才跳到該摺所在的組；上一組／下一組按鈕自行翻頁，
      // 不可在 render() 內重設 pair，否則按鈕會被立刻覆蓋回原位。
      syncToCurrent = () => {
        const f = features[cur];
        if (f) pair = pairOf(f.panel || 0);
      };
      render = () => {
        const f = features[cur];
        const start = pair * 2;
        [...strip.children].forEach((el, i) => {
          const open = i === start || i === start + 1;
          el.classList.toggle('is-open', open);
          const old = el.querySelector('.part3-fx-hl');
          if (old) old.remove();
          if (open && f && (f.panel || 0) === i) {
            const hl = document.createElement('div');
            hl.className = 'part3-fx-hl is-active';
            hl.dataset.fxFeature = f.key;
            el.appendChild(hl);
          }
        });
        indEl.textContent = `頁 ${pair + 1} / ${pairCount}`;
        prevBtn.disabled = pair === 0;
        nextBtn.disabled = pair >= pairCount - 1;
        buildTags((ft) => pairOf(ft.panel || 0) === pair, true);
      };

      prevBtn.addEventListener('click', () => { if (pair > 0) { pair -= 1; render(); } });
      nextBtn.addEventListener('click', () => { if (pair < pairCount - 1) { pair += 1; render(); } });

      // 摺子寬度依可用寬度換算，確保展開的兩摺完整顯示且不變形
      const sizeStrip = () => {
        const pane = strip.parentElement;
        const cs = window.getComputedStyle(pane);
        const avail = pane.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
        strip.style.setProperty('--fold-w', `${Math.max(avail, 240)}px`);
      };
      sizeStrip();
      window.addEventListener('resize', sizeStrip);
      if (typeof ResizeObserver === 'function') new ResizeObserver(sizeStrip).observe(strip.parentElement);
    }

    showFeature(0);
  });
};
// 呼叫寫在 parseJsonScript 定義之後（見 initAgenticScene 下方），避免 TDZ 錯誤。

const initPart3FlowNavigation = () => {
  document.querySelectorAll('[data-part3-flow-target]').forEach((button) => {
    button.addEventListener('click', () => {
      const target = button.dataset.part3FlowTarget;
      if (target) setActiveTab('part-3', { scrollTarget: target });
    });
  });
};
initPart3FlowNavigation();

/* ---------------------------------------------------------------------------
   Agentic AI 動畫場景：四個實際專案工作視窗逐字「打出來」再整段清空重播。
   每個視窗的內容（含語法標色用的 <span>）寫在 storymap-example.html 裡
   對應的 <script type="application/json"> 區塊，這裡只負責播放。
   --------------------------------------------------------------------------- */
const wait = (ms) => new Promise((resolve) => window.setTimeout(resolve, ms));

// 把一行（可能包含 <span class="..."> 這類語法標色標籤）逐字顯示出來。
// 做法：先把整行內容放進 DOM（標籤結構都在），再把每個文字節點清空，
// 之後照文件順序一個字一個字補回去，這樣顏色標籤不會被字元切斷。
const revealAgenticLine = (host, html, charDelay) => new Promise((resolve) => {
  const lineEl = document.createElement('span');
  lineEl.className = 'line';
  lineEl.innerHTML = html;
  host.appendChild(lineEl);
  host.scrollTop = host.scrollHeight;

  const walker = document.createTreeWalker(lineEl, NodeFilter.SHOW_TEXT);
  const textNodes = [];
  let current;
  while ((current = walker.nextNode())) {
    textNodes.push({ node: current, full: current.textContent });
    current.textContent = '';
  }
  if (!textNodes.length) { resolve(); return; }

  let nodeIndex = 0;
  let charIndex = 0;
  const typeNextChar = () => {
    if (nodeIndex >= textNodes.length) { resolve(); return; }
    const entry = textNodes[nodeIndex];
    if (charIndex >= entry.full.length) { nodeIndex += 1; charIndex = 0; typeNextChar(); return; }
    entry.node.textContent += entry.full[charIndex];
    charIndex += 1;
    // 內容比顯示區長時，跟著游標往下捲動，讓正在打的那一行保持可見。
    host.scrollTop = host.scrollHeight;
    window.setTimeout(typeNextChar, charDelay);
  };
  typeNextChar();
});

// 播放一組行：逐行打出來、停留一段時間（含閃爍游標），再清空重新開始。
// 回傳一個「停止」函式，畫面離開可視範圍時呼叫它暫停，不必真的移除內容。
const typeAgenticSequence = (host, lines, { charDelay = 26, lineDelay = 450, holdTime = 2600, clearDelay = 500 } = {}) => {
  let cancelled = false;

  const run = async () => {
    while (!cancelled) {
      host.innerHTML = '';
      for (let i = 0; i < lines.length; i += 1) {
        if (cancelled) return;
        await revealAgenticLine(host, lines[i], charDelay);
        if (cancelled) return;
        if (i < lines.length - 1) await wait(lineDelay);
      }
      if (cancelled) return;
      const caret = document.createElement('span');
      caret.className = 'agentic-caret';
      host.appendChild(caret);
      await wait(holdTime);
      if (cancelled) return;
      caret.remove();
      await wait(clearDelay);
    }
  };
  run();

  return () => { cancelled = true; };
};

// 讀取一個元素內第一個 <script type="application/json"> 的內容並解析成陣列。
// Agentic AI 與 OCR 兩組動畫的文字／頁面清單都用這個共用小工具讀取。
const parseJsonScript = (host) => {
  const script = host.querySelector('script[type="application/json"]');
  if (!script) return [];
  try {
    return JSON.parse(script.textContent);
  } catch (error) {
    return [];
  }
};

const initAgenticScene = () => {
  document.querySelectorAll('[data-agentic-scene]').forEach((scene) => {
    const sequences = [...scene.querySelectorAll('[data-agentic-sequence]')]
      .map((host) => ({ host, lines: parseJsonScript(host) }))
      .filter((item) => item.lines.length);
    if (!sequences.length) return;

    // 使用者要求減少動態效果時，直接顯示完整內容，不逐字播放。
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      const renderStatic = (host, lines) => {
        host.innerHTML = lines.map((line) => `<span class="line">${line}</span>`).join('');
      };
      sequences.forEach(({ host, lines }) => renderStatic(host, lines));
      return;
    }

    let stops = [];
    const start = () => {
      if (stops.length) return;
      stops = sequences.map(({ host, lines }) => typeAgenticSequence(host, lines, {
        charDelay: Number(host.dataset.agenticCharDelay) || 26,
        lineDelay: Number(host.dataset.agenticLineDelay) || 420,
        holdTime: Number(host.dataset.agenticHoldTime) || 2600,
        clearDelay: Number(host.dataset.agenticClearDelay) || 500
      }));
    };
    const stop = () => {
      stops.forEach((cancel) => cancel());
      stops = [];
    };

    // 畫面不在可視範圍（包含被 checklist 切到 hidden）時暫停播放，省資源。
    if (typeof IntersectionObserver === 'function') {
      new IntersectionObserver((entries) => {
        entries.forEach((entry) => { entry.isIntersecting ? start() : stop(); });
      }, { threshold: .1 }).observe(scene);
    } else {
      start();
    }
  });
};
initAgenticScene();

// 版面特徵探索器：函式定義在上方，但要等 parseJsonScript 宣告後才能執行。
initPart3FeatureExplorers();

// Codex 視窗分成兩個階段：先逐步顯示工作／思考過程，完成後隱藏該過程，
// 只保留安裝結果。離開可視範圍時取消本次播放，重新進入時從頭開始。
const renderAgenticLines = (host, lines) => {
  host.innerHTML = lines.map((line) => `<span class="line">${line}</span>`).join('');
};

const typeAgenticCodexPhases = (thinkingPhase, thinkingHost, resultPhase, resultHost, thinkingLines, resultLines, options = {}) => {
  let cancelled = false;
  const charDelay = Number(options.charDelay) || 12;
  const lineDelay = Number(options.lineDelay) || 320;

  const run = async () => {
    thinkingPhase.hidden = false;
    resultPhase.hidden = true;
    thinkingHost.innerHTML = '';
    resultHost.innerHTML = '';
    for (let i = 0; i < thinkingLines.length; i += 1) {
      if (cancelled) return;
      await revealAgenticLine(thinkingHost, thinkingLines[i], charDelay);
      if (cancelled) return;
      if (i < thinkingLines.length - 1) await wait(lineDelay);
    }
    if (cancelled) return;
    await wait(520);
    if (cancelled) return;
    thinkingPhase.hidden = true;
    resultPhase.hidden = false;
    renderAgenticLines(resultHost, resultLines);
  };
  run();

  return () => { cancelled = true; };
};

const initAgenticCodexPhases = () => {
  document.querySelectorAll('[data-agentic-codex-phases]').forEach((body) => {
    const scene = body.closest('[data-agentic-scene]');
    const thinkingPhase = body.querySelector('[data-agentic-codex-thinking]');
    const thinkingHost = body.querySelector('[data-agentic-codex-thinking-sequence]');
    const resultPhase = body.querySelector('[data-agentic-codex-result]');
    const resultHost = body.querySelector('[data-agentic-codex-result-lines]');
    if (!scene || !thinkingPhase || !thinkingHost || !resultPhase || !resultHost) return;
    const thinkingLines = parseJsonScript(thinkingHost);
    const resultLines = parseJsonScript(resultHost);
    if (!thinkingLines.length || !resultLines.length) return;

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      thinkingPhase.hidden = true;
      resultPhase.hidden = false;
      renderAgenticLines(resultHost, resultLines);
      return;
    }

    let cancel = null;
    const start = () => {
      if (cancel) return;
      cancel = typeAgenticCodexPhases(thinkingPhase, thinkingHost, resultPhase, resultHost, thinkingLines, resultLines, {
        charDelay: thinkingHost.dataset.agenticCodexCharDelay,
        lineDelay: thinkingHost.dataset.agenticCodexLineDelay
      });
    };
    const stop = () => {
      if (!cancel) return;
      cancel();
      cancel = null;
    };

    if (typeof IntersectionObserver === 'function') {
      new IntersectionObserver((entries) => {
        entries.forEach((entry) => { entry.isIntersecting ? start() : stop(); });
      }, { threshold: .1 }).observe(scene);
    } else {
      start();
    }
  });
};
initAgenticCodexPhases();

// 運用 Agentic AI 使用 PaddleOCR：Codex 對話視窗與 PaddleOCR Python 視窗重疊排列，
// 點擊任一視窗即可把該視窗切換到最上層。
const initPart3AgenticOcrWindows = () => {
  document.querySelectorAll('[data-agentic-window]').forEach((windowEl) => {
    windowEl.addEventListener('click', () => {
      const scene = windowEl.closest('.agentic-scene-paddleocr');
      if (!scene) return;
      const target = windowEl.dataset.agenticWindow;
      scene.querySelectorAll('[data-agentic-window]').forEach((win) => {
        win.style.zIndex = win.dataset.agenticWindow === target ? 3 : 2;
        win.classList.toggle('is-agentic-front', win.dataset.agenticWindow === target);
      });
    });
  });
};
initPart3AgenticOcrWindows();

/* ---------------------------------------------------------------------------
   OCR 掃描動畫（「甚麼是 OCR？」）：兩份文書的頁面各自循環切換，
   下方 JSON 輸出區沿用 Agentic AI 動畫同一套逐字打字技巧（typeAgenticSequence）。
   --------------------------------------------------------------------------- */

// 把一張圖片換成下一頁：先淡出移到左邊，換圖後瞬間跳到右邊（不轉場），
// 再讓轉場動畫把它帶回中間，畫面上就是「從右邊翻頁進來」的效果。
const cycleOcrPage = (img, pages, { interval = 3400, turnMs = 420 } = {}) => {
  if (pages.length < 2) return () => {};
  let index = 0;
  let stopped = false;
  const timer = window.setInterval(() => {
    if (stopped) return;
    img.classList.add('is-turning');
    window.setTimeout(() => {
      if (stopped) return;
      index = (index + 1) % pages.length;
      img.src = pages[index];
      img.classList.add('is-jumping');
      void img.offsetWidth; // 強制 reflow，讓「跳到右側」不被轉場動畫拖慢
      img.classList.remove('is-jumping');
      img.classList.remove('is-turning');
    }, turnMs);
  }, interval);
  return () => { stopped = true; window.clearInterval(timer); };
};

const initOcrScanScene = () => {
  document.querySelectorAll('[data-ocr-scene]').forEach((scene) => {
    const pageImgs = [...scene.querySelectorAll('[data-ocr-page-img]')];
    const outputHost = scene.querySelector('[data-ocr-output]');
    if (!pageImgs.length || !outputHost) return;

    const pageSets = pageImgs.map((img) => {
      const script = img.parentElement.querySelector('script[data-ocr-pages]');
      if (!script) return [];
      try {
        return JSON.parse(script.textContent);
      } catch (error) {
        return [];
      }
    });

    const outputLines = parseJsonScript(outputHost);
    if (!outputLines.length) return;

    // 使用者要求減少動態效果時，只顯示第一頁與完整 JSON，不逐字播放。
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      outputHost.innerHTML = outputLines.map((line) => `<span class="line">${line}</span>`).join('');
      return;
    }

    let stopPages = [];
    let stopOutput = null;
    const start = () => {
      if (stopPages.length || stopOutput) return;
      // 兩份文書的翻頁間隔稍微錯開，避免同時翻頁顯得太整齊、不自然。
      stopPages = pageImgs.map((img, i) => cycleOcrPage(img, pageSets[i], { interval: 3200 + i * 700 }));
      // body 欄位是全文，字數較多，打字間隔調快一點，避免跑完一輪要等太久。
      stopOutput = typeAgenticSequence(outputHost, outputLines, { charDelay: 9, lineDelay: 220, holdTime: 3600, clearDelay: 500 });
    };
    const stop = () => {
      stopPages.forEach((fn) => fn());
      stopOutput?.();
      stopPages = [];
      stopOutput = null;
    };

    // 畫面不在可視範圍時暫停播放，省資源。
    if (typeof IntersectionObserver === 'function') {
      new IntersectionObserver((entries) => {
        entries.forEach((entry) => { entry.isIntersecting ? start() : stop(); });
      }, { threshold: .1 }).observe(scene);
    } else {
      start();
    }
  });
};
initOcrScanScene();

/* 9. 輸出格式：JSON — 標籤點擊捲動＋持續反白，段落二展開／收合。
   純互動，沒有動畫迴圈，不需要 IntersectionObserver。 */
const initJsonViewer = () => {
  const wrap = document.querySelector('.part3-json-viewer-wrap');
  if (!wrap) return;

  let selectedButton = null;
  let selectedTargets = [];
  wrap.querySelectorAll('[data-json-target]').forEach((button) => {
    button.setAttribute('aria-pressed', 'false');
    button.addEventListener('click', () => {
      const ids = button.dataset.jsonTarget.split(/\s+/);
      const targets = ids.map((id) => document.getElementById(id)).filter(Boolean);
      if (!targets.length) return;

      if (selectedButton) {
        selectedButton.classList.remove('is-selected');
        selectedButton.setAttribute('aria-pressed', 'false');
      }
      selectedTargets.forEach((el) => el.classList.remove('is-selected'));

      targets[0].scrollIntoView({ block: 'center', behavior: 'smooth' });
      button.classList.add('is-selected');
      button.setAttribute('aria-pressed', 'true');
      targets.forEach((el) => el.classList.add('is-selected'));
      selectedButton = button;
      selectedTargets = targets;
    });
  });

  /* 一個按鈕，兩種功能：收起來時顯示「...」（點擊＝展開），
     展開時顯示向上的「⌃」（點擊＝收起來）。按鈕放在完整段落之後，
     因此展開時會自然移到「等情前來。」之後。 */
  wrap.querySelectorAll('.para-toggle').forEach((btn) => {
    btn.addEventListener('click', () => {
      const rest = wrap.querySelector(`[data-para-rest="${btn.dataset.paraToggle}"]`);
      if (!rest) return;
      const isHidden = rest.hidden;
      rest.hidden = !isHidden;
      const expanded = isHidden;
      btn.textContent = expanded ? '⌃' : '...';
      btn.setAttribute('aria-label', expanded ? '收合' : '展開');
      btn.setAttribute('title', expanded ? '收合' : '展開');
    });
  });
};
initJsonViewer();

/* 10. OCR測試 — 批次掃描／驗證動畫。
   先單頁測試（1頁），再變成 2×2 持續往下捲的批次處理（50頁）。
   四份文書的內容逐字取自 review-tools/shared data/stage1_original_text.json。
   時間快慢在這裡調整；大小、顏色在 storymap-cards.css 的
   #part-3-test .batch-scene 區塊。 */
const initBatchTestScene = () => {
  const scene = document.querySelector('[data-batch-scene]');
  const track = scene && scene.querySelector('[data-batch-track]');
  if (!scene || !track) return;

  const DOCS = [
    {
      pageLg: 'ocr-anim-1-lg.jpg', pageSm: 'ocr-anim-1-sm.jpg',
      json: {
        doc_id: '硃25', doc_type: '硃批',
        title: '為奏彰化失陷已調兵赴臺事',
        official_post: '福建水師提督', author: '黃仕簡',
        send_date: '乾隆五十一年十二月十日',
        rescript_text: '已有旨了。欽此。',
        body: '福建水師提督一等海澄公奴才黃仕簡謹奏，為奏聞事。竊照臺灣近來屢有匪徒滋事，奴才時刻留心察查，不敢稍有懈忽。'
      }
    },
    {
      pageLg: 'ocr-anim-2-lg.jpg', pageSm: 'ocr-anim-2-sm.jpg',
      json: {
        doc_id: '奏2', doc_type: '上奏',
        title: '為奏林爽文結黨失陷彰城事',
        official_post: '福建陸路提督', author: '任承恩',
        send_date: '乾隆五十一年十二月十日',
        rescript_text: '已有旨了。',
        body: '福建陸路提督革職留任奴才任承恩跪奏，為奏聞事。本年十二月初九日亥刻，奴才接據署臺灣府淡水同知程峻、竹塹營守備董得魁會銜差役楊添投稟報稱。'
      }
    },
    {
      pageLg: 'ocr-anim-3-lg.jpg', pageSm: 'ocr-anim-3-sm.jpg',
      json: {
        doc_id: '奏5', doc_type: '上奏',
        title: '為奏辦理赴剿臺灣匪徒事',
        official_post: '福建水師提督', author: '黃仕簡',
        send_date: '乾隆五十一年十二月十日',
        rescript_text: '已有旨了。',
        body: '茲本年十二月初五日戌刻，訪聞得臺灣彰化縣屬又有匪徒聚集會黨，於十一月二十九日辰刻攻打彰化縣城，至午刻縣城被陷，文武官員不知生死之事。'
      }
    },
    {
      pageLg: 'ocr-anim-4-lg.jpg', pageSm: 'ocr-anim-4-sm.jpg',
      json: {
        doc_id: '台1', doc_type: '其他',
        title: '天地會林爽文起事告示',
        official_post: null, author: '林爽文',
        send_date: null,
        rescript_text: null,
        body: '順天盟主林，為祝天瀝示，以安民心，以保農業事。照得居官愛民如子，才稱為民父母也。今據臺灣皆貪官污吏，擾害生靈，本帥不忍不誅，以救吾民。'
      }
    }
  ];

  const renderJson = (obj) => {
    const rows = Object.entries(obj).map(([k, v]) => {
      const val = v === null ? '<span class="key">null</span>' : `<span class="str">"${v}"</span>`;
      return `&nbsp;&nbsp;<span class="key">"${k}"</span>: ${val},`;
    });
    return ['{', ...rows, '}'].join('<br>');
  };

  /* 兩種尺寸的頁面影像：單頁階段那一頁很大，用 lg（約 1290×940）；
     2×2 批次階段每格只有一百多 px 寬，用 sm（約 495×360）就綽綽有餘。
     這樣批次階段要點陣化的像素量大幅下降，畫面才不會卡。 */
  const makeTile = (doc, countLabel, { big = false } = {}) => {
    const src = big ? doc.pageLg : doc.pageSm;
    const tile = document.createElement('div');
    tile.className = 'tile';
    tile.innerHTML = `
      <div class="tile-page">
        <img class="page-dim" src="${src}" alt="" decoding="async" fetchpriority="low">
        <img class="page-full" src="${src}" alt="" decoding="async" fetchpriority="low">
        <span class="tile-scanline"></span>
      </div>
      <div class="tile-json">
        <div class="tile-json-bar"><span class="tile-json-dot r"></span><span class="tile-json-dot y"></span><span class="tile-json-dot g"></span></div>
        <div class="tile-json-body">${renderJson(doc.json)}<span class="tile-readbeam"></span></div>
      </div>
      <div class="tile-glasses">
        <span class="tile-glasses-shape"></span>
        <span class="tile-lens l"></span>
        <span class="tile-lens r"></span>
      </div>
      <div class="tile-tick"><svg viewBox="0 0 48 48"><circle cx="24" cy="24" r="20"></circle><path d="M15 24.5 L21.5 31 L33 19"></path></svg></div>
      <div class="tile-count">${countLabel}</div>`;
    return tile;
  };

  const reset = (tile) => {
    tile.classList.remove('is-scanning', 'is-scanned', 'is-json', 'is-reading', 'is-verified', 'is-active');
    const badge = tile.querySelector('.tile-count');
    if (badge) badge.classList.remove('is-bump');
  };

  /* 一格的完整流程：掃描 → 上色 → 翻成 JSON → 眼鏡閱讀 → 綠勾。
     綠勾出現的同一刻，這一格右下角的頁數標示也會放大變藍，
     跟單頁測試「1頁 → 50頁」那次轉換用同一個 .is-bump 效果。 */
  const runTile = async (tile, { scanDur = 1500, readDur = 1600, holdDur = 900 } = {}) => {
    reset(tile);
    tile.style.setProperty('--scan-dur', `${scanDur}ms`);
    tile.style.setProperty('--read-dur', `${readDur}ms`);
    tile.classList.add('is-active');
    await wait(120);
    tile.classList.add('is-scanning');
    await wait(scanDur);
    tile.classList.add('is-scanned');
    await wait(340);
    tile.classList.add('is-json');
    await wait(520);
    tile.classList.add('is-reading');
    await wait(readDur);
    tile.classList.add('is-verified');
    const badge = tile.querySelector('.tile-count');
    if (badge) badge.classList.add('is-bump');
    /* 綠勾＋藍色「50頁」在這裡停留 holdDur，之後 tile 仍然維持這個狀態
       （不會自動還原），只是持續往上捲的畫面最終會把它捲出視野。 */
    await wait(holdDur);
  };

  /* 頁數標示從「1頁」換成「50頁」：先淡出縮小、換好文字、再放大淡入變藍，
     避免文字寬度瞬間變寬造成的跳動感。 */
  const swapBadge = async (badge, newText) => {
    badge.classList.add('is-swapping');
    await wait(220);
    badge.textContent = newText;
    badge.classList.remove('is-swapping');
    badge.classList.add('is-bump');
    await wait(320);
  };

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* 每一次啟動都拿一個新的編號。捲出畫面時編號 +1，舊的流程一發現
     自己的編號過期就自行結束——否則捲進捲出幾次之後，會有好幾個
     流程同時在操作同一個 track，互相清空、重建格子，看起來就像綠勾
     和「50頁」不斷閃掉又冒出來。 */
  let runId = 0;
  let running = false;
  const pendingTimers = [];
  const clearTimers = () => {
    while (pendingTimers.length) window.clearTimeout(pendingTimers.pop());
  };

  const runLoop = async (id) => {
    const stale = () => id !== runId;
    while (!stale()) {
      /* ---- 第一階段：單頁測試（1頁） ---- */
      scene.classList.add('is-switching-out');
      await wait(420);
      if (stale()) return;
      scene.classList.remove('is-batch');
      track.style.removeProperty('--scroll-speed');
      track.innerHTML = '';
      const single = makeTile(DOCS[0], '1頁', { big: true });
      track.appendChild(single);
      await wait(30);
      scene.classList.remove('is-switching-out');
      await wait(480);
      if (stale()) return;
      await runTile(single, { scanDur: 1700, readDur: 1900 });
      if (stale()) return;

      /* 標示從「1頁」平順換成「50頁」（淡出→換字→放大淡入變藍） */
      const badge = single.querySelector('.tile-count');
      await swapBadge(badge, '50頁');
      await wait(500);
      if (stale()) return;

      /* ---- 轉場：單頁縮小淡出 ---- */
      scene.classList.add('is-switching-out');
      await wait(520);
      if (stale()) return;

      /* ---- 第二階段：批次（50頁），2×2 並持續往下捲 ---- */
      track.innerHTML = '';
      const tiles = [];
      /* 2 欄 × 4 列＝8 格（畫面上一次仍然看到 4 格）；捲動 -50% 時剛好
         接回開頭，看起來是無限往下。格數從 16 減到 8，同時要點陣化的
         大圖也少了一半。 */
      for (let i = 0; i < 8; i += 1) {
        const t = makeTile(DOCS[i % DOCS.length], '50頁');
        track.appendChild(t);
        tiles.push(t);
      }
      scene.classList.remove('is-switching-out');
      scene.classList.add('is-batch', 'is-switching-in');
      await wait(30);
      scene.classList.remove('is-switching-in');
      await wait(480);
      if (stale()) return;

      /* 捲動是 translateY(-50%) 無限循環，也就是「第 i 格」接回的位置正好是
         「第 i + 半數 格」。因此這兩格必須用同一個時間點跑動畫，否則循環
         接回的瞬間，剛驗證完的格子會被還沒驗證的複製格取代，看起來就像
         綠勾和「50頁」忽然消失又重新出現。這裡只替前半排時間，後半跟著同步。 */
      const half = tiles.length / 2;
      for (let i = 0; i < half; i += 1) {
        const pair = [tiles[i], tiles[i + half]];
        pendingTimers.push(window.setTimeout(() => {
          if (stale()) return;
          pair.forEach((t) => runTile(t, { scanDur: 2200, readDur: 1500, holdDur: 2600 }));
        }, i * 760));
      }

      await wait(half * 760 + 9000);
      if (stale()) return;
      await wait(600);
    }
  };

  /* 靜態版本：不動畫，直接顯示第一頁掃描完成後的 JSON 與綠勾 */
  if (reduceMotion) {
    const still = makeTile(DOCS[0], '1頁', { big: true });
    still.classList.add('is-scanned', 'is-json', 'is-verified');
    track.appendChild(still);
    return;
  }

  /* 只在看得見的時候跑；離開畫面時除了停掉流程，也把 CSS 動畫暫停
     （is-paused），避免捲動列與掃描光線在看不到的地方繼續耗繪圖資源。 */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        scene.classList.remove('is-paused');
        if (running) return;
        running = true;
        runLoop(runId);
      } else {
        scene.classList.add('is-paused');
        if (!running) return;
        running = false;
        /* 讓目前這個流程過期，並清掉還沒觸發的排程 */
        runId += 1;
        clearTimers();
      }
    });
  }, { threshold: .2 });
  observer.observe(scene);
};
initBatchTestScene();

const activateFromLocation = () => {
  const hash = window.location.hash || '#cover';
  const tabName = panelForHash(hash);
  const nestedTarget = (tabName === 'intro' && hash.startsWith('#intro-'))
    || (tabName === 'part-3' && hash !== '#part-3') ? hash : null;
  setActiveTab(tabName, { updateHash: false, scrollTarget: nestedTarget });
};
window.addEventListener('popstate', activateFromLocation);
window.addEventListener('hashchange', activateFromLocation);
activateFromLocation();
