# Skill: LibraryCloud Search

## Purpose

Use this skill to search Harvard LibraryCloud or a similar catalog API for bibliographic records relevant to Sinitic, Chinese historical, and humanities research.

## When To Use

Use this skill when the task asks for:

- Finding catalog records.
- Checking whether a source title exists.
- Finding bibliographic metadata.
- Identifying possible editions.
- Enriching [[source-materials]].
- Recording provisional citation details.

## Required Inputs

- Search title or keyword.
- Author, editor, or creator if known.
- Language or script if relevant.
- Publication date or date range if known.
- API documentation or endpoint.
- Desired output fields.

## Workflow

1. Read the catalog API documentation.
2. Build a simple query first.
3. Search by exact title or distinctive keyword.
4. If there are many results, add author, language, date, or format filters.
5. Inspect multiple candidate records.
6. Compare title, creator, date, language, identifier, and format.
7. Record confirmed, possible, and rejected matches separately.
8. Add confirmed metadata to [[source-materials]].
9. Save raw API output in `outputs/` if the match is important or uncertain.
10. Record query used and date accessed.

## Matching Rules

- A title match alone is not always enough.
- Prefer records that match title, author, date, language, and format.
- If metadata is incomplete, mark uncertainty.
- Do not invent edition details.
- Do not invent page numbers.
- Do not cite a catalog record as evidence for textual content unless the record actually provides the content.

## Recommended Output Fields

- `source_id`
- `query`
- `title`
- `creator`
- `publication_date`
- `publisher`
- `language`
- `format`
- `identifier`
- `catalog_url`
- `match_status`
- `access_date`
- `notes`

## Example Source-Material Entry

```markdown
### Source: [source-id] — [title]

**Source type:**  
Catalog metadata / possible bibliographic record

**Title:**  
[Catalog title]

**Creator / author:**  
[Catalog value, or "Not provided"]

**Publication date:**  
[Catalog value, or "Not provided"]

**Publisher:**  
[Catalog value, or "Not provided"]

**Identifier:**  
[Catalog identifier]

**Catalog URL:**  
[Record URL]

**Query used:**  
`[query string]`

**Date accessed:**  
YYYY-MM-DD

**Match status:**  
Possible or confirmed match based on title, creator, date, language, and format.

**Notes:**  
Catalog metadata only; this record is not evidence for the source's textual content.
```

## Common Errors

- Assuming the first search result is correct.
- Treating catalog metadata as full text.
- Inventing missing author or edition information.
- Ignoring variant titles.
- Failing to record the access date.
- Failing to save the query used.

## Related Wiki Pages

- [[source-materials]]
- [[workflows]]
- [[known-errors]]
- [[examples]]
