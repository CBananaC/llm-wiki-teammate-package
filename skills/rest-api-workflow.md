# Skill: REST API Workflow

## Purpose

Use this skill to query external RESTful APIs safely, accurately, and repeatably for digital humanities work on Sinitic / Chinese texts.

## What RESTful API Means

- A REST API lets a program request data from a web service.
- Requests usually use URLs and query parameters.
- Responses are often JSON.
- Read the API documentation before using an endpoint.
- Do not guess endpoint names, parameter names, or response fields.

## When To Use

Use this skill when the task requires:

- Looking up external data.
- Enriching wiki pages with catalog records, identifiers, people, places, or dates.
- Checking names, places, dates, or source metadata.
- Calling a public database such as CBDB, CHGIS/TGAZ, LibraryCloud, or Wikidata.
- Writing a small repeatable script for API calls.

## Required Inputs

- API documentation URL or copied documentation.
- Base URL and endpoint.
- Query parameters.
- Expected response format.
- Output file or wiki page to update.
- Citation or source-recording rule.

## Workflow

1. Read the API documentation.
2. Identify the base URL, endpoint, required parameters, and rate limits.
3. Test one small request first.
4. Inspect the raw response before extracting fields.
5. Decide which fields are useful for the research task.
6. Save raw or summarized API results when they support later verification.
7. Add extracted data to the relevant wiki page or `outputs/` file.
8. Record endpoint URL, query used, access date, and uncertainty.
9. Keep external claims separate from source-derived claims.
10. Record repeated failures or confusing response fields in [[known-errors]].

## Safety Rules

- Do not hardcode API keys.
- Do not commit access tokens.
- Respect rate limits.
- Prefer an official API over scraping.
- Do not invent missing API fields.
- If the API response is empty, report that it is empty.
- If the API fails, show the error instead of guessing.

## Output Rules

When summarizing API data, preserve:

- Source or database name.
- Endpoint URL.
- Query used.
- Date accessed.
- Useful fields.
- Missing fields.
- Uncertainty or match status.

## Common Errors

- Treating API data as if it came from the primary source.
- Assuming the first match is correct.
- Dropping the query and access date.
- Normalizing names or places without recording the original API value.
- Hiding failed or empty API responses.

## Related Wiki Pages

- [[source-materials]]
- [[workflows]]
- [[known-errors]]
- [[examples]]
