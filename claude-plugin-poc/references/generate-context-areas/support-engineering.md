# Support Engineering -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Support Engineering lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Error message definitions | HIGH | Error constants, error enums, error message files, HTTP status code mappings |
| Health check endpoints | HIGH | `/health`, `/ready`, `/status`, `/ping` routes |
| Logging configuration | HIGH | Winston, Serilog, Zap, structlog config with multiple levels |
| Configuration files with user-facing settings | MEDIUM | `.env.example`, config documentation, admin settings |
| FAQ or troubleshooting docs | MEDIUM | `docs/troubleshooting.md`, `FAQ.md`, `docs/support/` |
| Diagnostic or admin endpoints | MEDIUM | `/admin/`, `/debug/`, `/diagnostics/` routes |
| Error tracking integration | MEDIUM | Sentry, Bugsnag, Rollbar, Application Insights SDK |
| User notification system | LOW | Email templates, notification services, alert components |
| Feedback or support ticket integration | LOW | Zendesk, Intercom, support widget config |

## What to Analyze

### Error and Message Inventory
- Look for: All user-facing error messages with their codes and locations
- Look for: Error categorization (authentication, validation, permission, server, integration)
- Look for: Error message clarity (does the message tell the user what to do?)
- Look for: Internationalized vs. hardcoded error messages
- Assess: Whether error messages help users self-resolve or require support intervention
- Document: Error inventory by category with message, location, meaning, and user action

### Configuration Analysis
- Look for: All user-configurable settings with their locations and defaults
- Look for: Environment variables with documentation
- Look for: Configuration validation (what happens with invalid config?)
- Look for: Common misconfiguration scenarios and their symptoms
- Assess: Whether configuration is well-documented and error-resistant
- Document: Configuration reference with setting, location, default, description, and impact

### Logging and Diagnostics
- Look for: Log file locations and formats
- Look for: Log level configuration and what each level captures
- Look for: Key log patterns that indicate specific issues
- Look for: Correlation IDs for request tracing
- Look for: Diagnostic endpoints or admin tools
- Assess: Whether logs provide enough information for troubleshooting
- Document: Logging reference with locations, levels, key patterns, and diagnostic tools

### Common Issues Analysis
- Look for: Error handling patterns that reveal likely failure scenarios
- Look for: External dependency failures and their user-facing symptoms
- Look for: Resource exhaustion scenarios (connection pool, memory, disk)
- Look for: Race conditions or timing-dependent behavior
- Assess: What the most common support scenarios would be based on code analysis
- Document: Common issue inventory with evidence, symptoms, and resolution steps

### Health Check and Status
- Look for: Health check endpoint implementation (liveness vs. readiness)
- Look for: What systems are checked (database, cache, external services)
- Look for: Status indicators visible to users or operators
- Assess: Whether health checks provide actionable information
- Document: Health check inventory with endpoint, purpose, and expected response

### Integration Points (Support View)
- Look for: External dependency list and their failure modes
- Look for: What users see when an external dependency fails
- Look for: Workarounds available when integrations are unavailable
- Look for: Timeout and retry configuration for external calls
- Assess: How gracefully the system handles integration failures
- Document: Integration failure matrix with dependency, symptoms, workaround, and resolution

### Troubleshooting Flows
- Look for: Decision trees for common issues (if X, check Y, then try Z)
- Look for: Escalation paths (L1 support to L2 to engineering)
- Look for: Self-service resolution options (reset password, clear cache, retry)
- Assess: Whether troubleshooting can be structured into repeatable flows
- Document: Troubleshooting flow diagrams for top 3-5 likely issues

### Support Documentation Gaps
- Look for: Missing troubleshooting guides
- Look for: Missing FAQ sections
- Look for: Missing known issues documentation
- Look for: Missing configuration guide for end users
- Assess: What documentation would most reduce support ticket volume
- Document: Support doc gap inventory prioritized by expected ticket reduction

### Supportability Assessment
- Look for: Error message quality (actionable vs. generic)
- Look for: Self-service capabilities (password reset, retry mechanisms, status pages)
- Look for: Admin tools for support engineers (user lookup, log access, config override)
- Look for: Audit trail for support investigations (who did what, when)
- Assess: Overall supportability maturity
- Document: Supportability assessment with strengths, gaps, and improvement recommendations

## Key Questions to Answer

1. What error messages does the user see and are they actionable?
2. What configuration options exist and what are common misconfigurations?
3. Where are the logs and what patterns indicate specific issues?
4. What are the likely common support issues based on code analysis?
5. What health check and diagnostic endpoints exist?
6. How does the system behave when external dependencies fail?
7. What troubleshooting flows can be built for common issues?
8. What support documentation is missing?
9. What self-service resolution options exist?
10. What would most reduce support ticket volume?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Good Error UX | Specific error messages, error codes, user action guidance | Low support ticket volume for known errors |
| Generic Error Messages | "Something went wrong", "Internal error" without context | High support volume, user frustration |
| Self-Service Capability | Password reset, retry buttons, status page, troubleshooting wizard | Users can resolve without support |
| No Self-Service | All issues require contacting support | High support load, user frustration |
| Comprehensive Logging | Structured JSON logs, correlation IDs, error context | Fast support resolution |
| Poor Logging | Unstructured text logs, no correlation, missing context | Slow investigation, guesswork |
| Admin Tools | Support admin panel, user lookup, config management | Efficient support operations |
| No Admin Tools | Database-only access for support investigations | Slow, error-prone support |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| Generic error messages with no user guidance | "Error occurred" without code or action steps | HIGH |
| No health check endpoints | Missing `/health` or `/ready` routes | HIGH |
| No logging configuration | Missing structured logging setup | HIGH |
| Sensitive data in error messages | Stack traces, DB queries, internal paths shown to users | HIGH |
| No configuration documentation | Missing `.env.example` or config reference | MEDIUM |
| No error tracking integration | Missing Sentry/Bugsnag/Rollbar | MEDIUM |
| Hardcoded error messages (no i18n) | String literals in code without localization | LOW |
| No diagnostic endpoints | No admin or debug tools for investigations | MEDIUM |
| No known issues documentation | Missing known issues list or FAQ | LOW |
| Silent failure on integration errors | External service fails without user notification | MEDIUM |

## Output Guidance

### Must Include
- Error message inventory by category with clarity assessment
- Configuration reference with settings, defaults, and common misconfigurations
- Health check endpoint inventory
- Logging reference with locations, levels, and key patterns
- Top 3-5 likely common issues with troubleshooting steps

### Should Include (if detected)
- Integration failure matrix with symptoms and workarounds
- Troubleshooting flow diagrams for common issues
- Support documentation gap assessment
- Supportability maturity evaluation
- Self-service capability inventory
- Recommendations for reducing support ticket volume

### Related Areas
- [site-reliability](./site-reliability.md) -- monitoring, alerting, incident response
- [backend-development](./backend-development.md) -- error handling patterns, API error responses
- [security](./security.md) -- sensitive data in error messages, audit logging
- [technical-writing](./technical-writing.md) -- troubleshooting guides, FAQ, user documentation
- [release-management](./release-management.md) -- known issues, release notes for support team
- [devops-infrastructure](./devops-infrastructure.md) -- log forwarding, monitoring hooks
