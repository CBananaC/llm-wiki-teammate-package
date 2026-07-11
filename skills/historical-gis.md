# Skill: Historical GIS

## Purpose

Use this skill to turn place references into map-ready historical GIS data while preserving uncertainty and avoiding invented coordinates.

## When To Use

Use this skill when the task asks for:

- Extracting or reviewing place names.
- Matching historical places to CHGIS/TGAZ or another gazetteer.
- Creating gazetteer CSV files.
- Creating GeoJSON for QGIS or web maps.
- Comparing historical geography with people, texts, or network data.

## Rules

- Preserve the original place wording from the source.
- Do not replace historical names with modern names unless asked.
- Do not invent coordinates.
- Keep broad regions, abbreviated places, and uncertain matches marked as uncertain.
- Record query names, query years, gazetteer IDs, endpoint URLs, and access dates.
- Keep source-derived place mentions separate from external gazetteer enrichments.

## Recommended Output Fields

- `source_id`
- `place_text`
- `normalized_place`
- `period`
- `gazetteer_id`
- `latitude`
- `longitude`
- `uncertain`
- `evidence`
- `notes`

For CHGIS/TGAZ enrichment, also record:

- `query_name`
- `query_year`
- `chgis_name`
- `chgis_id`
- `feature_type`
- `parent_name`
- `parent_chgis_id`
- `valid_from`
- `valid_to`
- `present_location`
- `api_url`

## Workflow

1. Extract place names from checked source text or TEI.
2. Decide whether each place is specific enough for gazetteer lookup.
3. Search an authoritative gazetteer such as CHGIS/TGAZ.
4. Use date or period filters when available.
5. Compare candidate matches by name, type, parent unit, and valid years.
6. Save matched and unmatched places in CSV.
7. Create GeoJSON only for places with verified coordinates.
8. Record limitations, especially when places are broad regions or index addresses.

## Common Errors

- Geocoding broad regions as precise points.
- Using modern coordinates for historical administrative units without explanation.
- Ignoring valid-year ranges.
- Treating an ancestral or index address as a travel route or residence.
- Hiding failed gazetteer queries.

## Related Wiki Pages

- [[source-materials]]
- [[extraction-rules]]
- [[workflows]]
- [[known-errors]]
