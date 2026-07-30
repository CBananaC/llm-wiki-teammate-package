# Clear demonstration data: 硃40—諭24

This folder contains a small demonstration set for the review timeline. It is
derived from the current sample state and does not modify the formal tool, the
sample tool, or the canonical Stage 1 source file.

## Contents

- `clear-demo.data` — one importable JSON review-state export containing the
  timeline overlay, source documents, and response-pair metadata.
- `build_clear_demo.py` — reproducible builder that refreshes the single export
  file from the current sample state.

The export keeps:

- 10 event dots sourced from 硃40, with one matching AI output card for each.
- 13 emperor-action dots sourced from 諭24, with the retained 諭24 AI action
  output cards and each action's structured `emperorDetail`.
- All existing event and emperor-action dots remain in `__events`, including the
  other documents' dots.
- All existing document dots remain visible. `__clearDemo.document_dots` records
  that only 硃40 and 諭24 are intended to be clickable later; other document dots
  remain visible but are marked non-clickable for future interaction code.
- `__clearDemo.event_dots.selected_data` separates the 硃40 event IDs and 諭24
  emperor-action IDs, while the selected document data remains under the matching
  top-level `硃40` and `諭24` keys.
- A single explicit document-pair link from 硃40 to 諭24, representing 諭24 as
  a response to 硃40 for demonstration purposes.
- The full source records for 硃40 and 諭24 under `__sourceDocuments` in the
  same JSON file.

The link is intentionally marked as demonstration-only. It should not be
copied into the formal confirmed-pair data without separate source review.
