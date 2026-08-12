/* ============================================================================
   Part 2 · 分析階段一「總結文書」— AI Skills 互動示範
   位於 2 段說明文字右側，示範 quick-summary.md／divide-into-parts.md
   兩個 Skill 如何把硃40 從「僅有原文」變成「摘要＋分段」。

   行為（桌面）：
   - 點擊 VS Code 風格視窗 → 逐字打出兩個 Skill 的指令內容（只播放一次）。
   - 播放完成後，文書面板出現邀請脈動；點擊文書面板套用摘要／分段
     （淡出原文、淡入摘要與分段卡片，只套用一次）。
   - 套用之後，兩個視窗變成一般可任意點擊切換前後順序的浮動視窗；
     視窗標題列的十字圖示可拖曳移動，右下角把手可拖曳縮放。
   - 打字完成後，直接點擊分頁籤（quick-summary.md／divide-into-parts.md）
     可即時切換顯示完整內容，不會重播打字動畫。

   行為（手機／窄螢幕，<=900px）：
   - 兩個視窗改為直向堆疊，VS Code 視窗在上。捲動到 VS Code 視窗時
     自動觸發打字效果；捲動到文書面板時自動套用摘要／分段。不支援
     拖曳與縮放（版面已固定為全寬堆疊）。

   本檔只服務 #part-2-summary-content 內的 [data-part2-summary-visual]
   容器，不影響頁面其他區域。
   ========================================================================== */
