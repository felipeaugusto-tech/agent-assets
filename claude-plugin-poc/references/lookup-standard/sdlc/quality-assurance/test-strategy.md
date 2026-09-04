---
id: QA-001
title: Test Strategy Standards
phase: quality-assurance
extends: null
tech: null
summary: Rules for the test pyramid and what to test at each level.
tags: [qa, test-strategy, test-pyramid, unit, integration, e2e]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Test Strategy Standards (QA-001)

## Purpose

An unplanned test strategy results in brittle, expensive test suites or dangerously low coverage. The test pyramid provides a principled approach to allocating test effort across levels.

---

## MUST

- **QA-001-01** Every service has a documented test strategy before production release, describing: the test pyramid levels applied, coverage targets per level, which layers are covered by automated vs manual tests, and the tooling at each level.
- **QA-001-02** The test suite follows the test pyramid: unit tests (test individual functions/classes in isolation) form the majority; integration tests (test collaboration including real or in-memory dependencies) are significantly fewer; end-to-end tests (complete user flows through the full stack) cover only a small set of critical path scenarios.

## MUST NOT

- **QA-001-03** Rely solely on end-to-end tests as the primary quality gate.

## SHOULD

- **QA-001-04** Before writing an integration or end-to-end test, evaluate whether a unit test can adequately verify the same behaviour. Only escalate to a higher level when the lower level cannot verify the interaction in question.
