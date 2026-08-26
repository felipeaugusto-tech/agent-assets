# Database Phase Standards

**Rule-ID prefix:** `DAT`

## Purpose

Database standards govern how data is modelled, stored, accessed, and maintained. Poor database practices produce data integrity issues, performance degradation, and privacy violations that are expensive to remediate after the fact.

## Standards in this phase

| File | Rule IDs | Summary |
|---|---|---|
| [`schema-design.md`](schema-design.md) | DAT-001 | Data modelling, normalisation, keys, constraints, naming |
| [`migrations.md`](migrations.md) | DAT-002 | Safe, reversible, zero-downtime migrations |
| [`query-standards.md`](query-standards.md) | DAT-003 | Performance, indexing, N+1 avoidance, parameterisation |
| [`data-lifecycle.md`](data-lifecycle.md) | DAT-004 | Retention, archival, backups, restore testing |
| [`pii-handling.md`](pii-handling.md) | DAT-005 | PII classification, minimisation, masking in databases |

## Tech overlays

| Technology | Folder | Applies to |
|---|---|---|
| PostgreSQL | [`postgresql/`](postgresql/README.md) | `**/*.sql` and PostgreSQL-backed services |

## Agent routing note

Load this index first. For SQL files, also open the PostgreSQL overlay if the project uses PostgreSQL.
