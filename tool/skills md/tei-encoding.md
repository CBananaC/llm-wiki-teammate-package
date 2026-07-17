# Skill: TEI Encoding

## Purpose

Use this skill to turn checked source text into structured TEI XML that preserves original wording and makes textual features auditable.

## When To Use

Use this skill when the task asks for:

- Encoding a source text, abstract, passage, or excerpt as TEI XML.
- Marking titles, paragraphs, divisions, people, places, dates, roles, or terms.
- Creating a reusable text representation for later NLP, GIS, or network workflows.
- Linking names to external identifiers after they have been verified.

## Rules

- Preserve the source wording.
- Do not silently modernize, translate, or normalize Chinese text.
- Keep unverified bibliographic metadata marked as unverified.
- Use valid XML and close every element.
- Prefer common TEI elements before inventing custom markup.
- Do not add external identifiers unless the match has been checked.
- Record encoding decisions and limitations in a note.

## Recommended Elements

- `<TEI>` for the root document.
- `<teiHeader>` for metadata and source description.
- `<titleStmt>` for title and author.
- `<sourceDesc>` for source and citation notes.
- `<text>`, `<body>`, `<div>`, `<head>`, and `<p>` for structure.
- `<persName>` for personal names.
- `<placeName>` for places.
- `<date>` for dates or time expressions.
- `<roleName>` for official titles or social roles.
- `<term>` for concepts and keywords.
- `<ref>` or `@ref` for verified external identifiers.

## Workflow

1. Start from checked OCR or transcription, not raw OCR if avoidable.
2. Confirm source metadata in [[source-materials]].
3. Create a minimal TEI header with known and unknown metadata clearly separated.
4. Encode document structure first.
5. Add entity markup only where supported by the source text.
6. Add verified external identifiers if available.
7. Validate XML with `xmllint --noout`.
8. Save the TEI in `outputs/source-id/`.
9. Record method and limitations in processing notes.

## Recommended Outputs

- `source-id.tei.xml`: valid TEI XML.
- Processing-note entry documenting what was encoded and what remains uncertain.
- Optional derived outputs, such as TEI-derived NLP tags or linked-data tables.

## Common Errors

- Creating XML that is not well-formed.
- Inventing TEI-like tags instead of using real TEI elements.
- Encoding OCR errors as if they were checked text.
- Treating inferred metadata as verified citation data.
- Adding CBDB or CHGIS IDs without explaining the match.

## Related Wiki Pages

- [[source-materials]]
- [[extraction-rules]]
- [[workflows]]
- [[known-errors]]
