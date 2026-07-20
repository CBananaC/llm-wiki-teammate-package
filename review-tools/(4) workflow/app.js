const node = (phase, title, status, summary, logic, input, output, files) => ({
  phase, title, status, summary, logic, contract: {Input: input, Output: output}, files,
});

const sharedZhuRunner = "tool/scripts py/run_review_bundle_test.py";
const shangyuSkill = "tool/skills md/shangyu-review-loop.md";
const shangyuRunner = "tool/scripts py/run_shangyu_loop_prompt.py";

const steps = {
  "pair-zhu": node(
    "00 · DOCUMENT GRAPH", "Pair later official documents with earlier 硃批", "DONE · OUTCOME WORKING WELL",
    "Reconstructs the private reply chain when an official quotes a 硃批 written on that official’s earlier memorial.",
    ["Extract 硃批 citation markers and quoted spans from the later document.", "Filter earlier documents by the same official and a plausible date window.", "Use exact or near-exact rescript wording, the named memorial, and the stated receipt date to rate the match.", "Keep every pair provisional until the researcher adopts it."],
    "One later official document plus candidate earlier memorials by the same official.",
    "JSON pair cards with zhu_doc_id, match_level, exact quotation, memorial reference, dates, and receipt route.",
    ["tool/skills md/zhu-response-pairing.md", "tool/scripts py/run_zhu_pairing.py"]
  ),
  "pair-yu": node(
    "00 · DOCUMENT GRAPH", "Pair 上諭 with later official replies", "DONE · OUTCOME WORKING WELL",
    "Connects an imperial edict to later memorials that acknowledge, quote, or carry out that edict.",
    ["Start from the edict’s named recipients.", "Require a later document after a plausible transit interval.", "Compare the cited issue date and quoted wording with the selected edict.", "Expose high, partial, and weak candidates for human confirmation."],
    "One 上諭 plus later documents by its recipient officials.",
    "JSON pair cards with reply_doc_id, match_level, issue/receipt dates, receipt route, and quotation evidence.",
    ["tool/skills md/yu-response-pairing.md", "tool/scripts py/run_yu_pairing.py"]
  ),
  "pair-yu-source": node(
    "00 · CONFIRMED DOCUMENT GRAPH", "Link each 上諭 to the official reports it uses", "DONE · CURATED PAIR JSON",
    "Provides the fixed yu_source edges used by the official-document loop. These edges select evidence; the loop does not rediscover them.",
    ["Read the curated yu-source.json pair list.", "Keep named, corroborating, and narrative-source matches distinct in their evidence.", "Use exact quotations from both the official document and the 上諭.", "Let the researcher curate the pair file before it becomes loop input."],
    "One 上諭 and official reports received in the configured five-day source window.",
    "Confirmed yu_source records with yu_doc_id, source document, paired quotations, memorialist, relation note, and provenance metadata.",
    ["tool/skills md/yu-source-pairing.md", "tool/scripts py/run_yu_source_pairing.py", "review-tools/(1) formal/yu-source.json"]
  ),
  "official-select": node(
    "01 · OFFICIAL-DOCUMENT LOOP", "Select the official document first", "LOOP INPUT",
    "The memorial or 硃批-bearing official document is the centre of every later step.",
    ["Select one or more official documents, never an 上諭 as the loop root.", "Preserve document ID, author, complete original text, send date, and receive/硃批 date.", "Read relation edges only from existing pair JSON or already adopted pairs."],
    "Selected 奏摺／硃批 official document(s).", "A stable document scope shared by every step of this loop.",
    ["tool/skills md/official-document-review-loop.md"]
  ),
  "official-lin": node(
    "02 · OFFICIAL-DOCUMENT LOOP", "Extract 林方 events", "ACTIVE · SOURCE TRACE INCLUDED",
    "Extracts rebel-side events from the official text and traces every candidate's source chain during the same run.",
    ["Extract concrete real-world actions, not the reporting act.", "Preserve the source quotation and document ID.", "Run one whole-document source scan and attach matching chains to each event candidate."],
    "Selected official text.", "林方 event cards with quotations, source chains, and review controls.",
    ["tool/skills md/extract-lin-actions.md", "tool/skills md/trace-source-chain.md", sharedZhuRunner]
  ),
  "official-qing": node(
    "02 · OFFICIAL-DOCUMENT LOOP", "Extract 清方 actions in one combined pass", "ACTIVE · THREE CATEGORIES",
    "Runs completed military, planned military, and non-military Qing extraction and presents one de-duplicated card set.",
    ["Run done, plan, and nonmil categories.", "Tag every item with its category.", "Remove overlap returned by more than one category.", "Trace source chains during extraction."],
    "Selected official text.", "One combined 清方 card set with category labels, quotations, and source chains.",
    ["tool/skills md/extract-qing-actions-done.md", "tool/skills md/extract-qing-actions-planned.md", "tool/skills md/extract-qing-nonmilitary-actions.md", "tool/skills md/trace-source-chain.md"]
  ),
  "event-dedup-source": node(
    "02 · OFFICIAL-DOCUMENT LOOP", "Identify re-reported events and name the earliest report", "ACTIVE · DURING EXTRACTION",
    "Compares original quotations and AI card wording across documents, names the earliest reporting document, and leaves the merge decision to the researcher.",
    ["Compare the new event with earlier extraction cards across all document stores.", "Use title similarity plus description/original-quotation evidence.", "Order matches by the source document's report date.", "Offer merge into the earliest event or keep a separate event."],
    "New 林方／清方 candidates plus all earlier extraction cards.", "A prior-report notice, earliest event name, and merge/keep-separate controls on each card.",
    ["tool/skills md/official-document-review-loop.md"]
  ),
  "confirmed-yu-response": node(
    "02 · OFFICIAL-DOCUMENT LOOP", "Explain how the official document answers earlier 上諭", "ACTIVE · PAIR-GROUNDED",
    "Uses only existing official_reply_to_yu edges, then analyzes the substance of the response instead of re-arguing the pair.",
    ["Resolve earlier 上諭 IDs from confirmed pair JSON.", "Extract the emperor's specific comment or command being answered.", "Quote the official's own response, excluding embedded imperial re-quotation.", "Describe compliance, progress, defence, clarification, request, or acknowledgement."],
    "Selected official document plus its confirmed earlier 上諭 records.", "Existing-pair response cards using the no-citation pairing layout, with response-focused subtitle, description, and quotations.",
    ["tool/skills md/confirmed-yu-response-analysis.md", "tool/skills md/yu-response-pairing-nocite.md", "tool/proxy/gemini-proxy/main.py"]
  ),
  "combined-emperor-actions": node(
    "02 · OFFICIAL-DOCUMENT LOOP", "Combine 硃批 and paired 上諭 into emperor actions", "ACTIVE · MULTI-SOURCE",
    "Outputs only the emperor's comment, reply, or command and merges equivalent wording across 硃批 and existing yu_source-linked 上諭.",
    ["Resolve linked 上諭 only from yu_source pairs.", "Exclude relayed 據奏 intelligence from emperor actions.", "Merge semantically equivalent imperial wording into one action.", "Keep a clickable source quotation for every 硃批 and 上諭."],
    "The selected memorial's rescript plus its confirmed paired 上諭.", "相關上諭-style emperor-action cards with one action and multiple documentary sources.",
    ["tool/skills md/combine-confirmed-emperor-actions.md", "tool/proxy/gemini-proxy/main.py"]
  ),
  "emperor-dedup": node(
    "02 · OFFICIAL-DOCUMENT LOOP", "Identify repeated emperor actions across time", "ACTIVE · HUMAN MERGE",
    "Detects the same concrete praise, blame, answer, or command in earlier emperor-action events even when wording or grammatical person differs.",
    ["Compare against earlier committed emperor actions supplied by the website.", "Require the same target and substantive imperial act, not topic overlap alone.", "Name the earliest equivalent action.", "Offer merge of the new sources or keep a separate action."],
    "New combined emperor actions plus earlier committed emperor events.", "Earliest-action notice and merge/keep-separate controls.",
    ["tool/skills md/combine-confirmed-emperor-actions.md", "tool/proxy/gemini-proxy/main.py"]
  ),
  "confirmed-official-response": node(
    "02 · OFFICIAL-DOCUMENT LOOP", "Analyze later official replies through confirmed pairs", "ACTIVE · NO CORPUS SEARCH",
    "Follows each paired 上諭 to later official documents using only official_reply_to_yu records and reuses the current official-response card UI.",
    ["Take every 上諭 linked to the selected official document by a confirmed yu_source edge.", "Resolve its later reply documents from confirmed pair JSON.", "Send only those fixed documents to official_response with confirmed_pairs_only=true.", "Explain how each official answers and preserve both quotations."],
    "A paired 上諭 and its confirmed later reply documents.", "Official-response cards with response subtitle, explanation, dates, and exact evidence.",
    ["tool/skills md/official-response.md", "tool/proxy/gemini-proxy/main.py"]
  ),
  "summary": node(
    "01 · PRE-READING", "Summarise every document", "ACTIVE WORKFLOW",
    "Produces a concise orientation summary and loads it into the summary area of each document’s information panel.",
    ["Preserve the selected document’s identity and type.", "Summarise its main report, request, judgment, or command.", "Do not replace the source text or invent historical context.", "Store the result separately so it can be reviewed and reloaded."],
    "Any selected 上奏, 硃批, or 上諭 record.",
    "summary.json with doc_id and concise summary text for the information panel.",
    ["tool/skills md/quick-summary.md", "tool/scripts py/summarize_stage1_shangzou_vertex.py", sharedZhuRunner]
  ),
  "divide": node(
    "01 · PRE-READING", "Divide a document into readable parts", "ACTIVE WORKFLOW",
    "Creates consecutive sections with subtitles, summaries, and original-text excerpts so the reader can understand the document’s internal structure before close reading.",
    ["Read the entire document before choosing boundaries.", "Divide it into consecutive, non-overlapping parts.", "Give each part a short subtitle and a faithful summary.", "Attach the exact original-text span to every part."],
    "One complete original document.",
    "division-parts.json with ordered parts, subtitles, summaries, and exact excerpts.",
    ["tool/skills md/divide-into-parts.md", sharedZhuRunner]
  ),
  "human-read": node(
    "01 · HUMAN CHECKPOINT", "Read the original text", "REQUIRED HUMAN STEP",
    "The pre-reading output is scaffolding. The researcher reads the full original document before using either analysis loop.",
    ["Review the summary for orientation.", "Use the section divisions to navigate the document.", "Read and interpret the complete original text.", "Carry corrections and uncertainties into the later adoption decisions."],
    "Summary, section divisions, and the complete original text.",
    "A human-informed reading state; no AI finding is automatically accepted.",
    ["tool/skills md/quick-summary.md", "tool/skills md/divide-into-parts.md", sharedZhuRunner]
  ),
  "zhu-select": node(
    "02 · LOOP 1 · 硃批", "Select one official 硃批 document", "LOOP INPUT",
    "Starts the reproducible official-document loop while keeping each analytical stage as a separate reviewable output.",
    ["Select records by the supplied document IDs or date window.", "Preserve the original ID, official, send date, receipt/硃批 date, and full text.", "Run each stage independently and write an empty result when nothing is found.", "Resume completed stages without replacing earlier output."],
    "A human-read 硃批 record or a selected date-window bundle.",
    "A review bundle manifest plus stage-specific JSON files.",
    ["tool/skills md/zhu-review-loop.md", "tool/scripts py/run_zhu_review_loop.py", sharedZhuRunner]
  ),
  "zhu-lin": node(
    "02 · LOOP 1 · 硃批", "Extract 林方 military events", "ACTIVE WORKFLOW",
    "Identifies discrete rebel-side actions that the memorial reports as actually having happened.",
    ["Locate actor, action, place, and time in the original text.", "Separate real events from rumours, plans, and Qing-side action.", "Write a clear topic sentence and fuller description.", "Preserve an exact supporting quotation."],
    "One official memorial’s complete text.",
    "lin-events.json event records with subtitle, description, who/where/when, quotation, and source document.",
    ["tool/skills md/extract-lin-actions.md", sharedZhuRunner]
  ),
  "zhu-qing-done": node(
    "02 · LOOP 1 · 硃批", "Extract completed 清方 military events", "DONE",
    "Captures Qing military actions already carried out and keeps them distinct from plans or imperial commands.",
    ["Identify a Qing actor and a completed action.", "Exclude intended, requested, or conditional action.", "Split distinct actions into separate event records.", "Attach exact quotation and document provenance."],
    "One official memorial’s complete text.",
    "qing-events-done.json with completed Qing event cards and source evidence.",
    ["tool/skills md/extract-qing-actions-done.md", sharedZhuRunner]
  ),
  "zhu-qing-plan": node(
    "02 · LOOP 1 · 硃批", "Extract planned 清方 military events", "NEXT / TO BE COMPLETED",
    "Captures what Qing actors plan, request, order, or intend to do, without mislabelling it as a completed battlefield event.",
    ["Detect future, requested, intended, ordered, or conditional action.", "Identify who is expected to act and what conditions apply.", "Keep the plan separate from later evidence of completion.", "Preserve the exact planning quotation."],
    "One official memorial’s complete text.",
    "qing-events-plan.json with planned-action cards and source evidence.",
    ["tool/skills md/extract-qing-actions-planned.md", sharedZhuRunner]
  ),
  "zhu-source": node(
    "02 · LOOP 1 · 硃批", "Trace a source chain for every event", "RUN ON EACH EVENT",
    "Makes every extracted event auditable by connecting the displayed claim to its immediate documentary evidence and earlier information source where supported.",
    ["Take one extracted event at a time.", "Find the exact quotation in the selected document.", "Search eligible earlier records without crossing the selected document’s receive date.", "Record only supported links and keep missing links explicitly unresolved."],
    "One event plus the selected document and date-qualified candidate sources.",
    "source-chain.json with event ID, source document IDs, quotations, dates, officials, and relation notes.",
    ["tool/skills md/trace-source-chain.md", sharedZhuRunner]
  ),
  "zhu-emperor": node(
    "02 · LOOP 1 · 硃批", "Extract the emperor’s 硃批", "ACTIVE WORKFLOW",
    "Separates every imperial marginal or final rescript from the official’s text and records what it responds to.",
    ["Extract every 硃批, including 夾批 and 尾批.", "Locate its position and response target in the memorial.", "Separate opinion, judgment, and command.", "Preserve exact imperial text and local evidence."],
    "The official memorial and its embedded rescript fields.",
    "zhupi.json with title, exact text, position, response target, opinion, and evidence fields.",
    ["tool/skills md/extract-zhupi.md", sharedZhuRunner]
  ),
  "zhu-yu-reply": node(
    "02 · LOOP 1 · 硃批", "Find the emperor’s related 上諭", "ACTIVE WORKFLOW",
    "Searches nearby edicts and retains only genuine imperial replies to points raised in the selected memorial.",
    ["Generate nearby 上諭 candidates after the memorial becomes available to the emperor.", "Compare each memorial point with each imperial point.", "Keep memorial and imperial quotations separate.", "Treat concrete commands as emperor-action candidates, not Qing-side completed events."],
    "One 硃批 document plus nearby 上諭 candidates.",
    "edict-match.json with paired points, summaries, response explanations, quotations, dates, and command classification.",
    ["tool/skills md/edict-match.md", "tool/skills md/extract-emperor-action.md", sharedZhuRunner]
  ),
  "zhu-official-reply": node(
    "02 · LOOP 1 · 硃批", "Find officials’ replies to the emperor", "ACTIVE WORKFLOW",
    "Closes the loop by locating later documents that acknowledge or act on the emperor’s 硃批 or related 上諭.",
    ["Start from the emperor’s response and its target official.", "Search only later official documents within a plausible transit window.", "Require a quotation, acknowledgment, or concrete answer to that response.", "Keep the link provisional until adopted."],
    "An extracted 硃批 or matched 上諭 plus later official documents.",
    "Official-response cards with response document, official, date, summary, quotation, and match evidence.",
    ["tool/skills md/yu-response-pairing.md", "tool/scripts py/run_yu_pairing.py"]
  ),
  "yu-select": node(
    "02 · LOOP 2 · 上諭", "Select one 上諭", "LOOP INPUT",
    "Starts an edict-centred review with prior reports and later replies selected around the edict’s issue date.",
    ["Load the complete edict, date, title, and recipients.", "Select candidate reports received on or before the edict date.", "Select later documents by command target and plausible response timing.", "Send the complete evidence packet through one saved review prompt."],
    "One 上諭, prior candidate reports, and later candidate responses.",
    "One structured review JSON containing reported events, commands, responses, and timeliness evidence.",
    [shangyuSkill, shangyuRunner]
  ),
  "yu-lin": node(
    "02 · LOOP 2 · 上諭", "Extract 林方 events known to the emperor", "ACTIVE WORKFLOW",
    "Reconstructs rebel-side battlefield facts that the emperor explicitly reports knowing in the selected edict.",
    ["Extract only events reported in the 上諭.", "Treat them as earlier historical events, not events occurring on the edict date.", "Attach the exact edict quotation.", "Keep imperial comment and command in separate fields."],
    "One complete 上諭.",
    "reported_events entries with side=lin, subtitle, description, who/where/when, edict quotation, and comment fields.",
    [shangyuSkill]
  ),
  "yu-qing": node(
    "02 · LOOP 2 · 上諭", "Extract 清方 events known to the emperor", "ACTIVE WORKFLOW",
    "Reconstructs the Qing-side battlefield situation represented in the emperor’s information state.",
    ["Extract completed or reported Qing actions stated in the edict.", "Do not convert a new imperial command into an already-completed Qing event.", "Attach actor, place, time, and exact edict quotation.", "Separate the emperor’s judgment from the underlying event."],
    "One complete 上諭.",
    "reported_events entries with side=qing and the same source and comment fields.",
    [shangyuSkill]
  ),
  "yu-source": node(
    "02 · LOOP 2 · 上諭", "Identify how the emperor knew", "NEXT / REFINEMENT",
    "Matches each event in the edict to the direct official document that delivered that information to the emperor.",
    ["Extract officials named by 據…奏 or use the edict’s recipients as fallback.", "Require the source document’s receive/硃批 date to be on or before the edict date.", "Prefer same-day evidence, then the nearest earlier reports, including the proposed 1–3-day search.", "Require the source quotation to support the same event; never invent an earlier relay chain."],
    "One reported event plus date-qualified official reports.",
    "direct_report with source_doc_id, source official, send/receive dates, source quotation, and 未明 when unsupported.",
    [shangyuSkill]
  ),
  "yu-command": node(
    "02 · LOOP 2 · 上諭", "Extract the emperor’s commands", "ACTIVE WORKFLOW",
    "Captures each concrete imperial order and its target while keeping criticism, judgment, information, and awards distinct.",
    ["Read the edict for actionable imperial language.", "Split commands with different targets or functions.", "Give each command a short title and a fuller explanation of what is ordered and why.", "Preserve the exact command quotation."],
    "One complete 上諭 and its named recipients.",
    "commands entries with title, target officials, summary, exact quotation, and nested response candidates.",
    ["tool/skills md/extract-emperor-action.md"]
  ),
  "yu-official-reply": node(
    "02 · LOOP 2 · 上諭", "Find later officials’ replies", "ACTIVE WORKFLOW",
    "Links each imperial command to later memorials that carry it out or directly answer it.",
    ["Restrict candidates to an official targeted by the command.", "Require a send date after the 上諭 and allow realistic transmission time.", "Require quoted wording or a clear report of compliance/answer.", "Record the reply quotation and how the official responded."],
    "One command plus later documents by its target official(s).",
    "Nested responses with reply document ID, official, send date, subtitle, description, and exact quotation.",
    ["tool/skills md/official-response.md"]
  ),
  "yu-timeliness": node(
    "02 · LOOP 2 · 上諭", "Compare 時效", "ANALYSIS TARGET",
    "Assesses the edict across an information window, accounting for battlefield change and reporting delay instead of using reply latency alone.",
    ["Set window_start to the earliest send date among the direct reports found for the edict.", "Set window_end to the 上諭 issue date.", "Compare dated later-situation evidence with the battlefield situation known to the emperor.", "Mark evidence sufficient or insufficient; do not call the order stale without a dated contradiction."],
    "Direct report dates, the 上諭 date, battlefield events, and any dated contrary/later-situation document.",
    "timeliness_evidence with status, window_start, window_end, explanatory note, and uncertainty.",
    ["tool/skills md/response-timeliness.md"]
  ),
  "json-output": node(
    "03 · SHARED OUTPUT", "Export structured AI output", "JSON CONTRACT",
    "Every analytical stage writes durable JSON so raw model output can be displayed, reloaded, compared, and reviewed without silently replacing another stage.",
    ["Keep one output file per analytical stage.", "Preserve document IDs, exact quotations, dates, and officials.", "Write empty results rather than skipping documents.", "Keep raw model output separate from human edits."],
    "Stage-specific AI findings from either analysis loop.",
    "summary, division, event, source-chain, zhupi, edict-match, command, response, and timeliness JSON records.",
    ["tool/skills md/zhu-review-loop.md", shangyuSkill, "tool/scripts py/run_zhu_review_loop.py", shangyuRunner, sharedZhuRunner]
  ),
  "review-card": node(
    "03 · SHARED OUTPUT", "Display every finding as a review card", "WEBSITE PRESENTATION",
    "Turns structured JSON into a consistent, evidence-first card that can be understood and judged without hiding the original source.",
    ["Lead with a clear topic sentence.", "Add a fuller description without overstating the evidence.", "Show the exact quotation and source metadata together.", "Expose an explicit adopt/reject decision for the researcher."],
    "One JSON finding with claim, description, quotation, and provenance.",
    "A website card showing topic sentence, description, quotation, source information, and decision controls.",
    ["tool/skills md/extract-emperor-action.md", "tool/skills md/official-response.md", sharedZhuRunner]
  ),
  "human-adopt": node(
    "03 · SHARED OUTPUT", "Adopt or reject the AI output", "HUMAN GATE",
    "Makes the researcher, rather than the model, the authority that turns a provisional suggestion into an accepted relationship or finding.",
    ["Compare the card’s claim with its exact quotation.", "Check the source document, date, official, and relationship context.", "Adopt supported findings; reject or edit unsupported ones.", "Persist human decisions separately from raw AI output and return to the next document."],
    "One AI review card plus the researcher’s reading of the source text.",
    "Human-reviewed evidence, accepted connectors, corrections, and notes for the timeline/wiki export.",
    ["tool/skills md/official-response.md", "tool/skills md/yu-response-pairing.md", "tool/scripts py/merge_pairs.py"]
  ),
};

