---
id: DAT-001
title: Database Schema Design Standards
phase: database
extends: null
tech: null
summary: Rules for data modelling, normalisation, keys, constraints, and naming.
tags: [database, schema, modelling, normalisation, keys, constraints, naming]
applies_to: ["**/*.sql", "**/migrations/**", "**/schema/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Database Schema Design Standards (DAT-001)

## Purpose

Schema design decisions are expensive to reverse after data is stored. These standards prevent the most common schema mistakes that lead to data integrity failures, performance problems, and maintainability issues.

---

## MUST

- **DAT-001-01** Every table has a primary key. Surrogate primary keys (`id` column, auto-incrementing integer or UUID) are preferred over composite natural-key primary keys for tables subject to frequent joins or foreign key references.
- **DAT-001-02** Relationships between tables are expressed as foreign key constraints in the schema, with explicit `ON DELETE` behaviour (`RESTRICT`, `CASCADE`, or `SET NULL`) based on the domain's referential rules.
- **DAT-001-03** Naming conventions: tables in `snake_case` plural noun (e.g. `order_items`); columns in `snake_case` singular (e.g. `created_at`); indexes as `idx_<table>_<columns>`; foreign keys as `fk_<table>_<referenced_table>`; unique constraints as `uq_<table>_<columns>`.
- **DAT-001-04** Columns that must always have a value are declared `NOT NULL`. Default values are specified for non-null columns where a sensible default exists.

## MUST NOT

- **DAT-001-05** Use SQL reserved words (e.g. `order`, `user`, `table`, `select`) as table or column names.

## SHOULD

- **DAT-001-06** Transactional data is normalised to at least 3NF. Denormalisation for performance is a deliberate, documented decision (e.g. in an ADR), applied to read-optimised views or separate reporting tables — not the primary transactional schema.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| PostgreSQL | [`postgresql/schema-design.md`](postgresql/schema-design.md) | `**/*.sql` |
