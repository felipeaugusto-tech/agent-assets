---
id: DOC-004
title: Changelog Standards
phase: documentation
extends: null
tech: null
summary: Rules for maintaining a changelog following Keep a Changelog conventions.
tags: [documentation, changelog, release-notes, keep-a-changelog, versioning]
applies_to: ["**/CHANGELOG*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Changelog Standards (DOC-004)

## Purpose

A changelog communicates what changed to users, operators, and auditors. It is the human-readable record of the project's evolution.

---

## MUST

- **DOC-004-01** Every repository that produces a released artefact has a `CHANGELOG.md` at the repository root, created when the first release is made.
- **DOC-004-02** `CHANGELOG.md` follows Keep a Changelog format with an `[Unreleased]` section, versioned sections in descending order, and entries grouped under `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Security`.
- **DOC-004-03** Changelog entries for user-visible changes are added to the `[Unreleased]` section at the time the change is merged to `main`, not retrospectively at release time.

## MUST NOT

- **DOC-004-04** Add changelog entries for internal refactors with no user-visible behaviour change, dependency updates with no API or behaviour impact, CI/CD pipeline changes, or documentation-only updates (unless the documentation is the shipped product).
