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
