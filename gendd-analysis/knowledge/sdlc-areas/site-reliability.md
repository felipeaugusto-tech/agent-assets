# Site Reliability -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Site Reliability lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Monitoring/metrics configuration | HIGH | Prometheus config, Datadog agent config, `metrics/`, `monitoring/` |
| Health check endpoints | HIGH | `/health`, `/ready`, `/healthz`, `/readyz` in routes |
| Alerting configuration | HIGH | Alert rules in YAML, PagerDuty/OpsGenie integration, alert manager config |
| Structured logging implementation | MEDIUM | Winston, Serilog, Zap, structlog config with JSON format |
| Circuit breaker or resilience library | MEDIUM | Polly, resilience4j, `gobreaker`, `cockatiel` imports |
| SLO/SLI definitions | MEDIUM | SLO config files, error budget dashboards, SLI metric definitions |
| Runbook or incident documentation | MEDIUM | `runbooks/`, `docs/incidents/`, on-call documentation |
| Tracing instrumentation | MEDIUM | OpenTelemetry, Jaeger, Zipkin, X-Ray SDK imports |
| Auto-scaling configuration | LOW | HPA manifests, auto-scaling group config, scaling policies |
| Chaos engineering config | LOW | Chaos Monkey, Litmus, Gremlin configuration files |

## What to Analyze

### Observability -- Logging
- Look for: Log format (structured JSON vs. plain text)
- Look for: Log level usage (DEBUG, INFO, WARN, ERROR) and consistency
- Look for: Correlation ID implementation for request tracing
- Look for: PII handling in logs (masking, filtering)
- Look for: Log retention and rotation configuration
- Assess: Whether logs provide enough information for troubleshooting
- Document: Logging implementation summary with format, levels, correlation, and PII handling

### Observability -- Metrics
- Look for: RED metrics (Request rate, Error rate, Duration)
- Look for: USE metrics (Utilization, Saturation, Errors) for resources
- Look for: Business metrics (transactions, conversions, active users)
- Look for: Custom metric definitions and instrumentation points
- Assess: Whether metrics cover the four golden signals
- Document: Metrics inventory by category with coverage assessment

### Observability -- Tracing
- Look for: Distributed tracing instrumentation (auto vs. manual)
- Look for: Span creation patterns and context propagation
- Look for: Cross-service trace correlation
- Look for: Sampling strategy configuration
- Assess: Tracing coverage across services
- Document: Tracing implementation with instrumentation type, coverage, and sampling

### SLO Analysis
- Look for: Defined Service Level Indicators (SLIs) -- availability, latency, throughput
- Look for: Service Level Objectives (SLOs) -- target values for each SLI
- Look for: Error budget tracking mechanism
- Look for: SLO-based alerting (burn rate alerts)
- Assess: Whether SLOs exist, are measurable, and are tracked
- Document: SLI/SLO table with current values, targets, and error budget status

### Alerting Assessment
- Look for: Alert rule definitions (conditions, severity, notification channels)
- Look for: Alert quality indicators (alert-to-incident ratio, false positive rate)
- Look for: Mean time to acknowledge (MTTA) and mean time to resolve (MTTR) indicators
- Look for: Escalation paths and on-call configuration
- Assess: Whether alerting is actionable or noisy
- Document: Alert inventory with conditions, severity, notification, and quality assessment

### Incident Response
- Look for: Runbook documentation for common scenarios (service down, high latency, data issues)
- Look for: Incident response process documentation
- Look for: Post-incident review (PIR) or post-mortem templates
- Look for: Incident communication channels and escalation paths
- Assess: Runbook coverage, freshness, and whether they have been tested
- Document: Runbook inventory with scenario, existence, last update, and test status

### Reliability Patterns
- Look for: Circuit breaker implementations
- Look for: Retry with exponential backoff
- Look for: Timeout handling on external calls
- Look for: Graceful degradation (fallback responses, feature flags)
- Look for: Rate limiting implementation
- Look for: Bulkhead pattern (isolation of failure domains)
- Assess: Which patterns are implemented and which are missing
- Document: Reliability pattern checklist with implementation status and effectiveness

### Capacity and Performance
- Look for: Current resource utilization (CPU, memory, connections, storage)
- Look for: Auto-scaling configuration and triggers
- Look for: Connection pool sizing and management
- Look for: Performance benchmarks or load test configuration
- Assess: Headroom and scaling readiness
- Document: Capacity assessment with current usage, thresholds, and scaling approach

## Key Questions to Answer

1. Are the three pillars of observability (logs, metrics, traces) implemented?
2. What SLIs/SLOs are defined and are they being tracked?
3. Are alerts actionable and is the false positive rate manageable?
4. Do runbooks exist for common failure scenarios and are they tested?
5. What reliability patterns (circuit breaker, retry, timeout) are implemented?
6. What is the current capacity headroom and scaling strategy?
7. How is incident response organized and what are the escalation paths?
8. Is there correlation between logs, metrics, and traces for debugging?
9. What are the MTTA and MTTR for incidents?
10. What reliability improvements would have the highest impact?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Comprehensive Observability | All three pillars implemented with correlation | Mature reliability practice, fast incident resolution |
| Alert-Only Monitoring | Alerts defined but no dashboards or SLOs | Reactive, not proactive reliability |
| Log-Only Observability | Structured logging but no metrics or traces | Limited visibility, slow debugging |
| SLO-Based Operations | Error budgets tracked, burn-rate alerts | Mature SRE practice |
| Chaos Engineering Practice | Chaos experiments defined, game day documentation | Proactive resilience testing |
| On-Call Rotation | PagerDuty/OpsGenie schedules, escalation policies | Defined incident response |
| Feature Flag Degradation | Feature flags with fallback behavior | Graceful degradation capability |
| Health Check Cascade | Health endpoints checking downstream dependencies | Accurate readiness signaling |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No health check endpoints | Missing `/health`, `/ready` routes | HIGH |
| No monitoring or metrics | No metrics library, no monitoring config | HIGH |
| No alerting configured | No alert rules, no notification integration | HIGH |
| Missing circuit breakers on external calls | Direct HTTP calls without resilience library | MEDIUM |
| No structured logging | Plain text logs, inconsistent format | MEDIUM |
| No SLOs defined | No availability or latency targets documented | MEDIUM |
| No runbooks | Missing incident response documentation | MEDIUM |
| No log correlation IDs | Cannot trace requests across services | MEDIUM |
| PII in logs | Unmasked personal data in log output | HIGH |
| No auto-scaling | Fixed instance count, no scaling policy | LOW |

## Output Guidance

### Must Include
- Observability assessment across all three pillars (logs, metrics, traces) with coverage rating
- SLI/SLO inventory with current values and targets
- Alerting health assessment with quality indicators
- Reliability patterns checklist with implementation status
- Top reliability risks with recommended mitigations

### Should Include (if detected)
- Runbook inventory with coverage and freshness assessment
- Capacity planning analysis with headroom and scaling approach
- Incident response process assessment
- MTTA/MTTR indicators
- Performance benchmark or load test results

### Related Areas
- [devops-infrastructure](./devops-infrastructure.md) -- deployment infrastructure, CI/CD, container strategy
- [architecture](./architecture.md) -- system architecture affecting reliability
- [security](./security.md) -- secure logging, PII handling
- [backend-development](./backend-development.md) -- error handling, external call patterns
- [support-engineering](./support-engineering.md) -- troubleshooting, error messages, diagnostic endpoints
