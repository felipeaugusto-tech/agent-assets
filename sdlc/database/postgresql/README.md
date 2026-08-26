# Database Phase — PostgreSQL Overlay

**Tech:** PostgreSQL
**Rule-ID prefix:** `DAT-POSTGRESQL`
**Applies to:** `**/*.sql` in PostgreSQL-backed services
**Extends:** [`sdlc/database/`](../README.md)

## Purpose

This overlay extends the agnostic database standards with PostgreSQL-specific rules for schema design, query optimisation, and index strategy.

## Files in this overlay

| File | Rule IDs | Summary |
|---|---|---|
| [`schema-design.md`](schema-design.md) | DAT-POSTGRESQL-001 | PostgreSQL-specific schema design and type selection rules |
| [`query-standards.md`](query-standards.md) | DAT-POSTGRESQL-002 | PostgreSQL query optimisation, index types, and EXPLAIN rules |

## How to use

Read the agnostic database standards first, then read these files for PostgreSQL-specific rules.
