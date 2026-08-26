# Role Playbook: Security Engineer

**Role:** Security Engineer
**Focus:** Security scan, OWASP checklist, auth/authz review, vulnerability assessment
**Time:** 45-60 minutes

---

## Purpose

Analyze a codebase from a Security Engineer perspective to understand:
- Security posture and vulnerabilities
- Authentication and authorization implementation
- OWASP Top 10 compliance
- Secret management practices
- Security-related configurations

---

## {ORGANIZATION} Security Standards in Story Lifecycle

> **Reference:** This playbook aligns with {ORGANIZATION}'s **Story Templates** and **Definition of Ready/Done** for security considerations.

### Security Flags in Epics & Stories

Epics and Stories must identify security review needs as part of Definition of Ready:

| Security Flag | Description | Triggers Security Review |
|---------------|-------------|-------------------------|
| **PCI** | Payment Card Industry data involved | Yes |
| **PII** | Personally Identifiable Information | Yes |
| **Auth** | Authentication or authorization changes | Yes |
| **Payments** | Payment processing or financial data | Yes |

### Security Review in Definition of Done

For stories flagged with security concerns, DoD includes:

- [ ] Security concerns identified earlier are addressed or approved
- [ ] No new security vulnerabilities introduced
- [ ] PCI/PII handling follows established patterns
- [ ] Auth/authz changes reviewed by security

### Anti-Patterns This Addresses

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Security discovered late | "In Secure Code Review" status blocks release | Flag security review need in DoR |
| Implicit security assumptions | Tribal knowledge about security patterns | Document in Story Integration & Risk Flags |
| Undocumented PCI scope | Compliance risk | Explicit PCI flag in Epic/Story |

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/security-engineer.md
Analyze @TargetRepo for security posture.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/security-engineer.md

Analyze @TargetRepo from a Security Engineer perspective:

## Context
- Application Type: [Web | API | Mobile | Desktop]
- Auth Method: [JWT | Session | OAuth | API Keys]
- Sensitive Data: [PCI | PII | PHI | Financial]
- Compliance: [SOC2 | PCI-DSS | HIPAA | GDPR | None]

## Phase 1: Authentication Review

### Current Implementation
| Aspect | Implementation | Status |
|--------|----------------|--------|
| Auth method | [JWT/Session/OAuth] | [assessment] |
| Password policy | [Requirements] | Strong/Weak/None |
| MFA support | [Yes/No/Optional] | [assessment] |
| Session management | [Mechanism] | [assessment] |
| Token storage | [Where] | Secure/Risk |
| Token expiry | [Duration] | Appropriate/Too long |

### Auth Flow Analysis
| Flow | Implementation | Vulnerabilities |
|------|----------------|-----------------|
| Login | [mechanism] | [findings] |
| Logout | [mechanism] | [findings] |
| Password reset | [mechanism] | [findings] |
| Session refresh | [mechanism] | [findings] |

## Phase 2: Authorization Review

### Current Model
| Aspect | Implementation | Status |
|--------|----------------|--------|
| Model | [RBAC/ABAC/Custom] | [assessment] |
| Permission checks | [Middleware/Inline/Decorator] | Consistent/Inconsistent |
| Role definitions | [Where defined] | [location] |
| Resource-level auth | [Yes/No] | [assessment] |

### Authorization Gaps
| Resource | Expected Auth | Actual Auth | Risk |
|----------|---------------|-------------|------|
| [Endpoint] | [Expected] | [Actual] | High/Med/Low |

## Phase 3: OWASP Top 10 Assessment

| Vulnerability | Status | Evidence | Risk |
|---------------|--------|----------|------|
| A01: Broken Access Control | Pass/Fail/Partial | [files/findings] | |
| A02: Cryptographic Failures | Pass/Fail/Partial | [files/findings] | |
| A03: Injection | Pass/Fail/Partial | [files/findings] | |
| A04: Insecure Design | Pass/Fail/Partial | [files/findings] | |
| A05: Security Misconfiguration | Pass/Fail/Partial | [files/findings] | |
| A06: Vulnerable Components | Pass/Fail/Partial | [files/findings] | |
| A07: Auth Failures | Pass/Fail/Partial | [files/findings] | |
| A08: Software/Data Integrity | Pass/Fail/Partial | [files/findings] | |
| A09: Logging/Monitoring Failures | Pass/Fail/Partial | [files/findings] | |
| A10: SSRF | Pass/Fail/Partial | [files/findings] | |

## Phase 4: Secret Management

### Secrets Inventory
| Secret Type | Storage | Rotation | Access Control |
|-------------|---------|----------|----------------|
| Database creds | [Vault/Env/Config] | [Policy] | [Who] |
| API keys | [Vault/Env/Config] | [Policy] | [Who] |
| Encryption keys | [Vault/HSM/Config] | [Policy] | [Who] |
| Service accounts | [Vault/Env/Config] | [Policy] | [Who] |

