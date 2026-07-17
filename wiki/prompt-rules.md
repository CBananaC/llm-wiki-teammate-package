# Prompt Rules

- State one task and its evidence boundary clearly.
- Provide the relevant source text or structured record directly.
- Name the required fields and exact output format.
- Require quotations or evidence spans for interpretive fields.
- Tell the model not to translate, normalize, convert dates, or infer missing facts unless requested.
- Require explicit uncertainty for ambiguous readings or relationships.
- Keep source evidence, external enrichment, and interpretation in separate fields.
- For JSON workflows, request raw JSON only, without prose or Markdown fences.
- Test revised prompts on positive, negative, and ambiguous records before batch use.
- Store reusable prompts in `tool/skills md/`, not inside the wiki.
- Treat all model outputs as candidates until reviewed in the appropriate review surface.