const zhUi = {
  connectionKicker: "文書關係重建", connectionTitle: "重建朝廷文書往復網絡",
  sourceCorpus: "原始文書群", corpusDesc: "官員奏摺、硃批與上諭",
  established: "已建立", planned: "規劃中", operational: "運作中", input: "輸入",
  perEvent: "逐項事件", refinement: "待完善", assessment: "評估",
  pairZhuTitle: "辨識官員對既有硃批的回覆", pairZhuDesc: "綜合具奏者身分、文書日期與所引御批文字進行配對",
  pairYuTitle: "辨識官員對上諭的後續回應", pairYuDesc: "綜合受旨官員、傳遞時程與所引諭旨內容進行配對",
  pairSourceTitle: "辨識每道上諭所依據的前置奏報", pairSourceDesc: "使用整理後的 yu_source 紀錄及雙方逐字引文",
  prereadKicker: "閱讀準備", prereadTitle: "為逐篇精讀建立文書導讀",
  officialSelectTitle: "先選定官員文書", officialSelectDesc: "整個迴圈固定使用同一奏摺／硃批文書範圍",
  summaryTitle: "撰寫精要文書提要", summaryDesc: "在資訊面板呈現該文書的主要奏報、請求、判斷或命令",
  divideTitle: "標示文書內部結構", divideDesc: "依原文順序分段，為各段配置說明性標題與忠實摘要",
  researcherCheckpoint: "研究者核讀", closeReadingTitle: "精讀完整原文", closeReadingDesc: "分析工具協助定位與理解；歷史詮釋仍以第一手文獻為準",
  analysisKicker: "以文書為核心的分析", analysisTitle: "單一官文優先審閱迴圈",
  cycleOne: "官文優先迴圈", cycleTwo: "舊版上諭迴圈",
  zhuCycleTitle: "從事件抽取到君臣往復審閱一份官文", zhuCycleDesc: "事件與來源同步處理，文書關係只沿用已確認配對。",
  yuCycleTitle: "上諭知情與回應循環", yuCycleDesc: "重建皇帝的資訊狀態、諭令內容、官員後續回應與時間適切性。",
  zhuSelectTitle: "抽取林方事件", zhuSelectDesc: "同一次抽取同步追索各事件來源鏈",
  zhuLinTitle: "三類合一抽取清方行動", zhuLinDesc: "合併已執行軍事、待執行軍事與非軍事行動",
  zhuQingDoneTitle: "辨識重複奏報與最早事件", zhuQingDoneDesc: "保留各份回報與來源鏈，並提供合併或不合併選項",
  zhuQingPlanTitle: "說明官文如何回應先前上諭", zhuQingPlanDesc: "只使用既有 official_reply_to_yu 配對，不再搜尋",
  zhuSourceTitle: "合併硃批與配對上諭為皇帝行動", zhuSourceDesc: "只輸出皇帝評論、答覆與命令，並保存全部來源",
  zhuEmperorTitle: "辨識跨時重複皇帝行動", zhuEmperorDesc: "指出最早等同行動，並提供合併或保持獨立",
  zhuYuTitle: "依已確認配對分析後出官員回奏", zhuYuDesc: "從每道配對上諭沿既有 official_reply_to_yu 關係前進",
  zhuReplyTitle: "把各階段保存為可審閱證據", zhuReplyDesc: "任何關係都須經研究者裁定才成為研究證據",
  nextZhu: "下一份硃批文書",
  yuSelectTitle: "確立上諭文書紀錄", yuSelectDesc: "整合上諭、合資格的前置奏報與後續回應候選文書",
  yuLinTitle: "抽取皇帝認知中的林方事件", yuLinDesc: "視為先前獲報的史事，不視為上諭頒發當日才發生的事件",
  yuQingTitle: "抽取皇帝認知中的清方事件", yuQingDesc: "區分已獲奏報的軍事行動與上諭中新頒的命令",
  yuSourceTitle: "辨識皇帝資訊的直接文獻來源", yuSourceDesc: "把上諭所述事件配對至將該訊息傳入宮廷的官員文書",
  yuCommandTitle: "分類皇帝諭令", yuCommandDesc: "區分具體命令、批評、判斷、資訊陳述與獎賞",
  yuReplyTitle: "連結官員執行與回奏", yuReplyDesc: "須具備正確受旨者、較晚日期，以及實際回應的文獻證據",
  yuTimelinessTitle: "評估諭令的時間適切性", yuTimelinessDesc: "比較戰場情勢變化、文書傳遞延遲與皇帝回應時間窗",
  nextYu: "下一道上諭",
  reviewKicker: "證據審閱", reviewTitle: "將模型發現轉化為可核驗的研究證據",
  jsonTitle: "保存結構化分析紀錄", jsonDesc: "按分析階段分別保存文書識別、逐字引文與來源資訊",
  reviewCard: "證據卡片", cardTitle: "簡明的分析命題", cardDesc: "說明該項歷史發現的文獻脈絡與研究意義。",
  cardQuote: "「第一手文書中的逐字證據。」", cardSource: "文書 · 日期 · 具奏者 · 來源關係",
  accept: "採納", reject: "不採納", researcherDecision: "研究者裁定",
  adoptTitle: "核准、修訂或否決模型建議", adoptDesc: "只有經研究者確認的證據才進入研究紀錄",
  iteration: "循環處理", iterationDesc: "保存已審閱證據，並進入下一份文書",
  algorithm: "分析程序", dataContract: "資料規格", chatUsageTitle: "在 AI 對話面板中的使用方式", implementation: "實作來源",
  sourceTitle: "提示詞、技能與執行程式", loadingSources: "正在載入來源檔案……", selectSource: "請選擇來源檔案以閱讀全文。",
};

