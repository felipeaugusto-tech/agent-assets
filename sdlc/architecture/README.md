# Architecture Phase Standards

**Rule-ID prefix:** `ARC`

## Purpose

Architecture standards govern technical design decisions before and during implementation. They reduce the cost of change by ensuring decisions are made deliberately, documented with their rationale, and reviewed before they are locked in.

## Standards in this phase

| File | Rule IDs | Summary |
|---|---|---|
| [`decision-records.md`](decision-records.md) | ARC-001 | When and how to write ADRs |
| [`design-documents.md`](design-documents.md) | ARC-002 | Technical design doc standard and triggers |
| [`api-design.md`](api-design.md) | ARC-003 | API versioning, compatibility, error model, pagination |
| [`non-functional-requirements.md`](non-functional-requirements.md) | ARC-004 | Capturing and validating NFRs |
| [`diagramming.md`](diagramming.md) | ARC-005 | Diagram conventions and source-control requirements |

## Tech overlays

| Technology | Folder | Applies to |
|---|---|---|
| OpenAPI | [`openapi/`](openapi/README.md) | `openapi.yaml`, `openapi.json`, `*.oas.yaml` |

## Agent routing note

Load this index first. Then open only the specific topic file relevant to your task. For API contract files, also open `openapi/api-design.md`.
