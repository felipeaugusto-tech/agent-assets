---
id: CICD-001
title: Pipeline Standards
phase: cicd
extends: null
tech: null
summary: Rules for required pipeline stages, quality gates, and fast feedback.
tags: [cicd, pipeline, stages, quality-gates, fast-feedback, security]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Pipeline Standards (CICD-001)

## Purpose

A CI/CD pipeline that is slow, unreliable, or skipped stops being a quality gate and becomes an obstacle. These standards make the pipeline fast, mandatory, and trustworthy.

---

## MUST

- **CICD-001-01** Every pipeline includes these stages in this order: (1) Lint/format check, (2) Build, (3) Unit tests, (4) Security scan (SAST + dependency vulnerability), (5) Integration tests, (6) Package/image build. Deployment steps follow only after all six stages pass.
- **CICD-001-02** Stages are ordered fastest to slowest. A failing stage stops the pipeline immediately and does not proceed to subsequent stages.
- **CICD-001-03** All pipeline configuration is stored as code in the repository alongside the code it builds and goes through the same PR review process.

## MUST NOT

- **CICD-001-04** Deploy to any environment — including staging — if any required pipeline stage has failed.
- **CICD-001-05** Set `continue-on-error: true` on lint, test, or security-scan stages.

## SHOULD

- **CICD-001-06** The CI pipeline completes within 10 minutes, achieved through parallelising test suites, caching dependencies, and gating integration tests on specific triggers.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| GitHub Actions | [`github-actions/pipeline-standards.md`](github-actions/pipeline-standards.md) | `.github/workflows/**` |
