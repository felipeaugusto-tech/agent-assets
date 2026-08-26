# Observability Phase Standards

**Rule-ID prefix:** `OBS`

## Purpose

Observability standards ensure systems are visible when they are failing, slow, or behaving unexpectedly. Well-instrumented services reduce mean time to detection (MTTD) and mean time to resolution (MTTR) for production incidents.

## Standards in this phase

| File | Rule IDs | Summary |
|---|---|---|
| [`logging.md`](logging.md) | OBS-001 | Structured logging, levels, no PII, correlation IDs |
| [`metrics.md`](metrics.md) | OBS-002 | RED/USE methods, naming, cardinality limits |
| [`tracing.md`](tracing.md) | OBS-003 | Distributed tracing and span conventions |
| [`alerting.md`](alerting.md) | OBS-004 | Actionable alerts, thresholds, on-call routing |
| [`slos.md`](slos.md) | OBS-005 | SLIs, SLOs, and error budgets |
| [`incident-management.md`](incident-management.md) | OBS-006 | Severity levels, runbooks, blameless postmortems |

## Tech overlays

| Technology | Folder | Applies to |
|---|---|---|
| OpenTelemetry | [`opentelemetry/`](opentelemetry/README.md) | All services using OTEL SDK |

## Agent routing note

Load this index first. Then open only the topic file(s) relevant to your task. For OpenTelemetry instrumentation, also open the OTEL overlay.
