# Documentation Phase Standards

**Rule-ID prefix:** `DOC`

## Purpose

Documentation standards ensure that code, APIs, and repositories remain understandable over time. Good documentation reduces onboarding time, reduces support burden, and makes the system's intent clear to future maintainers — human and AI.

## Standards in this phase

| File | Rule IDs | Summary |
|---|---|---|
| [`code-documentation.md`](code-documentation.md) | DOC-001 | Inline docs, docstrings, self-documenting code |
| [`api-documentation.md`](api-documentation.md) | DOC-002 | Public API docs, examples, contract-driven generation |
| [`repository-documentation.md`](repository-documentation.md) | DOC-003 | README, CONTRIBUTING, onboarding docs |
| [`changelog.md`](changelog.md) | DOC-004 | Changelog standard (Keep a Changelog) |
| [`knowledge-retention.md`](knowledge-retention.md) | DOC-005 | Decision capture, runbook/wiki upkeep |

## Tech overlays

| Technology | Folder | Applies to |
|---|---|---|
| Docusaurus | [`docusaurus/`](docusaurus/README.md) | `docs/**`, `website/**`, `docusaurus.config.*` |

## Agent routing note

Load this index first. For Docusaurus projects, also open the Docusaurus overlay.
