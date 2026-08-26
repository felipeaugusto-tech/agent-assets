---
# REQUIRED frontmatter — fill in every field before publishing a new standard.
id: "PHASE-NNN"                    # Unique rule-set ID, e.g. DEV-001
title: "Short descriptive title"
phase: "development"               # One of: product | architecture | development | security |
                                   #         database | quality-assurance | version-control |
                                   #         cicd | observability | infrastructure | documentation
extends: null                      # Tech overlays only: path to the agnostic file this extends,
                                   # e.g. "sdlc/development/coding-standards.md". null otherwise.
tech: null                         # Tech overlays only: technology name, e.g. "java". null otherwise.
summary: "One sentence — what this standard governs."
tags:
  - example-tag
applies_to:
  - "**/*"                         # Narrow this glob as tightly as the rule allows
version: "1.0.0"
last_reviewed: "YYYY-MM-DD"
# DO NOT add a severity: field — severity is expressed by section structure, not frontmatter.
---

# [Title] ([PHASE-NNN])

## Purpose

[1–2 sentences: why this standard exists and what outcome it protects.]

## Scope

[What files, roles, activities, and environments this standard covers. State any explicit exclusions. Omit this section only if Purpose fully covers it.]

---

## MUST

<!--
  List absolute requirements. Deviation requires a formal exception.
  Format: - **[PHASE-NNN-NN]** [Imperative statement in plain voice. No RFC 2119 keywords.]
  Omit this section if there are no MUST directives.
-->

- **[PHASE-NNN-01]** [Directive text — specific, actionable, imperative voice, no MUST/SHOULD/MAY keywords.]

---

## MUST NOT

<!--
  List absolute prohibitions. Deviation requires a formal exception.
  Omit this section if there are no MUST NOT directives.
-->

- **[PHASE-NNN-02]** [Directive text — describe what is forbidden.]

---

## SHOULD

<!--
  List strong defaults. Agents apply these unless there is a concrete documented reason not to.
  Omit this section if there are no SHOULD directives.
-->

- **[PHASE-NNN-03]** [Directive text — describe the preferred behaviour.]

---

## SHOULD NOT

<!--
  List strongly discouraged behaviours.
  Omit this section if there are no SHOULD NOT directives.
-->

---

## MAY

<!--
  List optional guidance. No justification required to skip.
  Omit this section if there are no MAY directives.
-->

---

## Tech-Specific Standards

<!--
  Agnostic files only. List technology overlays that extend this standard.
  Remove this section entirely from tech overlay files.
-->

The following technology overlays extend the rules in this file. If your work involves one of these technologies, open the linked overlay and apply its directives in addition to those above.

| Technology | Overlay file | Applies to |
|---|---|---|
| [Tech name] | [`phase/tech/topic.md`](../tech/topic.md) | `glob pattern` |

---

## References

<!--
  External links relevant to this standard. Remove this section if none.
-->

- [Reference title](url)
