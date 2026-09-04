---
id: DOC-003
title: Repository Documentation Standards
phase: documentation
extends: null
tech: null
summary: Rules for README, CONTRIBUTING, and onboarding documentation.
tags: [documentation, readme, contributing, onboarding, repository]
applies_to: ["**/README*", "**/CONTRIBUTING*", "**/docs/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Repository Documentation Standards (DOC-003)

## Purpose

A repository without a README requires every new developer to figure out setup through trial and error. These standards ensure every repository is self-describing and onboardable.

---

## MUST

- **DOC-003-01** Every repository has a `README.md` at its root containing: project title and summary (what and why, 1–3 sentences), prerequisites (tools and versions required), step-by-step local setup instructions, and instructions for running the automated test suite.
- **DOC-003-02** Setup instructions are updated in the same PR as any change that alters the setup process (new environment variable, changed tool version, new dependency).

## SHOULD

- **DOC-003-03** The README includes: an architecture overview, configuration reference (environment variables), deployment information or a link to deployment runbooks, and a link to CONTRIBUTING.md.
- **DOC-003-04** Repositories that accept contributions have a `CONTRIBUTING.md` covering the branch strategy, PR process, coding standards, and how to run tests locally.
