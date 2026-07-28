const DOCUMENTS = {
  '硃83': {
    title: '為奏聞鳳山失陷援兵渡海赴臺事', series: '明清台灣檔案匯編', book: 30, page: 188,
    docType: '硃', author: '常青', position: '閩浙總督', send: '1787/01/02', receive: '1787/01/15', lag: 13,
    subtitle: '常青催令福寧鎮等兵繼進', description: '總督常青催促續派之福寧鎮及銅山、羅源等營兵共一千名陸續跟進渡臺支援。',
    category: '待執行', location: '福寧', person: '常青',
    quote: '至續派之福寧鎮及銅山、羅源等營，共兵一千名，亦催令陸續繼進',
    body: "閩浙總督臣常青跪奏，為飛摺奏聞事十二月三十日戌刻，接據臺灣道永福十二月十四日來稟，內稱：竊照彰匪林爽文、王芬等謀為不軌，攻陷諸、彰兩邑，業經職道將官弁被害並督率兵丁分路救援各緣由，馳稟在案。職道以臺鎮雖經調遣將兵往救諸羅，並四處堵禦，而大兵未到，郡城兵少堪虞。正在嚴督實力守禦，一面會同柴鎮設法剿捕間，茲於十二月十三日亥刻，據南路兵丁劉茂光回稱：鳳邑瑚參將於十二日聞知賊匪有攻打鳳城之信，即帶兵三百名紮營城外。十三日天明時候，有賊匪二千餘名直攻縣城。瑚參將施放槍炮，僅斃賊五、六人，賊勢稍退。瑚參將放馬直追，賊匪乘虛由龜山北門撲入城內。斯時官兵槍炮莫施，旋即潰散。瑚參將縱馬由南而去，不知下落。等語又據逃回鳳邑跟丁稟稱：賊人進入縣署，該縣湯大奎情急拔劍自刎。等情。查賊匪恃眾猖獗四處潛聚，乘隙攻陷。臺屬兵少勢孤，顧此又虞失彼，郡城遼闊兵單，實難防守抵敵，事在危急，相應飛稟迅撥大兵來臺，以便克期進剿，恢復諸、彰等邑，不勝惶悚待命之至。等情到臣。臣接閱之下，驚駭憤懣，恨不親自奮飛殲此惡孽。但水、陸二提臣俱經臣派撥官兵，早令統率前往，因守風待渡，又經屢次發令嚴催。今據廈門同知稟報，水師提臣黃仕簡自金門收泊料羅，續於二十八日又自料羅放洋，計期兩、三日內，即可前抵鹿耳，援應郡城。陸路提臣任承恩係由蚶江出口，據蚶江通判稟報，亦於二十八日放洋。旋因風雨驟作，寄泊臭塗澳外。查該處與鹿仔港相對，一俟風定，即可揚帆直達。且接據署守備陳邦光稟報，鹿港一帶，但有義民，共相保守，可望接應，以壯聲援。惟是賊情猖獗，到處蔓延，自澎湖至鹿耳門，係屬臺郡咽喉，尤宜厚集兵力。臣前經續調督撫標兵一千名，原令由南臺出口，前往鹿耳，以備策應第恐海道行回，風汛難定，適預備之延、建兵一千名，亦已分起前來。因令督、撫標兵，仍駐省城防守。將延、建兵一千名派委延平協副將林天洛管帶，由陸路兼程赴廈，並派先經調來之汀州鎮總兵普吉保統率登舟；又於水師提標五營內，預備兵丁六百名，派令興化協副將格繃額帶領，亦從廈門配船飛渡，均由鹿耳赴臺，隨同水師提臣協力進剿。至續派之福寧鎮及銅山、羅源等營，共兵一千名，亦催令陸續繼進，並一面飛咨水陸兩提臣上緊援剿外，臣不勝憂憤急迫之至。合將據報鳳山被賊情形恭摺馳奏。再，漳、泉二郡，民俗凶悍，誠恐賊匪潛通勾結，臣俱密為防範。並往來泉、廈各海口嚴加督察，務保無虞。合並陳明，伏祈皇上睿鑒。謹奏。\n\n乾隆五十二年正月初二日\n乾隆五十二年正月十五日奉硃批：此時惟以鎮靜為要，毋得張皇失措，餘有旨諭。欽此。〔本文原收錄於軍錄】"
  }
};

