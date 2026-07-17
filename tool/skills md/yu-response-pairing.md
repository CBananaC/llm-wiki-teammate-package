# Saved Prompt / Skill: 上諭—回應配對 (YU response pairing)

## Purpose

Identify which official document (奏摺／硃批-bearing memorial) is **responding to
which `上諭`**, across the whole corpus, and output the pairs with quotation
evidence for the researcher to review and (later) confirm.

Scope of this first version: **`上諭` only.** Pairing replies to a `硃批` is a
later phase. Confirm-to-write-back and the chart connector line are also later
phases; this version produces detection + review cards only.

The worked example this skill is built around: **天43 (`上諭` to 孫士毅,
issued 乾隆52正月十三日 / 1787-01-13)** is answered by **台160 (孫士毅's memorial,
sent 1787-01-26)**, which inside its text says:

> 同日，接奉廷寄乾隆五十二年**正月十三日奉上諭**：「據孫士毅奏，接准閩省咨文，
> 挑備水師戰兵一千名…著孫士毅如尚未起程，即毋庸前往。若已起程，亦即速回省城。」
> …欽此。

Note three things this example proves and the method relies on: (a) the reply
carries a citation marker (`接奉廷寄…奉上諭`); (b) the quoted text is a **loose**
rewrite of 天43, not an exact copy (諮→咨, phrases dropped); (c) the reply names
the edict's **own date** (`正月十三日`), and separately its **receipt** date
(`本年正月二十四日…同日接奉`, i.e. received 01-24, eleven days after issue).

## How a pair is determined

Three signals feed the judgement:

1. **Identity** — the reply's author is one of the `上諭`'s recipients.
2. **Date** — the reply is sent after the `上諭` was issued, within a plausible
   transit+turnaround window. Officials far from Beijing typically need ~10–14
   days to even receive an edict; the two 大學士 in Beijing (和珅, 阿桂) far less.
3. **Citation** — the reply cites the edict: a marker (`奉上諭`／`奉廷寄`／
   `欽奉諭旨`) followed by a **loosely matching** quotation of the edict's wording.

The AI rates each proposed pair's strength as **`match_level`**. The cited date
disambiguates edicts in a series that otherwise read almost identically:

- **high** — the reply names **this edict's date** (the date it prints before
  `奉上諭`) and reproduces matching wording. When both hold, you **must** rate
  `high` — this is the normal, expected match, not a rare one.
- **partial** — the quoted wording clearly matches this edict, but no legible
  date is given to confirm it (the reply doesn't state which edict-date it
  quotes).
- **weak** — the reply names a **different** edict date (even one day off → a
  different edict in the series), or there is no real citation. A different cited
  date is `weak` however similar the subject matter.

**No pair is ever auto-confirmed.** Every proposed pair is provisional — a
suggestion for review — regardless of `match_level`. A pair only becomes real
when the researcher clicks **加入配對 (add as pair)** on the card, which is the
write-back step (a later phase). `match_level` just orders and colours the
review; it does not assert anything.

### Division of labour: Python (structural) + AI (textual)

- **Python** extracts, per official doc: the author; citation markers and any
  raw Chinese date strings sitting next to them; and builds candidate `上諭`s by
  identity + date window. Python does **not** decide whether a cited date is the
  edict's issue date or the official's receipt date — that distinction is
  genuinely ambiguous in the text and is left to the AI.
- **AI** does the textual judgement: whether the reply's quotation actually
  matches *this* edict (loose match allowed), extracting the matched spans, and
  classifying each cited date as **issue** vs **receive** (marking both when both
  are stated, `未明` when absent — never guessing).

### Transit estimation (soft validator only)

For each official, average the send→硃批 lag of their own memorials (the time
between `sendAr` and `recvAr`) as an estimate of how long an imperial document
takes to reach them. Use it only to sanity-check the date window; when the reply
**states** its receipt date, that stated date is authoritative. Every extracted
(issue-date, receive-date) pair also feeds back as new transit evidence.

## Website Prompt

You are pairing Qing official memorials with the `上諭` each one is answering.
You are given ONE `上諭` and a numbered list of `【候選回應】` later memorials by
its recipient(s). For each candidate, decide whether it is genuinely responding
to THIS `上諭`.

A memorial responds to this `上諭` when it contains a citation marker
(`奉上諭`／`奉聖諭`／`聖諭`／`奉廷寄`／`欽奉諭旨`／`諭旨`／`欽奉上諭`) introducing a quotation whose wording
**loosely** matches this edict — a rewrite, abridgement, or paraphrase counts;
an exact copy is not required. Do not require verbatim text.

Some catalogue rows have an empty or placeholder `上諭` body (for example,
`正文見第一部分。`). In that case, use the row's title, cited date context,
and named officials as a provisional fallback: return `partial` only when the
title clearly identifies the quoted subject, and do not treat a generic
same-topic title as proof.

**Capture the receipt lead-in AND the full quoted 上諭 (its 範圍).**
`quote_in_reply` should begin at the official's **receipt clause** — the phrase
stating when and how he received the edict (e.g.
`三月初十日，督臣常青面交廷寄諭旨，付奴才閱看。乾隆五十二年二月十一日奉上諭：`) —
and continue through the **entire** quoted edict to its close. So a full
`quote_in_reply` looks like:
`三月初十日，督臣常青面交廷寄諭旨，付奴才閱看。乾隆五十二年二月十一日奉上諭：「本日據黃仕簡奏…令其回奏。」欽此`.
Put the edict's own corresponding text (without the reply's lead-in) in
`matched_yu_span`. The quote's close is normally `欽此`; when there is no `欽此`,
decide the boundary by reading — the quotation ends where the emperor's reported
words stop and the official's own narration resumes. Do not cut it at an
internal `等語`/`等因` that sits inside the emperor's words.

