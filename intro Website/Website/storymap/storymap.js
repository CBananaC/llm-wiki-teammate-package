
const settingsButton = document.getElementById('settings-button');

document.querySelectorAll('.sample-doc-panel').forEach((panel) => {
  const minButton = panel.querySelector('.ip-min');
  const closeButton = panel.querySelector('.ip-close');
  const filterButton = panel.querySelector('.ip-filterbtn');
  const settingsButton = panel.querySelector('.ip-settingsbtn');
  minButton?.addEventListener('click', () => {
    panel.classList.toggle('is-folded');
    minButton.setAttribute('aria-expanded', String(!panel.classList.contains('is-folded')));
  });
  closeButton?.addEventListener('click', () => {
    panel.closest('.comparison-review-panel')?.setAttribute('hidden', '');
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

/* 圖片畫廊：左右翻頁、乾淨圖片、下方說明（預設只顯示標題，滑鼠移入展開）。
   每個 [data-photo-gallery] 讀取自己的 <script type="application/json"
   data-photo-gallery-data> 作為圖片與說明來源。 */
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
    const paras = (page.paragraphs || []).map((p) => `<p class="photo-gallery-desc">${p}</p>`).join('');
    const source = page.source
      ? `<p class="photo-gallery-source"><a href="${page.source.href}" target="_blank" rel="noopener noreferrer">${page.source.text} ↗</a></p>`
      : '';
    body.innerHTML = `
      <h3 class="photo-gallery-title">${page.title}</h3>
      <div class="photo-gallery-more"><div>
        ${paras}
        ${source}
      </div></div>
      <p class="photo-gallery-hint">將滑鼠移到此處查看完整說明</p>
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

const activateFromLocation = () => {
  const hash = window.location.hash || '#cover';
  const tabName = panelForHash(hash);
  const nestedTarget = tabName === 'intro' && hash.startsWith('#intro-') ? hash : null;
  setActiveTab(tabName, { updateHash: false, scrollTarget: nestedTarget });
};
window.addEventListener('popstate', activateFromLocation);
window.addEventListener('hashchange', activateFromLocation);
activateFromLocation();
