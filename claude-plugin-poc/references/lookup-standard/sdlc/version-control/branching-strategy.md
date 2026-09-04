---
id: VCS-001
title: Branching Strategy Standards
phase: version-control
extends: null
tech: null
summary: Rules for the branching model, branch naming, and branch lifecycle.
tags: [version-control, branching, git, trunk, feature-flags, branch-naming]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Branching Strategy Standards (VCS-001)

## Purpose

A clear branching strategy prevents merge conflicts, ensures `main` is always deployable, and makes work-in-progress visible and reviewable.

---

## MUST

- **VCS-001-01** The `main` branch is always in a releasable state. Every merge to `main` passes all CI checks. Code merged to `main` that breaks the build is reverted immediately.
- **VCS-001-02** Branch names follow the pattern `<type>/<ticket-id>-<short-description>`. Allowed type prefixes: `feat/`, `fix/`, `chore/`, `docs/`, `refactor/`, `test/`, `hotfix/`. Example: `feat/PROJ-123-add-password-reset`.

## MUST NOT

- **VCS-001-03** Push commits directly to `main`. All changes go through a pull request with at least one reviewer approval. Branch protection is configured to enforce this.

## SHOULD

- **VCS-001-04** Feature branches are merged or rebased onto `main` within 2 business days. Branches older than 5 days without merge activity are reviewed and either merged, rebased, or deleted. Feature flags are used to deploy incomplete features safely rather than keeping branches open.
