---
id: CICD-003
title: Versioning and Release Standards
phase: cicd
extends: null
tech: null
summary: Rules for semantic versioning, release tagging, and release notes.
tags: [cicd, versioning, semver, releases, tagging, changelog, release-notes]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Versioning and Release Standards (CICD-003)

## Purpose

Consistent versioning allows consumers to understand the impact of an upgrade, enables automated tooling, and provides a clear audit trail of what was released and when.

---

## MUST

- **CICD-003-01** All released artefacts use Semantic Versioning 2.0.0 (`MAJOR.MINOR.PATCH`): `MAJOR` for breaking API changes, `MINOR` for new backward-compatible features, `PATCH` for backward-compatible bug fixes. Pre-release versions use the semver pre-release format (e.g. `1.2.0-rc.1`).
- **CICD-003-02** Every release is tagged in version control with `v<MAJOR>.<MINOR>.<PATCH>` (e.g. `v1.2.0`) from the same commit used to build the released artefact. Tags are not deleted or moved after creation.
- **CICD-003-03** Every release has a corresponding entry in `CHANGELOG.md` following Keep a Changelog conventions, added before or at the time of release, not retroactively. See [`sdlc/documentation/changelog.md`](../documentation/changelog.md).

## SHOULD

- **CICD-003-04** Release pipelines automate changelog generation from Conventional Commits messages (e.g. `semantic-release`, `conventional-changelog`); automated release notes are reviewed before publication but do not require full manual authoring.
