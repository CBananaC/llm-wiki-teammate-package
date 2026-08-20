(function () {
  'use strict';

  var root = document.querySelector('#part-2-yu-source');
  var list = root && root.querySelector('[data-req-list]');
  if (!root || !list) return;

  var yuBody = String.raw`<span class="doc-focus">大學士公阿、大學士和，字寄閩浙總督常、福建水師提督黃、福建提督任、福建巡撫徐，<mark data-group="dateA">乾隆五十一年十二月二十七日</mark>奉上諭：<mark data-group="markerA">據常青等奏</mark>，臺灣彰化縣匪徒林爽文等，結黨滋事，騷擾地方。知縣俞駿（峻）拿匪被害，彰化縣城被匪徒竊踞。黃仕簡已帶兵渡臺剿捕，常青同任承恩親往泉州、蚶江彈壓調度等語。</span><span class="doc-dim">本日已刻，又據徐嗣曾由六百里馳奏，接蚶江通判陳惇稟稱，昨據船戶黃斌供，有傳說賊人赴諸羅縣攻城，被官兵殺死二千餘人。又鎮道已抵彰城，賊匪俱被殺死等語。臺灣地隔重洋，民刁俗悍，屢次滋生事端。今又有彰化縣賊匪林爽文等，糾衆不法，膽敢殺害官長，攻陷城池，尤爲罪大惡極，不可不嚴行戮，以示懲創。賊匪率衆擾諸羅，即被官兵殺死二千餘名。該地方文武，所辦尚好，著黃仕簡前往該處，即行查明。如果屬實，將帶兵剿殺賊匪者系屬何人，並首先出力之員及兵丁，分析具，候朕酌量加恩，以示獎勵。再，彰化知縣會同副將前往各莊搜捕，賊匪俱已逃竄。嗣又散而復聚，竟有數千人，已致被害。該縣於搜捕賊匪後，不能嚴密防範，雖失之疏懈，但帶兵緝犯，事屬因公，倉猝被害，尚非激變者可比。並著該督撫查明該縣，如平日並無別項劣跡及激變情事，即據實奏聞，候朕降旨交部議恤。至黃仕簡甫經病癒，一聞匪犯滋事之信，即帶兵渡臺，殊屬奮勉可嘉。著賞給大荷包一對，小藥包三對，金銀三個､銀錁三個、太平錢一對，以示優眷。並著於辦理搜捕諸務外，仍加意調攝，勿過勞。至賊匪麼烏合，經諸羅官兵剿殺二千餘人，餘黨自必聞風潰散。黃仕簡到彼，督率該鎮道路夾攻，盡力堵剿，無難立就撲滅。但恐餘黨四散逸，或偷越內渡。常青、任承恩現住蚶江一帶，著嚴飭沿海口岸地方文武員，實力巡防。如有竄逸餘匪，即行擒獲審辦，最爲緊要。常青、徐嗣曾等，總須不動聲色，妥協辦理。若因外洋遇有此等案件，該督撫等紛紛調遣，跡涉張皇，轉致內地民人心生疑駭，殊有關係，該督撫不可不處以鎮定也。將此由六百里加緊各傳諭知之。仍將現在剿捕及有無續獲首夥各犯情形，迅速由六百里復奏。欽此。遵旨寄信前來。</span>`;

  var zhu21Body = String.raw`<span class="doc-focus">閩浙總督臣常青跪奏，為飛摺奏聞事。……十一月二十七夜，彰化俞知縣在大墩地方拿匪遇害，本日早彰城失陷，路途梗塞，不能前進，將原文附回。等語。卑職等立即督率兵役，扼要堵禦，現在彰化既為匪徒竊踞，通報內地文稟不能由正口直達……臣一面飛咨水師提臣黃仕簡率領本標兵一千名、金門鎮兵五百名、南澳鎮銅山營兵五百名，由鹿耳門飛渡前進……臣即於泉州駐扎，會同陸路提臣任承恩居中調度……<br><br>乾隆五十一年十二月十二日<br><mark data-group="dateA">乾隆五十一年十二月二十七日</mark>奉硃批：即有旨諭。欽此。〔本文原收錄於軍錄〕</span>`;

  var zhu22Body = String.raw`<span class="doc-focus">福建陸路提督革職留任奴才任承恩跪奏，為奏聞事。……此月二十七日夜，本縣俞在大墩地方拿匪遇害。本日早彰城失陷，路途梗塞，不能前遞……臣除一面將沿海口隘，密飭各營將弁嚴加防守，一面派撥官兵，整頓軍火器械，雇備船隻，馳商督臣，聽候調遣外……奴才挑派備戰兵丁一千名，隨帶軍火器具，於十三日分配登舟，候風放洋。協同黃仕簡戮力剿除，速靖海疆……<br><br>乾隆五十一年十二月初十日<br><mark data-group="dateA">乾隆五十一年十二月二十七日</mark>奉硃批：即有旨諭。欽此。〔本文原收錄於軍錄〕</span>`;

  /* 2.3 shows the full canonical bodies in the desktop pair panels.  Keep
     the existing source excerpts as markerA fragments inside those bodies,
     so 「據常青等奏」 still highlights the evidence in both 硃 panels. */
  var sourceMarkerFragments = {
    '硃21': [
      '閩浙總督臣常青跪奏，為飛摺奏聞事。',
      '十一月二十七夜，彰化俞知縣在大墩地方拿匪遇害。本日早彰城失陷，路途梗塞，不能前進，將原文附回。等語。',
      '卑職等立即督率兵役，扼要堵禦。現在彰化既為匪徒竊踞，通報內地文稟，不能由正口直達。',
      '臣一面飛咨水師提臣黃仕簡率領本標兵一千名、金門鎮兵五百名、南澳鎮銅山營兵五百名，由鹿耳門飛渡前進。',
      '臣即於泉州駐扎，會同陸路提臣任承恩居中調度'
    ],
    '硃22': [
      '福建陸路提督臣任承恩跪奏，為奏聞事。',
      '此月二十七日夜，本縣俞在大墩地方拿匪遇害。本日早彰城失陷，路途梗塞，不能前遞，將原文附回。',
      '卑職等立即督率兵役，募集鄉勇、社番，扼要堵御。現在彰化既為匪徒竊踞，通報內地文稟，不能由正口直達。',
      '臣除一面將沿海口隘，密飭各營將弁嚴加防守，一面派撥官兵，整頓軍火器械，雇備船隻，馳商督臣，聽候調遣外'
    ]
  };

  function sourceRecord(docId) {
    var data = window.PART1_INTERFACE_DATA;
    var records = data && Array.isArray(data.documents) ? data.documents : [];
    return records.find(function (record) { return String(record.docId) === String(docId); }) || null;
  }

  function escapeSourceHtml(value) {
    return String(value).replace(/[&<>"']/g, function (char) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char];
    });
  }

  function sourceTextHtml(value) {
    return escapeSourceHtml(value).replace(/\n/g, '<br>');
  }

  function renderZhuSourceBody(docId) {
    var record = sourceRecord(docId);
    var body = record && record.body ? String(record.body) : '';
    if (!body) return docId === '硃21' ? zhu21Body : zhu22Body;

    var ranges = [];
    (sourceMarkerFragments[docId] || []).forEach(function (fragment) {
      var start = body.indexOf(fragment);
      if (start !== -1) ranges.push({ start: start, end: start + fragment.length, group: 'markerA' });
    });
    var dateText = '乾隆五十一年十二月二十七日';
    var dateStart = body.lastIndexOf(dateText);
    if (dateStart !== -1) ranges.push({ start: dateStart, end: dateStart + dateText.length, group: 'dateA' });
    ranges.sort(function (left, right) { return left.start - right.start; });

    var html = '<span class="doc-focus">';
    var cursor = 0;
    ranges.forEach(function (range) {
      if (range.start < cursor) return;
      html += sourceTextHtml(body.slice(cursor, range.start));
      html += '<mark data-group="' + range.group + '">' + sourceTextHtml(body.slice(range.start, range.end)) + '</mark>';
      cursor = range.end;
    });
    html += sourceTextHtml(body.slice(cursor)) + '</span>';
    return html;
  }

  var entries = [
    {
      id: 'markerA', index: '01', title: '「據⋯⋯奏」引述標記',
      summary: '在評論官員奏報和下達命令前，上諭通常會先使用「據某人奏」、「據某人馳奏」或「據某人奏稱」等引述標記，交代皇帝所收到的官員奏報。<br><br>此外，同一項資訊可能由多位官員奏報，而上諭卻大多只會使用「據某人等奏稱」或「據奏」的標記，不會列出所有的奏報官員。因此，不能只用 Python 擷取人名或標記，來確定上諭所回應的奏摺。',
      skill: '<div class="skill-row skill-heading"><span class="md-kw">## 3. Citation (來源標記)</span></div>' +
        '<div class="skill-row skill-lead">辨識上諭開頭引述之奏報來源標記：</div>' +
        '<div class="skill-row skill-highlight"><mark class="code-mark" data-group="markerA">來源標記：辨識「據某人奏」／「據某人馳奏」／「據某人奏稱」</mark></div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">來源定位</span>：找出上諭引用的奏報來源官員（如「據常青等奏」）。</div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">多源歸納</span>：比對候選奏摺池中各督撫作者與事件內容，建立多對一依據鏈。</div>'
    },
    {
      id: 'dateA', index: '02', title: '收發日期',
      summary: '然而，與回應上諭的奏摺不同，上諭通常不會註明皇帝何時收到相關奏摺，以及相關奏摺的發送日期。<br><br>儘管如此，上諭通常會回應最新收到的奏報，平台會先利用 Python搜尋上諭發布當日，以及發布前5日內收到的奏摺，作為後續分析的候選文本。',
      skill: '<div class="skill-row skill-heading"><span class="md-kw">## 2. Date (日期窗口篩選)</span></div>' +
        '<div class="skill-row skill-lead">比對上諭發布前之候選奏摺收訖時間：</div>' +
        '<div class="skill-row skill-highlight"><mark class="code-mark" data-group="dateA">日期篩選：以上諭發布日前五日內、或發布當日收到的奏摺作為候選</mark></div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">候選窗口</span>：篩選乾隆51年12月27日前5日內送達軍機處之奏摺。</div>' +
        '<div class="skill-row skill-bullet"><span class="md-bullet">•</span> <span class="md-kw">時效性比對</span>：鎖定常青（硃21）與任承恩（硃22）於同日進呈之奏報。</div>'
    }
  ];

  /* ==========================================================================
     Mobile / narrow layout (<= 860px)
     ========================================================================== */
  var mobileBuilt = false;
  function buildMobile() {
    if (mobileBuilt || list.dataset.reqBuilt === 'true') return;
    mobileBuilt = true;

    function miniWindow(candidate) {
      return window.part2DocPanel.create({
        outerClass: 'req-doc-mini',
        dataReqMini: candidate.id,
        badge: '硃',
        badgeClass: 'b-zhu',
        title: candidate.title,
        metaLines: [
          candidate.author + '（' + candidate.role + '）',
          candidate.id === '硃21' ? '乾隆51年12月12日上奏' : '乾隆51年12月10日上奏',
          '<mark data-group="dateA">乾隆51年12月27日</mark>硃批'
        ],
        label: '引文摘錄',
        body: renderZhuSourceBody(candidate.id)
      });
    }

    var candidates = [
      { title: '為奏林爽文攻陷彰化已星馳調兵赴臺事', author: '常青', role: '閩浙總督', id: '硃21', body: zhu21Body },
      { title: '為奏林爽文攻陷彰化已備兵聽候調遣事', author: '任承恩', role: '福建陸路提督', id: '硃22', body: zhu22Body }
    ];

    function buildEntry(entry) {
      var el = document.createElement('div');
      el.className = 'req-entry';
      el.setAttribute('data-req-item', entry.id);
      var yuPanel = window.part2DocPanel.create({
        outerClass: 'req-win req-win-doc',
        dataReqDoc: 'yu',
        badge: '諭',
        badgeClass: 'b-yu',
        title: '諭閩浙總督常青等嚴行殲戮林爽文等並防餘衆四散內渡',
        metaLines: ['常青（字寄轉發）', '乾隆51年12月12日下旨', '《天地會》'],
        label: '正文',
        body: yuBody
      });
      el.innerHTML = '<div class="req-card" data-req-card>' +
        '<button class="req-bar" type="button" aria-expanded="false" data-req-bar><span class="req-index">' + entry.index + '</span><strong>' + entry.title + '</strong><span class="req-arrow" aria-hidden="true">▾</span></button>' +
        '<div class="req-panel" data-req-panel><div class="req-panel-inner"><div class="req-wordcard" data-req-wordcard><p>' + entry.summary + '</p></div></div></div>' +
        '<div class="req-stage-wrap" data-req-stage-wrap><div class="req-stage-wrap-inner"><div class="req-visual"><div class="req-stage" data-req-stage style="grid-template-columns:1fr auto 1fr auto 1fr">' +
          '<div class="req-win req-win-skill" data-req-skill><div class="agentic-mac-titlebar"><span class="agentic-mac-dot red"></span><span class="agentic-mac-dot yellow"></span><span class="agentic-mac-dot green"></span><span class="agentic-window-title">yu-source.md</span></div><div class="req-vscode-shell"><div class="req-vscode-activitybar"><span>▦</span><span>⌕</span><span>⑂</span></div><div class="req-vscode-editor"><div class="req-vscode-tabs"><span class="req-vscode-tab">yu-source.md</span></div><div class="req-vscode-body" data-req-body>' + entry.skill + '</div></div></div></div>' +
          '<span class="req-connector" data-req-connector="1" aria-hidden="true">→</span>' + yuPanel +
          '<span class="req-connector" data-req-connector="2" aria-hidden="true">→</span>' +
          '<div class="req-win req-win-docstack" data-req-docstack>' + candidates.map(miniWindow).join('') + '</div>' +
        '</div></div></div></div></div>';
      return el;
    }

    entries.forEach(function (entry) { list.appendChild(buildEntry(entry)); });
    list.dataset.reqBuilt = 'true';
    var docPanel = window.part2DocPanel;

    var items = Array.prototype.slice.call(root.querySelectorAll('[data-req-item]')).map(function (el) {
      var stage = el.querySelector('[data-req-stage]'), skill = el.querySelector('[data-req-skill]'), yu = el.querySelector('[data-req-doc="yu"]'), stack = el.querySelector('[data-req-docstack]'), minis = Array.prototype.slice.call(stack.querySelectorAll('[data-req-mini]'));
      var bodies = { skill: skill.querySelector('[data-req-body]'), yu: yu.querySelector('[data-req-body]'), minis: minis.map(function (mini) { return mini.querySelector('[data-req-body]'); }) };
      bodies.skill.dataset.original = bodies.skill.innerHTML; bodies.yu.dataset.original = bodies.yu.innerHTML; bodies.minis.forEach(function (body) { body.dataset.original = body.innerHTML; });
      return { id: el.getAttribute('data-req-item'), el: el, card: el.querySelector('[data-req-card]'), bar: el.querySelector('[data-req-bar]'), panel: el.querySelector('[data-req-panel]'), wordcard: el.querySelector('[data-req-wordcard]'), stageWrap: el.querySelector('[data-req-stage-wrap]'), stage: stage, wins: [skill, yu, stack], connectors: [el.querySelector('[data-req-connector="1"]'), el.querySelector('[data-req-connector="2"]')], bodies: bodies, timers: [] };
    });
    function reset(item) {
      item.timers.forEach(function (t) { clearTimeout(t); }); item.timers = [];
      item.el.classList.remove('is-open'); item.card.classList.remove('is-open'); item.panel.classList.remove('is-open'); item.stageWrap.classList.remove('is-open'); item.wordcard.classList.remove('is-shown');
      item.wins.forEach(function (win) { win.classList.remove('is-shown'); if (docPanel) docPanel.reset(win); }); item.connectors.forEach(function (connector) { connector.classList.remove('is-shown'); });
      item.bodies.skill.innerHTML = item.bodies.skill.dataset.original; item.bodies.yu.innerHTML = item.bodies.yu.dataset.original; item.bodies.minis.forEach(function (body) { body.innerHTML = body.dataset.original; });
    }
    function activate(item, rawGroup) {
      var groups = String(rawGroup || '').split(/\s+/);
      if (groups.indexOf(item.id) === -1) return;
      item.wins.forEach(function (win) {
        win.querySelectorAll('mark[data-group]').forEach(function (mark) {
          if (docPanel && !docPanel.matchesGroup(mark, item.id)) return;
          mark.classList.remove('is-active'); void mark.offsetWidth; mark.classList.add('is-active');
        });
        if (docPanel && win.classList.contains('source-flow-document')) docPanel.focus(win, item.id);
      });
    }
    function close(item) { item.bar.setAttribute('aria-expanded', 'false'); reset(item); }
    function open(item) {
      items.forEach(function (other) { if (other !== item && other.el.classList.contains('is-open')) close(other); });
      reset(item); item.el.classList.add('is-open'); item.bar.setAttribute('aria-expanded', 'true');
      item.card.classList.add('is-open'); item.stageWrap.classList.add('is-open');
      item.wins.forEach(function (w) { w.classList.add('is-shown'); });
      item.connectors.forEach(function (c) { c.classList.add('is-shown'); });
      activate(item, item.id);
      item.panel.classList.add('is-open');
      item.wordcard.classList.add('is-shown');
    }
    items.forEach(function (item) {
      item.bar.addEventListener('click', function () { if (item.el.classList.contains('is-open')) close(item); else open(item); });
      item.stage.addEventListener('click', function (event) { var mark = event.target.closest('mark[data-group]'); if (mark) activate(item, mark.getAttribute('data-group')); });
      if (docPanel) docPanel.bindAll(item.wins);
    });
  }

  /* ==========================================================================
     Desktop layout (> 860px) with 3 Document Panels and 1 上諭 -> 2 奏摺 Links
     ========================================================================== */
  var DESKTOP_MARKUP =
    '<div class="replica-shell">' +
      '<div data-part1 data-part1-data="PART1_INTERFACE_DATA_YU_SOURCE" data-part1-chart-scale="1.5"><div class="part1-replica" data-part1-replica></div></div>' +
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
                '<span class="req-skill-title-text">yu-source.md</span>' +
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
    '#part-2-content #part-2-yu-source [data-req-idle-wrap], #part-2-content #part-2-yu-source .req-idle-skill { display: none !important; }',
    '#part-2-content #part-2-yu-source { padding-top: 0 !important; padding-left: clamp(2px, 0.8vw, 14px) !important; padding-right: clamp(2px, 0.8vw, 14px) !important; }',
    '#part-2-yu-source { --yu-source-date: 255, 214, 68; }',
    '#part-2-content #part-2-yu-source > .part2-substage-cover, #part-2-yu-source .part2-substage-cover { padding-top: 24px !important; padding-bottom: 20px !important; margin-top: 0 !important; margin-bottom: 0 !important; }',
    '#part-2-content #part-2-yu-source > .story-inner, #part-2-content #part-2-yu-source > .part2-yu-source-story-inner { width: 100% !important; max-width: 100% !important; margin: 0 !important; padding-top: 0 !important; }',
    '#part-2-yu-source .req-desktop-tool { margin: 12px 0 0 !important; width: 100%; }',
    '#part-2-yu-source .replica-shell { width: 100%; background: #f1eadc; border: 1px solid #d8cdbb; border-radius: 6px; box-shadow: 0 13px 30px rgba(47,57,52,.15); overflow: hidden; --stage-dock-pct: 70%; }',
    '#part-2-yu-source .replica-shell .part1-replica { --font-scale: 1; }',
    '#part-2-yu-source .replica-stage { padding: 6px; gap: 8px; height: clamp(660px, 74vh, 820px); }',

    /* description panel sits BELOW the visual */
    '#part-2-yu-source .req-desc { display: flex; flex-direction: column; margin: 18px 0 0; background: var(--card); border: 1px solid #d8cdbb; border-radius: 6px; box-shadow: 0 8px 24px rgba(47,57,52,.1); overflow: hidden; }',
    '#part-2-yu-source .req-desc-head { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; padding: 13px 20px 11px; border-bottom: 1px solid var(--line); background: rgba(244,239,230,.4); }',
    '#part-2-yu-source .req-desc .req-desc-index { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 30px; height: 30px; color: #fffaf2; background: #8a7c66; border-radius: 50%; font: 800 13px/1 var(--sans); }',
    '#part-2-yu-source .req-desc[data-active-req="markerA"] .req-desc-index { background: rgb(var(--yu-source-marker)) !important; }',
    '#part-2-yu-source .req-desc[data-active-req="dateA"] .req-desc-index { background: rgb(var(--yu-source-date)) !important; color: #3b2800 !important; }',
    '#part-2-yu-source .req-desc-head h3 { flex: 1; min-width: 160px; margin: 0; color: var(--ink); font: 700 calc(18px * var(--font-scale, 1))/1.35 var(--serif); }',
    '#part-2-yu-source .req-desc[data-active-req="dateA"] .req-desc-head h3 { color: rgb(var(--yu-source-date)) !important; }',
    '#part-2-yu-source .req-desc-body { padding: 16px 20px 18px; }',

    /* 50% / 50% split layout */
    '#part-2-yu-source .req-desc-split { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: stretch; width: 100%; }',
    '#part-2-yu-source .req-desc-text-panel { display: flex; flex-direction: column; justify-content: center; min-width: 0; padding: 4px 0; height: 100%; }',
    '#part-2-yu-source .req-desc .req-wordcard { display: flex; flex-direction: column; justify-content: center; height: 100%; border-top: none !important; padding-top: 0 !important; margin: 0 !important; opacity: 1 !important; transform: none !important; }',
    '#part-2-yu-source .req-desc .req-wordcard p { margin: 0; color: var(--text); font: 500 calc(18px * var(--font-scale, 1))/1.85 var(--serif); text-align: justify; }',
    '#part-2-yu-source .req-desc-head h3, #part-2-yu-source .req-desc .req-wordcard p { font-size: calc(18px * var(--font-scale, 1)) !important; }',

    /* Right Skills Window: 50% width */
    '#part-2-yu-source .req-desc-skill-panel { display: flex; flex-direction: column; min-width: 0; height: 100%; }',
    '#part-2-yu-source .req-win-skill-box { display: flex; flex-direction: column; height: 100%; min-height: max-content; background: #1e1e1e; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,.18), 0 0 0 1px rgba(255,255,255,.07) inset; }',
    '#part-2-yu-source .req-skill-titlebar { display: flex; align-items: center; gap: 6px; padding: 8px 12px; background: #252526; border-bottom: 1px solid #333333; flex: none; }',
    '#part-2-yu-source .req-mac-dot { width: 8.5px; height: 8.5px; border-radius: 50%; flex: none; }',
    '#part-2-yu-source .req-mac-dot.red { background: #ff5f57; }',
    '#part-2-yu-source .req-mac-dot.yellow { background: #febc2e; }',
    '#part-2-yu-source .req-mac-dot.green { background: #28c840; }',
    '#part-2-yu-source .req-skill-title-text { margin-left: 5px; color: #b5b5b5; font: 600 calc(12px * var(--font-scale, 1))/1 "SF Mono", ui-monospace, Menlo, Consolas, monospace; letter-spacing: .02em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex: 1; }',

    '#part-2-yu-source .req-skill-shell { display: grid; grid-template-columns: 26px 1fr; flex: 1 1 auto; height: 100%; min-height: max-content; background: #1e1e1e; }',
    '#part-2-yu-source .req-skill-activitybar { display: flex; flex-direction: column; align-items: center; gap: 12px; padding: 16px 0; color: #707070; background: #2b2b2b; font: 10.5px/1 var(--sans); border-right: 1px solid #383838; user-select: none; height: 100%; }',
    '#part-2-yu-source .req-skill-editor { display: flex; flex-direction: column; min-width: 0; min-height: max-content; height: 100%; }',
    '#part-2-yu-source .req-skill-body { flex: 1 1 auto; height: auto; min-height: max-content; overflow: visible !important; padding: 18px 18px 20px; color: #d4d4d4; font: 500 calc(15px * var(--font-scale, 1))/1.75 "SF Mono", ui-monospace, Menlo, Consolas, monospace; word-break: break-word; scrollbar-width: none; }',
    '#part-2-yu-source .req-skill-body::-webkit-scrollbar { display: none; }',
    '#part-2-yu-source .req-skill-body .skill-row { margin-bottom: 7px; }',
    '#part-2-yu-source .req-skill-body .skill-row:last-child { margin-bottom: 0; }',
    '#part-2-yu-source .req-skill-body .skill-heading { font-weight: 700; color: #4fc1ff; margin-bottom: 10px; font-size: calc(13.5px * var(--font-scale, 1)); }',
    '#part-2-yu-source .req-skill-body .skill-lead { margin-bottom: 6px; }',
    '#part-2-yu-source .req-skill-body .skill-highlight { margin: 8px 0 9px; }',
    '#part-2-yu-source .req-skill-body .skill-bullet { margin-bottom: 7px; }',
    '#part-2-yu-source .req-skill-body .md-kw { color: #4fc1ff; font-weight: 600; }',
    '#part-2-yu-source .req-skill-body .md-bullet { color: #9cdcfe; font-weight: bold; margin-right: 4px; }',

    /* Highlight in skill window */
    '#part-2-yu-source .req-skill-body mark.code-mark { display: inline-block; padding: 2px 7px; border-radius: 4px; color: #ffffff !important; font-weight: 600; line-height: 1.45; box-decoration-break: clone; -webkit-box-decoration-break: clone; }',
    '#part-2-yu-source .req-desc[data-active-req="markerA"] .req-skill-body mark.code-mark[data-group="markerA"] { background: rgba(var(--yu-source-marker), .85) !important; box-shadow: 0 0 0 1px rgba(var(--yu-source-marker), 1); }',
    '#part-2-yu-source .req-desc[data-active-req="dateA"] .req-skill-body mark.code-mark[data-group="dateA"] { background: rgba(var(--yu-source-date), .9) !important; box-shadow: 0 0 0 1px rgba(var(--yu-source-date), 1); }',

    '#part-2-yu-source .req-nav { display: flex; align-items: center; gap: 6px; margin-left: auto; }',
    '#part-2-yu-source .req-nav-arrow { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; color: var(--ink); background: transparent; border: 1px solid var(--line); border-radius: 50%; cursor: pointer; transition: background .15s ease, color .15s ease; }',
    '#part-2-yu-source .req-nav-arrow:hover { color: #fffaf2; background: var(--accent); border-color: var(--accent); }',

    /* Match 2.1: the replica toolbar is a faded, non-interactive visual header. */
    '#part-2-yu-source .replica-shell .part1-toolbar { pointer-events: none !important; background: transparent !important; border-bottom-color: transparent !important; }',
    '#part-2-yu-source .replica-shell .part1-toolbar * { pointer-events: none !important; cursor: default !important; }',
    '#part-2-yu-source .replica-shell .part1-toolbar button, #part-2-yu-source .replica-shell .part1-toolbar select, #part-2-yu-source .replica-shell .part1-toolbar input { opacity: .45; }',
    '#part-2-yu-source .replica-shell .part1-toolbar [data-type-pop], #part-2-yu-source .replica-shell .part1-toolbar [data-tools-pop] { display: none !important; }',

    /* 3 Document Panels Layout with 3-Way Resizers */
    '#part-2-yu-source .replica-shell { --site-font-scale: var(--font-scale, 1); }',
    '#part-2-yu-source .part1-replica { --font-scale: var(--site-font-scale) !important; --body-font-scale: var(--site-font-scale) !important; }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-dock { grid-template-columns: 1fr !important; }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-stack { grid-template-columns: calc(var(--col-1-pct, 33.33%) - 7px) 10px calc(var(--col-2-pct, 33.33%) - 6px) 10px calc(var(--col-3-pct, 33.34%) - 7px) !important; gap: 0 !important; }',
    '@media (max-width: 1080px) { #part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-stack { grid-template-columns: 1fr !important; gap: 10px !important; } }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-head { padding: 12px 14px 10px; background: linear-gradient(#fffdf8, #f3eada); border-bottom: 1px solid #e1d8c9; }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-head .part1-doc-title, #part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-title, #part-2-yu-source .part1-replica[data-pair-doc="true"] [data-doc-panel-title] { font: 700 calc(16.5px * var(--font-scale, 1))/1.35 var(--serif) !important; color: #2d261d !important; letter-spacing: .02em; margin: 0 0 5px; }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .badge, #part-2-yu-source .part1-replica[data-pair-doc="true"] [data-doc-panel-badge] { display: inline-block; width: auto; height: auto; margin-right: 5px; padding: 2px 6px; color: #fffaf2; background: #c46a2b; border-radius: 6px; font: 800 calc(12px * var(--font-scale, 1))/1.1 var(--sans) !important; vertical-align: 1px; }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] [data-doc-panel-doc="諭13"] .badge { background: #315d5d !important; }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-meta { margin: 0; color: #7a6f63; font: 500 calc(12px * var(--font-scale, 1))/1.5 var(--sans); line-height: 1.5; }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-section-label { font-size: calc(15px * var(--font-scale)); }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-body { font-size: calc(17px * var(--font-scale)); }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-window-controls { display: none !important; }',
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-doc-title { padding-right: 0 !important; }',

    '#part-2-yu-source .req-pair-resize { position: relative; z-index: 6; cursor: ew-resize; touch-action: none; user-select: none; }',
    '#part-2-yu-source .req-pair-resize::before { content: ""; position: absolute; top: 38%; bottom: 38%; left: 4px; width: 2px; border-radius: 2px; background: #d1c2ad; opacity: .7; transition: background .15s ease, opacity .15s ease, transform .15s ease; }',
    '#part-2-yu-source .req-pair-resize:hover::before, #part-2-yu-source .req-pair-resize:focus-visible::before, #part-2-yu-source .req-pair-resize.is-dragging::before { background: #a67d4f; opacity: 1; transform: scaleX(1.8); }',
    '#part-2-yu-source .req-pair-resize:focus-visible { outline: 2px solid rgba(166,125,79,.45); outline-offset: -1px; }',

    /* floating clue bubble on the 1st (上諭) panel */
    '#part-2-yu-source .part1-replica[data-pair-doc="true"] .part1-pair-doc { position: relative; }',
    '#part-2-yu-source .req-float-bubble { position: absolute; left: 0; top: 0; z-index: 30; display: flex; align-items: center; gap: 8px; height: 38px; max-width: calc(100% - 16px); padding: 5px 12px 5px 6px; color: #241d12; background: #fffdf8; border: 2px solid rgb(var(--bc, var(--yu-source-marker))); border-radius: 999px; box-shadow: 0 8px 18px rgba(30,22,10,.22); font: 700 10px/1 var(--sans); white-space: nowrap; transition: opacity .15s ease, left .12s ease, top .12s ease; }',
    '#part-2-yu-source .req-float-bubble[data-bubble-group="markerA"] { --bc: var(--yu-source-marker); }',
    '#part-2-yu-source .req-float-bubble[data-bubble-group="dateA"] { --bc: var(--yu-source-date); }',
    '#part-2-yu-source .req-float-bubble.req-float-hidden { opacity: 0; pointer-events: none; }',
    '#part-2-yu-source .req-float-num { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 24px; height: 24px; color: #fffdf8; background: rgb(var(--bc)); border-radius: 50%; font: 800 13px/1 var(--sans); }',
    '#part-2-yu-source .req-float-title { flex: 1 1 auto; min-width: 0; padding: 0 4px; overflow: hidden; text-overflow: ellipsis; color: #241d12; font: 800 calc(14px * var(--font-scale, 1))/1.35 var(--serif); }',
    '#part-2-yu-source .req-float-arrow { flex: none; display: inline-flex; align-items: center; justify-content: center; width: 22px; height: 22px; color: rgb(var(--bc)); background: transparent; border: 1.5px solid rgba(var(--bc),.5); border-radius: 50%; cursor: pointer; font: 700 13px/1 var(--sans); transition: background .15s ease; }',
    '#part-2-yu-source .req-float-arrow:hover { background: rgba(var(--bc),.16); }',
    '#part-2-yu-source .req-float-tail { position: absolute; left: 50%; bottom: -7px; width: 13px; height: 13px; background: #fffdf8; border-right: 2px solid rgb(var(--bc, var(--yu-source-marker))); border-bottom: 2px solid rgb(var(--bc, var(--yu-source-marker))); transform: translateX(-50%) rotate(45deg); border-radius: 0 0 3px 0; }',
    '#part-2-yu-source .req-float-bubble.req-float-flip .req-float-tail { bottom: auto; top: -7px; border-right: 0; border-bottom: 0; border-left: 2px solid rgb(var(--bc, var(--yu-source-marker))); border-top: 2px solid rgb(var(--bc, var(--yu-source-marker))); border-radius: 3px 0 0 0; }',

    /* highlight marks */
    '#part-2-yu-source .part1-pair-doc .part1-doc-body mark[data-group] { padding: 2px 4px; border-radius: 3px; box-decoration-break: clone; -webkit-box-decoration-break: clone; color: inherit !important; background: transparent !important; cursor: pointer; transition: background-color .15s ease, color .15s ease; opacity: 1 !important; }',
    '#part-2-yu-source .part1-pair-doc .part1-doc-body mark[data-group]:hover { filter: brightness(.92); }',
    '#part-2-yu-source .req-desktop-tool[data-active-req="markerA"] .part1-pair-doc .part1-doc-body mark[data-group*="markerA"], #part-2-yu-source .req-desktop-tool[data-active-req="markerA"] .part1-pair-doc .part1-doc-body mark[data-group*="markerA"].is-active { background: #3ee0cf !important; color: #043834 !important; font-weight: 600; }',
    '#part-2-yu-source .req-desktop-tool[data-active-req="dateA"] .part1-pair-doc .part1-doc-body mark[data-group*="dateA"], #part-2-yu-source .req-desktop-tool[data-active-req="dateA"] .part1-pair-doc .part1-doc-body mark[data-group*="dateA"].is-active { background: #ffd644 !important; color: #3b2800 !important; font-weight: 600; }',
    '#part-2-yu-source .part1-pair-doc .part1-doc-body mark[data-group].is-active { animation: part2-yu-response-hl-flash .5s ease-out; }',

    /* doc dim and focus */
    '#part-2-yu-source .part1-pair-doc .doc-dim { opacity: 0.35; transition: opacity .2s ease; }',
    '#part-2-yu-source .part1-pair-doc .doc-dim:hover { opacity: 0.72; }',
    '#part-2-yu-source .part1-pair-doc .doc-focus { opacity: 1; color: #18120b; font-weight: 500; }',
    '#part-2-yu-source .part1-pair-doc mark[data-group] { opacity: 1 !important; }',

    /* chart links: 1 上諭 dot (3rd line) -> 2 奏摺 dots (3rd line) -> 2 奏摺 dots (2nd line) */
    '#part-2-yu-source .part1-chart-links .part1-bg-link { opacity: 0.22 !important; pointer-events: none !important; }',
    '#part-2-yu-source .part1-chart-links .req-chart-link, #part-2-yu-source .part1-chart-links .part1-example-link { transition: opacity .2s ease, stroke-width .2s ease; cursor: pointer; pointer-events: stroke; }',
    '#part-2-yu-source .part1-chart-links .req-chart-link { opacity: .88 !important; stroke-width: 4 !important; }',
    '#part-2-yu-source .part1-chart-links .req-chart-link.is-active { opacity: 1 !important; stroke-width: 4.8 !important; }',

    '@media (max-width: 860px) { #part-2-yu-source .req-desc-split { grid-template-columns: 1fr; gap: 10px; } }',
    '@media (max-width: 900px) { #part-2-yu-source .req-float-title { display: none; } }'
  ].join('\n');

  var desktopBuilt = false;
  var desktopWrap = null;
  var desktopSetActive = null;

  function buildDesktopDataClone() {
    var GLOBAL_NAME = 'PART1_INTERFACE_DATA_YU_SOURCE';
    var base = window.PART1_INTERFACE_DATA;
    if (!base) return null;
    var docMap = new Map((base.documents || []).map(function (rec) { return [rec.docId, rec]; }));
    var yuDoc = docMap.get('諭13') || {
      docId: '諭13', docType: '上諭', title: '諭閩浙總督常青等嚴行殲戮林爽文等並防餘衆四散內渡',
      author: { position: '軍機處字寄', name: '常青等' },
      compiledIn: { book: '《天地會》', volume: '《天地會》' },
      sendDate: ['乾隆五十一年十二月十二日', '1786/12/12'], receiveDate: ['乾隆五十一年十二月十二日', '1786/12/12']
    };
    yuDoc = Object.assign({}, yuDoc, {
      announceDate: ['乾隆五十一年十二月十二日', '1786/12/12']
    });
    var zhu21 = docMap.get('硃21') || {
      docId: '硃21', docType: '硃批', title: '為奏林爽文攻陷彰化已星馳調兵赴臺事',
      author: { position: '閩浙總督', name: '常青' },
      compiledIn: { book: 30, volume: 30, page: 130 },
      sendDate: ['乾隆五十一年十二月十二日', '1786/12/12'], receiveDate: ['乾隆五十一年十二月二十七日', '1786/12/27']
    };
    var zhu22 = docMap.get('硃22') || {
      docId: '硃22', docType: '硃批', title: '為奏林爽文攻陷彰化已備兵聽候調遣事',
      author: { position: '福建陸路提督', name: '任承恩' },
      compiledIn: { book: 30, volume: 30, page: 112 },
      sendDate: ['乾隆五十一年十二月初十日', '1786/12/10'], receiveDate: ['乾隆五十一年十二月二十七日', '1786/12/27']
    };

    var EXAMPLE_NODE_IDS = ['doc-諭13-R', 'doc-硃21-R', 'doc-硃21-L', 'doc-硃22-R', 'doc-硃22-L'];
    var clone = Object.assign({}, base);
    clone.document = yuDoc;
    clone.documents = [zhu21, zhu22];
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

    // Active foreground links: 1 上諭 dot (3rd line) -> 2 奏摺 dots (3rd line) -> 2 奏摺 dots (2nd line)
    var activeLinks = [
      {
        id: 'example-link-yu13-to-zhu21R',
        from: 'doc-諭13-R',
        to: 'doc-硃21-R',
        className: 'part1-preview-link req-chart-link',
        color: '#c45d38',
        width: 2.8,
        background: false,
        title: '諭13 (第3線) ↔ 硃21 (第3線)'
      },
      {
        id: 'example-link-zhu21R-to-zhu21L',
        from: 'doc-硃21-R',
        to: 'doc-硃21-L',
        className: 'part1-preview-link req-chart-link',
        color: '#c45d38',
        width: 2.8,
        background: false,
        title: '硃21 (第3線) ↔ 硃21 原奏 (第2線)'
      },
      {
        id: 'example-link-yu13-to-zhu22R',
        from: 'doc-諭13-R',
        to: 'doc-硃22-R',
        className: 'part1-preview-link req-chart-link',
        color: '#c45d38',
        width: 2.8,
        background: false,
        title: '諭13 (第3線) ↔ 硃22 (第3線)'
      },
      {
        id: 'example-link-zhu22R-to-zhu22L',
        from: 'doc-硃22-R',
        to: 'doc-硃22-L',
        className: 'part1-preview-link req-chart-link',
        color: '#c45d38',
        width: 2.8,
        background: false,
        title: '硃22 (第3線) ↔ 硃22 原奏 (第2線)'
      }
    ];

    clone.chartPreview = Object.assign({}, base.chartPreview, {
      nodes: nodes,
      links: bgLinks.concat(activeLinks)
    });
    window[GLOBAL_NAME] = clone;
    return GLOBAL_NAME;
  }

  var DESKTOP_STYLE_ID = 'part2-yu-source-desktop-style';
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
      var markEl = leftBody && leftBody.querySelector('mark[data-group*="' + activeId + '"]');
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

    function flashMarks(groupId) {
      panelBodies().forEach(function (body) {
        body.querySelectorAll('mark[data-group*="' + groupId + '"]').forEach(function (mark) {
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
      if (descSummary) descSummary.innerHTML = req.summary;
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
          var mark = body.querySelector('mark[data-group*="' + groupId + '"]');
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
      if (mark) {
        var g = mark.getAttribute('data-group');
        if (g.indexOf('markerA') !== -1) setActive('markerA', { openDesc: true });
        else if (g.indexOf('dateA') !== -1) setActive('dateA', { openDesc: true });
        return;
      }
    });
    var navPrev = wrap.querySelector('[data-nav-prev]');
    var navNext = wrap.querySelector('[data-nav-next]');
    if (navPrev) navPrev.addEventListener('click', function () { goTo(-1); });
    if (navNext) navNext.addEventListener('click', function () { goTo(1); });

    function inject3WayResizers() {
      var stack = wrap.querySelector('[data-doc-stack]');
      if (!stack || stack.querySelector('[data-pair-resize]')) return;
      var panels = stack.querySelectorAll('[data-doc-panel-doc]');
      if (panels.length < 3) return;

      var handle1 = document.createElement('div');
      handle1.className = 'req-pair-resize';
      handle1.setAttribute('data-pair-resize', '1');
      handle1.setAttribute('role', 'separator');
      handle1.setAttribute('aria-orientation', 'vertical');
      handle1.setAttribute('tabindex', '0');
      handle1.setAttribute('aria-label', '調整上諭與第一份奏摺面板的寬度比例');
      stack.insertBefore(handle1, panels[1]);

      var handle2 = document.createElement('div');
      handle2.className = 'req-pair-resize';
      handle2.setAttribute('data-pair-resize', '2');
      handle2.setAttribute('role', 'separator');
      handle2.setAttribute('aria-orientation', 'vertical');
      handle2.setAttribute('tabindex', '0');
      handle2.setAttribute('aria-label', '調整第一份奏摺與第二份奏摺面板的寬度比例');
      stack.insertBefore(handle2, panels[2]);

      var col1 = 33.33;
      var col2 = 33.33;
      var col3 = 33.34;

      function apply() {
        stack.style.setProperty('--col-1-pct', col1.toFixed(2) + '%');
        stack.style.setProperty('--col-2-pct', col2.toFixed(2) + '%');
        stack.style.setProperty('--col-3-pct', col3.toFixed(2) + '%');
        positionBubble();
      }

      function setupHandle(handle, handleIndex) {
        handle.addEventListener('pointerdown', function (e) {
          e.preventDefault();
          handle.classList.add('is-dragging');
          if (handle.setPointerCapture) { try { handle.setPointerCapture(e.pointerId); } catch (err) {} }
          var rect = stack.getBoundingClientRect();
          function onMove(ev) {
            var pct = ((ev.clientX - rect.left) / rect.width) * 100;
            if (handleIndex === 1) {
              var newCol1 = Math.max(15, Math.min(65, pct));
              var diff = newCol1 - col1;
              if (col2 - diff >= 15) {
                col1 = newCol1;
                col2 = col2 - diff;
              }
            } else {
              var targetCol12 = Math.max(col1 + 15, Math.min(85, pct));
              var newCol2 = targetCol12 - col1;
              var newCol3 = 100 - col1 - newCol2;
              if (newCol2 >= 15 && newCol3 >= 15) {
                col2 = newCol2;
                col3 = newCol3;
              }
            }
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
      }

      setupHandle(handle1, 1);
      setupHandle(handle2, 2);
      apply();
    }

    function centerPairLine() {
      var scrollEl = wrap.querySelector('[data-chart-scroll]');
      if (!scrollEl) return;
      var n1 = wrap.querySelector('[data-chart-node-id="doc-諭13-R"]');
      var n2 = wrap.querySelector('[data-chart-node-id="doc-硃21-L"]');
      var n3 = wrap.querySelector('[data-chart-node-id="doc-硃22-L"]');
      var nodes = [n1, n2, n3].filter(Boolean);
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

    function initPair() {
      var BODIES = { '諭13': yuBody, '硃21': renderZhuSourceBody('硃21'), '硃22': renderZhuSourceBody('硃22') };
      ['諭13', '硃21', '硃22'].forEach(function (docId) {
        var panel = wrap.querySelector('[data-doc-panel-doc="' + docId + '"]');
        if (!panel) return;
        var body = panel.querySelector('[data-doc-body]');
        if (body && BODIES[docId]) body.innerHTML = BODIES[docId];
      });
      injectFloatBubble();
      inject3WayResizers();
      setActive(activeId, { skipScroll: true, openDesc: true });
      centerPairLine();
      scheduleCenter();
    }

    var dataClone = window.PART1_INTERFACE_DATA_YU_SOURCE;
    if (dataClone) {
      dataClone.onPairInit = function () {
        initPair();
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

    initPair();
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
