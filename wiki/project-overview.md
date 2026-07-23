# Project Overview

This project studies communication, command, and response during the 林爽文事件 using structured first-hand records and human-reviewed AI assistance.

The formal review tool is the evidence-review workspace. The wiki stores durable context and rules; it is not a second copy of datasets, review state, generated bundles, or progress logs.

## Dual deliverable and student-facing purpose

The repository is also an example system for students preparing work in the
2026 PolyU AI X Digital Humanities Awards. The completed hand-in has two
connected parts: a working review website for 上奏／硃批／上諭 materials and a
dynamic companion website that explains the historical question, demonstrates
how to use the review surfaces, and teaches students how to recreate the data,
AI-review, and visualisation workflow.

The competition brief is stored in `Competition Info/`. It is a bilingual
public draft with unresolved placeholders and should guide planning, not be
treated as the final official rules. The competition context particularly
supports showing a demonstrable tool, explaining educational and research
value, documenting AI use and human judgement, and acknowledging source and
licensing constraints.

## Context supplied by the second-hand and FYP materials

The materials in `2nd Material & FYP/` suggest a concise teaching narrative:

1. Existing scholarship provides historical context on the 林爽文事件,
   battlefield stages, Qing governance in Taiwan, local and military
   mobilisation, logistics, and spatial reconstruction.
2. The FYP frames the research problem as wartime information delay: the
   emperor relied on delayed 奏摺 and returned 硃批／上諭 while frontline and
   Fujian officials had to act with newer local knowledge.
3. A dynamic-institutional or 新政治史 approach makes the workflow itself
   meaningful: students can see how documents are extracted, dated, linked,
   reviewed, and turned into a cautious historical interpretation.
4. Maps, place-name notes, coordinates, and GIS material provide a spatial
   layer that complements the document timeline and relationship network.

These materials are secondary or working notes. They are useful for framing
and teaching, but they do not replace the canonical first-hand dataset or the
human review required before a claim is promoted into the system.

## Research principles

- Treat AI output as a proposal until reviewed.
- Keep original evidence beside every extracted or interpreted claim.
- Distinguish document chronology from event chronology and imperial knowledge chronology.
- Preserve differences among `send_date`, `receive_date`, `announce_date`, and remaining `issue_date`.
- Keep formal, sample, and generated candidate data separate.
- Preserve uncertainty and provenance through every processing stage.

## Wiki scope

Keep only:

- current research framing;
- source and corpus descriptions;
- terminology and rules;
- repeatable workflows;
- links to canonical skills;
- concise attempt-specific decisions.

Store operational history in `PROJECT_LOG.md`, executable prompts in `tool/skills md/`, and research data in the canonical review-tool locations.
