(() => {
  const $ = (selector, scope = document) => scope.querySelector(selector);
  const $$ = (selector, scope = document) => [...scope.querySelectorAll(selector)];

  /* 介面字級：只調整本獨立教學頁，不改動原 StoryMap 的設定。 */
  const FONT_KEY = 'ocr-standalone-font-scale';
  const FONT_MIN = .8;
  const FONT_MAX = 1.25;
  const FONT_STEP = .05;
  const fontValue = $('[data-font-value]');
  const readFontScale = () => {
    const saved = Number.parseFloat(localStorage.getItem(FONT_KEY));
    return Number.isFinite(saved) ? Math.min(FONT_MAX, Math.max(FONT_MIN, saved)) : 1;
  };
  const applyFontScale = (value) => {
    const scale = Math.min(FONT_MAX, Math.max(FONT_MIN, value));
    document.documentElement.style.setProperty('--font-scale', String(scale));
    if (fontValue) fontValue.textContent = `${Math.round(scale * 100)}%`;
    localStorage.setItem(FONT_KEY, String(scale));
  };
  applyFontScale(readFontScale());
  $$('[data-font]').forEach((button) => {
    button.addEventListener('click', () => {
      const delta = button.dataset.font === 'increase' ? FONT_STEP : -FONT_STEP;
      applyFontScale(readFontScale() + delta);
    });
  });

  /* 進度列：以 section 位置同步左側步驟。 */
  const sectionLinks = $$('[data-nav-target]');
  const sectionMap = new Map();
  sectionLinks.forEach((link) => {
    const target = document.getElementById(link.dataset.navTarget);
    if (target) sectionMap.set(link.dataset.navTarget, target);
  });
  const setActiveNav = (id) => {
    sectionLinks.forEach((link) => link.classList.toggle('is-active', link.dataset.navTarget === id));
  };
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (visible[0]) setActiveNav(visible[0].target.id);
    }, { rootMargin: '-18% 0px -68% 0px', threshold: 0 });
    sectionMap.forEach((section) => observer.observe(section));
  }

  /* 開頭的 OCR 影像流：頁面會循環不同掃描頁，按鈕可重新開始。 */
  const scanVisual = $('[data-scan-visual]');
  if (scanVisual) {
    const scanImages = {
      handwritten: [
        '../storymap/ocr-zhu25-handwritten-1-enhanced.png',
        '../storymap/ocr-zhu25-handwritten-2-enhanced.png',
        '../storymap/ocr-zhu25-handwritten-3-enhanced.png',
        '../storymap/ocr-zhu25-handwritten-4-enhanced.png'
      ],
      printed: [
        '../storymap/ocr-zhu25-printed-1-enhanced.png',
        '../storymap/ocr-zhu25-printed-2-enhanced.png'
      ]
    };
    const indexes = { handwritten: 0, printed: 0 };
    const imageEls = $$('[data-scan-image]', scanVisual);
    const advanceScan = () => {
      imageEls.forEach((image) => {
        const kind = image.dataset.scanImage;
        const pages = scanImages[kind];
        indexes[kind] = (indexes[kind] + 1) % pages.length;
        image.classList.add('is-changing');
        window.setTimeout(() => {
          image.src = pages[indexes[kind]];
          image.classList.remove('is-changing');
        }, 120);
      });
    };
    let scanTimer = window.setInterval(advanceScan, 4200);
    $('[data-scan-play]', scanVisual)?.addEventListener('click', () => {
      imageEls.forEach((image) => {
        const kind = image.dataset.scanImage;
        indexes[kind] = 0;
        image.src = scanImages[kind][0];
      });
      window.clearInterval(scanTimer);
      scanTimer = window.setInterval(advanceScan, 4200);
    });
  }

  /* Agentic AI 動畫：用來解釋工作步驟，明確標記為示範。 */
  const agenticDemo = $('[data-agentic-demo]');
  if (agenticDemo) {
    const status = $('[data-agentic-status]', agenticDemo);
    const output = $('[data-agentic-output]', agenticDemo);
    const runButton = $('[data-agentic-run]', agenticDemo);
    const messages = [
      ['檢查環境…', '我會先檢查 Python 版本與作業系統，再建立隔離環境。'],
      ['安裝 OCR 套件…', '環境準備完成。現在安裝 PaddlePaddle 與 PaddleOCR，並保留版本記錄。'],
      ['測試一頁…', '我會以一頁史料做快速測試，確認文字方向、欄位與輸出格式。'],
      ['示範完成', '流程示意完成：真正的 OCR 輸出仍要由研究者逐頁比對原始影像。']
    ];
    let running = false;
    const play = () => {
      if (running) return;
      running = true;
      runButton.disabled = true;
      let index = 0;
      const tick = () => {
        const [label, message] = messages[index];
        status.textContent = label;
        output.textContent = message;
        index += 1;
        if (index < messages.length) window.setTimeout(tick, 850);
        else {
          running = false;
          runButton.disabled = false;
          runButton.innerHTML = '再播放一次 <span aria-hidden="true">↻</span>';
        }
      };
      tick();
    };
    runButton.addEventListener('click', play);
  }

  const printedFeatures = [
    {
      key: 'text-info', title: '文本資訊', image: '../storymap/辨識印刷字Label/文本資訊.png', base: '../storymap/ocr-zhu25-printed-1-enhanced.png', colour: '#8fcfe0',
      desc: '正文前的史料來源、標題、作者和日期不是普通正文，應保留為可檢索的獨立欄位。',
      prompt: '辨識正文前的文本資訊：史料來源、標題、作者、日期，並把四項資料輸出為獨立欄位。',
      code: '# 先抽取 header，再處理正文\nheader = extract_header(result)\ndoc["metadata"] = header',
      json: '{ "source": "《明清臺灣檔案彙編》第30冊",\n  "title": "為奏彰化失陷已調兵赴臺事" }'
    },
    {
      key: 'single-column', title: '直排單欄', image: '../storymap/辨識印刷字Label/直排單欄.png', base: '../storymap/ocr-zhu25-printed-1-enhanced.png', colour: '#82adef',
      desc: '印刷奏摺的欄線和閱讀方向要先說清楚，否則 OCR 可能按照錯誤順序拼接文字。',
      prompt: '正文為直排單欄。請依由右至左、由上至下的順序輸出文字。',
      code: '# 直排、由右至左\nboxes = sort_vertical_rtl(result.boxes)\ntext = join_columns(boxes)',
      json: '{ "text_direction": "vertical_rtl",\n  "column_count": 9 }'
    },
    {
      key: 'paragraphs', title: '分段', image: '../storymap/辨識印刷字Label/分段.png', base: '../storymap/ocr-zhu25-printed-1-enhanced.png', colour: '#8e77dd',
      desc: '段落是資料結構的一部分。保留段首縮排或空行，後續才可以逐段定位引文。',
      prompt: '根據段首的縮排劃分段落，保留每一段的內容，不要合併不同段落。',
      code: '# 段首縮排作為分段訊號\nparagraphs = split_by_indent(lines)\nreturn {"paragraphs": paragraphs}',
      json: '{ "paragraphs": [\n  "福建水師提督一等海澄公…",\n  "竊照臺灣近來屢有匪徒滋事…"\n] }'
    },
    {
      key: 'page', title: '頁碼', image: '../storymap/辨識印刷字Label/頁碼.png', base: '../storymap/ocr-zhu25-printed-1-enhanced.png', colour: '#bd70de',
      desc: '頁碼不應混入正文，但要保留，讓研究者可以回到原件定位。',
      prompt: '辨識每一頁角落的頁碼，保存於 page_numbers 欄位，不要納入正文。',
      code: '# 頁碼獨立保存\ndoc["page_numbers"] = detect_page_numbers(image)',
      json: '{ "page_numbers": ["80", "81"] }'
    },
    {
      key: 'mark', title: '標題符號', image: '../storymap/辨識印刷字Label/標題符號.png', base: '../storymap/ocr-zhu25-printed-1-enhanced.png', colour: '#d980a0',
      desc: '標題符號會影響檢索和分段。要明確要求 AI 保留，而不是將它當作噪音刪掉。',
      prompt: '保留標題、標題符號與正文的層級，不要把標題併入第一段正文。',
      code: '# 標題與正文分開\ndoc["title"] = extract_title(lines)\ndoc["body"] = extract_body(lines)',
      json: '{ "title": "為奏彰化失陷已調兵赴臺事",\n  "title_marker": "保留" }'
    },
    {
      key: 'inline-zhu', title: '夾批', image: '../storymap/辨識印刷字Label/夾批.png', base: '../storymap/ocr-zhu25-printed-2-enhanced.png', colour: '#e6ada4',
      desc: '夾批不是正文的一部分。把它標示出來，才能在後續研究中區分奏摺文字與批語。',
      prompt: '辨識夾批，獨立保存其位置和文字，不要把夾批混入正文。',
      code: '# 夾批另存，保留頁面座標\nnotes.append({"kind": "inline_zhu", "bbox": box, "text": text})',
      json: '{ "annotations": [{\n  "kind": "inline_zhu", "text": "…"\n}] }'
    },
    {
      key: 'tail-zhu', title: '落款與尾批', image: '../storymap/辨識印刷字Label/落款與尾批.png', base: '../storymap/ocr-zhu25-printed-2-enhanced.png', colour: '#dfc484',
      desc: '官員落款、上奏日期與皇帝尾批各自有不同意義，不能在輸出時被壓成一段普通文字。',
      prompt: '分別保存官員上奏日期、皇帝硃批日期、尾批，不要混入正文。',
      code: '# 尾端欄位分開保存\ndoc["sent_date"] = extract_sent_date(tail)\ndoc["zhu_text"] = extract_zhu(tail)',
      json: '{ "sent_date": "乾隆五十一年十二月初十日",\n  "zhu_text": "已有旨了。欽此。" }'
    }
  ];

  const handwrittenFeatures = [
    {
      key: 'vertical', title: '直排單欄', image: '../storymap/辨識手寫字Label/直排單欄.png', base: '../storymap/ocr-zhu25-handwritten-3-enhanced.png', colour: '#7fb5b1',
      desc: '手寫奏摺採用直排書寫，閱讀方向由右至左、由上至下。OCR 必須按此順序輸出文字。',
      prompt: '奏摺用直排書寫，請按由右至左、由上至下的順序輸出文字。',
      code: '# 直排、由右至左\ncolumns = group_by_vertical_position(boxes)\ntext = read_right_to_left(columns)',
      json: '{ "text_direction": "vertical_rtl",\n  "column_count": 9 }'
    },
    {
      key: 'regular-script', title: '正文字體', image: '../storymap/辨識手寫字Label/正文字體.png', base: '../storymap/ocr-zhu25-handwritten-3-enhanced.png', colour: '#a28ca8',
      desc: '正文手寫字體與硃批、落款不同，應先分辨角色，再決定是否送入同一個 OCR 規則。',
      prompt: '辨識正文手寫字，與硃批、落款、印章分開處理，並保留原來的段落順序。',
      code: '# 不同書寫角色分開\nregions = classify_writing_regions(image)\nbody = ocr(regions["body"])',
      json: '{ "regions": {\n  "body": "handwritten",\n  "zhu": "separate"\n} }'
    },
    {
      key: 'author', title: '上奏官員', image: '../storymap/辨識手寫字Label/上奏官員.png', base: '../storymap/ocr-zhu25-handwritten-1-enhanced.png', colour: '#c88f8a',
      desc: '上奏官員姓名是文書的核心 metadata，不能只依 OCR 猜測，必須保留原文位置以便核對。',
      prompt: '辨識上奏官員，將官職與姓名分別輸出，並保留原文引文供研究者核驗。',
      code: '# 官職、姓名分開\ndoc["official_post"] = extract_post(header)\ndoc["author"] = extract_author(header)',
      json: '{ "official_post": "福建水師提督",\n  "author": "黃仕簡" }'
    },
    {
      key: 'minister', title: '臣字款', image: '../storymap/辨識手寫字Label/臣字款.png', base: '../storymap/ocr-zhu25-handwritten-1-enhanced.png', colour: '#6e98d0',
      desc: '臣字款是奏摺格式的線索。它屬於文書結構，不是普通正文。',
      prompt: '保留奏摺末端的臣字款，標記為 signoff，不要刪除或併入正文。',
      code: '# 臣字款另存\ndoc["signoff"] = find_signoff(image)\ndoc["body"] = remove_region(body, doc["signoff"] )',
      json: '{ "signoff": {\n  "kind": "臣字款",\n  "review": true\n} }'
    },
    {
      key: 'respect', title: '抬頭', image: '../storymap/辨識手寫字Label/抬頭.png', base: '../storymap/ocr-zhu25-handwritten-2-enhanced.png', colour: '#d97967',
      desc: '抬頭與避諱格式可以影響文字的實際位置和閱讀順序，應以版面標記保存。',
      prompt: '辨識抬頭，保留它在原頁面中的位置，並在 JSON 中標示版面角色。',
      code: '# 抬頭保留座標\nlayout.append({"kind": "respect", "bbox": bbox, "text": text})',
      json: '{ "layout": [{\n  "kind": "respect",\n  "text": "…"\n}] }'
    },
    {
      key: 'rescript', title: '硃批', image: '../storymap/辨識手寫字Label/硃批.png', base: '../storymap/ocr-zhu25-handwritten-4-enhanced.png', colour: '#c86f62',
      desc: '硃批是皇帝回應的原始文字，與臣下奏摺正文必須分開保存，並附上日期。',
      prompt: '辨識硃批，獨立輸出 zhu_date 與 zhu_text，不要混入奏摺正文。',
      code: '# 硃批獨立欄位\ndoc["zhu_date"] = extract_zhu_date(tail)\ndoc["zhu_text"] = extract_zhu_text(tail)',
      json: '{ "zhu_date": "乾隆五十一年十二月二十七日",\n  "zhu_text": "已有旨了。欽此。" }'
    },
    {
      key: 'watermark', title: '浮水印', image: '../storymap/辨識手寫字Label/浮水印.png', base: '../storymap/ocr-zhu25-handwritten-2-enhanced.png', colour: '#d7c47d',
      desc: '浮水印不是史料正文。可以遮蔽或標記它，但不要讓它被誤收進文字欄位。',
      prompt: '辨識浮水印，將它排除於正文文字之外，並在輸出中記錄處理方式。',
      code: '# 浮水印先遮蔽\nimage = mask_watermark(image)\nocr_result = ocr(image)',
      json: '{ "watermark": "excluded",\n  "review_note": "保留原圖" }'
    },
    {
      key: 'stamp', title: '印章', image: '../storymap/辨識手寫字Label/印章.png', base: '../storymap/ocr-zhu25-handwritten-4-enhanced.png', colour: '#d89a7e',
      desc: '印章是圖像區域，不應被當成正文辨識。研究者要同時保存它的存在與位置。',
      prompt: '忽略奏摺正文後的印章，記錄其頁面位置，不把它輸出成正文文字。',
      code: '# 印章遮蔽，不送入文字辨識\nstamp = detect_stamp(image)\nimage = mask_region(image, stamp.bbox)',
      json: '{ "stamp": {\n  "page": 6,\n  "excluded_from_text": true\n} }'
    }
  ];

  /* 印刷字與手寫字共用同一套探索器，只更換資料。 */
  $$('.feature-explorer[data-explorer]').forEach((explorer) => {
    const mode = explorer.dataset.explorer;
    const features = mode === 'handwritten' ? handwrittenFeatures : printedFeatures;
    const tabs = $('[data-explorer-tabs]', explorer);
    const index = $('[data-explorer-index]', explorer);
    const title = $('[data-explorer-title]', explorer);
    const description = $('[data-explorer-description]', explorer);
    const prompt = $('[data-explorer-prompt]', explorer);
    const code = $('[data-explorer-code]', explorer);
    const json = $('[data-explorer-json]', explorer);
    const image = $('[data-explorer-image]', explorer);
    const base = $('[data-explorer-base]', explorer);
    let current = 0;
    const selectFeature = (next) => {
      current = (next + features.length) % features.length;
      const feature = features[current];
      tabs.querySelectorAll('button').forEach((button, buttonIndex) => button.classList.toggle('is-active', buttonIndex === current));
      index.textContent = `${String(current + 1).padStart(2, '0')} / ${String(features.length).padStart(2, '0')}`;
      title.textContent = feature.title;
      description.textContent = feature.desc;
      prompt.textContent = feature.prompt;
      code.textContent = feature.code;
      json.textContent = feature.json;
      image.src = feature.image;
      image.alt = `人工標示的${feature.title}版面特徵`;
      image.style.setProperty('--feature-colour', feature.colour);
      base.src = feature.base;
    };
    features.forEach((feature, featureIndex) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = feature.title;
      button.addEventListener('click', () => selectFeature(featureIndex));
      tabs.appendChild(button);
    });
    selectFeature(0);
  });

  /* JSON 欄位導覽：這個互動視覺就是獨立頁相對舊版的主要補足。 */
  const jsonViewer = $('[data-json-viewer]');
  if (jsonViewer) {
    const fields = [
      ['source', '來源', '這份資料從哪裡來？保存書名、冊次或檔案來源，讓 OCR 文字能回到原件。'],
      ['title', '標題', '文書標題是檢索入口；不要讓它與正文第一段混在一起。'],
      ['official_post', '官職', '官職與姓名分開保存，方便後續按官員或職位查詢。'],
      ['author', '姓名', '上奏官員姓名來自原始文本；OCR 只提供候選，仍需回看原圖。'],
      ['sent_date', '具奏日期', '記錄奏摺的具奏日期，不要用其他事件日期替代。'],
      ['zhu_date', '硃批日期', '硃批日期是皇帝回應的時間欄位，與具奏日期分開。'],
      ['zhu_text', '硃批內容', '皇帝回應的原文要獨立保存，不能混進官員奏摺正文。'],
      ['page_numbers', '頁碼', '頁碼不是正文，但它讓研究者可以回到原件定位。'],
      ['paragraphs', '正文段落', '正文以段落陣列保存，後續才能逐段引用、搜尋與核驗。']
    ];
    const fieldHost = $('[data-json-fields]', jsonViewer);
    const lines = $$('[data-json-line]', jsonViewer);
    const previous = $('[data-json-nav="prev"]', jsonViewer);
    const next = $('[data-json-nav="next"]', jsonViewer);
    const explain = $('[data-json-explain]', jsonViewer);
    const expand = $('[data-json-expand]', jsonViewer);
    let current = 0;
    let expanded = false;
    fields.forEach(([key, label], fieldIndex) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'json-field-button';
      button.dataset.jsonTarget = key;
      button.textContent = label;
      button.addEventListener('click', () => selectField(fieldIndex));
      fieldHost.appendChild(button);
    });
    const selectField = (fieldIndex) => {
      current = Math.min(fields.length - 1, Math.max(0, fieldIndex));
      const [key, , description] = fields[current];
      fieldHost.querySelectorAll('button').forEach((button) => button.classList.toggle('is-active', button.dataset.jsonTarget === key));
      lines.forEach((line) => line.classList.toggle('is-active', line.dataset.jsonLine === key || (key === 'paragraphs' && line.dataset.jsonLine === 'paragraphs-2')));
      explain.textContent = description;
      previous.disabled = current === 0;
      next.disabled = current === fields.length - 1;
      const active = lines.find((line) => line.classList.contains('is-active'));
      active?.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    };
    previous.addEventListener('click', () => selectField(current - 1));
    next.addEventListener('click', () => selectField(current + 1));
    expand.addEventListener('click', () => {
      expanded = !expanded;
      const paragraphLine = lines.find((line) => line.dataset.jsonLine === 'paragraphs-2');
      paragraphLine?.classList.toggle('is-expanded', expanded);
      expand.textContent = expanded ? '收起較長段落' : '展開較長段落';
      if (expanded) explain.textContent = '完整結構會保留更多原文段落；教學畫面只顯示節錄，避免把視覺當成資料檔本身。';
    });
    selectField(0);
  }

  /* OCR 測試：把「先做少量頁面」做成一個可重播的流程。 */
  const batchBoard = $('[data-batch-board]');
  const batchButton = $('[data-run-batch]');
  if (batchBoard && batchButton) {
    const pages = $$('[data-batch-page]', batchBoard);
    const status = $('[data-batch-status]', batchBoard);
    let running = false;
    batchButton.addEventListener('click', () => {
      if (running) return;
      running = true;
      batchButton.disabled = true;
      pages.forEach((page) => { page.classList.remove('is-running', 'is-done'); page.querySelector('em').textContent = '待測'; });
      status.textContent = '逐頁檢查中…';
      pages.forEach((page, index) => {
        window.setTimeout(() => {
          page.classList.add('is-running');
          page.querySelector('em').textContent = '檢查中';
        }, index * 430);
        window.setTimeout(() => {
          page.classList.remove('is-running');
          page.classList.add('is-done');
          page.querySelector('em').textContent = '待核驗';
          if (index === pages.length - 1) {
            status.textContent = '測試批次完成 · 仍需人工核驗';
            running = false;
            batchButton.disabled = false;
          }
        }, index * 430 + 280);
      });
    });
  }

  const tryData = {
    printed: {
      label: '印刷字',
      pages: ['../storymap/試一試/印刷字/page1.png', '../storymap/試一試/印刷字/page2.png'],
      pdf: '../storymap/試一試/印刷字/為請酌籌加調官兵協力進剿事_印刷字.pdf',
      hotspots: {
        info: { left: '70%', top: '9%', width: '24%', height: '28%', colour: '#8fcfe0' },
        column: { left: '12%', top: '20%', width: '56%', height: '62%', colour: '#82adef' },
        page: { left: '6%', top: '88%', width: '14%', height: '7%', colour: '#bd70de' }
      }
    },
    handwritten: {
      label: '手寫字',
      pages: ['../storymap/試一試/手寫字/page1.png', '../storymap/試一試/手寫字/page2.png', '../storymap/試一試/手寫字/page3.png'],
      pdf: '../storymap/試一試/手寫字/為請酌籌加調官兵協力進剿事_手寫字.pdf',
      hotspots: {
        author: { left: '67%', top: '8%', width: '26%', height: '20%', colour: '#c88f8a' },
        vertical: { left: '12%', top: '15%', width: '68%', height: '69%', colour: '#7fb5b1' },
        zhu: { left: '12%', top: '59%', width: '58%', height: '26%', colour: '#c86f62' }
      }
    }
  };
  const tryLab = $('[data-try-lab]');
  if (tryLab) {
    const image = $('[data-try-image]', tryLab);
    const hotspots = $('[data-try-hotspots]', tryLab);
    const pageLabel = $('[data-try-page]', tryLab);
    const modeLabel = $('[data-try-mode-label]', tryLab);
    const progress = $('[data-try-progress]', tryLab);
    const stage = $('[data-try-stage]', tryLab);
    const feedback = $('[data-try-feedback]', tryLab);
    const stages = ['download', 'order', 'format', 'fields'];
    let mode = 'printed';
    let page = 0;
    let stageIndex = 0;
    const renderDocument = (activeHotspot = '') => {
      const data = tryData[mode];
      image.src = data.pages[page];
      image.alt = `試一試${data.label}史料頁面 ${page + 1}`;
      modeLabel.textContent = data.label;
      pageLabel.textContent = `頁 ${page + 1} / ${data.pages.length}`;
      hotspots.innerHTML = '';
      const box = data.hotspots[activeHotspot];
      if (box) {
        const mark = document.createElement('span');
        mark.className = 'try-hotspot is-active';
        mark.style.left = box.left;
        mark.style.top = box.top;
        mark.style.width = box.width;
        mark.style.height = box.height;
        mark.style.setProperty('--hotspot-color', box.colour);
        hotspots.appendChild(mark);
      }
    };
    const renderProgress = () => {
      progress.innerHTML = stages.map((_, index) => `<span class="try-progress-dot ${index < stageIndex ? 'is-done' : ''} ${index === stageIndex ? 'is-current' : ''}">${index < stageIndex ? '✓' : index + 1}</span>`).join('');
    };
    const setFeedback = (text, success = false) => {
      feedback.textContent = text;
      feedback.classList.toggle('is-success', success);
    };
    const optionButton = (label, value, correct, action) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'try-option';
      button.textContent = label;
      button.addEventListener('click', () => {
        if (correct) {
          button.classList.add('is-correct');
          action();
        } else {
          button.classList.add('is-wrong');
          setFeedback(`「${value}」不是這一步要保留的答案，請再看一次原件。`);
          window.setTimeout(() => button.classList.remove('is-wrong'), 400);
        }
      });
      return button;
    };
    const nextStage = () => { stageIndex += 1; renderStage(); };
    const renderStage = () => {
      renderProgress();
      setFeedback('');
      if (stageIndex === 0) {
        renderDocument('');
        stage.innerHTML = `<h3>第一步 · 下載史料</h3><p>先把這份史料下載到你的電腦。實際工作中，請確認檔案來源與使用權。</p><div class="try-file">${tryData[mode].pdf.split('/').pop()}</div><div class="try-stage-actions"><a class="button button-dark" href="${tryData[mode].pdf}" download>下載 ↧</a><button type="button" class="button button-quiet" data-try-confirm>已下載</button></div>`;
        $('[data-try-confirm]', stage).addEventListener('click', nextStage);
      } else if (stageIndex === 1) {
        renderDocument('column');
        stage.innerHTML = `<h3>第二步 · 先說清楚閱讀順序</h3><p>這份奏摺的正文要按照哪一個方向輸出？</p><div class="try-stage-actions" data-try-options></div>`;
        const options = $('[data-try-options]', stage);
        [['由右至左、由上至下', '由右至左', true], ['由左至右、由上至下', '由左至右', false], ['由下至上', '由下至上', false]].forEach(([label, value, correct]) => options.appendChild(optionButton(label, value, correct, nextStage)));
      } else if (stageIndex === 2) {
        renderDocument('info');
        stage.innerHTML = `<h3>第三步 · 指定輸出格式</h3><p>為了讓 Python、AI 和網站讀取，你要要求 AI 輸出哪一種格式？</p><div class="try-stage-actions" data-try-options></div>`;
        const options = $('[data-try-options]', stage);
        [['JSON', 'JSON', true], ['TXT', 'TXT', false], ['DOCX', 'DOCX', false]].forEach(([label, value, correct]) => options.appendChild(optionButton(label, value, correct, nextStage)));
      } else if (stageIndex === 3) {
        renderDocument('page');
        stage.innerHTML = `<h3>第四步 · 保留可核驗欄位</h3><p>請選出完成這份 OCR JSON 時不可省略的欄位。</p><div class="try-stage-actions" data-try-options></div>`;
        const options = $('[data-try-options]', stage);
        [['來源', 'source', true], ['正文段落', 'paragraphs', true], ['頁碼', 'page_numbers', true], ['只保留 AI 摘要', 'summary-only', false]].forEach(([label, value, correct]) => {
          const button = optionButton(label, value, correct, () => {
            button.dataset.selected = 'true';
            button.disabled = true;
            const selected = options.querySelectorAll('[data-selected="true"]');
            if (selected.length === 3) {
              stage.innerHTML += '<div class="try-stage-actions"><button type="button" class="button button-dark" data-try-finish>完成練習</button></div>';
              $('[data-try-finish]', stage).addEventListener('click', nextStage);
              setFeedback('三個必要欄位已選好。還要把 OCR 候選逐頁和原圖比對。', true);
            }
          });
          options.appendChild(button);
        });
      } else {
        renderDocument('');
        stage.innerHTML = '<h3>完成：先結構化，再分析</h3><p>你已把來源、版面規則與 JSON 輸出連成一條可核驗的流程。接下來才適合讓 AI 從結構化資料中抽取研究問題所需的資訊。</p><div class="try-stage-actions"><button type="button" class="button button-dark" data-try-reset>重新開始</button></div>';
        setFeedback('完成練習 · AI 候選仍不是研究者確認結果。', true);
        $('[data-try-reset]', stage).addEventListener('click', () => { stageIndex = 0; renderStage(); });
      }
    };
    $('[data-try-mode-switch]')?.addEventListener('click', (event) => {
      const button = event.target.closest('[data-try-mode]');
      if (!button) return;
      mode = button.dataset.tryMode;
      page = 0;
      stageIndex = 0;
      $$('[data-try-mode-switch] button').forEach((item) => item.classList.toggle('is-on', item.dataset.tryMode === mode));
      renderStage();
    });
    $$('[data-try-prev]').forEach((button) => button.addEventListener('click', () => { page = Math.max(0, page - 1); renderDocument(); }));
    $$('[data-try-next]').forEach((button) => button.addEventListener('click', () => { page = Math.min(tryData[mode].pages.length - 1, page + 1); renderDocument(); }));
    renderStage();
  }
})();
