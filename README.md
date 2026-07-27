# C16 — Generative AI for Adobe Photoshop

Courseware for the Tertiary Infotech non-WSQ short course **Generative AI for
Adobe Photoshop (C16)** — a one-day, hands-on course on transforming image-editing
workflows with the generative AI built into Adobe Photoshop (Adobe Firefly).

Course page: https://www.tertiarycourses.com.sg/generative-ai-for-adobe-photoshop.html

## What's here

| Path | Contents |
|---|---|
| `courseware/` | Slide deck (PPTX + PDF), Lesson Plan (DOCX + PDF), Learner Guide (DOCX + PDF) |
| `labs/` | 10 hands-on labs, a README index, `tools.md`, a `reference-pack/` and `starter-files/` |
| `LG-Generative AI for Adobe Photoshop (C16).md` | Markdown mirror of the Learner Guide |
| `.claude/skills/non-wsq-courseware-build/` | The single-source build engine and course data |

## Single source of truth

Every artifact — the slide deck, the Lesson Plan, the Learner Guide and every lab —
is generated from one content module so they stay 100% aligned:

- `.claude/skills/non-wsq-courseware-build/build/course_data.py` — course metadata,
  learning outcomes, topics, schedule and Learner-Guide content.
- `.claude/skills/non-wsq-courseware-build/build/data_domain1.py` / `data_domain2.py` —
  the two topics and their labs.

## Rebuild

```bash
# labs
python .claude/skills/non-wsq-courseware-build/build/gen_labs.py
# PPT + LP + LG (DOCX + PDF, with page-numbered TOCs)
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
```

## The course

Learners build one connected deliverable — a brand campaign key visual for the
fictional **Solace Radiance Serum** — across all 10 labs:

**Topic 1 — Generative Editing Essentials in Photoshop**
1. Get Started with Firefly and Generative AI in Photoshop
2. Write Effective Prompts for Image Generation
3. Add and Remove Content with Generative Fill
4. Extend Images with Generative Expand
5. One-Click Cleanup with the AI Remove Tool
6. Generate and Replace the Background

**Topic 2 — Advanced Generative Workflows**
7. Text-to-Image Generation with Reference Images and Styles
8. AI-Powered Portrait Retouching and Neural Filters
9. Combine Generative Layers with Masks and Blend Modes
10. Build the End-to-End Workflow and Check Commercial Use and IP

This is a commercial short course: no assessment, and each lab verifies itself with
a "Test it" step.

---

© 2026 Tertiary Infotech Academy Pte Ltd
