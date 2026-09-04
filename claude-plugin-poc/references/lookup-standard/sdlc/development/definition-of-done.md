---
id: DEV-006
title: Definition of Done
phase: development
extends: null
tech: null
summary: Checklist every code change must satisfy before it can be merged.
tags: [development, definition-of-done, dod, checklist, merge, quality-gate]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Definition of Done (DEV-006)

## Purpose

The Definition of Done (DoD) is the shared contract that defines what "finished" means for a code change. It prevents "done but broken", "done but unreviewed", and "done but undocumented" outcomes.

---

## MUST

- **DEV-006-01** Every item in the DoD checklist below is satisfied before a change is merged to the main branch. Urgency is not a valid reason to merge incomplete work.

## SHOULD

- **DEV-006-02** The DoD checklist is validated by the author before requesting review, not by the reviewer.

---

## Definition of Done Checklist

**Code quality**
- [ ] Code follows [`coding-standards.md`](coding-standards.md) — naming, structure, function size.
- [ ] Cyclomatic complexity of modified functions is at or below 10 (see [`code-complexity.md`](code-complexity.md)).
- [ ] No commented-out code or orphaned TODO/FIXME comments without a ticket reference.
- [ ] No dead code (unreachable blocks, unused imports, unused variables) introduced.
- [ ] Formatter passes with no violations.
- [ ] Linter passes with no new warnings or errors.

**Error handling**
- [ ] All errors are handled explicitly — no empty catch blocks or silently swallowed exceptions (see [`error-handling.md`](error-handling.md)).
- [ ] Error responses to external callers do not contain stack traces or internal system details.

**Tests**
- [ ] New functionality is covered by automated tests at the appropriate level(s).
- [ ] All existing tests pass.
- [ ] No new flaky tests introduced.
- [ ] Test names clearly describe the scenario and expected outcome.

**Security**
- [ ] No secrets, credentials, or PII present in the diff.
- [ ] Input validation and output encoding applied to all code handling external data (see [`sdlc/security/input-validation-output-encoding.md`](../security/input-validation-output-encoding.md)).
- [ ] New or updated dependencies scanned for known vulnerabilities (see [`dependency-management.md`](dependency-management.md)).

**Documentation**
- [ ] Public APIs, functions, and types have docstrings.
- [ ] CHANGELOG updated if the change is user-visible or alters existing behaviour.
- [ ] README or onboarding documentation updated if setup steps changed.

**Review**
- [ ] At least one peer review approved with no outstanding blocking comments.
- [ ] All reviewer comments have been addressed or explicitly dismissed with justification.
- [ ] PR description links to the story or ticket being closed.

**Deployment readiness**
- [ ] The change can be deployed and rolled back independently.
- [ ] Feature flags added for high-risk or incremental rollouts (where applicable).
- [ ] Monitoring or observability impact considered — new metrics, alerts, or log entries added if the change introduces new failure modes.
