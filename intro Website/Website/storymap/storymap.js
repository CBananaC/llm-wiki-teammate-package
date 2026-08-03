
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
  if (hash === '#part-3') return 'part-3';
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
  `;
  document.body.appendChild(overlay);
  const img = overlay.querySelector('img');
  const caption = overlay.querySelector('.photo-lightbox-caption');
  const closeBtn = overlay.querySelector('.photo-lightbox-close');
  let lastFocused = null;

  const close = () => {
    overlay.classList.remove('is-open');
    img.src = '';
    if (lastFocused) lastFocused.focus();
  };
  const open = (src, alt, captionText, triggerEl) => {
    lastFocused = triggerEl || null;
    img.src = src;
    img.alt = alt || '';
    if (captionText) { caption.textContent = captionText; caption.hidden = false; }
    else { caption.textContent = ''; caption.hidden = true; }
    overlay.classList.add('is-open');
    closeBtn.focus();
  };

  /* 點外部深色區域（不是圖片本身）即關閉 */
  overlay.addEventListener('click', (event) => {
    if (event.target === overlay || event.target === overlay.firstElementChild) close();
  });
  closeBtn.addEventListener('click', close);
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && overlay.classList.contains('is-open')) close();
  });

  return { open, close };
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
    body.classList.toggle('is-source-only', !hasDescription && hasSource);
    body.innerHTML = `
      <h3 class="photo-gallery-title">${page.title}</h3>
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

const activateFromLocation = () => {
  const hash = window.location.hash || '#cover';
  const tabName = panelForHash(hash);
  const nestedTarget = tabName === 'intro' && hash.startsWith('#intro-') ? hash : null;
  setActiveTab(tabName, { updateHash: false, scrollTarget: nestedTarget });
};
window.addEventListener('popstate', activateFromLocation);
window.addEventListener('hashchange', activateFromLocation);
activateFromLocation();
