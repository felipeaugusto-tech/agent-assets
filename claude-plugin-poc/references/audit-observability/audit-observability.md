# Audit Observability and Reliability

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | SRE, DevOps Engineer, Tech Lead |
| **Prerequisites** | Repository cloned, access to application code and infrastructure config |
| **Inputs** | Path to the target repository |
| **Outputs** | Observability audit covering logging, metrics, alerting, SLOs, and incident readiness |

## When to Use

- Onboarding as an SRE and need to assess production readiness
- Preparing for a reliability review or incident retrospective
- Evaluating whether the system has adequate observability before a launch

## Before You Start

- [ ] Repository is cloned and accessible
- [ ] You can identify logging, metrics, and alerting configuration
- [ ] You have context on the system's SLAs or expected availability targets

## Steps

1. **Identify observability components**
   - Do: Locate all logging, metrics, tracing, and alerting configuration
   - How: Search for logging frameworks, metrics exporters, tracing SDKs, alert rules, dashboard definitions, and health check endpoints
   - Expect: An inventory of observability tooling in use

2. **Run the SRE role-playbook analysis**
   - Do: Perform a role-specific deep analysis of reliability and observability
   - How: Use the following prompt:
     ```
     Read @GenDD-Flow/playbooks/by-role/sre.md

     Analyze @TargetRepo focusing on observability and reliability.

     Generate:
     1. Logging inventory (structured vs unstructured, levels, coverage)
     2. Metrics and instrumentation (what's measured, what's missing)
     3. Alerting rules and thresholds
     4. SLO/SLI definitions (existing or recommended)
     5. Health check and readiness probe coverage
     6. Incident runbook inventory
     7. Reliability risk areas (single points of failure, missing retries, no circuit breakers)
     ```
   - Expect: A comprehensive observability and reliability audit

3. **Document findings**
   - Do: Save the audit as a structured report
   - How: Save to `@TargetRepo/docs/observability-audit.md`
   - Expect: Actionable reliability improvement plan

## Expected Output

```
TargetRepo/docs/
└── observability-audit.md
```

**Save to:** `@TargetRepo/docs/observability-audit.md`

## What's Next

- [ ] [Audit CI/CD Pipeline](audit-ci-cd-pipeline.md) to review deployment safety
- [ ] [Run Delta Analysis](run-delta-analysis.md) after implementing reliability improvements

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| SRE Role Playbook | `playbooks/by-role/sre.md` | Deep-dive SRE analysis prompt |
| DevOps Role Playbook | `playbooks/by-role/devops-engineer.md` | Infrastructure analysis prompt |
