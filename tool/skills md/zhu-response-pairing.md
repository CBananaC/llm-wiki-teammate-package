# Saved Prompt / Skill: 硃批—回應配對 (ZHU response pairing)

## Purpose

Identify which official document (奏摺／硃批-bearing memorial) is **acknowledging
or replying to which `硃批`** (the emperor's vermillion rescript), across the
whole corpus, and output the pairs with quotation evidence for the researcher to
review and (later) confirm.

This is the sibling of `yu-response-pairing.md`. There the emperor side is an
`上諭` (a standalone edict record); here the emperor side is a `硃批` — the
rescript the emperor wrote **on an official's own earlier memorial**. That
memorial is a normal record in the corpus (`type` `zhupi` or `shangzou`) whose
`rescript` field holds the emperor's words. When the same official later writes a
new memorial that opens `…奉硃批：「…」欽此`, he is quoting the emperor's rescript on
**his own earlier document** — that earlier document is the pair's emperor side.

Scope of this first version: **quote-bearing replies only.** A reply that merely
states it received a 硃批 but does **not** quote it (`奉到硃批，欽遵在案` with no
`「…」`) is a **later phase** — this version pairs only replies that reproduce the
rescript text. Confirm-to-write-back and the chart connector line reuse the yu
pipeline's later phases.

The worked examples this skill is built around:

- **台46 (常青)** opens `竊臣奏請來京請訓一摺，於十二月二十四日奉到硃批：「准汝來。」欽此`.
  The `硃批「准汝來。」` sits on 常青's earlier memorial (`奏請來京請訓一摺`); that
  earlier record is the emperor side of the pair.
- **台108 (孫士毅)** opens `…挑備戰兵以資策應一摺，本年正月二十四日敬奉硃批：「另有旨諭。」欽此`.
  The `硃批「另有旨諭。」` sits on 孫士毅's earlier `挑備戰兵` memorial.

Note three things these examples prove and the method relies on: (a) the reply
carries a 硃批 citation marker (`奉到硃批`／`敬奉硃批`／`奉硃批`); (b) the quoted
rescript is **short** — often two to six characters (`准汝來`, `另有旨諭`) — so it
frequently cannot be disambiguated by wording alone; (c) the reply usually names
the **date it received the 硃批** and, right before the marker, **which of its own
earlier memorials** the rescript answered (`奏請來京請訓一摺`).

## How a pair is determined

Three signals feed the judgement:

1. **Identity** — the 硃批 sits on an **earlier memorial by the same official**
   who is now quoting it. So the reply's author equals the emperor-side
   document's author. (This is the strongest structural signal, because a 硃批 is
   a private reply to that official's own memorial. It replaces the yu pairing's
   "reply author is one of the edict's recipients" test.)
2. **Date** — the emperor-side document's 硃批 date (`recvAr`) is **before** the
   reply's send date, within a plausible window. The reply often states the 硃批
   receipt date explicitly (`十二月二十四日奉到硃批`); when it does, that stated
   date should line up with the emperor-side document's `recvAr`.
3. **Citation** — the reply cites the rescript: a marker (`奉硃批`／`奉到硃批`／
   `敬奉硃批`／`欽奉硃批`／`蒙硃批`) followed by a `「…」` quotation whose wording
   matches the emperor-side document's `rescript` field. Because rescripts are
   short, an **exact or near-exact** match of the quoted characters to the
   candidate's `rescript` is the decisive test here (unlike yu pairing, where the
   quotation is a long, loose paraphrase).

The AI rates each proposed pair's strength as **`match_level`**:

- **high** — the quoted `「…」` matches this candidate's `rescript` (exact or
  near-exact) **and** the reply names its own earlier memorial (the one this
  rescript answered) in a way consistent with the candidate, and/or names a 硃批
  receipt date consistent with the candidate's `recvAr`. This is the normal,
  expected match — do not hedge it down.
- **partial** — the quoted rescript matches, but the reply gives no earlier-memorial
  reference and no legible receipt date to confirm **which** memorial's rescript
  it is (a risk when the same short rescript, e.g. `覽`/`知道了`, recurs).
- **weak** — no `「…」` quotation of a rescript (bare `奉到硃批` acknowledgement
  only), or the quoted text does not match this candidate's `rescript`, or the
  named receipt date points to a different document. A different named memorial or
  date is `weak` however plausible the pairing seems.

