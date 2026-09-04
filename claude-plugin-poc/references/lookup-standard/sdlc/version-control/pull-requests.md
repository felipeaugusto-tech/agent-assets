---
id: VCS-003
title: Pull Request Standards
phase: version-control
extends: null
tech: null
summary: Rules for PR size, description quality, and linking to tickets.
tags: [version-control, pull-requests, pr, size, description, linking]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Pull Request Standards (VCS-003)

## Purpose

Pull requests are the primary review surface in the development workflow. Clear, focused PRs that are easy to review receive better feedback, fewer missed defects, and faster approvals.

---

## MUST

- **VCS-003-01** Every PR references the ticket or issue it closes or relates to in the PR description using the platform's closing keyword syntax (e.g. `Closes #123`, `Fixes PROJ-456`).
- **VCS-003-02** Every PR description explains: what changed (2–4 sentence summary), why the change was made (the problem being solved), and how to test it (steps the reviewer can follow to verify the change works).
- **VCS-003-03** PRs do not exceed 400 lines of changed non-generated production code. When a task requires more than 400 lines, it is broken into a series of smaller, independently reviewable PRs using feature flags or draft PRs for in-progress work. Generated code, lock files, and migration files are excluded from the 400-line count.
- **VCS-003-04** Authors verify before requesting review: CI passes with no new failures, the Definition of Done is satisfied, the description includes what/why/how-to-test, and the ticket link is present.

## SHOULD

- **VCS-003-05** PR descriptions use [`templates/pull-request-template.md`](../../templates/pull-request-template.md) as their structure.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| GitHub | [`github/pull-requests.md`](github/pull-requests.md) | Teams using GitHub |
