const parts = [
  {
    id: 'intro-1-1', tab: '1.1', number: '1.1 / 制度', title: '清代奏折制度', tone: 'paper', mark: '奏',
    position: '--card-x: 8vw; --card-y: 13vh; --card-w: 540px; --story-height: 1120px; --card-accent: #b66d48;',
    paragraphs: [
      '清代的上行官方文書主要包括題本、奏本和奏折。題本用於正式公務，奏本用於官員私人事務。兩者送達中央後，均須經過內閣票擬，才會呈送到皇帝手上。',
      '相反，奏摺主要由皇帝親信及地方大員使用，並由官員親自撰寫，密封後直送至御前，由皇帝親自審閱和硃批。雍正設立軍機處後，批閱完成的奏摺會交由軍機處處理，如需另行頒旨，則由軍機大臣擬寫上諭，經皇帝閱定後，再由內閣明發或由軍機處廷寄地方。',
      '奏摺制度省去了內閣票擬等的中間程序，使皇帝得以更直接和迅速地與地方官員溝通，掌握地方政務，進一步強化中央集權，學界因此普遍認為，奏折是清代最重要的官方文書制度。'
    ]
  },
  {
    id: 'intro-1-2', tab: '1.2', number: '1.2 / 研究價值', title: '清代奏折上諭的研究價值', tone: 'network', mark: '網',
    position: '--card-x: 52vw; --card-y: 19vh; --card-w: 560px; --story-height: 960px; --card-accent: #c7543f;',
    paragraphs: [
      '在清史研究中，奏摺是極為重要的第一手史料。奏摺、硃批與上諭完整保存了中央與地方在政治決策過程中的原始通信記錄，呈現地方資訊如何透過奏摺上達御前、皇帝如何藉硃批與上諭下達命令，以及在後續奏報中，地方官員如何對這些命令作出回應。因此，透過分析特定議題的相關奏摺與上諭，研究者得以重構該議題的政治決策過程。'
    ]
  },
  {
    id: 'intro-1-3-a', tab: '1.3', nav: 'intro-1-3', number: '1.3 / 01', title: '研究清代奏折的主要困難', tone: 'ink', mark: '困',
    position: '--card-x: 9vw; --card-y: 12vh; --card-w: 570px; --story-height: 1040px; --card-accent: #a45e4c;',
    paragraphs: [{
      before: '然而，研究奏折與上諭有不少困難。首先，部分議題的奏摺與上諭數量極為龐大。以研究白蓮教戰爭為例，學者戴英從指出，該戰爭的重要史料《欽定剿平三省邪匪方略》共有六十九冊，超過二萬七千頁。',
      citation: { href: '../references.html#ref-dai-2019', text: '（戴英從，2019，第一章，頁碼待核）' },
      after: '收錄了四千多份奏摺和上諭，篇幅之大令人望而卻步，當代學者對白蓮教戰爭的研究因此相當有限。'
    }]
  },
  {
    id: 'intro-1-3-b', tab: '1.3', nav: 'intro-1-3', number: '1.3 / 02', title: '研究清代奏折的主要困難', tone: 'gold', mark: '信',
    position: '--card-x: 48vw; --card-y: 18vh; --card-w: 570px; --story-height: 1040px; --card-accent: #ad7a35;',
    note: '通信關係的第二個層次',
    paragraphs: [
      '另外，奏摺與上諭之間涉及複雜的通信關係。最基本的一層，是地方官員奏報，皇帝再透過硃批或上諭作出回覆。然而，研究者不僅需要掌握每份奏摺和上諭的收發時間，也要釐清一份奏摺是否回應先前的硃批或上諭，以及皇帝發布的命令又在何時、由哪些官員於後續奏報中作出回應。'
    ]
  },
  {
    id: 'intro-1-3-c', tab: '1.3', nav: 'intro-1-3', number: '1.3 / 03', title: '研究清代奏折的主要困難', tone: 'river', mark: '流',
    position: '--card-x: 8vw; --card-y: 12vh; --card-w: 600px; --story-height: 1160px; --card-accent: #4d817c;',
    note: '事件、消息來源與資訊網絡',
    paragraphs: [
      '此外，針對奏摺所載的具體事件，研究者還要關注事件的發生時間及消息來源。而皇帝往往又會同時收到多位官員就同一事件的奏報，各奏報的的描述及消息來源都不盡相同，形成了錯綜複雜的消息網絡。',
      '因此，研究者既要分析單份文書所載的資訊，也要理解宏觀的資訊傳遞網絡。然而，面對大量文書及複雜的通信關係，研究者難以單憑人力掌握資訊傳遞的整體脈絡，因此需要運用視覺化工具，呈現文書之間的關聯與資訊流向。'
    ]
  },
  {
    id: 'intro-1-4', tab: '1.4', number: '1.4 / 數位方法', title: '以數位方法研究清代奏折和上諭', tone: 'archive', mark: 'AI',
    position: '--card-x: 7vw; --card-y: 13vh; --card-w: 470px; --story-height: 1200px; --card-accent: #7e6a39;',
    paragraphs: [
      '筆者認為，人工智能（AI）與視覺化的數位工具，能夠協助研究者處理上述的兩大難題，包括：'
    ],
    table: [
      ['研究困難', '數位工具', '如何協助研究'],
      ['史料數量龐大', 'AI', '總結長篇文本，協助研究者迅速掌握文書的主要內容，並判斷其中是否包含值得深入閱讀與分析的資訊。'],
      ['史料數量龐大', '人工智能技能（AI Skills）', '按照不同研究問題設計技能，讓AI從文本中提取特定資訊，並由研究者核對、審核及修正。'],
      ['通信關係複雜', 'Python 文本搜尋', '搜尋文書中的特定字詞，辨識奏摺與上諭之間的回應關係，重構官員與皇帝之間的資訊傳遞過程。'],
      ['通信關係複雜', '互動式網站', '以時間線和關係網絡等視覺化工具，呈現文書的收發時間及資訊傳遞的流向，協助研究者掌握宏觀的通信網絡。']
    ]
  },
  {
    id: 'intro-1-6-a', tab: '1.6', nav: 'intro-1-6', number: '1.6 / 示範案例', title: '示範案例：林爽文事件', tone: 'taiwan', mark: '林',
    position: '--card-x: 50vw; --card-y: 12vh; --card-w: 590px; --story-height: 1120px; --card-accent: #c7543f;',
    paragraphs: [
      '為展示本網站的研究方法及各項功能，本文將以林爽文民變作為示範案例。林爽文民變於乾隆五十一年（1786）爆發，歷時約兩年，由天地會領袖林爽文在臺灣中部的彰化發動，並迅速蔓延至臺灣多地，最終促使清廷派遣福康安率軍來臺鎮壓。乾隆帝其後將平定此役列為「十全武功」之一。'
    ]
  },
  {
    id: 'intro-1-6-b', tab: '1.6', nav: 'intro-1-6', number: '1.6 / 原因 01', title: '示範案例：林爽文事件', tone: 'network', mark: '延',
    position: '--card-x: 8vw; --card-y: 10vh; --card-w: 610px; --story-height: 1260px; --card-accent: #b66d48;',
    note: '選取林爽文民變作為示範案例，主要有以下原因：',
    paragraphs: [
      '第一，資訊傳遞是戰時軍事決策形成的重要環節。戰爭期間，地方官員須持續透過奏摺向皇帝奏報軍情、兵力部署及戰場變化，而皇帝則根據奏報發布上諭，指示軍事部署及後續行動，形成地方與中央之間持續往返的決策過程。然而，林爽文民變發生於臺灣，與北京相距遙遠，文書傳遞往往需時數星期。當皇帝收到奏摺時，前線局勢很可能已經改變，軍事決策因此仰賴前線官員臨機處置。因此，林爽文民變是一個合適的研究案例，用來探討資訊傳遞延遲如何影響戰時軍事決策的形成與執行。'
    ]
  },
  {
    id: 'intro-1-6-c', tab: '1.6', nav: 'intro-1-6', number: '1.6 / 原因 02', title: '示範案例：林爽文事件', tone: 'gold', mark: '史',
    position: '--card-x: 47vw; --card-y: 12vh; --card-w: 610px; --story-height: 1260px; --card-accent: #ad7a35;',
    paragraphs: [
      '第二，林爽文民變保存了大量奏摺與上諭，完整記錄戰時地方官員與皇帝之間的通信過程，為研究提供了豐富的材料。本研究主要採用《明清臺灣檔案彙編》（臺灣史料集成編輯委員會編）及《天地會檔案彙編》（中國人民大學清史研究所、中國第一歷史檔案館編）所收錄的奏摺和上諭。這些史料均經當代學者整理、校勘及出版，完整保留文書原文、文書類型、收發日期及硃批等重要資訊，為研究提供了可靠的材料。'
    ]
  }
];

