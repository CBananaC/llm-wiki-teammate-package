const parts = [
  {
    id: 'intro-1-1', tab: '1.1', number: '1.1 / 制度', title: '清代奏折制度', tone: 'paper', mark: '奏',
    position: '--card-x: 8vw; --card-y: 13vh; --card-w: 540px; --story-height: 1120px; --card-accent: #b66d48;',
    paragraphs: [
      '清代的上行官方文書主要包括題本、奏本和奏折。題本用於正式公務，奏本用於官員私人事務。兩者送達中央後，均須經過內閣票擬，才會呈送到皇帝手上。',
      '相反，奏摺主要由皇帝親信及地方大員使用，並由官員親自撰寫，密封後直送至御前，由皇帝親自審閱和硃批。雍正設立軍機處後，批閱完成的奏摺會交由軍機處處理，如需另行頒旨，則由軍機大臣擬寫上諭，經皇帝閱定後，再由內閣明發或由軍機處廷寄地方。',
      '奏摺制度省去了內閣票擬等的中間程序，使皇帝得以更直接和迅速地與地方官員溝通，掌握地方政務，進一步強化中央集權，學界因此普遍認為，奏折是清代最重要的官方文書制度。'
    ]
  },
  {
    id: 'intro-1-2', tab: '1.2', number: '1.2 / 研究價值', title: '清代奏折上諭的研究價值', tone: 'network', mark: '網',
    position: '--card-x: 52vw; --card-y: 19vh; --card-w: 560px; --story-height: 960px; --card-accent: #c7543f;',
    paragraphs: [
      '在清史研究中，奏摺是極為重要的第一手史料。奏摺、硃批與上諭完整保存了中央與地方在政治決策過程中的原始通信記錄，呈現地方資訊如何透過奏摺上達御前、皇帝如何藉硃批與上諭下達命令，以及在後續奏報中，地方官員如何對這些命令作出回應。因此，透過分析特定議題的相關奏摺與上諭，研究者得以重構該議題的政治決策過程。'
    ]
  },
  {
    id: 'intro-1-3-a', tab: '1.3', nav: 'intro-1-3', number: '1.3 / 01', title: '研究清代奏折的主要困難', tone: 'ink', mark: '困',
    position: '--card-x: 9vw; --card-y: 12vh; --card-w: 570px; --story-height: 1040px; --card-accent: #a45e4c;',
    paragraphs: [{
      before: '然而，研究奏折與上諭有不少困難。首先，部分議題的奏摺與上諭數量極為龐大。以研究白蓮教戰爭為例，學者戴英從指出，該戰爭的重要史料《欽定剿平三省邪匪方略》共有六十九冊，超過二萬七千頁。',
      citation: { href: '../references.html#ref-dai-2019', text: '（戴英從，2019，第一章，頁碼待核）' },
      after: '收錄了四千多份奏摺和上諭，篇幅之大令人望而卻步，當代學者對白蓮教戰爭的研究因此相當有限。'
    }]
  },
  {
    id: 'intro-1-3-b', tab: '1.3', nav: 'intro-1-3', number: '1.3 / 02', title: '研究清代奏折的主要困難', tone: 'gold', mark: '信',
    position: '--card-x: 48vw; --card-y: 18vh; --card-w: 570px; --story-height: 1040px; --card-accent: #ad7a35;',
    note: '通信關係的第二個層次',
    paragraphs: [
      '另外，奏摺與上諭之間涉及複雜的通信關係。最基本的一層，是地方官員奏報，皇帝再透過硃批或上諭作出回覆。然而，研究者不僅需要掌握每份奏摺和上諭的收發時間，也要釐清一份奏摺是否回應先前的硃批或上諭，以及皇帝發布的命令又在何時、由哪些官員於後續奏報中作出回應。'
    ]
  },
  {
    id: 'intro-1-3-c', tab: '1.3', nav: 'intro-1-3', number: '1.3 / 03', title: '研究清代奏折的主要困難', tone: 'river', mark: '流',
    position: '--card-x: 8vw; --card-y: 12vh; --card-w: 600px; --story-height: 1160px; --card-accent: #4d817c;',
    note: '事件、消息來源與資訊網絡',
    paragraphs: [
      '此外，針對奏摺所載的具體事件，研究者還要關注事件的發生時間及消息來源。而皇帝往往又會同時收到多位官員就同一事件的奏報，各奏報的的描述及消息來源都不盡相同，形成了錯綜複雜的消息網絡。',
      '因此，研究者既要分析單份文書所載的資訊，也要理解宏觀的資訊傳遞網絡。然而，面對大量文書及複雜的通信關係，研究者難以單憑人力掌握資訊傳遞的整體脈絡，因此需要運用視覺化工具，呈現文書之間的關聯與資訊流向。'
    ]
  },
  {
    id: 'intro-1-4', tab: '1.4', number: '1.4 / 數位方法', title: '以數位方法研究清代奏折和上諭', tone: 'archive', mark: 'AI',
    position: '--card-x: 7vw; --card-y: 13vh; --card-w: 470px; --story-height: 1200px; --card-accent: #7e6a39;',
    paragraphs: [
      '筆者認為，人工智能（AI）與視覺化的數位工具，能夠協助研究者處理上述的兩大難題，包括：'
    ],
    table: [
      ['研究困難', '數位工具', '如何協助研究'],
      ['史料數量龐大', 'AI', '總結長篇文本，協助研究者迅速掌握文書的主要內容，並判斷其中是否包含值得深入閱讀與分析的資訊。'],
      ['史料數量龐大', '人工智能技能（AI Skills）', '按照不同研究問題設計技能，讓AI從文本中提取特定資訊，並由研究者核對、審核及修正。'],
      ['通信關係複雜', 'Python 文本搜尋', '搜尋文書中的特定字詞，辨識奏摺與上諭之間的回應關係，重構官員與皇帝之間的資訊傳遞過程。'],
      ['通信關係複雜', '互動式網站', '以時間線和關係網絡等視覺化工具，呈現文書的收發時間及資訊傳遞的流向，協助研究者掌握宏觀的通信網絡。']
    ]
  },
  {
    id: 'intro-1-5', tab: '1.5', number: '1.5 / 研究成果', title: '研究成果：「清代奏摺與上諭分析平台」', tone: 'review', mark: '台',
    position: '--card-x: 6vw; --card-y: 11vh; --card-w: 500px; --story-height: 1120px; --card-accent: #c46a2b;',
    paragraphs: [
      '基於上述理念，筆者建立了一個結合人工智能與視覺化工具的研究網站，作為研究奏摺與上諭的輔助平台。',
      '網站能夠載入大量文書，運用人工智能提取特定資訊，供研究者核對和分析；同時透過時間線和關係網絡等視覺化工具，呈現皇帝與官員之間的文書傳遞關係及資訊流向。',
      '透過上述功能，研究者既可從微觀層面閱讀單份文書的原文與資訊提取結果，亦可掌握宏觀的通信脈絡及資訊傳遞過程。'
    ],
    review: true
  },
  {
    id: 'intro-1-6-a', tab: '1.6', nav: 'intro-1-6', number: '1.6 / 示範案例', title: '示範案例：林爽文事件', tone: 'taiwan', mark: '林',
    position: '--card-x: 50vw; --card-y: 12vh; --card-w: 590px; --story-height: 1120px; --card-accent: #c7543f;',
    paragraphs: [
      '為展示本網站的研究方法及各項功能，本文將以林爽文民變作為示範案例。林爽文民變於乾隆五十一年（1786）爆發，歷時約兩年，由天地會領袖林爽文在臺灣中部的彰化發動，並迅速蔓延至臺灣多地，最終促使清廷派遣福康安率軍來臺鎮壓。乾隆帝其後將平定此役列為「十全武功」之一。'
    ]
  },
  {
    id: 'intro-1-6-b', tab: '1.6', nav: 'intro-1-6', number: '1.6 / 原因 01', title: '示範案例：林爽文事件', tone: 'network', mark: '延',
    position: '--card-x: 8vw; --card-y: 10vh; --card-w: 610px; --story-height: 1260px; --card-accent: #b66d48;',
    note: '選取林爽文民變作為示範案例，主要有以下原因：',
    paragraphs: [
      '第一，資訊傳遞是戰時軍事決策形成的重要環節。戰爭期間，地方官員須持續透過奏摺向皇帝奏報軍情、兵力部署及戰場變化，而皇帝則根據奏報發布上諭，指示軍事部署及後續行動，形成地方與中央之間持續往返的決策過程。然而，林爽文民變發生於臺灣，與北京相距遙遠，文書傳遞往往需時數星期。當皇帝收到奏摺時，前線局勢很可能已經改變，軍事決策因此仰賴前線官員臨機處置。因此，林爽文民變是一個合適的研究案例，用來探討資訊傳遞延遲如何影響戰時軍事決策的形成與執行。'
    ]
  },
  {
    id: 'intro-1-6-c', tab: '1.6', nav: 'intro-1-6', number: '1.6 / 原因 02', title: '示範案例：林爽文事件', tone: 'gold', mark: '史',
    position: '--card-x: 47vw; --card-y: 12vh; --card-w: 610px; --story-height: 1260px; --card-accent: #ad7a35;',
    paragraphs: [
      '第二，林爽文民變保存了大量奏摺與上諭，完整記錄戰時地方官員與皇帝之間的通信過程，為研究提供了豐富的材料。本研究主要採用《明清臺灣檔案彙編》（臺灣史料集成編輯委員會編）及《天地會檔案彙編》（中國人民大學清史研究所、中國第一歷史檔案館編）所收錄的奏摺和上諭。這些史料均經當代學者整理、校勘及出版，完整保留文書原文、文書類型、收發日期及硃批等重要資訊，為研究提供了可靠的材料。'
    ]
  }
];

