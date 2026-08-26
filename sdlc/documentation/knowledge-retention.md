---
id: DOC-005
title: Knowledge Retention Standards
phase: documentation
extends: null
tech: null
summary: Rules for capturing decisions, keeping runbooks current, and wiki hygiene.
tags: [documentation, knowledge, runbooks, wiki, decisions, institutional-knowledge]
applies_to: ["**/docs/**", "**/runbooks/**", "**/wiki/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Knowledge Retention Standards (DOC-005)

## Purpose

Knowledge that lives only in individuals' heads is fragile. These standards ensure that operational knowledge, decisions, and tribal wisdom are documented and accessible to the whole team.

---

## MUST

- **DOC-005-01** Significant technical decisions are documented as ADRs in version control. See [`sdlc/architecture/decision-records.md`](../architecture/decision-records.md) for trigger criteria and template.
- **DOC-005-02** After every SEV1 or SEV2 incident, runbooks used during the response are updated to reflect missing steps, incorrect steps, and the resolution steps that actually worked. Runbook updates are a tracked action item in the postmortem.

## MUST NOT

- **DOC-005-03** Allow critical operational procedures to have a single point of knowledge failure — procedures are documented such that at least two engineers can perform them without assistance from the original author.

## SHOULD

- **DOC-005-04** Runbooks are stored in version control under `docs/runbooks/` and linked from the alerts and monitoring dashboards they correspond to.
