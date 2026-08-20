/*
 * 3.1 teaching visual: chart + saved AI event output + 硃83 source text.
 *
 * This is an isolated presentation layer. It does not write review-tool
 * state, and the event dots live only for the current visual interaction.
 */
(function () {
  'use strict';

  function escapeHtml(value) {
    return String(value == null ? '' : value).replace(/[&<>"']/g, function (char) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[char];
    });
  }

  function parseDate(value) {
    var match = String(value || '').match(/^(\d{4})[\/-](\d{1,2})[\/-](\d{1,2})$/);
    return match ? Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3])) : 0;
  }

  function init() {
    var root = document.querySelector('[data-part2-events-visual]');
    var data = window.PART2_EVENTS_VISUAL_DATA;
    if (!root || !data || !data.document) return;

    var state = {
      addedIds: new Set(),
      activeQuote: '',
      selectedEventId: ''
    };
    var chartStart = parseDate('1786/12/01');
    var chartEnd = parseDate('1787/02/28');
    var chartSpan = chartEnd - chartStart;

    root.innerHTML = `
      <div class="part1-region part1-toolbar part2-events-visual-head" data-region="nav" aria-label="3.1 圖表工具列">
        <div class="part1-toolbar-start">
          <div class="part1-menu">
            <button class="part1-pill part1-pill-button" type="button" tabindex="-1" aria-disabled="true"><span class="part1-pl">點線類型</span><span aria-hidden="true">⌄</span></button>
          </div>
          <div class="part1-people-control"><span class="part1-pl">人物</span><select aria-label="選擇人物" tabindex="-1"><option>— 選擇人物 —</option></select><button type="button" tabindex="-1" aria-label="新增人物" aria-disabled="true">＋</button></div>
          <label class="part1-search"><span aria-hidden="true">⌕</span><input type="search" placeholder="搜尋原文 / 所有欄位…" aria-label="搜尋原文或所有欄位" readonly></label>
        </div>
        <span class="part1-toolgroup" data-toolgroup="areas">
          <button class="part1-toolbtn" type="button" tabindex="-1" aria-disabled="true">Note</button>
          <button class="part1-toolbtn is-emphasis" type="button" tabindex="-1" aria-disabled="true">AI</button>
          <button class="part1-toolbtn" type="button" tabindex="-1" aria-disabled="true">事件鏈</button>
        </span>
        <span class="part1-toolgroup" data-toolgroup="io">
          <button class="part1-toolbtn part1-gear-btn" type="button" tabindex="-1" aria-label="工具" aria-disabled="true">⚙</button>
          <span class="part1-count" title="硃83・保存的 AI 候選">硃83</span>
        </span>
      </div>
      <div class="part2-events-visual-stage" data-events-stage>
        <section class="part2-events-chart-panel" aria-label="事件時間線圖表">
          <div class="part2-events-panel-head">
            <div><span class="part2-events-panel-kicker">圖表</span><strong>戰場事件</strong></div>
            <span class="part2-events-count" data-events-count>文書 1 · 事件 0</span>
          </div>
          <div class="part2-events-chart-toolbar">
            <span class="part2-events-chart-legend"><i class="is-doc"></i>文書圓點</span>
            <span class="part2-events-chart-legend"><i class="is-lin"></i>林方行動</span>
            <span class="part2-events-chart-legend"><i class="is-qing"></i>清方行動</span>
          </div>
          <div class="part2-events-chart-labels" aria-hidden="true">
            <span>戰場事件</span><span>官員上奏</span><span>皇帝硃批下旨</span><span>皇帝行動</span>
          </div>
          <div class="part2-events-chart-plot" data-events-chart-plot>
            <div class="part2-events-chart-ruler" aria-hidden="true">
              <span style="top:2%">1786/12</span>
              <span style="top:38%">1787/1</span>
              <span style="top:73%">1787/2</span>
              <span style="top:98%">28</span>
            </div>
            <div class="part2-events-chart-canvas" data-events-chart-canvas>
              <svg class="part2-events-chart-links" data-events-chart-links aria-hidden="true"></svg>
              <div class="part2-events-chart-lane" data-events-lane="events"><span class="part2-events-lane-axis"></span></div>
              <div class="part2-events-chart-lane" data-events-lane="official"><span class="part2-events-lane-axis"></span></div>
              <div class="part2-events-chart-lane" data-events-lane="imperial"><span class="part2-events-lane-axis"></span></div>
              <div class="part2-events-chart-lane" data-events-lane="emperor"><span class="part2-events-lane-axis"></span></div>
            </div>
          </div>
          <p class="part2-events-chart-hint">先點選 AI 引文定位原文，再按「加入圖表」建立事件圓點；點擊圓點可查看完整事件資料。</p>
        </section>

        <aside class="part2-events-ai-panel" aria-label="AI 輸出面板">
          <div class="part2-events-panel-head">
            <div><span class="part2-events-panel-kicker">AI</span><strong>事件候選輸出</strong></div>
            <span class="part2-events-panel-status">未加入的候選</span>
          </div>
          <div class="part2-events-ai-run">
            <span class="part2-events-run-dot"></span>
            <span><b>${escapeHtml(data.bundleName)}</b><br>林方行動＋清方行動</span>
          </div>
          <p class="part2-events-ai-instruction">點按引文可在右側原文中定位；研究者確認後，才把候選加入圖表。</p>
          <div class="part2-events-ai-list" data-events-ai-list></div>
        </aside>

        <aside class="part2-events-doc-panel" aria-label="硃83原文面板">
          <div class="part2-events-doc-head">
            <div class="part2-events-doc-title"><span class="part2-events-doc-badge">硃</span><span>${escapeHtml(data.document.title)}</span></div>
            <p class="part2-events-doc-meta">${escapeHtml(data.document.author.position)}・${escapeHtml(data.document.author.name)}<br>${escapeHtml(data.document.sendDate[0])}上奏　${escapeHtml(data.document.receiveDate[0])}硃批<br>${escapeHtml(data.document.series)} 冊${escapeHtml(data.document.compiledIn.book)} 頁${escapeHtml(data.document.compiledIn.page)}・硃83</p>
          </div>
          <div class="part2-events-doc-tools">
            <span>原文</span><span class="part2-events-doc-tools-note">摘要與分段已展開</span>
          </div>
          <div class="part2-events-doc-scroll" data-events-doc-scroll>
            <section class="part2-events-doc-summary">
              <h4>摘要</h4>
              <p>${escapeHtml(data.summary)}</p>
            </section>
            <nav class="part2-events-doc-divisions" aria-label="文書分段" data-events-doc-divisions></nav>
            <div class="part2-events-doc-body" data-events-doc-body></div>
          </div>
        </aside>

        <aside class="part2-events-event-panel" data-events-event-panel hidden aria-label="事件圓點完整資料">
          <div class="part2-events-panel-head">
            <div><span class="part2-events-panel-kicker">事件圓點</span><strong data-events-event-heading>完整資料</strong></div>
            <button class="part2-events-icon-button" type="button" data-events-event-close aria-label="關閉事件圓點面板">×</button>
          </div>
          <div class="part2-events-event-body" data-events-event-body></div>
        </aside>
      </div>
      <p class="part2-events-visual-footnote">資料邊界：畫面展示保存的 AI 候選；加入圖表仍是研究者確認後的展示動作，不會改寫正式審閱資料。</p>
    `;

    var stage = root.querySelector('[data-events-stage]');
    var chartCanvas = root.querySelector('[data-events-chart-canvas]');
    var chartLinks = root.querySelector('[data-events-chart-links]');
    var countEl = root.querySelector('[data-events-count]');
    var aiList = root.querySelector('[data-events-ai-list]');
    var docBody = root.querySelector('[data-events-doc-body]');
    var docScroll = root.querySelector('[data-events-doc-scroll]');
    var divisionsNav = root.querySelector('[data-events-doc-divisions]');
    var eventPanel = root.querySelector('[data-events-event-panel]');
    var eventHeading = root.querySelector('[data-events-event-heading]');
    var eventBody = root.querySelector('[data-events-event-body]');

    var divisionRanges = data.divisions.map(function (part, index) {
      var start = data.document.body.indexOf(part.excerpt);
      if (start < 0) start = index ? 0 : 0;
      var next = data.divisions[index + 1];
      var nextStart = next ? data.document.body.indexOf(next.excerpt, Math.max(start, 0)) : data.document.body.length;
      if (nextStart < 0) nextStart = data.document.body.length;
      return { label: part.label, start: start, end: nextStart };
    });

    function eventById(id) {
      return data.events.find(function (event) { return event.id === id; }) || null;
    }

    function chartDate(event) {
      return parseDate(event.whenAr) || parseDate(data.document.sendDate[1]);
    }

    function chartDateLabel(event) {
      if (event.whenCh && event.whenAr) return event.whenCh + ' · ' + event.whenAr;
      if (event.whenCh) return event.whenCh;
      if (event.whenAr) return event.whenAr;
      return '用文書發送日 ' + data.document.sendDate[1] + '（事件日期未明）';
    }

    function percentForDate(value) {
      var date = parseDate(value);
      if (!date) return 0;
      return Math.max(2, Math.min(98, ((date - chartStart) / chartSpan) * 100));
    }

    function renderTextWithHighlight(text, quote) {
      var chunks = quote ? quote.split(/\.\.\.|…{2,}/).map(function (item) { return item.trim(); }).filter(Boolean) : [];
      var ranges = [];
      var cursor = 0;
      chunks.forEach(function (chunk) {
        var index = text.indexOf(chunk, cursor);
        if (index < 0) index = text.indexOf(chunk);
        if (index >= 0) {
          ranges.push({ start: index, end: index + chunk.length });
          cursor = index + chunk.length;
        }
      });
      if (!ranges.length && quote) {
        var exact = text.indexOf(quote);
        if (exact >= 0) ranges = [{ start: exact, end: exact + quote.length }];
      }
      ranges.sort(function (a, b) { return a.start - b.start; });
      var html = '';
      var at = 0;
      ranges.forEach(function (range) {
        if (range.start < at) return;
        html += escapeHtml(text.slice(at, range.start));
        html += '<mark class="part2-events-source-highlight" data-active-highlight>' + escapeHtml(text.slice(range.start, range.end)) + '</mark>';
        at = range.end;
      });
      html += escapeHtml(text.slice(at));
      return html.replace(/\n/g, '<br>');
    }

    function renderDocument() {
      divisionsNav.innerHTML = data.divisions.map(function (part, index) {
        return '<button type="button" class="part2-events-division-button" data-division-index="' + index + '"><span>' + (index + 1) + '</span>' + escapeHtml(part.label) + '</button>';
      }).join('');
      docBody.innerHTML = divisionRanges.map(function (range, index) {
        var text = data.document.body.slice(range.start, range.end);
        return '<section class="part2-events-doc-part" id="part2-events-doc-part-' + index + '">' +
          '<h4><span>' + (index + 1) + '</span>' + escapeHtml(range.label) + '</h4>' +
          '<p>' + renderTextWithHighlight(text, state.activeQuote) + '</p>' +
          '</section>';
      }).join('');
    }

    function updateActiveCard() {
      aiList.querySelectorAll('[data-ai-card]').forEach(function (card) {
        card.classList.toggle('is-quote-active', card.getAttribute('data-ai-card') === state.selectedEventId && Boolean(state.activeQuote));
      });
    }

    function highlightQuote(eventId) {
      var event = eventById(eventId);
      if (!event) return;
      state.selectedEventId = event.id;
      state.activeQuote = event.quote;
      renderDocument();
      updateActiveCard();
      var mark = docBody.querySelector('[data-active-highlight]');
      if (mark) {
        mark.classList.add('is-located');
        window.setTimeout(function () { mark.scrollIntoView({ block: 'center', behavior: 'smooth' }); }, 20);
      }
    }

    function factsMarkup(event) {
      var date = event.whenCh || event.whenAr || '本次輸出未提供';
      return '<dl class="part2-events-ai-facts">' +
        '<dt>地點</dt><dd>' + escapeHtml(event.where || '未提供') + '</dd>' +
        '<dt>人物</dt><dd>' + escapeHtml((event.who || []).join('、') || '未提供') + '</dd>' +
        '<dt>發生日期</dt><dd>' + escapeHtml(date) + '</dd>' +
        '</dl>';
    }

    function cardMarkup(event) {
      var colourClass = event.actor === 'lin' ? 'is-lin' : 'is-qing';
      return '<article class="part2-events-ai-card ' + colourClass + '" data-ai-card="' + escapeHtml(event.id) + '">' +
        '<div class="part2-events-ai-card-top"><span class="part2-events-skill-badge">' + escapeHtml(event.skill) + '</span><span class="part2-events-card-state" data-card-state>未加入</span></div>' +
        '<h4>' + escapeHtml(event.subtitle) + '</h4>' +
        '<p class="part2-events-ai-description">' + escapeHtml(event.description) + '</p>' +
        '<button class="part2-events-ai-quote" type="button" data-quote-event="' + escapeHtml(event.id) + '">「' + escapeHtml(event.quote) + '」<span>—硃83　點按定位</span></button>' +
        factsMarkup(event) +
        '<div class="part2-events-ai-card-bottom"><span class="part2-events-ai-provenance">' + escapeHtml(data.bundleName) + '／' + escapeHtml(event.sourceFile) + '</span><button class="part2-events-add" type="button" data-add-event="' + escapeHtml(event.id) + '">加入圖表</button></div>' +
        '</article>';
    }

    function renderAi() {
      aiList.innerHTML = data.events.map(cardMarkup).join('');
      aiList.querySelectorAll('[data-quote-event]').forEach(function (button) {
        button.addEventListener('click', function () { highlightQuote(button.getAttribute('data-quote-event')); });
      });
      aiList.querySelectorAll('[data-add-event]').forEach(function (button) {
        button.addEventListener('click', function () {
          addEvent(button.getAttribute('data-add-event'));
        });
      });
    }

    function nodePosition(node) {
      var canvasRect = chartCanvas.getBoundingClientRect();
      var rect = node.getBoundingClientRect();
      return {
        x: rect.left - canvasRect.left + rect.width / 2,
        y: rect.top - canvasRect.top + rect.height / 2
      };
    }

    function drawLinks() {
      if (!chartLinks) return;
      var width = chartCanvas.clientWidth;
      var height = chartCanvas.clientHeight;
      chartLinks.setAttribute('viewBox', '0 0 ' + width + ' ' + height);
      chartLinks.setAttribute('width', width);
      chartLinks.setAttribute('height', height);
      var docDot = chartCanvas.querySelector('[data-document-dot]');
      var source = docDot ? nodePosition(docDot) : null;
      chartLinks.innerHTML = source ? Array.from(chartCanvas.querySelectorAll('[data-event-dot]')).map(function (dot) {
        var target = nodePosition(dot);
        return '<line x1="' + source.x.toFixed(1) + '" y1="' + source.y.toFixed(1) + '" x2="' + target.x.toFixed(1) + '" y2="' + target.y.toFixed(1) + '"></line>';
      }).join('') : '';
    }

    function docDotMarkup() {
      var top = percentForDate(data.document.sendDate[1]);
      return '<button class="part2-events-chart-dot is-document" type="button" data-document-dot style="top:' + top + '%" aria-label="硃83・官員上奏・' + escapeHtml(data.document.title) + '"><span class="part2-events-dot-label">硃83</span></button>';
    }

    function eventDotMarkup(event) {
      var top = percentForDate(event.whenAr || data.document.sendDate[1]);
      var colour = event.actor === 'lin' ? 'is-lin' : 'is-qing';
      var dateNote = event.whenAr ? chartDateLabel(event) : chartDateLabel(event);
      return '<button class="part2-events-chart-dot is-event ' + colour + '" type="button" data-event-dot="' + escapeHtml(event.id) + '" style="top:' + top + '%" aria-label="' + escapeHtml(event.subtitle + '・' + dateNote) + '"><span class="part2-events-dot-label">' + escapeHtml(event.subtitle) + '</span></button>';
    }

    function renderChart() {
      var officialLane = chartCanvas.querySelector('[data-events-lane="official"]');
      var eventsLane = chartCanvas.querySelector('[data-events-lane="events"]');
      officialLane.querySelectorAll('[data-document-dot]').forEach(function (dot) { dot.remove(); });
      eventsLane.querySelectorAll('[data-event-dot]').forEach(function (dot) { dot.remove(); });
      officialLane.insertAdjacentHTML('beforeend', docDotMarkup());
      state.addedIds.forEach(function (id) {
        var event = eventById(id);
        if (event) eventsLane.insertAdjacentHTML('beforeend', eventDotMarkup(event));
      });
      countEl.textContent = '文書 1 · 事件 ' + state.addedIds.size;
      chartCanvas.querySelectorAll('[data-document-dot]').forEach(function (dot) {
        dot.addEventListener('click', function () {
          state.selectedEventId = '';
          state.activeQuote = '';
          renderDocument();
          updateActiveCard();
          docScroll.scrollTop = 0;
        });
      });
      chartCanvas.querySelectorAll('[data-event-dot]').forEach(function (dot) {
        dot.addEventListener('click', function () { openEvent(dot.getAttribute('data-event-dot')); });
      });
      window.requestAnimationFrame(drawLinks);
    }

    function syncAddedCard(eventId) {
      var card = aiList.querySelector('[data-ai-card="' + eventId + '"]');
      if (!card) return;
      card.classList.add('is-added');
      var stateEl = card.querySelector('[data-card-state]');
      var button = card.querySelector('[data-add-event]');
      if (stateEl) stateEl.textContent = '✓ 已加入圖表';
      if (button) {
        button.textContent = '已加入圖表';
        button.disabled = true;
      }
    }

    function addEvent(eventId) {
      var event = eventById(eventId);
      if (!event || state.addedIds.has(eventId)) return;
      state.addedIds.add(eventId);
      syncAddedCard(eventId);
      renderChart();
    }

    function relationMarkup(event) {
      if (!event.relations || !event.relations.length) return '<p class="part2-events-event-empty">本筆輸出未提供關係欄位。</p>';
      return '<ul class="part2-events-event-relations">' + event.relations.map(function (relation) {
        return '<li><span>' + escapeHtml(relation.source || '') + '</span><b>' + escapeHtml(relation.relation || '') + '</b><span>' + escapeHtml(relation.target || '') + '</span><small>' + escapeHtml(relation.evidence || '') + '</small></li>';
      }).join('') + '</ul>';
    }

    function openEvent(eventId) {
      var event = eventById(eventId);
      if (!event) return;
      state.selectedEventId = event.id;
      chartCanvas.querySelectorAll('[data-event-dot]').forEach(function (dot) {
        dot.classList.toggle('is-selected', dot.getAttribute('data-event-dot') === event.id);
      });
      eventPanel.hidden = false;
      stage.classList.add('has-event-detail');
      eventHeading.textContent = event.subtitle;
      eventBody.innerHTML =
        '<div class="part2-events-event-badges"><span class="part2-events-skill-badge ' + (event.actor === 'lin' ? 'is-lin' : 'is-qing') + '">' + escapeHtml(event.skill) + '</span><span class="part2-events-event-category">' + escapeHtml(event.category || '事件') + '</span></div>' +
        '<p class="part2-events-event-description">' + escapeHtml(event.description) + '</p>' +
        '<dl class="part2-events-event-facts">' +
          '<dt>地點</dt><dd>' + escapeHtml(event.where || '未提供') + '</dd>' +
          '<dt>人物</dt><dd>' + escapeHtml((event.who || []).join('、') || '未提供') + '</dd>' +
          '<dt>發生日期</dt><dd>' + escapeHtml(event.whenCh || '未提供') + '</dd>' +
          '<dt>圖表日期</dt><dd>' + escapeHtml(event.whenAr ? event.whenAr : '文書發送日 ' + data.document.sendDate[1] + '（事件日期未明）') + '</dd>' +
          '<dt>知悉方式</dt><dd>' + escapeHtml(event.howKnown || '未提供') + '</dd>' +
        '</dl>' +
        '<button class="part2-events-event-quote" type="button" data-event-detail-quote>「' + escapeHtml(event.quote) + '」<span>點按定位原文</span></button>' +
        '<h4 class="part2-events-event-section-title">關係</h4>' + relationMarkup(event) +
        '<div class="part2-events-event-source"><b>保存來源</b><br>' + escapeHtml(data.bundleName) + '<br>' + escapeHtml(event.sourceFile) + '<br>硃83</div>';
      var detailQuote = eventBody.querySelector('[data-event-detail-quote]');
      if (detailQuote) detailQuote.addEventListener('click', function () { highlightQuote(event.id); });
      updateActiveCard();
    }

    root.querySelector('[data-events-event-close]').addEventListener('click', function () {
      eventPanel.hidden = true;
      stage.classList.remove('has-event-detail');
      state.selectedEventId = '';
      chartCanvas.querySelectorAll('[data-event-dot]').forEach(function (dot) { dot.classList.remove('is-selected'); });
      updateActiveCard();
    });

    divisionsNav.addEventListener('click', function (event) {
      var button = event.target.closest('[data-division-index]');
      if (!button) return;
      var part = root.querySelector('#part2-events-doc-part-' + button.getAttribute('data-division-index'));
      if (part) part.scrollIntoView({ block: 'start', behavior: 'smooth' });
    });

    window.addEventListener('resize', function () { window.requestAnimationFrame(drawLinks); });

    renderDocument();
    renderAi();
    renderChart();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
