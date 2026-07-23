# Skill: 皇帝行動（硃批＋既有配對上諭）

**Kind:** combined_emperor_actions

## Website Prompt

```text
只根據輸入的本奏摺、其中皇帝的硃批，以及研究者既有配對資料所連到的上諭，擷取皇帝自己的評論、答覆、褒獎、責備、准駁、詢問或命令。不得搜尋其他上諭或另造配對。**本奏摺是關聯性範圍的錨點**：既有 `yu_source` 只表示該上諭可以作為候選來源，不代表整道上諭的每一項命令都在回應本奏摺。對每一項行動作語義關聯判斷，填 `memorial_relation`：`direct` 表示皇帝的評論／命令直接回應本奏摺自己的報告、請求、問題或具體事實，允許不同措辭與間接指涉；`contextual` 表示同一民變、同一事件或同一上諭網絡中的相關內容，但其實是在回應別的奏摺、別的官員或別的問題；`unrelated` 表示沒有有意義的關聯。只有 `direct` 才能輸出，`contextual` 與 `unrelated` 省略。不要只用逐字相似或人名是否相同判斷：若命令對另一官員，但本摺具體提供了觸發該命令的事項，仍可判 `direct`；反之，同一大事件或同一上諭並不足以判定直接回應。以硃25為例，本摺主要自述黃仕簡帶兵赴臺；關於任承恩已渡臺或常青的一般鎮定調度，若不是本摺自身提出或回報的事項，應判 `contextual`，不予輸出。先區分上諭中的「據某奏／某官報告」等轉述情報與皇帝自己的話；前者不是皇帝行動。每一項只能是一個具體皇帝行動：若同一段上諭或硃批含數個不同指示（例如既命嚴防餘眾內渡、又交代撫恤被害官員、又告誡調兵須鎮定），必須拆成數項。反之，若硃批與已配對上諭以不同措辭表達同一件事（例如硃批稱某官辦理甚好、上諭稱該官辦理妥善），合為一項並在 sources 同時列出硃批與上諭；只有同一對象且同一具體評論／命令才算同一件，僅主題相近不算。每項給 title、description、memorial_relation、relevance_reason、action_type（comment|reply|praise|blame|approve|reject|question|command）、whenCh、whenAr、where、who、who_loc、relations、same_as_event_id 及 sources。每個 source 必須含 doc_id、source_type（硃批或上諭）、quote（皇帝原話逐字）、title、date；若 source_type 為硃批，另填 position（夾批或尾批）。夾批必須在 context_quote 填入其緊鄰、被批註的奏摺原文那一句（官員的話，逐字）；尾批或上諭的 context_quote 留空字串。source 的 doc_id 只能來自本奏摺或輸入的既有配對上諭。只可把 same_as_event_id 設為輸入的較早皇帝行動清單中的 id，並只在對象與具體評論／命令均相同時使用；若重複，title 沿用該最早行動的標題。不要把「已有旨」「另有旨」等無實質內容的套語單獨當作行動。只輸出 JSON：{"actions":[{"title":"","description":"","memorial_relation":"direct|contextual|unrelated","relevance_reason":"","action_type":"comment|reply|praise|blame|approve|reject|question|command","whenCh":"","whenAr":"","where":"","who":[],"who_loc":{},"relations":[],"same_as_event_id":"","sources":[{"doc_id":"","source_type":"硃批|上諭","position":"夾批|尾批","quote":"","context_quote":"","title":"","date":""}]}]}。所有引文必須逐字來自輸入文本，不得杜撰。
夾批的 `context_quote` 必須逐字引用其所批註的完整奏摺原文句子或完整分句，不得只摘錄最後幾個字（例如不得只寫「首報加以重賞」）；要保留足以理解主語、動作與對象的較長上下文。尾批或上諭的 `context_quote` 留空字串。
```

## Purpose

The pair files decide which documents may participate; the model only explains
the imperial content in those documents. The selected official document's
硃批 and every `yu_source`-linked 上諭 are sent together so semantically
equivalent imperial wording can become one action with multiple quotations.
The model must still distinguish a direct response to the selected memorial
from merely contextual material elsewhere in the same 上諭 network.

The existing `相關上諭` card is used for display. Its source quotations remain
clickable, and the existing earlier-action comparison offers merge or keep
separate when a concrete imperial action has already appeared.

## Evidence rules

- Do not infer an imperial command from a reported fact.
- Treat the selected memorial as the relevance boundary. A linked 上諭 may contain
  many commands for other officials; omit actions judged `contextual` or
  `unrelated`, even when they concern the same wider incident. The judgement is
  semantic rather than an exact-quote or name-matching test.
- For every retained action, give `relevance_reason` in one Traditional Chinese
  sentence explaining why it directly responds to this memorial. An exact quote
  may be included when useful, but is not required.
- Do not invent a source quotation or use a document not supplied in the input.
- Routine routing formulae are supporting context only.
- Missing evidence is an empty source or no action, not a guessed relationship.
- For a 夾批 `context_quote`, quote the complete adjacent memorial sentence or
  complete clause verbatim. Do not return only the final few words, such as
  `首報加以重賞`; retain enough context to identify the subject, action, and
  object being commented on. 尾批 and 上諭 sources leave `context_quote` empty.

## Point-card constraints

- `title` is the subtitle of one concrete action, not the title of the whole
  linked 上諭. If one 上諭 contains several commands, every point must have its
  own specific title naming its object and action; never repeat a generic
  `諭閩浙總督…` wrapper title for unrelated points.
- `memorial_relation` is required for every action and must be `direct`,
  `contextual`, or `unrelated`. Only `direct` actions are output. The
  `relevance_reason` is a semantic explanation, not a required verbatim quote.
- `same_as_event_id` is only an exact same-action reference to an item in the
  supplied earlier-action list. Do not use it merely because the same 上諭,
  official, or broad topic appears.
