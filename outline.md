# Intro Website Outline

## Approved framing

The website presents a general-purpose system for reviewing Qing official
communication. 林爽文事件 is a case study that demonstrates how the system
can help researchers study 奏折 and 上諭; it is not the system's only subject.

奏折 and 上諭 are introduced as “two central forms of Qing imperial
communication.” 硃批 is explained as the emperor's vermilion response written
on or attached to a memorial, and as an important response layer for
reconstructing the communication chain.

The homepage opening is:

> **Reconstructing Qing Imperial Communication**
>
> An AI-assisted, human-reviewed system for studying 奏折, 硃批, and 上諭.

## Brainstorm record — assistant response

The following records the assistant's previous brainstorm output that was
approved as the starting point for this outline.

Yes, this is the stronger framing. The website should present a general-purpose system for reviewing Qing official communication, while 林爽文事件 is only the case study that demonstrates its value.

For historical precision, I suggest describing 奏折 and 上諭 as “two central forms of Qing imperial communication”:

- 奏折: officials report to the emperor.
- 硃批: the emperor’s vermilion response written on or attached to a memorial.
- 上諭: imperial instructions sent from the emperor to officials.

The proposed website structure could be:

1. **What are 奏折 and 上諭?**
   Introduce their functions, participants, direction of communication, and value as first-hand historical materials.

2. **Why are they difficult to study?**
   Explain the enormous quantity of documents, fragmented communication chains, missing dates, unclear replies, and time delays between officials, the emperor, and the battlefield.

3. **Why visualization is necessary**
   Show how plain-text reading hides chronology and relationships, while timelines, dots, lines, and chart lanes reveal communication patterns.

4. **What this website does**
   Present the system as an AI-assisted, human-reviewed research environment:

   `large text corpus → AI extraction → relationship reconstruction → human review → visual chart`

5. **Case study: 林爽文事件**
   Explain why it is a useful example: wartime communication was crucial, information delay affected military decisions, and a substantial corpus of 奏折 and 上諭 survives in scholarly compilations.

6. **Core design principle**
   Emphasize that AI proposes; humans judge. Users read the original source, verify quotations and dates, review AI outputs in the chat panel, and only then add accepted events or relationships to the chart.

7. **How to use the system**
   Cover source selection, document search, AI-output review, timeline reading, relationship inspection, and chart interaction.

8. **How to recreate the system**
   Explain:
   - choosing a research question and corpus;
   - OCR and source-preserving structuring;
   - storing document type, title, sender, receiver, dates, original text, and provenance;
   - reconstructing relationships through explicit textual evidence, date rules, and LLM assistance;
   - running skills on individual documents;
   - loading JSON outputs into the website;
   - human verification and chart promotion.

9. **The AI loop**
   Introduce the three components separately:
   - **Skills:** task-specific instructions defining what to extract and how to preserve evidence.
   - **AI model:** Claude, GPT, Gemini, DeepSeek, etc.; compare them by task, accuracy, structure, cost, speed, and Chinese-text performance.
   - **Loop:** repeatable processing across many documents, with JSON outputs, resumability, and review bundles.

   Model comparisons should be based on small project tests rather than permanent claims that one model is always best.

10. **Research example and further use**
    Display selected 林爽文 research results, then explain how reviewed outputs can feed the LLM Wiki and future historical research.

For the UI, I suggest separating the website into two modes:

- **System mode:** explains the general method and teaches students how to recreate it.
- **Case-study mode:** demonstrates the method with 林爽文事件 materials.

The homepage could begin with:

> **Reconstructing Qing Imperial Communication**
>
> An AI-assisted, human-reviewed system for studying 奏折, 硃批, and 上諭.

Visually, the most effective interactive element would be a single document journey:

`奏折 sent → emperor receives → 硃批／上諭 issued → official receives or acts → later report`

Known dates should appear as solid points. Missing or inferred dates should appear as gaps or dashed elements rather than invented precision.

The four-line chart should be explained using the system’s actual lane labels. The introduction site should avoid inventing new lane names or implying that 林爽文事件 is the system’s only possible subject.

