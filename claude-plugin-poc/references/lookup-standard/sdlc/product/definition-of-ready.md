---
id: PRD-003
title: Definition of Ready
phase: product
extends: null
tech: null
summary: Entry checklist a backlog item must meet before development starts.
tags: [product, definition-of-ready, backlog, refinement, sprint-planning]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Definition of Ready (PRD-003)

## Purpose

The Definition of Ready (DoR) is the shared checklist that a backlog item must satisfy before a team can begin development. It prevents starting work on poorly defined items and reduces mid-sprint rework caused by unclear requirements.

## Scope

Applies to all user stories, bug fixes with user-visible behaviour change, and spikes. Pure technical chores may use a lighter checklist defined by the team.

---

## MUST

- **PRD-003-01** A story is not committed to a sprint unless every DoR checklist item below is satisfied. Stories that are not ready at sprint planning are returned to the backlog for further refinement.

## SHOULD

- **PRD-003-02** DoR compliance is reviewed during backlog refinement sessions, before sprint planning. Stories that fail DoR at refinement are assigned an owner and a target date for re-review.

---

## Definition of Ready Checklist

All items below must be true before a story is Ready.

**Problem and value**
- [ ] Written in "As a / I want / so that" format with a specific, named persona.
- [ ] Business value is clearly stated and agreed upon by the product owner.
- [ ] Linked to a parent epic or initiative.

**Acceptance criteria**
- [ ] At least two acceptance criteria are written in Given/When/Then format.
- [ ] At least one criterion covers the unhappy or error path.
- [ ] All criteria are objectively verifiable (no subjective language).

**Scope and size**
- [ ] All six INVEST criteria are satisfied (see [`user-stories.md`](user-stories.md)).
- [ ] The story has been estimated and the estimate is within the team's maximum story size.
- [ ] Out-of-scope items are explicitly listed.

**Dependencies**
- [ ] All external dependencies (other stories, APIs, teams) are identified.
- [ ] Dependencies are either resolved or have a confirmed unblocking plan with an owner and date.
- [ ] Required access or permissions (environments, data, third-party services) have been provisioned or formally requested.

**Design and UX (if applicable)**
- [ ] Wireframes, mockups, or design specifications are attached or linked and in final or approved-draft state.
- [ ] Edge cases and empty states are covered in the design artefacts.

**Technical clarity**
- [ ] The team has discussed the story and reached shared understanding of the approach.
- [ ] No known technical blockers exist.
- [ ] Any required spike or proof-of-concept has been completed and its outcome is documented.
