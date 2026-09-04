---
id: QA-002
title: Test Automation Standards
phase: quality-assurance
extends: null
tech: null
summary: Rules for automation structure, test naming, determinism, and maintainability.
tags: [qa, test-automation, naming, determinism, aaa, structure]
applies_to: ["**/*.test.*", "**/*.spec.*", "**/test/**", "**/tests/**", "**/__tests__/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Test Automation Standards (QA-002)

## Purpose

Test suites that are hard to read, flaky, or order-dependent lose the trust of the team and are gradually disabled. These standards make automated tests reliable, understandable, and maintainable.

---

## MUST

- **QA-002-01** Test names describe the unit under test, the scenario, and the expected outcome. Format: `[unit]_[scenario]_[expected outcome]` or plain English sentence. Acceptable: `"createUser when email already exists throws DuplicateEmailException"`. Not acceptable: `"testCreateUser"`, `"test1"`, `"should work"`.
- **QA-002-02** Every test follows Arrange/Act/Assert: Arrange (set up the system and inputs), Act (invoke the single action being tested), Assert (verify the expected outcome). Each section is separated by a blank line or comment. A test contains only one Act section.
- **QA-002-03** Tests are deterministic: no dependency on current time without an injectable clock, no random data without a fixed seed or controlled input, no real external network calls in unit tests (use mocks/stubs), no shared mutable state between tests.

## MUST NOT

- **QA-002-04** Write tests that depend on each other's execution order. Each test sets up its own state and cleans up after itself.

## SHOULD

- **QA-002-05** Each test verifies a single, focused behaviour. Tests verifying multiple unrelated outcomes are split.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| JUnit | [`junit/test-automation.md`](junit/test-automation.md) | `**/*Test.java` |
