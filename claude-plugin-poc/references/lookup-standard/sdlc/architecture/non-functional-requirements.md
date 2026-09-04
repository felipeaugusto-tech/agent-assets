---
id: ARC-004
title: Non-Functional Requirements Standards
phase: architecture
extends: null
tech: null
summary: Rules for capturing and validating scalability, reliability, performance, and cost NFRs.
tags: [architecture, nfr, performance, scalability, reliability, cost]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Non-Functional Requirements Standards (ARC-004)

## Purpose

Systems without explicit NFRs are routinely discovered to be too slow, too fragile, or too expensive only after they reach production. These standards ensure NFRs are defined upfront, measured, and verified.

## Required NFR categories for new services

Performance (p50/p95/p99 targets at stated RPS), Availability (uptime SLO), Scalability (peak load and headroom), Durability/Data retention (backup and archival), Recovery (RTO and RPO), Security (auth and data classification), Compliance (regulatory and data-residency), Cost (infrastructure budget at stated load).

---

## MUST

- **ARC-004-01** NFRs are defined before architecture design begins for any new service or for any feature with significant performance, reliability, or cost implications.
- **ARC-004-02** Every NFR is expressed in measurable form: e.g. "p99 response time < 200ms at 500 RPS" (not "the system should be fast"); "99.9% uptime measured monthly" (not "high availability"); "RTO < 1 hour, RPO < 15 minutes" (not "recoverable from failure").
- **ARC-004-03** NFRs relevant to a feature are listed in that feature's Definition of Done and verified before the feature is marked done.

## MUST NOT

- **ARC-004-04** Accept qualitative NFR statements (e.g. "fast", "reliable", "scalable", "cost-effective") as complete requirements.

## SHOULD

- **ARC-004-05** Performance and scalability NFRs are validated via automated load or performance tests that run in a staging environment before production release.