const part1Parts = [
  {
    id: 'part-1-areas', tab: 'part-1', number: '1 / 四大區域', title: '平台的四大區域', tone: 'network', mark: '四',
    position: '--card-x: 7vw; --card-y: 13vh; --card-w: 620px; --story-height: 1220px; --card-accent: #4d817c;',
    paragraphs: ['平台介面主要由四個區域組成，分別是導覽列、時間與關係圖表、原始史料區，以及AI分析區。'],
    subsections: [
      { title: '導覽列', paragraphs: ['介面區域切換、資料輸入與輸出，以及修改顯示設定。'] },
      { title: '時間與關係圖表', paragraphs: ['呈現文書與事件的時間順序及相互聯繫。'] },
      { title: '原始史料區', paragraphs: ['顯示文書的基本資料及完整原文。'] },
      { title: 'AI 分析區', paragraphs: ['展示人工智能從文書中提取的資訊，供研究者檢視。'] }
    ]
  },
  {
    id: 'part-1-navigation', tab: 'part-1', number: '2 / 導覽列', title: '導覽列', tone: 'archive', mark: '列',
    position: '--card-x: 49vw; --card-y: 14vh; --card-w: 600px; --story-height: 1320px; --card-accent: #7e6a39;',
    subsections: [
      {
        title: '1. 輸入與輸出資料',
        paragraphs: ['研究者可以從本機輸入結構化的原始文本和AI 分析結果；完成檢視和修改後，亦可以將結構化資料輸出至本機，供後續研究使用。']
      },
      {
        title: '2. 切換介面區域',
        paragraphs: ['研究者可以透過導覽列切換不同的介面區域。例如，在閱讀原文後，開啟 AI 分析區，檢視人工智能提取的資訊，同時開啟筆記頁，記錄閱讀所得，並在完成審閱後，點擊「事件鏈」，沿著事件的時間順序，追蹤戰場消息如何向上傳遞、皇帝的命令如何向下傳達，以及官員如何回應先前的硃批或上諭。']
      }
    ]
  },
  {
    id: 'part-1-timeline', tab: 'part-1', number: '3 / 時間與關係圖表', title: '時間與關係圖表', tone: 'river', mark: '時',
    position: '--card-x: 7vw; --card-y: 12vh; --card-w: 650px; --story-height: 1420px; --card-accent: #4d817c;',
    paragraphs: [
      '時間與關係圖表位於介面的主要區域，用以呈現文書和事件的時間及傳遞關係。',
      '時間與關係圖表由四條事件線組成，中間兩條線「官員上奏」及「皇帝硃批下旨」呈現文書的發送及接收時間，資料來源自原始文本中已有的收發時間。一個節點代表一份文書。',
      '兩側的事件線是「奏報事件」和「皇帝行動」，其中的節點分別由「官員上奏」和「皇帝硃批下旨」的節點延伸而成。這些事件首先由 AI 從原始文書中提取，再由研究者閱讀原文查證，經確認後，才會以節點形式加入圖表。',
      '四條線上的文書和事件節點，會按照時間順序排列，並透過連線呈現彼此的傳遞關係。',
      '研究者可以點擊任何節點，查看該文書或事件的詳細資料，或進一步點擊「事件鏈」，沿著時間順序，了解相關文書和事件的具體傳遞關係。'
    ]
  },
  {
    id: 'part-1-node', tab: 'part-1', number: '5 / 節點資訊區', title: '節點資訊區', tone: 'ink', mark: '節',
    position: '--card-x: 52vw; --card-y: 15vh; --card-w: 560px; --story-height: 900px; --card-accent: #a45e4c;',
    paragraphs: ['當研究者點擊圖表上的節點時，介面會開啟獨立的資訊面板，顯示該節點的完整 AI 提取結果，包括標題、描述、時間、原文引文及史料來源。']
  },
  {
    id: 'part-1-original', tab: 'part-1', number: '6 / 原始史料區', title: '原始史料區', tone: 'paper', mark: '原',
    position: '--card-x: 8vw; --card-y: 13vh; --card-w: 620px; --story-height: 1080px; --card-accent: #b66d48;',
    paragraphs: [
      '文書區顯示原始文書的完整原文及基本資料，包括標題、文書類型、作者、收發日期和史料出處。',
      '文書區亦設有篩選功能，用以標示不同 AI Skills 的提取結果。研究者可以點擊相關結果的標籤，查看該項結果的完整資訊。'
    ]
  },
  {
    id: 'part-1-ai', tab: 'part-1', number: '7 / 人工智能分析區', title: '人工智能分析區', tone: 'gold', mark: 'AI',
    position: '--card-x: 48vw; --card-y: 13vh; --card-w: 650px; --story-height: 1260px; --card-accent: #ad7a35;',
    paragraphs: [
      '研究者可以在本機執行 AI Skills，並將整理後的結構化結果上載至網站。上載後，分析結果會以卡片形式顯示於 AI Chat 面板中。',
      '每張卡片均會列出相關原文引文。研究者可以點擊引文，返回原始文書的相應位置進行核對。',
      '確認結果後，研究者可以將其加入圖表，作為獨立事件或事件中的相關資訊；如結果需要修正，研究者可以編輯或拒絕該結果，亦可以手動新增事件。'
    ]
  }
];

