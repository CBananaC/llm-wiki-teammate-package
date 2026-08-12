/* ============================================================================
   第一部分「平台的整體介面」— 審閱工具互動複本的行為

   這個檔案只負責介紹網站內的教學複本。它不會讀取或寫入任何審閱狀態，
   也不會載入 review-tools 內的檔案；所有內容都來自 part-1-interface-data.js。

   四個可點區域：
     1 導覽列          兩個浮動標籤：輸入與輸出資料、切換介面區域
     2 時間與關係圖表  四條線各有一個固定圓點，點擊在 AI 分析區開啟對應輸出卡片
     3 原始史料區      示範 AI Skills 篩選標示
     4 AI 分析區       四個步驟：本機執行 → 候選卡片 → 加入圖表 → 引文定位
   ========================================================================== */

const PART1_CHAT_ICONS = {
  list: '<svg class="part1-chat-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="20" y2="6"/><line x1="8" y1="12" x2="20" y2="12"/><line x1="8" y1="18" x2="20" y2="18"/><line x1="3.5" y1="6" x2="3.51" y2="6"/><line x1="3.5" y1="12" x2="3.51" y2="12"/><line x1="3.5" y1="18" x2="3.51" y2="18"/></svg>',
  collapse: '<svg class="part1-chat-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>',
  jump: '<svg class="part1-chat-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 14 20 9 15 4"/><path d="M4 20v-7a4 4 0 0 1 4-4h12"/></svg>',
  move: '<svg class="part1-chat-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="5 9 2 12 5 15"/><polyline points="9 5 12 2 15 5"/><polyline points="15 19 12 22 9 19"/><polyline points="19 9 22 12 19 15"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="12" y1="2" x2="12" y2="22"/></svg>',
  close: '<svg class="part1-chat-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/></svg>',
  filter: '<svg class="part1-chat-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="21 4 3 4 10 12.5 10 19 14 21 14 12.5 21 4"/></svg>',
  gear: '<svg class="part1-chat-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09A1.65 1.65 0 0 0 15 4.6a1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09A1.65 1.65 0 0 0 19.4 15z"/></svg>'
};

const PART1_CHAT_EYE_ICON = '<svg class="part1-chat-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12z"/><circle cx="12" cy="12" r="2.5"/></svg>';

