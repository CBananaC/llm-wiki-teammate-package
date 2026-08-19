(function () {
  'use strict';

  var configs = [
    { id: 'part-2-zhu-response', file: 'zhu-response-pairing.md' },
    { id: 'part-2-yu-source', file: 'yu-source-pairing.md' }
  ];

  function fitIdleSkill(idle, wrap) {
    var body = idle.querySelector('[data-req-idle-body]');
    if (!body) return;
    idle.classList.add('is-content-fit');
    body.classList.add('is-content-fit');
    var height = Math.ceil(idle.scrollHeight);
    if (!height) return;
    idle.style.height = height + 'px';
    wrap.style.minHeight = height + 'px';
  }

  function makeIdleSkill(root, list, file) {
    var idle = document.createElement('div');
    idle.className = 'req-idle-skill';
    idle.setAttribute('data-req-idle-skill', '');
    idle.setAttribute('aria-hidden', 'true');
    idle.innerHTML = '<div class="agentic-mac-titlebar"><span class="agentic-mac-dot red"></span><span class="agentic-mac-dot yellow"></span><span class="agentic-mac-dot green"></span><span class="agentic-window-title">Visual Studio Code — ' + file + '</span></div>' +
      '<div class="req-vscode-shell"><div class="req-vscode-activitybar"><span>▦</span><span>⌕</span><span>⑂</span><span>▣</span><span>⚙</span></div><div class="req-vscode-editor"><div class="req-vscode-tabs"><span class="req-vscode-tab">' + file + '</span></div><div class="req-vscode-body req-idle-vscode-body" data-req-idle-body></div></div></div>';

    var skillBodies = list.querySelectorAll('[data-req-skill] [data-req-body]');
    var preview = Array.prototype.map.call(skillBodies, function (body) { return body.textContent; }).join('\n\n');
    var idleBody = idle.querySelector('[data-req-idle-body]');
    idleBody.textContent = '# AI 技能：' + file + '\n\n' + preview;
    return idle;
  }

  configs.forEach(function (config) {
    var root = document.getElementById(config.id);
    var list = root && root.querySelector('[data-req-list]');
    if (!root || !list || list.closest('[data-req-idle-wrap]')) return;

    var wrap = document.createElement('div');
    wrap.className = 'req-idle-wrap';
    wrap.setAttribute('data-req-idle-wrap', '');
    list.parentNode.insertBefore(wrap, list);
    wrap.appendChild(list);
    var idle = makeIdleSkill(root, list, config.file);
    wrap.appendChild(idle);
    window.requestAnimationFrame(function () { fitIdleSkill(idle, wrap); });

    root.addEventListener('click', function (event) {
      if (!event.target.closest('[data-req-bar]')) return;
      window.requestAnimationFrame(function () {
        wrap.classList.toggle('has-open', !!root.querySelector('.req-entry.is-open'));
      });
    });
  });
})();
