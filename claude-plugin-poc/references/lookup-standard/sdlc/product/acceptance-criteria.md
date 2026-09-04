---
id: PRD-002
title: Acceptance Criteria Standards
phase: product
extends: null
tech: null
summary: Rules for writing testable Given/When/Then acceptance criteria.
tags: [product, acceptance-criteria, gherkin, bdd, testability]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Acceptance Criteria Standards (PRD-002)

## Purpose

Acceptance criteria are the contract between product and development. Ambiguous or incomplete criteria are the primary cause of "done but wrong" outcomes. These standards ensure criteria are precise, testable, and complete.

## Scope

Applies to all acceptance criteria on user stories, bug reports, and spike outcomes that result in verifiable behaviour, whether verified by automated or manual tests.

---

## MUST

- **PRD-002-01** Every acceptance criterion follows the structure: "Given [specific precondition or system state] / When [single atomic action] / Then [specific, objectively observable outcome]." Each clause is specific enough to set up or verify in a test.
- **PRD-002-02** Every story has at least one acceptance criterion covering an unhappy or error path: an invalid/unexpected user input, a system failure or unavailable dependency, or a boundary condition (empty state, maximum values, expired sessions).
- **PRD-002-03** Each criterion is independently verifiable — its "Then" clause describes a single observable outcome that does not depend on the outcome of another criterion in the same story.

## MUST NOT

- **PRD-002-04** Include references to specific API endpoints, HTTP verbs, database fields or table names, UI component names, DOM selectors, class names, method names, or internal identifiers in any Given/When/Then clause.
- **PRD-002-05** Use subjective language in "Then" clauses (e.g. "looks good", "is fast", "is appropriate") — outcomes are objectively verifiable.

## SHOULD

- **PRD-002-06** For stories involving data input, numeric ranges, or conditional logic, criteria include scenarios for minimum and maximum valid values, values just outside the valid range, and empty/null/whitespace inputs where applicable.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| Jira | [`jira/acceptance-criteria.md`](jira/acceptance-criteria.md) | Teams using Jira |
