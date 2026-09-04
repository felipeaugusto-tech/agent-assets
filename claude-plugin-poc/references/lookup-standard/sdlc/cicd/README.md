# CI/CD Phase Standards

**Rule-ID prefix:** `CICD`

## Purpose

CI/CD standards ensure that the pipeline is a reliable, fast, and secure path from code to production. They prevent the pipeline from becoming a bottleneck, a security gap, or a source of non-reproducible builds.

## Standards in this phase

| File | Rule IDs | Summary |
|---|---|---|
| [`pipeline-standards.md`](pipeline-standards.md) | CICD-001 | Required stages, quality gates, fast feedback |
| [`build-reproducibility.md`](build-reproducibility.md) | CICD-002 | Deterministic builds, artifact integrity, provenance |
| [`versioning-releases.md`](versioning-releases.md) | CICD-003 | Semantic versioning, tagging, release notes |
| [`deployment-strategies.md`](deployment-strategies.md) | CICD-004 | Blue/green, canary, rollback, feature flags |
| [`environments.md`](environments.md) | CICD-005 | Environment parity and promotion |

## Tech overlays

| Technology | Folder | Applies to |
|---|---|---|
| GitHub Actions | [`github-actions/`](github-actions/README.md) | `.github/workflows/**` |

## Agent routing note

Load this index first. For GitHub Actions workflow files, also open the GitHub Actions overlay.
