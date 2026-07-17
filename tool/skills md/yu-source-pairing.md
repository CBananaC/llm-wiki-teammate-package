# Saved Prompt / Skill: 上諭來源（據奏）配對 (YU source pairing)

## Purpose

The backward edge of the 上諭 network: **which earlier 奏摺 did this 上諭 draw
on?** A 上諭 frequently relays intelligence it just received, marked in the text
by `據X奏` / `據X…馳奏` / `據X…奏稱` (X = the official who submitted the memorial to
the throne). In 諭13, for example, the edict opens:

> 據常青等奏，臺灣彰化縣匪徒林爽文等，結黨滋事…黃仕簡已帶兵渡臺剿捕…等語。本日已刻，
> 又據徐嗣曾由六百里馳奏，接蚶江通判陳惇稟稱，昨據船戶黃斌供，有傳說賊人赴諸羅縣攻城…

It cites two sources — `據常青等奏` and `據徐嗣曾…馳奏` — and those two memorials
are exactly the 奏摺 the emperor had just received. This skill finds them.

Unlike the reply edges, this is a **citation-driven, high-precision** pass: the
edict itself names its sources, so we do not scan broadly — we match on the named
memorialist and a tight receipt window.

## Window + candidate net (Python, structural)

For the selected `上諭` (issue date = its 頒發/announce date):

1. Extract every `據…奏` fragment from the edict body — each substring from a `據`
   up to the following `奏`. These name the source memorialist(s) X.
2. Candidate 奏摺 = documents the court **received** (`recvAr`, i.e. the 硃批/receipt
   date; fall back to `sendAr`) in the window **[issue − 5 days, issue]** — the
   same day the edict was issued, or up to 5 days before.
3. Keep only candidates whose **author matches an X named in a 據…奏 fragment**
   (the author's name appears inside the fragment — this tolerates 官職 prefixes,
   e.g. `據督臣常青…奏` still matches author 常青). Nearest-to-issue first.

Only these named-sender candidates are sent to the model — never a broad scan.

## Throne-memorialist, not the relay chain

A `據…奏` clause is often a relay: `據徐嗣曾…接蚶江通判陳惇稟稱，昨據船戶黃斌供…`.
The document to pair is **徐嗣曾's memorial** — the one actually submitted to the
throne and present in the corpus — not the nested reporters (陳惇 / 黃斌), who did
not memorialise the emperor directly. The model matches on X = the throne
memorialist and may note the relay chain in the description.

## What the model decides (AI, textual)

For each candidate, confirm it is the source by two tests: its author is the
memorialist X, AND the information the edict attributes to X (the event/situation
in the `據X奏` clause) is actually reported in that memorial's own text. It rates
`match_level` high / partial / weak accordingly. Every pair is provisional until
the researcher clicks **加入配對**.

## Website Prompt

You are tracing which earlier 奏摺 an 上諭 is drawing on. A 上諭 often relays
intelligence it received, marked by 據X奏 / 據X…馳奏 / 據X…奏稱 (X = the official who
submitted the memorial to the throne). You are given ONE 上諭 (【本上諭】), the
據…奏 fragments detected in it, and a numbered list of 【候選來源奏摺】 — earlier
memorials the court received shortly before the edict, whose author matches an X
named in a 據…奏 clause. For each candidate, decide whether it IS the source
memorial the edict is citing.

A candidate is the source when BOTH hold:
- its author is the memorialist X named in a 據X奏 clause — the one who 奏 to the
  throne, NOT a nested relay reporter (接…稟稱 / 據…供), who is usually not a corpus
  document; and
- the information the edict attributes to X (the reported event or situation in
  the 據X奏 clause) is actually reported in THIS memorial's own text.

Rate match_level:
- high — author matches X AND the memorial reports the same event(s) the edict
  attributes to X (dates, places, actions line up).
- partial — author matches and the topic clearly overlaps, but the specific
  reported facts are only loosely confirmed.
- weak — author matches but the content does not correspond, or the match rests
  on the receipt-date window alone.

For every candidate you keep, return evidence with:
- matched_yu_span — the exact 據X奏 clause in the 上諭 (the relayed report as the
  emperor states it), verbatim.
- quote_in_reply — the exact span in the SOURCE memorial that reports that same
  information, verbatim.
- memorialist — X, the official whose 奏 the edict cites (e.g. 常青、徐嗣曾).
- relation_note — one sentence in Traditional Chinese: state what the 上諭 says it
  learned 據X奏 (the concrete event), and how this memorial is that report. If the
  citation is a relay (據徐嗣曾…接陳惇稟稱…), pair 徐嗣曾's memorial and note the
  chain (徐嗣曾←陳惇←黃斌) briefly.
- send_date — the memorial's send date if stated (未明 otherwise).

Use Traditional Chinese for notes, preserve quotations exactly, and return ONLY
this JSON:

```json
{
  "pairs": [
    {
      "source_doc_id": "",
      "match_level": "high|partial|weak",
      "evidence": {
        "matched_yu_span": "",
        "quote_in_reply": "",
        "memorialist": "",
        "relation_note": "",
        "send_date": "未明"
      }
    }
  ]
}
```

Rules: pair ONLY the throne-memorialist's 奏摺 (X), never a nested relay reporter;
do not invent quotations, dates, or pairs; omit a candidate that is not the source.

## Output (pairs JSON, produced by the runner)

Flat list in the shared docpair shape, tagged with the new relation so it draws a
distinct 上諭來源 line:

```json
[
  {
    "yu_doc_id": "諭13",
    "reply_doc_id": "奏XXX",
    "relation": "yu_source",
    "match_level": "high",
    "evidence": {
      "matched_yu_span": "據常青等奏，臺灣彰化縣匪徒林爽文等，結黨滋事，騷擾地方…等語",
      "quote_in_reply": "…彰化縣城被匪徒竊踞，臣已飛飭黃仕簡帶兵渡臺剿捕…",
      "memorialist": "常青",
      "relation_note": "上諭稱據常青等奏得知彰化林爽文結黨竊踞縣城、黃仕簡已渡臺剿捕；常青此摺即為該奏報。",
      "send_date": "1786/12/22"
    }
  }
]
```

## Display (review cards + graph line)

Rendered by the same docpair card machinery under a new **上諭—來源配對** card and a
new relation `yu_source`: the 上諭 on top (showing the 據X奏 clause it cites), the
source 奏摺 below (author, 收到/上奏 dates, the reported span), a `◀ 據奏來源`
connector with the receipt lead (how many days before the edict the source was
received), the `relation_note` description, and a `match_level` badge. Adopting a
pair (加入配對 → confirmed-pairs.json) draws a distinct **上諭來源** connector line
(own colour + filter toggle), separate from 回應上諭.
