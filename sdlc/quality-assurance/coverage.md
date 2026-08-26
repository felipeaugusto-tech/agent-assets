---
id: QA-003
title: Test Coverage Standards
phase: quality-assurance
extends: null
tech: null
summary: Coverage expectations, how they are measured, and what they do and do not guarantee.
tags: [qa, coverage, metrics, branch-coverage, line-coverage]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Test Coverage Standards (QA-003)

## Purpose

Coverage metrics are useful signals but imperfect guarantees. These standards establish meaningful targets while preventing the common failure mode of "gaming" coverage with low-quality tests.

---

## MUST

- **QA-003-01** Coverage is measured and reported in the CI pipeline for every pull request. CI blocks merge if coverage falls below the minimum thresholds.
- **QA-003-02** Production application code maintains a minimum of 80% line coverage. Auto-generated code, configuration files, framework boilerplate, and data transfer objects may be excluded from coverage calculation via the project's coverage tool configuration.

## MUST NOT

- **QA-003-03** Write tests that increase coverage without making meaningful assertions about the behaviour. Tests that call a method and assert only that no exception was thrown, without asserting the result, are not an acceptable coverage strategy.

## SHOULD

- **QA-003-04** Branch coverage of at least 70% is targeted in addition to line coverage.