**No pair is ever auto-confirmed.** Every proposed pair is provisional — a
suggestion for review — regardless of `match_level`. A pair only becomes real
when the researcher clicks **加入配對 (add as pair)** on the card.

### Division of labour: Python (structural) + AI (textual)

- **Python** extracts, per official doc: the author; 硃批 citation markers and the
  `「…」` span that follows each; any Chinese date next to the marker; and builds
  candidate emperor-side documents by identity (same author) + date window +
  non-empty `rescript`, optionally boosted when the candidate's `rescript` text
  actually appears inside the reply's quoted span. Python strips the reply's own
  **trailing** `【硃批】…` rescript block before scanning, so a document is never
  matched to itself by its own rescript.
- **AI** does the textual judgement: whether the reply's `「…」` really quotes
  **this** candidate's `rescript` (short-string match), extracting the matched
  spans, resolving which earlier memorial the reply names, and classifying the
  named date as the 硃批 **receipt** date (`未明` when absent — never guessing).

## Website Prompt

You are pairing Qing official memorials with the `硃批` (imperial vermillion
rescript) each one is **acknowledging or quoting**. A `硃批` is the emperor's
short reply written on an official's own earlier memorial; that earlier memorial
is one of the candidate documents below (its `rescript` field holds the 硃批
text). You are given ONE later memorial (`【本回應】`) and a numbered list of
`【候選硃批文書】` — earlier documents by the same official, each carrying a
`rescript`. For each candidate, decide whether the memorial is quoting THAT
candidate's `硃批`.

A memorial replies to a `硃批` when it contains a citation marker
(`奉硃批`／`奉到硃批`／`敬奉硃批`／`欽奉硃批`／`蒙硃批`) introducing a `「…」`
quotation whose characters **match a candidate's `rescript`**. Rescripts are
short (often 2–6 characters, e.g. `准汝來`、`另有旨諭`、`知道了`、`覽`), so require a
close character match of the quoted span to the candidate's `rescript`, not a
loose paraphrase. Ignore the memorial's OWN trailing `【硃批】` block (that is the
emperor's reply to *this* memorial, not a quotation of an earlier one).

**Capture the leading date AND the full quoted 硃批.** `quote_in_reply` **must
begin at the date that identifies the original memorial** — the concrete date
printed *before* the memorial reference / citation marker (e.g. the `又上年十二月
初十日` in `又上年十二月初十日奴才奏報登舟渡臺一摺，奉硃批：「已有旨了。」`). That leading
date is the single most important piece of confirming evidence, because it is
what pins the quoted 硃批 to a specific earlier memorial (whose own send date it
should equal); dropping it makes the pairing unverifiable. Do **not** start the
quote at the memorial title (`奴才奏報登舟渡臺一摺…`) — always reach back to include
the date in front of it. From that date, continue through the memorial reference,
the marker, and the entire `「…」` quotation to its close (normally `欽此`; a reply
may quote two rescripts in one span — include both, as in the 台124 example).
Worked example (台124):

> 又上年十二月初十日奴才奏報登舟渡臺一摺，奉硃批：「已有旨了。」摺内帶領官兵登舟，句旁奉硃批：「仍以調養為要，勿過勞。」