const escapeHtml = (value) => String(value).replace(/[&<>"']/g, (char) => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[char]));
const params = new URLSearchParams(window.location.search);
const docId = params.get('doc') || '硃83';
const doc = DOCUMENTS[docId] || DOCUMENTS['硃83'];
const panels = new Set((params.get('panels') || 'ai,original').split(',').map((item) => item.trim()).filter(Boolean));
const aiPanel = document.getElementById('ai-panel');
const originalPanel = document.getElementById('original-panel');
if (!panels.has('ai')) aiPanel.hidden = true;
if (!panels.has('original')) originalPanel.hidden = true;
if (panels.size === 1) document.getElementById('embed-shell').style.gridTemplateColumns = '1fr';

document.getElementById('ai-hint').textContent = `${docId} · 清廷行動`;
document.getElementById('doc-header').innerHTML = `<div class="m1"><span class="badge">${escapeHtml(doc.docType)}</span> <b>${escapeHtml(doc.title)}</b></div><table class="meta-table"><tr><td>${escapeHtml(doc.position)}・${escapeHtml(doc.author)}</td></tr><tr><td>${escapeHtml(doc.send)} 上奏，${escapeHtml(doc.receive)} 硃批（${doc.lag} 日）</td></tr><tr><td>${escapeHtml(doc.series)} 冊${doc.book} 頁${doc.page}・${escapeHtml(docId)}</td></tr></table>`;
document.getElementById('ai-card').innerHTML = `<div class="cx-head"><span>AI 清廷行動（1）</span><span class="head-spacer"></span><button class="tb-close" type="button" aria-label="移除示例訊息">×</button></div><div class="cx-qcat">${escapeHtml(doc.category)}</div><div class="cx-sub">${escapeHtml(doc.subtitle)}</div><div class="cx-desc">${escapeHtml(doc.description)}</div><div class="cx-q" data-target="source-quote" title="點按在原文中顯示">「${escapeHtml(doc.quote)}」<span class="cx-src">—${escapeHtml(docId)}</span></div><dl class="cx-meta"><dt>地點</dt><dd>${escapeHtml(doc.location)}</dd><dt>人物</dt><dd>${escapeHtml(doc.person)}</dd><dt>發生日期</dt><dd>未明</dd></dl><div class="cx-acts"><button type="button" class="review-action" data-decision="approve">加入</button><button type="button" class="review-action cx-skip" data-decision="reject">略過</button></div><p class="review-status" id="review-status">點擊引文，在右側原文面板定位並標示。</p>`;
const bodyEl = document.getElementById('original-body');
const start = doc.body.indexOf(doc.quote);
bodyEl.innerHTML = `${escapeHtml(doc.body.slice(0, start))}<span class="quote-target" id="source-quote">${escapeHtml(doc.quote)}</span>${escapeHtml(doc.body.slice(start + doc.quote.length))}`;
document.querySelector('.cx-q[data-target]').addEventListener('click', (event) => {
  const target = document.getElementById(event.currentTarget.dataset.target);
  document.querySelector('.cx-q[data-target]').classList.add('is-selected');
  target.classList.add('is-highlighted');
  target.scrollIntoView({ behavior:'smooth', block:'center' });
  document.getElementById('review-status').textContent = '已定位：原文引文已在右側文書面板標示。';
});
document.querySelectorAll('.review-action').forEach((action) => action.addEventListener('click', () => {
  document.querySelectorAll('.review-action').forEach((item) => item.classList.remove('is-active'));
  action.classList.add('is-active');
  document.getElementById('review-status').textContent = action.dataset.decision === 'approve' ? '已暫存：研究者批准此項結果，可加入圖表。' : '已暫存：研究者略過此項結果。';
}));
