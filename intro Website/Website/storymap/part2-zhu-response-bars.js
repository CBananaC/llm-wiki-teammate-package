(function () {
  'use strict';

  var root = document.querySelector('#part-2-zhu-response');
  var list = root && root.querySelector('[data-req-list]');
  if (!root || !list) return;

  var zhuReplyBody = String.raw`<span class="doc-dim">奴才<mark data-group="identity">黃仕簡</mark>謹奏，為欽奉上諭，恭摺覆奏事。本年三月初四日，接到廷寄乾隆五十二年二月十二日奉上諭：「昨據黃仕簡奏，派令總兵郝壯猷、柴大紀分路剿捕賊匪，該提督在郡城南北衝要處堵禦擒捕。等語。所奏殊不詳悉。」等因。欽此。二月十三日奉上諭：「本日據任承恩奏，發兵剿賊情形一摺，所奏略有頭緒。」等因。欽此。二月十四日奉上諭：「本日常青奏，接據陸路提督各報，剿殺彰化賊匪情形一摺，皆係任承恩業經奏聞之事。」等因。欽此。</span><span class="doc-focus">又，<mark data-group="identity">正月初五日，奴才具奏報到臺灣查辦情形一摺</mark>，<mark data-group="marker">奉硃批</mark>：「<mark data-group="quote">所奏已遲，早有旨諭。</mark>」欽此。</span><span class="doc-dim">三月初六日，又接到廷寄二月十一日奉上諭：「本日據黃仕簡奏報，派員帶兵進剿南北二路賊匪情形一摺。」等因。欽此。又，正月十三日奴才具奏分遣官兵進剿一摺，奉硃批：「所奏既遲，又不詳悉，已有旨了。」欽此。查，鳳山、諸羅二縣，奴才到臺灣時，各縣尚為賊踞，未經收復。隨即分遣總兵郝壯猷柴大紀等，帶領官兵，馳赴南、北二路剿匪。郡城為全臺根本，不可無大員彈壓，且附郡之大穆〔目〕降、本縣莊、崗山、羅漢門等處，介在南北之中，均離府城不遠。各處有賊匪往來出沒。奴才親督官兵居中堵禦搜捕，並為兩路軍兵接應聲援，此在郡未敢遽離之情形也。但奴才前奏，未能詳悉聲明，實屬糊塗之至。迨諸羅於正月二十二日，鳳山於二月二十一日，先後克復，殺敗賊匪，四處逃竄，復於附郡村莊，潛聚滋擾。奴才派撥官兵，嚴密擒捕。而諸羅之大武壟、礁〔噍〕吧哖各莊，仍有匪黨聚集。該處山路極為險峻，現在整兵進剿，日內督臣常青到臺灣，奴才即親率官兵到處剿捕。掃除之後，隨赴諸羅督同總兵柴大紀進攻斗六門、沙連等處，繼至彰化，會同總兵普吉保等攻剿大里杙賊巢，務期生擒逆首林爽文，解京究辦。並剿盡匪夥，斷不敢稍有遲延觀望，自取罪戾。至奴才染患風症，前在內地時發時愈，一聞臺灣逆匪肆擾，即奏明力疾東渡。自到臺灣，因機務焦迫，心神倍覺恍惚，氣力日見頹憊，惟念職任海疆，只當竭盡駑駘。是以自內地及到臺灣，均未敢將病症據實奏明。茲蒙睿示周詳，奴才感激涕零之下，彌覺悚惶無地，惟有謹遵聖訓，躬率士卒，奮勉剿匪，淨盡根株，以期克日蕆事，仰慰宸衷懸注之至意。所有欽奉上諭遵辦緣由，理合恭摺由驛四百里覆奏，伏乞皇上睿鑒。謹奏。<br><br>乾隆五十二年三月初七日<br>乾隆五十二年四月初三日奉硃批：一味飾詞，常青查奏。欽此。【本文原收錄於軍錄】</span>`;

  var zhuOrigBody = String.raw`<span class="doc-dim">福建水師提督一等海澄公奴才<mark data-group="identity">黃仕簡</mark>謹奏，為奏聞事。竊照臺灣賊匪攻城殺官，奴才聞報，隨即派調官兵船隻，力疾帶領登舟東渡進剿，並將接准臺灣鎮道初報情形，均經恭摺具奏。自十二月十五日出口，連日俱遇頂頭暴風，狂浪洶湧但臺郡急望救援，奴才日夜在洋，親督各船敲銭駕駛，衝風觸浪，不避艱危，仰蒙皇上福庇，所帶官兵船隻，倖俱保固，於正月初三夜，趕潮進入鹿耳門。初四早，登岸進城。所有督臣派調水陸官兵內，海壇鎮總兵郝壯猷，及臺灣水師協副將丁朝雄、署福州城守副將事長福、營參將那穆素里，亦於是日到臺。查賊匪林爽文、王芬等糾夥謀為不軌，先於上年十一月二十七日夜，猝攻北路大墩營盤，所有訪拿會匪之北路協副將赫生額、臺灣鎮標中營遊擊耿世文、彰化縣知縣俞峻先被殺害。又於十一月二十九日，匪黨數千攻彰化縣，因存城兵力單薄不敵，縣城被陷。臺灣府知府孫景燧、理番同知長庚、前署彰化縣劉亨基、署典史馮啟宗、北路協都司王宗武，俱被殺害。十二月初六日，攻陷諸羅縣城。攝諸羅縣俸滿臺防同知董啟埏、臺灣鎮標左營遊擊李中揚、諸羅守備郝輝龍、典史鐘燕超俱同日被害。賊夥蔓延，擾及淡水，十二月十三日，南路賊匪復攻陷鳳山縣城，知縣湯大奎自刎盡難。典史史謙被害。賊眾連結，迫攻府城。臺灣鎮總兵柴大紀督率官兵堵禦，臺灣道永福等招募鄉勇義民，協同官兵守禦。自十二月初九、初十、十三、十六、十九、二十六、三十等日，打仗殺死賊匪甚多，並有生擒賊犯，搶獲刀鋅各器械。逆賊散而復聚，甚屬猖獗，此先後據報之情形也。察看臺灣五方雜處，逆匪於光天化日之下，膽敢恣行不法，罪大惡極，莫此為甚。但此等多係無籍匪徒，烏合聚眾，其間或被迫脅隨行者自必不少，是欲殲其渠魁，必亟散其黨羽奴才先經飛檄，示知臺地民人，現在帶領官兵進剿，凡被賊匪迫脅隨行者，速須解散，無致悉被刑誅，嚴切曉示在案。先聞賊匪於正月初四、五等日，要來再攻郡城，迨奴才統領官兵到臺，初四、初五等日，逆賊不敢復來迫攻。緣郡城最關緊要，奴才隨將到臺官兵，先即一面分派四路堵截，嚴加保固府城，一面相機發兵進剿。日內陸路提臣任承恩亦即續帶官兵及金門、南澳、銅山等標營兵丁到臺，自可調度分發，南北夾攻，以期速殲逆賊，痛加剿洗，重治收復各縣城池，綏靖海疆。所有奴才到臺查辦情形，合先恭摺由驛六百里奏聞，伏乞皇上睿鑒。謹<br><br></span><span class="doc-focus"><mark data-group="identity">乾隆五十二年正月初五日</mark><br>乾隆五十二年二月十三日<mark data-group="marker">奉硃批</mark>：<mark data-group="quote">所奏已遲，早有旨諭。</mark>欽此。【本文原收錄於軍錄】</span>`;

  var entries = [
    {
      id: 'marker', index: '01', title: '「奉硃批」等引述標記',
      summary: '首先，官員通常會使用「奉硃批」、「奉到硃批」、「敬奉硃批」、「欽奉硃批」或「蒙硃批」等引述標記，接著引用硃批原文。平台會從奏摺中擷取標記、硃批引文、硃批收訖日期，以及奏摺所提及的較早奏摺名稱和日期。',
      skill: '<div class="skill-row skill-heading"><span class="md-kw">## 3. Citation (引述標記)</span></div>' +
        '<div class="skill-row skill-lead">擷取奏摺中的硃批引述標記：</div>' +
        '<div class="skill-row skill-highlight"><mark class="code-mark" data-group="marker">「奉硃批」／「奉到硃批」／「敬奉硃批」／「欽奉硃批」／「蒙硃批」</mark></div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">Python 擷取</span>：從原始奏摺擷取標記、硃批引文及所提及之較早奏摺名稱。</div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">AI 判斷</span>：比對其後的硃批引文，確認奏摺確實引用前置硃批。</div>'
    },
    {
      id: 'identity', index: '02', title: '同一官員較早發出',
      summary: '系統篩選候選文書的第一項條件：候選文書必須由同一名官員較早發出，並載有硃批。',
      skill: '<div class="skill-row skill-heading"><span class="md-kw">## 1. Identity (官員身分)</span></div>' +
        '<div class="skill-row skill-lead">確認硃批所載之奏摺官員同一性：</div>' +
        '<div class="skill-row skill-highlight"><mark class="code-mark" data-group="identity">同一官員：硃批應在該官員較早發出的奏摺上，而現在的奏摺正在引用它</mark></div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">官員比對</span>：具奏官員（如水師提督黃仕簡）必須前後一致。</div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">時間先後</span>：被引用的原奏發送日期必早於當前覆奏日期。</div>'
    },
    {
      id: 'quote', index: '03', title: '引號中的硃批文字',
      summary: '系統篩選候選文書的第三項條件：回應奏摺引號中的硃批文字，必須與候選文書的硃批原文完全或大致相同。',
      skill: '<div class="skill-row skill-heading"><span class="md-kw">## 3. Citation (硃批引文)</span></div>' +
        '<div class="skill-row skill-lead">比對奏摺引用的硃批原文內容：</div>' +
        '<div class="skill-row skill-highlight"><mark class="code-mark" data-group="quote">硃批引文：擷取引號「」內、與候選硃批相符的文字</mark></div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">逐字比對</span>：比對奏摺所引硃批（如「所奏已遲，早有旨諭」）與原件硃批。</div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">配對確認</span>：引文精確相符時建立高置信度硃批通信鏈。</div>'
    }
  ];

  /* ==========================================================================
     Mobile / narrow layout (<= 860px)
     ========================================================================== */
  var mobileBuilt = false;
  function buildMobile() {
    if (mobileBuilt || list.dataset.reqBuilt === 'true') return;
    mobileBuilt = true;

    function docWindow(type) {
      var isReply = type === 'reply';
      var body = isReply ? zhuReplyBody : zhuOrigBody;
      var title = isReply ? '為屢接上諭覆奏現在攻戰情形事' : '為奏聞統兵到臺查辦及兵力布置情形事';
      var meta = isReply
        ? ['黃仕簡（福建水師提督）', '乾隆52年3月7日上奏', '乾隆52年4月3日硃批', '明清台檔31，頁64']
        : ['黃仕簡（福建水師提督）', '乾隆52年1月5日上奏', '乾隆52年2月13日硃批', '明清台檔30，頁320'];
      var panel = window.part2DocPanel;
      return panel.create({
        outerClass: 'req-win req-win-doc',
        dataReqDoc: isReply ? 'zhu' : 'yu',
        badge: '硃',
        badgeClass: 'b-zhu',
        title: title,
        metaLines: meta,
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
          '<div class="req-win req-win-skill" data-req-skill><div class="agentic-mac-titlebar"><span class="agentic-mac-dot red"></span><span class="agentic-mac-dot yellow"></span><span class="agentic-mac-dot green"></span><span class="agentic-window-title">zhu-response-pairing.md</span></div><div class="req-vscode-shell"><div class="req-vscode-activitybar"><span>▦</span><span>⌕</span><span>⑂</span><span>▣</span><span>⚙</span></div><div class="req-vscode-editor"><div class="req-vscode-tabs"><span class="req-vscode-tab">zhu-response-pairing.md</span></div><div class="req-vscode-body" data-req-body>' + entry.skill + '</div></div></div></div>' +
          '<span class="req-connector" data-req-connector="1" aria-hidden="true">→</span>' + docWindow('reply') +
          '<span class="req-connector" data-req-connector="2" aria-hidden="true">→</span>' + docWindow('orig') +
        '</div></div></div></div></div>';
      return el;
    }

    entries.forEach(function (entry) { list.appendChild(buildEntry(entry)); });
    list.dataset.reqBuilt = 'true';
    var docPanel = window.part2DocPanel;

    var items = Array.prototype.slice.call(root.querySelectorAll('[data-req-item]')).map(function (el) {
      var stage = el.querySelector('[data-req-stage]');
      var skillWin = el.querySelector('[data-req-skill]');
      var zhuWin = el.querySelector('[data-req-doc="zhu"]');
      var yuWin = el.querySelector('[data-req-doc="yu"]');
      var bodies = {
        skill: skillWin.querySelector('[data-req-body]'),
        zhu: zhuWin.querySelector('[data-req-body]'),
        yu: yuWin.querySelector('[data-req-body]')
      };
      Object.keys(bodies).forEach(function (k) { bodies[k].dataset.original = bodies[k].innerHTML; });
      return {
        id: el.getAttribute('data-req-item'), el: el, card: el.querySelector('[data-req-card]'), bar: el.querySelector('[data-req-bar]'),
        panel: el.querySelector('[data-req-panel]'), wordcard: el.querySelector('[data-req-wordcard]'), stageWrap: el.querySelector('[data-req-stage-wrap]'),
        stage: stage, wins: [skillWin, zhuWin, yuWin], connectors: [el.querySelector('[data-req-connector="1"]'), el.querySelector('[data-req-connector="2"]')], bodies: bodies, timers: []
      };
    });

    function resetItem(item) {
      item.timers.forEach(function (t) { clearTimeout(t); clearInterval(t); }); item.timers = [];
      item.card.classList.remove('is-open'); item.panel.classList.remove('is-open'); item.stageWrap.classList.remove('is-open'); item.wordcard.classList.remove('is-shown');
      item.wins.forEach(function (w) { w.classList.remove('is-shown'); if (docPanel) docPanel.reset(w); }); item.connectors.forEach(function (c) { c.classList.remove('is-shown'); });
      Object.keys(item.bodies).forEach(function (k) { item.bodies[k].innerHTML = item.bodies[k].dataset.original; item.bodies[k].scrollTop = 0; });
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
    }
    function closeItem(item) { item.el.classList.remove('is-open'); item.bar.setAttribute('aria-expanded', 'false'); resetItem(item); }
    function openItem(item) {
      items.forEach(function (other) { if (other !== item && other.el.classList.contains('is-open')) closeItem(other); });
      resetItem(item); item.el.classList.add('is-open'); item.bar.setAttribute('aria-expanded', 'true');
      item.card.classList.add('is-open'); item.stageWrap.classList.add('is-open');
      item.wins.forEach(function (w) { w.classList.add('is-shown'); });
      item.connectors.forEach(function (c) { c.classList.add('is-shown'); });
      activateGroup(item, item.id);
      item.panel.classList.add('is-open');
      item.wordcard.classList.add('is-shown');
    }
    items.forEach(function (item) {
      item.bar.addEventListener('click', function () { if (item.el.classList.contains('is-open')) closeItem(item); else openItem(item); });
      item.stage.addEventListener('click', function (e) { var mark = e.target.closest('mark[data-group]'); if (mark) activateGroup(item, mark.getAttribute('data-group')); });
      if (docPanel) docPanel.bindAll(item.wins);
    });
  }

  /* ==========================================================================
     Desktop layout (> 860px)
     ========================================================================== */
  var DESKTOP_MARKUP =
    '<div class="replica-shell">' +
      '<div data-part1 data-part1-data="PART1_INTERFACE_DATA_ZHU_RESPONSE" data-part1-chart-scale="1.25"><div class="part1-replica" data-part1-replica></div></div>' +
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
                '<span class="req-skill-title-text">zhu-response-pairing.md</span>' +
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
    '#part-2-content #part-2-zhu-response [data-req-idle-wrap], #part-2-content #part-2-zhu-response .req-idle-skill { display: none !important; }',
    '#part-2-content #part-2-zhu-response { padding-top: 0 !important; padding-left: clamp(2px, 0.8vw, 14px) !important; padding-right: clamp(2px, 0.8vw, 14px) !important; }',
    '#part-2-content #part-2-zhu-response > .part2-substage-cover, #part-2-zhu-response .part2-substage-cover { padding-top: 24px !important; padding-bottom: 20px !important; margin-top: 0 !important; margin-bottom: 0 !important; }',
    '#part-2-content #part-2-zhu-response > .story-inner, #part-2-content #part-2-zhu-response > .part2-zhu-response-story-inner { width: 100% !important; max-width: 100% !important; margin: 0 !important; padding-top: 0 !important; }',
    '#part-2-zhu-response .req-desktop-tool { margin: 12px 0 0 !important; width: 100%; }',
    '#part-2-zhu-response .replica-shell { width: 100%; background: #f1eadc; border: 1px solid #d8cdbb; border-radius: 6px; box-shadow: 0 13px 30px rgba(47,57,52,.15); overflow: hidden; --stage-dock-pct: 50%; }',
    '#part-2-zhu-response .replica-shell .part1-replica { --font-scale: 1; }',
    '#part-2-zhu-response .replica-stage { padding: 6px; gap: 8px; height: clamp(640px, 72vh, 800px); }',

    /* description panel sits BELOW the visual */
    '#part-2-zhu-response .req-desc { display: flex; flex-direction: column; margin: 18px 0 0; background: var(--card); border: 1px solid #d8cdbb; border-radius: 6px; box-shadow: 0 8px 24px rgba(47,57,52,.1); overflow: hidden; }',
    '#part-2-zhu-response .req-desc-head { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; padding: 13px 20px 11px; border-bottom: 1px solid var(--line); background: rgba(244,239,230,.4); }',
    '#part-2-zhu-response .req-desc .req-desc-index { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 30px; height: 30px; color: #fffaf2; background: #8a7c66; border-radius: 50%; font: 800 13px/1 var(--sans); }',
    '#part-2-zhu-response .req-desc[data-active-req="marker"] .req-desc-index { background: rgb(var(--hl-marker)) !important; }',
    '#part-2-zhu-response .req-desc[data-active-req="identity"] .req-desc-index { background: rgb(var(--hl-author)) !important; }',
    '#part-2-zhu-response .req-desc[data-active-req="quote"] .req-desc-index { background: rgb(var(--hl-quote)) !important; }',
    '#part-2-zhu-response .req-desc-head h3 { flex: 1; min-width: 160px; margin: 0; color: var(--ink); font: 700 calc(18px * var(--font-scale, 1))/1.35 var(--serif); }',
    '#part-2-zhu-response .req-desc-body { padding: 16px 20px 18px; }',

    /* 50% / 50% split layout */
    '#part-2-zhu-response .req-desc-split { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: stretch; width: 100%; }',
    '#part-2-zhu-response .req-desc-text-panel { display: flex; flex-direction: column; justify-content: center; min-width: 0; padding: 4px 0; height: 100%; }',
    '#part-2-zhu-response .req-desc .req-wordcard { display: flex; flex-direction: column; justify-content: center; height: 100%; border-top: none !important; padding-top: 0 !important; margin: 0 !important; opacity: 1 !important; transform: none !important; }',
    '#part-2-zhu-response .req-desc .req-wordcard p { margin: 0; color: var(--text); font: 500 calc(18px * var(--font-scale, 1))/1.85 var(--serif); text-align: justify; }',
    '#part-2-zhu-response .req-desc-head h3, #part-2-zhu-response .req-desc .req-wordcard p { font-size: calc(18px * var(--font-scale, 1)) !important; }',

    /* Right Skills Window: 50% width, matches text card height */
    '#part-2-zhu-response .req-desc-skill-panel { display: flex; flex-direction: column; min-width: 0; height: 100%; }',
    '#part-2-zhu-response .req-win-skill-box { display: flex; flex-direction: column; height: 100%; min-height: max-content; background: #1e1e1e; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,.18), 0 0 0 1px rgba(255,255,255,.07) inset; }',
    '#part-2-zhu-response .req-skill-titlebar { display: flex; align-items: center; gap: 6px; padding: 8px 12px; background: #252526; border-bottom: 1px solid #333333; flex: none; }',
    '#part-2-zhu-response .req-mac-dot { width: 8.5px; height: 8.5px; border-radius: 50%; flex: none; }',
    '#part-2-zhu-response .req-mac-dot.red { background: #ff5f57; }',
    '#part-2-zhu-response .req-mac-dot.yellow { background: #febc2e; }',
    '#part-2-zhu-response .req-mac-dot.green { background: #28c840; }',
    '#part-2-zhu-response .req-skill-title-text { margin-left: 5px; color: #b5b5b5; font: 600 calc(12px * var(--font-scale, 1))/1 "SF Mono", ui-monospace, Menlo, Consolas, monospace; letter-spacing: .02em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex: 1; }',

    '#part-2-zhu-response .req-skill-shell { display: grid; grid-template-columns: 26px 1fr; flex: 1 1 auto; height: 100%; min-height: max-content; background: #1e1e1e; }',
    '#part-2-zhu-response .req-skill-activitybar { display: flex; flex-direction: column; align-items: center; gap: 12px; padding: 16px 0; color: #707070; background: #2b2b2b; font: 10.5px/1 var(--sans); border-right: 1px solid #383838; user-select: none; height: 100%; }',
    '#part-2-zhu-response .req-skill-editor { display: flex; flex-direction: column; min-width: 0; min-height: max-content; height: 100%; }',
    '#part-2-zhu-response .req-skill-body { flex: 1 1 auto; height: auto; min-height: max-content; overflow: visible !important; padding: 18px 18px 20px; color: #d4d4d4; font: 500 calc(15px * var(--font-scale, 1))/1.75 "SF Mono", ui-monospace, Menlo, Consolas, monospace; word-break: break-word; scrollbar-width: none; }',
    '#part-2-zhu-response .req-skill-body::-webkit-scrollbar { display: none; }',
    '#part-2-zhu-response .req-skill-body .skill-row { margin-bottom: 7px; }',
    '#part-2-zhu-response .req-skill-body .skill-row:last-child { margin-bottom: 0; }',
    '#part-2-zhu-response .req-skill-body .skill-heading { font-weight: 700; color: #4fc1ff; margin-bottom: 10px; font-size: calc(13.5px * var(--font-scale, 1)); }',
    '#part-2-zhu-response .req-skill-body .skill-lead { margin-bottom: 6px; }',
    '#part-2-zhu-response .req-skill-body .skill-highlight { margin: 8px 0 9px; }',
    '#part-2-zhu-response .req-skill-body .skill-bullet { margin-bottom: 7px; }',
    '#part-2-zhu-response .req-skill-body .md-kw { color: #4fc1ff; font-weight: 600; }',
    '#part-2-zhu-response .req-skill-body .md-bullet { color: #9cdcfe; font-weight: bold; margin-right: 4px; }',

    /* Highlight in skill window */
    '#part-2-zhu-response .req-skill-body mark.code-mark { display: inline-block; padding: 2px 7px; border-radius: 4px; color: #ffffff !important; font-weight: 600; line-height: 1.45; box-decoration-break: clone; -webkit-box-decoration-break: clone; }',
    '#part-2-zhu-response .req-desc[data-active-req="marker"] .req-skill-body mark.code-mark[data-group="marker"] { background: rgba(var(--hl-marker), .85) !important; box-shadow: 0 0 0 1px rgba(var(--hl-marker), 1); }',
    '#part-2-zhu-response .req-desc[data-active-req="identity"] .req-skill-body mark.code-mark[data-group="identity"] { background: rgba(var(--hl-author), .88) !important; box-shadow: 0 0 0 1px rgba(var(--hl-author), 1); }',
    '#part-2-zhu-response .req-desc[data-active-req="quote"] .req-skill-body mark.code-mark[data-group="quote"] { background: rgba(var(--hl-quote), .85) !important; box-shadow: 0 0 0 1px rgba(var(--hl-quote), 1); }',

    '#part-2-zhu-response .req-nav { display: flex; align-items: center; gap: 6px; margin-left: auto; }',
    '#part-2-zhu-response .req-nav-arrow { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; color: var(--ink); background: transparent; border: 1px solid var(--line); border-radius: 50%; cursor: pointer; transition: background .15s ease, color .15s ease; }',
    '#part-2-zhu-response .req-nav-arrow:hover { color: #fffaf2; background: var(--accent); border-color: var(--accent); }',

    /* Match 2.1: the replica toolbar is a faded, non-interactive visual header. */
    '#part-2-zhu-response .replica-shell .part1-toolbar { pointer-events: none !important; background: transparent !important; border-bottom-color: transparent !important; }',
    '#part-2-zhu-response .replica-shell .part1-toolbar * { pointer-events: none !important; cursor: default !important; }',
    '#part-2-zhu-response .replica-shell .part1-toolbar button, #part-2-zhu-response .replica-shell .part1-toolbar select, #part-2-zhu-response .replica-shell .part1-toolbar input { opacity: .45; }',
    '#part-2-zhu-response .replica-shell .part1-toolbar [data-type-pop], #part-2-zhu-response .replica-shell .part1-toolbar [data-tools-pop] { display: none !important; }',

    /* doc panels */
    '#part-2-zhu-response .replica-shell { --site-font-scale: var(--font-scale, 1); }',
    '#part-2-zhu-response .part1-replica { --font-scale: var(--site-font-scale) !important; --body-font-scale: var(--site-font-scale) !important; }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-dock { grid-template-columns: 1fr !important; }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-doc-stack { grid-template-columns: calc(var(--pair-left-pct, 50%) - 5px) 10px calc(var(--pair-right-pct, 50%) - 5px) !important; gap: 0 !important; }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-doc-head { padding: 14px 16px 12px; background: linear-gradient(#fffdf8, #f3eada); border-bottom: 1px solid #e1d8c9; }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-doc-head .part1-doc-title, #part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-doc-title, #part-2-zhu-response .part1-replica[data-pair-doc="true"] [data-doc-panel-title] { font: 700 calc(18px * var(--font-scale, 1))/1.35 var(--serif) !important; color: #2d261d !important; letter-spacing: .02em; margin: 0 0 6px; }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .badge, #part-2-zhu-response .part1-replica[data-pair-doc="true"] [data-doc-panel-badge] { display: inline-block; width: auto; height: auto; margin-right: 6px; padding: 2px 7px; color: #fffaf2; background: #c46a2b; border-radius: 6px; font: 800 calc(13px * var(--font-scale, 1))/1.1 var(--sans) !important; vertical-align: 1px; }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-doc-meta { margin: 0; color: #7a6f63; font: 500 calc(13px * var(--font-scale, 1))/1.55 var(--sans); line-height: 1.55; }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-doc-section-label { font-size: calc(17px * var(--font-scale)); }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-doc-body { font-size: calc(18px * var(--font-scale)); }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-doc-window-controls { display: none !important; }',
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-doc-title { padding-right: 0 !important; }',

    '#part-2-zhu-response .req-pair-resize { position: relative; z-index: 6; cursor: ew-resize; touch-action: none; user-select: none; }',
    '#part-2-zhu-response .req-pair-resize::before { content: ""; position: absolute; top: 38%; bottom: 38%; left: 4px; width: 2px; border-radius: 2px; background: #d1c2ad; opacity: .7; transition: background .15s ease, opacity .15s ease, transform .15s ease; }',
    '#part-2-zhu-response .req-pair-resize:hover::before, #part-2-zhu-response .req-pair-resize:focus-visible::before, #part-2-zhu-response .req-pair-resize.is-dragging::before { background: #a67d4f; opacity: 1; transform: scaleX(1.8); }',
    '#part-2-zhu-response .req-pair-resize:focus-visible { outline: 2px solid rgba(166,125,79,.45); outline-offset: -1px; }',

    /* floating clue bubble */
    '#part-2-zhu-response .part1-replica[data-pair-doc="true"] .part1-pair-doc { position: relative; }',
    '#part-2-zhu-response .req-float-bubble { position: absolute; left: 0; top: 0; z-index: 30; display: flex; align-items: center; gap: 8px; height: 38px; max-width: calc(100% - 16px); padding: 5px 12px 5px 6px; color: #241d12; background: #fffdf8; border: 2px solid rgb(var(--bc, var(--hl-marker))); border-radius: 999px; box-shadow: 0 8px 18px rgba(30,22,10,.22); font: 700 10px/1 var(--sans); white-space: nowrap; transition: opacity .15s ease, left .12s ease, top .12s ease; }',
    '#part-2-zhu-response .req-float-bubble[data-bubble-group="marker"] { --bc: var(--hl-marker); }',
    '#part-2-zhu-response .req-float-bubble[data-bubble-group="identity"] { --bc: var(--hl-author); }',
    '#part-2-zhu-response .req-float-bubble[data-bubble-group="quote"] { --bc: var(--hl-quote); }',
    '#part-2-zhu-response .req-float-bubble.req-float-hidden { opacity: 0; pointer-events: none; }',
    '#part-2-zhu-response .req-float-num { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 24px; height: 24px; color: #fffdf8; background: rgb(var(--bc)); border-radius: 50%; font: 800 13px/1 var(--sans); }',
    '#part-2-zhu-response .req-float-title { flex: 1 1 auto; min-width: 0; padding: 0 4px; overflow: hidden; text-overflow: ellipsis; color: #241d12; font: 800 calc(14.5px * var(--font-scale, 1))/1.35 var(--serif); }',
    '#part-2-zhu-response .req-float-arrow { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 22px; height: 22px; color: rgb(var(--bc)); background: transparent; border: 1.5px solid rgba(var(--bc),.5); border-radius: 50%; cursor: pointer; font: 700 13px/1 var(--sans); transition: background .15s ease; }',
    '#part-2-zhu-response .req-float-arrow:hover { background: rgba(var(--bc),.16); }',
    '#part-2-zhu-response .req-float-tail { position: absolute; left: 50%; bottom: -7px; width: 13px; height: 13px; background: #fffdf8; border-right: 2px solid rgb(var(--bc, var(--hl-marker))); border-bottom: 2px solid rgb(var(--bc, var(--hl-marker))); transform: translateX(-50%) rotate(45deg); border-radius: 0 0 3px 0; }',
    '#part-2-zhu-response .req-float-bubble.req-float-flip .req-float-tail { bottom: auto; top: -7px; border-right: 0; border-bottom: 0; border-left: 2px solid rgb(var(--bc, var(--hl-marker))); border-top: 2px solid rgb(var(--bc, var(--hl-marker))); border-radius: 3px 0 0 0; }',

    /* highlight marks */
    '#part-2-zhu-response .part1-pair-doc .part1-doc-body mark[data-group] { padding: 2px 4px; border-radius: 3px; box-decoration-break: clone; -webkit-box-decoration-break: clone; color: inherit !important; background: transparent !important; cursor: pointer; transition: background-color .15s ease, color .15s ease; }',
    '#part-2-zhu-response .part1-pair-doc .part1-doc-body mark[data-group]:hover { filter: brightness(.92); }',
    '#part-2-zhu-response .req-desktop-tool[data-active-req="marker"] .part1-pair-doc .part1-doc-body mark[data-group="marker"], #part-2-zhu-response .req-desktop-tool[data-active-req="marker"] .part1-pair-doc .part1-doc-body mark[data-group="marker"].is-active { background: #3ee0cf !important; color: #043834 !important; font-weight: 600; box-shadow: 0 0 0 1px rgba(35, 195, 180, .4); }',
    '#part-2-zhu-response .req-desktop-tool[data-active-req="identity"] .part1-pair-doc .part1-doc-body mark[data-group="identity"], #part-2-zhu-response .req-desktop-tool[data-active-req="identity"] .part1-pair-doc .part1-doc-body mark[data-group="identity"].is-active { background: #d896ff !important; color: #23043d !important; font-weight: 600; box-shadow: 0 0 0 1px rgba(170, 80, 225, .4); }',
    '#part-2-zhu-response .req-desktop-tool[data-active-req="quote"] .part1-pair-doc .part1-doc-body mark[data-group="quote"], #part-2-zhu-response .req-desktop-tool[data-active-req="quote"] .part1-pair-doc .part1-doc-body mark[data-group="quote"].is-active { background: #ff9370 !important; color: #3e1204 !important; font-weight: 600; box-shadow: 0 0 0 1px rgba(225, 90, 50, .4); }',
    '#part-2-zhu-response .part1-pair-doc .part1-doc-body mark[data-group].is-active { animation: part2-yu-response-hl-flash .5s ease-out; }',

    /* doc dim and focus */
    '#part-2-zhu-response .part1-pair-doc .doc-dim { opacity: 0.35; transition: opacity .2s ease; }',
    '#part-2-zhu-response .part1-pair-doc .doc-dim:hover { opacity: 0.72; }',
    '#part-2-zhu-response .part1-pair-doc .doc-focus { opacity: 1; color: #18120b; font-weight: 500; }',
    '#part-2-zhu-response .part1-pair-doc mark[data-group] { opacity: 1 !important; }',

    /* chart links */
    '#part-2-zhu-response .part1-chart-links .part1-bg-link { opacity: 0.22 !important; pointer-events: none !important; }',
    '#part-2-zhu-response .part1-chart-links .req-chart-link, #part-2-zhu-response .part1-chart-links .part1-example-link { transition: opacity .2s ease, stroke-width .2s ease; cursor: pointer; pointer-events: stroke; }',
    '#part-2-zhu-response .part1-chart-links .req-chart-link { opacity: .88 !important; stroke-width: 4 !important; }',
    '#part-2-zhu-response .part1-chart-links .req-chart-link.is-active { opacity: 1 !important; stroke-width: 4.8 !important; }',

    '@media (max-width: 860px) { #part-2-zhu-response .req-desc-split { grid-template-columns: 1fr; gap: 10px; } }',
    '@media (max-width: 900px) { #part-2-zhu-response .req-float-title { display: none; } }'
  ].join('\n');

  var desktopBuilt = false;
  var desktopWrap = null;
  var desktopSetActive = null;

  function buildDesktopDataClone() {
    var GLOBAL_NAME = 'PART1_INTERFACE_DATA_ZHU_RESPONSE';
    var base = window.PART1_INTERFACE_DATA;
    if (!base) return null;
    var docMap = new Map((base.documents || []).map(function (rec) { return [rec.docId, rec]; }));
    var zhuReply = docMap.get('硃297') || {
      docId: '硃297', docType: '硃批', title: '為屢接上諭覆奏現在攻戰情形事',
      author: { position: '福建水師提督', name: '黃仕簡' },
      compiledIn: { book: 31, volume: 31, page: 64 },
      sendDate: ['乾隆五十二年三月七日', '1787/03/07'], receiveDate: ['乾隆五十二年四月三日', '1787/04/03'],
      rescriptText: '一味飾詞，常青查奏。欽此。'
    };
    var zhuOrig = docMap.get('硃155') || {
      docId: '硃155', docType: '硃批', title: '為奏聞統兵到臺查辦及兵力布置情形事',
      author: { position: '福建水師提督', name: '黃仕簡' },
      compiledIn: { book: 30, volume: 30, page: 320 },
      sendDate: ['乾隆五十二年一月五日', '1787/01/05'], receiveDate: ['乾隆五十二年二月十三日', '1787/02/13'],
      rescriptText: '所奏已遲，早有旨諭。欽此。'
    };

    var EXAMPLE_NODE_IDS = ['doc-硃155-L', 'doc-硃155-R', 'doc-硃297-L'];
    var clone = Object.assign({}, base);
    clone.document = zhuReply;
    clone.documents = [zhuOrig];
    clone.pairDoc = true;

    // Filter out all blue circle dots (shangzou documents), retaining other nodes identical to 2.1
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

    // Active foreground links: 1st dot (原奏) -> 2nd dot on 3rd line (皇帝硃批) -> 3rd dot (覆奏)
    var activeLinks = [
      {
        id: 'example-link-zhu155L-to-155R',
        from: 'doc-硃155-L',
        to: 'doc-硃155-R',
        className: 'part1-preview-link req-chart-link',
        color: '#c45d38',
        width: 2.8,
        background: false,
        title: '硃155 原奏 (第2線) ↔ 硃155 硃批 (第3線)'
      },
      {
        id: 'example-link-zhu155R-to-297L',
        from: 'doc-硃155-R',
        to: 'doc-硃297-L',
        className: 'part1-preview-link req-chart-link',
        color: '#c45d38',
        width: 2.8,
        background: false,
        title: '硃155 硃批 (第3線) ↔ 硃297 覆奏 (第2線)'
      }
    ];

    clone.chartPreview = Object.assign({}, base.chartPreview, {
      nodes: nodes,
      links: bgLinks.concat(activeLinks)
    });
    window[GLOBAL_NAME] = clone;
    return GLOBAL_NAME;
  }

  var DESKTOP_STYLE_ID = 'part2-zhu-response-desktop-style';
  function ensureDesktopStyle() {
    if (document.getElementById(DESKTOP_STYLE_ID)) return;
    var style = document.createElement('style');
    style.id = DESKTOP_STYLE_ID;
    style.textContent = DESKTOP_CSS;
    document.head.appendChild(style);
  }

  function setupDesktopOverlay(wrap) {
    var GROUP_ORDER = entries.map(function (e) { return e.id; });
    var activeId = GROUP_ORDER[0];
    var floatBubble = null;

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
        '<span class="req-float-num" data-req-float-num>1</span>' +
        '<span class="req-float-title" data-req-float-title></span>' +
        '<button type="button" class="req-float-arrow" data-bubble-prev aria-label="上一項線索">‹</button>' +
        '<button type="button" class="req-float-arrow" data-bubble-next aria-label="下一項線索">›</button>' +
        '<span class="req-float-tail" aria-hidden="true"></span>';
      leftPanel.appendChild(bubble);
      floatBubble = bubble;

      var scrollEl = leftPanel.querySelector('[data-doc-scroll]');
      if (scrollEl) scrollEl.addEventListener('scroll', positionBubble);
      if ('ResizeObserver' in window) new ResizeObserver(positionBubble).observe(leftPanel);
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(positionBubble);
    }

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
      handle.setAttribute('tabindex', '0');
      handle.setAttribute('aria-label', '調整兩份文書面板的寬度比例');
      stack.insertBefore(handle, panels[1]);

      var leftPct = 50;
      function apply() {
        stack.style.setProperty('--pair-left-pct', leftPct + '%');
        stack.style.setProperty('--pair-right-pct', (100 - leftPct) + '%');
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

    function setActive(groupId, opts) {
      opts = opts || {};
      activeId = groupId;
      var idx = GROUP_ORDER.indexOf(groupId);
      if (idx === -1) idx = 0;
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
        line.classList.toggle('is-active', true);
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
    });
    var navPrev = wrap.querySelector('[data-nav-prev]');
    var navNext = wrap.querySelector('[data-nav-next]');
    if (navPrev) navPrev.addEventListener('click', function () { goTo(-1); });
    if (navNext) navNext.addEventListener('click', function () { goTo(1); });

    function centerPairLine() {
      var scrollEl = wrap.querySelector('[data-chart-scroll]');
      if (!scrollEl) return;
      var n1 = wrap.querySelector('[data-chart-node-id="doc-硃155-L"]');
      var n2 = wrap.querySelector('[data-chart-node-id="doc-硃155-R"]');
      var n3 = wrap.querySelector('[data-chart-node-id="doc-硃297-L"]');
      // Keep the first highlighted relationship pair in view.  The third
      // node remains in the scrollable chain, but centering all three at once
      // would leave fewer than two endpoint dots visible at the enlarged scale.
      var nodes = [n1, n2].filter(Boolean);
      if (!nodes.length) return;
      var sr = scrollEl.getBoundingClientRect();
      var sumX = 0, sumY = 0;
      nodes.forEach(function (n) {
        var r = n.getBoundingClientRect();
        sumX += (r.left + r.right) / 2;
        sumY += (r.top + r.bottom) / 2;
      });
      var midX = sumX / nodes.length;
      var midY = sumY / nodes.length;
      var tx = scrollEl.scrollLeft + midX - (sr.left + sr.width / 2);
      var ty = scrollEl.scrollTop + midY - (sr.top + sr.height / 2);
      scrollEl.scrollTo({ left: tx, top: ty, behavior: 'auto' });
    }

    var centerTimer = 0;
    function scheduleCenter() {
      if (centerTimer) return;
      centerTimer = window.setTimeout(function () {
        centerTimer = 0;
        requestAnimationFrame(function () { centerPairLine(); positionBubble(); });
      }, 350);
    }
    window.addEventListener('resize', scheduleCenter);

    var tabPanel = root.closest('[data-tab-panel]');
    if (tabPanel && 'MutationObserver' in window) {
      new MutationObserver(function () {
        if (!tabPanel.hidden) scheduleCenter();
      }).observe(tabPanel, { attributes: true, attributeFilter: ['hidden'] });
    }

    var dataClone = window.PART1_INTERFACE_DATA_ZHU_RESPONSE;
    if (dataClone) {
      dataClone.onPairInit = function (records) {
        records.forEach(function (record, i) {
          var panel = wrap.querySelector('[data-doc-panel-doc="' + record.docId + '"]');
          if (!panel) return;
          var body = panel.querySelector('[data-doc-body]');
          if (body) body.innerHTML = i === 0 ? zhuReplyBody : zhuOrigBody;
        });
        injectFloatBubble();
        injectPairResizer();
        setActive(activeId, { skipScroll: true, openDesc: true });
        centerPairLine();
        scheduleCenter();
      };
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
      if (dataClone && dataClone.onPairInit) {
        dataClone.onPairInit([{ docId: '硃297' }, { docId: '硃155' }]);
      }
    }
    return setActive;
  }

  function buildDesktop() {
    if (desktopBuilt) return;
    if (typeof window.part1InitRoot !== 'function') return;
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

  var mq = window.matchMedia('(max-width: 860px)');
  function applyMode() {
    root.setAttribute('data-req-mode', mq.matches ? 'mobile' : 'desktop');
    if (mq.matches) {
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