## Draft content — What are 奏折 and 上諭?

### 這一部分要讓學生理解甚麼

奏折和上諭不是兩類互相獨立的歷史文件，而是清代皇帝與官員之間往返
通信的兩個主要方向。奏折由官員上呈皇帝，上諭則由皇帝下達臣下；硃批
是連接兩者的重要回應層。這一部分先建立文書的方向、功能和研究價值，
再引導讀者理解後文的時間差與關係重建問題。

### 可直接放入網站的正文

#### 奏折與上諭：清代帝國通信的兩種核心形式

在研究清代政治和戰爭時，奏折與上諭不能只被看成兩類互相獨立的文件。
奏折通常由官員向皇帝呈報，讓皇帝接收來自地方和前線的消息；上諭則由
皇帝向臣下發布，傳達命令、判斷和處置方向。兩者形成一條往返的文書
通信，將身處不同地方的官員和皇帝連接起來。

#### 奏折：官員向皇帝呈報

奏折是官員向皇帝呈報政務的上行官方文書。學者王劍指出，奏折亦稱
「密折」「折子」或「奏帖」，是清代臣工直接上奏皇帝的文書；隨著大量
原本收藏於宮中的奏折逐步公開，這類文書的史料價值也受到學界重視。對
研究者而言，奏折不只是某一位官員的報告，也保存了官員如何描述情勢、
提出請求、解釋行動和回應中央要求的過程。

在戰爭情境中，前線官員可以透過奏折報告戰況、請求援兵、說明糧餉和
交通困難，或提出下一步的行動計畫。這些內容讓研究者能夠追問：官員在
甚麼時候掌握了哪些消息？他向皇帝呈報了甚麼？又有哪些情況可能沒有被
寫入奏折？

#### 上諭：皇帝向官員發布指示

上諭是皇帝以自身名義向臣下發布的指示或命令。它可以回應官員的奏報，
也可以對戰略、軍務、人事和地方行政作出判斷、要求、嘉獎或責備。與奏折
由下而上不同，上諭代表皇帝把中央的判斷和要求傳回地方或前線。

上諭並不等於單一固定的傳遞路徑。清代涉及機密政務時，皇帝的指示可能
由內廷官員協助撰擬，後來亦常由軍機處處理廷寄；因此，研究文書通信時，
需要把「上諭」理解為皇帝發布的指示或文書類型，把「廷寄」理解為其中
一種傳達和運轉方式，而不能把兩者不加區分地當成同義詞。

#### 硃批：連接奏折與上諭的回應層

在奏折送到皇帝手中後，皇帝可以在奏折上以硃筆批示，形成硃批。硃批
不是另一個與奏折、上諭完全平行的方向，而是皇帝閱讀和回應奏折的重要
記錄。後續的上諭也可能延續、補充或調整硃批所反映的判斷。

因此，本網站不只把文件按照類型分開，也會嘗試把它們放回通信關係中
閱讀：

`官員發出奏折 → 皇帝收到並作硃批 → 皇帝發出上諭 → 官員收到或採取行動`

這條路徑不是每一份文件都能完整重建。研究者需要檢查原文、日期、人物、
地點和回應語句，才能判斷某一份上諭是否真的回應某一份奏折。若收到日期
缺失，或文件關係只是根據語義推測，網站應該保留這種不確定性，而不是
把推算日期或推測關係寫成確定事實。

奏折和上諭的研究價值，正是在於它們讓我們不只看見皇帝最後下了甚麼
命令，也能追蹤消息如何由地方上報、在中央被閱讀和判斷，再以新的文書
傳回前線。當這些文件數量增加，通信之間的時間差和關係就越難單靠逐篇
閱讀掌握；這也是本網站需要把原文、文書關係和時間線放在一起呈現的原因。

### 建議的互動或視覺呈現

以三張互相連接的文件卡片展示：

- `奏折`：官員 → 皇帝；顯示發出者、發出日期和原文摘錄。
- `硃批`：皇帝在奏折上的回應；顯示批示文字和可核對的日期資料。
- `上諭`：皇帝 → 官員；顯示發布者、接收對象、發布日期和命令內容。