(function () {
  'use strict';

  const root = document.querySelector('[data-part2-summary-visual]');
  if (!root) return;

  const stage = root.querySelector('.part2-summary-stage');
  const skillWin = root.querySelector('.part2-summary-skill-win');
  const docWin = root.querySelector('.part2-summary-doc-win');
  const skillBody = root.querySelector('.part2-summary-skill-body');
  const tabs = Array.from(root.querySelectorAll('.part2-summary-tab'));
  const hintSkill = root.querySelector('.part2-summary-hint-skill');
  const hintApply = root.querySelector('.part2-summary-hint-apply');
  const caption = root.querySelector('.part2-summary-caption');
  const docBody = root.querySelector('.part2-summary-doc-body');
  if (!stage || !skillWin || !docWin || !skillBody || !docBody) return;

  const SKILLS = [
    {
      html:
        '<span class="hd"># Skill: Quick Document Summary</span>\n' +
        '<span class="cmt">Kind: summary</span>\n\n' +
        '<span class="hd">## Website Prompt</span>\n' +
        '<span class="str">用繁體中文，為上述文書寫一段更精簡、流暢的摘要\n' +
        '（約 3-5 句），突出最關鍵的人、事、時、地，\n' +
        '避免逐句翻譯。</span>\n\n' +
        '<span class="hd">## Purpose</span>\n' +
        '<span class="cmt">為任何單一文書（上奏／硃批／上諭）提供快速、通用的\n' +
        '文字摘要。此指示同時用於終端機批次執行的 summary\n' +
        '步驟，以及網站上的「進一步摘要」按鈕——同一份 Skill\n' +
        '檔案、同一段指示文字，兩種觸發方式。</span>'
    },
    {
      html:
        '<span class="hd"># Skill: Divide Document Into Parts</span>\n' +
        '<span class="cmt">Kind: divide</span>\n\n' +
        '<span class="hd">## Website Prompt</span>\n' +
        '<span class="str">將上述『原文』依內容與功能切分為數個連續段落。\n' +
        '對每一段給出：</span>\n' +
        '  <span class="kw">label</span>   段落標題（如「情報來源」「軍事部署」「請旨」）\n' +
        '  <span class="kw">summary</span> 一句繁體中文短摘要\n' +
        '  <span class="kw">excerpt</span> 該段原文，盡量逐字節錄\n\n' +
        '<span class="hd">## Purpose</span>\n' +
        '<span class="cmt">將文書切分為多個標籤化的段落，並直接在資訊面板的\n' +
        '原文上標示出來。無論是透過終端機（大量文書掃描）\n' +
        '或網站的「分段標註」按鈕（單一文書、審閱時使用，\n' +
        '用來補查大量掃描可能遺漏之處）觸發，皆使用同一段\n' +
        '指示文字。</span>'
    }
  ];

  const messages = {
    idle: '點擊左側視窗，查看「總結文書」所使用的兩個 AI Skill 指令。',
    typing: 'AI Skill 正在載入指令……',
    ready: '指令載入完成。點擊文書面板，套用摘要與分段結果。',
    applied: '摘要與分段已套用至文書面板；研究者仍需回到原文核對，確認無誤後才能加入圖表。點擊任一視窗可切換前後順序，標題列的十字圖示可拖曳移動，右下角把手可拖曳縮放。'
  };

  let phase = 'idle';
  let typing = false;
  let skillsTyped = false;
  const isMobile = window.matchMedia('(max-width: 900px)').matches;

  function setCaption(p) { if (caption) caption.textContent = messages[p]; }
  function stripTags(html) { return html.replace(/<[^>]+>/g, ''); }

  function setActiveTab(index) {
    tabs.forEach((t, i) => t.classList.toggle('is-active', i === index));
  }

  function renderTabFull(index) {
    setActiveTab(index);
    skillBody.innerHTML = SKILLS[index].html;
    skillBody.scrollTop = 0;
  }

  function typeSkill(index, done) {
    const skill = SKILLS[index];
    setActiveTab(index);
    const plain = stripTags(skill.html);
    let i = 0;
    skillBody.innerHTML = '';
    const caret = document.createElement('span');
    caret.className = 'part2-summary-caret';

    const timer = setInterval(() => {
      i += 2;
      if (i >= plain.length) {
        clearInterval(timer);
        skillBody.innerHTML = skill.html;
        if (tabs[index]) tabs[index].classList.add('is-typed');
        done();
        return;
      }
      skillBody.textContent = plain.slice(0, i);
      skillBody.appendChild(caret);
      skillBody.scrollTop = skillBody.scrollHeight;
    }, 34);
  }

  function startTyping() {
    if (phase !== 'idle' || typing) return;
    typing = true;
    phase = 'typing';
    setCaption('typing');
    if (hintSkill) hintSkill.classList.remove('is-shown');
    if (!isMobile) { skillWin.classList.add('is-top'); docWin.classList.add('is-dim'); }

    typeSkill(0, () => {
      setTimeout(() => {
        typeSkill(1, () => {
          typing = false;
          skillsTyped = true;
          phase = 'ready';
          setCaption('ready');
          skillWin.classList.add('is-done');
          docWin.classList.remove('is-dim');
          if (!isMobile) {
            skillWin.classList.remove('is-top');
            docWin.classList.add('is-invite');
            if (hintApply) hintApply.classList.add('is-shown');
          }
        });
      }, 320);
    });
  }

  function applyResult() {
    if (phase === 'applied') return;
    phase = 'applied';
    setCaption('applied');
    if (hintApply) hintApply.classList.remove('is-shown');
    docWin.classList.remove('is-invite');
    docBody.classList.add('is-fading');
    window.setTimeout(() => {
      docWin.classList.add('is-applied');
      requestAnimationFrame(() => {
        docWin.classList.add('is-applied-visible');
      });
    }, 300);
  }

  function bringToFront(el, other) {
    other.classList.remove('is-top');
    el.classList.add('is-top');
  }

  tabs.forEach((tab, i) => {
    tab.addEventListener('click', (e) => {
      e.stopPropagation();
      if (!skillsTyped) return;
      renderTabFull(i);
    });
  });

  /* ------------------------------------------------------------ 拖曳與縮放 */
  function clampNum(v, min, max) { return Math.min(Math.max(v, min), max); }

  function makeDraggable(win, handle) {
    if (!handle) return;
    let dragging = false;
    let startX = 0, startY = 0, startLeft = 0, startTop = 0;

    handle.addEventListener('pointerdown', (e) => {
      e.preventDefault();
      e.stopPropagation();
      dragging = true;
      try { handle.setPointerCapture(e.pointerId); } catch (err) { /* noop */ }
      const winRect = win.getBoundingClientRect();
      const stageRect = stage.getBoundingClientRect();
      startX = e.clientX;
      startY = e.clientY;
      startLeft = winRect.left - stageRect.left;
      startTop = winRect.top - stageRect.top;
      bringToFront(win, win === skillWin ? docWin : skillWin);
    });
    handle.addEventListener('pointermove', (e) => {
      if (!dragging) return;
      const stageRect = stage.getBoundingClientRect();
      const dx = e.clientX - startX;
      const dy = e.clientY - startY;
      const nextLeft = clampNum(startLeft + dx, -120, stageRect.width - 60);
      const nextTop = clampNum(startTop + dy, -30, stageRect.height - 40);
      win.style.left = nextLeft + 'px';
      win.style.top = nextTop + 'px';
    });
    ['pointerup', 'pointercancel'].forEach((evt) => {
      handle.addEventListener(evt, () => { dragging = false; });
    });
    handle.addEventListener('click', (e) => e.stopPropagation());
  }

  function makeResizable(win, handle, opts) {
    if (!handle) return;
    let resizing = false;
    let startX = 0, startY = 0, startW = 0, startH = 0;

    handle.addEventListener('pointerdown', (e) => {
      e.preventDefault();
      e.stopPropagation();
      resizing = true;
      try { handle.setPointerCapture(e.pointerId); } catch (err) { /* noop */ }
      const rect = win.getBoundingClientRect();
      startX = e.clientX;
      startY = e.clientY;
      startW = rect.width;
      startH = rect.height;
      bringToFront(win, win === skillWin ? docWin : skillWin);
    });
    handle.addEventListener('pointermove', (e) => {
      if (!resizing) return;
      const dx = e.clientX - startX;
      const dy = e.clientY - startY;
      win.style.width = clampNum(startW + dx, opts.minW, opts.maxW) + 'px';
      win.style.height = clampNum(startH + dy, opts.minH, opts.maxH) + 'px';
    });
    ['pointerup', 'pointercancel'].forEach((evt) => {
      handle.addEventListener(evt, () => { resizing = false; });
    });
    handle.addEventListener('click', (e) => e.stopPropagation());
  }

  if (!isMobile) {
    makeDraggable(skillWin, skillWin.querySelector('.part2-summary-move'));
    makeDraggable(docWin, docWin.querySelector('.part2-summary-move'));
    makeResizable(skillWin, skillWin.querySelector('.part2-summary-resize-handle'), { minW: 380, minH: 260, maxW: 800, maxH: 640 });
    makeResizable(docWin, docWin.querySelector('.part2-summary-resize-handle'), { minW: 380, minH: 320, maxW: 860, maxH: 780 });

    skillWin.addEventListener('click', () => {
      if (phase === 'applied') { bringToFront(skillWin, docWin); return; }
      startTyping();
    });
    skillWin.addEventListener('keydown', (e) => {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      e.preventDefault();
      if (phase === 'applied') { bringToFront(skillWin, docWin); return; }
      startTyping();
    });
    docWin.addEventListener('click', () => {
      if (phase === 'ready') { applyResult(); return; }
      if (phase === 'applied') { bringToFront(docWin, skillWin); return; }
    });
    docWin.addEventListener('keydown', (e) => {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      e.preventDefault();
      if (phase === 'ready') { applyResult(); return; }
      if (phase === 'applied') { bringToFront(docWin, skillWin); return; }
    });
    setCaption('idle');
    if (hintSkill) hintSkill.classList.add('is-shown');
  } else {
    setCaption('idle');
    let skillSeen = false;
    let docSeen = false;
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting || entry.intersectionRatio < 0.55) return;
        if (entry.target === skillWin && !skillSeen) { skillSeen = true; startTyping(); }
        if (entry.target === docWin && !docSeen) { docSeen = true; applyResult(); }
      });
    }, { threshold: [0.55] });
    io.observe(skillWin);
    io.observe(docWin);
  }
})();
