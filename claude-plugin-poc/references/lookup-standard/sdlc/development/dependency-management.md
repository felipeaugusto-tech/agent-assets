---
id: DEV-004
title: Dependency Management Standards
phase: development
extends: null
tech: null
summary: Rules for adding, pinning, and auditing third-party dependencies.
tags: [development, dependencies, supply-chain, pinning, audit, licensing]
applies_to: ["**/package.json", "**/pom.xml", "**/build.gradle", "**/requirements.txt", "**/go.mod", "**/Cargo.toml", "**/Gemfile", "**/*.lock"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Dependency Management Standards (DEV-004)

## Purpose

Third-party dependencies are the largest attack surface in modern applications. These standards reduce supply-chain risk, licence exposure, and the cost of dependency maintenance.

---

## MUST

- **DEV-004-01** All production and build-time dependencies are pinned to a specific version or a version range that cannot resolve to a semver-major update without explicit developer action. Lock files (e.g. `package-lock.json`, `poetry.lock`, `Cargo.lock`) are committed to version control for applications. `latest`, `*`, or unbounded `>=` ranges are not used for production dependencies.
- **DEV-004-02** Before a new dependency is added, a vulnerability scan runs using the project's configured tool (e.g. `npm audit`, `pip-audit`, `trivy`, `snyk`). A dependency with a known critical or high severity vulnerability with no available fix is not added; if a fix exists, the fixed version is used.

## MUST NOT

- **DEV-004-03** Add a dependency with a licence that is incompatible with the project's licence. Copyleft licences (GPL, AGPL) in application dependencies require explicit approval from the Governance Owner.
- **DEV-004-04** Add a dependency that has had no release or commit activity in its primary repository for more than 24 months and has no active fork or maintainer.

## SHOULD

- **DEV-004-05** When multiple libraries solve the same problem, prefer the one with the smallest transitive dependency footprint.
- **DEV-004-06** Dependencies are reviewed and updated at minimum quarterly. Security patches are applied within the SLA defined in [`sdlc/security/vulnerability-management.md`](../security/vulnerability-management.md).