const zhNode = (phase, title, status, summary, logic, input, output) => ({
  phase, title, status, summary, logic, contract: {輸入: input, 輸出: output},
});

const zhSteps = {
  "pair-zhu": zhNode("文書關係重建", "配對後出官員文書與其所引前次硃批", "已建立",
    "藉由官員在後出奏摺中引述前次硃批，重建皇帝對該官員早前奏摺的私密回覆鏈。",
    ["擷取奉硃批等標記及其後完整引文。", "依同一具奏者與合理日期範圍篩選前置奏摺。", "比對御批文字、前奏稱謂與奉到日期。", "配對在研究者採納前均保持為候選關係。"],
    "一份後出官員文書，以及同一官員的前置硃批候選文書。", "包含文書識別碼、配對強度、逐字引文、日期與接收方式的 JSON 候選卡片。"),
  "pair-yu": zhNode("文書關係重建", "配對上諭與官員後續回奏", "已建立",
    "辨識後續奏摺中對特定上諭的奉到、引述或執行情形。",
    ["以上諭所列受旨官員為候選作者。", "限定在合理傳遞時間之後形成的文書。", "比對所引頒旨日期與諭旨內容。", "將不同強度的候選結果交由研究者確認。"],
    "一道上諭及其受旨官員的後出文書。", "包含回奏文書、配對強度、頒旨／奉到日期、傳遞方式與引文的 JSON。"),
  "pair-yu-source": zhNode("已確認文書關係圖", "連結上諭與其採用的官員奏報", "已完成 · 整理後配對 JSON",
    "提供官文優先迴圈使用的固定 yu_source 關係；迴圈只讀取，不重新搜尋。",
    ["讀取整理後的 yu-source.json。", "在證據中區分具名、同期佐證與敘事性來源。", "保存官文與上諭雙方逐字引文。", "由研究者先整理配對檔，才成為迴圈輸入。"],
    "一道上諭及五日來源窗內的官員奏報。", "含上諭、來源文書、雙方引文、具奏者與關係說明的已確認 yu_source 紀錄。"),
  "official-select": zhNode("官文優先迴圈", "先選定官員文書", "迴圈輸入",
    "每個後續步驟都以所選奏摺／硃批官文為中心。",
    ["選擇一份或多份官文，不以上諭作為迴圈根節點。", "保存文書編號、具奏者、全文、上奏日及收受／硃批日。", "關係只讀取既有配對 JSON 或研究者已採納的配對。"],
    "所選奏摺／硃批官文。", "所有迴圈步驟共用的固定文書範圍。"),
  "official-lin": zhNode("官文優先迴圈", "抽取林方事件", "運作中 · 同步來源追索",
    "從官文抽取林方事件，並在同一次執行中為每個候選預先追索來源鏈。",
    ["抽取真實世界行動，不把奏報行為本身當事件。", "保存來源引文與文書編號。", "每篇來源文書只掃描一次，再把來源鏈附到相符事件。"],
    "所選官文全文。", "含引文、來源鏈與審閱控制的林方事件卡片。"),
  "official-qing": zhNode("官文優先迴圈", "三類合一抽取清方行動", "運作中 · 三類合一",
    "依次抽取已執行軍事、待執行軍事及非軍事行動，再以同一組卡片呈現。",
    ["執行 done、plan、nonmil 三類。", "標示每項分類。", "移除跨類別重複結果。", "抽取時同步追索來源鏈。"],
    "所選官文全文。", "含分類標籤、引文及來源鏈的清方合併卡片。"),
  "event-dedup-source": zhNode("官文優先迴圈", "辨識重複奏報並指出最早回報", "運作中 · 抽取時執行",
    "跨文書比較原文引文與 AI 卡片用語，指出最早回報，合併與否由研究者決定。",
    ["把新事件與所有較早抽取卡片比較。", "綜合標題、說明及原文引文。", "按來源文書的回報日期決定最早者。", "提供併入最早事件或保持獨立兩種操作。"],
    "新林方／清方候選及全部既有抽取卡片。", "最早回報提示及合併／不合併控制。"),
  "confirmed-yu-response": zhNode("官文優先迴圈", "說明官文如何回應先前上諭", "運作中 · 依既有配對",
    "只沿用 official_reply_to_yu 關係，分析實際答覆內容，不再論證配對。",
    ["從已確認配對取得先前上諭。", "定位官員所答的皇帝評論、問題或命令。", "引用官員自己的答覆，排除重引皇帝原話。", "分類為遵行、進度、申辯、澄清、請旨或知悉。"],
    "所選官文及其已確認先前上諭。", "沿用無引文配對介面的回應內容卡片。"),
  "combined-emperor-actions": zhNode("官文優先迴圈", "合併硃批與配對上諭為皇帝行動", "運作中 · 多重來源",
    "只輸出皇帝的評論、答覆或命令，並把硃批與既有 yu_source 上諭中的同義表達合為一項。",
    ["只由 yu_source 配對取得上諭。", "排除據奏轉述情報。", "合併語義相同的皇帝表達。", "為每份硃批與上諭保留可點按引文。"],
    "本摺硃批及其已確認配對上諭。", "沿用相關上諭介面的多來源皇帝行動卡片。"),
  "emperor-dedup": zhNode("官文優先迴圈", "辨識跨時重複皇帝行動", "運作中 · 人工合併",
    "即使用語或人稱不同，仍比較是否為同一具體嘉許、責備、答覆或命令。",
    ["與較早已建立皇帝行動比較。", "要求對象與實質行動相同，不以主題相近代替。", "指出最早等同行動。", "提供併入來源或保持獨立。"],
    "新皇帝行動及較早既有皇帝行動。", "最早行動提示及合併／不合併控制。"),
  "confirmed-official-response": zhNode("官文優先迴圈", "依既有配對分析後續官員回奏", "運作中 · 不搜尋全集",
    "從每道配對上諭沿 official_reply_to_yu 關係取得後出官文，沿用官員回應卡片。",
    ["取與所選官文有已確認 yu_source 關係的每道上諭。", "從已確認配對取得後出回奏。", "以 confirmed_pairs_only=true 只送出固定文書。", "說明官員如何答覆並保存雙方引文。"],
    "一道配對上諭及其已確認後出回奏。", "含標題、說明、日期及逐字證據的官員回應卡片。"),
  summary: zhNode("閱讀準備", "撰寫文書提要", "運作中",
    "為每份文書建立精要導讀，並置入其資訊面板，供精讀前掌握核心內容。",
    ["保存文書身分與類型。", "概括主要奏報、請求、判斷或命令。", "不得以摘要取代原文或補造背景。", "摘要獨立保存，便於重新載入與審閱。"],
    "任一上奏、硃批或上諭文書。", "供資訊面板顯示的 summary.json。"),
  divide: zhNode("閱讀準備", "標示文書內部結構", "運作中",
    "依內容轉折將全文劃分為連續段落，並為各段配置標題、摘要與原文範圍。",
    ["先通讀全文再決定分界。", "各段必須連續且不可重疊。", "標題簡潔，摘要忠於原意。", "每段保留精確原文。"],
    "一份完整原始文書。", "依序排列的 division-parts.json，包含標題、摘要與逐字原文。"),
  "human-read": zhNode("研究者核讀", "精讀完整原文", "必要的人工作業",
    "導讀結果只負責協助定位；研究者須在進入兩條分析循環前閱讀完整原文。",
    ["先以提要掌握文書方向。", "利用分段快速定位內容。", "通讀並詮釋完整原文。", "把疑義與修正帶入後續採納判斷。"],
    "提要、結構分段與完整原文。", "以人工閱讀為基礎的理解狀態；模型結果不會自動成立。"),
  "zhu-select": zhNode("循環一 · 硃批", "確立待分析的奏摺紀錄", "循環輸入",
    "以可重複方式啟動官員文書分析，並使各分析階段保持為互不覆蓋的審閱單元。",
    ["依指定識別碼或日期範圍選取文書。", "保存具奏者、上奏日、硃批／收受日與全文。", "各階段獨立執行；無結果亦明確輸出空值。", "可續跑已完成工作而不覆蓋舊結果。"],
    "經精讀的硃批文書或指定日期範圍。", "審閱套件清單及按階段分開的 JSON。"),
  "zhu-lin": zhNode("循環一 · 硃批", "抽取林方軍事事件", "運作中",
    "辨識奏摺中被陳述為已發生的林方個別行動。",
    ["辨識人物、行動、地點與時間。", "排除傳聞、計畫及清方行動。", "每項事件配置清楚命題與說明。", "保存逐字證據。"],
    "一份官員奏摺全文。", "含事件標題、說明、人物、地點、日期、引文與文書來源的 lin-events.json。"),
  "zhu-qing-done": zhNode("循環一 · 硃批", "抽取清方已完成的軍事事件", "已建立",
    "記錄清方已實施的軍事行動，並與未來計畫及皇帝命令分開。",
    ["辨識清方行動者與完成式行動。", "排除意圖、請求與條件式方案。", "不同事件分列紀錄。", "附上逐字引文與文書出處。"],
    "一份官員奏摺全文。", "清方已完成事件及其證據的 qing-events-done.json。"),
  "zhu-qing-plan": zhNode("循環一 · 硃批", "抽取清方擬議中的軍事行動", "待完善",
    "記錄清方將要、請求、奉令或有條件準備執行的行動，避免誤列為既成事件。",
    ["辨識將來式、請求、意圖、命令或條件。", "確認預期執行者及限制條件。", "與後來完成證據分開。", "保存計畫內容的逐字引文。"],
    "一份官員奏摺全文。", "擬議行動及其來源證據的 qing-events-plan.json。"),
  "zhu-source": zhNode("循環一 · 硃批", "追索每項事件的文獻來源", "逐項執行",
    "使每個事件命題均可沿著文獻鏈回查至直接證據與有支持的前置資訊來源。",
    ["每次處理一項事件。", "定位本篇文書中的精確引文。", "只檢索在本篇收受日以前可成立的來源。", "無證據的環節保持未決。"],
    "一項事件、本篇文書與符合日期條件的候選來源。", "含事件、來源文書、引文、日期、官員及關係說明的 source-chain.json。"),
  "zhu-emperor": zhNode("循環一 · 硃批", "分析皇帝硃批", "運作中",
    "把所有夾批與尾批從官員正文中分離，並判定其回應對象與功能。",
    ["擷取每條硃批。", "判定其在奏摺中的位置與所回應段落。", "區分判斷、意見與命令。", "保存完整御批文字與局部證據。"],
    "官員奏摺及其硃批欄位。", "含位置、回應對象、判斷與引文的 zhupi.json。"),
  "zhu-yu-reply": zhNode("循環一 · 硃批", "連結後續相關上諭", "運作中",
    "檢索時間相近的上諭，僅保留確實回應本篇奏摺要點的諭旨。",
    ["建立本篇文書可被皇帝閱讀後的上諭候選。", "逐點比對奏摺與諭旨。", "分列官員引文與皇帝引文。", "把具體命令列為皇帝行動，不混入清方既成事件。"],
    "一份硃批文書及時間相近的上諭。", "含對應要點、說明、雙方引文、日期與命令分類的 edict-match.json。"),
  "zhu-official-reply": zhNode("循環一 · 硃批", "連結官員對皇帝回應的後續回奏", "運作中",
    "辨識後出官員文書是否奉到、執行或具體答覆相關硃批或上諭。",
    ["從皇帝回應及其對象開始。", "只檢索合理傳遞期之後的文書。", "要求存在引述、奉到或具體執行證據。", "關係須經研究者採納才成立。"],
    "一條硃批或相配上諭，以及後出官員文書。", "含回奏文書、官員、日期、摘要、引文與配對依據的候選卡片。"),
  "yu-select": zhNode("循環二 · 上諭", "確立待分析的上諭紀錄", "循環輸入",
    "以上諭日期為中心，整合前置奏報與後續回奏候選，建立完整分析證據包。",
    ["載入上諭全文、日期、標題與受旨官員。", "選取頒旨日以前收到的奏報候選。", "依受旨者與合理時程選取後出回奏。", "將完整證據交由同一保存提示詞處理。"],
    "一道上諭、前置奏報候選及後續回奏候選。", "含已知事件、命令、回奏與時效證據的結構化 JSON。"),
  "yu-lin": zhNode("循環二 · 上諭", "抽取皇帝已知的林方事件", "運作中",
    "重建上諭中明示皇帝已獲知的林方戰場事實。",
    ["只抽取上諭所述事件。", "視為先前事件而非頒旨日新發事件。", "附上上諭逐字引文。", "皇帝評語與命令另列欄位。"],
    "一道完整上諭。", "side=lin 的 reported_events，含事件、時地人、引文與評語欄位。"),
  "yu-qing": zhNode("循環二 · 上諭", "抽取皇帝已知的清方事件", "運作中",
    "重建皇帝資訊狀態中所呈現的清方戰場情勢。",
    ["抽取上諭陳述的清方已發生行動。", "不得把上諭新命令當成已完成事件。", "附上行動者、時地與逐字引文。", "皇帝判斷與基礎事件分開。"],
    "一道完整上諭。", "side=qing 的 reported_events 及來源與評語欄位。"),
  "yu-source": zhNode("循環二 · 上諭", "辨識皇帝資訊的直接奏報來源", "待完善",
    "把上諭中的每項事件配對至將該資訊直接送達皇帝的官員文書。",
    ["優先使用「據某奏」所明示官員。", "來源文書必須在頒旨日以前收到。", "先查同日，再查前三日內最近奏報。", "來源引文須支持同一事件，不補造更早傳遞鏈。"],
    "一項上諭所述事件與符合日期條件的官員奏報。", "含來源文書、官員、上奏／收受日期、引文及未明標記的 direct_report。"),
  "yu-command": zhNode("循環二 · 上諭", "分類皇帝命令", "運作中",
    "擷取每項具體諭令及其受命官員，並與批評、判斷、資訊陳述和獎賞分開。",
    ["辨識可執行的諭令語句。", "不同對象或功能的命令分列。", "說明命令內容及其理由。", "保存逐字諭令。"],
    "一道完整上諭及其受旨官員。", "含標題、受命者、說明、引文與後續回奏的 commands。"),
  "yu-official-reply": zhNode("循環二 · 上諭", "連結官員的執行與回奏", "運作中",
    "把每項皇帝命令連接至後出奏摺中的執行情形或直接答覆。",
    ["候選作者須為受命官員。", "回奏上奏日須晚於上諭並符合傳遞時程。", "須有引文或清楚執行證據。", "記錄官員如何回應及其逐字證據。"],
    "一項命令及受命官員的後出文書。", "含回奏文書、官員、日期、摘要、說明與引文的 responses。"),
  "yu-timeliness": zhNode("循環二 · 上諭", "評估諭令的時間適切性", "分析目標",
    "以資訊形成時間窗評估上諭，並納入戰況變化與奏報延遲，而非只計算回奏速度。",
    ["以直接來源中最早上奏日為時間窗起點。", "以上諭頒發日為終點。", "比較具日期的後續戰況與皇帝已知情勢。", "只有具備相反日期證據時，才可判定諭令已過時。"],
    "直接奏報日期、上諭日期、戰場事件及具日期的後續情勢文書。", "含證據充分性、起迄日期、說明與不確定性的 timeliness_evidence。"),
  "json-output": zhNode("證據審閱", "輸出結構化分析紀錄", "JSON 規格",
    "各分析階段分別保存模型結果，使其可重新載入、比較與審閱，並避免互相覆蓋。",
    ["每個分析階段使用獨立輸出檔。", "保存文書識別碼、逐字引文、日期與官員。", "無發現時輸出空結果，不跳過文書。", "模型原始結果與人工修訂分開。"],
    "任一分析循環產生的分階段發現。", "提要、分段、事件、來源鏈、硃批、上諭配對、命令、回奏與時效 JSON。"),
  "review-card": zhNode("證據審閱", "以證據卡片呈現每項模型發現", "介面呈現",
    "把結構化結果轉為一致的證據卡片，使研究者能在不脫離原文的情況下判斷。",
    ["以清楚分析命題開頭。", "提供不逾越證據的完整說明。", "同時呈現逐字引文與來源資訊。", "提供明確的採納與不採納操作。"],
    "一項包含命題、說明、引文與來源的 JSON 發現。", "含命題、說明、引文、文書資訊與審閱操作的網站卡片。"),
  "human-adopt": zhNode("證據審閱", "核准、修訂或否決模型建議", "人工裁定",
    "由研究者決定候選關係或分析發現是否成為正式研究紀錄。",
    ["以逐字引文核對分析命題。", "檢查文書、日期、官員與關係脈絡。", "採納有支持的結果，否決或修訂不足者。", "人工決定與模型原始輸出分別保存。"],
    "一張模型證據卡片及研究者對原文的理解。", "經人工確認的證據、文書連線、修訂與研究筆記。"),
};

