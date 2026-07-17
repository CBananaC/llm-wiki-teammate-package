# Saved Prompt / Skill: 相關上諭配對（無引文）(YU response pairing — no-citation recall)

## Purpose

The citation-based pairing (`tool/skills md/yu-response-pairing.md`, action **相關上諭配對**)
is high **precision**: it only surfaces a later memorial when that memorial
carries a citation marker (`奉上諭`／`奉廷寄`／`欽奉諭旨`…) and quotes the edict, and
when its author is one of the edict's named recipients. That rule misses a real
class of replies:

- **no citation** — the memorial acts on or answers the edict without ever
  quoting it or naming `奉上諭`;
- **a different sender** — an official the edict did not name directly, but who
  is drawn into the same operation, reports on it;
- **a longer, realistic lag** — the reply arrives well after the edict, once it
  has physically travelled to the field.

This skill is the **recall** pass that recovers those cases. It does **not** look
for citation markers at all. Instead it takes one `上諭`, gathers later documents
in a plausible reply window, ranks them by **shared subject matter** (the same
reported event, operation, officials, and places), and asks the model to judge
relatedness from content alone. Every result is provisional and shown as a review
card for the researcher to adopt — exactly like `相關上諭配對`.

## Window (structural pre-filter)

A genuine reply cannot arrive until the edict has reached the official, so the
first stretch after issue is pure transit and is skipped. The recall window is:

- **skip the first 10 days** after the `上諭` issue date (transit period — no
  reply can have arrived yet), then
- **search the following 20 days** — i.e. candidate send dates in
  **[issue + 10 days, issue + 30 days]**.

Nothing inside the first 10 days and nothing past day 30 is considered by this
pass. (The tight, exact citation cases outside this window are already covered by
`相關上諭配對`; this pass only adds the content-matched recall inside it.)

## How a candidate is ranked (Python, structural)

Within the window, and across **all** officials (the recipient/identity filter is
deliberately dropped), each later document is scored by character-bigram overlap
between the edict (title + body) and the candidate (title + body). This is a
cheap topic-overlap proxy that stands in for "shares the same 人名／地名／事件".
Only the top-K highest-overlap candidates are sent to the model, so the model
never reads the whole corpus — it reads a short, ranked shortlist.

The overlap score is a **ranking signal only**. It decides which candidates the
model looks at; it never asserts a relationship on its own.

## Two axes (AI, textual)

Because dropping the citation and sender filters lets in documents that merely
report the **same** affair without responding to the edict, the model rates each
candidate on **two independent axes**, and the card shows both:

1. **`match_level`** — how strongly the memorial's *content* relates to this
   edict's matter (`high` / `partial` / `weak`).
2. **`reply_status`** — whether it actually *answers or carries out* the edict
   (`done`), is clearly related and consistent but not yet a completed answer
   (`ack`), or, despite subject overlap, is an **independent report** rather than
   a response (`unrelated`).

The key judgement this pass exists to make: a memorial can be `match_level: high`
on subject overlap yet `reply_status: unrelated` — it reports the same battlefield
event but was not written in response to the imperial command. Surfacing those
for a human glance (rather than silently dropping or silently pairing them) is the
whole point.

**No pair is ever auto-confirmed.** A pair becomes real only when the researcher
clicks **加入配對 (add as pair)** on the card. `match_level` / `reply_status` only
order and colour the review.

## Website Prompt

You are finding Qing official memorials (奏摺／硃批-bearing) that RESPOND TO or
CARRY OUT a given `上諭`, WITHOUT relying on any citation marker. Unlike the
citation-based pairing, these candidates do NOT quote the edict and may be written
by an official who is NOT the edict's named recipient. You are given ONE `上諭`
(`【本上諭】`) and a numbered list of `【候選回應】` later memorials, already
pre-filtered to a plausible reply window and ranked by shared subject matter
(people, places, events).

**FIRST read the `上諭` in two layers, because you will pair only against the
second layer.** An edict normally mixes:
- **(A) relayed intelligence** — passages where the emperor is REPEATING what an
  official already reported to him (`據某奏`／`據某稟報`／`某奏稱…等語`／
  `具奏前來`…). These are battlefield events the emperor learned FROM a memorial;
  they are NOT the emperor's own instruction.
- **(B) the emperor's own response** — his judgement, comment, praise/blame,
  reward, and above all his COMMAND (`著…`／`諭令…`／`飭…`／`嘉獎`／`申飭`…).

A genuine reply answers or carries out **layer (B)**. A later memorial that merely
reports the SAME event described in **layer (A)** is NOT a reply — the emperor was
already relaying that event from someone else's report, so this memorial is a
parallel or source report of the same intelligence, not an answer to the edict.
Mark such a candidate `reply_status: unrelated` (it will be dropped) unless it
also acts on the emperor's command in (B). Do the pairing against (B), never (A).

For each candidate decide TWO separate things.

`match_level` — how strongly the memorial's CONTENT is related to this edict's
matter (the same reported event, the same operation, the same named
officials/places):
- `high` — the memorial clearly concerns the very matter this edict commands or
  discusses, and reads as acting on or answering it.