卡片之間以箭頭連接，但對缺失或推算的日期使用虛線或空白狀態。點擊
任何卡片後，學生都應該可以回到原文和來源資訊，而不是只看到 AI 生成
的摘要。

### 本段使用的來源

- 王劍，〈近50年來清代奏摺制度研究綜述〉，《中國史研究動態》，2004年
  第7期，頁20–21。原文 PDF 位於
  `2nd Material & FYP/(2)二手研究/(3)中央制度、軍機處與文書傳遞/`。
- 宋希斌，《清代軍機處職權的來源及其演變：以公文運轉程序與政局變動為
  核心的考察》，中國社會科學出版社，2018，頁碼待核。該資料說明上諭
  撰擬、廷寄運轉和軍機處處理奏摺之間的制度關係。
- 臺灣史料集成編輯委員會編，《明清臺灣檔案彙編》第32冊，臺北：遠流出版
  事業股份有限公司，2007，頁503；台852。這是資料夾內「收訊息時間」
  筆記所引用的福康安接收上諭案例，正式公開前仍應回到原始編纂本核對。

### 需要人工核對

- 宋希斌資料是資料夾內的文字摘錄，尚未確定其對應的原書頁碼；公開網站
  需要補回原書頁碼。
- 需要確認網站正文是否把「上諭」和「廷寄」採用上述區分，並以專案實際
  的 `doc_type`、資料欄位和 UI 顯示名稱作最後統一。
- `奏折` 是網站正文的統一用語；直接引用來源時，保留書名、檔名和原文
  中的「奏摺」字形。

## Draft content — Why are they difficult to study?

### 這一部分要讓學生理解甚麼

研究奏折和上諭的困難，不只是文件數量多，而是文件分散在不同編纂本和
檔案系統中，通信關係、收發日期和資訊內容也不一定完整。研究者需要同時
處理文字、時間、人物、地點和來源版本，才能判斷一份文件在通信網絡中的
位置。

### 可直接放入網站的正文

#### 為甚麼奏折與上諭難以研究？

奏折和上諭留下了大量關於清代政治、地方治理和戰爭的記錄，但數量龐大
並不代表它們可以直接拼成一個完整故事。學者王劍指出，隨著大量原本收藏
於宮中的奏折逐步公開，奏折的史料價值才受到學界重視；然而，研究者要
理解這些材料，仍然需要追問它們如何形成、如何傳遞，以及在甚麼制度環境
下被保存下來。對今天的研究者而言，同一事件可能分散在不同官員的奏折、
皇帝的硃批、後續上諭和後來的文獻彙編之中。

第一個困難，是它們不是一組整齊的來回對話。官員可能先後多次呈報同一
問題，皇帝也可能根據不同時間收到的消息，先後發出幾道內容不同的上諭。
一份文件有時只提到「前奏」或「前旨」，卻不完整列出所回應的文件；同一
場戰事也可能由前線官員、福建後方大臣和北京官員從不同位置加以描述。
因此，研究者不能只按照文件出現的次序閱讀，而要比較文句、人物、地點和
事件，逐步重建它們之間可能存在的關係。

第二個困難，是文書上的「日期」不只有一個。研究者可能需要區分事件
發生日期、官員發出奏折的日期、皇帝收到奏折並作硃批的日期、上諭發布的
日期，以及官員收到上諭的日期。這些日期有時並不完整，甚至需要根據
奏折正文中「接到」或「奉到」某日上諭的語句反推。以福康安等人的台951
為例，文件記錄的發出日期是1787年9月24日，而收到／硃批日期是同年10月7日，
中間相隔十三日。這段時間對正在渡海和作戰的官員而言，可能足以讓戰場
形勢發生變化。

