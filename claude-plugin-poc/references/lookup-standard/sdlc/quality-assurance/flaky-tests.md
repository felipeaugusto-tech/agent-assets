---
id: QA-005
title: Flaky Test Policy
phase: quality-assurance
extends: null
tech: null
summary: Rules for detecting, quarantining, and fixing flaky tests with SLAs.
tags: [qa, flaky-tests, quarantine, reliability, ci]
applies_to: ["**/*.test.*", "**/*.spec.*", "**/test/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Flaky Test Policy (QA-005)

## Purpose

Flaky tests erode trust in the test suite. When developers cannot trust CI to give reliable signal, they start ignoring failures — including real ones. These standards treat flaky tests as defects that must be resolved on a schedule.

---

## MUST

- **QA-005-01** A test that fails intermittently without a code change is moved to a quarantine category within 24 hours of identification. Quarantined tests do not block the CI pipeline. A ticket is created to track the fix.
- **QA-005-02** Quarantined tests are fixed or deleted within 14 calendar days of quarantine. If the underlying behaviour cannot be tested reliably within 14 days, the test is deleted and a tracking ticket is created for a better-designed replacement.

## MUST NOT

- **QA-005-03** Permanently disable tests (using `@Ignore`, `@Skip`, `xit`, or equivalent) without a linked, active ticket. Disabled tests that have been in the repository for more than 30 days with no active remediation are removed.

## SHOULD

- **QA-005-04** Flaky tests are tracked in the team's bug backlog with the same severity as production bugs, with the root cause documented in the fix ticket.
