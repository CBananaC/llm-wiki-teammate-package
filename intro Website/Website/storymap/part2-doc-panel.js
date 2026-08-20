(function () {
  'use strict';

  var SVG_MOVE = '<svg class="svgic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"></path></svg>';
  var SVG_MIN = '<svg class="svgic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14"></path></svg>';
  var SVG_CLOSE = '<svg class="svgic" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"></path></svg>';
  var SVG_FILTER = '<svg class="svgic" viewBox="0 0 24 24" aria-hidden="true"><path d="m4 5 6 7v5l4 2v-7l6-7z"></path></svg>';
  var SVG_SETTINGS = '<svg class="svgic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7Zm0-5v2m0 13v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M3 12h2m14 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"></path></svg>';

  function joinAttrs(options) {
    var attrs = '';
    if (options.dataReqDoc) attrs += ' data-req-doc="' + options.dataReqDoc + '"';
    if (options.dataReqMini) attrs += ' data-req-mini="' + options.dataReqMini + '"';
    if (options.dataReqStack) attrs += ' data-req-docstack';
    return attrs;
  }

  function panelInner(options, body) {
    var lines = options.metaLines || [];
    var rows = lines.map(function (line) { return '<tr><td>' + line + '</td></tr>'; }).join('');
    var classes = options.innerClass || '';
    var label = options.label || '原文';
    return '<div class="ip-head">' +
      '<div class="ip-titles">' +
        '<div class="m1"><span class="badge ' + (options.badgeClass || 'b-zhu') + '">' + (options.badge || '硃') + '</span> <b>' + options.title + '</b></div>' +
        '<table class="meta-table"><tbody>' + rows + '</tbody></table>' +
      '</div>' +
      '<div class="ip-btns">' +
        '<button class="ip-move" type="button" aria-label="移動文書面板">' + SVG_MOVE + '</button>' +
        '<button class="ip-min" type="button" aria-label="收合文書面板" aria-expanded="true">' + SVG_MIN + '</button>' +
        '<button class="ip-close" type="button" aria-label="關閉文書面板">' + SVG_CLOSE + '</button>' +
      '</div>' +
      '<div class="ip-head-resize" aria-hidden="true"></div>' +
    '</div>' +
    '<div class="ip-body ' + classes + '">' +
      '<div class="ip-filterdock">' +
        '<button class="ip-filterbtn" type="button" aria-label="篩選標記" aria-pressed="false">' + SVG_FILTER + '</button>' +
        '<button class="ip-settingsbtn" type="button" aria-label="文書設定" aria-pressed="false">' + SVG_SETTINGS + '</button>' +
      '</div>' +
      '<div class="ip-scroll">' +
        '<div class="ip-pane ix active">' +
          '<div class="ix-cols"><div class="ix-text"><div class="blk">' +
            '<span class="blk-label">' + label + '</span>' +
            '<div class="source-flow-body-text" data-req-body>' + body + '</div>' +
          '</div></div><div class="ix-margin"></div></div>' +
        '</div>' +
      '</div>' +
    '</div>';
  }

  function panelMarkup(options) {
    var base = options.outerClass || 'req-win req-win-doc';
    var classes = (base + ' source-flow-document doc-panel-sample ip').trim();
    return '<div class="' + classes + '"' + joinAttrs(options) + '>' + panelInner(options, options.body || '') + '</div>';
  }

  function matchesGroup(mark, group) {
    var wanted = String(group || '').split(/\s+/);
    var groups = String(mark.getAttribute('data-group') || '').split(/\s+/);
    return wanted.some(function (token) { return token && groups.indexOf(token) !== -1; });
  }

  function focus(panel, group) {
    if (!panel || panel.hidden) return;
    var scroll = panel.querySelector('.ip-scroll');
    if (!scroll) return;
    var marks = Array.prototype.filter.call(panel.querySelectorAll('.source-flow-body-text mark[data-group]'), function (mark) {
      return matchesGroup(mark, group);
    });
    var mark = marks[0];
    if (!mark) {
      scroll.scrollTop = 0;
      return;
    }
    var scrollRect = scroll.getBoundingClientRect();
    var markRect = mark.getBoundingClientRect();
    var target = scroll.scrollTop + markRect.top - scrollRect.top - Math.max(18, scroll.clientHeight * 0.18);
    scroll.scrollTop = Math.max(0, target);
  }

  function bind(panel) {
    if (!panel || panel.dataset.docPanelBound === 'true') return;
    panel.dataset.docPanelBound = 'true';
    var min = panel.querySelector('.ip-min');
    var close = panel.querySelector('.ip-close');
    var filter = panel.querySelector('.ip-filterbtn');
    var settings = panel.querySelector('.ip-settingsbtn');
    if (min) min.addEventListener('click', function () {
      var folded = panel.classList.toggle('is-folded');
      min.setAttribute('aria-expanded', folded ? 'false' : 'true');
    });
    if (close) close.addEventListener('click', function () { panel.hidden = true; });
    [filter, settings].forEach(function (button) {
      if (!button) return;
      button.addEventListener('click', function () {
        var active = button.classList.toggle('is-active');
        button.setAttribute('aria-pressed', active ? 'true' : 'false');
      });
    });
  }

  function bindAll(panels) {
    panels.forEach(function (panel) {
      if (panel.classList.contains('source-flow-document')) bind(panel);
      panel.querySelectorAll('.source-flow-document').forEach(function (child) { bind(child); });
    });
  }

  function reset(panel) {
    if (!panel) return;
    panel.hidden = false;
    panel.classList.remove('is-folded');
    panel.querySelectorAll('.ip-filterbtn, .ip-settingsbtn').forEach(function (button) {
      button.classList.remove('is-active');
      button.setAttribute('aria-pressed', 'false');
    });
    var min = panel.querySelector('.ip-min');
    if (min) min.setAttribute('aria-expanded', 'true');
    var scroll = panel.querySelector('.ip-scroll');
    if (scroll) scroll.scrollTop = 0;
    panel.querySelectorAll('.source-flow-document').forEach(function (child) { reset(child); });
  }

  function upgrade(panel, options) {
    if (!panel) return panel;
    var body = panel.querySelector('[data-req-body], .req-doc-body');
    var bodyHtml = body ? body.innerHTML : '';
    var preserved = {
      dataReqDoc: panel.getAttribute('data-req-doc') || options.dataReqDoc,
      dataReqMini: panel.getAttribute('data-req-mini') || options.dataReqMini,
      dataReqStack: panel.hasAttribute('data-req-docstack')
    };
    options = Object.assign({}, options, preserved, { body: bodyHtml });
    panel.className = (panel.className + ' source-flow-document doc-panel-sample ip').trim();
    panel.innerHTML = panelInner(options, bodyHtml);
    bind(panel);
    return panel;
  }

  window.part2DocPanel = {
    create: panelMarkup,
    upgrade: upgrade,
    bind: bind,
    bindAll: bindAll,
    reset: reset,
    focus: focus,
    matchesGroup: matchesGroup
  };

  // The 2.2 panels are static HTML because their source excerpts are long.
  // Upgrade them here before the bar behaviour script stores each original body.
  var zhuRoot = document.querySelector('#part-2-zhu-response');
  if (zhuRoot) {
    zhuRoot.querySelectorAll('.req-win.req-win-doc[data-req-doc]').forEach(function (panel) {
      var title = panel.querySelector('.req-doc-title');
      var titleText = title ? title.textContent.replace(/^\s*(硃|諭)\s*/, '').trim() : '';
      var isEarlier = titleText.indexOf('統兵到臺') !== -1;
      upgrade(panel, {
        badge: '硃',
        badgeClass: 'b-zhu',
        title: titleText,
        metaLines: isEarlier
          ? ['黃仕簡（福建水師提督）', '乾隆52年1月5日上奏', '乾隆52年2月13日硃批', '明清台檔30，頁320']
          : ['黃仕簡（福建水師提督）', '乾隆52年3月7日上奏', '乾隆52年4月3日硃批', '明清台檔31，頁64'],
        label: '原文'
      });
    });
  }
})();
