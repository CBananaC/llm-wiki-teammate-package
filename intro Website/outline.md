# Intro Website Outline

## Approved framing

The website presents a general-purpose system for reviewing Qing official
communication. 林爽文事件 is a case study that demonstrates how the system
can help researchers study 奏折 and 上諭; it is not the system's only subject.

奏折 and 上諭 are introduced as “two central forms of Qing imperial
communication.” 硃批 is explained as the emperor's vermilion response written
on or attached to a memorial, and as an important response layer for
reconstructing the communication chain.

The homepage opening is:

> **Reconstructing Qing Imperial Communication**
>
> An AI-assisted, human-reviewed system for studying 奏折, 硃批, and 上諭.

## Brainstorm record — assistant response

The following records the assistant's previous brainstorm output that was
approved as the starting point for this outline.

Yes, this is the stronger framing. The website should present a general-purpose system for reviewing Qing official communication, while 林爽文事件 is only the case study that demonstrates its value.

For historical precision, I suggest describing 奏折 and 上諭 as “two central forms of Qing imperial communication”:

- 奏折: officials report to the emperor.
- 硃批: the emperor’s vermilion response written on or attached to a memorial.
- 上諭: imperial instructions sent from the emperor to officials.

The proposed website structure could be:

1. **What are 奏折 and 上諭?**
   Introduce their functions, participants, direction of communication, and value as first-hand historical materials.

2. **Why are they difficult to study?**
   Explain the enormous quantity of documents, fragmented communication chains, missing dates, unclear replies, and time delays between officials, the emperor, and the battlefield.

3. **Why visualization is necessary**
   Show how plain-text reading hides chronology and relationships, while timelines, dots, lines, and chart lanes reveal communication patterns.

4. **What this website does**
   Present the system as an AI-assisted, human-reviewed research environment:

   `large text corpus → AI extraction → relationship reconstruction → human review → visual chart`

5. **Case study: 林爽文事件**
   Explain why it is a useful example: wartime communication was crucial, information delay affected military decisions, and a substantial corpus of 奏折 and 上諭 survives in scholarly compilations.

6. **Core design principle**
   Emphasize that AI proposes; humans judge. Users read the original source, verify quotations and dates, review AI outputs in the chat panel, and only then add accepted events or relationships to the chart.

7. **How to use the system**
   Cover source selection, document search, AI-output review, timeline reading, relationship inspection, and chart interaction.

8. **How to recreate the system**
   Explain:
   - choosing a research question and corpus;
   - OCR and source-preserving structuring;
   - storing document type, title, sender, receiver, dates, original text, and provenance;
   - reconstructing relationships through explicit textual evidence, date rules, and LLM assistance;
   - running skills on individual documents;
   - loading JSON outputs into the website;
   - human verification and chart promotion.

9. **The AI loop**
   Introduce the three components separately:
   - **Skills:** task-specific instructions defining what to extract and how to preserve evidence.
   - **AI model:** Claude, GPT, Gemini, DeepSeek, etc.; compare them by task, accuracy, structure, cost, speed, and Chinese-text performance.
   - **Loop:** repeatable processing across many documents, with JSON outputs, resumability, and review bundles.

   Model comparisons should be based on small project tests rather than permanent claims that one model is always best.

10. **Research example and further use**
    Display selected 林爽文 research results, then explain how reviewed outputs can feed the LLM Wiki and future historical research.

For the UI, I suggest separating the website into two modes:

- **System mode:** explains the general method and teaches students how to recreate it.
- **Case-study mode:** demonstrates the method with 林爽文事件 materials.

The homepage could begin with:

> **Reconstructing Qing Imperial Communication**
>
> An AI-assisted, human-reviewed system for studying 奏折, 硃批, and 上諭.

Visually, the most effective interactive element would be a single document journey:

`奏折 sent → emperor receives → 硃批／上諭 issued → official receives or acts → later report`

Known dates should appear as solid points. Missing or inferred dates should appear as gaps or dashed elements rather than invented precision.

The four-line chart should be explained using the system’s actual lane labels. The introduction site should avoid inventing new lane names or implying that 林爽文事件 is the system’s only possible subject.
