---
id: DAT-002
title: Database Migration Standards
phase: database
extends: null
tech: null
summary: Rules for safe, reversible, zero-downtime, backward-compatible migrations.
tags: [database, migrations, zero-downtime, rollback, backward-compatible]
applies_to: ["**/migrations/**", "**/*.migration.*", "**/flyway/**", "**/liquibase/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Database Migration Standards (DAT-002)

## Purpose

Migrations that cannot be rolled back or that break running application versions are a primary cause of production incidents. These standards make migrations safe to run in live systems.

---

## MUST

- **DAT-002-01** Every migration includes a rollback (`down`) script that returns the schema to its previous state, tested locally before the migration is committed. Migrations that cannot be made reversible (e.g. dropping a column with non-recoverable data) require a prior data backup step and explicit human approval before execution.
- **DAT-002-02** Migrations are backward-compatible with the version of the application running at the time of migration. Breaking schema changes use the expand-contract pattern: (1) Expand — add the new column/table while keeping the old structure; (2) Migrate — backfill data; (3) Contract — remove the old structure in a subsequent migration only after the new application version is fully deployed. The following operations are prohibited in a migration running during a live deployment: dropping a column or table still referenced by the running application; renaming a column or table; adding a NOT NULL constraint without a default value.
- **DAT-002-03** Migrations are tested against a local database populated with representative data before being committed. Both the `up` and `down` migrations are tested in sequence.

## MUST NOT

- **DAT-002-04** Modify a migration file that has been applied to any environment. A new migration that corrects the issue is created instead.

## SHOULD

- **DAT-002-05** Migrations use `IF NOT EXISTS`, `IF EXISTS`, and `ON CONFLICT DO NOTHING` clauses to be idempotent and safe to re-run after a partial failure.
