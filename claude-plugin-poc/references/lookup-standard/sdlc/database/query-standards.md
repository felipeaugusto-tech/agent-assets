---
id: DAT-003
title: Query Standards
phase: database
extends: null
tech: null
summary: Rules for query performance, indexing, N+1 avoidance, and parameterisation.
tags: [database, queries, performance, indexing, n+1, sql-injection, parameterisation]
applies_to: ["**/*.sql", "**/*.hql", "**/repositories/**", "**/dao/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Query Standards (DAT-003)

## Purpose

Poorly written queries are the primary source of database-related performance incidents and the most common vector for SQL injection.

---

## MUST

- **DAT-003-01** All queries use parameterised queries or prepared statements throughout every data access layer (ORM, raw SQL, query builder). See also [`sdlc/security/input-validation-output-encoding.md`](../security/input-validation-output-encoding.md).
- **DAT-003-02** An index is created — via a migration — for every foreign key column, every column used as the sole or leading filter in a frequent `WHERE` clause on a table expected to grow beyond 10,000 rows, and every column used in `ORDER BY` or `GROUP BY` on large tables.

## MUST NOT

- **DAT-003-03** Use `SELECT *` in application code. Column names are specified explicitly in all production queries.

## SHOULD

- **DAT-003-04** Queries that fetch a collection of records followed by associated data use a JOIN, eager loading, or batch loading strategy. ORM lazy loading on collections accessed in a loop is treated as a code smell and reviewed for N+1 risk.
- **DAT-003-05** `EXPLAIN ANALYZE` (or equivalent) is run for any new query expected to execute on a table with more than 100,000 rows or more than 100 times per second, and full-table scans on large tables are resolved before the query reaches production.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| PostgreSQL | [`postgresql/query-standards.md`](postgresql/query-standards.md) | `**/*.sql` |
