# Observability Phase — OpenTelemetry Overlay

**Tech:** OpenTelemetry
**Rule-ID prefix:** `OBS-OTEL`
**Applies to:** All services using the OpenTelemetry SDK
**Extends:** [`sdlc/observability/`](../README.md)

## Purpose

This overlay extends the agnostic observability standards with OpenTelemetry SDK-specific instrumentation rules for tracing and metrics.

## Files in this overlay

| File | Rule IDs | Summary |
|---|---|---|
| [`tracing.md`](tracing.md) | OBS-OTEL-001 | OpenTelemetry SDK tracing instrumentation rules |
| [`metrics.md`](metrics.md) | OBS-OTEL-002 | OpenTelemetry SDK metrics API and SDK rules |

## How to use

Read the agnostic observability standards first, then read this overlay for OTEL-specific rules.
