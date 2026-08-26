---
id: DAT-POSTGRESQL-001
title: Schema Design Standards — PostgreSQL
phase: database
extends: sdlc/database/schema-design.md
tech: postgresql
summary: Extends DAT-001 with PostgreSQL-specific schema design rules.
tags: [database, schema, postgresql, types, uuid, jsonb]
applies_to: ["**/*.sql"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Schema Design Standards — PostgreSQL (DAT-POSTGRESQL-001)

> This overlay extends [`sdlc/database/schema-design.md`](../schema-design.md). All directives in DAT-001 remain in full effect. Only PostgreSQL-specific directives appear here.

## Purpose

PostgreSQL's type system has specific characteristics that affect correctness and performance. Using the right types avoids common pitfalls with integer overflow, timezone ambiguity, and JSONB indexing.

---

## MUST

- **DAT-POSTGRESQL-001-01** Primary key columns use `BIGSERIAL` (auto-incrementing 64-bit integer) or `UUID` (with `gen_random_uuid()` default). `SERIAL` (`INT`) is not used for new tables. `UUID` is preferred for tables that may be sharded or that have IDs generated outside the database.
- **DAT-POSTGRESQL-001-02** All timestamp columns use `TIMESTAMPTZ` (`TIMESTAMP WITH TIME ZONE`). `TIMESTAMP` without time zone is not used for new columns.

## SHOULD

- **DAT-POSTGRESQL-001-03** When JSON storage is required, `JSONB` is used. `JSON` type is used only when exact byte-level preservation of the input JSON is a business requirement.
- **DAT-POSTGRESQL-001-04** `TEXT` is used for string columns unless a specific length limit is a genuine business constraint enforced at the database level, in which case `VARCHAR(n)` is acceptable.