document.querySelectorAll('[data-part1]').forEach((root) => {
  'use strict';

  const data = window.PART1_INTERFACE_DATA;
  if (!data) return;

  const replica = root.querySelector('[data-part1-replica]');
  const mode = root.dataset.part1Mode || 'all';
  if (!replica) return;

  const escapeHtml = (value) => String(value == null ? '' : value)
    .replace(/[&<>"']/g, (char) => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[char]));

  /* ---------------------------------------------------------------- 原文 */

  /* 在原文中把每段引文包成 <mark>，供篩選標示與引文定位使用。
     引文由建置腳本確認過是原文的連續子字串，因此可直接以位置切分。 */
  const buildDocumentBody = (rangeStart = 0, rangeEnd = data.document.body.length) => {
    const body = data.document.body;
    const spans = [];
    const seen = new Set();
    const collect = (item) => {
      if (!item || !item.quote || item.quoteDocId !== data.document.docId) return;
      if (seen.has(item.quote)) return;
      const start = body.indexOf(item.quote);
      if (start < 0) return;
      seen.add(item.quote);
      spans.push({ start, end: start + item.quote.length, skill: item.aiFilterLabel, key: item.id });
    };
    collect(data.dots.events);
    data.aiCandidates.forEach(collect);

    spans.sort((a, b) => a.start - b.start);
    let html = '';
    let cursor = rangeStart;
    spans.forEach((span) => {
      if (span.end <= rangeStart || span.start >= rangeEnd || span.start < cursor) return;
      const start = Math.max(span.start, rangeStart);
      const end = Math.min(span.end, rangeEnd);
      if (start > cursor) html += escapeHtml(body.slice(cursor, start));
      html += `<mark data-skill="${escapeHtml(span.skill)}" data-source-chain="true" data-quote-key="${escapeHtml(span.key)}">`
        + `${escapeHtml(body.slice(start, end))}</mark>`;
      cursor = end;
    });
    html += escapeHtml(body.slice(cursor, rangeEnd));
    return html.replace(/\n/g, '<br>');
  };

  /* ------------------------------------------------------------ 版面組裝 */

  const doc = data.document;
  const docDivisionSpecs = [
    ['奏題開端', '飛飭各路'],
    ['軍情來源', '是彰化、諸羅俱已失陷'],
    ['兵力調度', '至官兵裏帶口糧'],
    ['結尾與硃批', '乾隆五十一年十二月十八日']
  ];
  const docDivisions = docDivisionSpecs.map(([label, marker], index) => {
    const start = index === 0 ? 0 : Math.max(0, doc.body.indexOf(docDivisionSpecs[index - 1][1]));
    const end = index === docDivisionSpecs.length - 1 ? doc.body.length : Math.max(start, doc.body.indexOf(marker));
    const text = doc.body.slice(start, end).trim();
    return { label, start, end, summary: text.split('。')[0] ? `${text.split('。')[0]}。` : '' };
  });
  const docSummary = doc.body.split('。').slice(0, 4).join('。') + '。';
  const authorLine = doc.author.name;
  const sourceLine = `明清台檔${doc.compiledIn.book}, ${doc.compiledIn.page}, ${doc.docId}`;
  const compactDate = (value) => String(value || '').replace(/^(\d{4})\/(\d{1,2})\/(\d{1,2})$/, (_, year, month, day) => `${year}/${Number(month)}/${Number(day)}`);
  const dateLine = `${compactDate(doc.sendDate[1])}-${compactDate(doc.receiveDate[1]).replace(/^\d{4}\//, '')}（15 日）`;

  /* 四條線的固定圓點。圓點的水平位置由 dateAr 計算，
     保持與真正樣本工具的橫向時間軸閱讀方式一致。 */
  const laneDots = [
    { lane: 'events', actor: 'lin', dot: data.dots.events, label: data.dots.events.whenCh },
    { lane: 'official', actor: 'official', dot: data.dots.official, label: '十二月十八日' },
    { lane: 'imperial', actor: 'imperial', dot: data.dots.imperial, label: '正月初二日' },
    { lane: 'emperor', actor: 'emperor', dot: data.dots.emperor, label: '正月初二日' }
  ];

  replica.dataset.part1Mode = mode;
  replica.innerHTML = `
    <div class="part1-region part1-toolbar" data-region="nav">
      <div class="part1-toolbar-start">
        <div class="part1-menu">
          <button class="part1-pill part1-pill-button" type="button" data-type-toggle><span class="part1-pl">點線類型</span><span aria-hidden="true">⌄</span></button>
          <div class="part1-menu-pop part1-type-pop" data-type-pop hidden>
            <strong>點線類型</strong>
            <label><input type="checkbox" checked> 戰場事件</label>
            <label><input type="checkbox" checked> 官員上奏</label>
            <label><input type="checkbox" checked> 皇帝硃批下旨</label>
            <label><input type="checkbox" checked> 皇帝行動</label>
          </div>
        </div>
        <div class="part1-people-control"><span class="part1-pl">人物</span><select aria-label="選擇人物"><option>— 選擇人物 —</option></select><button type="button" aria-label="新增人物">＋</button></div>
        <label class="part1-search"><span aria-hidden="true">⌕</span><input type="search" placeholder="搜尋原文 / 所有欄位…" aria-label="搜尋原文或所有欄位"></label>
      </div>
      <span class="part1-toolgroup" data-toolgroup="areas">
        <button class="part1-toolbtn" type="button" data-region-trigger="doc">Note</button>
        <button class="part1-toolbtn is-emphasis" type="button" data-region-trigger="ai">AI</button>
        <button class="part1-toolbtn" type="button" data-region-trigger="eventline">事件鏈</button>
      </span>
      <span class="part1-toolgroup" data-toolgroup="io">
        <button class="part1-toolbtn part1-gear-btn" type="button" data-tool-toggle="tools" aria-label="工具">${PART1_CHAT_ICONS.gear}</button>
        <div class="part1-menu-pop part1-tools-pop" data-tools-pop hidden>
          <div class="part1-tools-grid">
            <section class="part1-tools-section part1-tools-data">
              <h3>資料</h3>
              <div class="part1-tools-button-stack">
                <button type="button" data-tool-action="export">匯出</button>
                <button type="button" data-tool-action="export-split">分項匯出</button>
                <label class="part1-tools-file">匯入<input type="file" accept=".data,.json,application/json" data-import-file aria-label="匯入資料"></label>
                <button type="button" data-tool-action="load-skills">載入技能輸出</button>
                <input type="file" accept=".data,.json,application/json" data-skills-file aria-label="載入技能輸出檔" hidden>
              </div>
            </section>
            <section class="part1-tools-section part1-tools-type">
              <h3>字級</h3>
              <div class="part1-tools-setting"><span>介面字級</span><button type="button" data-tool-action="ui-smaller">A−</button><button type="button" data-tool-action="ui-larger">A＋</button></div>
              <div class="part1-tools-setting"><span>正文</span><button type="button" data-tool-action="body-smaller">A−</button><button type="button" data-tool-action="body-larger">A＋</button></div>
            </section>
            <section class="part1-tools-section part1-tools-wide">
              <h3>連線</h3>
              <label class="part1-tools-slider"><span>實線透明度</span><input type="range" min="0.05" max="1" step="0.01" value="0.32" data-tool-range aria-label="實線透明度"><output>32%</output></label>
              <label class="part1-tools-slider"><span>虛線透明度</span><input type="range" min="0.05" max="1" step="0.01" value="0.5" data-tool-range aria-label="虛線透明度"><output>50%</output></label>
            </section>
            <section class="part1-tools-section part1-tools-wide">
              <h3>時間軸</h3>
              <label class="part1-tools-slider"><span>圓點大小</span><input type="range" min="0.6" max="2.4" step="0.1" value="1" data-tool-range aria-label="圓點大小"><output>1×</output></label>
              <label class="part1-tools-slider"><span>圓點水平距離</span><input type="range" min="4" max="36" step="1" value="12" data-tool-range aria-label="圓點水平距離"><output>12 px</output></label>
              <label class="part1-tools-slider"><span>每日距離</span><input type="range" min="4" max="36" step="1" value="11" data-tool-range aria-label="每日距離"><output>11 px</output></label>
              <label class="part1-tools-slider"><span>四線距離</span><input type="range" min="1.5" max="2.8" step="0.05" value="1.5" data-tool-range aria-label="四線距離"><output>1.5×</output></label>
            </section>
          </div>
        </div>
      </span>
      <span class="part1-count">236/363</span>
    </div>

    <div class="part1-stage">
      <div class="part1-region part1-chart" data-region="chart">
        <div class="part1-chart-scroll" data-chart-scroll aria-label="可移動及縮放的四線時間與關係圖表">
          <div class="part1-chart-zoomspace" data-chart-zoomspace>
            <div class="part1-lanes" data-lanes>
              <svg class="part1-chart-links" data-chart-links role="img" aria-label="時間與關係圖表"></svg>
              <div class="part1-ruler-labels" data-chart-ruler aria-hidden="true"><span>1786/11</span><span>11</span><span>21</span><span>1786/12</span><span>11</span><span>21</span><span>1787/1</span><span>11</span></div>
            </div>
          </div>
        </div>
      </div>

      <section class="part1-region part1-eventline" data-region="eventline" aria-label="事件鏈">
        <div class="part1-eventline-head">
          <strong>事件鏈</strong>
          <div class="part1-eventline-controls">
            <button type="button" aria-label="移動事件鏈面板">${PART1_CHAT_ICONS.move}</button>
            <button type="button" aria-label="關閉事件鏈面板" data-eventline-close>${PART1_CHAT_ICONS.close}</button>
          </div>
        </div>
        <div class="part1-eventline-body" data-eventline-body></div>
      </section>

      <aside class="part1-dock">
        <div class="part1-region part1-ai part1-linked-panel part1-tool-box" data-region="ai">
          <div class="part1-linked-head tool-box-head">
            <span class="part1-chat-head-actions">
              <button class="part1-chat-icon-btn" type="button" data-ai-pop="toc" aria-expanded="false" aria-label="對話目錄"><span aria-hidden="true">${PART1_CHAT_ICONS.list}</span></button>
              <button class="part1-chat-icon-btn" type="button" aria-label="收合輸入面板"><span aria-hidden="true">${PART1_CHAT_ICONS.collapse}</span></button>
              <button class="part1-chat-icon-btn" type="button" aria-label="跳到最近的 AI 結果"><span aria-hidden="true">${PART1_CHAT_ICONS.jump}</span></button>
            </span>
            <span class="part1-chat-window-actions">
              <button class="part1-chat-icon-btn" type="button" aria-label="移動 AI 面板"><span aria-hidden="true">${PART1_CHAT_ICONS.move}</span></button>
              <button class="part1-chat-icon-btn" type="button" aria-label="關閉 AI 面板"><span aria-hidden="true">${PART1_CHAT_ICONS.close}</span></button>
            </span>
          </div>
          <div class="part1-ai-body tool-box-body" data-ai-body></div>
          <div class="part1-linked-foot"></div>
          <div class="part1-chat-window" aria-label="AI 對話輸入區"></div>
          <div class="part1-ai-popover part1-ai-toc" data-ai-popover="toc" hidden></div>
          <div class="part1-ai-popover part1-ai-actions" data-ai-popover="act" hidden></div>
          <div class="part1-ai-popover part1-ai-settings" data-ai-popover="cfg" hidden>
            <div class="part1-ai-settings-row">
              <label>AI 服務<select aria-label="AI 服務"><option>Gemini / Google Cloud</option><option>OpenAI GPT</option><option>ChatGPT via TokenRouter</option><option>Anthropic Claude</option><option>DeepSeek</option><option>第三方 API</option></select></label>
            </div>
            <div class="part1-ai-settings-row">
              <label>模型<input type="text" value="deepseek-v3.2-maas" aria-label="模型"></label>
            </div>
            <div class="part1-ai-settings-row">
              <label>API Base<input type="text" value="https://generativelanguage.googleapis.com/v1beta" aria-label="API Base"></label>
            </div>
            <div class="part1-ai-settings-row">
              <label>API Key
                <span class="part1-ai-input-with-action"><input type="password" placeholder="API key（只保留至此分頁關閉）" aria-label="API Key"><button type="button" class="part1-ai-key-toggle" data-ai-key-toggle aria-label="顯示或隱藏 API key">${PART1_CHAT_EYE_ICON}</button></span>
              </label>
            </div>
            <div class="part1-ai-settings-row part1-ai-memory-row">
              <label><input type="checkbox"> 記憶對話（跨訊息記住脈絡）</label>
            </div>
            <div class="part1-ai-settings-row">
              <label>代理網址<input type="text" value="http://127.0.0.1:8766/api/ai" aria-label="代理網址"></label>
            </div>
          </div>
        </div>

        <div class="part1-region part1-doc part1-ip" data-region="doc">
          <div class="part1-doc-head ip-head">
            <div class="part1-doc-window-controls">
              <button class="part1-doc-window-btn" type="button" aria-label="移動文書面板"><span aria-hidden="true">${PART1_CHAT_ICONS.move}</span></button>
              <button class="part1-doc-window-btn" type="button" aria-label="收合文書面板"><span aria-hidden="true"><svg class="part1-chat-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"/></svg></span></button>
              <button class="part1-doc-window-btn" type="button" aria-label="關閉文書面板"><span aria-hidden="true">${PART1_CHAT_ICONS.close}</span></button>
            </div>
            <p class="part1-doc-title"><span class="badge">${escapeHtml(doc.docType.slice(0, 1))}</span>${escapeHtml(doc.title)}</p>
            <p class="part1-doc-meta">${escapeHtml(authorLine)}<br>${escapeHtml(dateLine)}<br>${escapeHtml(sourceLine)}</p>
          </div>
          <div class="part1-filterdock ip-filterdock" data-filterdock>
            <button class="part1-filterbtn part1-filter-trigger" type="button" data-filter-toggle aria-expanded="false" aria-controls="part1-filter-popover">
              <span class="part1-filter-icon" aria-hidden="true">${PART1_CHAT_ICONS.filter}</span>
            </button>
            <button class="part1-filter-gear" type="button" data-view-toggle aria-expanded="false" aria-label="顯示設定"><span aria-hidden="true">${PART1_CHAT_ICONS.gear}</span></button>
            <div class="part1-filter-popover" id="part1-filter-popover" data-filter-popover hidden>
              <div class="part1-filter-chipbar" data-filter-chipbar></div>
            </div>
            <div class="part1-view-popover" data-view-popover hidden>
              <label><input type="checkbox" data-view-summary> 顯示摘要</label>
              <label><input type="checkbox" data-view-divisions> 顯示分段</label>
            </div>
          </div>
          <div class="part1-doc-scroll ip-scroll" data-doc-scroll>
            <div class="part1-doc-summary" data-doc-summary hidden>
              <h3>摘要</h3>
              <p>${escapeHtml(docSummary)}</p>
            </div>
            <p class="part1-doc-section-label">原文</p>
            <div class="part1-doc-divisions" data-doc-divisions hidden>
              ${docDivisions.map((part, index) => `
                <article class="part1-doc-part">
                  <h3><span>${index + 1}.</span> ${escapeHtml(part.label)}</h3>
                  <p class="part1-doc-part-summary">${escapeHtml(part.summary)}</p>
                  <div class="part1-doc-part-body">${buildDocumentBody(part.start, part.end)}</div>
                </article>
              `).join('')}
            </div>
            <div class="part1-doc-body ip-body" data-doc-body>${buildDocumentBody()}</div>
          </div>
        </div>
      </aside>
    </div>
  `;

  const lanesEl = replica.querySelector('[data-lanes]');
  const chartScroll = replica.querySelector('[data-chart-scroll]');
  const chartZoomspace = replica.querySelector('[data-chart-zoomspace]');
  const chartRuler = replica.querySelector('[data-chart-ruler]');
  const linksSvg = replica.querySelector('[data-chart-links]');
  const docBody = replica.querySelector('[data-doc-body]');
  const docSummaryEl = replica.querySelector('[data-doc-summary]');
  const docDivisionsEl = replica.querySelector('[data-doc-divisions]');
  const docScroll = replica.querySelector('[data-doc-scroll]');
  const filterDock = replica.querySelector('[data-filterdock]');
  const filterTrigger = replica.querySelector('[data-filter-toggle]');
  const filterPopover = replica.querySelector('[data-filter-popover]');
  const filterChipbar = replica.querySelector('[data-filter-chipbar]');
  const viewToggle = replica.querySelector('[data-view-toggle]');
  const viewPopover = replica.querySelector('[data-view-popover]');
  const summaryToggle = replica.querySelector('[data-view-summary]');
  const divisionsToggle = replica.querySelector('[data-view-divisions]');
  const aiBody = replica.querySelector('[data-ai-body]');
  const eventLineBody = replica.querySelector('[data-eventline-body]');
  let renderedEventItems = [];
  let activeFilter = 'all';
  let showSummary = false;
  let showDivisions = false;

  // The explanatory progress strip belongs to the introduction layer, not the
  // tool recreation. Keep the existing action flow quiet after removing it.
  const setProgress = () => {};

  /* ------------------------------------------------------------ 圖表圓點 */

  const parseDate = (value) => {
    const match = String(value || '').match(/^(\d{4})[\/-](\d{1,2})[\/-](\d{1,2})$/);
    return match ? Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3])) : 0;
  };
  const chartPreview = data.chartPreview || {};
  const fallbackChartNodes = laneDots.map(({ lane, actor, dot, label }) => ({
    id: `${lane}-${dot.id || dot.docId || 'node'}`,
    lane,
    actor,
    dateAr: dot.dateAr,
    label,
    payload: dot
  }));
  const chartInputNodes = Array.isArray(chartPreview.nodes) && chartPreview.nodes.length
    ? chartPreview.nodes
    : fallbackChartNodes;
  const baseChartNodes = chartInputNodes.map((node, index) => {
    const payload = node.payload || node.dot || data.dots[node.lane] || {};
    return {
      ...node,
      id: String(node.id || payload.id || `${node.lane || 'node'}-${index}`),
      lane: node.lane || 'events',
      actor: node.actor || payload.actor || 'lin',
      dateAr: node.dateAr || payload.dateAr,
      label: node.label || payload.whenCh || payload.title || payload.subtitle || '',
      payload
    };
  });
  const chartDateValues = baseChartNodes.map((node) => parseDate(node.dateAr)).filter(Boolean);
  const fallbackStart = chartDateValues.length ? Math.min(...chartDateValues) : parseDate('1786/11/01');
  const fallbackEnd = chartDateValues.length ? Math.max(...chartDateValues) : parseDate('1787/02/01');
  const defaultChartStart = parseDate('1786/11/01');
  const defaultChartEnd = parseDate('1787/02/01');
  const chartStart = parseDate(chartPreview.startAr) || defaultChartStart || fallbackStart;
  const chartEnd = parseDate(chartPreview.endAr) || defaultChartEnd || (fallbackEnd > chartStart ? fallbackEnd : chartStart + 86400000);
  const CHART_BASE_WIDTH = 1080;
  const CHART_BASE_HEIGHT = 620;
  const REPLICA_SETTINGS_KEY = 'introWebsite.part1Replica.settings.v1';
  const REPLICA_DEFAULTS = Object.freeze({
    uiScale: 1,
    bodyScale: 1,
    solidOpacity: 0.32,
    dashedOpacity: 0.5,
    dotSize: 1,
    dotGap: 12,
    daySpacing: 11,
    laneSpacing: 1.5
  });
  const clamp = (value, min, max) => Math.max(min, Math.min(max, Number(value)));
  const roundTo = (value, places = 2) => {
    const factor = 10 ** places;
    return Math.round(Number(value) * factor) / factor;
  };
  const readReplicaSettings = () => {
    try {
      const stored = JSON.parse(localStorage.getItem(REPLICA_SETTINGS_KEY) || '{}');
      return { ...REPLICA_DEFAULTS, ...stored };
    } catch (error) {
      return { ...REPLICA_DEFAULTS };
    }
  };
  const storedReplicaSettings = readReplicaSettings();
  let uiScale = clamp(storedReplicaSettings.uiScale, 0.8, 2.2);
  let bodyScale = clamp(storedReplicaSettings.bodyScale, 0.8, 2.6);
  let solidOpacity = clamp(storedReplicaSettings.solidOpacity, 0.05, 1);
  let dashedOpacity = clamp(storedReplicaSettings.dashedOpacity, 0.05, 1);
  let dotSizeScale = clamp(storedReplicaSettings.dotSize, 0.6, 2.4);
  let dotGap = clamp(storedReplicaSettings.dotGap, 4, 36);
  let daySpacing = clamp(storedReplicaSettings.daySpacing, 4, 36);
  let laneSpacing = clamp(storedReplicaSettings.laneSpacing, 1.5, 2.8);
  let chartScale = 1;
  const chartLaneRatios = Object.freeze({
    events: 0.38,
    official: 0.46,
    imperial: 0.54,
    emperor: 0.66,
    ...(chartPreview.laneRatios || {})
  });
  const chartPlot = (chartWidth = lanesEl.clientWidth || CHART_BASE_WIDTH) => {
    const width = chartWidth;
    const left = Math.min(68, Math.max(48, width * 0.12));
    const right = Math.min(11, Math.max(8, width * 0.03));
    return { width, left, right, inner: Math.max(1, width - left - right) };
  };
  const chartLaneX = (lane, width = lanesEl.clientWidth) => {
    const plot = chartPlot(width || CHART_BASE_WIDTH);
    const baseRatio = chartLaneRatios[lane] ?? 0.5;
    const ratio = 0.5 + (baseRatio - 0.5) * (laneSpacing / REPLICA_DEFAULTS.laneSpacing);
    return plot.left + plot.inner * ratio;
  };

  const chartHeight = () => Math.max(360, Math.round(CHART_BASE_HEIGHT * (daySpacing / REPLICA_DEFAULTS.daySpacing)));

  const applyChartScale = () => {
    if (!lanesEl || !chartZoomspace) return;
    lanesEl.style.width = `${CHART_BASE_WIDTH}px`;
    lanesEl.style.height = `${chartHeight()}px`;
    lanesEl.style.transform = `scale(${chartScale})`;
    chartZoomspace.style.width = `${CHART_BASE_WIDTH * chartScale}px`;
    chartZoomspace.style.height = `${chartHeight() * chartScale}px`;
    syncChartRuler();
  };

  /* ------------------------------------------------------ 工具設定與資料 */

  const persistReplicaSettings = () => {
    try {
      localStorage.setItem(REPLICA_SETTINGS_KEY, JSON.stringify({
        uiScale: roundTo(uiScale, 2),
        bodyScale: roundTo(bodyScale, 2),
        solidOpacity: roundTo(solidOpacity, 2),
        dashedOpacity: roundTo(dashedOpacity, 2),
        dotSize: roundTo(dotSizeScale, 2),
        dotGap: roundTo(dotGap, 2),
        daySpacing: roundTo(daySpacing, 2),
        laneSpacing: roundTo(laneSpacing, 2)
      }));
    } catch (error) {
      // Private browsing and embedded previews can deny localStorage. The
      // controls still work for the current page in that case.
    }
  };

  const applyReplicaCssSettings = () => {
    replica.style.setProperty('--font-scale', String(uiScale));
    replica.style.setProperty('--body-font-scale', String(bodyScale));
  };

  const formatToolValue = (input, value) => {
    const label = input.getAttribute('aria-label') || '';
    if (label.includes('透明度')) return `${Math.round(value * 100)}%`;
    if (label.includes('大小') || label.includes('四線')) return `${roundTo(value, 2)}×`;
    return `${roundTo(value, 2)} px`;
  };

  const syncToolControls = () => {
    const values = {
      實線透明度: solidOpacity,
      虛線透明度: dashedOpacity,
      圓點大小: dotSizeScale,
      圓點水平距離: dotGap,
      每日距離: daySpacing,
      四線距離: laneSpacing
    };
    toolsPop?.querySelectorAll('[data-tool-range]').forEach((input) => {
      const label = input.getAttribute('aria-label') || '';
      const key = Object.keys(values).find((candidate) => label.includes(candidate));
      if (!key) return;
      input.value = String(values[key]);
      const output = input.parentElement?.querySelector('output');
      if (output) output.textContent = formatToolValue(input, values[key]);
    });
  };

  const serialiseChartNode = (node) => ({
    id: node.id,
    lane: node.lane,
    actor: node.actor,
    dateAr: node.dateAr,
    label: node.label,
    color: node.color,
    radius: node.radius,
    payload: node.payload
  });

  const getReplicaState = () => ({
    settings: {
      uiScale: roundTo(uiScale, 2),
      bodyScale: roundTo(bodyScale, 2),
      solidOpacity: roundTo(solidOpacity, 2),
      dashedOpacity: roundTo(dashedOpacity, 2),
      dotSize: roundTo(dotSizeScale, 2),
      dotGap: roundTo(dotGap, 2),
      daySpacing: roundTo(daySpacing, 2),
      laneSpacing: roundTo(laneSpacing, 2)
    },
    chartScale: roundTo(chartScale, 2),
    chartScroll: { left: chartScroll?.scrollLeft || 0, top: chartScroll?.scrollTop || 0 },
    activeFilter,
    showSummary,
    showDivisions,
    chartExtraNodes: chartExtraNodes.map(serialiseChartNode)
  });

  const downloadJson = (filename, value) => {
    const blob = new Blob([JSON.stringify(value, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = filename;
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 1500);
  };

  const exportReplica = () => {
    downloadJson('part1-replica.data', {
      format: 'intro-website-part1-replica',
      version: 1,
      exportedAt: new Date().toISOString(),
      document: { id: doc.docId, title: doc.title },
      state: getReplicaState()
    });
    setProgress('已匯出示範複本狀態。檔案只包含此複本的設定與已加入節點。');
  };

  const exportReplicaSplit = () => {
    const sourceItems = [data.dots.events, ...data.aiCandidates, ...chartExtraNodes.map((node) => node.payload)]
      .filter(Boolean);
    const withQuote = sourceItems.filter((item) => item.quote);
    downloadJson('part1-replica-split.data', {
      format: 'intro-website-part1-replica-split',
      version: 1,
      document: { id: doc.docId, title: doc.title },
      summary: [{ doc_id: doc.docId, title: doc.title, text: docSummary }],
      'division-parts': docDivisions.map((part) => ({ doc_id: doc.docId, ...part })),
      'lin-events': sourceItems.filter((item) => item.actor === 'lin'),
      'qing-events': sourceItems.filter((item) => item.actor === 'qing'),
      'emperor-events': [data.dots.emperor],
      'event-drafts': chartExtraNodes.map((node) => node.payload),
      'source-chain': withQuote.map((item) => ({ doc_id: item.quoteDocId, quote: item.quote, event_id: item.id })),
      'manual-edits': [{ kind: 'replica-settings', settings: getReplicaState().settings }],
      'chat-log': []
    });
    setProgress('已分項匯出示範複本資料；每個分項可獨立檢查其來源。');
  };

  const normalizeImportedNode = (node, index) => {
    if (!node || typeof node !== 'object') return null;
    const payload = node.payload || node;
    const dateAr = node.dateAr || payload.dateAr || payload.whenAr;
    if (!dateAr || !parseDate(dateAr)) return null;
    const lane = ['events', 'official', 'imperial', 'emperor'].includes(node.lane) ? node.lane : 'events';
    return {
      ...node,
      id: String(node.id || payload.id || `imported-${index}`),
      lane,
      actor: node.actor || payload.actor || (lane === 'emperor' ? 'emperor' : 'qing'),
      dateAr,
      label: node.label || payload.whenCh || payload.title || payload.subtitle || dateAr,
      payload,
      isNew: true
    };
  };

  const getImportedState = (imported) => {
    if (!imported || typeof imported !== 'object') return null;
    if (imported.state && typeof imported.state === 'object') return imported.state;
    if (imported.replicaState && typeof imported.replicaState === 'object') return imported.replicaState;
    const eventCandidates = imported.chartExtraNodes || imported.__events || imported.events || imported['event-drafts'];
    if (Array.isArray(eventCandidates)) return { ...imported, chartExtraNodes: eventCandidates };
    if (Array.isArray(imported['manual-edits'])) {
      const edit = imported['manual-edits'].find((item) => item?.kind === 'replica-settings');
      if (edit) return { ...imported, settings: edit.settings };
    }
    return null;
  };

  const applyImportedState = (imported) => {
    const state = getImportedState(imported);
    if (!state) throw new Error('這不是可供複本使用的資料檔。');
    const settings = state.settings || {};
    uiScale = clamp(settings.uiScale ?? uiScale, 0.8, 2.2);
    bodyScale = clamp(settings.bodyScale ?? bodyScale, 0.8, 2.6);
    solidOpacity = clamp(settings.solidOpacity ?? solidOpacity, 0.05, 1);
    dashedOpacity = clamp(settings.dashedOpacity ?? dashedOpacity, 0.05, 1);
    dotSizeScale = clamp(settings.dotSize ?? dotSizeScale, 0.6, 2.4);
    dotGap = clamp(settings.dotGap ?? dotGap, 4, 36);
    daySpacing = clamp(settings.daySpacing ?? daySpacing, 4, 36);
    laneSpacing = clamp(settings.laneSpacing ?? laneSpacing, 1.5, 2.8);
    chartExtraNodes.length = 0;
    const importedNodes = Array.isArray(state.chartExtraNodes) ? state.chartExtraNodes : [];
    importedNodes.forEach((node, index) => {
      const normalized = normalizeImportedNode(node, index);
      if (normalized) chartExtraNodes.push(normalized);
    });
    activeFilter = filterChoices.some((choice) => choice.key === state.activeFilter) ? state.activeFilter : 'all';
    showSummary = Boolean(state.showSummary);
    showDivisions = Boolean(state.showDivisions);
    chartScale = clamp(state.chartScale ?? chartScale, 0.5, 3);
    applyReplicaCssSettings();
    applyChartScale();
    renderFilterChips();
    renderDocView();
    drawLinks();
    chartScroll?.scrollTo({ left: Number(state.chartScroll?.left) || 0, top: Number(state.chartScroll?.top) || 0, behavior: 'auto' });
    syncToolControls();
    persistReplicaSettings();
    setProgress(`已匯入複本資料：${chartExtraNodes.length} 個新增圖表節點。`);
  };

  // Keep the date ruler aligned vertically with the chart while cancelling
  // only the horizontal scroll of the wider timeline canvas.
  const syncChartRuler = () => {
    if (!chartRuler || !chartScroll) return;
    chartRuler.style.transform = `translateX(${chartScroll.scrollLeft / chartScale}px)`;
  };

  const chartScrollOffset = () => {
    const scrollRect = chartScroll.getBoundingClientRect();
    const canvasRect = lanesEl.getBoundingClientRect();
    return {
      x: canvasRect.left - scrollRect.left + chartScroll.scrollLeft,
      y: canvasRect.top - scrollRect.top + chartScroll.scrollTop
    };
  };

  const zoomChartTo = (nextScale, clientX = null, clientY = null) => {
    if (!chartScroll) return;
    const newScale = Math.max(0.5, Math.min(3, nextScale));
    if (Math.abs(newScale - chartScale) < 0.001) return;
    const rect = chartScroll.getBoundingClientRect();
    const px = clientX == null ? rect.width / 2 : clientX;
    const py = clientY == null ? rect.height / 2 : clientY;
    const before = chartScrollOffset();
    const chartX = (chartScroll.scrollLeft + px - before.x) / chartScale;
    const chartY = (chartScroll.scrollTop + py - before.y) / chartScale;
    chartScale = newScale;
    applyChartScale();
    const after = chartScrollOffset();
    chartScroll.scrollLeft = after.x + chartX * chartScale - px;
    chartScroll.scrollTop = after.y + chartY * chartScale - py;
  };

  applyChartScale();

  if (chartScroll) {
    // Match the sample tool: plain two-finger trackpad movement remains native
    // scrolling, while macOS pinch emits a meta/ctrl wheel event that zooms
    // around the pointer instead of jumping the whole chart.
    chartScroll.addEventListener('wheel', (event) => {
      if (!(event.ctrlKey || event.metaKey)) return;
      event.preventDefault();
      const rect = chartScroll.getBoundingClientRect();
      const factor = Math.exp(-event.deltaY * 0.01);
      zoomChartTo(chartScale * factor, event.clientX - rect.left, event.clientY - rect.top);
    }, { passive: false });

    // Click-drag panning is useful when the chart has been enlarged and also
    // mirrors the sample's mouse fallback for the same scroll viewport.
    let panning = false;
    let panX = 0;
    let panY = 0;
    let panScrollLeft = 0;
    let panScrollTop = 0;
    chartScroll.addEventListener('mousedown', (event) => {
      if (event.button !== 0) return;
      const target = event.target;
      if (target instanceof Element && target.closest('[data-chart-node-id]')) return;
      panning = true;
      panX = event.clientX;
      panY = event.clientY;
      panScrollLeft = chartScroll.scrollLeft;
      panScrollTop = chartScroll.scrollTop;
      chartScroll.classList.add('is-panning');
    });
    window.addEventListener('mousemove', (event) => {
      if (!panning) return;
      chartScroll.scrollLeft = panScrollLeft - (event.clientX - panX);
      chartScroll.scrollTop = panScrollTop - (event.clientY - panY);
    });
    window.addEventListener('mouseup', () => {
      panning = false;
      chartScroll.classList.remove('is-panning');
    });
    chartScroll.addEventListener('scroll', () => {
      syncChartRuler();
    }, { passive: true });
  }

  const eventOffsetLabel = (dateAr) => {
    const start = parseDate(doc.sendDate[1]);
    const date = parseDate(dateAr);
    if (!start || !date) return '';
    const days = Math.round((date - start) / 86400000);
    if (days === 0) return '同日';
    return `${Math.abs(days)}日${days < 0 ? '前' : '後'}`;
  };

  const eventLineCard = ({ title, meta, color, description, quote, selected = false }) => `
    <article class="part1-eventline-card${selected ? ' is-selected' : ''}" style="--eventline-color:${color}">
      <div class="part1-eventline-card-row">
        <span class="part1-eventline-dot" aria-hidden="true"></span>
        <div class="part1-eventline-main">
          <strong>${escapeHtml(title)}</strong>
          <div class="part1-eventline-meta">${escapeHtml(meta)}</div>
        </div>
        <span class="part1-eventline-caret" aria-hidden="true">▾</span>
      </div>
      <div class="part1-eventline-detail">
        ${description ? `<p>${escapeHtml(description)}</p>` : ''}
        ${quote ? `<blockquote>「${escapeHtml(quote)}」</blockquote>` : ''}
      </div>
    </article>`;

  const renderEventLine = () => {
    if (!eventLineBody) return;
    const officialMeta = `${authorLine}　${doc.sendDate[1]}`;
    const eventItems = [data.dots.events, ...data.aiCandidates];
    const actorLabel = (item) => item.actor === 'lin' ? '林方行動' : '清方行動';
    const actorColor = (item) => item.actor === 'lin' ? '#c4482f' : '#3f789c';
    const eventCards = eventItems.map((item) => eventLineCard({
      title: item.subtitle,
      meta: `${actorLabel(item)}　${item.dateAr}（${eventOffsetLabel(item.dateAr)}）`,
      color: actorColor(item),
      description: item.description,
      quote: item.quote
    })).join('');
    const emperor = data.dots.emperor;
    eventLineBody.innerHTML = `
      <div class="part1-eventline-seclabel">官方文書・硃批</div>
      ${eventLineCard({
        title: doc.title,
        meta: officialMeta,
        color: '#c46a2b',
        description: docSummary,
        quote: doc.rescriptText,
        selected: true
      })}
      <div class="part1-eventline-arrow"><span class="part1-eventline-arrow-line"></span><span class="part1-eventline-arrow-head">▼</span><strong>報告之事件</strong></div>
      ${eventCards}
      <div class="part1-eventline-arrow"><span class="part1-eventline-arrow-line"></span><span class="part1-eventline-arrow-head">▼</span><strong>皇帝批覆與行動</strong></div>
      ${eventLineCard({
        title: emperor.subtitle,
        meta: `相關上諭　${emperor.dateAr}（${eventOffsetLabel(emperor.dateAr)}）`,
        color: '#7d4ab8',
        description: emperor.description,
        quote: emperor.quote
      })}`;
    eventLineBody.querySelectorAll('.part1-eventline-card').forEach((card) => {
      card.addEventListener('click', () => {
        const open = card.classList.toggle('is-open');
        card.querySelector('.part1-eventline-caret').textContent = open ? '▴' : '▾';
      });
    });
  };

  const chartExtraNodes = [];
  const chartNodeElements = new Map();
  let selectedChartNodeId = '';

  const nodeColor = (node) => {
    if (node.color) return node.color;
    if (node.actor === 'lin') return '#b5462e';
    if (node.actor === 'qing') return '#3f6f8f';
    if (node.actor === 'emperor') return '#7d4ab8';
    if (node.lane === 'imperial') return '#c46a2b';
    if (node.lane === 'official') return '#2f75b5';
    return '#8a765a';
  };

  const drawLinks = () => {
    if (!linksSvg) return;
    const width = lanesEl.clientWidth || CHART_BASE_WIDTH;
    const height = lanesEl.clientHeight || CHART_BASE_HEIGHT;
    if (!width || !height) return;
    linksSvg.setAttribute('viewBox', `0 0 ${width} ${height}`);
    linksSvg.setAttribute('preserveAspectRatio', 'none');
    linksSvg.innerHTML = '';
    chartNodeElements.clear();

    const NS = 'http://www.w3.org/2000/svg';
    const plot = chartPlot(width);
    const daySpan = chartEnd - chartStart || 1;
    const yFor = (dateAr) => {
      const date = parseDate(dateAr);
      return Math.max(6, Math.min(height - 6, ((date - chartStart) / daySpan) * height));
    };
    const xFor = (lane, offset = 0) => chartLaneX(lane, width) + offset;
    const makeSvg = (tag, attributes, className) => {
      const element = document.createElementNS(NS, tag);
      if (className) element.setAttribute('class', className);
      Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, String(value)));
      linksSvg.appendChild(element);
      return element;
    };
    // Four fixed vertical axes and the same light month/day grid rhythm as the sample.
    ['events', 'official', 'imperial', 'emperor'].forEach((lane) => {
      const x = xFor(lane);
      makeSvg('line', { x1: x.toFixed(1), y1: 0, x2: x.toFixed(1), y2: height, opacity: solidOpacity }, 'part1-preview-axis');
    });
    const gridDate = new Date(chartStart);
    for (let i = 0; i < 130 && gridDate.getTime() <= chartEnd; i += 1) {
      const day = gridDate.getUTCDate();
      if (day === 1 || day === 11 || day === 21) {
        const dateAr = `${gridDate.getUTCFullYear()}/${String(gridDate.getUTCMonth() + 1).padStart(2, '0')}/${String(day).padStart(2, '0')}`;
        const y = yFor(dateAr);
        makeSvg('line', { x1: plot.left, y1: y.toFixed(1), x2: width - plot.right, y2: y.toFixed(1), opacity: dashedOpacity }, day === 1 ? 'part1-preview-month-grid' : 'part1-preview-grid');
      }
      gridDate.setUTCDate(gridDate.getUTCDate() + 1);
    }

    // Keep one readable, source-backed chain in the replica. The preview model
    // supplies the four teaching nodes; these three segments show how the
    // selected event moves through the official, imperial, and emperor lanes.
    const nodes = [...baseChartNodes, ...chartExtraNodes];
    const points = new Map();
    const pointsByLane = new Map();
    const nodesByLane = new Map();
    nodes.forEach((node) => {
      if (!nodesByLane.has(node.lane)) nodesByLane.set(node.lane, []);
      nodesByLane.get(node.lane).push(node);
    });
    nodes.forEach((node) => {
      if (!node.dateAr || !parseDate(node.dateAr)) return;
      const laneNodes = nodesByLane.get(node.lane) || [];
      const nodeIndex = laneNodes.indexOf(node);
      const horizontalOffset = (nodeIndex - (laneNodes.length - 1) / 2) * dotGap;
      const point = { x: xFor(node.lane, horizontalOffset), y: yFor(node.dateAr), node };
      points.set(node.id, point);
      if (!pointsByLane.has(node.lane)) pointsByLane.set(node.lane, point);
    });
    const defaultLinks = [
      { from: 'events', to: 'official', color: '#b5462e' },
      { from: 'official', to: 'imperial', color: '#c46a2b' },
      { from: 'imperial', to: 'emperor', color: '#7d4ab8' }
    ];
    const linkSpecs = Array.isArray(chartPreview.links) && chartPreview.links.length
      ? chartPreview.links
      : defaultLinks;
    const resolvePoint = (key) => points.get(String(key)) || pointsByLane.get(String(key));
    linkSpecs.forEach((link, index) => {
      const from = resolvePoint(link.from || link.source);
      const to = resolvePoint(link.to || link.target);
      if (!from || !to) return;
      makeSvg('line', {
        x1: from.x.toFixed(1), y1: from.y.toFixed(1),
        x2: to.x.toFixed(1), y2: to.y.toFixed(1),
        stroke: link.color || '#c46a2b',
        'stroke-width': link.width || 1.8,
        'stroke-linecap': 'round',
        opacity: solidOpacity
      }, link.className || `part1-preview-link part1-preview-link-${index}`);
    });

    nodes.forEach((node) => {
      const point = points.get(node.id);
      if (!point) return;
      const label = `${node.payload.subtitle || node.payload.title || '圖表節點'}（${node.label || node.dateAr}）`;
      const circle = makeSvg('circle', {
        cx: point.x.toFixed(1),
        cy: point.y.toFixed(1),
        r: (node.radius || 6.5) * dotSizeScale,
        fill: nodeColor(node),
        stroke: '#fffaf2',
        'stroke-width': 2,
        tabindex: 0,
        role: 'button',
        'aria-label': label,
        'data-chart-node-id': node.id
      }, `part1-dot part1-svg-dot${selectedChartNodeId === node.id ? ' is-selected' : ''}`);
      circle.dataset.actor = node.actor;
      circle._part1 = node;
      circle.addEventListener('click', () => selectDot(circle));
      circle.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          selectDot(circle);
        }
      });
      const title = document.createElementNS(NS, 'title');
      title.textContent = label;
      circle.appendChild(title);
      chartNodeElements.set(node.id, circle);
    });

  };

  /* ------------------------------------------------ 節點 → AI 輸出卡片 */

  const aiChatSources = Array.isArray(data.aiChatSources) ? data.aiChatSources : [];
  const chatKindLabel = (kind) => ({
    extract: '事件抽取',
    edictmatch: '上諭分析',
    officialresponse: '官員回應',
    emperor_action: '皇帝行動',
    output: 'AI 輸出'
  }[kind] || kind || 'AI 輸出');
  const chatSourceByEventId = (eventId) => {
    if (!eventId) return null;
    for (const source of aiChatSources) {
      for (const turn of source.turns || []) {
        for (const item of turn.outputItems || []) {
          if ((item.eventIds || []).includes(eventId)) return { source, turn, item };
        }
      }
    }
    return null;
  };
  const sourceRoleLabel = (source) => source?.role === 'event_source' ? '事件圓點來源' : source?.role === 'emperor_action_source' ? '皇帝行動圓點來源' : 'AI 輸出來源';
  const chatItemMarkup = (item, compact = false) => `
    <article class="part1-chat-output-item${compact ? ' is-compact' : ''}"${item.eventIds?.length ? ` data-chat-event-id="${escapeHtml(item.eventIds[0])}"` : ''}>
      <div class="part1-chat-output-head"><span>${escapeHtml(chatKindLabel(item.kind))}</span><span>${escapeHtml(item.sourceDocId || '')}</span></div>
      <p class="part1-chat-output-title">${escapeHtml(item.title)}</p>
      ${item.description ? `<p class="part1-chat-output-desc">${escapeHtml(item.description)}</p>` : ''}
      ${(item.where || item.who?.length || item.whenCh || item.whenAr) ? `<p class="part1-chat-output-meta">${escapeHtml([item.whenCh || item.whenAr, item.where, item.who?.length ? item.who.join('、') : ''].filter(Boolean).join('　'))}</p>` : ''}
      ${item.quote ? `<button class="part1-quote part1-chat-output-quote" type="button" data-quote="${escapeHtml(item.quote)}" data-quote-doc="${escapeHtml(item.sourceDocId || '')}">「${escapeHtml(item.quote)}」<span class="part1-quote-src">—${escapeHtml(item.sourceDocId || '')}／AI 輸出引文　點按定位</span></button>` : ''}
      ${item.eventIds?.length ? `<p class="part1-chat-output-link">形成圖表圓點：${escapeHtml(item.eventIds.join('、'))}</p>` : ''}
    </article>`;
  const chatSourceButton = (source) => `<button class="part1-chat-source-btn" type="button" data-chat-source-doc="${escapeHtml(source.docId)}">載入 ${escapeHtml(source.aiOutputPath || `${source.docId}.chat`)}（${escapeHtml(source.outputItemCount)} 項輸出）</button>`;
  const chatSourceLauncher = () => aiChatSources.length ? `
    <section class="part1-chat-source-box">
      <div class="part1-chat-source-head"><strong>目前 sample 的 AI 對話輸出</strong><span>已保存</span></div>
      <p>這些是形成示範圓點的原始 AI 輸出：${aiChatSources.map((source) => `${escapeHtml(source.docId)} → ${escapeHtml(source.aiOutputPath)}`).join('；')}。</p>
      <div class="part1-chat-source-actions">${aiChatSources.map(chatSourceButton).join('')}</div>
    </section>` : '';
  const loadChatSource = (docId, focusEventId = '') => {
    const source = aiChatSources.find((item) => item.docId === docId);
    if (!source) return;
    aiBody.innerHTML = `
      <div class="part1-chat-source-view">
        <div class="part1-node-result-head"><strong>${escapeHtml(sourceRoleLabel(source))}</strong><span>${escapeHtml(source.docId)}.chat</span></div>
        <p class="part1-chat-source-summary">${escapeHtml(source.docId)} 的保存輸出共有 ${escapeHtml(source.turnCount)} 個對話回合、${escapeHtml(source.outputItemCount)} 項輸出；下列每項都保留其回合、技能組包與事件圓點對應。</p>
        ${(source.turns || []).map((turn) => `<details class="part1-chat-output-turn"${turn.outputItems?.some((item) => (item.eventIds || []).includes(focusEventId)) ? ' open' : ''}>
          <summary>第 ${escapeHtml(Number(turn.turnIndex) + 1)} 回　${escapeHtml(chatKindLabel(turn.kind))}　${escapeHtml(turn.outputItems?.length || 0)} 項</summary>
          <div class="part1-chat-output-turn-meta">${escapeHtml(turn.bundleName || '未標示技能組包')} ${turn.runId ? `／${escapeHtml(turn.runId)}` : ''}${turn.prompt ? `<br>提示：${escapeHtml(turn.prompt)}` : ''}</div>
          ${(turn.outputItems || []).map((item) => chatItemMarkup(item, false)).join('') || '<p class="part1-chat-output-empty">此回合沒有可顯示的輸出卡。</p>'}
        </details>`).join('')}
        <div class="part1-chat-source-actions">${chatSourceButton(source)}${chatSourceLauncher()}</div>
      </div>`;
    aiBody.querySelectorAll('[data-quote]').forEach((button) => button.addEventListener('click', () => locateQuote(button.dataset.quote, button.dataset.quoteDoc)));
    const focus = focusEventId && aiBody.querySelector(`[data-chat-event-id="${CSS.escape(focusEventId)}"]`);
    if (focus && typeof focus.scrollIntoView === 'function') focus.scrollIntoView({ block: 'center' });
    setRegion('ai', { silent: true });
    setProgress(`已載入 ${source.aiOutputPath || `${source.docId}.chat`}；這裡就是示範圓點所依據的保存 AI 輸出。`);
  };
  const matchedChatSourceMarkup = (match) => match ? `
    <section class="part1-chat-source-box is-matched">
      <div class="part1-chat-source-head"><strong>此圓點的 AI 對話輸出來源</strong><span>${escapeHtml(match.source.docId)}.chat</span></div>
      <p>此圓點由保存的 ${escapeHtml(match.source.docId)} AI 輸出形成；以下是對應回合中的原始結果卡。</p>
      ${chatItemMarkup(match.item, true)}
      <button class="part1-chat-source-btn" type="button" data-chat-source-doc="${escapeHtml(match.source.docId)}" data-chat-focus-event="${escapeHtml(match.item.eventIds?.[0] || '')}">載入完整 ${escapeHtml(match.source.aiOutputPath || `${match.source.docId}.chat`)}</button>
    </section>` : chatSourceLauncher();

  const renderNodePanel = (payload, laneKey, label) => {
    const laneLabels = {
      events: '戰場事件',
      official: '官員上奏',
      imperial: '皇帝硃批下旨',
      emperor: '皇帝行動'
    };
    const laneLabel = laneLabels[laneKey] || '圖表節點';
    const title = payload.subtitle || payload.title || '未命名結果';
    const quote = payload.quote || (laneKey === 'imperial' ? payload.rescriptText : '');
    const quoteDocId = payload.quoteDocId || payload.docId || doc.docId;
    const matchedChat = chatSourceByEventId(payload.id);
    const factRows = [
      ['時間', payload.whenCh || label || payload.dateAr],
      ['地點', payload.where],
      ['人物', payload.who?.length ? payload.who.join('、') : ''],
    ].filter(([, value]) => value);
    const facts = factRows.map(([term, value]) => `<dt>${escapeHtml(term)}</dt><dd>${escapeHtml(value)}</dd>`).join('');
    const quoteCard = quote ? `
      <div class="part1-event-source">
        <div class="part1-event-source-head"><span>來源引文</span><span class="part1-event-source-role">${escapeHtml(laneKey === 'emperor' ? '相關上諭' : laneKey === 'events' ? '林方報告' : '硃批原文')}</span></div>
        <button class="part1-quote part1-event-quote" type="button" data-quote="${escapeHtml(quote)}" data-quote-doc="${escapeHtml(quoteDocId)}">
          「${escapeHtml(quote)}」
          <span class="part1-quote-src">—${escapeHtml(quoteDocId)}／原文　點按定位</span>
        </button>
      </div>` : '';

    let cardMarkup;
    if (laneKey === 'events' || laneKey === 'emperor') {
      const isLin = laneKey === 'events';
      const outputLabel = isLin ? '林方事件' : '皇帝行動';
      const skillLabel = payload.aiFilterLabel || (isLin ? '林方行動' : '相關上諭');
      cardMarkup = `
        <section class="part1-event-group ${isLin ? 'is-lin' : 'is-qing'}">
          <div class="part1-event-group-head"><span>${escapeHtml(outputLabel)}</span><span>1 項</span></div>
          <article class="part1-card part1-event-card ${isLin ? 'is-lin' : 'is-qing'} is-confirmed part1-node-output-card">
            <div class="part1-card-head">
              <span>AI ${escapeHtml(outputLabel)}</span>
              <span class="part1-card-skill">${escapeHtml(skillLabel)}</span>
            </div>
            <p class="part1-card-title">${escapeHtml(title)}</p>
            ${payload.description ? `<p class="part1-card-desc">${escapeHtml(payload.description)}</p>` : ''}
            ${facts ? `<dl class="part1-event-facts">${facts}</dl>` : ''}
            ${quoteCard}
            <p class="part1-card-status">由圖表節點開啟；點擊來源引文可回到原始史料區核對。</p>
          </article>
        </section>`;
    } else {
      const isImperial = laneKey === 'imperial';
      const outputLabel = isImperial ? '硃批' : '官員上奏';
      const skillLabel = isImperial ? '硃批' : '官文優先審閱迴圈';
      const documentFacts = [
        ['文書', `${payload.docId || doc.docId}　${payload.title || doc.title}`],
        ['作者', authorLine],
        ['日期', payload.whenCh || label || payload.dateAr]
      ].map(([term, value]) => `<dt>${escapeHtml(term)}</dt><dd>${escapeHtml(value)}</dd>`).join('');
      cardMarkup = `
        <article class="part1-card part1-node-document-card ${isImperial ? 'is-imperial' : 'is-official'}">
          <div class="part1-card-head">
            <span>AI ${escapeHtml(outputLabel)}</span>
            <span class="part1-card-skill">${escapeHtml(skillLabel)}</span>
          </div>
          <p class="part1-card-title">${escapeHtml(payload.title || doc.title)}</p>
          <p class="part1-card-desc">${escapeHtml(isImperial ? '皇帝硃批回應此份奏摺，形成後續上諭與行動的依據。' : docSummary)}</p>
          <dl class="part1-event-facts">${documentFacts}</dl>
          ${quoteCard}
          <p class="part1-card-status">由圖表節點開啟；此卡保留文書與批覆的來源脈絡。</p>
        </article>`;
    }

    aiBody.innerHTML = `
      <div class="part1-node-result" data-node-result>
        <div class="part1-node-result-head"><strong>節點資訊區</strong><span>${escapeHtml(laneLabel)}</span></div>
        ${cardMarkup}
        ${matchedChatSourceMarkup(matchedChat)}
      </div>`;
    aiBody.scrollTop = 0;
    aiBody.querySelectorAll('[data-quote]').forEach((button) => {
      button.addEventListener('click', () => locateQuote(button.dataset.quote, button.dataset.quoteDoc));
    });
  };

  const selectDot = (button) => {
    const node = button?._part1;
    if (!node) return;
    selectedChartNodeId = node.id;
    chartNodeElements.forEach((element) => element.classList.toggle('is-selected', element === button));
    renderNodePanel(node.payload, node.lane, node.label);
    setRegion('ai', { silent: true });
    const laneLabel = data.lanes.find((item) => item.key === node.lane)?.label || '節點';
    setProgress(`已在 AI 分析區開啟「${node.payload.subtitle || node.payload.title}」的${laneLabel}輸出卡片。`);
  };

  /* -------------------------------------------------------- 引文定位 */

  const locateQuote = (quote, quoteDocId) => {
    if (quoteDocId && quoteDocId !== doc.docId) {
      setProgress(`此引文出自 ${quoteDocId}，不在目前開啟的 ${doc.docId} 原文之內。在真正的工具中，平台會另外開啟 ${quoteDocId} 的文書面板。`);
      return;
    }
    const marks = [...replica.querySelectorAll('.part1-doc mark')];
    const target = marks.find((mark) => mark.textContent === quote);
    marks.forEach((mark) => mark.classList.remove('is-located'));
    if (!target) {
      setProgress('這段引文沒有對應的標示範圍。');
      return;
    }
    target.classList.add('is-located');
    const scrollRect = docScroll.getBoundingClientRect();
    const markRect = target.getBoundingClientRect();
    docScroll.scrollTop += markRect.top - scrollRect.top - scrollRect.height / 2 + markRect.height / 2;
    setRegion('doc', { silent: true });
    setProgress('已在原始史料區標示該段引文。每一項 AI 結果都可以這樣回到原文核對。');
  };

  /* ------------------------------------------------------ 原始史料篩選 */

  const filterChoices = [
    { key: 'all', label: '全部', count: '', color: '' },
    { key: '林方行動', label: '林方行動', count: '1', color: '#e3a09a' },
    { key: '清軍事：已執行', label: '清軍事：待執行', count: '2', color: '#9ebbd4' },
    { key: 'source-chain', label: '來源鏈', count: '4', color: '#d2b98d' }
  ];

  const renderFilterChips = () => {
    if (!filterChipbar) return;
    filterChipbar.innerHTML = filterChoices.map((choice) => `
      <button class="part1-filter-chip${activeFilter === choice.key ? ' is-on' : ''}" type="button" data-filter-chip="${escapeHtml(choice.key)}">
        ${choice.color ? `<span class="part1-filter-chip-dot" style="background:${choice.color}"></span>` : ''}
        <span>${escapeHtml(choice.label)}</span>${choice.count ? `<b>${escapeHtml(choice.count)}</b>` : ''}
      </button>
    `).join('');
  };

  const renderDocView = () => {
    if (docSummaryEl) docSummaryEl.hidden = !showSummary;
    if (docDivisionsEl) docDivisionsEl.hidden = !showDivisions;
    if (docBody) docBody.hidden = showDivisions;
    if (summaryToggle) summaryToggle.checked = showSummary;
    if (divisionsToggle) divisionsToggle.checked = showDivisions;
  };

  const applyFilter = (value) => {
    activeFilter = value;
    renderFilterChips();
    replica.querySelectorAll('.part1-doc mark').forEach((mark) => {
      const show = value === 'all'
        || mark.dataset.skill === value
        || (value === 'source-chain' && mark.dataset.sourceChain === 'true');
      mark.classList.toggle('is-shown', show);
      mark.classList.remove('is-located');
    });
    setProgress(value === 'all'
      ? '已標示全部 AI Skills 的提取範圍。每個顏色代表一項 Skill。'
      : `已標示「${filterChoices.find((choice) => choice.key === value)?.label || value}」在原文中的提取範圍。`);
  };

  filterTrigger?.addEventListener('click', () => {
    const open = Boolean(filterPopover?.hidden);
    if (filterPopover) filterPopover.hidden = !open;
    filterTrigger.setAttribute('aria-expanded', String(open));
    filterTrigger.classList.toggle('is-open', open);
    if (open) renderFilterChips();
  });

  filterChipbar?.addEventListener('click', (event) => {
    const button = event.target.closest('[data-filter-chip]');
    if (!button) return;
    applyFilter(button.dataset.filterChip);
    setRegion('doc', { silent: true });
  });

  viewToggle?.addEventListener('click', () => {
    const open = Boolean(viewPopover?.hidden);
    if (viewPopover) viewPopover.hidden = !open;
    viewToggle.setAttribute('aria-expanded', String(open));
    viewToggle.classList.toggle('is-open', open);
  });

  summaryToggle?.addEventListener('change', () => {
    showSummary = summaryToggle.checked;
    renderDocView();
  });
  divisionsToggle?.addEventListener('change', () => {
    showDivisions = divisionsToggle.checked;
    renderDocView();
  });

  renderFilterChips();
  renderDocView();

  /* ---------------------------------------------------------- AI 分析區 */

  const TERMINAL_LINES = [
    '$ python3 "tool/scripts py/run_ai_loop.py" \\',
    '    --doc 硃42 --skill lin-events --skill qing-actions',
    '',
    '<span class="part1-term-dim">載入原始文本 …… stage1_original_text.json</span>',
    '<span class="part1-term-dim">執行 AI Skills …… 2 項</span>',
    '<span class="part1-term-ok">✓ 已輸出審閱包：review-bundles/</span>',
    '<span class="part1-term-dim">請在網站按「輸入資料」上載此審閱包。</span>'
  ];

  const AI_TOC_ROWS = [
    ['擷取林方行動（3）', '2026-07-25 05:38', 'zhu-december-rerun-g36'],
    ['擷取清方行動（7）', '2026-07-25 05:38', 'zhu-december-rerun-g36']
  ];

  const AI_ACTION_GROUPS = [
    ['官文優先審閱迴圈', '回應的先前上諭', '回應的先前上諭（無引文）', '上諭回應的奏折', '回應的先前硃批'],
    ['摘要', '分段'],
    ['林方事件', '林方來源', '全文來源鏈'],
    ['清方行動（三類合一）'],
    ['硃批', '上諭', '皇帝行動（奏／諭）', '硃批／上諭來源', '回應時效', '官員回應'],
    ['整合重複事件', '逐日／期間摘要'],
    ['管理提示']
  ];

  const aiPopovers = [...replica.querySelectorAll('[data-ai-popover]')];
  aiPopovers.forEach((popover) => document.body.appendChild(popover));
  const getAiPopover = (name) => aiPopovers.find((popover) => popover.dataset.aiPopover === name);

  const closeAiPopovers = () => {
    aiPopovers.forEach((popover) => {
      popover.hidden = true;
      popover.classList.remove('is-viewport');
      ['top', 'right', 'bottom', 'left', 'width', 'max-height'].forEach((property) => popover.style.removeProperty(property));
    });
    replica.querySelectorAll('[data-ai-pop]').forEach((button) => {
      button.setAttribute('aria-expanded', 'false');
      button.classList.remove('is-open');
    });
  };

  const renderAiToc = () => {
    const popover = getAiPopover('toc');
    if (!popover) return;
    popover.innerHTML = AI_TOC_ROWS.map(([title, time, bundle]) => `
      <button class="part1-ai-toc-item" type="button" data-ai-menu-item>
        <span class="part1-ai-toc-title">${escapeHtml(title)}</span>
        <span class="part1-ai-toc-meta">${escapeHtml(time)}</span>
        <span class="part1-ai-toc-meta">${escapeHtml(bundle)}</span>
      </button>`).join('');
    popover.querySelectorAll('[data-ai-menu-item]').forEach((item) => item.addEventListener('click', closeAiPopovers));
  };

  const renderAiActions = () => {
    const popover = getAiPopover('act');
    if (!popover) return;
    popover.innerHTML = AI_ACTION_GROUPS.map((group, groupIndex) => `
      ${groupIndex ? '<div class="part1-ai-menu-divider" role="separator"></div>' : ''}
      ${group.map((label) => `<button class="part1-ai-menu-item" type="button" data-ai-menu-item${label === '林方事件' || label === '清方行動（三類合一）' ? ' data-ai-action="load-cards"' : ''}>${escapeHtml(label)}</button>`).join('')}
    `).join('');
    popover.querySelectorAll('[data-ai-menu-item]').forEach((item) => item.addEventListener('click', () => {
      if (item.dataset.aiAction === 'load-cards') renderCandidates();
      closeAiPopovers();
    }));
  };

  const toggleAiPopover = (name) => {
    const popover = getAiPopover(name);
    if (!popover) return;
    const wasOpen = !popover.hidden;
    closeAiPopovers();
    if (wasOpen) return;
    if (name === 'toc') renderAiToc();
    if (name === 'act') renderAiActions();
    popover.hidden = false;
    const trigger = replica.querySelector(`[data-ai-pop="${name}"]`);
    trigger?.setAttribute('aria-expanded', 'true');
    trigger?.classList.add('is-open');

    const panel = replica.querySelector('.part1-ai')?.getBoundingClientRect();
    const triggerRect = trigger?.getBoundingClientRect();
    if (!panel || !triggerRect) return;
    popover.classList.add('is-viewport');
    popover.style.setProperty('left', `${Math.max(8, panel.left + 1)}px`, 'important');
    popover.style.setProperty('right', 'auto', 'important');
    popover.style.setProperty('bottom', 'auto', 'important');
    popover.style.setProperty('width', `${Math.max(160, panel.width - 2)}px`, 'important');
    popover.style.setProperty('max-height', 'calc(100vh - 16px)', 'important');
    const popoverHeight = popover.getBoundingClientRect().height;
    const targetTop = name === 'toc'
      ? triggerRect.bottom + 4
      : (replica.querySelector('.part1-linked-foot')?.getBoundingClientRect().top || triggerRect.top) - popoverHeight - 6;
    const top = Math.max(8, Math.min(targetTop, window.innerHeight - popoverHeight - 8));
    popover.style.setProperty('top', `${top}px`, 'important');
  };

  getAiPopover('cfg')?.querySelector('[data-ai-key-toggle]')?.addEventListener('click', (event) => {
    const keyToggle = event.currentTarget;
    const keyInput = keyToggle.parentElement?.querySelector('input');
    if (!keyInput) return;
    const visible = keyInput.type === 'text';
    keyInput.type = visible ? 'password' : 'text';
    keyToggle.setAttribute('aria-label', visible ? '顯示或隱藏 API key' : '隱藏 API key');
  });

  const renderAiIdle = () => {
    closeAiPopovers();
    aiBody.innerHTML = `
      <div class="part1-linked-source">據奏來源（上諭前 0 日收到）</div>
      <div class="part1-linked-doc">
        <p class="part1-linked-title">${escapeHtml(doc.title)}<br><span>徐嗣曾</span></p>
        <p class="part1-linked-date">${escapeHtml(doc.receiveDate[1])}</p>
        <blockquote><b>①</b>「${escapeHtml('提臣黃仕簡已於十五日由廈門出口放洋')}」</blockquote>
        <blockquote><b>②</b>「${escapeHtml('任承恩亦配兵登舟，合之郝壯猷所帶，計共兵六千人')}」</blockquote>
      </div>
      ${chatSourceLauncher()}
    `;
    const foot = replica.querySelector('.part1-linked-foot');
    if (foot) foot.innerHTML = `
      <button type="button">請點選文書</button>
      <button type="button" data-ai-pop="act" aria-expanded="false">功能⌄</button>
      <button class="part1-chat-settings" type="button" data-ai-pop="cfg" aria-expanded="false" aria-label="AI 設定"><span aria-hidden="true">${PART1_CHAT_ICONS.gear}</span></button>
    `;
  };

  let terminalTimer = 0;
  const runTerminal = () => {
    const pre = aiBody.querySelector('[data-terminal]');
    const button = aiBody.querySelector('[data-run-ai]');
    if (!pre) return;
    if (button) button.disabled = true;
    window.clearTimeout(terminalTimer);
    pre.innerHTML = '';
    setRegion('ai', { silent: true });
    setProgress('AI Skills 正在本機執行。平台本身不會呼叫外部模型，研究者完全掌握資料。');

    let index = 0;
    const step = () => {
      if (index >= TERMINAL_LINES.length) {
        highlightImportButton();
        return;
      }
      pre.innerHTML += `${TERMINAL_LINES[index]}\n`;
      index += 1;
      terminalTimer = window.setTimeout(step, 340);
    };
    step();
  };

  const highlightImportButton = () => {
    const ioGroup = replica.querySelector('[data-toolgroup="io"]');
    ioGroup?.classList.add('is-pointed');
    setProgress('本機執行完成。研究者接著按導覽列的「輸入資料」，把審閱包上載到平台。');
    aiBody.insertAdjacentHTML('beforeend',
      '<div class="part1-step"><span class="part1-step-num">2</span>按導覽列的「輸入資料」上載審閱包，AI 結果會以卡片形式顯示。</div>'
      + '<button class="part1-act" type="button" data-load-cards>上載審閱包</button>');
    aiBody.querySelector('[data-load-cards]')?.addEventListener('click', renderCandidates);
  };

  const renderCandidates = () => {
    renderedEventItems = [
      { ...data.dots.events, __confirmed: true, resultLabel: '林方事件', sourceRole: '林方報告' },
      ...data.aiCandidates.map((item) => ({ ...item, resultLabel: '清方行動', sourceRole: '清方軍事行動' }))
    ];

    const actorLabel = (actor) => actor === 'lin' ? '林方事件' : '清方行動';
    const actorClass = (actor) => actor === 'lin' ? 'is-lin' : 'is-qing';
    const sourceDate = (item) => item.quoteDocId === doc.docId ? doc.sendDate[1] : '';
    const sourceTitle = (item) => item.quoteDocId === doc.docId
      ? `${doc.title}（${doc.docId}）`
      : String(item.quoteDocId || '來源文書');
    const sourceChain = (item, index) => `
      <div class="part1-source-chain" data-source-chain="${index}"${item.__confirmed ? '' : ' hidden'}>
        <div class="part1-source-chain-head">
          <span class="part1-source-chain-label">來源鏈 1</span>
          <span class="part1-source-chain-status">直接奏報</span>
        </div>
        <div class="part1-source-hop">
          <span class="part1-source-node">${escapeHtml(sourceTitle(item))}</span>
          <span class="part1-source-arrow" aria-hidden="true">→</span>
          <span class="part1-source-node">${escapeHtml(actorLabel(item.actor))}</span>
        </div>
        <div class="part1-source-chain-events">
          <span>此來源鏈所報事件</span>
          <button class="part1-source-event" type="button" data-quote="${escapeHtml(item.quote)}" data-quote-doc="${escapeHtml(item.quoteDocId)}">
            ${escapeHtml(item.subtitle)}
          </button>
        </div>
      </div>`;
    const renderEventCard = (item, index) => {
      const confirmed = Boolean(item.__confirmed);
      const sendDate = sourceDate(item);
      return `
        <article class="part1-card part1-event-card ${actorClass(item.actor)}${confirmed ? ' is-confirmed' : ''}" data-candidate="${index}">
          <div class="part1-card-head">
            <span>AI ${escapeHtml(actorLabel(item.actor))}</span>
            <span class="part1-card-skill">${escapeHtml(item.aiFilterLabel)}</span>
          </div>
          <p class="part1-card-title">${escapeHtml(item.subtitle)}</p>
          <p class="part1-card-desc">${escapeHtml(item.description)}</p>
          <dl class="part1-event-facts">
            <dt>地點</dt><dd>${escapeHtml(item.where || '？')}</dd>
            ${item.who?.length ? `<dt>人物</dt><dd>${escapeHtml(item.who.join('、'))}</dd>` : ''}
            <dt>發生日期</dt><dd>${escapeHtml(item.whenCh || '未明')}（${escapeHtml(item.dateAr || '未明')}）</dd>
          </dl>
          <div class="part1-event-source">
            <div class="part1-event-source-head">
              <span>來源引文</span>
              <span class="part1-event-source-role">${escapeHtml(item.sourceRole)}</span>
            </div>
            <button class="part1-quote part1-event-quote" type="button" data-quote="${escapeHtml(item.quote)}" data-quote-doc="${escapeHtml(item.quoteDocId)}">
              「${escapeHtml(item.quote)}」
              <span class="part1-quote-src">—${escapeHtml(item.quoteDocId)}／原文　點按定位</span>
            </button>
            <div class="part1-event-source-meta">${escapeHtml(sourceTitle(item))}${sendDate ? `　發送日 ${escapeHtml(sendDate)}` : ''}</div>
          </div>
          <div class="part1-card-acts">
            ${confirmed
              ? '<span class="part1-confirmed">✓ 已加入</span>'
              : `<button class="part1-act" type="button" data-add="${index}">加入圖表</button>
                 ${sendDate ? `<button class="part1-act part1-act-date" type="button" data-use-date="${index}">用文書發送日 ${escapeHtml(sendDate)}</button>` : ''}
                 <button class="part1-act part1-act-skip" type="button" data-skip="${index}">略過</button>`}
          </div>
          <p class="part1-card-status" data-status="${index}">${confirmed ? '此林方事件已在圖表上；以下保留其來源鏈供核對。' : ''}</p>
          ${sourceChain(item, index)}
        </article>`;
    };

    const groups = ['lin', 'qing'].map((actor) => {
      const items = renderedEventItems.map((item, index) => ({ item, index })).filter(({ item }) => item.actor === actor);
      if (!items.length) return '';
      return `<section class="part1-event-group ${actorClass(actor)}">
        <div class="part1-event-group-head"><span>${actor === 'lin' ? '林方事件' : '清方行動'}</span><span>${items.length} 項</span></div>
        ${items.map(({ item, index }) => renderEventCard(item, index)).join('')}
      </section>`;
    }).join('');

    aiBody.innerHTML = `
      <div class="part1-step"><span class="part1-step-num">3</span>AI 結果依照林方／清方事件分組。每張卡先顯示事件內容，再顯示可回到原文核對的來源引文；只有確認後才加入圖表。</div>
      ${groups}
    `;
    setProgress('AI 結果已載入。先點來源引文回原文核對，再確認是否加入圖表。');

    aiBody.querySelectorAll('[data-quote]').forEach((button) => {
      button.addEventListener('click', () => locateQuote(button.dataset.quote, button.dataset.quoteDoc));
    });
    aiBody.querySelectorAll('[data-add]').forEach((button) => {
      button.addEventListener('click', () => addCandidate(Number(button.dataset.add)));
    });
    aiBody.querySelectorAll('[data-skip]').forEach((button) => {
      button.addEventListener('click', () => {
        const index = Number(button.dataset.skip);
        const card = aiBody.querySelector(`[data-candidate="${index}"]`);
        card?.classList.add('is-skipped');
        card?.querySelectorAll('.part1-act').forEach((item) => { item.disabled = true; });
        const status = aiBody.querySelector(`[data-status="${index}"]`);
        if (status) status.textContent = '已略過：此項不會加入圖表。';
        setProgress('已略過該項結果。被略過的結果不會進入圖表，原始文書不受影響。');
      });
    });
    aiBody.querySelectorAll('[data-use-date]').forEach((button) => {
      button.addEventListener('click', () => {
        const index = Number(button.dataset.useDate);
        const item = renderedEventItems[index];
        const status = aiBody.querySelector(`[data-status="${index}"]`);
        if (status) status.textContent = `已套用來源文書發送日：${sourceDate(item)}。正式工具會以此日期補正事件位置。`;
        button.disabled = true;
        setProgress('已示範以來源文書發送日補正事件日期；正式工具會把修正後日期帶入圖表。');
      });
    });
  };

  const addedCandidates = new Set();
  const addCandidate = (index) => {
    if (addedCandidates.has(index)) return;
    const item = renderedEventItems[index];
    if (!item || item.__confirmed) return;
    addedCandidates.add(index);

    const card = aiBody.querySelector(`[data-candidate="${index}"]`);
    card?.classList.add('is-added');
    card?.querySelectorAll('.part1-act').forEach((button) => { button.disabled = true; });
    const status = aiBody.querySelector(`[data-status="${index}"]`);
    if (status) status.textContent = '已加入圖表：可在「戰場事件」線上點擊新圓點查看；來源鏈已保留在此卡片下方。';
    card?.querySelector('.part1-source-chain')?.removeAttribute('hidden');

    const chartNode = {
      id: String(item.id || `candidate-${index}`),
      lane: 'events',
      actor: item.actor === 'lin' ? 'lin' : 'qing',
      dateAr: item.dateAr,
      label: item.whenCh,
      payload: item,
      isNew: true
    };
    chartExtraNodes.push(chartNode);
    drawLinks();
    setRegion('chart', { silent: true });
    setProgress(`「${item.subtitle}」已加入戰場事件線。點擊新圓點，或在卡片下方查看其來源鏈。`);
    const button = chartNodeElements.get(chartNode.id);
    button?.classList.add('is-new');
    window.setTimeout(() => button?.classList.remove('is-new'), 700);
  };

  function setRegion(region, options = {}) {
    replica.dataset.eventlineOpen = region === 'eventline' ? 'true' : 'false';
    if (region === 'eventline') renderEventLine();
  }

  /* 導覽列的下拉選單是展示用互動，但保留真正樣本工具的控制層級：
     點線類型在左側，工具與介面區域切換在右側。 */
  const typePop = replica.querySelector('[data-type-pop]');
  const toolsPop = replica.querySelector('[data-tools-pop]');
  const importFile = replica.querySelector('[data-import-file]');
  const skillsFile = replica.querySelector('[data-skills-file]');
  applyReplicaCssSettings();
  syncToolControls();
  replica.querySelector('[data-type-toggle]')?.addEventListener('click', (event) => {
    event.stopPropagation();
    if (typePop) typePop.hidden = !typePop.hidden;
    if (toolsPop) toolsPop.hidden = true;
    setRegion('nav', { silent: true });
    setProgress('已開啟「點線類型」篩選。真正工具會依研究問題顯示或隱藏不同線型。');
  });
  replica.querySelector('[data-tool-toggle]')?.addEventListener('click', (event) => {
    event.stopPropagation();
    if (toolsPop) toolsPop.hidden = !toolsPop.hidden;
    if (typePop) typePop.hidden = true;
    setRegion('nav', { silent: true });
    setProgress('已開啟「工具」選單。輸入與輸出資料集中在這裡，字級也可由此調整。');
  });
  replica.querySelectorAll('[data-region-trigger]').forEach((button) => {
    button.addEventListener('click', () => setRegion(button.dataset.regionTrigger));
  });
  replica.querySelector('[data-eventline-close]')?.addEventListener('click', () => setRegion('chart'));
  toolsPop?.querySelectorAll('[data-tool-range]').forEach((input) => {
    input.addEventListener('input', () => {
      const value = Number(input.value);
      const label = input.getAttribute('aria-label') || '';
      if (label.includes('實線透明度')) solidOpacity = clamp(value, 0.05, 1);
      else if (label.includes('虛線透明度')) dashedOpacity = clamp(value, 0.05, 1);
      else if (label.includes('圓點大小')) dotSizeScale = clamp(value, 0.6, 2.4);
      else if (label.includes('圓點水平距離')) dotGap = clamp(value, 4, 36);
      else if (label.includes('每日距離')) daySpacing = clamp(value, 4, 36);
      else if (label.includes('四線距離')) laneSpacing = clamp(value, 1.5, 2.8);
      const output = input.parentElement?.querySelector('output');
      if (output) output.textContent = formatToolValue(input, value);
      persistReplicaSettings();
      if (label.includes('每日距離')) applyChartScale();
      drawLinks();
      setProgress(`已套用「${label}」：${formatToolValue(input, value)}。設定會保留在此教學複本。`);
    });
  });

  const changeFontScale = (kind, delta) => {
    if (kind === 'ui') uiScale = roundTo(clamp(uiScale + delta, 0.8, 2.2), 2);
    else bodyScale = roundTo(clamp(bodyScale + delta, 0.8, 2.6), 2);
    applyReplicaCssSettings();
    persistReplicaSettings();
    setProgress(`已調整${kind === 'ui' ? '介面字級' : '正文'}至 ${kind === 'ui' ? uiScale : bodyScale}×。`);
  };

  const toolActions = {
    export: exportReplica,
    'export-split': exportReplicaSplit,
    'ui-smaller': () => changeFontScale('ui', -0.1),
    'ui-larger': () => changeFontScale('ui', 0.1),
    'body-smaller': () => changeFontScale('body', -0.1),
    'body-larger': () => changeFontScale('body', 0.1),
    'load-skills': () => {
      setProgress('請選擇本機的 AI Skill 輸出或審閱包（.data / .json）。');
      skillsFile?.click();
    }
  };

  toolsPop?.querySelectorAll('button[data-tool-action]').forEach((button) => {
    button.addEventListener('click', (event) => {
      event.stopPropagation();
      const keepToolsOpen = ['ui-smaller', 'ui-larger', 'body-smaller', 'body-larger']
        .includes(button.dataset.toolAction);
      if (!keepToolsOpen) toolsPop.hidden = true;
      replica.querySelector('[data-toolgroup="io"]')?.classList.add('is-pointed');
      button.classList.add('is-pointed');
      toolActions[button.dataset.toolAction]?.();
    });
  });

  const readJsonFile = async (input, message) => {
    const file = input?.files?.[0];
    if (!file) return;
    try {
      const imported = JSON.parse(await file.text());
      applyImportedState(imported);
      if (message) setProgress(message);
    } catch (error) {
      setProgress(`載入失敗：${error.message || '資料檔格式無法辨識。'}`);
    } finally {
      input.value = '';
    }
  };

  importFile?.addEventListener('change', () => readJsonFile(importFile, '已匯入並套用複本設定；原始史料內容未被修改。'));
  skillsFile?.addEventListener('change', () => readJsonFile(skillsFile, '已載入 AI Skill 輸出；可點擊新增圓點檢查其資料。'));

  replica.addEventListener('click', (event) => {
    const panelClose = event.target.closest('[data-panel-close]');
    if (panelClose) {
      event.stopPropagation();
      setPanelOpen(panelClose.dataset.panelClose, false);
      return;
    }
    const chatSourceTrigger = event.target.closest('[data-chat-source-doc]');
    if (chatSourceTrigger) {
      event.stopPropagation();
      loadChatSource(chatSourceTrigger.dataset.chatSourceDoc, chatSourceTrigger.dataset.chatFocusEvent || '');
      return;
    }
    const keyToggle = event.target.closest('[data-ai-key-toggle]');
    if (keyToggle) {
      const keyInput = keyToggle.parentElement?.querySelector('input');
      if (keyInput) {
        const visible = keyInput.type === 'text';
        keyInput.type = visible ? 'password' : 'text';
        keyToggle.setAttribute('aria-label', visible ? '顯示或隱藏 API key' : '隱藏 API key');
      }
      return;
    }
    const aiTrigger = event.target.closest('[data-ai-pop]');
    if (aiTrigger) {
      event.stopPropagation();
      toggleAiPopover(aiTrigger.dataset.aiPop);
      return;
    }
    const aiMenuItem = event.target.closest('[data-ai-menu-item]');
    if (aiMenuItem) {
      if (aiMenuItem.dataset.aiAction === 'load-cards') renderCandidates();
      closeAiPopovers();
      return;
    }
    if (!event.target.closest('[data-ai-popover]')) closeAiPopovers();
    if (!event.target.closest('[data-type-toggle]') && !event.target.closest('[data-type-pop]')
      && !event.target.closest('[data-tool-toggle]') && !event.target.closest('[data-tools-pop]')) {
      if (typePop) typePop.hidden = true;
      if (toolsPop) toolsPop.hidden = true;
    }
  });

  /* -------------------------------------------------------------- 重設 */

  const reset = () => {
    window.clearTimeout(terminalTimer);
    addedCandidates.clear();
    renderedEventItems = [];
    chartExtraNodes.length = 0;
    selectedChartNodeId = '';
    replica.querySelectorAll('.part1-doc mark').forEach((mark) => {
      mark.classList.remove('is-shown', 'is-located');
    });
    activeFilter = 'all';
    showSummary = false;
    showDivisions = false;
    uiScale = REPLICA_DEFAULTS.uiScale;
    bodyScale = REPLICA_DEFAULTS.bodyScale;
    solidOpacity = REPLICA_DEFAULTS.solidOpacity;
    dashedOpacity = REPLICA_DEFAULTS.dashedOpacity;
    dotSizeScale = REPLICA_DEFAULTS.dotSize;
    dotGap = REPLICA_DEFAULTS.dotGap;
    daySpacing = REPLICA_DEFAULTS.daySpacing;
    laneSpacing = REPLICA_DEFAULTS.laneSpacing;
    try { localStorage.removeItem(REPLICA_SETTINGS_KEY); } catch (error) { /* current-page reset still applies */ }
    applyReplicaCssSettings();
    chartScale = 1;
    applyChartScale();
    chartScroll?.scrollTo({ left: 0, top: 0, behavior: 'auto' });
    if (filterPopover) filterPopover.hidden = true;
    if (viewPopover) viewPopover.hidden = true;
    filterTrigger?.classList.remove('is-open');
    viewToggle?.classList.remove('is-open');
    filterTrigger?.setAttribute('aria-expanded', 'false');
    viewToggle?.setAttribute('aria-expanded', 'false');
    renderFilterChips();
    renderDocView();
    syncToolControls();
    renderAiIdle();
    drawLinks();
    setProgress('已重設示範。點擊複本上任何一個編號標籤，重新開始。');
  };

  replica.querySelector('[data-part1-reset]')?.addEventListener('click', reset);

  /* -------------------------------------------------------------- 初始化 */

  renderAiIdle();
  drawLinks();

  const initialRegion = mode === 'node' ? 'chart' : mode === 'all' ? '' : mode;
  if (initialRegion) setRegion(initialRegion, { silent: true });
  if (mode === 'node') {
    const firstDot = chartNodeElements.values().next().value;
    if (firstDot) selectDot(firstDot);
  }

  window.addEventListener('resize', () => {
    drawLinks();
  });
  if ('ResizeObserver' in window) new ResizeObserver(drawLinks).observe(lanesEl);
});
