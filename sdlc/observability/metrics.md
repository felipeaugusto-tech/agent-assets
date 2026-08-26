---
id: OBS-002
title: Metrics Standards
phase: observability
extends: null
tech: null
summary: Rules for RED/USE metrics, naming conventions, and cardinality limits.
tags: [observability, metrics, red, use, cardinality, prometheus, naming]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Metrics Standards (OBS-002)

## Purpose

Metrics are the primary signal for SLO monitoring and alerting. Without standardised metrics, services are invisible to automated monitoring and on-call responders.

---

## MUST

- **OBS-002-01** Every service that handles external requests emits RED metrics: Rate (requests per second as a counter), Errors (error count labelled by code or type), and Duration (request latency histogram with at minimum p50, p95, p99), as separate metric labels per endpoint or operation type.
- **OBS-002-02** Metric names follow the pattern `<service_name>_<subsystem>_<name>_<unit>` — all lowercase `snake_case`, with the base unit as a suffix (e.g. `_seconds`, `_bytes`, `_total`).

## MUST NOT

- **OBS-002-03** Use user IDs, account IDs, session IDs, request IDs, trace IDs, full URL paths, or any free-form string value as metric labels — labels are limited to pre-defined, low-cardinality values (e.g. HTTP status code, endpoint name, error type, region).

## SHOULD

- **OBS-002-04** Infrastructure components (CPU, memory, disk, network, connection pools, queue depths) emit USE metrics: Utilisation (usage as a fraction of capacity), Saturation (queue depth or wait time), and Errors.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| OpenTelemetry | [`opentelemetry/metrics.md`](opentelemetry/metrics.md) | Services using OTEL SDK |