const chatBindings = {
  "tool/skills md/quick-summary.md": {
    state: "live", action: "Summary / 進一步摘要", mode: "summary",
    note: "The panel loads the Website Prompt through skillPromptFor('quick-summary') and sends it as the summary instruction.",
    zhAction: "摘要／進一步摘要", zhMode: "summary（摘要）",
    zhNote: "面板透過 skillPromptFor('quick-summary') 讀取 Website Prompt，並把它作為摘要指令送出。",
  },
  "tool/skills md/divide-into-parts.md": {
    state: "live", action: "Divide / 分段標註", mode: "divide",
    note: "The saved Website Prompt is loaded through skillPromptFor('divide-into-parts') and passed as the division instruction.",
    zhAction: "分段／分段標註", zhMode: "divide（分段）",
    zhNote: "面板透過 skillPromptFor('divide-into-parts') 載入 Website Prompt，並作為分段指令使用。",
  },
  "tool/skills md/extract-lin-actions.md": {
    state: "live", action: "林方事件", mode: "events · actor=lin",
    note: "runExtract reads this saved prompt through skillPromptFor and sends it as actor_instruction.",
    zhAction: "林方事件", zhMode: "events · actor=lin",
    zhNote: "runExtract 透過 skillPromptFor 讀取此提示詞，並以 actor_instruction 傳送。",
  },
  "tool/skills md/extract-qing-actions-done.md": {
    state: "live", action: "清方已行動", mode: "events · actor=qing · category=done",
    note: "runExtract loads this Website Prompt as the Qing completed-action instruction.",
    zhAction: "清方已行動", zhMode: "events · actor=qing · category=done",
    zhNote: "runExtract 載入此 Website Prompt，作為清方已完成行動的抽取指令。",
  },
  "tool/skills md/extract-qing-actions-planned.md": {
    state: "live", action: "清方待行動", mode: "events · actor=qing · category=plan",
    note: "runExtract loads this Website Prompt as the Qing prospective-action instruction.",
    zhAction: "清方待行動", zhMode: "events · actor=qing · category=plan",
    zhNote: "runExtract 載入此 Website Prompt，作為清方擬議行動的抽取指令。",
  },
  "tool/skills md/extract-qing-nonmilitary-actions.md": {
    state: "live", action: "清方非軍事", mode: "events · actor=qing · category=nonmil",
    note: "runExtract loads this Website Prompt as the non-military Qing action instruction.",
    zhAction: "清方非軍事", zhMode: "events · actor=qing · category=nonmil",
    zhNote: "runExtract 載入此 Website Prompt，作為清方非軍事行動的抽取指令。",
  },
  "tool/skills md/edict-match.md": {
    state: "live", action: "上諭 / @相關上諭", mode: "edict_match",
    note: "runEdictScan dynamically loads this Website Prompt through skillPromptFor('edict-match').",
    zhAction: "上諭／@相關上諭", zhMode: "edict_match（上諭配對）",
    zhNote: "runEdictScan 透過 skillPromptFor('edict-match') 動態載入此 Website Prompt。",
  },
  "tool/skills md/trace-source-chain.md": {
    state: "not-linked", action: "林方來源 / 全文來源鏈 / @追溯來源", mode: "trace",
    note: "The chat actions use the trace proxy mode, but the saved Markdown prompt is not currently injected through skillPromptFor.",
    zhAction: "林方來源／全文來源鏈／@追溯來源", zhMode: "trace（來源鏈）",
    zhNote: "面板動作會使用 trace 模式，但目前沒有透過 skillPromptFor 注入此 Markdown 的保存提示詞。",
  },
  "tool/skills md/extract-zhupi.md": {
    state: "backend", action: "硃批 / @硃批", mode: "zhupi",
    note: "runZhupi checks skillPromptFor('extract-zhupi'), but this file has no Website Prompt section; the proxy's built-in prompt is therefore used.",
    zhAction: "硃批／@硃批", zhMode: "zhupi（硃批抽取）",
    zhNote: "runZhupi 會查詢 skillPromptFor('extract-zhupi')，但此檔沒有 Website Prompt，因此實際使用代理端內建提示詞。",
  },
  "tool/skills md/extract-emperor-action.md": {
    state: "local", action: "皇帝行動（奏／諭）", mode: "local emperor_action card",
    note: "The panel creates an editable emperor-action card locally. This Markdown supplies the specification, but no Website Prompt is sent to the model.",
    zhAction: "皇帝行動（奏／諭）", zhMode: "本機 emperor_action 卡片",
    zhNote: "面板直接在本機建立可編輯的皇帝行動卡片；此 Markdown 提供規格，但沒有 Website Prompt 送往模型。",
  },
  "tool/skills md/official-document-review-loop.md": {
    state: "live", action: "官文優先審閱迴圈", mode: "official_document_loop",
    note: "The one-click action chains the existing reading/event stages, then traverses only confirmed relationship records for the response stages.",
    zhAction: "官文優先審閱迴圈", zhMode: "official_document_loop（官文優先迴圈）",
    zhNote: "一鍵動作先串接既有閱讀與事件階段，再只沿已確認文書關係執行回應分析。",
  },
  "tool/skills md/confirmed-yu-response-analysis.md": {
    state: "backend", action: "官文迴圈：回應先前上諭", mode: "confirmed_yu_response",
    note: "The browser supplies only earlier Yu records already linked by official_reply_to_yu; the proxy analyzes response substance, not pair probability.",
    zhAction: "官文迴圈：回應先前上諭", zhMode: "confirmed_yu_response（既有配對回應分析）",
    zhNote: "瀏覽器只送出 official_reply_to_yu 已連結的先前上諭；代理分析答覆內容，不重新評估配對。",
  },
  "tool/skills md/combine-confirmed-emperor-actions.md": {
    state: "backend", action: "官文迴圈：硃批／上諭皇帝行動", mode: "combined_emperor_actions",
    note: "The browser supplies the selected rescript, yu_source-linked edicts, and an earlier emperor-action registry for semantic merge review.",
    zhAction: "官文迴圈：硃批／上諭皇帝行動", zhMode: "combined_emperor_actions（多來源皇帝行動）",
    zhNote: "瀏覽器送出本摺硃批、yu_source 配對上諭及較早皇帝行動清單，供語義合併審閱。",
  },
  "tool/skills md/official-response.md": {
    state: "backend", action: "官員回應 / @官員回應", mode: "official_response",
    note: "The action uses the official_response proxy mode. The saved Markdown is not loaded by skillPromptFor, so the proxy-side prompt performs the live analysis.",
    zhAction: "官員回應／@官員回應", zhMode: "official_response（官員回應）",
    zhNote: "此動作使用 official_response 代理模式；Markdown 未經 skillPromptFor 載入，實際分析由代理端提示詞執行。",
  },
  "tool/skills md/yu-response-pairing.md": {
    state: "embedded", action: "相關上諭配對", mode: "ask · runYuPairingForSel",
    note: "The panel uses an embedded YU_PAIR_PROMPT snapshot. It corresponds to this saved skill, but is not dynamically reloaded from the Markdown file.",
    zhAction: "相關上諭配對", zhMode: "ask · runYuPairingForSel",
    zhNote: "面板使用內嵌的 YU_PAIR_PROMPT 快照；內容對應此技能，但不會從 Markdown 動態重新載入。",
  },
  "tool/skills md/zhu-response-pairing.md": {
    state: "embedded", action: "相關硃批配對", mode: "ask · runZhuPairingForSel",
    note: "The panel uses an embedded ZHU_PAIR_PROMPT snapshot. It corresponds to this saved skill, but is not dynamically reloaded from the Markdown file.",
    zhAction: "相關硃批配對", zhMode: "ask · runZhuPairingForSel",
    zhNote: "面板使用內嵌的 ZHU_PAIR_PROMPT 快照；內容對應此技能，但不會從 Markdown 動態重新載入。",
  },
  "tool/skills md/shangyu-review-loop.md": {
    state: "generic", action: "Saved prompt list / 載入技能輸出", mode: "ask or bundle import",
    note: "Because it has a Website Prompt but no recognized Kind, it appears as a generic saved prompt in the document AI panel. Its structured loop output is also specially recognized when a review bundle is loaded.",
    zhAction: "保存提示詞清單／載入技能輸出", zhMode: "ask 或審閱套件匯入",
    zhNote: "此檔有 Website Prompt 但沒有已識別的 Kind，因此會在文書 AI 面板列為一般保存提示詞；載入審閱套件時，系統亦會特別辨識其結構化輸出。",
  },
  "tool/skills md/response-timeliness.md": {
    state: "live", action: "回應時效 / @回應時效", mode: "ask · runSituFit",
    note: "runSituFit dynamically loads this Website Prompt, then appends baseline, change_docs, and response_docs before sending the request.",
    zhAction: "回應時效／@回應時效", zhMode: "ask · runSituFit",
    zhNote: "runSituFit 會動態載入此 Website Prompt，再附加 baseline、change_docs 與 response_docs 後送出。",
  },
  "tool/skills md/zhu-review-loop.md": {
    state: "bundle", action: "載入技能輸出", mode: "review-bundle import",
    note: "This orchestration skill is run outside the live chat. The AI panel receives its stage outputs through the local review-bundle loader.",
    zhAction: "載入技能輸出", zhMode: "審閱套件匯入",
    zhNote: "此協調技能不在即時對話中執行；AI 面板透過本機審閱套件載入其各階段輸出。",
  },
};

