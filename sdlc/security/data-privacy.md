---
id: SEC-005
title: Data Privacy Standards
phase: security
extends: null
tech: null
summary: Privacy-by-design principles, data-subject rights, and data minimisation.
tags: [security, privacy, gdpr, data-minimisation, pii, data-subject-rights]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Data Privacy Standards (SEC-005)

## Purpose

Privacy is a fundamental right and a regulatory requirement in most jurisdictions. These standards embed privacy considerations into the design and implementation of every system that handles personal data.

---

## MUST

- **SEC-005-01** Systems collect only the personal data that is necessary and proportionate to the stated purpose. Data fields are reviewed at design time, and any field whose necessity is uncertain is omitted until necessity is demonstrated.
- **SEC-005-02** All data stored or processed is classified at design time using the organisation's data classification scheme (at minimum: Public, Internal, Confidential, Restricted). Storage, access, and encryption controls are commensurate with the classification.
- **SEC-005-03** Systems that store personal data are designed to support data-subject rights: right of access (retrieve all personal data for a given individual), right to erasure (delete all personal data including from backups where feasible), and right to data portability (export in machine-readable format). These capabilities are designed in from the start.

## MUST NOT

- **SEC-005-04** Use personal data for any purpose that is incompatible with the purpose stated at the time of collection. Secondary uses require compatibility assessment and, where required, additional consent or legal basis.
- **SEC-005-05** Include PII (names, email addresses, phone numbers, national identifiers, health data, financial data, location data) in application logs, distributed traces, or error reports. Use pseudonymous identifiers (user IDs, correlation IDs) in observability data instead.
