---
id: PRD-001
title: User Story Standards
phase: product
extends: null
tech: null
summary: Rules for writing well-formed, estimable, independently testable user stories.
tags: [product, user-stories, invest, personas, splitting]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# User Story Standards (PRD-001)

## Purpose

User stories are the primary unit of work in the product phase. Poorly written stories are the leading cause of rework, estimation errors, and missed requirements. These standards ensure every story entering development is understood, testable, and deliverable.

## Scope

Applies to all user stories created for features, enhancements, and user-facing behaviour changes. Does not apply to technical chores, bug reports, or purely infrastructure work — though INVEST criteria are recommended for all work items.

---

## MUST

- **PRD-001-01** Every user story is written in the format: "As a **[specific named persona]**, I want to **[single action or capability]**, so that **[concrete outcome or value]**." Each component is meaningful: the persona is a specific named user type (not "user" or "admin"), the action describes a single capability, the outcome describes concrete value (not "so that I can use the feature").
- **PRD-001-02** Every story satisfies all six INVEST criteria: Independent (deliverable without another in-progress story), Negotiable (describes a goal, not a solution), Valuable (delivers value to the persona), Estimable (the team can size it), Small (completable within a single sprint by one or two engineers), Testable (at least one verifiable acceptance criterion exists).
- **PRD-001-03** Stories have been estimated and the estimate is within the team's agreed maximum story size before entering a sprint.

## MUST NOT

- **PRD-001-04** Include specific technology choices, UI layout/visual design details, database schema requirements, or other implementation prescriptions in the story text — these belong in a linked technical task or design document.

## SHOULD

- **PRD-001-05** When a story exceeds the team's maximum size, it is split using one of: workflow steps, data variations, roles/personas, CRUD operations, or happy path vs edge cases. Each resulting story independently satisfies INVEST.
- **PRD-001-06** Stories are created using [`templates/user-story-template.md`](../../templates/user-story-template.md).

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| Jira | [`jira/user-stories.md`](jira/user-stories.md) | Teams using Jira |