function chatBindingFor(path) {
  const binding = chatBindings[path];
  if (binding) return currentLanguage === "zh" ? {
    ...binding, action: binding.zhAction, mode: binding.zhMode, note: binding.zhNote,
  } : binding;
  if (path.startsWith("tool/scripts py/")) return currentLanguage === "zh" ? {
    state: "terminal", action: "不在 AI 對話面板中執行", mode: "終端執行程式",
    note: "此 Python 檔負責批次選取、候選建立、代理呼叫或輸出寫入；面板只顯示其結果。",
  } : {
    state: "terminal", action: "Not executed in the AI chat panel", mode: "terminal runner",
    note: "This Python file handles batch selection, candidate construction, proxy calls, or output writing; the panel only displays its results.",
  };
  return currentLanguage === "zh" ? {
    state: "support", action: "支援規格", mode: "無直接面板綁定",
    note: "此檔支援本步驟，但目前未直接綁定至 AI 對話面板動作。",
  } : {
    state: "support", action: "Supporting specification", mode: "no direct panel binding",
    note: "This file supports the step but is not directly bound to an AI chat-panel action.",
  };
}

let currentLanguage = localStorage.getItem("ai-loop-language") === "zh" ? "zh" : "en";
let currentStepId = null;

function applyLanguage(language) {
  currentLanguage = language;
  document.documentElement.lang = language === "zh" ? "zh-Hant" : "en";
  document.querySelectorAll("[data-i18n]").forEach(element => {
    if (!element.dataset.en) element.dataset.en = element.textContent;
    const key = element.dataset.i18n;
    element.textContent = language === "zh" ? (zhUi[key] || element.dataset.en) : element.dataset.en;
  });
  const toggle = document.querySelector("#language-toggle");
  toggle.textContent = language === "zh" ? "English" : "中文";
  toggle.setAttribute("aria-label", language === "zh" ? "Switch to English" : "切換至中文");
  document.title = language === "zh" ? "清代君臣文書分析流程" : "Imperial Communication Analysis Workflow";
  localStorage.setItem("ai-loop-language", language);
  const loadingLabel = document.querySelector("#source-loading");
  if (loadingLabel && sourceFiles) {
    loadingLabel.textContent = language === "zh"
      ? `可閱讀 ${Object.keys(sourceFiles).length} 份來源檔案`
      : `${Object.keys(sourceFiles).length} source files available`;
  }
  if (dialog?.open && currentStepId) renderStep(currentStepId);
}