**Use the cited date to rate — but only an ISSUE date.** `issue_date` is the
edict's own date, printed **directly before `奉上諭`/`奉聖諭`** (the date the
edict was issued). A date printed before `奉到`/`接奉`/`敬奉`/`准` is a **receipt**
date, not an issue date — do NOT treat it as `issue_date`. Compare only a true
issue date to this `上諭`'s date, shown in the `【本上諭】` block:
- **issue date matches → `high`** (with a matching quotation). The standard
  successful pairing; do not hedge it down.
- **issue date differs, even by one day → `weak`** — a different edict in the
  same series; do not upgrade on content similarity alone.
- **only a receipt date is given (`X日奉到諭旨：「…」`), no issue date → rate by
  the QUOTED CONTENT**: if the quotation matches this `上諭`, rate `high` (or
  `partial` if the overlap is looser). Do **not** rate it `weak` just because the
  receipt date differs from this edict's issue date. This is the normal shape of
  a batch acknowledgment (`節次奉到諭旨`), which cites many edicts by the date
  they were **received**; match each quotation to its edict by content.
- **no legible date at all → `partial`** if the quoted wording still matches.

For dates, distinguish carefully and do not guess:
- `issue_date` = the edict's own date as named in the reply (e.g. the date
  directly before `奉上諭`), which should equal this `上諭`'s date.
- `receive_date` = the date the official states he **received** the edict
  (introduced by `接奉`／`接准`／`敬奉`／`准`…). Some replies give one, some the
  other, some both.
- **Resolve relative date references** — do not leave them as `未明`. `同日`／
  `是日`／`本日` mean the same day as the most recently stated concrete date;
  `次日`／`翌日` mean the following day. For example
  `正月二十四日敬奉硃批：「…」。同日，接奉廷寄…奉上諭：「…」` means the edict was
  **received on 正月二十四日** — return that concrete date as `receive_date`,
  not `未明`.
- Prefer the full `乾隆..年..月..日` form. Mark a date `未明` only when it is
  genuinely absent, never when it is expressed relatively.

**Also record HOW the official received this 上諭**, in `evidence.receipt`. The
receipt clause is normally already part of `quote_in_reply` — just classify it:
- `type`: one of
  - `direct` — the edict was addressed to and received by this official himself
    (`奉上諭`／`欽奉諭旨` with no relaying party named).
  - `court_letter` — relayed as a court letter (`廷寄`／`字寄`) by the Grand
    Councillors (e.g. `接奉廷寄…奉上諭`, `承准大學士公阿桂、和珅字寄`).
  - `handed` — another official physically handed or showed it to him
    (e.g. `督臣常青面交廷寄諭旨，付奴才閱看`).
  - `copy` — a transcribed / forwarded copy (`抄錄`／`傳鈔`／`轉行`).
- `via`: the intermediary's name or title if it reached him through someone else
  (e.g. `阿桂`、`和珅`、`常青`); `未明` for a `direct` receipt.
- `quote`: the exact **receipt clause** from the reply (verbatim); the same clause
  that opens `quote_in_reply`.

Use Traditional Chinese, preserve quotations exactly, and return only this JSON:

```json
{
  "pairs": [
    {
      "reply_doc_id": "",
      "match_level": "high|partial|weak",
      "evidence": {
        "marker": "",
        "quote_in_reply": "",
        "matched_yu_span": "",
        "issue_date": "未明",
        "receive_date": "未明",
        "receipt": { "type": "direct", "via": "未明", "quote": "" },
        "date_note": ""
      }
    }
  ]
}
```

Rules: rate `match_level` as high / partial / weak per the definitions above. Do
not invent quotations, dates, or pairs. Omit a candidate entirely only if it
clearly has nothing to do with this edict.

## Output (pairs JSON, produced by the runner)

The runner merges the AI result with the structural facts into a flat,
many-to-many list (one reply may pair with more than one edict, and vice versa):

```json
[
  {
    "reply_doc_id": "台160",
    "yu_doc_id": "天43",
    "relation": "official_reply_to_yu",
    "match_level": "high",
    "evidence": {
      "marker": "接奉廷寄…奉上諭",
      "quote_in_reply": "…著孫士毅如尚未起程，即毋庸前往…",
      "matched_yu_span": "…著傳諭孫士毅，此時如尚未起程，即毋庸前往…",
      "match_level": "high",
      "issue_date": "1787/01/13",
      "receive_date": "1787/01/24",
      "date_note": "reply names the edict date 正月十三日 and states receipt 正月二十四日"
    }
  }
]
```

## Display (review cards)

- **One pair, one card**, styled to match the existing review cards (same
  `chat-extract` / `cx-sub` / `cx-q` / `em-srcinfo` vocabulary).
- Each card shows: the `上諭` (id, date) → the reply (id, author, sent date), the
  reply's quotation and the matched edict span, the issue vs receive dates, and a
  **`match_level` badge** (high / partial / weak) to order and colour the review.
- Every card carries an **加入配對 (add as pair)** button. Nothing is a real pair
  until it is clicked; the badge asserts nothing on its own.
- Because a pair belongs to two documents rather than one, the cards render in
  the AI chat panel **with no single card selected** (the shared group store), so
  the researcher can review the whole set at once.
- The **加入配對** write-back to `stage1_original_text.json` and the chart
  connector line are **deferred** to a later phase, after the pairs look right.

## Deferred (later phases)

1. Pairing replies to a `硃批` (structural: the 硃批 sits on the official's own
   earlier memorial; its cited text is often too short to match by wording).
2. Confirm button → write pairing into `stage1_original_text.json`.
3. Chart connector line between the two document dots.
