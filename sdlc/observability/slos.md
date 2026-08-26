---
id: OBS-005
title: SLI/SLO and Error Budget Standards
phase: observability
extends: null
tech: null
summary: Rules for defining Service Level Indicators, Objectives, and error budgets.
tags: [observability, slo, sli, error-budget, reliability, sre]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# SLI/SLO and Error Budget Standards (OBS-005)

## Purpose

SLOs create a shared, measurable contract between engineering and stakeholders about service reliability. Error budgets give teams a principled framework for balancing reliability with feature velocity.

---

## MUST

- **OBS-005-01** Every service has at least one SLI and corresponding SLO defined, agreed with stakeholders, before it is deployed to production.
- **OBS-005-02** SLIs measure service quality from the user's perspective: Availability (fraction of successful requests), Latency (fraction of requests completed below a threshold), Correctness (for data pipelines), or Throughput (for streaming systems) — not internal system metrics like CPU or memory.
- **OBS-005-03** An error budget policy is defined and communicated to stakeholders, specifying at minimum: what happens when 100% of the error budget is consumed (feature work pauses; reliability work takes priority), and what burn rate triggers an on-call page.

## SHOULD

- **OBS-005-04** SLOs are reviewed at minimum quarterly to assess whether targets are too tight (causing alert fatigue) or too loose (missing real incidents).
