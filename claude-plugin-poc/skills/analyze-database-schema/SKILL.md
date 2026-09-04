---
name: analyze-database-schema
description: Analyze a repository's database layer -- schema inventory, relationships, migration health, naming conventions, index usage, and risk areas. Manual invocation only.
disable-model-invocation: true
---

# Analyze Database Schema

For onboarding onto a project's data model, reviewing schema changes before a migration, or auditing data health. Read-only against the codebase, one structured report out.

## 1. Fix the target

The target is **the user's current repository**, never this plugin or the GenDD corpus. Identify the database engine in use before analyzing — ask if it isn't obvious from the code.

## 2. Load the reference (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/analyze-database-schema/analyze-database-schema.md` | **Primary task flow.** |
| `${CLAUDE_PLUGIN_ROOT}/references/analyze-database-schema/dba.md` | **The actual analysis method** the primary flow delegates to. |

Reading these as they are: verbatim corpus copies, `@GenDD-Flow/...`/`@TargetRepo` links don't resolve here.

## 3. Run the process

1. **Locate schema sources** — migration files, ORM model definitions, SQL scripts, seed data.
2. **Apply the DBA analysis method** from `dba.md` to produce:
   - Schema inventory (tables, views, stored procedures)
   - Relationship map (foreign keys, join patterns)
   - Migration history and health
   - Naming convention audit
   - Index usage and optimization opportunities
   - Data ownership boundaries
   - Risk areas (missing constraints, orphan tables, N+1 patterns)
3. **Save the report** to `docs/database-analysis.md`.

## 4. Never invent

A relationship, index, or risk finding not backed by an actually-inspected schema file or migration is a guess. If the migration history is incomplete or ambiguous, say so as a gap rather than reconstructing a plausible history.

## 5. Hard limits

- Writes only `docs/database-analysis.md` in the target repository.
- No schema, migration, or data changes — this is an audit, not a migration tool.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
- Read-only against the codebase throughout.