在臺灣戰場，距離和海峽風浪又進一步放大了這個問題。李智君指出，閩浙
總督的奏折由臺灣發出，到乾隆收到硃批或諭旨返回，往往需要一兩個月。專案
對文件日期的統計也顯示，福康安硃批奏折由發出至皇帝收到，平均約24.86日；
柴大紀的奏折平均約45日。這表示皇帝收到的往往不是正在發生的戰場，而是
數日、數週甚至更早以前的戰場。相反地，前線官員收到上諭時，皇帝當初作出
判斷所依據的情勢也可能已經改變。

第三個困難，是文書本身不是透明而完整的現場記錄。官員需要在奏折中選擇
如何描述戰況、解釋延誤和提出請求；皇帝則只能根據已經送達的材料判斷前線
情勢。不同官員的資訊位置不一樣：前線將領較早接觸戰場，福建後方官員負責
接收和轉報消息，北京的皇帝則擁有最高決策權，卻可能最晚收到最新情報。由此
可見，研究者不只要問「發生了甚麼」，還要問「誰在甚麼時候知道甚麼」，以及
「哪些資訊在傳遞、整理和回應的過程中被保留、改變或延遲」。

最後，單靠按順序閱讀的純文字，很難同時看見這些層次。文字可以保存原文
和細節，卻不容易讓研究者一眼看出文件之間的時間差、回應關係、人物位置和
地理距離。這也是本網站需要把原文保留下來，再以結構化資料、時間線和關係
圖表輔助閱讀的原因。AI 可以協助從大量文字中提出日期、人物、行動和可能的
文件關係，但每一項結果仍然需要回到原文，由研究者核對和判斷。

### 建議的互動或視覺呈現

使用一條可以逐步展開的通信時間線，並把不同種類的時間分開顯示：

`事件發生 → 奏折發出 → 皇帝收到／硃批 → 上諭發出 → 官員收到或行動`

已知日期使用實線和實心點；由正文反推的日期使用虛線和「推算」標籤；
缺失日期則保留空白。點擊一份文件時，同時顯示原文、來源、發出者、接收者
和目前判斷的關係，讓學生看見「研究困難」如何轉化為網站的資料設計。

### 本段使用的來源

- 王劍，〈近50年來清代奏摺制度研究綜述〉，《中國史研究動態》，2004年
  第7期，頁20–21。
- 李智君，〈清代大陸兵力對臺灣的跨海投送——以乾隆朝平定林爽文的戰爭為
  例〉，《南國學術》，2021年第1期，頁碼待核；資料夾內的書目記錄出現
  頁118–130與頁118–131兩種版本。
- 臺灣史料集成編輯委員會編，《明清臺灣檔案彙編》第33冊，臺北：遠流出版
  事業股份有限公司，2007，頁191；台951。
- 專案研究筆記〈收訊息時間〉，資料來源為
  `matched_blocks_grouped_by_unified_date.json`；此項統計沒有出版頁碼，
  正式公開前需由研究者重新核對原始文件和計算方法。

### 需要人工核對

- 「台951」的文件類型、發出日期、收到／硃批日期和《明清臺灣檔案彙編》
  第33冊頁191，需回到原始編纂本再核對一次。
- 李智君文章的頁碼在 `FYP_Essay.docx`、`Reference List.docx` 和研究筆記
  之間不一致；公開網站應先補正頁碼，再把「頁碼待核」改為正式頁碼。
- 柴大紀平均約45日是專案統計結果，不應冒充已出版研究的頁碼結論；需要
  在網站中標示統計口徑、納入條件和資料來源。

## Draft content — Why is visualization necessary?

### 這一部分要讓學生理解甚麼

視覺化不是把歷史材料裝飾成圖表，而是把原本分散在不同文件中的時間、
人物、地點、行動和文書關係放到同一個可檢查的分析介面中。學生需要明白，
圖表可以幫助研究者提出問題和發現關係，但不能取代原文，也不能把推算
結果變成確定的歷史事實。

### 可直接放入網站的正文

#### 為甚麼研究奏折與上諭需要視覺化？

如果研究者只按照文件在檔案或資料庫中的排列次序閱讀，每一份奏折和上諭
往往只呈現一個官員、一次報告或一個時間點。可是，清代帝國通信真正值得
研究的地方，正在於不同時間點之間的落差：一件戰事何時發生，前線何時
上奏，皇帝何時收到，硃批或上諭何時形成，以及命令何時抵達前線。這些
資訊分散在不同欄位、文件和正文語句之中，單靠逐篇閱讀很難同時掌握。

