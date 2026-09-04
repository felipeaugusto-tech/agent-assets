# Role Playbook: Site Reliability Engineer (SRE)

**Role:** Site Reliability Engineer
**Focus:** Observability, SLOs, incident patterns, runbooks
**Time:** 45-60 minutes

---

## Purpose

Analyze a codebase from an SRE perspective to understand:
- Observability implementation (logs, metrics, traces)
- Service level objectives and error budgets
- Incident detection and response capabilities
- Reliability patterns and anti-patterns

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/sre.md
Analyze @TargetRepo for observability and reliability.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/sre.md

Analyze @TargetRepo from an SRE perspective:

## Context
- Monitoring Stack: [Prometheus/Datadog/CloudWatch/etc]
- Logging: [ELK/CloudWatch/Splunk/etc]
- Tracing: [Jaeger/Zipkin/X-Ray/etc]
- Alerting: [PagerDuty/OpsGenie/Slack/etc]
- SLA Requirements: [99.9% / 99.99% / etc]

## Phase 1: Observability Assessment

### Logging
| Aspect | Implementation | Status |
|--------|----------------|--------|
| Log format | [Structured JSON/Text] | Good/Fair/Poor |
| Log levels | [DEBUG/INFO/WARN/ERROR] | Good/Fair/Poor |
| Correlation IDs | [Yes/No] | Good/Missing |
| PII handling | [Masked/None] | Good/Risk |
| Retention | [Duration] | Adequate/Short |

### Metrics
| Category | Metrics Present | Coverage |
|----------|-----------------|----------|
| Request rate | [list] | Full/Partial/None |
| Error rate | [list] | Full/Partial/None |
| Latency (p50, p95, p99) | [list] | Full/Partial/None |
| Saturation | [list] | Full/Partial/None |
| Business metrics | [list] | Full/Partial/None |

### Tracing
| Aspect | Implementation | Coverage |
|--------|----------------|----------|
| Instrumentation | [Auto/Manual/None] | [%] |
| Span creation | [Framework] | [key spans] |
| Cross-service | [Yes/No] | [services] |
| Sampling | [Strategy] | [rate] |

## Phase 2: SLO Analysis

### Current SLIs/SLOs
| Service | SLI | Current SLO | Actual | Error Budget |
|---------|-----|-------------|--------|--------------|
| [API] | Availability | 99.9% | [%] | [remaining] |
| [API] | Latency p99 | <500ms | [ms] | N/A |
| [Worker] | Success rate | 99.5% | [%] | [remaining] |

### SLO Gaps
| Expected SLO | Current State | Gap |
|--------------|---------------|-----|
| [SLO] | Not measured/Partial | [action needed] |

## Phase 3: Alerting Assessment

### Current Alerts
| Alert | Condition | Severity | Notification |
|-------|-----------|----------|--------------|
| High error rate | errors > 5% for 5m | P1 | PagerDuty |
| High latency | p99 > 2s for 10m | P2 | Slack |

### Alert Quality
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Alert-to-incident ratio | [%] | >50% | Good/Poor |
| MTTA (time to ack) | [time] | <5m | Good/Poor |
| MTTR (time to resolve) | [time] | <1h | Good/Poor |
| False positive rate | [%] | <20% | Good/Poor |

### Missing Alerts
| Scenario | Impact | Recommended Alert |
|----------|--------|-------------------|
| [Scenario] | [Impact] | [Alert definition] |

## Phase 4: Incident Response

### Runbook Assessment
| Scenario | Runbook Exists | Last Updated | Tested |
|----------|----------------|--------------|--------|
| Service down | Yes/No | [date] | Yes/No |
| Database issues | Yes/No | [date] | Yes/No |
| High latency | Yes/No | [date] | Yes/No |
| Data corruption | Yes/No | [date] | Yes/No |

### Incident Patterns
| Pattern | Detection | Response Gap |
|---------|-----------|--------------|
| [Pattern] | Auto/Manual | [Gap] |

## Phase 5: Reliability Patterns

### Implemented
| Pattern | Implementation | Effectiveness |
|---------|----------------|---------------|
| Circuit breaker | [Library/Custom/None] | [assessment] |
| Retry with backoff | [Yes/No] | [assessment] |
| Timeout handling | [Yes/No] | [assessment] |
| Graceful degradation | [Yes/No] | [assessment] |
| Rate limiting | [Yes/No] | [assessment] |
| Bulkhead | [Yes/No] | [assessment] |

### Missing Patterns
| Pattern | Risk | Recommendation |
|---------|------|----------------|
| [Pattern] | [Risk] | [Action] |

## Phase 6: Capacity & Performance

### Current Capacity
| Resource | Usage | Threshold | Headroom |
|----------|-------|-----------|----------|
| CPU | [%] | 80% | [%] |
| Memory | [%] | 80% | [%] |
| Connections | [n] | [max] | [%] |
| Storage | [%] | 80% | [%] |

### Scaling Assessment
| Component | Current | Auto-scale | Trigger |
|-----------|---------|------------|---------|
| [Component] | [instances] | Yes/No | [condition] |

## Phase 7: Recommendations

### Critical (P1) - Reliability Risk
| Issue | Impact | Recommendation | Effort |
|-------|--------|----------------|--------|

### Important (P2) - Observability Gap
| Issue | Impact | Recommendation | Effort |
|-------|--------|----------------|--------|

### Improvement (P3) - Best Practice
| Issue | Impact | Recommendation | Effort |
|-------|--------|----------------|--------|
```

---

## Output: SRE Assessment Report

```markdown
# SRE Assessment: [Project Name]
Generated: [Date]
Analyzed by: SRE Playbook

## Reliability Score: [X/10]

## Observability Summary

### Three Pillars Status
| Pillar | Implementation | Coverage | Health |
|--------|----------------|----------|--------|
| Logs | [tool] | [%] | Good/Fair/Poor |
| Metrics | [tool] | [%] | Good/Fair/Poor |
| Traces | [tool] | [%] | Good/Fair/Poor |

## SLO Dashboard

| Service | SLI | SLO | Current | Status |
|---------|-----|-----|---------|--------|
| | | | | |

### Error Budget
```
[Visual representation of error budget consumption]
```

## Alerting Health

### Alert Coverage
- Critical paths covered: [%]
- False positive rate: [%]
- MTTA: [time]
- MTTR: [time]

### Alert Recommendations
1. [Recommendation]

## Runbooks

### Coverage
| Scenario | Status | Link |
|----------|--------|------|

### Gaps
1. [Missing runbook]

## Reliability Patterns

### Implemented
- [x] [Pattern]
- [ ] [Missing pattern]

## Capacity Planning

### Current State
[Analysis]

### Recommendations
1. [Recommendation]

## Action Items

### Immediate (This Week)
- [ ] [Action]

### Short-term (This Quarter)
- [ ] [Action]

### Long-term (Roadmap)
- [ ] [Action]
```

---

## Reference Templates

This playbook's analysis areas align with the universal principles in the Context Pack template. Reference them for baseline expectations:

| Template | Relevant Sections |
|----------|-------------------|
| `templates/context-pack.md` (conventions.md section) | Logging: log levels, structured logging, what to log, what never to log, error logging |
| `templates/context-pack.md` (agents.md section) | Secure error handling (no internal details to clients), dependency security |

---

## Follow-Up Actions

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