const part2Parts = [
  {
    id: 'part-2-overview', tab: 'part-2', number: '1 / 平台的運作流程', title: '1. 平台的運作流程', tone: 'archive', mark: '流',
    position: '--card-x: 7vw; --card-y: 13vh; --card-w: 640px; --story-height: 1100px; --card-accent: #7e6a39;',
    paragraphs: [
      '因此，平台運用人工智能協助研究者總結文書內容、提取重要資訊，供研究者進一步檢視和核驗，從而減輕整理史料的工作量。',
      '同時，平台亦運用視覺化工具，透過時間與關係圖表呈現資訊的傳遞網絡，協助研究者掌握文書和事件的時間順序和相互關係。'
    ]
  },
  {
    id: 'part-2-flow', tab: 'part-2', number: '3 / 運作流程圖', title: '3. 運作流程圖', tone: 'network', mark: '圖',
    position: '--card-x: 49vw; --card-y: 15vh; --card-w: 660px; --story-height: 900px; --card-accent: #c7543f;',
    paragraphs: [
      '輸入結構化的原始文書 → AI Skills → 1. 總結文書、2. 重構文書間的通訊關係、3. 收取奏摺的資訊、4. 收取上諭的資訊→載入分析結果 → 研究者審閱 →結果載入至圖表中呈現'
    ]
  },
  {
    id: 'part-2-input', tab: 'part-2', number: '4 / 輸入結構化資料', title: '4. 輸入結構化資料', tone: 'paper', mark: '資', coverBar: true,
    position: '--card-x: 7vw; --card-y: 38vh; --card-w: 650px; --story-height: 1450px; --card-accent: #b66d48;',
    paragraphs: [
      '在選定研究主題及所使用的奏摺與上諭後，第一步是對史料進行 OCR，並把結果輸出為結構化 的JSON 資料，再載入到平台之中。（由於 OCR 並不是本網站內置的功能，相關方法將留待下一節「重用平台於其他研究主題」中再作介紹。）',
      '在結構化資料中，每份奏摺或上諭都需要分成不同欄位，包括文書類型、作者資料、標題、文書編號、文書正文及史料來源。',
      '如果史料來自學者編纂的檔案彙編，通常都會清楚標示文書的發送和接收日期，因此亦應加入相關日期的欄位。這些日期資料可以用於排列文書的時間順序，以及重建文書之間的傳遞關係。',
      '輸入後，網站會讀取這些欄位，並根據文書的收發日期，在時間與關係圖表上建立各份文書的節點；同時，文書區亦會顯示文書的基本資料及完整原文。'
    ]
  },
  {
    id: 'part-2-ai', tab: 'part-2', number: '5 / 使用AI從原文中抽取資訊', title: '5. 使用AI從原文中抽取資訊', tone: 'gold', mark: 'AI', coverBar: true,
    position: '--card-x: 48vw; --card-y: 38vh; --card-w: 670px; --story-height: 1450px; --card-accent: #ad7a35;',
    paragraphs: ['完成輸入結構化原始文書後，下一步便是運用 AI 和AI Skills，從史料中提取特定的資訊。'],
    subsections: [
      {
        title: '1. AI Skills',
        paragraphs: [
          'AI Skills 是一套預先設計的 AI 指令，讓人工智能按照指定規則處理數據，提取指定資料，並以特定格式輸出結果。',
          '平台中的 AI Skills 是根據特定研究問題設計的，要求 AI 從文書中找出與研究問題相關的資訊，並保留相應的原文引文作為證據。'
        ]
      },
      {
        title: '2. 資訊提取的核心理念',
        paragraphs: ['平台視 AI 為協助研究的工具，AI 提取的結果需要由研究者作出最後判斷。因此，在 AI 輸出結果後，研究者需要回到原始文書，檢查結果是否準確。相關資訊要經研究者確認，才會加入到圖表之中，成為後續研究和分析的一部分。']
      },
      {
        title: '3. 四個分析階段',
        paragraphs: ['平台共有四組 AI Skills，分別用於四個分析階段：總結文書、重建通信關係、提取奏摺資訊，以及提取上諭資訊。']
      }
    ]
  },
  {
    id: 'part-2-summary', tab: 'part-2', number: '1 / 總結文書', title: '1.  總結文書', tone: 'paper', mark: '總', coverBar: true,
    position: '--card-x: 7vw; --card-y: 38vh; --card-w: 650px; --story-height: 1050px; --card-accent: #b66d48;',
    paragraphs: [
      '第一組 AI Skills 負責總結文書。AI 會先將整份文書概括為一段摘要，再按照內容和功能將原文劃分成不同部分，並為每一部分提供簡短的標題和摘要。',
      '摘要和分段結果會顯示在原始文書區中，供研究者在完整閱讀原文前快速瀏覽，掌握文書的主要內容和結構。'
    ]
  },
  {
    id: 'part-2-communication', tab: 'part-2', number: '2 / 重建通信關係', title: '2. 重建通信關係', tone: 'network', mark: '關', coverBar: true,
    position: '--card-x: 48vw; --card-y: 38vh; --card-w: 670px; --story-height: 1050px; --card-accent: #c7543f;',
    paragraphs: [
      '在奏摺和上諭的結尾，通常會標示奏摺的發送日期、硃批日期及上諭的發布日期。平台會利用這些日期建立文書之間的時間順序及收發關係，形成通信網絡的第一層。',
      '然而，文書之間還存在更深層的通訊關係，例如奏摺是否回應了先前的上諭或硃批，以及上諭是否回應了先前收到的奏摺。這便需要從文書正文中尋找相關線索，並與其他文書相互比對，才能確認和重建這些更深層的關係。',
      '平台因此設有兩種的 Skills，分別用於辨識一份奏摺所回應的硃批或上諭，以及辨識一份上諭所回應的奏摺。'
    ]
  },
  {
    id: 'part-2-yu-response', tab: 'part-2', number: '1 / 辨識奏摺所回應的上諭', title: '1. 辨識奏摺所回應的上諭', tone: 'gold', mark: '諭',
    position: '--card-x: 7vw; --card-y: 14vh; --card-w: 680px; --story-height: 1650px; --card-accent: #ad7a35;',
    paragraphs: [
      '「上諭—回應配對」Skill 會根據以下線索，辨識一份奏摺所回應的上諭：',
      '首先，官員在奏摺中回應皇帝的上諭時，通常會使用「奉上諭」、「奉聖諭」、「聖諭」、「奉廷寄」、「欽奉諭旨」或「欽奉上諭」等引述標記，並在標記前寫明上諭的發出日期，再引用上諭的內容，部分也會使用「接奉」、「接准」或「敬奉」等的標記，注明自己收到上諭的日期。因此，平台會先利用 Python 從原始文書中擷取這些標記、引文和日期，再與較早的上諭內容作出比較。',
      '系統會根據三項條件篩選候選文書。第一，上諭的發佈日期必須和「奉上諭」標記前的日期相符；第二，奏摺作者應為上諭的受文官員之一；第三，奏摺中的上諭引文必須與候選上諭的內容完全或大致相同。',
      'AI 會輸出結構化的結果，列出相配的上諭和奏摺，並提供兩份文書中的引文和關鍵日期，包括上諭的發佈日期、官員的收到日期和回覆日期，供研究者查核。研究者確認無誤後，便可以把通信關係加入到圖表中。'
    ]
  },
  {
    id: 'part-2-zhu-response', tab: 'part-2', number: '2 / 辨識奏摺所回應的硃批', title: '2. 辨識奏摺所回應的硃批', tone: 'ink', mark: '批',
    position: '--card-x: 50vw; --card-y: 14vh; --card-w: 620px; --story-height: 920px; --card-accent: #a45e4c;',
    paragraphs: [
      '在回應皇帝的硃批時，官員同樣會用「奉硃批」、「奉到硃批」、「敬奉硃批」、「欽奉硃批」或「蒙硃批」等引述標記，再引用硃批原文。因此，辨識奏摺所回應硃批的 Skill，其方法和判斷邏輯與「上諭—回應配對」基本相同。'
    ]
  },
  {
    id: 'part-2-yu-source', tab: 'part-2', number: '3 / 辨識上諭所回應的奏摺', title: '3. 辨識上諭所回應的奏摺', tone: 'river', mark: '源',
    position: '--card-x: 7vw; --card-y: 14vh; --card-w: 690px; --story-height: 2050px; --card-accent: #4d817c;',
    paragraphs: [
      '系統會使用「上諭來源配對」Skill 辨識上諭所回應的奏摺。',
      '在評論官員奏報和下達命令前，上諭通常會先使用「據某人奏」、「據某人馳奏」或「據某人奏稱」等引述標記，交代皇帝所收到的官員奏報。',
      '然而，與回應上諭的奏摺不同，上諭通常不會註明皇帝何時收到相關奏摺，以及相關奏摺的發送日期。',
      '此外，同一項資訊可能由多位官員奏報，而上諭卻大多只會使用「據某人等奏稱」或「據奏」的標記，不會列出所有的奏報官員。因此，不能只用 Python 擷取人名或標記，來確定上諭所回應的奏摺。',
      '儘管如此，上諭通常會回應最新收到的奏報，平台會先利用 Python搜尋上諭發布當日，以及發布前5日內收到的奏摺，作為後續分析的候選文本。',
      '接著，系統會運用 AI，先提取上諭中有「據奏」標記的資訊，再閱讀每份候選奏摺的正文，判斷該資訊出現於哪一份或哪些奏摺之中，從以辨識哪些奏摺是上諭的回應對象。'
    ]
  },
  {
    id: 'part-2-extract', tab: 'part-2', number: '3 / 抽取奏摺的資訊', title: '3. 抽取奏摺的資訊', tone: 'archive', mark: '取', coverBar: true,
    position: '--card-x: 48vw; --card-y: 38vh; --card-w: 670px; --story-height: 1050px; --card-accent: #7e6a39;',
    paragraphs: [
      '完成通信關係重建後，平台會進一步從奏摺和上諭正文中的資訊。',
      '系統把奏摺內容劃分為四類資訊：官員奏報的事件、奏報者與其他官員對事件的回應、以上兩種資訊的來源，以及官員對皇帝先前硃批或上諭的回應。系統會用四種Skills 讓AI抽取以上資訊。'
    ]
  },
  {
    id: 'part-2-events', tab: 'part-2', number: '1 / 抽取官員奏報的事件、官員對事件的回應', title: '1. 抽取官員奏報的事件、官員對事件的回應', tone: 'taiwan', mark: '事',
    position: '--card-x: 7vw; --card-y: 14vh; --card-w: 700px; --story-height: 1700px; --card-accent: #c7543f;',
    paragraphs: [
      '在林爽文民變的案例中，官員奏報的事件就是林爽文及其部眾的軍事行動，官員的回應則包括已採取或計劃採取的軍事行動，以及非軍事措施（如後勤調度、案件調查）。',
      '所有事件和回應皆由AI提取，並以結構化格式輸出，包含標題、描述、發生時間及相關引文，供研究者核對、修正及確認。確認無誤後，研究者便可把事件加入到平台的第一條時間線——「戰場事件」上。',
      '考慮到每類事件（如軍事事件）包含的細類眾多（如攻城、防守、追捕等），研究者可根據研究需要，在 Skills 中預先限定需抽取的事件類型及細類，亦可不設限制，由讓AI自行判斷和抽取，再由研究者選擇採用的抽取結果。',
      '另外，如何在Skills中定義「事件」亦值得注意。事件可以按時間單位（如時辰、日期）劃分，也可以按事件的邏輯關係（如同一任務）劃分。不同的定義會影響 AI 提取事件的「粒度」（Granularity）。研究者應根據研究需要，在 Skills 中定義事件的劃分方式。'
    ]
  },
  {
    id: 'part-2-sources', tab: 'part-2', number: '2 / 追溯資訊的來源', title: '2. 追溯資訊的來源', tone: 'paper', mark: '源',
    position: '--card-x: 49vw; --card-y: 14vh; --card-w: 650px; --story-height: 1200px; --card-accent: #b66d48;',
    paragraphs: [
      '完成抽取事件後，系統會用「來源鏈追溯」Skill，逐層追溯不同事件的資訊來源。',
      'AI 會根據文書中的資訊傳遞標記，識別表示消息來源的文句，例如「字寄」、「咨」、「移會」、「稟」、「據某人稟」、「接據某人」等。',
      '不少資訊並非直接來自奏摺作者，而是經多人逐層轉報，AI因此會追蹤資訊由最初報告者逐步傳遞至奏摺作者的過程，重建完整的傳遞鏈，例如「甲 → 乙 → 丙 → 奏摺作者」。'
    ]
  },
  {
    id: 'part-2-yu-info', tab: 'part-2', number: '4 / 收取上諭的資訊', title: '4. 收取上諭的資訊', tone: 'ink', mark: '諭', coverBar: true,
    position: '--card-x: 7vw; --card-y: 38vh; --card-w: 700px; --story-height: 1750px; --card-accent: #a45e4c;',
    subsections: [
      {
        title: '1.皇帝上諭對官員奏摺的回應',
        paragraphs: [
          '完成提取奏摺中的事件和來源後，系統可以使用 `extract-yu-emperor-actions.md`，根據先前階段已確認的「上諭回應奏摺」關係，取得相應的上諭，分析皇帝如何回應奏摺中的內容。',
          '每份上諭可以產生多項回應的結果，AI 會將每項結果整理成結構化資料，包括上諭、硃批和奏摺中的相關引文，並說明皇帝如何針對奏摺作出評論或命令。'
        ]
      },
      {
        title: '2. 官員對皇帝上諭的回應',
        paragraphs: ['同樣，系統亦可以執行 confirmed-yu-response-analysis.md Skill，根據先前階段已確認的「奏摺回應上諭」關係，取得相關的奏摺，分析官員後續如何就上諭中的評論、命令作出回應。']
      },
      {
        title: '3. 上諭中皇帝所知的事件',
        paragraphs: ['除此之外，在單獨分析上諭時，系統亦可以執行 extract-yu-reported-events.md Skill，根據「據奏」等引述標記，辨識皇帝從官員奏報中得知的事件；再根據先前已確認的「上諭來源配對」關係，從相關奏摺中找出報告這些事件的原文，追溯情報的來源。']
      }
    ]
  },
  {
    id: 'part-2-visualize', tab: 'part-2', number: '4 / 視覺化呈現分析的結果', title: '4. 視覺化呈現分析的結果', tone: 'network', mark: '呈', coverBar: true,
    position: '--card-x: 48vw; --card-y: 38vh; --card-w: 680px; --story-height: 1100px; --card-accent: #c7543f;',
    paragraphs: [
      'AI 完成資訊抽取後，研究者可把分析結果匯入至平台，逐一與原文比對，並選擇接受、修改或拒絕結果。系統為被採用的結果，在圖表中建立相應的節點及連線，形成事件與文書之間的關係網絡。',
      '研究者亦可以點擊圖表上的文書或事件節點，查看其詳細資料、原文引文和資料來源，也可以開啟事件鏈，沿著時間順序追蹤一項事件由最初的報告者傳遞至官員和皇帝的過程。'
    ]
  }
];

