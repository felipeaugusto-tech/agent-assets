---
id: CICD-GHA-001
title: Pipeline Standards — GitHub Actions
phase: cicd
extends: sdlc/cicd/pipeline-standards.md
tech: github-actions
summary: Extends CICD-001 with GitHub Actions workflow security and structure rules.
tags: [cicd, pipeline, github-actions, security, permissions, secrets]
applies_to: [".github/workflows/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Pipeline Standards — GitHub Actions (CICD-GHA-001)

> This overlay extends [`sdlc/cicd/pipeline-standards.md`](../pipeline-standards.md). All directives in CICD-001 remain in full effect. Only GitHub Actions-specific directives appear here.

## Purpose

GitHub Actions workflows have unique security constraints around permissions, third-party action supply chain, and secret handling that require explicit controls.

---

## MUST

- **CICD-GHA-001-01** Every workflow declares a `permissions` block at the top level set to minimum required values (default to `contents: read`). Jobs that need additional permissions declare them at the job level. `permissions: write-all` is never used.
- **CICD-GHA-001-02** All third-party actions are pinned to a full commit SHA with a comment indicating the human-readable version tag (e.g. `uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2`). Tags and branches are not used in `uses:` fields.

## MUST NOT

- **CICD-GHA-001-03** Print secrets to workflow logs via `echo`, `run: env`, or debug output. Enable `ACTIONS_STEP_DEBUG` in production pipelines. Pass secret values as command-line arguments — use environment variables or files instead.

## SHOULD

- **CICD-GHA-001-04** Deployment jobs targeting production reference a GitHub Environment configured with required reviewers, with environment-scoped secrets for production credentials rather than repository-level secrets.
- **CICD-GHA-001-05** Workflows authenticating to cloud providers (AWS, GCP, Azure) use OIDC-based authentication (`id-token: write` permission) rather than storing static access keys as repository secrets.
