# Development Phase Standards

**Rule-ID prefix:** `DEV`

## Purpose

Development standards define how code is written, structured, and handed off. They reduce defect rates, onboarding time, and the long-term cost of maintenance.

## Standards in this phase

| File | Rule IDs | Summary |
|---|---|---|
| [`coding-standards.md`](coding-standards.md) | DEV-001 | Naming, formatting, structure, function size, immutability |
| [`error-handling.md`](error-handling.md) | DEV-002 | Errors, exceptions, boundaries, fail-safe behaviour |
| [`code-complexity.md`](code-complexity.md) | DEV-003 | Complexity limits, duplication, dead-code removal |
| [`dependency-management.md`](dependency-management.md) | DEV-004 | Adding, pinning, and auditing dependencies |
| [`code-comments.md`](code-comments.md) | DEV-005 | When and how to comment; docstrings |
| [`definition-of-done.md`](definition-of-done.md) | DEV-006 | Checklist for a code change to be complete |

## Tech overlays

| Technology | Folder | Applies to |
|---|---|---|
| Java | [`java/`](java/README.md) | `**/*.java` |

## Agent routing note

Load this index first. Then open only the topic file(s) relevant to your task. For Java code, also open the corresponding file under `java/`.
