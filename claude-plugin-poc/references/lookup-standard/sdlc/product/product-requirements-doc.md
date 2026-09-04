---
id: PRD-004
title: Product Requirements Document Standard
phase: product
extends: null
tech: null
summary: Standard structure and content requirements for a PRD.
tags: [product, prd, requirements, goals, success-metrics]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Product Requirements Document Standard (PRD-004)

## Purpose

A PRD aligns product, design, and engineering on the problem to be solved, the goals, and the constraints before any story is written or design is started.

## Scope

Required for: new features, significant enhancements, cross-team initiatives, any change that affects an external API or user-facing contract. Not required for: single-sprint bug fixes, dependency upgrades, purely operational changes with no user-facing impact.

---

## MUST

- **PRD-004-01** The PRD states the problem being solved before any solution, goal, or feature is described. The problem statement identifies the affected user segment, describes the current state and why it is unsatisfactory, and is stated in terms of user or business impact — not in terms of missing features.
- **PRD-004-02** The PRD includes at least two success metrics that are measurable (expressible as a number, rate, or percentage), baseline-anchored (the current value is known or estimated), and time-bounded (the target is expected by a specific date).
- **PRD-004-03** The PRD contains a section that explicitly lists what is out of scope for this initiative, reviewed and agreed upon by the product owner and at least one engineering representative before the PRD is baselined.
- **PRD-004-04** Every PRD contains these sections in order: Overview, Problem Statement, Goals, Success Metrics, User Personas, Requirements (MoSCoW prioritised), Out of Scope, Assumptions and Constraints, Dependencies, Open Questions (with owners and target resolution dates).

## MUST NOT

- **PRD-004-05** Generate user stories from a PRD that lacks a problem statement, success metrics, or scope definition.

## SHOULD

- **PRD-004-06** The PRD is reviewed and acknowledged by at least one Tech Lead or Senior Engineer, focusing on feasibility, integration impact, and non-functional requirements, before user stories are written from it.