### Secret Scanning
| Check | Result | Files |
|-------|--------|-------|
| Hardcoded secrets | Found/Clean | [files] |
| .env in git | Found/Clean | [status] |
| gitignore coverage | Complete/Gaps | [missing] |

## Phase 5: Input Validation

### Current State
| Input Type | Validation | Sanitization | Status |
|------------|------------|--------------|--------|
| User input | [Method] | [Method] | Good/Risk |
| File uploads | [Method] | [Method] | Good/Risk |
| API parameters | [Method] | [Method] | Good/Risk |
| Query strings | [Method] | [Method] | Good/Risk |

### Injection Points
| Location | Type | Protection | Status |
|----------|------|------------|--------|
| [location] | SQL | Parameterized | Safe/Risk |
| [location] | XSS | Output encoding | Safe/Risk |
| [location] | Command | [Protection] | Safe/Risk |

## Phase 6: Data Protection

### Encryption
| Data | At Rest | In Transit | Status |
|------|---------|------------|--------|
| User data | [Method] | TLS 1.2+ | Good/Risk |
| Passwords | [Hash algo] | TLS 1.2+ | Good/Risk |
| PII | [Method] | TLS 1.2+ | Good/Risk |
| Backups | [Method] | [Method] | Good/Risk |

### Data Handling
| Practice | Implementation | Status |
|----------|----------------|--------|
| PII masking in logs | [Yes/No] | Good/Risk |
| Data retention policy | [Policy] | Compliant/Gap |
| Right to deletion | [Implemented] | Compliant/Gap |

## Phase 7: Dependency Security

### Vulnerability Scan Results
| Severity | Count | Critical Examples |
|----------|-------|-------------------|
| Critical | [n] | [packages] |
| High | [n] | [packages] |
| Medium | [n] | [packages] |
| Low | [n] | - |

### Dependency Management
| Practice | Status |
|----------|--------|
| Lock file present | Yes/No |
| Automated scanning | [Tool] |
| Update policy | [Policy] |

## Phase 8: Security Headers & Config

### HTTP Headers
| Header | Value | Status |
|--------|-------|--------|
| Content-Security-Policy | [value] | Present/Missing |
| X-Frame-Options | [value] | Present/Missing |
| X-Content-Type-Options | [value] | Present/Missing |
| Strict-Transport-Security | [value] | Present/Missing |
| X-XSS-Protection | [value] | Present/Missing |

### Configuration
| Setting | Current | Recommended | Status |
|---------|---------|-------------|--------|
| Debug mode | [state] | Off in prod | Good/Risk |
| Error details | [state] | Hidden in prod | Good/Risk |
| CORS | [policy] | Restrictive | Good/Risk |

## Phase 9: Recommendations

### Critical (Fix Immediately)
| Finding | Risk | Recommendation | Files |
|---------|------|----------------|-------|

### High (Fix This Sprint)
| Finding | Risk | Recommendation | Files |
|---------|------|----------------|-------|

### Medium (Plan to Fix)
| Finding | Risk | Recommendation | Files |
|---------|------|----------------|-------|

### Low (Best Practice)
| Finding | Risk | Recommendation | Files |
|---------|------|----------------|-------|
```

---

## Output: Security Assessment Report

```markdown
# Security Assessment: [Project Name]
Generated: [Date]
Analyzed by: Security Engineer Playbook

## Security Score: [X/10]

## Executive Summary
[2-3 sentence summary of security posture]

## Critical Findings
| Finding | Risk | Impact | Remediation |
|---------|------|--------|-------------|

## Authentication & Authorization

### Auth Summary
- Method: [JWT/Session/etc]
- MFA: [Yes/No]
- Session management: [assessment]

### Gaps
1. [Gap]

## OWASP Top 10 Status

| Category | Status | Priority |
|----------|--------|----------|
| A01: Broken Access Control | | |
| ... | | |

## Secret Management

### Current State
[Assessment]

### Recommendations
1. [Recommendation]

## Dependency Vulnerabilities

### Critical/High Findings
| Package | Vulnerability | Fix |
|---------|---------------|-----|

## Security Headers

### Missing/Misconfigured
| Header | Current | Required |
|--------|---------|----------|

## Remediation Roadmap

### Immediate (This Week)
- [ ] [Critical fix]

### Short-term (This Month)
- [ ] [High priority fix]

### Long-term (This Quarter)
- [ ] [Medium priority improvement]
```

---

## Reference Templates

This playbook's analysis areas align with the universal principles in the Context Pack template. Reference them for baseline expectations when evaluating findings:

| Template | Relevant Sections |
|----------|-------------------|
| `templates/context-pack.md` (agents.md section) | Security rules: secrets handling, input validation, multi-tenant isolation, secure error handling, auth/authz, dependency security, what never to log |
| `templates/context-pack.md` (conventions.md section) | Logging: what never to log (PII, credentials, card data), log levels. Code quality: error handling, DI |

---

## Follow-Up Actions

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