function localizedStep(stepId) {
  const base = steps[stepId];
  if (currentLanguage !== "zh" || !zhSteps[stepId]) return base;
  return {...base, ...zhSteps[stepId], files: base.files};
}

const dialog = document.querySelector("#step-dialog");
const dialogTitle = document.querySelector("#dialog-title");
const dialogPhase = document.querySelector("#dialog-phase");
const dialogStatus = document.querySelector("#dialog-status");
const dialogSummary = document.querySelector("#dialog-summary");
const dialogLogic = document.querySelector("#dialog-logic");
const dialogContract = document.querySelector("#dialog-contract");
const dialogChatUsage = document.querySelector("#dialog-chat-usage");
const sourceTabs = document.querySelector("#source-tabs");
const sourcePath = document.querySelector("#source-path");
const sourceCode = document.querySelector("#source-code code");
const sourceLoading = document.querySelector("#source-loading");
let sourceFiles = null;

function renderList(target, values) {
  target.replaceChildren(...values.map(value => {
    const li = document.createElement("li");
    li.textContent = value;
    return li;
  }));
}

function renderContract(contract) {
  const nodes = [];
  Object.entries(contract).forEach(([term, description]) => {
    const dt = document.createElement("dt");
    const dd = document.createElement("dd");
    dt.textContent = term;
    dd.textContent = description;
    nodes.push(dt, dd);
  });
  dialogContract.replaceChildren(...nodes);
}