- `partial` — related to the same affair, but the connection is looser or the
  memorial only touches part of it.
- `weak` — only incidental overlap (a shared place name or generic phrase) with
  no real connection.

`reply_status` — whether the memorial actually answers or executes the edict, as
opposed to merely being about the same affair:
- `done` — the memorial carries out, reports compliance with, or directly answers
  the edict's command.
- `ack` — clearly related and consistent with the edict, but it does not yet
  complete or explicitly answer it (e.g. an interim report on the same operation).
- `unrelated` — despite surface overlap, it is an independent report, not a
  response. This INCLUDES a memorial that reports the same event the edict was
  itself relaying in layer (A): reporting the same battlefield fact the emperor
  already had is not answering his command.

Judge by CONTENT, not by any citation. A memorial that independently reports the
same battlefield event WITHOUT responding to the imperial command in layer (B) is
`reply_status: unrelated` even when `match_level` is `high` on subject overlap —
say so plainly; do not force it into a reply.

For every candidate you keep, provide:
- `quote_in_reply` — the exact span FROM THE MEMORIAL that shows the relation, in
  **the official's OWN words**: his report of what he did, his compliance, or his
  answer. It must NOT be a re-quotation of imperial words embedded in the
  memorial. Memorials often quote the very edict or a 硃批 before responding
  (`奉上諭：「…著…勿過勞」欽此`); NEVER put such an imperial span — anything that is
  the emperor speaking (`著…`／`諭…`／praise, reward, or command language issued BY
  the emperor, `欽此`) — in `quote_in_reply`. Skip past the quoted edict to the
  official's own responding text. If the ONLY text overlapping this edict that you
  can find in the memorial is itself an imperial quotation, the memorial is not
  replying with its own content → `reply_status: unrelated`.
- `matched_yu_span` — the span of THIS edict that the memorial answers. It MUST be
  taken from **layer (B)** — the emperor's comment or command — NOT from the
  relayed-report layer (A). Preserve it verbatim.
- `relation_note` — in Traditional Chinese, explain the relation by PAIRING
  SPECIFICS, not by summarising generically. First name the particular
  instruction(s) or piece(s) of information IN THIS `上諭` that the memorial
  addresses — state the concrete point, quoting or closely paraphrasing it (e.g.
  `諭命任承恩渡臺事竣後速回`、`諭命常青駐蚶江廈門調度策應`、
  `諭命查參黃仕簡傳牌攻城之失`) — and THEN state how the memorial responds to that
  point (遵行／回報進度／請俟查明另奏／申辯／請旨…). Pair each edict point with its
  matching response; when the memorial answers several points, cover each one.
  Do NOT write a vague catch-all such as `逐一回覆上諭之指示` — always tie the
  response to the specific edict content it answers.
- `send_date` — the memorial's send date if stated (`未明` otherwise).

Use Traditional Chinese for notes, preserve quotations exactly, and return ONLY
this JSON:

```json
{
  "pairs": [
    {
      "reply_doc_id": "",
      "match_level": "high|partial|weak",
      "reply_status": "done|ack|unrelated",
      "evidence": {
        "quote_in_reply": "",
        "matched_yu_span": "",
        "relation_note": "",
        "send_date": "未明"
      }
    }
  ]
}
```

Rules: do NOT require or invent a citation marker; do NOT invent quotations,
dates, or pairs. Omit a candidate entirely only if it has nothing to do with this
edict. Keep a candidate you judge `unrelated` only when its subject overlap is
high enough to be worth the researcher's glance; otherwise omit it.

## Output (pairs JSON, produced by the runner)

The runner merges the AI result with the structural facts into the same flat,
many-to-many pair list used by `相關上諭配對`, tagged so the site can show the
no-citation provenance and the two axes:

```json
[
  {
    "reply_doc_id": "台160",
    "yu_doc_id": "天43",
    "relation": "official_reply_to_yu",
    "no_citation": true,
    "match_level": "high",
    "reply_status": "done",
    "evidence": {
      "quote_in_reply": "…遵即撥兵二千名分駐交界策應…",
      "matched_yu_span": "…著傳諭孫士毅於附近水師營內酌撥戰兵二三千名…",
      "relation_note": "上諭命於交界備撥水師策應，本摺回報已遵撥兵二千名分駐，屬對該諭令的執行。",
      "send_date": "1787/01/26"
    }
  }
]
```

## Display (review cards)

Rendered by the same **上諭—回應配對** card machinery (`docpair` /
`relation: official_reply_to_yu`), with two additions:

- a **無引文** tag, so the researcher knows this pair rests on content, not a cited
  quotation;
- the **`reply_status`** flag shown alongside `match_level`, so a `高度符合 ✓ /
  完成回覆 ×` case (highly related but not a completed reply) is visible at a
  glance.

The card leads with the `relation_note` description and the two quoted spans
(`quote_in_reply` → `matched_yu_span`), then the dates and the two badges. Every
card carries **加入配對**; nothing is a real pair until it is clicked.

De-duplication: this pass shares the pair store with `相關上諭配對`, so a pair the
citation pass already found is not added a second time (same `reply_doc_id` +
`yu_doc_id` + `relation`).
