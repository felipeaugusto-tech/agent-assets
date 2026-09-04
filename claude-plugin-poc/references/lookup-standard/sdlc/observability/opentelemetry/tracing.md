---
id: OBS-OTEL-001
title: Distributed Tracing Standards — OpenTelemetry
phase: observability
extends: sdlc/observability/tracing.md
tech: opentelemetry
summary: Extends OBS-003 with OpenTelemetry SDK instrumentation rules for distributed tracing.
tags: [observability, tracing, opentelemetry, otel, sdk, spans, context-propagation]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Distributed Tracing Standards — OpenTelemetry (OBS-OTEL-001)

> This overlay extends [`sdlc/observability/tracing.md`](../tracing.md). All directives in OBS-003 remain in full effect. Only OpenTelemetry-specific directives appear here.

## Purpose

OpenTelemetry SDK projects require specific initialisation, auto-instrumentation, and naming conventions to produce consistent, interoperable trace data.

---

## MUST

- **OBS-OTEL-001-01** The `TracerProvider` is configured at application startup — before any HTTP servers, consumers, or background jobs start — with the `W3CTraceContextPropagator` as the text map propagator, the appropriate exporter (OTLP, Jaeger, Zipkin, or console for local dev), and a `Resource` containing at minimum `service.name`, `service.version`, and `deployment.environment`.
- **OBS-OTEL-001-02** Where an `opentelemetry-instrumentation-*` library exists for the HTTP framework, database client, or messaging library in use, it is used instead of manual span creation. Manual spans are only added for application-level operations not covered by auto-instrumentation.

## MUST NOT

- **OBS-OTEL-001-03** Replace or reconfigure the global `TracerProvider` after application startup. Tests use an in-memory exporter configured at test startup, not a runtime override of the global provider.

## SHOULD

- **OBS-OTEL-001-04** Custom spans use span names and attribute keys from the OpenTelemetry Semantic Conventions (e.g. `http.request.method`, `db.system`, `db.operation.name`).
