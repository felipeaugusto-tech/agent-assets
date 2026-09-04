---
id: DAT-005
title: PII Handling in Databases
phase: database
extends: null
tech: null
summary: Rules for data classification, minimisation, and masking of PII in databases.
tags: [database, pii, data-classification, masking, privacy, encryption]
applies_to: ["**/*.sql", "**/migrations/**", "**/schema/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# PII Handling in Databases (DAT-005)

## Purpose

PII in databases is the highest-risk data exposure vector. These rules complement [`sdlc/security/data-privacy.md`](../security/data-privacy.md) with database-specific controls.

---

## MUST

- **DAT-005-01** Columns storing PII are annotated with their classification in the schema documentation (e.g. `PII:Contact`, `PII:Financial`, `PII:Health`). Column comments in the database include the classification.
- **DAT-005-02** PII is not present in unmasked form in non-production databases. Non-production data is either synthetically generated (preferred) or masked/pseudonymised via an automated masking pipeline. Manual or ad hoc scrubbing of production exports is not acceptable.

## MUST NOT

- **DAT-005-03** Store PII in plaintext in audit log tables, change history tables, or application log tables. If PII must be captured in audit tables for legal reasons, it is encrypted using the same controls as the primary data.

## SHOULD

- **DAT-005-04** High-sensitivity PII fields (national identifiers, financial account numbers, health data) use application-level field encryption before storage. Encrypted values are not directly queryable — a secondary index on a non-reversible hash is used if filtering on the encrypted field is required.
