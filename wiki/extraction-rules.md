# Extraction Rules

## Evidence

- Extract only what the source supports.
- Preserve original wording in evidence fields.
- Separate evidence from normalization and interpretation.
- Do not infer missing people, places, offices, dates, recipients, or relationships.
- Mark uncertain OCR, identity, category, or linkage explicitly.

## Entity handling

- Keep personal names and official titles in separate fields.
- Preserve historical place names; normalize only in a separate field with authority and date basis.
- Preserve Chinese dates. If a verified conversion is needed, keep both forms.
- Treat overlapping or ambiguous entities as uncertain rather than forcing one category.

## 林爽文 document fields

Preserve when available:

- `doc_id`, `series`, `doc_type`, `author`, `title`
- `send_date`, `receive_date`, `announce_date`, `issue_date`
- `body`, `rescript_text`
- event date and reported place
- communication direction
- action or issue category
- evidence quotation
- interpretive note
- uncertainty

## Output rules

- Follow the requested JSON or CSV schema exactly.
- Return raw structured data without Markdown fences when machine parsing is expected.
- Use empty arrays or null values according to the schema; do not substitute prose.
- Retain stable source identifiers so every row can be audited.

