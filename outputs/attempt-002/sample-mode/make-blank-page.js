#!/usr/bin/env node
/*
 * make-blank-page.js  (lives in outputs/attempt-002/sample-mode/)
 * --------------------------------------------------------------
 * Generates `stage1-timeline-blank.html` (in THIS sample-mode folder) from the
 * live `../stage1-timeline.html` one level up.
 *
 * The blank page keeps ALL baked-in documents (the `const DUAL=[...]` dots) and
 * the full timeline layout, but starts with an EMPTY edit overlay and is fully
 * ISOLATED from the real data, so you can build sample data (e.g. yu->zhu reply
 * lines) for a presentation without ever touching the live timeline:
 *
 *   1. Uses its own localStorage key  -> real page's data is untouched.
 *   2. Never POSTs edits to /api/edits -> the durable disk file
 *      (../timeline-edits.local.json) is never overwritten.
 *   3. Never loads edits from /api/edits -> the real overlay is never pulled in.
 *   4. Adds a "清空範例" button (bottom-right) to reset to empty anytime, plus a
 *      banner so it's obvious you're on the sample page.
 *
 * Served by review-app/server.py at:
 *   http://127.0.0.1:8766/attempt-002/sample-mode/stage1-timeline-blank.html
 *
 * Re-run this anytime after editing ../stage1-timeline.html to regenerate a
 * fresh, up-to-date blank page.
 *
 * Usage:  node sample-mode/make-blank-page.js   (or cd sample-mode && node make-blank-page.js)
 */
const fs = require('fs');
const path = require('path');

const HERE = __dirname;                       // .../attempt-002/sample-mode
const ATTEMPT = path.dirname(HERE);           // .../attempt-002
const SRC = path.join(ATTEMPT, 'stage1-timeline.html');
const OUT = path.join(HERE, 'stage1-timeline-blank.html');
const BLANK_KEY = 'llmwiki.timeline.edits.BLANK.v1';

function replaceOnce(html, needle, replacement, label) {
  const i = html.indexOf(needle);
  if (i === -1) throw new Error('Anchor not found (' + label + '). ../stage1-timeline.html may have changed; update make-blank-page.js.');
  if (html.indexOf(needle, i + needle.length) !== -1) throw new Error('Anchor not unique (' + label + ').');
  return html.slice(0, i) + replacement + html.slice(i + needle.length);
}

let html = fs.readFileSync(SRC, 'utf8');

// T1: isolate localStorage key
html = replaceOnce(html,
  "const EDIT_KEY='llmwiki.timeline.edits.v1';",
  "const EDIT_KEY='" + BLANK_KEY + "';",
  'EDIT_KEY');

// T2: disk-sync sample edits to a SEPARATE endpoint/file (sample-mode/sample-edits.local.json)
// instead of the real /api/edits -> the real overlay is never written, and sample data persists
// across reloads without the ~5-10MB localStorage cap.
html = replaceOnce(html,
  "fetch('/api/edits', {method:'POST',",
  "fetch('/api/edits-blank', {method:'POST',",
  'syncEditsToServer POST url');

// T3: on boot, load the isolated sample file (not the real overlay) so sample data auto-loads.
html = replaceOnce(html,
  "fetch('/api/edits').then(r=>r.ok?r.json():null).then(server=>{",
  "fetch('/api/edits-blank').then(r=>r.ok?r.json():null).then(server=>{",
  'loadEditsFromServer fetch url');

// T4: inject reset button + banner just before </body>
const inject = `
<script>
/* BLANK PAGE controls: reset-to-empty button + banner. Isolated to key ${BLANK_KEY}. */
(function(){
  try{
    var K='${BLANK_KEY}';
    var reset=document.createElement('button');
    reset.textContent='🧹 清空範例';
    reset.title='清除此空白頁的所有範例資料並重新載入（不影響正式時間軸資料）';
    reset.style.cssText='position:fixed;right:12px;bottom:12px;z-index:99999;padding:6px 11px;font-size:12px;background:#c0392b;color:#fff;border:none;border-radius:6px;cursor:pointer;box-shadow:0 1px 5px rgba(0,0,0,.35)';
    reset.onclick=function(){ if(!confirm('確定清空此空白頁的所有範例資料？（不影響正式時間軸資料）')) return;
      try{ localStorage.removeItem(K); }catch(e){}
      var done=function(){ location.reload(); };
      try{ fetch('/api/edits-blank',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'}).then(done,done); }catch(e){ done(); } };
    document.body.appendChild(reset);
    var banner=document.createElement('div');
    banner.textContent='空白範例頁 · 資料獨立存於 sample-mode/sample-edits.local.json，不影響正式時間軸';
    banner.style.cssText='position:fixed;left:12px;bottom:12px;z-index:99999;padding:4px 9px;font-size:11px;background:#2c3e50;color:#fff;border-radius:6px;opacity:.85';
    document.body.appendChild(banner);
  }catch(e){}
})();
</script>
</body>`;
html = replaceOnce(html, '</body>', inject, '</body>');

fs.writeFileSync(OUT, html);
console.log('Wrote ' + path.relative(ATTEMPT, OUT) + ' (' + html.length + ' chars). Isolated key: ' + BLANK_KEY);
