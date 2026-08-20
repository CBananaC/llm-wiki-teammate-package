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

  function buildPart2ChartData(data) {
    var base = window.PART1_INTERFACE_DATA;
    if (!base || !base.chartPreview || !Array.isArray(base.chartPreview.nodes)) return null;

    var documentRecord = (base.documents || []).find(function (record) {
      return record && record.docId === data.document.docId;
    });
    if (!documentRecord) return null;

    var documentNodeId = 'doc-' + data.document.docId + '-L';
    var removedDocumentNodeId = 'doc-' + data.document.docId + '-R';
    var exampleNodeIds = [documentNodeId];
    var nodes = base.chartPreview.nodes.filter(function (node) {
      if (node.id === removedDocumentNodeId) return false;
      var isBlueDocument = node.kind === 'document'
        && (node.recordType === 'shangzou' || node.color === '#2f75b5');
      return !isBlueDocument || exampleNodeIds.indexOf(node.id) !== -1;
    }).map(function (node) {
      var copy = Object.assign({}, node);
      copy.background = exampleNodeIds.indexOf(node.id) === -1;
      return copy;
    });

    var candidateNodes = data.events.map(function (event) {
      return {
        id: event.id,
        kind: 'event',
        recordType: 'event',
        lane: 'events',
        side: 'L',
        actor: event.actor === 'lin' ? 'lin' : 'qing',
        dateAr: event.whenAr || data.document.sendDate[1],
        label: event.whenCh || event.whenAr || '日期未明',
        color: event.actor === 'lin' ? '#b5462e' : '#3f6f8f',
        radius: 5.2,
        background: true,
        payload: event
      };
    });

    var nodeIds = new Set(nodes.concat(candidateNodes).map(function (node) { return node.id; }));
    var nodeById = new Map(base.chartPreview.nodes.map(function (node) { return [node.id, node]; }));
    var backgroundLinks = (base.chartPreview.links || []).map(function (link) {
      if (['document-endpoint', 'event-source'].indexOf(link.kind) === -1) return null;
      if (!nodeIds.has(link.from) || !nodeIds.has(link.to)) return null;
      var fromNode = nodeById.get(link.from);
      var toNode = nodeById.get(link.to);
      var fromLane = fromNode ? fromNode.lane : '';
      var toLane = toNode ? toNode.lane : '';
      if ((fromLane === 'emperor' && toLane === 'official') || (fromLane === 'official' && toLane === 'emperor')) return null;
      return Object.assign({}, link, { background: true, opacity: 0.22 });
    }).filter(Boolean);

    var candidateLinks = data.events.map(function (event) {
      return {
        from: event.id,
        to: documentNodeId,
        className: 'part2-events-link-' + event.id,
        color: event.actor === 'lin' ? '#b5462e' : '#3f6f8f',
        width: 1.8,
        kind: 'event-source',
        dash: '4 4',
        background: true,
        opacity: 0
      };
    });

    var clone = Object.assign({}, base, {
      document: documentRecord,
      documents: base.documents
    });
    clone.chartPreview = Object.assign({}, base.chartPreview, {
      nodes: nodes.concat(candidateNodes),
      links: backgroundLinks.concat(candidateLinks)
    });
    window.PART1_INTERFACE_DATA_EVENTS = clone;
    return 'PART1_INTERFACE_DATA_EVENTS';
  }

  function init() {
    var root = document.querySelector('[data-part2-events-visual]');
    var data = window.PART2_EVENTS_VISUAL_DATA;
    if (!root || !data || !data.document) return;

    var chartDataName = buildPart2ChartData(data);
    if (!chartDataName || typeof window.part1InitRoot !== 'function') {
      console.warn('3.1 visual: shared 2.1 chart data or part1InitRoot() is unavailable.');
      return;
    }

    var state = {
      addedIds: new Set(),
      activeQuote: '',
      selectedEventId: ''
    };
    root.innerHTML = `
      <div class="part2-events-visual-stage" data-events-stage>
        <section class="part2-events-chart-panel" aria-label="事件時間線圖表">
          <div class="part2-events-chart-replica-shell" data-events-chart-replica>
            <div data-part1 data-part1-data="${chartDataName}" data-part1-mode="chart" data-part1-chart-scale="1" role="group" aria-label="沿用 2.1 的時間與關係圖表">
              <div class="part1-replica" data-part1-replica aria-live="polite"></div>
            </div>
          </div>
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
    var chartPartRoot = root.querySelector('[data-part1]');
    window.part1InitRoot(chartPartRoot);
    var chartReplica = chartPartRoot.querySelector('[data-part1-replica]');
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

    function chartDateLabel(event) {
      if (event.whenCh && event.whenAr) return event.whenCh + ' · ' + event.whenAr;
      if (event.whenCh) return event.whenCh;
      if (event.whenAr) return event.whenAr;
      return '用文書發送日 ' + data.document.sendDate[1] + '（事件日期未明）';
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

    function chartNodeForId(id) {
      if (!chartReplica) return null;
      return Array.prototype.slice.call(chartReplica.querySelectorAll('[data-chart-node-id]')).find(function (node) {
        return node.getAttribute('data-chart-node-id') === id;
      }) || null;
    }

    function chartLinkForEvent(eventId) {
      return chartReplica ? chartReplica.querySelector('.part2-events-link-' + eventId) : null;
    }

    function setCandidateNodeState(event, isAdded) {
      var node = chartNodeForId(event.id);
      var link = chartLinkForEvent(event.id);
      if (node) {
        node.classList.toggle('is-added', isAdded);
        node.style.opacity = isAdded ? '1' : '0';
        node.style.pointerEvents = isAdded ? 'auto' : 'none';
        if (isAdded) {
          node.removeAttribute('aria-hidden');
          node.setAttribute('role', 'button');
          node.setAttribute('tabindex', '0');
          node.setAttribute('aria-label', event.subtitle + '・' + chartDateLabel(event));
        } else {
          node.setAttribute('aria-hidden', 'true');
          node.removeAttribute('role');
          node.removeAttribute('tabindex');
        }
      }
      if (link) link.style.opacity = isAdded ? '0.88' : '0';
    }

    function bindChartNodes() {
      data.events.forEach(function (event) {
        var node = chartNodeForId(event.id);
        if (!node) return;
        node.classList.add('part2-events-candidate-node');
        node.setAttribute('data-part2-event-id', event.id);
        if (node.dataset.part2EventsBound !== 'true') {
          node.dataset.part2EventsBound = 'true';
          node.addEventListener('click', function () {
            if (state.addedIds.has(event.id)) openEvent(event.id);
          });
          node.addEventListener('keydown', function (keyboardEvent) {
            if ((keyboardEvent.key === 'Enter' || keyboardEvent.key === ' ') && state.addedIds.has(event.id)) {
              keyboardEvent.preventDefault();
              openEvent(event.id);
            }
          });
        }
      });

      var documentNode = chartNodeForId('doc-' + data.document.docId + '-L');
      if (documentNode) {
        documentNode.classList.add('part2-events-document-node');
        if (documentNode.dataset.part2EventsBound !== 'true') {
          documentNode.dataset.part2EventsBound = 'true';
          documentNode.addEventListener('click', function () {
            state.selectedEventId = '';
            state.activeQuote = '';
            renderDocument();
            updateActiveCard();
            docScroll.scrollTop = 0;
          });
        }
      }
    }

    function bindChartNodesWhenReady() {
      bindChartNodes();
      renderChart();
      if (!chartReplica || typeof MutationObserver !== 'function') return;

      var observer = new MutationObserver(function () {
        bindChartNodes();
        renderChart();
      });
      observer.observe(chartReplica, { childList: true, subtree: true });

      window.requestAnimationFrame(function () {
        bindChartNodes();
        renderChart();
      });
      window.setTimeout(function () {
        bindChartNodes();
        renderChart();
      }, 80);
    }

    function renderChart() {
      data.events.forEach(function (event) {
        setCandidateNodeState(event, state.addedIds.has(event.id));
      });
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
      chartReplica.querySelectorAll('.part2-events-candidate-node').forEach(function (dot) {
        dot.classList.toggle('is-selected', dot.getAttribute('data-part2-event-id') === event.id);
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
      chartReplica.querySelectorAll('.part2-events-candidate-node').forEach(function (dot) { dot.classList.remove('is-selected'); });
      updateActiveCard();
    });

    divisionsNav.addEventListener('click', function (event) {
      var button = event.target.closest('[data-division-index]');
      if (!button) return;
      var part = root.querySelector('#part2-events-doc-part-' + button.getAttribute('data-division-index'));
      if (part) part.scrollIntoView({ block: 'start', behavior: 'smooth' });
    });

    window.addEventListener('resize', function () { window.requestAnimationFrame(renderChart); });

    renderDocument();
    renderAi();
    bindChartNodesWhenReady();
    if ('ResizeObserver' in window) {
      new ResizeObserver(function () {
        bindChartNodes();
        renderChart();
      }).observe(chartReplica);
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
