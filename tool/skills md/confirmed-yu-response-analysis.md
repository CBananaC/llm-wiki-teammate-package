# Skill: 分析官文如何回應已確認上諭

**Kind:** confirmed_yu_response

## Purpose

For one selected official document, follow only existing
`official_reply_to_yu` records in `confirmed-pairs.json` (plus pairs the user has
already adopted in the review state). Do not search the corpus and do not decide
whether the documents form a pair. The pair is already evidence.

Analyze how the official document responds to each paired earlier `上諭`:

- identify the concrete imperial comment, question, or command being answered;
- quote the official's own response, excluding any embedded re-quotation of the
  emperor's words;
- distinguish compliance, progress reporting, defence, clarification, request,
  and acknowledgement;
- split independent response points into separate review items.

Cards reuse the current `docpair` / `yu-response-pairing-nocite` visual form, but
their subtitle, description, quotations, and relation note describe the response
content. They do not show pairing criteria or offer a new corpus search.

## Website Prompt

```text
配對關係已由研究者確認，不要搜尋其他文書、不要評分配對強弱、也不要解釋為何兩篇是配對。以『本官文如何回應每一道已確認上諭』為中心：先在上諭中區分（A）皇帝轉述的據奏情報與（B）皇帝自己的評論、命令或詢問，只針對（B）分析回應。為每一道上諭拆成一項或多項具體回應，每項給 yu_doc_id、subtitle（直接命名官員如何回應哪一項諭令）、description（交代諭命與官員的具體答覆，不談配對規則）、response_type（done|progress|defence|clarification|request|ack）、quote_in_reply（官員自己的回應原文，排除其重引的皇帝話語）、matched_yu_span（上諭中被回應的皇帝原話逐字，不取據某奏等轉述層）、relation_note（諭命／諭問什麼 → 本官如何答覆）。卡片沿用 docpair／無引文回應卡版式，以回應內容為主。若官文只重引上諭而無自己的答覆，不得虛構回應。引文必須逐字，不得杜撰。
```

## Proxy

`tool/proxy/gemini-proxy/main.py`, mode `confirmed_yu_response`.

Input contains exactly one official document and the earlier `上諭` records
already linked to it. Output:

```json
{
  "items": [
    {
      "yu_doc_id": "諭…",
      "subtitle": "官員如何回應某項諭令",
      "description": "具體說明",
      "response_type": "done|progress|defence|clarification|request|ack",
      "quote_in_reply": "官員自己的逐字回應",
      "matched_yu_span": "皇帝被回應的逐字原話",
      "relation_note": "諭命／諭問什麼 → 官員如何答覆",
      "where": "",
      "who": [],
      "who_loc": {},
      "relations": []
    }
  ]
}
```

Never invent quotations, never use an unconfirmed pair, and never turn a mere
repetition of the `上諭` into an official response.
