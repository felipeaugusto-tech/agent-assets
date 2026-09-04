---
id: VCS-002
title: Commit Convention Standards
phase: version-control
extends: null
tech: null
summary: Rules for Conventional Commits format, atomic commits, and commit signing.
tags: [version-control, commits, conventional-commits, git, atomic, signing]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Commit Convention Standards (VCS-002)

## Purpose

Consistent commit messages make the history readable, enable automated changelog generation, and allow tooling to detect breaking changes. Atomic commits make bisecting and reverting safe.

---

## MUST

- **VCS-002-01** Every commit message follows Conventional Commits 1.0.0 format: `<type>[optional scope]: <description>`. Allowed types: `feat` (MINOR bump), `fix` (PATCH bump), `chore`, `docs`, `refactor`, `test`, `perf`, `ci`, `build`. Breaking changes are indicated with `!` after the type/scope or a `BREAKING CHANGE:` footer.
- **VCS-002-02** Each commit represents one logical, complete change. A commit that adds a feature does not also fix an unrelated bug; a commit that refactors code does not also change behaviour.
- **VCS-002-03** A `.gitignore` is present and configured to exclude: secrets/credentials/API keys, build artefacts and compiled binaries, generated code reproducible from source, dependency vendor directories (e.g. `node_modules/`, `.venv/`), and personal IDE/editor configuration files.

## MUST NOT

- **VCS-002-04** Commit secrets, credentials, API keys, or private keys. See [`sdlc/security/secrets-management.md`](../security/secrets-management.md).
- **VCS-002-05** Commit build artefacts, compiled binaries, generated code reproducible from source, dependency vendor directories, or personal IDE configuration files.

## SHOULD

- **VCS-002-06** Commits are signed using a GPG or SSH key configured with the version control platform, with signing required for merges to `main`.
