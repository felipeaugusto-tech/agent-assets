---
id: QA-007
title: Mocking Standards
phase: quality-assurance
extends: null
tech: null
summary: Rules for where mocking belongs, what must never be mocked, and how mocked dependencies stay faithful to the real contract.
tags: [qa, mocking, test-doubles, fakes, boundaries]
applies_to: ["**/*.test.*", "**/*.spec.*", "**/test/**", "**/tests/**", "**/__tests__/**"]
version: "1.0.0"
last_reviewed: "2026-07-30"
---

# Mocking Standards (QA-007)

## Purpose

Mocking is a tool for isolating a unit from dependencies it does not own, not a way to avoid testing behaviour. Mocking the wrong thing hides real integration defects, and asserting on a mock's internals couples tests to implementation rather than behaviour. These standards define where mocking belongs and where it does not.

---

## MUST

- **QA-007-01** Mock only at architectural boundaries the test does not own: external HTTP/API calls, databases in unit tests, the file system, and system clock/randomness sources.
- **QA-007-02** Model a mocked dependency's request and response shape after its real, currently-documented contract, including its documented error responses, so the mock cannot silently diverge from the behaviour it stands in for.
- **QA-007-03** Provide both success and failure/error response fixtures for every mocked external dependency, so failure-handling logic is exercised and not only the happy path.

## MUST NOT

- **QA-007-04** Mock the unit under test itself, pure functions, simple value objects or DTOs, or internal implementation details of the code being verified.
- **QA-007-05** Assert on a mocked collaborator's internal call order or private state when the test's purpose is to verify observable behaviour. Assert on the inputs and outputs of the interaction instead.
- **QA-007-06** Rely on live calls to third-party vendor services in unit tests or automated PR-gating tests. Validate a vendor integration itself through a contract test or a controlled vendor sandbox, not by mocking the vendor away.

## SHOULD

- **QA-007-07** Prefer a fake or in-memory test double over a deep chain of stubbed mock calls when the dependency has meaningful behaviour worth modelling, for example an in-memory repository instead of a mocked data-access object with dozens of stubbed methods.
- **QA-007-08** Update a mocked dependency's stubbed responses whenever the real dependency's contract changes, so the mock does not drift out of sync with production behaviour.

## MAY

- **QA-007-09** Maintain a shared mock or fixture library for a frequently-mocked external dependency, such as a common vendor API, to keep stub definitions consistent across test suites.