function bindingStateLabel(state) {
  const labels = currentLanguage === "zh" ? {
    live: "即時載入提示詞", "not-linked": "面板動作存在／提示詞未連結", backend: "代理端提示詞",
    local: "本機面板功能", embedded: "內嵌提示詞快照", generic: "一般保存提示詞",
    bundle: "審閱套件匯入", terminal: "僅供終端執行", support: "支援規格",
  } : {
    live: "Live saved prompt", "not-linked": "Panel action / prompt not linked", backend: "Proxy-side prompt",
    local: "Local panel function", embedded: "Embedded prompt snapshot", generic: "Generic saved prompt",
    bundle: "Review-bundle import", terminal: "Terminal only", support: "Supporting specification",
  };
  return labels[state] || state;
}

function renderChatUsage(paths) {
  const rows = paths.map(path => {
    const binding = chatBindingFor(path);
    const row = document.createElement("article");
    row.className = `chat-binding chat-binding-${binding.state}`;

    const head = document.createElement("div");
    head.className = "chat-binding-head";
    const filename = document.createElement("code");
    filename.textContent = path;
    const state = document.createElement("span");
    state.textContent = bindingStateLabel(binding.state);
    head.append(filename, state);

    const action = document.createElement("strong");
    action.textContent = binding.action;
    const mode = document.createElement("code");
    mode.className = "chat-binding-mode";
    mode.textContent = binding.mode;
    const note = document.createElement("p");
    note.textContent = binding.note;
    row.append(head, action, mode, note);
    return row;
  });
  dialogChatUsage.replaceChildren(...rows);
}

