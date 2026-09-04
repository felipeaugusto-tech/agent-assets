---
id: DAT-POSTGRESQL-002
title: Query Standards — PostgreSQL
phase: database
extends: sdlc/database/query-standards.md
tech: postgresql
summary: Extends DAT-003 with PostgreSQL-specific query optimisation and index type rules.
tags: [database, queries, postgresql, indexing, explain, partial-index, gin]
applies_to: ["**/*.sql"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Query Standards — PostgreSQL (DAT-POSTGRESQL-002)

> This overlay extends [`sdlc/database/query-standards.md`](../query-standards.md). All directives in DAT-003 remain in full effect. Only PostgreSQL-specific directives appear here.

## Purpose

PostgreSQL has specific index types, pagination constraints, and query analysis tools that require explicit conventions beyond the general query standards.

---

## MUST

- **DAT-POSTGRESQL-002-01** `EXPLAIN (ANALYZE, BUFFERS)` is run for any new query that operates on a table with more than 100,000 rows before the query is deployed. The result is reviewed for: sequential scans on large tables, row estimate errors greater than 10x (trigger a statistics refresh), and high buffer hit count.

## MUST NOT

- **DAT-POSTGRESQL-002-02** Use `OFFSET`-based pagination on tables with more than 10,000 rows where more than the first few pages will be accessed. Cursor-based pagination (`WHERE id > :last_id ORDER BY id`) is used instead.

## SHOULD

- **DAT-POSTGRESQL-002-03** Queries that always filter on a low-cardinality condition (e.g. active records, pending jobs) use a partial index (e.g. `CREATE INDEX idx_orders_pending ON orders(created_at) WHERE status = 'pending'`).
- **DAT-POSTGRESQL-002-04** `JSONB` columns queried with `@>`, `?`, or `?|`, and `tsvector` columns used for full-text search, use GIN indexes (`CREATE INDEX ... USING GIN (...)`).
