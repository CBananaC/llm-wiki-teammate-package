/* ============================================================================
   Part 2 · 分析階段二「重建通信關係」— 辨識奏摺所回應的上諭
   第二張卡片「系統會根據三項條件篩選候選文書……」右側的諭43／硃160
   對照視覺（[data-part2-evidence-visual]）。

   行為：
   - 預設只顯示硃160，寬度佔滿整個視覺區塊（諭43寬度為 0，貼齊硃160
     左邊界，完全不可見）。
   - 第一次點擊硃160原文中任一標色文字時：硃160收縮、諭43從硃160左
     邊界向左展開，兩者變成同尺寸、同高度、左右並排（50:50）；諭43
     的內文接著以較快速度逐字打出，打完後點亮對應的目標文字。此展開
     ＋打字動畫只播放一次。
   - 之後再點擊硃160其他標色文字，只切換諭43內已打好文字中的亮點，
     不會重播動畫；重新整理頁面會重置成初始狀態。
   - 泡泡提示指向硃160中第一個可點的標色文字（接奉廷寄），點擊任一
     標色文字後會消失。

   本檔初始化 #part-2-yu-response 內的互動視覺，並把其中的硃160
   「為奏料理撤兵及回省日期事」文件面板複製到 2-2 的右側位置。
   不影響頁面其他區域。
   ========================================================================== */
(function () {
  'use strict';

  const sourceRoot = document.querySelector('#part-2-yu-response [data-part2-evidence-visual]');
  const copyPlaceholder = document.querySelector('#part-2-zhu-response [data-part2-evidence-visual-copy]');
  const sourcePanel = sourceRoot && sourceRoot.querySelector('[data-evidence-zhu]');
  if (sourcePanel && copyPlaceholder) {
    const stage = document.createElement('div');
    stage.className = 'part2-evidence-stage part2-evidence-single-stage';
    stage.setAttribute('data-evidence-copy-stage', '');
    const panelClone = sourcePanel.cloneNode(true);
    panelClone.removeAttribute('data-evidence-zhu');
    panelClone.classList.add('part2-evidence-zhu-copy');
    stage.appendChild(panelClone);
    copyPlaceholder.replaceChildren(stage);
  }

  const roots = Array.prototype.slice.call(document.querySelectorAll('[data-part2-evidence-visual]'));
  roots.forEach(initEvidenceVisual);

  function initEvidenceVisual(root) {
    const stage = root.querySelector('[data-evidence-stage]');
    const zhuPanel = root.querySelector('[data-evidence-zhu]');
    const yuPanel = root.querySelector('[data-evidence-yu]');
    const zhuBody = root.querySelector('[data-evidence-zhu-body]');
    const yuBody = root.querySelector('[data-evidence-yu-body]');
    const hintBubble = root.querySelector('[data-evidence-hint]');
    if (!stage || !zhuPanel || !yuPanel || !zhuBody || !yuBody) return;

    const zhuMarks = Array.prototype.slice.call(zhuBody.querySelectorAll('mark[data-hl]'));
    const yuBodyHTML = yuBody.innerHTML; // 完整含 <mark> 目標的原始標記，稍後打字結束後還原用
    let firstReveal = true;

    function clearZhuPicked() {
      zhuMarks.forEach((el) => el.classList.remove('is-picked'));
    }
    function clearYuActive() {
      yuBody.querySelectorAll('mark[data-target]').forEach((el) => el.classList.remove('is-active'));
    }

    function activateTarget(targetKey) {
      clearYuActive();
      const targets = yuBody.querySelectorAll('mark[data-target="' + targetKey + '"]');
      targets.forEach((el) => {
        el.classList.remove('is-active');
        void el.offsetWidth; // 強制重繪，讓每次點擊都重播一次閃現動畫
        el.classList.add('is-active');
      });
      if (targets.length) targets[0].scrollIntoView({ block: 'center', behavior: 'smooth' });
    }

    function revealYuPanelThenType(targetKey) {
      zhuPanel.classList.add('is-shown');
      yuPanel.classList.add('is-shown');
      window.setTimeout(() => {
        const plain = yuBody.textContent;
        let i = 0;
        yuBody.textContent = '';
        const timer = setInterval(() => {
          i += 6;
          if (i >= plain.length) {
            clearInterval(timer);
            yuBody.innerHTML = yuBodyHTML;
            activateTarget(targetKey);
            return;
          }
          yuBody.textContent = plain.slice(0, i);
        }, 8);
      }, 220);
    }

    function positionHint() {
      if (!hintBubble || !zhuMarks.length) return;
      const first = zhuMarks[0];
      const stageRect = stage.getBoundingClientRect();
      const r = first.getBoundingClientRect();
      hintBubble.style.left = (r.left - stageRect.left) + 'px';
      hintBubble.style.top = (r.top - stageRect.top) + 'px';
    }
    function hideHint() {
      if (hintBubble) hintBubble.classList.remove('is-shown');
    }

    zhuMarks.forEach((el) => {
      el.addEventListener('click', () => {
        const group = el.dataset.hl;
        const targetKey = group === 'quote' ? 'b' : 'a';

        clearZhuPicked();
        zhuMarks.filter((m) => m.dataset.hl === group).forEach((m) => m.classList.add('is-picked'));

        hideHint();

        if (firstReveal) {
          firstReveal = false;
          revealYuPanelThenType(targetKey);
        } else {
          activateTarget(targetKey);
        }
      });
    });

    if (zhuMarks.length && hintBubble) {
      positionHint();
      hintBubble.classList.add('is-shown');
      hintBubble.addEventListener('click', () => zhuMarks[0].click());
      window.addEventListener('resize', positionHint);
    }
  }
})();
