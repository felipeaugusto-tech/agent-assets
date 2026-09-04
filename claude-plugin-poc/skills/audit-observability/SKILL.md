---
name: audit-observability
description: Audit a repository's logging, metrics, alerting, SLOs, and incident readiness, and flag reliability risk areas. Manual invocation only.
disable-model-invocation: true
---

# Audit Observability and Reliability

For onboarding as an SRE, prepping a reliability review, or evaluating production readiness before a launch. Read-only against the codebase, one structured report out.

## 1. Fix the target

The target is **the user's current repository**, never this plugin or the GenDD corpus. If the user has SLA/availability targets in mind, get those before analyzing — they change what counts as a gap.

## 2. Load the reference (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/audit-observability/audit-observability.md` | **Primary task flow.** |
| `${CLAUDE_PLUGIN_ROOT}/references/audit-observability/sre.md` | **The actual analysis method** the primary flow delegates to. |

Reading these as they are: verbatim corpus copies, `@GenDD-Flow/...`/`@TargetRepo` links don't resolve here.

## 3. Run the process

1. **Locate observability components** — logging frameworks, metrics exporters, tracing SDKs, alert rules, dashboard definitions, health check endpoints.
2. **Apply the SRE analysis method** from `sre.md` to produce:
   - Logging inventory (structured vs. unstructured, levels, coverage)
   - Metrics and instrumentation (what's measured, what's missing)
   - Alerting rules and thresholds
   - SLO/SLI definitions (existing or recommended)
   - Health check and readiness probe coverage
   - Incident runbook inventory
   - Reliability risk areas (single points of failure, missing retries, no circuit breakers)
3. **Save the report** to `docs/observability-audit.md`.

## 4. Never invent

A "missing alert" or "single point of failure" claim not backed by an actual absence found in the code/config is a guess. If something can't be determined from the repo alone (e.g. actual production alert routing), say so as a limitation.

## 5. Hard limits

- Writes only `docs/observability-audit.md` in the target repository.
- No changes to code, configuration, alerting rules, or infrastructure.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
- Read-only against the codebase throughout.