const escapeHtml = (value) => String(value).replace(/[&<>"']/g, (char) => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[char]));
const paragraphHtml = (paragraphs) => paragraphs.map((paragraph) => {
  if (typeof paragraph === 'string') return `<p>${escapeHtml(paragraph)}</p>`;
  const citation = paragraph.citation
    ? `<a class="inline-reference" href="${escapeHtml(paragraph.citation.href)}">${escapeHtml(paragraph.citation.text)}</a>`
    : '';
  return `<p>${escapeHtml(paragraph.before || '')}${citation}${escapeHtml(paragraph.after || '')}</p>`;
}).join('');
const subsectionHtml = (subsections = []) => subsections.map((subsection) => `<h3>${escapeHtml(subsection.title)}</h3>${paragraphHtml(subsection.paragraphs)}`).join('');
const tableHtml = (rows) => `<table class="method-table"><thead><tr>${rows[0].map((cell) => `<th scope="col">${escapeHtml(cell)}</th>`).join('')}</tr></thead><tbody>${rows.slice(1).map((row) => `<tr>${row.map((cell) => `<td>${escapeHtml(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
const backdropHtml = (part) => {
  if (part.review) {
    return `<div class="backdrop review-backdrop" data-mark="台"><div class="review-window"><iframe class="review-iframe" data-file-src="../../../review-tools/(2)%20sample/index.html?embed=1&amp;doc=%E7%A1%83%38%33&amp;panels=ai%2Coriginal&amp;v=20260728-chat-data" title="硃83 AI 引文核驗示例"></iframe></div></div>`;
  }
  if (part.table) return `<div class="backdrop method-backdrop" data-mark="AI">${tableHtml(part.table)}</div>`;
  if (part.tone === 'signal') return `<div class="backdrop signal-backdrop" data-mark="流"><div class="signals"><span class="signal-label one">地方奏報</span><span class="signal-label two">皇帝回應</span><span class="signal-label three">後續回應</span></div></div>`;
  return `<div class="backdrop ${part.tone}" data-mark="${escapeHtml(part.mark)}"></div>`;
};
const partHtml = (part) => `<section class="story content-story${part.coverBar ? ' cover-bar-story' : ''}" id="${part.id}" data-tab="${part.tab}" data-nav="#${part.nav || part.id}" style="${part.position}">${backdropHtml(part)}${part.coverBar ? `<div class="cover-bar" data-mark="${escapeHtml(part.mark)}"><h2>${escapeHtml(part.title)}</h2></div>` : ''}<article class="story-card">${part.coverBar ? '' : `<h2>${escapeHtml(part.title)}</h2>`}${part.note ? `<div class="part-note">${escapeHtml(part.note)}</div>` : ''}${paragraphHtml(part.paragraphs || [])}${subsectionHtml(part.subsections)}</article></section>`;
document.getElementById('intro-content').innerHTML = parts.map(partHtml).join('');
document.getElementById('part-1-content').innerHTML = part1Parts.map(partHtml).join('');
document.getElementById('part-2-content').innerHTML = part2Parts.map(partHtml).join('');

const setReviewFrameSource = () => {
  const frame = document.querySelector('.review-iframe');
  if (!frame) return;
  frame.src = location.protocol === 'file:'
    ? frame.dataset.fileSrc
    : 'http://127.0.0.1:8766/sample?embed=1&doc=%E7%A1%83%38%33&panels=ai%2Coriginal&v=20260728-chat-data';
};
setReviewFrameSource();

const settingsButton = document.getElementById('settings-button');
const settingsPanel = document.getElementById('site-settings-panel');
const fontSizeDecrease = document.getElementById('font-size-decrease');
const fontSizeIncrease = document.getElementById('font-size-increase');
const fontSizeValue = document.getElementById('font-size-value');
const FONT_SCALE_KEY = 'intro-website-font-scale';
const FONT_SCALE_MIN = 0.55;
const FONT_SCALE_MAX = 2.2;
const FONT_SCALE_STEP = 0.05;
const clampFontScale = (value) => Math.min(FONT_SCALE_MAX, Math.max(FONT_SCALE_MIN, value));
const readFontScale = () => {
  try {
    const saved = Number.parseFloat(localStorage.getItem(FONT_SCALE_KEY));
    return Number.isFinite(saved) ? clampFontScale(saved) : 1;
  } catch (error) {
    return 1;
  }
};
const applyFontScale = (value) => {
  const scale = clampFontScale(value);
  document.documentElement.style.setProperty('--font-scale', String(scale));
  fontSizeValue.value = `${Math.round(scale * 100)}%`;
  fontSizeValue.textContent = fontSizeValue.value;
  fontSizeDecrease.disabled = scale <= FONT_SCALE_MIN;
  fontSizeIncrease.disabled = scale >= FONT_SCALE_MAX;
  try {
    localStorage.setItem(FONT_SCALE_KEY, String(scale));
  } catch (error) {
    // Continue without persistence when storage is unavailable.
  }
};
const setSettingsOpen = (open) => {
  settingsPanel.hidden = !open;
  settingsButton.setAttribute('aria-expanded', String(open));
  settingsButton.setAttribute('aria-label', open ? '關閉網站設定' : '開啟網站設定');
};
applyFontScale(readFontScale());
settingsButton.addEventListener('click', () => setSettingsOpen(settingsPanel.hidden));
fontSizeDecrease.addEventListener('click', () => applyFontScale(readFontScale() - FONT_SCALE_STEP));
fontSizeIncrease.addEventListener('click', () => applyFontScale(readFontScale() + FONT_SCALE_STEP));
document.addEventListener('click', (event) => {
  if (!settingsPanel.hidden && !event.target.closest('.settings-wrap')) setSettingsOpen(false);
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !settingsPanel.hidden) {
    setSettingsOpen(false);
    settingsButton.focus();
  }
});

const tabs = [...document.querySelectorAll('.main-nav-link')];
const tabPanels = [...document.querySelectorAll('[data-tab-panel]')];
const introDropdown = document.querySelector('.nav-dropdown');
const introDropdownTrigger = introDropdown.querySelector('.nav-dropdown-trigger');
const introDropdownMenu = introDropdown.querySelector('.nav-dropdown-menu');
const workflowNodes = [...document.querySelectorAll('.workflow-node')];
let introDropdownCloseTimer;
const setIntroDropdownOpen = (open) => {
  window.clearTimeout(introDropdownCloseTimer);
  introDropdown.classList.toggle('open', open);
  introDropdownTrigger.setAttribute('aria-expanded', String(open));
};
introDropdown.addEventListener('mouseenter', () => setIntroDropdownOpen(true));
const scheduleIntroDropdownClose = () => {
  window.clearTimeout(introDropdownCloseTimer);
  introDropdownCloseTimer = window.setTimeout(() => {
    const pointerInside = introDropdown.matches(':hover') || introDropdownMenu.matches(':hover');
    const focusInside = introDropdown.contains(document.activeElement);
    if (!pointerInside && !focusInside) setIntroDropdownOpen(false);
  }, 80);
};
introDropdown.addEventListener('mouseleave', scheduleIntroDropdownClose);
introDropdownMenu.addEventListener('mouseenter', () => setIntroDropdownOpen(true));
introDropdownMenu.addEventListener('mouseleave', scheduleIntroDropdownClose);
introDropdown.addEventListener('focusin', () => setIntroDropdownOpen(true));
introDropdown.addEventListener('focusout', scheduleIntroDropdownClose);
const panelForHash = (hash) => {
  if (hash === '#intro' || hash.startsWith('#intro-')) return 'intro';
  if (hash === '#part-1') return 'part-1';
  if (hash === '#part-2') return 'part-2';
  return 'cover';
};
const setActiveTab = (tabName, { updateHash = true, scrollTarget = null } = {}) => {
  const panel = tabPanels.find((item) => item.dataset.tabPanel === tabName);
  if (!panel) return;
  tabPanels.forEach((item) => { item.hidden = item !== panel; });
  tabs.forEach((tab) => tab.classList.toggle('active', tab.dataset.navTarget === tabName));
  introDropdown.classList.toggle('active', tabName === 'intro');
  setIntroDropdownOpen(false);
  if (updateHash) history.pushState(null, '', scrollTarget || `#${tabName}`);
  if (scrollTarget) {
    window.requestAnimationFrame(() => document.querySelector(scrollTarget)?.scrollIntoView({ block: 'start' }));
  } else {
    window.scrollTo(0, 0);
  }
};
tabs.forEach((tab) => {
  tab.addEventListener('click', (event) => {
    event.preventDefault();
    setActiveTab(tab.dataset.navTarget);
  });
});
introDropdown.querySelectorAll('.nav-dropdown-menu a').forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    setActiveTab('intro', { scrollTarget: link.dataset.workflowTarget });
  });
});
workflowNodes.forEach((node) => {
  node.addEventListener('click', () => {
    workflowNodes.forEach((item) => item.classList.toggle('is-selected', item === node));
  });
});
document.addEventListener('click', (event) => {
  if (!introDropdown.contains(event.target)) setIntroDropdownOpen(false);
});
const sections = [...document.querySelectorAll('.story[data-tab]')];
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    const target = entry.target.dataset.nav || '#' + entry.target.id;
    const workflowTarget = entry.target.id.startsWith('intro-1-3-') ? '#' + entry.target.id : target;
    workflowNodes.forEach((node) => node.classList.toggle('is-selected', node.dataset.workflowTarget === workflowTarget));
  });
}, { threshold: 0.55 });
sections.forEach((section) => observer.observe(section));

const activateFromLocation = () => {
  const hash = window.location.hash || '#cover';
  const tabName = panelForHash(hash);
  const nestedTarget = tabName === 'intro' && hash.startsWith('#intro-') ? hash : null;
  setActiveTab(tabName, { updateHash: false, scrollTarget: nestedTarget });
};
window.addEventListener('popstate', activateFromLocation);
window.addEventListener('hashchange', activateFromLocation);
activateFromLocation();
