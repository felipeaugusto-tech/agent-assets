---
id: GOV-VERSIONING
title: Versioning and Change Management
phase: governance
summary: Semantic versioning of standards, changelog process, and deprecation lifecycle.
tags: [governance, versioning, changelog, deprecation]
applies_to: ["**/*"]
tech: null
extends: null
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Versioning and Change Management

## Purpose

This document defines how changes to the standards in this repository are versioned, communicated, and tracked, so that teams always know which version of a rule they are working against.

## Repository Versioning

The entire repository is versioned as a whole using Semantic Versioning 2.0.0.

| Change type | Version bump | Example |
|---|---|---|
| New rule IDs added, new tech overlays added | **MINOR** | `1.0.0` → `1.1.0` |
| Existing **SHOULD** rule tightened to **MUST** | **MINOR** | `1.1.0` → `1.2.0` |
| Existing **MUST** rule relaxed to **SHOULD** | **MAJOR** | `1.2.0` → `2.0.0` |
| Existing **MUST** rule removed or its meaning changed | **MAJOR** | `1.2.0` → `2.0.0` |
| Clarification, typo fix, wording improvement (no semantic change) | **PATCH** | `1.2.0` → `1.2.1` |
| New governance meta document added | **PATCH** | `1.2.1` → `1.2.2` |

Individual standard documents also carry their own `version` field in frontmatter. Increment the document version using the same scheme when the document changes.

## Changelog

All changes to the repository MUST be recorded in `CHANGELOG.md` at the repository root. The changelog follows Keep a Changelog conventions.

### Changelog categories

- **Added** — new standard files, new rules, new tech overlays.
- **Changed** — updates to existing rules that alter their meaning or severity.
- **Deprecated** — rules or standards that are still present but should no longer be followed.
- **Removed** — rules or standard files deleted (rare; prefer deprecation).
- **Fixed** — corrections to wording that do not change the intent of a rule.
- **Security** — changes addressing a security issue in the standards themselves.

### Changelog entry format

```markdown
## [MAJOR.MINOR.PATCH] — YYYY-MM-DD

### Added
- `sdlc/security/data-privacy.md` — new standard for privacy-by-design principles (SEC-005).

### Changed
- `sdlc/development/coding-standards.md` DEV-003: tightened function length limit from 80 to 50 lines.

### Deprecated
- `sdlc/development/old-standard.md` DEV-010: superseded by DEV-011.
```

## Change Process

### Minor and patch changes (non-breaking)

1. Branch off `main`.
2. Make changes following the authoring process in [`rule-authoring.md`](rule-authoring.md).
3. Update `CHANGELOG.md`.
4. Bump the `version` field in the changed document's frontmatter.
5. Open a pull request. At least one Tech Lead or Governance Owner must approve.
6. Merge to `main`. Tag the repository with the new version.

### Major changes (breaking)

Major changes alter the meaning of a MUST rule or remove a rule. These require:

1. A documented rationale (ADR or governance ticket).
2. A migration guide appended to the changelog entry (describing what teams need to change).
3. A communication to all engineering teams with at least **14 days' notice** before the change is merged.
4. Approval from the Governance Owner.

## Deprecation Lifecycle

1. A rule enters **deprecated** status via a MINOR version bump. The rule remains in the repository and `rules-manifest.yaml` with a `deprecated: true` flag.
2. Deprecated rules are announced in the changelog and communicated to engineering teams.
3. After a **90-day** grace period, a deprecated rule may be removed in a MAJOR version bump.
4. Rule IDs of removed rules are **never reused**.

## Communication

Repository version releases are communicated via:

- A tag and GitHub release (or equivalent) on the repository.
- A notification to the engineering channel with the changelog summary.
- For MAJOR releases: a dedicated announcement with migration guide and deadline.
