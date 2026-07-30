# Clear demonstration data: 硃40—諭24

This folder contains a small demonstration set for the review timeline. It is
derived from the current sample state and does not modify the formal tool, the
sample tool, or the canonical Stage 1 source file.

## Contents

- `clear-demo.data` — importable review-state overlay.
- `source-documents.json` — only the two source documents used here: 硃40 and
  諭24.
- `confirmed-pairs.json` — the requested 諭24 → 硃40 response connection,
  labelled `demonstration` rather than confirmed research evidence.
- `build_clear_demo.py` — reproducible builder that refreshes the three data
  files from the current sample state.

The overlay keeps:

- 10 event dots sourced from 硃40, with one matching AI output card for each.
- 13 emperor-action dots sourced from 諭24, with the retained 諭24 AI action
  output cards and each action's structured `emperorDetail`.
- Only the 硃40 and 諭24 document dots; unrelated base document dots are hidden
  in the overlay.
- A single explicit document-pair link from 硃40 to 諭24, representing 諭24 as
  a response to 硃40 for demonstration purposes.

The link is intentionally marked as demonstration-only. It should not be
copied into the formal confirmed-pair data without separate source review.