例如，福康安抵臺初期的研究顯示，乾隆對諸羅戰局的判斷曾隨著新奏報抵達
而改變，戰略先後在「先救諸羅、再攻大里杙」、「直接進攻大里杙」和按前線
情勢彈性進兵之間調整。若只閱讀其中一份上諭，研究者可能只看見皇帝在
某一時刻作出的命令，卻看不見這項命令所依據的消息、它抵達前線時的時間，
以及前後判斷如何互相修正。（本專案研究稿〈戰爭中的資訊延遲與中央集權——以福康安平定林爽文事件（1786–1788）的戰略形成過程為例〉，未刊稿，頁17–26。）

視覺化可以把這個過程拆成幾種彼此連接的元素。時間軸顯示事件發生、文書
發出和收到之間的先後；不同分道區分皇帝、地方官員、前線或其他研究者
指定的行動位置；點代表文件或事件，線則代表呈報、回應、命令、接收或
後續行動。當研究者把這些元素放在一起，便能從「某一份文件寫了甚麼」
進一步追問「誰在甚麼時候知道甚麼」和「這個消息如何影響下一步行動」。

這種做法也能處理地理空間對通信的影響。林加豐研究〈清軍圍捕林爽文圖〉
時指出，戰圖可以呈現清軍兵力配置、追捕路線和內山地形，並補充文字文獻
記載不足的部分；他更指出，圖像中的路線和部署能夠幫助研究者重建文字
材料未能完整說明的追剿過程。（林加豐，〈圖史互證：院藏〈清軍圍捕林爽文圖〉與福康安剿捕林爽文之役〉，《故宮學術季刊》，第二十六卷第三期，2009年春季，頁121–122。）

同樣地，奏折與上諭的圖表不應只顯示「有沒有文件」，還要保存文件的
時間性和證據層次。已由原文直接確認的日期、人物或關係，可以使用實線和
實心點；根據正文語句反推的日期，應使用虛線並標示「推算」；無法確認的
部分則保留空白或「未知」狀態。這樣的設計讓研究者看見材料的限制，而不
會誤以為每一段文書通信都已經被完整重建。

因此，本網站的視覺化功能不是直接替研究者作出結論，而是提供一個可以
反覆檢查的中介層。使用者可以從圖表發現可能的時間差或文件關係，再點擊
回到原文、來源卷冊和 AI 提出的證據，檢查圖上的每一個點和每一條線是否
有足夠根據。換言之，圖表負責把複雜關係呈現出來，原文和研究者的判斷
則決定這些關係能否被接受。

### 建議的互動或視覺呈現

以同一組文件製作「純文字閱讀」與「關係圖表」的對照：

- 左側顯示奏折或上諭原文，保留文件編號、來源、發出者、接收者和日期。
- 右側顯示時間軸及分道，把事件、奏折、硃批、上諭和後續行動放在相互
  可追蹤的位置。
- 點擊文件時，同步突出其前一份來源、後續回應和相關事件；若關係只是
  根據文字或日期推測，使用虛線並顯示「推測關係」。
- 在圖表旁保留「已知」「推算」「未知」的圖例，讓學生學會區分史料證據
  和研究者的重建。

### 本段使用的來源與核對

- 福康安戰略變化的例子取自本專案研究稿〈戰爭中的資訊延遲與中央集權——
  以福康安平定林爽文事件（1786–1788）的戰略形成過程為例〉，未刊稿，
  頁17–26；該檔案未載作者與年份，網站正式出版前需要補回完整書目。
- 林加豐文章的出版資訊和頁碼已按資料夾內 PDF 核對；引用內容集中在頁
  121–122。
- 「已知／推算／未知」和圖表互動屬於本網站的研究設計，不是上述文獻的
  直接結論；正式實作時需要與網站實際資料欄位和四條分道的名稱保持一致。