Here the leading `上年十二月初十日` fixes which memorial the two rescripts sit on, so
it belongs in `quote_in_reply`. Put the matched rescript text itself (the
characters inside `「…」`, matching the candidate's `rescript`) in
`matched_zhu_span`.

**Use identity + the named memorial + the receipt date to rate.**
- If the `「…」` matches this candidate's `rescript` AND the reply names the
  earlier memorial (or a 硃批 receipt date) consistent with this candidate →
  `high`.
- If the `「…」` matches but nothing pins down which memorial → `partial`.
- If there is no `「…」` rescript quotation, or it does not match this candidate's
  `rescript`, or the named memorial/date points elsewhere → `weak`.

For dates, distinguish carefully and do not guess:
- `receive_date` = the date the official states he **received** the 硃批
  (introduced by `奉到硃批`／`敬奉硃批`／`奉硃批` and usually preceded by a date).
- Resolve relative references (`同日`／`是日`／`本日` = the most recently stated
  concrete date; `次日`／`翌日` = the following day). Prefer the full
  `乾隆..年..月..日` form. Mark `未明` only when genuinely absent.
- `own_memorial_ref` = the short phrase by which the reply names its **own earlier
  memorial** that this 硃批 answered (e.g. `奏請來京請訓一摺`,
  `挑備戰兵以資策應一摺`), or `未明` if none is given.
- `original_memorial_date` = the leading date printed in front of that memorial
  reference (e.g. `上年十二月初十日` / `乾隆五十一年十二月初十日`), which should equal
  the candidate 硃批 document's own send date. This is the confirming date — copy
  it verbatim; mark `未明` only when genuinely absent.

**Also record HOW the official received this 硃批**, in `evidence.receipt`. The
receipt clause is normally already part of `quote_in_reply` — do not repeat the
whole thing, just classify it:
- `type`: one of
  - `direct` — the emperor's 硃批 written on the official's **own** memorial, which
    he now quotes back (e.g. `臣…一摺，奉硃批：`). This is the usual case.
  - `court_letter` — relayed to him as a court letter (`廷寄`／`字寄`) by the
    Grand Councillors (e.g. `承准大學士公阿桂、和珅字寄`).
  - `handed` — another official physically handed or showed it to him
    (e.g. `督臣常青面交廷寄諭旨，付奴才閱看`).
  - `copy` — a transcribed / forwarded copy (`抄錄`／`傳鈔`／`轉行`).
- `via`: the intermediary's name or title if the rescript reached him through
  someone else (e.g. `阿桂`、`和珅`、`常青`); `未明` for a `direct` receipt.
- `quote`: the exact **receipt clause** from the reply (the phrase stating when
  and how he received it) — verbatim; this is the same clause that opens
  `quote_in_reply`.

Use Traditional Chinese, preserve quotations exactly, and return only this JSON:

```json
{
  "pairs": [
    {
      "zhu_doc_id": "",
      "match_level": "high|partial|weak",
      "evidence": {
        "marker": "",
        "quote_in_reply": "",
        "matched_zhu_span": "",
        "own_memorial_ref": "未明",
        "original_memorial_date": "未明",
        "receive_date": "未明",
        "receipt": { "type": "direct", "via": "未明", "quote": "" },
        "date_note": ""
      }
    }
  ]
}
```

For a **label-only** judgement (the runner appends a note when the reply
acknowledges a 硃批 without quoting it), set `matched_zhu_span` to `""`, add
`"quote_type": "label_only"` to `evidence`, still fill `own_memorial_ref` /
`original_memorial_date` / `receipt`, and cap `match_level` at `partial`.

Rules: rate `match_level` as high / partial / weak per the definitions above. Do
not invent quotations, dates, or pairs. Omit a candidate entirely only if the
memorial clearly does not quote its `硃批`.

## Output (pairs JSON, produced by the runner)

The runner merges the AI result with the structural facts into a flat,
many-to-many list. Each pair carries `relation: "official_reply_to_emperor_zhu"`. The emperor-side
document id is stored under **both** `zhu_doc_id` (semantic) and `yu_doc_id` (so
the website's existing pair-rendering machinery, which keys off `yu_doc_id`, draws
the connector line to the 硃批 dot without change):

```json
[
  {
    "reply_doc_id": "台46",
    "zhu_doc_id": "台??",
    "yu_doc_id": "台??",
    "relation": "official_reply_to_emperor_zhu",
    "match_level": "high",
    "evidence": {
      "marker": "奉到硃批",
      "quote_in_reply": "竊臣奏請來京請訓一摺，於十二月二十四日奉到硃批：「准汝來。」欽此",
      "matched_zhu_span": "准汝來。",
      "own_memorial_ref": "奏請來京請訓一摺",
      "original_memorial_date": "未明",
      "receive_date": "1786/12/24",
      "date_note": "reply names receipt 十二月二十四日 and its own earlier 請訓 memorial"
    }
  }
]
```

## Display (review cards)

Same review-card treatment as yu pairing (one pair, one card, `加入配對` button,
rendered in the AI chat panel with no single card selected). The card shows the
`硃批` side (the earlier memorial's id/date + the rescript text) → the reply (id,
author, sent date), the reply's quotation and matched rescript span, the named
earlier memorial and receipt date, and a `match_level` badge. The connector line
runs between the 硃批 dot of the earlier document and the reply document's dot.

## Deferred (later phases)

1. **Receipt-only replies** (state a 硃批 was received but do not quote it) — the
   structural net here (rescript-text match) cannot see them; they need the
   named-memorial + receipt-date signals alone.
2. Confirm button → write pairing into `stage1_original_text.json`.
3. Chart connector styling distinct from the 上諭 connector.
