---
id: VCS-GITHUB-001
title: Pull Request Standards — GitHub
phase: version-control
extends: sdlc/version-control/pull-requests.md
tech: github
summary: Extends VCS-003 with GitHub branch-protection and repository settings rules.
tags: [version-control, pull-requests, github, branch-protection, codeowners]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Pull Request Standards — GitHub (VCS-GITHUB-001)

> This overlay extends [`sdlc/version-control/pull-requests.md`](../pull-requests.md). All directives in VCS-003 remain in full effect. Only GitHub-specific directives appear here.

## Purpose

GitHub branch protection and repository settings must be explicitly configured to enforce the review and CI requirements defined in VCS-003 and VCS-004.

---

## MUST

- **VCS-GITHUB-001-01** The `main` branch has GitHub branch protection rules configured with: `Require a pull request before merging` (enabled), `Required approvals` (minimum 1), `Dismiss stale reviews when new commits are pushed` (enabled), `Require status checks to pass before merging` (enabled), `Restrict direct pushes` (enabled).
- **VCS-GITHUB-001-02** All CI jobs running the test suite, lint, and security scan are added as required status checks on `main`. A PR is not mergeable if any required status check is failing.
- **VCS-GITHUB-001-03** A `CODEOWNERS` file is present and configured to require review from the appropriate owner for: security-critical files (authentication, authorisation, secrets management), CI/CD pipeline configuration, infrastructure IaC files, and governance/standards files.

## SHOULD

- **VCS-GITHUB-001-04** The `Require branches to be up to date before merging` option is enabled in branch protection settings; authors rebase or merge `main` before requesting a final merge.
- **VCS-GITHUB-001-05** A PR template is placed at `.github/pull_request_template.md` using [`templates/pull-request-template.md`](../../../templates/pull-request-template.md) as its source.
