
const setReviewFrameSource = () => {
  const frame = document.querySelector('.review-iframe');
  if (!frame) return;
  frame.src = location.protocol === 'file:'
    ? frame.dataset.fileSrc
    : 'http://127.0.0.1:8766/sample?embed=1&doc=%E7%A1%83%38%33&panels=ai%2Coriginal&v=20260728-chat-data';
};
setReviewFrameSource();

const settingsButton = document.getElementById('settings-button');
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
introDropdown.querySelectorAll('.nav-dropdown-menu a').forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    setActiveTab('intro', { scrollTarget: link.dataset.workflowTarget });
  });
});
workflowNodes.forEach((node) => {
  node.addEventListener('click', () => {
    workflowNodes.forEach((item) => item.classList.toggle('is-selected', item === node));
  });
});
document.addEventListener('click', (event) => {
  if (!introDropdown.contains(event.target)) setIntroDropdownOpen(false);
});
const sections = [...document.querySelectorAll('.story[data-tab]')];
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    const target = entry.target.dataset.nav || '#' + entry.target.id;
    const workflowTarget = entry.target.id.startsWith('intro-1-3-') ? '#' + entry.target.id : target;
    workflowNodes.forEach((node) => node.classList.toggle('is-selected', node.dataset.workflowTarget === workflowTarget));
  });
}, { threshold: 0.55 });
sections.forEach((section) => observer.observe(section));

const activateFromLocation = () => {
  const hash = window.location.hash || '#cover';
  const tabName = panelForHash(hash);
  const nestedTarget = tabName === 'intro' && hash.startsWith('#intro-') ? hash : null;
  setActiveTab(tabName, { updateHash: false, scrollTarget: nestedTarget });
};
window.addEventListener('popstate', activateFromLocation);
window.addEventListener('hashchange', activateFromLocation);
activateFromLocation();
