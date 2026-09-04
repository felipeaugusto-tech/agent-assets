---
id: QA-004
title: Test Data Management Standards
phase: quality-assurance
extends: null
tech: null
summary: Rules for fixtures, factories, and the prohibition of production data in tests.
tags: [qa, test-data, fixtures, factories, pii, production-data]
applies_to: ["**/*.test.*", "**/*.spec.*", "**/test/**", "**/fixtures/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Test Data Management Standards (QA-004)

## Purpose

Test data that is hardcoded, shared, or sourced from production creates brittle, insecure, and non-reproducible tests. These standards ensure test data is safe, isolated, and maintainable.

---

## MUST

- **QA-004-01** Test data is created using factory functions, builder objects, or data-generation libraries rather than hardcoded fixture files. Each factory provides sensible defaults that produce a valid object with the ability to override specific fields for the scenario under test.

## MUST NOT

- **QA-004-02** Use data extracted from production systems in tests. Test databases are populated with synthetic or anonymised data only. See [`sdlc/database/pii-handling.md`](../database/pii-handling.md).
- **QA-004-03** Commit test fixture files containing real PII (real names, email addresses, phone numbers, national IDs, financial data). Use obviously synthetic values (e.g. `test@example.com`, `John Test`, `555-0100`) or randomised fake data libraries.

## SHOULD

- **QA-004-04** Each test creates only the data it needs in a scoped context (e.g. within a transaction that is rolled back, or in a freshly created test scope). Shared test data sets are avoided in favour of per-test data setup.
