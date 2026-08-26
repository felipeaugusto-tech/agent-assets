# Quality Assurance Phase Standards

**Rule-ID prefix:** `QA`

## Purpose

Quality assurance standards define how testing is planned, automated, and maintained. They ensure defects are caught close to their origin, preventing expensive late-stage discoveries.

## Standards in this phase

| File | Rule IDs | Summary |
|---|---|---|
| [`test-strategy.md`](test-strategy.md) | QA-001 | Test pyramid and what to test at each level |
| [`test-automation.md`](test-automation.md) | QA-002 | Automation structure, naming, determinism |
| [`coverage.md`](coverage.md) | QA-003 | Coverage expectations and measurement |
| [`test-data-management.md`](test-data-management.md) | QA-004 | Fixtures, factories, no production data |
| [`flaky-tests.md`](flaky-tests.md) | QA-005 | Flaky test detection, quarantine, and fix SLAs |
| [`non-functional-testing.md`](non-functional-testing.md) | QA-006 | Performance, load, security, accessibility testing |
| [`mocking.md`](mocking.md) | QA-007 | Mocking boundaries, test doubles, contract fidelity |
| [`ai-generated-test-review.md`](ai-generated-test-review.md) | QA-008 | Human review and validation of AI-authored tests |

## Tech overlays

| Technology | Folder | Applies to |
|---|---|---|
| JUnit | [`junit/`](junit/README.md) | `**/*Test.java`, `**/*Tests.java` |

## Agent routing note

Load this index first. For Java test files, also open the JUnit overlay.

## Referenced by

This domain is the canonical, ID'd rule source for the `QA-GenDD` operating model's QA playbooks — see `QA-GenDD/.cursor/rules/automation-qa-standards.md` (mocking, AI usage) and `QA-GenDD/.cursor/rules/core-principles.md` (Related Files). Those files carry an operator-facing summary; this domain is authoritative on conflict.