async function loadSources() {
  if (sourceFiles) return sourceFiles;
  sourceLoading.textContent = currentLanguage === "zh" ? "正在載入來源檔案……" : "Loading source files…";
  const response = await fetch("/api/workflow-sources");
  const payload = await response.json();
  if (!response.ok || payload.error) throw new Error(payload.error || (currentLanguage === "zh" ? "無法載入來源檔案。" : "Source files could not be loaded."));
  sourceFiles = payload.files || {};
  sourceLoading.textContent = currentLanguage === "zh"
    ? `可閱讀 ${Object.keys(sourceFiles).length} 份來源檔案`
    : `${Object.keys(sourceFiles).length} source files available`;
  return sourceFiles;
}

function showSource(path) {
  const file = sourceFiles?.[path];
  sourcePath.textContent = path;
  sourceCode.textContent = file?.text || `Source file is not available: ${path}`;
  sourceTabs.querySelectorAll("button").forEach(button => {
    const selected = button.dataset.path === path;
    button.setAttribute("aria-selected", String(selected));
  });
}

function renderSourceTabs(paths) {
  const buttons = paths.map((path, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.role = "tab";
    button.dataset.path = path;
    button.setAttribute("aria-selected", String(index === 0));
    button.textContent = path.split("/").pop();
    button.addEventListener("click", () => showSource(path));
    return button;
  });
  sourceTabs.replaceChildren(...buttons);
}

function renderStep(stepId) {
  const step = localizedStep(stepId);
  if (!step) return;
  dialogPhase.textContent = step.phase;
  dialogTitle.textContent = step.title;
  dialogStatus.textContent = step.status;
  dialogSummary.textContent = step.summary;
  renderList(dialogLogic, step.logic);
  renderContract(step.contract);
  renderChatUsage(step.files);
}

async function openStep(stepId) {
  const step = localizedStep(stepId);
  if (!step) return;
  currentStepId = stepId;
  renderStep(stepId);
  sourceTabs.replaceChildren();
  sourcePath.textContent = "";
  sourceCode.textContent = currentLanguage === "zh" ? "正在載入來源檔案……" : "Loading source files…";
  if (!dialog.open) dialog.showModal();
  try {
    await loadSources();
    renderSourceTabs(step.files);
    showSource(step.files[0]);
  } catch (error) {
    sourceLoading.textContent = currentLanguage === "zh" ? "來源檔案無法使用" : "Source files unavailable";
    sourceCode.textContent = currentLanguage === "zh"
      ? `${error.message}\n\n請透過本機審閱伺服器開啟本流程，以閱讀完整 .md 與 .py 檔案。`
      : `${error.message}\n\nOpen this workflow through the local review server to inspect the complete .md and .py files.`;
  }
}

document.querySelectorAll("[data-node]").forEach(button => {
  button.addEventListener("click", () => openStep(button.dataset.node));
});

document.querySelector("#dialog-close").addEventListener("click", () => dialog.close());
dialog.addEventListener("click", event => {
  if (event.target === dialog) dialog.close();
});

document.querySelector("#language-toggle").addEventListener("click", () => {
  applyLanguage(currentLanguage === "en" ? "zh" : "en");
});

applyLanguage(currentLanguage);
