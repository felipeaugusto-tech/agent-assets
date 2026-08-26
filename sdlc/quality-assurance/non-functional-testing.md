---
id: QA-006
title: Non-Functional Testing Standards
phase: quality-assurance
extends: null
tech: null
summary: Rules for performance, load, security, and accessibility testing.
tags: [qa, performance-testing, load-testing, security-testing, accessibility, non-functional]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Non-Functional Testing Standards (QA-006)

## Purpose

Functional tests verify what a system does. Non-functional tests verify how it performs. Systems without non-functional testing frequently fail their NFRs only after reaching production.

---

## MUST

- **QA-006-01** For any service with defined NFRs (see [`sdlc/architecture/non-functional-requirements.md`](../architecture/non-functional-requirements.md)), at least one automated test validates each NFR before the first production deployment. NFRs that cannot be validated by an automated test have a documented manual verification procedure.
- **QA-006-02** Load and performance tests run against a staging environment, never against production. Staging matches production in data volume, configuration, and hardware tier for results to be valid.

## SHOULD

- **QA-006-03** CI pipelines include SAST scanning against source code. DAST runs against the staging environment on a scheduled basis or before major releases. Security test results are reviewed and tracked with the same SLA as vulnerability findings in [`sdlc/security/vulnerability-management.md`](../security/vulnerability-management.md).
- **QA-006-04** User-facing UI features are tested for WCAG 2.1 Level AA conformance using automated scanning (e.g. axe-core, Lighthouse) in the UI test suite, with manual keyboard navigation and screen reader testing for critical user flows.
