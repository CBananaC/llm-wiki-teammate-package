(function () {
  'use strict';

  var root = document.querySelector('#part-2-yu-response');
  var list = root && root.querySelector('[data-req-list]');
  if (!root || !list) return;

var zhuBody = String.raw`<span class="doc-dim doc-author-lead">兩廣總督兼署廣東巡撫臣<mark data-group="author">孫士毅</mark>跪奏，為遵旨起程回省，恭摺奏覆事竊臣於上年十二月二十四日具奏，接准閩省咨文，挑備戰兵以資策應一摺，本年正月二十四日敬奉硃批：「另有旨諭。」欽此。</span><span class="doc-focus">同日，<mark data-group="marker">接奉廷寄</mark><mark data-group="date">乾隆五十二年正月十三日</mark><mark data-group="marker">奉上諭</mark>：「<mark data-group="quote">據孫士毅奏，接准閩省咨文，挑備水師戰兵一千名，立即起程前赴南澳，以資策應，並知會署提臣彭承堯先赴潮州稽查彈壓。等語。閩粵境壤毗連，臺匪糾眾滋事，各隘口嚴密盤詰，此係當辦之事。孫士毅止當鎮靜地方，密飭隘口堵拿逸犯，豈得輕離省城，以致內地民人心懷疑惑。著孫士毅如尚未起程，即毋庸前往。若已起程，亦即速回省城。</mark>」等因。欽此。</span><span class="doc-dim">臣跪讀之下，仰見我皇上睿謨廣運，坐照無遺，萬里情形，洞如觀火。臣才庸識淺，不知輕重緩急，惑於漳、潮壤接，民情疑恐，親赴彈壓。一經聖明詳晰指示，臣自知錯謬，不禁慚悚交集（硃批：此時又當前往，爾等總不知機要，奈何）。茲臣雖未得閩省剿滅逆匪之信，但據報水陸兩提臣齊抵臺灣，逆賊漸已逃竄，自可即日蕩平。臣已於正月二十一日起，先將督標官兵陸續撤回歸伍。其先赴閩省之水師一千名，昨准閩浙督臣知會，現在暫駐漳州，用資彈壓。其駐紮黃崗等處水陸兵丁，臣現與署提臣彭承堯商酌，俟再得閩省剿賊確信。察看漳、潮交界處所，民情十分寧貼，亦即分起撤回。惟粵省惠、潮民人入天地會者，諒復不少，此種匪會，現有攻城殺官之事，非別項邪教止圖誆騙錢財者可比，必須徹底查辦，淨絕根株。其從外竄逃入境及內地勾引入會之人，均應一一搜捕，不留餘孽。臬司姚棻現已行調來潮，專司督緝，俟有續獲，另容隨時訊供具奏。一切稽查防範事宜，臣遵旨交與署提臣彭承堯，暫駐潮州督率料理。臣即於正月二十六日起程回省，仍俟續得臺地信息，隨時由驛迅速奏聞。所有臣欽奉諭旨，現在料理撤兵緝匪及起程回省日期，理合由驛四百里覆奏，伏乞皇上睿鑒。謹奏。<br><br>乾隆五十二年正月二十六日<br>乾隆五十二年二月十四日奉硃批：已有旨了。欽此。〔本文原收錄於軍錄〕</span>`;

var yuBody = String.raw`大學士公阿、大學士和，字寄兩廣總督<mark data-group="author">孫</mark>，<mark data-group="date">乾隆五十二年正月十三日</mark><mark data-group="marker">奉上諭</mark>：<mark data-group="quote">據孫士毅奏，接準閩省諮文，挑備水師戰兵一千名，立即起程，前赴南澳，以資策應。並知會署提臣彭承堯，先赴潮州稽查彈壓</mark>，數日內略爲料理地方事務，即親赴潮州駐紮，以便就近辦理等語，已於折內詳悉批示。<mark data-group="quote">閩粵境壤毗連，臺匪糾衆滋事，孫士毅接準諮文，派兵前往預備策應，及嚴飭各隘口，嚴密盤潔，遇有形跡可疑之人，立即究辦。此係當辦之事。</mark>至林爽文不過一烏合之衆，無難速就撲滅。前因該省水陸兩提督概行渡臺，朕尚以爲過當。<mark data-group="quote">孫士毅系鄰省總督，止當鎮靜地方，密飭各隘口堵拿逸犯，豈得輕離省城，以致粵東內地民人心懷疑惑。</mark>外省各督撫遇有此等事件，每以親身前往，見其急公，而不權事理之輕重緩急。督撫固不可養尊處優，身耽安逸，然當鎮靜辦理之事，亦不可過涉張皇，斷無因一二賊匪騷動各省之理。<mark data-group="quote">著傳諭孫士毅，此時如尚未起程，即毋庸前往。若業已起程，亦即回省城。</mark>潮州現有彭承堯在彼，盡足以資彈壓。若續得閩省臺地信息，即行迅速具奏。將此由六百里加緊諭令知之。欽此。遵旨寄信前來。`;

  var entries = [
    {
      id: 'marker', index: '01', title: '「奉上諭」等引述標記',
      summary: '官員在奏摺中回應皇帝的上諭時，通常會使用「奉上諭」、「奉聖諭」、「聖諭」、「奉廷寄」、「欽奉諭旨」或「欽奉上諭」等引述標記；部分回覆也會先用「接奉」、「接准」或「敬奉」等標記，注明自己收到上諭的日期。平台會先利用 Python 從原始文書中擷取這些標記，作為辨識奏摺是否回應上諭的第一項線索。',
      skill: '<div class="skill-row skill-heading"><span class="md-kw">## 3. Citation (引述標記)</span></div>' +
        '<div class="skill-row skill-lead">擷取奏摺中的引述標記：</div>' +
        '<div class="skill-row skill-highlight"><mark class="code-mark" data-group="marker">「奉上諭」／「奉聖諭」／「奉廷寄」／「欽奉諭旨」</mark></div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">Python 擷取</span>：從原始文書抓取標記及緊鄰的受文日期字串。</div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">AI 判斷</span>：比對標記後引用的內容，確認是否正在回應該道上諭。</div>'
    },
    {
      id: 'date', index: '02', title: '上諭的發出日期',
      summary: '系統篩選候選文書的第一項條件：上諭的發佈日期，必須和奏摺中「奉上諭」標記前所寫明的日期相符。',
      skill: '<div class="skill-row skill-heading"><span class="md-kw">## 2. Date (日期比對)</span></div>' +
        '<div class="skill-row skill-lead">比對上諭發布與收訖時間序：</div>' +
        '<div class="skill-row skill-highlight"><mark class="code-mark" data-group="date">以「奉上諭」前之日期為發布日，比對發文時間序</mark></div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">傳遞時差</span>：廷寄至外省約需 10–14 天；奏摺發出必在上諭之後。</div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">收訖判定</span>：「接奉」前為官員收訖日，與發布日相互驗證。</div>'
    },
    {
      id: 'quote', index: '03', title: '上諭引文',
      summary: '系統篩選候選文書的第三項條件：奏摺中引用的上諭內容，必須與候選上諭的內容完全或大致相同。',
      skill: '<div class="skill-row skill-heading"><span class="md-kw">## 3. Citation (引文比對)</span></div>' +
        '<div class="skill-row skill-lead">擷取奏摺所引之完整上諭內容：</div>' +
        '<div class="skill-row skill-highlight"><mark class="code-mark" data-group="quote">擷取奏摺所引完整上諭，比對候選正文（允許節略重寫）</mark></div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">範圍擷取</span>：自官員收訖說明開始，至「欽此」前之完整引文。</div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">寬鬆匹配</span>：清代奏摺轉述常有字句刪節，AI 判斷語意一致性。</div>'
    },
    {
      id: 'author', index: '04', title: '奏摺作者',
      summary: '系統篩選候選文書的第二項條件：奏摺作者，應為上諭的受文官員之一。',
      skill: '<div class="skill-row skill-heading"><span class="md-kw">## 1. Identity (官員身分)</span></div>' +
        '<div class="skill-row skill-lead">確認奏摺官員與受文者之對應關係：</div>' +
        '<div class="skill-row skill-highlight"><mark class="code-mark" data-group="author">奏摺具名作者必須為該道上諭之受文官員之一</mark></div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">職權對應</span>：如大學士寄信予兩廣總督孫士毅，回應必由孫發出。</div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">候選篩選</span>：依官員身分與日期窗口建立候選文書配對池。</div>'
    }
  ];

  /* ==========================================================================
     Mobile / narrow layout (<= 860px, the section's existing breakpoint —
     see storymap-cards.css "@media (max-width: 860px) { #part-2-yu-response
     .req-stage ... }"): the original folded-tab accordion — VS Code style
     skill window + two document windows, typed reveal animation. Unchanged
     from the previous production behaviour; only wrapped in a function so
     it can be built lazily and only for narrow viewports.
     ========================================================================== */
  var mobileBuilt = false;
  function buildMobile() {
    if (mobileBuilt || list.dataset.reqBuilt === 'true') return;
    mobileBuilt = true;

    function docWindow(type) {
        var isZhu = type === 'zhu';
        var body = isZhu ? zhuBody : yuBody;
        var title = isZhu ? '為奏料理撤兵及回省日期事' : '諭兩廣總督孫士毅毋庸親往潮州';
        var panel = window.part2DocPanel;
        return panel.create({
          outerClass: 'req-win req-win-doc',
          dataReqDoc: type,
          badge: isZhu ? '硃' : '諭',
          badgeClass: isZhu ? 'b-zhu' : 'b-yu',
          title: title,
          metaLines: isZhu
            ? ['孫士毅（兩廣總督兼署廣東巡撫）', '乾隆52年1月26日發出', '乾隆52年2月14日硃批', '明清台檔30，頁329']
            : ['大學士公阿桂、大學士和珅 字寄兩廣總督孫（士毅）', '乾隆52年1月13日發佈', '《天地會》1，頁231'],
          label: '原文',
          body: body
        });
      }

      function buildEntry(entry) {
        var el = document.createElement('div');
        el.className = 'req-entry';
        el.setAttribute('data-req-item', entry.id);
        el.innerHTML = '<div class="req-card" data-req-card>' +
          '<button class="req-bar" type="button" aria-expanded="false" data-req-bar><span class="req-index">' + entry.index + '</span><strong>' + entry.title + '</strong><span class="req-arrow" aria-hidden="true">▾</span></button>' +
          '<div class="req-panel" data-req-panel><div class="req-panel-inner"><div class="req-wordcard" data-req-wordcard><p>' + entry.summary + '</p></div></div></div>' +
        '<div class="req-stage-wrap" data-req-stage-wrap><div class="req-stage-wrap-inner"><div class="req-visual"><div class="req-stage" data-req-stage>' +
          '<div class="req-win req-win-skill" data-req-skill><div class="agentic-mac-titlebar"><span class="agentic-mac-dot red"></span><span class="agentic-mac-dot yellow"></span><span class="agentic-mac-dot green"></span><span class="agentic-window-title">yu-response-pairing.md</span></div><div class="req-vscode-shell"><div class="req-vscode-activitybar"><span>▦</span><span>⌕</span><span>⑂</span><span>▣</span><span>⚙</span></div><div class="req-vscode-editor"><div class="req-vscode-tabs"><span class="req-vscode-tab">yu-response-pairing.md</span></div><div class="req-vscode-body" data-req-body>' + entry.skill + '</div></div></div></div>' +
          '<span class="req-connector" data-req-connector="1" aria-hidden="true">→</span>' + docWindow('zhu') +
          '<span class="req-connector" data-req-connector="2" aria-hidden="true">→</span>' + docWindow('yu') +
        '</div></div></div>' +
        '</div></div>';
        return el;
      }

      entries.forEach(function (entry) { list.appendChild(buildEntry(entry)); });
      list.dataset.reqBuilt = 'true';
      var docPanel = window.part2DocPanel;

      var WIDTH_MS = 380;
      var PANEL_MS = 380;
      var WIN_REVEAL_MS = 380;

      var items = Array.prototype.slice.call(root.querySelectorAll('[data-req-item]')).map(function (el) {
        var stage = el.querySelector('[data-req-stage]');
        var skillWin = el.querySelector('[data-req-skill]');
        var zhuWin = el.querySelector('[data-req-doc="zhu"]');
        var yuWin = el.querySelector('[data-req-doc="yu"]');
        var bodies = { skill: skillWin.querySelector('[data-req-body]'), zhu: zhuWin.querySelector('[data-req-body]'), yu: yuWin.querySelector('[data-req-body]') };
        Object.keys(bodies).forEach(function (k) { bodies[k].dataset.original = bodies[k].innerHTML; });
        return {
          id: el.getAttribute('data-req-item'), el: el, card: el.querySelector('[data-req-card]'), bar: el.querySelector('[data-req-bar]'),
          panel: el.querySelector('[data-req-panel]'), wordcard: el.querySelector('[data-req-wordcard]'), stageWrap: el.querySelector('[data-req-stage-wrap]'),
          stage: stage, wins: [skillWin, zhuWin, yuWin], connectors: [el.querySelector('[data-req-connector="1"]'), el.querySelector('[data-req-connector="2"]')], bodies: bodies, timers: []
        };
      });

      function clearItemTimers(item) { item.timers.forEach(function (t) { clearTimeout(t); clearInterval(t); }); item.timers = []; }
      function resetItem(item) {
        clearItemTimers(item); item.card.classList.remove('is-open'); item.panel.classList.remove('is-open'); item.stageWrap.classList.remove('is-open'); item.wordcard.classList.remove('is-shown');
        item.wins.forEach(function (w) { w.classList.remove('is-shown'); if (docPanel) docPanel.reset(w); }); item.connectors.forEach(function (c) { c.classList.remove('is-shown'); });
        Object.keys(item.bodies).forEach(function (k) { item.bodies[k].innerHTML = item.bodies[k].dataset.original; item.bodies[k].scrollTop = 0; });
      }
      function typeInto(item, el, step, tickMs, done) {
        var full = el.dataset.original;
        var plain = (function () { var tmp = document.createElement('div'); tmp.innerHTML = full; return tmp.textContent; })();
        var i = 0; el.textContent = ''; var caret = document.createElement('span'); caret.className = 'req-caret';
        var timer = setInterval(function () { i += step; if (i >= plain.length) { clearInterval(timer); el.innerHTML = full; if (done) done(); return; } el.textContent = plain.slice(0, i); el.appendChild(caret); el.scrollTop = el.scrollHeight; }, tickMs);
        item.timers.push(timer);
      }
      function activateGroup(item, group) {
        if (!group || group !== item.id) return;
        item.wins.forEach(function (w) {
          w.querySelectorAll('mark[data-group]').forEach(function (m) {
            if (!docPanel || docPanel.matchesGroup(m, group)) {
              m.classList.remove('is-active'); void m.offsetWidth; m.classList.add('is-active');
            }
          });
          if (docPanel && w.classList.contains('source-flow-document')) docPanel.focus(w, group);
        });
        var first = item.el.querySelector('.req-win [data-group="' + group + '"]');
        if (first) first.scrollIntoView({ block: 'nearest', inline: 'nearest', behavior: 'smooth' });
      }
      function revealStage(item) {
        var skillWin = item.wins[0], zhuWin = item.wins[1], yuWin = item.wins[2], c1 = item.connectors[0], c2 = item.connectors[1];
        skillWin.classList.add('is-shown');
        item.timers.push(setTimeout(function () {
          typeInto(item, item.bodies.skill, 5, 9, function () {
            c1.classList.add('is-shown');
            zhuWin.classList.add('is-shown');
            item.timers.push(setTimeout(function () {
              typeInto(item, item.bodies.zhu, 10, 9, function () {
                c2.classList.add('is-shown');
                yuWin.classList.add('is-shown');
                item.timers.push(setTimeout(function () {
                  typeInto(item, item.bodies.yu, 8, 9, function () {
                    activateGroup(item, item.id);
                  });
                }, WIN_REVEAL_MS));
              });
            }, WIN_REVEAL_MS));
          });
        }, WIN_REVEAL_MS));
      }
      function closeItem(item) { item.el.classList.remove('is-open'); item.bar.setAttribute('aria-expanded', 'false'); resetItem(item); }
      function openItem(item) {
        items.forEach(function (other) { if (other !== item && other.el.classList.contains('is-open')) closeItem(other); });
        resetItem(item); item.el.classList.add('is-open'); item.bar.setAttribute('aria-expanded', 'true');
        // 窄條展開與三欄視覺區塊（含待機大 Skill 視窗 → 本列小視窗的交接動畫）同步觸發，
        // 文字卡緊接著（原節奏）由上至下展開。
        item.card.classList.add('is-open');
        item.stageWrap.classList.add('is-open');
        revealStage(item);
        item.timers.push(setTimeout(function () {
          item.panel.classList.add('is-open');
          item.timers.push(setTimeout(function () {
            item.wordcard.classList.add('is-shown');
          }, PANEL_MS));
        }, WIDTH_MS));
      }
      items.forEach(function (item) {
        item.bar.addEventListener('click', function () { if (item.el.classList.contains('is-open')) closeItem(item); else openItem(item); });
        item.stage.addEventListener('click', function (e) { var mark = e.target.closest('mark[data-group]'); if (mark) activateGroup(item, mark.getAttribute('data-group')); });
        if (docPanel) docPanel.bindAll(item.wins);
      });
  }

  var DESKTOP_MARKUP =
    '<div class="replica-shell">' +
      '<div data-part1 data-part1-data="PART1_INTERFACE_DATA_YU_RESPONSE"><div class="part1-replica" data-part1-replica></div></div>' +
    '</div>' +
    '<div class="req-desc is-open" data-req-desc>' +
      '<div class="req-desc-head">' +
        '<span class="req-desc-index" data-req-desc-index>1</span>' +
        '<h3 data-req-desc-title></h3>' +
        '<div class="req-nav" data-req-nav>' +
          '<button class="req-nav-arrow" type="button" data-nav-prev aria-label="上一項線索">&#8592;</button>' +
          '<button class="req-nav-arrow" type="button" data-nav-next aria-label="下一項線索">&#8594;</button>' +
        '</div>' +
      '</div>' +
      '<div class="req-desc-body">' +
        '<div class="req-desc-split">' +
          '<div class="req-desc-text-panel"><div class="req-wordcard"><p data-req-desc-summary></p></div></div>' +
          '<div class="req-desc-skill-panel">' +
            '<div class="req-win-skill-box">' +
              '<div class="req-skill-titlebar">' +
                '<span class="req-mac-dot red"></span><span class="req-mac-dot yellow"></span><span class="req-mac-dot green"></span>' +
                '<span class="req-skill-title-text">yu-response-pairing.md</span>' +
              '</div>' +
              '<div class="req-skill-shell">' +
                '<div class="req-skill-activitybar"><span>▦</span><span>⌕</span><span>⑂</span><span>▣</span></div>' +
                '<div class="req-skill-editor">' +
                  '<div class="req-skill-body" data-req-skill-body></div>' +
                '</div>' +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>' +
    '</div>';


  var DESKTOP_CSS = [
    /* the shared "idle Skill window" decoration (part2-req-ui-style.js) is
       a mobile-only holdover from the folded-tab accordion look — the
       reviewed desktop tool already has its own description card, so hide
       the idle window (and the wrap it lives in) whenever desktop mode is
       active, however/whenever it appears in the DOM. */
    /* Generous upper margin and surrounding space around the visual. */
    '#part-2-content #part-2-yu-response { padding-top: 0 !important; padding-left: clamp(2px, 0.8vw, 14px) !important; padding-right: clamp(2px, 0.8vw, 14px) !important; }',
    '#part-2-content #part-2-yu-response > .part2-substage-cover, #part-2-yu-response .part2-substage-cover { padding-top: 28px !important; padding-bottom: 26px !important; margin-top: 0 !important; margin-bottom: 0 !important; }',
    '#part-2-content #part-2-yu-response > .story-inner, #part-2-content #part-2-yu-response > .part2-yu-response-story-inner { width: 100% !important; max-width: 100% !important; margin: 0 !important; padding-top: 0 !important; }',
    '#part-2-yu-response .req-desktop-tool { margin: 22px 0 0 !important; width: 100%; }',
    '#part-2-yu-response .replica-shell { width: 100%; background: #f1eadc; border: 1px solid #d8cdbb; border-radius: 6px; box-shadow: 0 13px 30px rgba(47,57,52,.15); overflow: hidden; --stage-dock-pct: 50%; }',
    '#part-2-yu-response .replica-shell .part1-replica { --font-scale: 1; }',
    '#part-2-yu-response .replica-stage { padding: 6px; gap: 8px; height: clamp(640px, 72vh, 800px); }',

    /* description panel sits BELOW the visual with its own card spacing */
    '#part-2-yu-response .req-desc { display: flex; flex-direction: column; margin: 18px 0 0; background: var(--card); border: 1px solid #d8cdbb; border-radius: 6px; box-shadow: 0 8px 24px rgba(47,57,52,.1); overflow: hidden; }',
    '#part-2-yu-response .req-desc-head { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; padding: 13px 20px 11px; border-bottom: 1px solid var(--line); background: rgba(244,239,230,.4); }',
    /* number circle in description card: align background color with the active clue\'s highlight color. */
    '#part-2-yu-response .req-desc .req-desc-index { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 30px; height: 30px; color: #fffaf2; background: #8a7c66; border-radius: 50%; font: 800 13px/1 var(--sans); }',
    '#part-2-yu-response .req-desc[data-active-req="marker"] .req-desc-index { background: rgb(var(--hl-marker)) !important; }',
    '#part-2-yu-response .req-desc[data-active-req="date"] .req-desc-index { background: rgb(var(--hl-date)) !important; }',
    '#part-2-yu-response .req-desc[data-active-req="quote"] .req-desc-index { background: rgb(var(--hl-quote)) !important; }',
    '#part-2-yu-response .req-desc[data-active-req="author"] .req-desc-index { background: rgb(var(--hl-author)) !important; }',
    '#part-2-yu-response .req-desc-head h3 { flex: 1; min-width: 160px; margin: 0; color: var(--ink); font: 700 18px/1.35 var(--serif); }',
    '#part-2-yu-response .req-desc-body { padding: 16px 20px 18px; }',

    /* 50% / 50% split layout: left text explanation, right skill window with matching height */
    '#part-2-yu-response .req-desc-split { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: stretch; width: 100%; }',
    '#part-2-yu-response .req-desc-text-panel { display: flex; flex-direction: column; justify-content: center; min-width: 0; padding: 4px 0; height: 100%; }',
    '#part-2-yu-response .req-desc .req-wordcard { display: flex; flex-direction: column; justify-content: center; height: 100%; }',
    '#part-2-yu-response .req-desc .req-wordcard p { margin: 0; color: var(--text); font: 500 calc(15px * var(--font-scale, 1))/1.95 var(--serif); text-align: justify; }',

    /* Right Skills Window: 50% width, matches text card height, always full height with zero scrolling */
    '#part-2-yu-response .req-desc-skill-panel { display: flex; flex-direction: column; min-width: 0; height: 100%; }',
    '#part-2-yu-response .req-win-skill-box { display: flex; flex-direction: column; height: 100%; min-height: max-content; background: #1e1e1e; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,.18), 0 0 0 1px rgba(255,255,255,.07) inset; }',
    '#part-2-yu-response .req-skill-titlebar { display: flex; align-items: center; gap: 6px; padding: 8px 12px; background: #252526; border-bottom: 1px solid #333333; flex: none; }',
    '#part-2-yu-response .req-mac-dot { width: 8.5px; height: 8.5px; border-radius: 50%; flex: none; }',
    '#part-2-yu-response .req-mac-dot.red { background: #ff5f57; }',
    '#part-2-yu-response .req-mac-dot.yellow { background: #febc2e; }',
    '#part-2-yu-response .req-mac-dot.green { background: #28c840; }',
    '#part-2-yu-response .req-skill-title-text { margin-left: 5px; color: #b5b5b5; font: 600 calc(12px * var(--font-scale, 1))/1 "SF Mono", ui-monospace, Menlo, Consolas, monospace; letter-spacing: .02em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex: 1; }',

    '#part-2-yu-response .req-skill-shell { display: grid; grid-template-columns: 26px 1fr; flex: 1 1 auto; height: 100%; min-height: max-content; background: #1e1e1e; }',
    '#part-2-yu-response .req-skill-activitybar { display: flex; flex-direction: column; align-items: center; gap: 12px; padding: 16px 0; color: #707070; background: #2b2b2b; font: 10.5px/1 var(--sans); border-right: 1px solid #383838; user-select: none; height: 100%; }',
    '#part-2-yu-response .req-skill-editor { display: flex; flex-direction: column; min-width: 0; min-height: max-content; height: 100%; }',
    '#part-2-yu-response .req-skill-body { flex: 1 1 auto; height: auto; min-height: max-content; overflow: visible !important; padding: 18px 18px 20px; color: #d4d4d4; font: 500 calc(13px * var(--font-scale, 1))/1.8 "SF Mono", ui-monospace, Menlo, Consolas, monospace; word-break: break-word; scrollbar-width: none; }',
    '#part-2-yu-response .req-skill-body::-webkit-scrollbar { display: none; }',
    '#part-2-yu-response .req-skill-body .skill-row { margin-bottom: 7px; }',
    '#part-2-yu-response .req-skill-body .skill-row:last-child { margin-bottom: 0; }',
    '#part-2-yu-response .req-skill-body .skill-heading { font-weight: 700; color: #4fc1ff; margin-bottom: 10px; font-size: calc(13.5px * var(--font-scale, 1)); }',
    '#part-2-yu-response .req-skill-body .skill-lead { margin-bottom: 6px; }',
    '#part-2-yu-response .req-skill-body .skill-highlight { margin: 8px 0 9px; }',
    '#part-2-yu-response .req-skill-body .skill-bullet { margin-bottom: 7px; }',
    '#part-2-yu-response .req-skill-body .md-kw { color: #4fc1ff; font-weight: 600; }',
    '#part-2-yu-response .req-skill-body .md-bullet { color: #9cdcfe; font-weight: bold; margin-right: 4px; }',

    /* Highlight in skill window */
    '#part-2-yu-response .req-skill-body mark.code-mark { display: inline-block; padding: 2px 7px; border-radius: 4px; color: #ffffff !important; font-weight: 600; line-height: 1.45; box-decoration-break: clone; -webkit-box-decoration-break: clone; }',
    '#part-2-yu-response .req-desc[data-active-req="marker"] .req-skill-body mark.code-mark[data-group="marker"] { background: rgba(var(--hl-marker), .85) !important; box-shadow: 0 0 0 1px rgba(var(--hl-marker), 1); }',
    '#part-2-yu-response .req-desc[data-active-req="date"] .req-skill-body mark.code-mark[data-group="date"] { background: rgba(var(--hl-date), .9) !important; box-shadow: 0 0 0 1px rgba(var(--hl-date), 1); }',
    '#part-2-yu-response .req-desc[data-active-req="quote"] .req-skill-body mark.code-mark[data-group="quote"] { background: rgba(var(--hl-quote), .85) !important; box-shadow: 0 0 0 1px rgba(var(--hl-quote), 1); }',
    '#part-2-yu-response .req-desc[data-active-req="author"] .req-skill-body mark.code-mark[data-group="author"] { background: rgba(var(--hl-author), .88) !important; box-shadow: 0 0 0 1px rgba(var(--hl-author), 1); }',

    '#part-2-yu-response .req-nav { display: flex; align-items: center; gap: 6px; margin-left: auto; }',
    '#part-2-yu-response .req-nav-arrow { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; color: var(--ink); background: transparent; border: 1px solid var(--line); border-radius: 50%; cursor: pointer; transition: background .15s ease, color .15s ease; }',
    '#part-2-yu-response .req-nav-arrow:hover { color: #fffaf2; background: var(--accent); border-color: var(--accent); }',

    /* top toolbar is decorative in this teaching visual: not clickable. */
    '#part-2-yu-response .replica-shell .part1-toolbar { pointer-events: none !important; }',
    '#part-2-yu-response .replica-shell .part1-toolbar * { pointer-events: none !important; cursor: default !important; }',
    '#part-2-yu-response .replica-shell .part1-toolbar button, #part-2-yu-response .replica-shell .part1-toolbar select, #part-2-yu-response .replica-shell .part1-toolbar input { opacity: .45; }',
    '#part-2-yu-response .replica-shell .part1-toolbar [data-type-pop], #part-2-yu-response .replica-shell .part1-toolbar [data-tools-pop] { display: none !important; }',

    /* the two real doc panels must stay open: disable the close button. */
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-window-btn[data-panel-close] { pointer-events: none !important; opacity: .35; }',
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-window-btn[data-panel-close] .part1-chat-svg, #part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-window-btn[data-panel-close] svg { display: none; }',
    /* remove the drag (move) and minimise buttons from the doc-panel title. */
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-window-btn[aria-label="移動文書面板"], #part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-window-btn[aria-label="收合文書面板"] { display: none !important; }',
    /* disable the filter and settings buttons in the doc panel. */
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-filter-trigger, #part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-filter-gear { pointer-events: none !important; opacity: .35; }',

    /* Remove the shorter second horizontal line inside the text card by stripping border-top from .req-wordcard. */
    '#part-2-yu-response .req-desc .req-wordcard { border-top: none !important; padding-top: 0 !important; margin: 0 !important; opacity: 1 !important; transform: none !important; }',

    /* Follow the website\'s font-size setting (root --font-scale) instead of the engine\'s pinned --font-scale:1. */
    '#part-2-yu-response .replica-shell { --site-font-scale: var(--font-scale, 1); }',
    '#part-2-yu-response .part1-replica { --font-scale: var(--site-font-scale) !important; --body-font-scale: var(--site-font-scale) !important; }',

    /* Apply the exact typography from 總結文書 (為奏聞林爽文攻陷彰化情形事) to the doc panel header. */
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-head { padding: 14px 16px 12px; background: linear-gradient(#fffdf8, #f3eada); border-bottom: 1px solid #e1d8c9; }',
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-head .part1-doc-title, #part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-title, #part-2-yu-response .part1-replica[data-pair-doc="true"] [data-doc-panel-title] { font: 700 calc(18px * var(--font-scale, 1))/1.35 var(--serif) !important; color: #2d261d !important; letter-spacing: .02em; margin: 0 0 6px; }',
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .badge, #part-2-yu-response .part1-replica[data-pair-doc="true"] [data-doc-panel-badge] { display: inline-block; width: auto; height: auto; margin-right: 6px; padding: 2px 7px; color: #fffaf2; background: #c46a2b; border-radius: 6px; font: 800 calc(13px * var(--font-scale, 1))/1.1 var(--sans) !important; vertical-align: 1px; }',
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-meta { margin: 0; color: #7a6f63; font: 500 calc(13px * var(--font-scale, 1))/1.55 var(--sans); line-height: 1.55; }',
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-section-label { font-size: calc(17px * var(--font-scale)); }',
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-body { font-size: calc(15.5px * var(--font-scale)); }',
    '#part-2-yu-response .req-desc-head h3 { font-size: calc(22px * var(--font-scale)) !important; }',
    '#part-2-yu-response .req-desc .req-wordcard p { font-size: calc(16px * var(--font-scale)); }',

    /* fix: pair-doc dock must track the two real panels, not a fixed-size reserved 2nd grid column. */
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-dock { grid-template-columns: 1fr !important; }',

    /* width changer: a real-style drag handle between the two doc panels. */
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-doc-stack { grid-template-columns: calc(var(--pair-left-pct, 50%) - 5px) 10px calc(var(--pair-right-pct, 50%) - 5px) !important; gap: 0 !important; }',
    '#part-2-yu-response .req-pair-resize { position: relative; z-index: 6; cursor: ew-resize; touch-action: none; user-select: none; }',
    '#part-2-yu-response .req-pair-resize::before { content: ""; position: absolute; top: 38%; bottom: 38%; left: 4px; width: 2px; border-radius: 2px; background: #d1c2ad; opacity: .7; transition: background .15s ease, opacity .15s ease, transform .15s ease; }',
    '#part-2-yu-response .req-pair-resize:hover::before, #part-2-yu-response .req-pair-resize:focus-visible::before, #part-2-yu-response .req-pair-resize.is-dragging::before { background: #a67d4f; opacity: 1; transform: scaleX(1.8); }',
    '#part-2-yu-response .req-pair-resize:focus-visible { outline: 2px solid rgba(166,125,79,.45); outline-offset: -1px; }',

    /* floating clue bubble: larger text for the bubble title + comfortable buttons. */
    '#part-2-yu-response .part1-replica[data-pair-doc="true"] .part1-pair-doc { position: relative; }',
    '#part-2-yu-response .req-float-bubble { position: absolute; left: 0; top: 0; z-index: 30; display: flex; align-items: center; gap: 8px; height: 38px; max-width: calc(100% - 16px); padding: 5px 12px 5px 6px; color: #241d12; background: #fffdf8; border: 2px solid rgb(var(--bc, var(--hl-marker))); border-radius: 999px; box-shadow: 0 8px 18px rgba(30,22,10,.22); font: 700 10px/1 var(--sans); white-space: nowrap; transition: opacity .15s ease, left .12s ease, top .12s ease; }',
    '#part-2-yu-response .req-float-bubble[data-bubble-group="marker"] { --bc: var(--hl-marker); }',
    '#part-2-yu-response .req-float-bubble[data-bubble-group="date"] { --bc: var(--hl-date); }',
    '#part-2-yu-response .req-float-bubble[data-bubble-group="quote"] { --bc: var(--hl-quote); }',
    '#part-2-yu-response .req-float-bubble[data-bubble-group="author"] { --bc: var(--hl-author); }',
    '#part-2-yu-response .req-float-bubble.req-float-hidden { opacity: 0; pointer-events: none; }',
    '#part-2-yu-response .req-float-num { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 24px; height: 24px; color: #fffdf8; background: rgb(var(--bc)); border-radius: 50%; font: 800 13px/1 var(--sans); }',
    '#part-2-yu-response .req-float-title { flex: 1 1 auto; min-width: 0; padding: 0 4px; overflow: hidden; text-overflow: ellipsis; color: #241d12; font: 800 calc(14.5px * var(--font-scale, 1))/1.35 var(--serif); }',
    '#part-2-yu-response .req-float-arrow { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 22px; height: 22px; color: rgb(var(--bc)); background: transparent; border: 1.5px solid rgba(var(--bc),.5); border-radius: 50%; cursor: pointer; font: 700 13px/1 var(--sans); transition: background .15s ease; }',
    '#part-2-yu-response .req-float-arrow:hover { background: rgba(var(--bc),.16); }',
    '#part-2-yu-response .req-float-tail { position: absolute; left: 50%; bottom: -7px; width: 13px; height: 13px; background: #fffdf8; border-right: 2px solid rgb(var(--bc, var(--hl-marker))); border-bottom: 2px solid rgb(var(--bc, var(--hl-marker))); transform: translateX(-50%) rotate(45deg); border-radius: 0 0 3px 0; }',
    '#part-2-yu-response .req-float-bubble.req-float-flip .req-float-tail { bottom: auto; top: -7px; border-right: 0; border-bottom: 0; border-left: 2px solid rgb(var(--bc, var(--hl-marker))); border-top: 2px solid rgb(var(--bc, var(--hl-marker))); border-radius: 3px 0 0 0; }',

    /* Vivid, bright persistent highlight marks inside the doc panels (staying luminous after click). */
    '#part-2-yu-response .part1-pair-doc .part1-doc-body mark[data-group] { padding: 2px 4px; border-radius: 3px; box-decoration-break: clone; -webkit-box-decoration-break: clone; color: inherit !important; background: transparent !important; cursor: pointer; transition: background-color .15s ease, color .15s ease; }',
    '#part-2-yu-response .part1-pair-doc .part1-doc-body mark[data-group]:hover { filter: brightness(.92); }',
    '#part-2-yu-response .req-desktop-tool[data-active-req="marker"] .part1-pair-doc .part1-doc-body mark[data-group="marker"], #part-2-yu-response .req-desktop-tool[data-active-req="marker"] .part1-pair-doc .part1-doc-body mark[data-group="marker"].is-active { background: #3ee0cf !important; color: #043834 !important; font-weight: 600; box-shadow: 0 0 0 1px rgba(35, 195, 180, .4); }',
    '#part-2-yu-response .req-desktop-tool[data-active-req="date"] .part1-pair-doc .part1-doc-body mark[data-group="date"], #part-2-yu-response .req-desktop-tool[data-active-req="date"] .part1-pair-doc .part1-doc-body mark[data-group="date"].is-active { background: #ffd644 !important; color: #3b2800 !important; font-weight: 600; box-shadow: 0 0 0 1px rgba(220, 165, 20, .4); }',
    '#part-2-yu-response .req-desktop-tool[data-active-req="quote"] .part1-pair-doc .part1-doc-body mark[data-group="quote"], #part-2-yu-response .req-desktop-tool[data-active-req="quote"] .part1-pair-doc .part1-doc-body mark[data-group="quote"].is-active { background: #ff9370 !important; color: #3e1204 !important; font-weight: 600; box-shadow: 0 0 0 1px rgba(225, 90, 50, .4); }',
    '#part-2-yu-response .req-desktop-tool[data-active-req="author"] .part1-pair-doc .part1-doc-body mark[data-group="author"], #part-2-yu-response .req-desktop-tool[data-active-req="author"] .part1-pair-doc .part1-doc-body mark[data-group="author"].is-active { background: #d896ff !important; color: #23043d !important; font-weight: 600; box-shadow: 0 0 0 1px rgba(170, 80, 225, .4); }',
    '#part-2-yu-response .part1-pair-doc .part1-doc-body mark[data-group].is-active { animation: part2-yu-response-hl-flash .5s ease-out; }',
    '@keyframes part2-yu-response-hl-flash { 0% { filter: brightness(1.28) saturate(1.25); } 100% { filter: brightness(1); } }',

    /* Left Document Panel (硃160 奏摺): Highlight the focal response quotation and make surrounding context text transparent/dimmed */
    '#part-2-yu-response [data-doc-panel-doc="硃160"] .doc-dim, #part-2-yu-response [data-req-doc="zhu"] .doc-dim { opacity: 0.35; transition: opacity .2s ease; }',
    '#part-2-yu-response [data-doc-panel-doc="硃160"] .doc-dim:hover, #part-2-yu-response [data-req-doc="zhu"] .doc-dim:hover { opacity: 0.72; }',
    '#part-2-yu-response [data-doc-panel-doc="硃160"] .doc-focus, #part-2-yu-response [data-req-doc="zhu"] .doc-focus { opacity: 1; color: #18120b; font-weight: 500; }',
    '#part-2-yu-response .req-desktop-tool[data-active-req="author"] [data-doc-panel-doc="硃160"] .doc-author-lead, #part-2-yu-response .req-desktop-tool[data-active-req="author"] [data-req-doc="zhu"] .doc-author-lead { opacity: 1 !important; color: #18120b !important; font-weight: 500; }',
    '#part-2-yu-response .part1-pair-doc .part1-doc-body mark[data-group], #part-2-yu-response [data-req-stage] .req-doc-body mark[data-group] { opacity: 1 !important; }',

    /* linking line between the two example dots on the real engine chart */
    '#part-2-yu-response .part1-chart-links .part1-bg-link { opacity: 0.22 !important; pointer-events: none !important; }',
    '#part-2-yu-response .part1-chart-links .req-chart-link, #part-2-yu-response .part1-chart-links .part1-example-link { transition: opacity .2s ease, stroke-width .2s ease; cursor: pointer; pointer-events: stroke; }',
    '#part-2-yu-response .part1-chart-links .req-chart-link:hover, #part-2-yu-response .part1-chart-links .part1-example-link:hover { stroke-width: 3.4 !important; filter: brightness(1.2); }',
    '#part-2-yu-response .part1-chart-links .req-chart-link.is-active { opacity: 1 !important; stroke-width: 3.2 !important; }',

    '@media (max-width: 860px) { #part-2-yu-response .req-desc-split { grid-template-columns: 1fr; gap: 10px; } }',
    '@media (max-width: 900px) { #part-2-yu-response .req-float-title { display: none; } }'
  ].join('\n');

  /* ==========================================================================
     Desktop layout (> 860px): the real platform-interface-replica engine
     (part-1-interface.js + part-1-interface.css, already loaded on this
     page for Part 1) running in its guarded "pairDoc" mode — real chart
     with all 723 real nodes as background dots + the two real 硃160／諭43
     document panels + a floating clue bubble. This ports the reviewed
     storymap-2-1-yu-response-draft-v8.html into production. Built lazily,
     and only once, the first time a >860px viewport is seen.
     ========================================================================== */
  var desktopBuilt = false;
  var desktopWrap = null;
  var desktopSetActive = null;

  // Clone (not mutate) window.PART1_INTERFACE_DATA: the same data object
  // also drives the five [data-part1] "Part 1" teaching mounts elsewhere on
  // this page, so this section must not rewrite it in place.
  function buildDesktopDataClone() {
    var GLOBAL_NAME = 'PART1_INTERFACE_DATA_YU_RESPONSE';
    var base = window.PART1_INTERFACE_DATA;
    if (!base) return null;
    var docMap = new Map((base.documents || []).map(function (rec) { return [rec.docId, rec]; }));
    var zhuRecord = docMap.get('硃160');
    var yuRecord = docMap.get('諭43');
    if (!zhuRecord || !yuRecord) {
      console.warn('2-1 desktop tool: 硃160/諭43 not found in the real chart data.');
      return null;
    }
    var EXAMPLE_NODE_IDS = ['doc-硃160-L', 'doc-諭43-R'];
    var clone = Object.assign({}, base);
    clone.document = zhuRecord;
    clone.documents = [yuRecord];
    clone.pairDoc = true;

    // Filter out all blue circle dots (shangzou documents), retaining other nodes
    var nodes = (base.chartPreview.nodes || []).filter(function (node) {
      var isBlueCircle = node.kind === 'document' && (node.recordType === 'shangzou' || node.color === '#2f75b5');
      if (isBlueCircle && EXAMPLE_NODE_IDS.indexOf(node.id) === -1) {
        return false;
      }
      return true;
    }).map(function (node) {
      var copy = Object.assign({}, node);
      copy.background = EXAMPLE_NODE_IDS.indexOf(node.id) === -1;
      return copy;
    });

    var existingNodeIds = new Set(nodes.map(function (n) { return n.id; }));
    var nodeById = new Map((base.chartPreview.nodes || []).map(function (n) { return [n.id, n]; }));

    // Retain only allowed background links ('document-endpoint' and 'event-source'),
    // making them semi-transparent and unclickable. Exclude emperor-action -> official-doc links.
    var ALLOWED_BG_KINDS = new Set(['document-endpoint', 'event-source']);
    var bgLinks = (base.chartPreview.links || []).map(function (link) {
      if (!ALLOWED_BG_KINDS.has(link.kind)) return null;
      if (!existingNodeIds.has(link.from) || !existingNodeIds.has(link.to)) return null;
      var isExamplePair = (link.from === 'doc-諭43-R' && link.to === 'doc-硃160-L') ||
                          (link.from === 'doc-硃160-L' && link.to === 'doc-諭43-R');
      if (isExamplePair) return null;

      var fn = nodeById.get(link.from);
      var tn = nodeById.get(link.to);
      var flane = fn ? fn.lane : '';
      var tlane = tn ? tn.lane : '';
      if ((flane === 'emperor' && tlane === 'official') || (flane === 'official' && tlane === 'emperor')) {
        return null;
      }

      var copy = Object.assign({}, link);
      copy.background = true;
      copy.opacity = 0.22;
      return copy;
    }).filter(Boolean);

    // Active foreground example link: clear, prominent, clickable
    var exampleLink = {
      id: 'example-pair-yu43-zhu160',
      from: 'doc-諭43-R',
      to: 'doc-硃160-L',
      className: 'part1-preview-link req-chart-link',
      color: '#c45d38',
      width: 2.8,
      background: false,
      title: '諭43 ↔ 硃160（回應上諭配對）'
    };

    clone.chartPreview = Object.assign({}, base.chartPreview, {
      nodes: nodes,
      links: bgLinks.concat([exampleLink])
    });
    window[GLOBAL_NAME] = clone;
    return GLOBAL_NAME;
  }

  var DESKTOP_STYLE_ID = 'part2-yu-response-desktop-style';
  function ensureDesktopStyle() {
    if (document.getElementById(DESKTOP_STYLE_ID)) return;
    var style = document.createElement('style');
    style.id = DESKTOP_STYLE_ID;
    style.textContent = DESKTOP_CSS;
    document.head.appendChild(style);
  }

  function buildDesktop() {
    if (desktopBuilt) return;
    if (typeof window.part1InitRoot !== 'function') {
      console.warn('2-1 desktop tool: part1InitRoot() not found — part-1-interface.js may be an older version.');
      return;
    }
    var globalName = buildDesktopDataClone();
    if (!globalName) return;
    desktopBuilt = true;
    ensureDesktopStyle();

    desktopWrap = document.createElement('div');
    desktopWrap.className = 'req-desktop-tool';
    desktopWrap.setAttribute('data-req-desktop-tool', '');
    desktopWrap.innerHTML = DESKTOP_MARKUP;
    list.parentNode.insertBefore(desktopWrap, list.nextSibling);

    window.part1InitRoot(desktopWrap.querySelector('[data-part1]'));
    desktopSetActive = setupDesktopOverlay(desktopWrap);
  }

  // Teaching overlay: one floating clue bubble (number + title + prev/next
  // arrows, same colour, only the text changes) floating over the LEFT
  // (奏摺) panel only; the RIGHT (上諭) panel only gets the synced
  // highlight. Only one clue's highlight is shown at a time, in both
  // panels; switching is via the arrows (bubble or the description card).
  function setupDesktopOverlay(wrap) {
    var GROUP_ORDER = entries.map(function (e) { return e.id; });
    var activeId = GROUP_ORDER[0];
    var floatBubble = null;

    function pad2(n) { return String(n).padStart(2, '0'); }
    function pairDocPanels() { return Array.prototype.slice.call(wrap.querySelectorAll('[data-doc-panel-doc]')); }
    function panelBodies() { return Array.prototype.slice.call(wrap.querySelectorAll('[data-doc-body]')); }

    function injectFloatBubble() {
      var panels = pairDocPanels();
      var leftPanel = panels[0];
      if (!leftPanel) return;
      var existingBubble = leftPanel.querySelector('[data-req-float-bubble]');
      if (existingBubble) {
        floatBubble = existingBubble;
        return;
      }
      var bubble = document.createElement('div');
      bubble.className = 'req-float-bubble';
      bubble.setAttribute('data-req-float-bubble', '');
      bubble.innerHTML =
        '<span class="req-float-num" data-req-float-num></span>' +
        '<span class="req-float-title" data-req-float-title></span>' +
        '<button type="button" class="req-float-arrow" data-bubble-prev aria-label="上一項線索">‹</button>' +
        '<button type="button" class="req-float-arrow" data-bubble-next aria-label="下一項線索">›</button>' +
        '<span class="req-float-tail" aria-hidden="true"></span>';
      leftPanel.appendChild(bubble);
      floatBubble = bubble;

      // Keep the bubble locked onto the active clue's highlighted text as
      // the panel resizes (the drag handle), the window resizes, or the
      // panel's own text scrolls.
      var scrollEl = leftPanel.querySelector('[data-doc-scroll]');
      if (scrollEl) scrollEl.addEventListener('scroll', positionBubble);
      if ('ResizeObserver' in window) {
        new ResizeObserver(positionBubble).observe(leftPanel);
      }
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(positionBubble);
    }

    // Points the bubble at the active clue's first highlighted mark inside
    // the LEFT panel, using its live on-screen position rather than a fixed
    // corner — so it stays correct across panel-width changes, font-size
    // changes, and viewport resizes. Fades out (instead of drifting to a
    // wrong spot or sitting over blank space) once that mark scrolls
    // outside the panel's visible text area.
    function positionBubble() {
      if (!floatBubble) return;
      var leftPanel = pairDocPanels()[0];
      var leftBody = leftPanel && leftPanel.querySelector('[data-doc-body]');
      var markEl = leftBody && leftBody.querySelector('mark[data-group="' + activeId + '"]');
      if (!leftPanel || !markEl) { floatBubble.classList.add('req-float-hidden'); return; }

      var scrollEl = leftPanel.querySelector('[data-doc-scroll]');
      var markRect = markEl.getBoundingClientRect();
      if (scrollEl) {
        var scrollRect = scrollEl.getBoundingClientRect();
        var inView = markRect.bottom > scrollRect.top + 2 && markRect.top < scrollRect.bottom - 2;
        if (!inView) { floatBubble.classList.add('req-float-hidden'); return; }
      }
      floatBubble.classList.remove('req-float-hidden');

      var panelRect = leftPanel.getBoundingClientRect();
      var bubbleW = floatBubble.offsetWidth;
      var bubbleH = floatBubble.offsetHeight;
      var pad = 8;
      var centerX = markRect.left + markRect.width / 2 - panelRect.left;
      var left = centerX - bubbleW / 2;
      left = Math.max(pad, Math.min(left, panelRect.width - bubbleW - pad));
      var gap = 12;
      var topAbove = markRect.top - panelRect.top - bubbleH - gap;
      var flipped = false;
      var top;
      if (topAbove < pad) {
        flipped = true;
        top = markRect.bottom - panelRect.top + gap;
      } else {
        top = topAbove;
      }
      floatBubble.style.left = left + 'px';
      floatBubble.style.top = top + 'px';
      floatBubble.classList.toggle('req-float-flip', flipped);
      var tail = floatBubble.querySelector('.req-float-tail');
      if (tail) {
        var tailLeft = Math.max(14, Math.min(centerX - left, bubbleW - 14));
        tail.style.left = tailLeft + 'px';
      }
    }

    function injectPairResizer() {
      var stack = wrap.querySelector('[data-doc-stack]');
      if (!stack || stack.querySelector('[data-pair-resize]')) return;
      var panels = stack.querySelectorAll('[data-doc-panel-doc]');
      if (panels.length < 2) return;
      var handle = document.createElement('div');
      handle.className = 'req-pair-resize';
      handle.setAttribute('data-pair-resize', '');
      handle.setAttribute('role', 'separator');
      handle.setAttribute('aria-orientation', 'vertical');
      handle.setAttribute('aria-valuemin', '20');
      handle.setAttribute('aria-valuemax', '80');
      handle.setAttribute('aria-valuenow', '50');
      handle.setAttribute('tabindex', '0');
      handle.setAttribute('aria-label', '調整兩份文書面板的寬度比例');
      stack.insertBefore(handle, panels[1]);

      var leftPct = 50;
      function apply() {
        stack.style.setProperty('--pair-left-pct', leftPct + '%');
        stack.style.setProperty('--pair-right-pct', (100 - leftPct) + '%');
        handle.setAttribute('aria-valuenow', String(Math.round(leftPct)));
        positionBubble();
      }
      handle.addEventListener('pointerdown', function (e) {
        e.preventDefault();
        handle.classList.add('is-dragging');
        if (handle.setPointerCapture) { try { handle.setPointerCapture(e.pointerId); } catch (err) {} }
        var rect = stack.getBoundingClientRect();
        function onMove(ev) {
          var pct = ((ev.clientX - rect.left) / rect.width) * 100;
          leftPct = Math.max(20, Math.min(80, pct));
          apply();
        }
        function onUp() {
          handle.classList.remove('is-dragging');
          document.removeEventListener('pointermove', onMove);
          document.removeEventListener('pointerup', onUp);
        }
        document.addEventListener('pointermove', onMove);
        document.addEventListener('pointerup', onUp);
      });
      handle.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowLeft') { leftPct = Math.max(20, leftPct - 4); apply(); }
        else if (e.key === 'ArrowRight') { leftPct = Math.min(80, leftPct + 4); apply(); }
        else { return; }
        e.preventDefault();
      });
      apply();
    }

    function flashMarks(groupId) {
      panelBodies().forEach(function (body) {
        body.querySelectorAll('mark[data-group="' + groupId + '"]').forEach(function (mark) {
          mark.classList.remove('is-active');
          void mark.offsetWidth;
          mark.classList.add('is-active');
        });
      });
    }

    function centerPairLine() {
      var scrollEl = wrap.querySelector('[data-chart-scroll]');
      if (!scrollEl) return;
      var a = wrap.querySelector('[data-chart-node-id="doc-硃160-L"]');
      var b = wrap.querySelector('[data-chart-node-id="doc-諭43-R"]');
      if (!a || !b) return;
      var ra = a.getBoundingClientRect();
      var rb = b.getBoundingClientRect();
      var sr = scrollEl.getBoundingClientRect();
      var midX = (ra.left + ra.right + rb.left + rb.right) / 4;
      var midY = (ra.top + ra.bottom + rb.top + rb.bottom) / 4;
      var tx = scrollEl.scrollLeft + midX - (sr.left + sr.width / 2);
      var ty = scrollEl.scrollTop + midY - (sr.top + sr.height / 2);
      scrollEl.scrollTo({ left: tx, top: ty, behavior: 'auto' });
    }

    // Center the example-dot linking line once layout has settled (the engine
    // redraws the chart synchronously during init, then fonts/layout land a
    // frame later), and re-center after any resize that re-runs drawLinks.
    // Also re-runs the clue bubble's own positioning, since both rely on
    // real on-screen geometry that only settles at the same points.
    var centerTimer = 0;
    function scheduleCenter() {
      if (centerTimer) return;
      centerTimer = window.setTimeout(function () {
        centerTimer = 0;
        requestAnimationFrame(function () { centerPairLine(); positionBubble(); });
      }, 350);
    }
    window.addEventListener('resize', scheduleCenter);

    // Both centerPairLine() and positionBubble() read getBoundingClientRect(),
    // which is zeroed out while this section's tab panel is [hidden] — and
    // this section is built on page load, before the visitor has necessarily
    // clicked into the "Part 2" tab that reveals it. Re-run once the tab
    // panel actually becomes visible, using the same
    // MutationObserver({attributeFilter:['hidden']}) pattern storymap.js
    // itself already uses elsewhere for tab-gated content (see
    // initResponsiveSequentialRows in storymap.js).
    var tabPanel = root.closest('[data-tab-panel]');
    if (tabPanel && 'MutationObserver' in window) {
      new MutationObserver(function () {
        if (!tabPanel.hidden) scheduleCenter();
      }).observe(tabPanel, { attributes: true, attributeFilter: ['hidden'] });
    }

    function setActive(groupId, opts) {
      opts = opts || {};
      activeId = groupId;
      var idx = GROUP_ORDER.indexOf(groupId);
      var req = entries[idx];
      if (!req) return;

      var descIdx = wrap.querySelector('[data-req-desc-index]');
      var descTitle = wrap.querySelector('[data-req-desc-title]');
      var descSummary = wrap.querySelector('[data-req-desc-summary]');
      var descSkillBody = wrap.querySelector('[data-req-skill-body]');
      if (descIdx) descIdx.textContent = String(idx + 1);
      if (descTitle) descTitle.textContent = req.title;
      if (descSummary) descSummary.textContent = req.summary;
      if (descSkillBody) descSkillBody.innerHTML = req.skill;
      // The description panel with text card + 50% skill window sits below the visual.
      var desc = wrap.querySelector('[data-req-desc]');
      if (desc) {
        desc.setAttribute('data-active-req', groupId);
        if (opts.openDesc !== false) desc.classList.add('is-open');
      }

      if (floatBubble) {
        floatBubble.setAttribute('data-bubble-group', groupId);
        var numEl = floatBubble.querySelector('[data-req-float-num]');
        var titleEl = floatBubble.querySelector('[data-req-float-title]');
        if (numEl) numEl.textContent = String(idx + 1);
        if (titleEl) titleEl.textContent = req.title;
      }

      wrap.setAttribute('data-active-req', groupId);

      wrap.querySelectorAll('.part1-chart-links .req-chart-link').forEach(function (line) {
        line.classList.toggle('is-active', groupId === 'marker' || groupId === 'quote');
      });

      if (!opts.skipScroll) {
        panelBodies().forEach(function (body) {
          var mark = body.querySelector('mark[data-group="' + groupId + '"]');
          if (!mark) return;
          var scroll = body.closest('[data-doc-scroll]');
          if (scroll) {
            var sr = scroll.getBoundingClientRect();
            var mr = mark.getBoundingClientRect();
            scroll.scrollTop = Math.max(0, scroll.scrollTop + mr.top - sr.top - Math.max(18, scroll.clientHeight * 0.18));
          }
        });
      }
      flashMarks(groupId);
      requestAnimationFrame(positionBubble);
    }

    function goTo(delta) {
      var i = GROUP_ORDER.indexOf(activeId);
      setActive(GROUP_ORDER[(i + delta + GROUP_ORDER.length) % GROUP_ORDER.length], { openDesc: true });
    }

    wrap.addEventListener('click', function (e) {
      var prev = e.target.closest('[data-bubble-prev]');
      if (prev) { goTo(-1); return; }
      var next = e.target.closest('[data-bubble-next]');
      if (next) { goTo(1); return; }
      var mark = e.target.closest('.part1-doc-body mark[data-group]');
      if (mark) { setActive(mark.getAttribute('data-group'), { openDesc: true }); return; }
      var exLink = e.target.closest('.part1-chart-links .req-chart-link, .part1-chart-links .part1-example-link');
      if (exLink) {
        setActive(activeId, { openDesc: true });
        if (typeof window.__part1OnDocSelect === 'function') {
          window.__part1OnDocSelect({ docId: '硃160' });
          window.__part1OnDocSelect({ docId: '諭43' });
        }
        return;
      }
    });
    var navPrev = wrap.querySelector('[data-nav-prev]');
    var navNext = wrap.querySelector('[data-nav-next]');
    if (navPrev) navPrev.addEventListener('click', function () { goTo(-1); });
    if (navNext) navNext.addEventListener('click', function () { goTo(1); });

    window.__part1OnLinkSelect = function (link) {
      if ((link.from === 'doc-諭43-R' && link.to === 'doc-硃160-L') ||
          (link.from === 'doc-硃160-L' && link.to === 'doc-諭43-R') ||
          link.className?.indexOf('req-chart-link') !== -1) {
        setActive(activeId, { openDesc: true });
        if (typeof window.__part1OnDocSelect === 'function') {
          window.__part1OnDocSelect({ docId: '硃160' });
          window.__part1OnDocSelect({ docId: '諭43' });
        }
      }
    };

    var dataClone = window.PART1_INTERFACE_DATA_YU_RESPONSE;
    function initPair(records) {
      var PANEL_BY_DOC = { '硃160': 'zhu', '諭43': 'yu' };
      var BODY_BY_KEY = { zhu: zhuBody, yu: yuBody };
      records.forEach(function (record) {
        var panel = wrap.querySelector('[data-doc-panel-doc="' + record.docId + '"]');
        if (!panel) return;
        var body = panel.querySelector('[data-doc-body]');
        var bodyText = BODY_BY_KEY[PANEL_BY_DOC[record.docId]];
        if (body && bodyText) body.innerHTML = bodyText;
      });
      injectFloatBubble();
      injectPairResizer();
      setActive(activeId, { skipScroll: true, openDesc: true });
      centerPairLine();
      scheduleCenter();
    }
    if (dataClone) {
      dataClone.onPairInit = initPair;
      dataClone.onDocSelect = function (record) {
        var panel = wrap.querySelector('[data-doc-panel-doc="' + record.docId + '"]');
        if (panel) {
          panel.classList.remove('is-flash');
          void panel.offsetWidth;
          panel.classList.add('is-flash');
          window.setTimeout(function () { panel.classList.remove('is-flash'); }, 900);
        }
      };
    }

    if (wrap.querySelector('[data-doc-panel-doc]')) {
      initPair([{ docId: '硃160' }, { docId: '諭43' }]);
    }
    return setActive;
  }

  /* ==========================================================================
     Pick mobile vs desktop by the section's existing 860px breakpoint, and
     react if the viewport is resized across it (e.g. testing responsive
     layouts in a desktop browser) so the right variant is always showing.
     Both variants build lazily and only once; switching after that is a
     plain show/hide, so no state is lost and nothing is rebuilt.

     Note on data-req-mode: part2-req-ui-style.js (loaded after this file)
     wraps [data-req-list] in a shared "idle Skill window" decoration used
     by all of 2-1/2-2/2-3 — it isn't present in the DOM yet when this
     script first runs, so it can't be hidden by JS at that point. The
     data-req-mode="desktop" CSS rule below hides it reactively whenever it
     shows up, regardless of script timing.
     ========================================================================== */
  var mq = window.matchMedia('(max-width: 860px)');
  function applyMode() {
    root.setAttribute('data-req-mode', mq.matches ? 'mobile' : 'desktop');
    if (mq.matches) {
      buildMobile();
      list.style.display = '';
      if (desktopWrap) desktopWrap.style.display = 'none';
    } else {
      buildDesktop();
      list.style.display = 'none';
      if (desktopWrap) desktopWrap.style.display = '';
    }
  }
  applyMode();
  if (mq.addEventListener) mq.addEventListener('change', applyMode);
  else if (mq.addListener) mq.addListener(applyMode);
})();
