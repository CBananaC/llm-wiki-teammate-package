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
「密折」「折子」或「奏帖」，是清代臣工直接上奏皇帝的文書；隨着大量
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
