# Skill: Network Analysis

## Purpose

Use this skill to create evidence-based network nodes and edges from source text, TEI markup, or external databases such as CBDB.

## When To Use

Use this skill when the task asks for:

- Extracting relationships between people, places, texts, offices, or concepts.
- Creating node and edge CSV files.
- Creating GEXF files for Gephi.
- Comparing source-derived relationships with database-derived relationships.
- Explaining what a network can and cannot support.

## Rules

- Every edge must have evidence.
- Do not create edges from co-occurrence alone.
- Keep source-derived edges separate from external database edges.
- Preserve original relationship wording when possible.
- Mark direction, uncertainty, and evidence source.
- Do not infer friendship, kinship, influence, residence, or affiliation unless the evidence states it.

## Recommended Node Fields

- `node_id`
- `label`
- `node_type`
- `uncertain`
- `notes`

## Recommended Edge Fields

- `source_id`
- `source_node`
- `source_type`
- `target_node`
- `target_type`
- `relationship`
- `evidence`
- `uncertain`
- `notes`

For external database edges, also record:

- `year`
- `evidence_source`
- `evidence_pages`
- `api_url`
- external IDs such as `cbdb_person_id`

## Workflow

1. Identify candidate nodes from reviewed entity extraction, TEI, or database records.
2. Identify explicit relationship statements.
3. Create a node table with stable IDs and labels.
4. Create an edge table with evidence for each relationship.
5. Mark uncertainty where relationship type, direction, date, or target is unclear.
6. Export GEXF only after node and edge CSVs are inspectable.
7. Add a short interpretation note explaining what the network supports and what it does not support.

## Common Errors

- Treating co-occurrence as a relationship.
- Mixing article claims with CBDB claims.
- Dropping edge evidence.
- Reversing directed relationships.
- Over-interpreting a small demonstration network.
- Treating database relationships as complete social reality.

## Related Wiki Pages

- [[source-materials]]
- [[extraction-rules]]
- [[workflows]]
- [[known-errors]]
