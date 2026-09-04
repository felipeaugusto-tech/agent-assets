---
id: OBS-OTEL-002
title: Metrics Standards — OpenTelemetry
phase: observability
extends: sdlc/observability/metrics.md
tech: opentelemetry
summary: Extends OBS-002 with OpenTelemetry metrics API and SDK rules.
tags: [observability, metrics, opentelemetry, otel, sdk, instruments]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Metrics Standards — OpenTelemetry (OBS-OTEL-002)

> This overlay extends [`sdlc/observability/metrics.md`](../metrics.md). All directives in OBS-002 remain in full effect. Only OpenTelemetry-specific directives appear here.

## Purpose

OpenTelemetry metrics require the correct API, instrument selection, and export configuration to produce accurate, backend-agnostic metric data.

---

## MUST

- **OBS-OTEL-002-01** All metric instrumentation uses the `MeterProvider` API to create instruments. Direct use of Prometheus client libraries in application code is not mixed with OTEL instrumentation.
- **OBS-OTEL-002-02** The correct instrument type is selected for the measurement: `Counter` for values that only increase (requests, errors); `UpDownCounter` or `ObservableGauge` for values that can increase and decrease (active connections, queue depth); `ObservableGauge` for point-in-time measurements (CPU%, memory%); `Histogram` for distributions (request latency, message size).

## SHOULD

- **OBS-OTEL-002-03** Metrics are exported via OTLP to an OTEL Collector, which forwards to the backend (Prometheus, Datadog, etc.), rather than via a separate direct-to-backend client library.
