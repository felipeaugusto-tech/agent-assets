---
id: OBS-004
title: Alerting Standards
phase: observability
extends: null
tech: null
summary: Rules for actionable alerts, thresholds, and on-call routing.
tags: [observability, alerting, on-call, thresholds, runbooks, actionable]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Alerting Standards (OBS-004)

## Purpose

Alert fatigue is a leading cause of incidents being missed. An alert that fires and cannot be acted upon trains engineers to ignore alerts. These standards ensure every alert is meaningful and actionable.

---

## MUST

- **OBS-004-01** Every alert has a clear, documented human action to take when it fires, fires only when a human must act immediately, and is suppressable during planned maintenance.
- **OBS-004-02** Every alert includes a `runbook_url` annotation linking to a runbook that describes what the alert means, how to investigate, remediation steps, and the escalation path.
- **OBS-004-03** Alerts are routed to the team that owns the affected service; critical alerts (SLO burn, data loss risk) page the on-call engineer immediately.

## SHOULD

- **OBS-004-04** Service health alerts are based on SLO error budget burn rate rather than raw metric thresholds, using multi-window multi-burn-rate alerting to detect both fast and slow burns.
- **OBS-004-05** Alerts that trigger only auto-remediation without requiring a human are labelled as such and routed to a non-paging channel.
