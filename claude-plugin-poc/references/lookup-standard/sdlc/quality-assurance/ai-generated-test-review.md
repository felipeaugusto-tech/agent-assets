---
id: QA-008
title: AI-Generated Test Review Standards
phase: quality-assurance
extends: null
tech: null
summary: Rules for validating AI-authored or AI-assisted tests before they are trusted as a quality gate.
tags: [qa, ai-generated-tests, review, gendd, validation]
applies_to: ["**/*.test.*", "**/*.spec.*", "**/test/**", "**/tests/**", "**/__tests__/**"]
version: "1.0.0"
last_reviewed: "2026-07-30"
---

# AI-Generated Test Review Standards (QA-008)

## Purpose

An AI agent can produce a test suite that reaches a target coverage number while asserting nothing meaningful, or that encodes the current, possibly buggy, behaviour of the code as the expected result. These standards ensure a human validates AI-authored or AI-assisted tests before they are trusted as regression protection or release evidence.

## Scope

Applies to any test file authored, substantially drafted, or substantially modified by an AI coding agent, regardless of language or stack. Does not replace the directives in [`test-automation.md`](test-automation.md) (QA-002) or [`coverage.md`](coverage.md) (QA-003) — an AI-generated test is still subject to those standards in full; this file adds the review obligations specific to AI authorship.

---

## MUST

- **QA-008-01** A human reviewer reads and approves every AI-generated test file before it is merged. An AI agent's own summary or self-report of passing tests is not sufficient sign-off.
- **QA-008-02** Before an AI-generated test is trusted as a regression guard, confirm that it fails when the code under test is reverted to its pre-fix or pre-feature state and passes only against the correct behaviour. Delete or rewrite a test that passes regardless of the implementation it is supposed to verify.
- **QA-008-03** Every AI-generated test carries traceability to the requirement, acceptance criterion, or defect it verifies, for example a reference to the AC ID or ticket number in the test name, display name, or an adjacent comment.
- **QA-008-04** AI-generated test suites for high-risk code — payment, authentication, identity verification, and PII handling — receive the same senior-engineer review required for human-written tests in that risk tier. AI authorship does not lower the review bar.

## MUST NOT

- **QA-008-05** Accept an AI-generated test that only calls the method under test and asserts the absence of an exception, without asserting on the actual result or resulting state, as satisfying coverage or acceptance-criteria requirements.
- **QA-008-06** Treat an AI agent's reported coverage percentage or reported "all tests passing" status as sufficient release evidence without independent human review or a deterministic CI-enforced check.
- **QA-008-07** Allow an AI agent to mark its own generated tests as validated or approved. Validation status is set by a human reviewer or a deterministic CI gate, never by the generating agent.

## SHOULD

- **QA-008-08** Record, alongside each AI-generated test artefact, its source basis (the requirement or spec section it was generated from), a confidence level, and its current validation status, so reviewers can prioritise scrutiny.
- **QA-008-09** Spot-check AI-generated test data and fixtures for realistic-looking PII the model may have fabricated or carried over from its prompt context, in addition to the standing prohibition on real PII in [`test-data-management.md`](test-data-management.md) (QA-004).

## MAY

- **QA-008-10** Use a second AI pass to review a first AI pass's generated tests for tautological assertions or missed edge cases, as a pre-filter before human review. This does not replace the human review required by QA-008-01.