const escapeHtml = (value) => String(value).replace(/[&<>"']/g, (char) => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[char]));
const paragraphHtml = (paragraphs) => paragraphs.map((paragraph) => {
  if (typeof paragraph === 'string') return `<p>${escapeHtml(paragraph)}</p>`;
  const citation = paragraph.citation
    ? `<a class="inline-reference" href="${escapeHtml(paragraph.citation.href)}">${escapeHtml(paragraph.citation.text)}</a>`
    : '';
  return `<p>${escapeHtml(paragraph.before || '')}${citation}${escapeHtml(paragraph.after || '')}</p>`;
}).join('');
const tableHtml = (rows) => `<table class="method-table"><thead><tr>${rows[0].map((cell) => `<th scope="col">${escapeHtml(cell)}</th>`).join('')}</tr></thead><tbody>${rows.slice(1).map((row) => `<tr>${row.map((cell) => `<td>${escapeHtml(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
const backdropHtml = (part) => {
  if (part.review) {
    return `<div class="backdrop review-backdrop" data-mark="台"><div class="review-window"><iframe class="review-iframe" data-file-src="../../../review-tools/(2)%20sample/index.html?embed=1&amp;doc=%E7%A1%83%38%33&amp;panels=ai%2Coriginal&amp;v=20260728-chat-data" title="硃83 AI 引文核驗示例"></iframe></div></div>`;
  }
  if (part.table) return `<div class="backdrop method-backdrop" data-mark="AI">${tableHtml(part.table)}</div>`;
  if (part.tone === 'signal') return `<div class="backdrop signal-backdrop" data-mark="流"><div class="signals"><span class="signal-label one">地方奏報</span><span class="signal-label two">皇帝回應</span><span class="signal-label three">後續回應</span></div></div>`;
  return `<div class="backdrop ${part.tone}" data-mark="${escapeHtml(part.mark)}"></div>`;
};
const partHtml = (part) => `<section class="story content-story" id="${part.id}" data-tab="${part.tab}" data-nav="#${part.nav || part.id}" style="${part.position}">${backdropHtml(part)}<article class="story-card"><h2>${escapeHtml(part.title)}</h2>${part.note ? `<div class="part-note">${escapeHtml(part.note)}</div>` : ''}${paragraphHtml(part.paragraphs)}</article></section>`;
document.getElementById('intro-content').innerHTML = parts.map(partHtml).join('');

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
applyFontScale(readFontScale());
settingsButton.addEventListener('click', () => setSettingsOpen(settingsPanel.hidden));
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

const tabs = [...document.querySelectorAll('.tabs a')];
const sections = [...document.querySelectorAll('.story[data-tab]')];
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    const target = entry.target.dataset.nav || '#' + entry.target.id;
    tabs.forEach((tab) => tab.classList.toggle('active', tab.getAttribute('href') === target));
  });
}, { threshold: 0.55 });
sections.forEach((section) => observer.observe(section));
