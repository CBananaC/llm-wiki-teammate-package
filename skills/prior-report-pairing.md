# Saved Prompt / Skill: 在案—前奏配對 (prior-report pairing)

## Purpose

Identify a later official memorial that says an earlier report was already
submitted (`在案`) and pair it with that earlier memorial. The later text may
give (a) the earlier memorial's send date, (b) a short summary of what was
reported, or (c) both. Every result is provisional until the researcher clicks
**加入配對** in the AI chat panel.

The canonical example is `台171 → 台147`. In `台171`, 常青 writes that Guangdong
and Zhejiang troops were sent back while 2,000 Chaozhou troops were temporarily
retained, `於正月二十八日附摺奏明在案`. `台147`, sent on 正月二十八日 by 常青,
contains that earlier report in full.

## Structural candidate rules

The runner and website first find a report-reference passage ending in `在案`,
such as `前經奏明在案`, `另摺奏報在案`, or `於…附摺奏明在案`. Candidates must:

1. be an earlier official document (not an `上諭`);
2. normally share an author with the later document;
3. fall within the configured date window;
4. rank first when their Chinese send date matches the date cited before `在案`;
5. otherwise rank by overlap between the brief report in the later passage and
   the candidate's title/original text.

Every exact cited-date candidate is retained. Only low-signal fallback
candidates are capped, so a dated reference cannot disappear because of a
fixed candidate limit.

Run `python3 scripts/run_prior_report_pairing.py --all --structural-only` to
produce conservative review cards immediately from date/text evidence, or pass
`--proxy URL --all` for AI adjudication. Structural-only results remain
provisional and use `partial` unless date plus distinctive content justify
`high`; neither mode confirms a connector automatically.

## Match levels

- `high`: cited date matches and the report topic agrees, or a distinctive
  multi-clause summary strongly matches the earlier original text.
- `partial`: date matches but the summary is too generic, or a meaningful
  summary matches without a usable date.
- `weak`: only generic `在案` wording matches, the date conflicts, or the
  candidate concerns a different matter.

## Website Prompt

You are pairing Qing official memorials that refer back to information the same
official had already reported in an earlier memorial. You are given ONE later
memorial (`【本次奏報】`), one or more passages ending in `在案`, and numbered
`【候選前奏】` documents.

Decide which earlier candidate the later memorial is referring to. `在案` by
itself is not enough. Use both kinds of evidence when available:

1. **Cited send date.** A phrase such as `於正月二十八日附摺奏明在案` names the
   earlier memorial's own send date. Compare it with each candidate's `上奏日`.
   Treat 正月／一月／元月 as equivalent. A conflicting date makes the candidate
   `weak` even if the broad topic is similar.
2. **Previously reported information.** Compare the concrete facts immediately
   before `在案` with the candidate's title and original text. Named people,
   places, troop numbers, actions, and outcomes are especially useful. A close
   paraphrase counts; verbatim copying is not required.

The earlier and later records are both official memorials. This is not an
`上諭` response and not a `硃批` response.

Use Traditional Chinese, preserve quoted source text exactly, and return only:

```json
{
  "pairs": [
    {
      "previous_doc_id": "",
      "match_level": "high|partial|weak",
      "evidence": {
        "marker": "在案",
        "reference_in_later_doc": "",
        "previous_report_date": "未明",
        "previous_report_summary": "",
        "matched_previous_span": "",
        "matched_later_span": "",
        "date_note": ""
      }
    }
  ]
}
```

`reference_in_later_doc` and `matched_later_span` should contain the complete
later passage: begin far enough before `在案` to include the brief facts being
recalled, and continue through `在案`. `matched_previous_span` must be an exact
quotation from the selected earlier document that supports the match.
`previous_report_date` is the earlier memorial date stated in the later passage,
or `未明` when absent. Do not invent dates, quotations, or pairs.

## Output

The runner emits `relation: "prior_report"`. For compatibility with the shared
pair-card and connector machinery, the earlier id is stored in both
`previous_doc_id` and `yu_doc_id`; the later id is stored as `reply_doc_id`.
Confirmed `prior_report` connectors run from the earlier official send dot to
the later official send dot on the second timeline lane.
