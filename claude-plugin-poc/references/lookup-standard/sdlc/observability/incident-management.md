---
id: OBS-006
title: Incident Management Standards
phase: observability
extends: null
tech: null
summary: Rules for severity levels, runbooks, and blameless postmortem practice.
tags: [observability, incidents, runbooks, postmortem, on-call, severity]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Incident Management Standards (OBS-006)

## Purpose

Incident management standards ensure consistent response to outages, structured learning from failures, and systematic improvement of system reliability over time.

---

## MUST

- **OBS-006-01** Every incident is classified using the severity levels: SEV1 (complete outage, data loss/breach — immediate 24/7 response), SEV2 (significant degradation for majority of users — 15 min business hours / 1 hr outside), SEV3 (partial degradation for subset of users — 4 hours), SEV4 (minor issue, no/minimal user impact — 2 business days).
- **OBS-006-02** A blameless postmortem is conducted for every SEV1 and SEV2 incident within 5 business days of resolution, documenting the event timeline, contributing factors (not a single root cause), distinction between immediate triggers and systemic conditions, and using no language that assigns blame to individuals.
- **OBS-006-03** Every postmortem produces at least one action item that is specific and measurable, has a named owner, has a due date, and is tracked in the team's issue tracker.

## SHOULD

- **OBS-006-04** Every service maintains runbooks for its known failure modes, stored under `docs/runbooks/`, linked from alerts, and updated after every incident that reveals a gap.
