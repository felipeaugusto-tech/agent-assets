---
id: VCS-004
title: Code Review Standards
phase: version-control
extends: null
tech: null
summary: Rules for reviewer responsibilities, review checklist, and SLAs.
tags: [version-control, code-review, reviewer, checklist, sla, feedback]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Code Review Standards (VCS-004)

## Purpose

Code review is the primary human quality gate. These standards ensure reviews are timely, thorough, and constructive.

---

## MUST

- **VCS-004-01** Reviewers provide a review within 1 business day of being assigned. If unable to review within the SLA, the reviewer communicates a revised timeline or reassigns.
- **VCS-004-02** At least one peer approval is required before a PR can be merged to `main`. For changes to security-critical code (authentication, authorisation, secrets management, data access), at least one approver is a Tech Lead or security-aware engineer.
- **VCS-004-03** Reviewers check: correctness (does the change do what the description says; are edge cases handled?), security (see [`sdlc/security/`](../security/README.md)), tests (are new tests adequate, deterministic, and meaningful?), and DoD compliance.

## MUST NOT

- **VCS-004-04** Approve a PR that contains a known violation of a MUST rule. The reviewer flags the violation as a blocking comment.

## SHOULD

- **VCS-004-05** Review comments are specific (reference the exact line, explain the problem) and actionable (suggest a concrete alternative). Non-blocking suggestions are prefixed with `nit:` or `suggestion:` to distinguish them from blocking feedback.
