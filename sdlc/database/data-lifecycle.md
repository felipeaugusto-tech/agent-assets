---
id: DAT-004
title: Data Lifecycle Standards
phase: database
extends: null
tech: null
summary: Rules for data retention, archival, backups, and restore testing.
tags: [database, retention, archival, backup, restore, disaster-recovery]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Data Lifecycle Standards (DAT-004)

## Purpose

Data retained without a policy accumulates indefinitely, increasing storage costs, breach surface area, and regulatory exposure. Backups that have never been tested frequently fail when they are needed most.

---

## MUST

- **DAT-004-01** Every data type stored by the system has a defined retention period before the system goes to production, sufficient to meet legal/regulatory minimums, no longer than necessary for the operational purpose, and documented in the system's data classification register.
- **DAT-004-02** Database backups are automated with documented backup frequency, retention period, separate storage location (different region or availability zone), and encryption at rest.
- **DAT-004-03** Database restoration is tested at minimum quarterly, verifying that the backup can be retrieved, the database can be restored to a consistent state, and the restored data is intact and queryable. Test results are documented; a failed test triggers immediate investigation and remediation.

## MUST NOT

- **DAT-004-04** Retain personal data beyond its defined retention period. Automated deletion or anonymisation processes are in place for data that reaches its retention limit. See [`pii-handling.md`](pii-handling.md).
