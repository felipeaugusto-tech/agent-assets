# Security -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Security lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Authentication middleware/configuration | HIGH | `auth/`, JWT config, OAuth setup, Passport.js, IdentityServer |
| Security headers configuration | HIGH | Helmet.js, security middleware, CSP config |
| Encryption/hashing libraries | HIGH | bcrypt, argon2, crypto imports, certificate files |
| RBAC/ABAC permission definitions | MEDIUM | `roles/`, `permissions/`, policy files, authorization guards |
| Secret management integration | MEDIUM | Vault client, AWS Secrets Manager SDK, Azure Key Vault |
| Security scanning config in CI | MEDIUM | Snyk, Dependabot, CodeQL, SonarQube, Trivy config |
| Input validation libraries | MEDIUM | Joi, Zod, class-validator, FluentValidation imports |
| CORS configuration | LOW | `cors()` middleware, CORS policy definitions |
| Rate limiting configuration | LOW | Rate limiter middleware, throttle decorators |
| Audit logging | LOW | Audit trail tables, security event logging |

## What to Analyze

### Authentication Review
- Look for: Auth method (JWT, session-based, OAuth 2.0, SAML, API keys)
- Look for: Password policy enforcement (complexity, length, history)
- Look for: Multi-factor authentication support
- Look for: Session management (duration, rotation, invalidation)
- Look for: Token storage approach and expiry configuration
- Look for: Account lockout mechanism
- Assess: Security of each auth flow (login, logout, password reset, session refresh)
- Document: Auth implementation with method, flows, and vulnerability findings

### Authorization Review
- Look for: Permission model (RBAC, ABAC, custom, ACL)
- Look for: Permission check consistency across endpoints
- Look for: Role definitions and where they are stored
- Look for: Resource-level authorization (not just route-level)
- Look for: API endpoint authorization matrix
- Assess: Whether all protected resources have appropriate authorization checks
- Document: Authorization model with gaps where endpoints lack proper checks

### OWASP Top 10 Assessment
- Look for: Broken Access Control -- missing auth checks, IDOR vulnerabilities
- Look for: Cryptographic Failures -- weak algorithms, improper key management
- Look for: Injection -- SQL injection, command injection, XSS via unescaped output
- Look for: Insecure Design -- missing threat modeling, no security requirements
- Look for: Security Misconfiguration -- debug mode in production, default credentials
- Look for: Vulnerable Components -- outdated dependencies with known CVEs
- Look for: Authentication Failures -- weak credentials, no brute force protection
- Look for: Software/Data Integrity -- unsigned updates, untrusted deserialization
- Look for: Logging/Monitoring Failures -- missing security event logging
- Look for: SSRF -- unvalidated URLs in server-side requests
- Document: OWASP Top 10 assessment table with pass/fail/partial per category

### Secret Management
- Look for: How secrets are stored (environment variables, Vault, cloud secret managers, config files)
- Look for: Hardcoded secrets in source code (API keys, passwords, connection strings)
- Look for: `.env` files committed to git
- Look for: `.gitignore` coverage for sensitive files
- Look for: Secret rotation policies and mechanisms
- Look for: Access control on secrets (who can read which secrets)
- Assess: Whether secrets are properly managed and not exposed
- Document: Secret inventory with storage method, rotation policy, and exposure risks

### Input Validation
- Look for: Validation on user input (forms, API parameters, query strings)
- Look for: File upload validation (type, size, content)
- Look for: Sanitization of output to prevent XSS
- Look for: Parameterized queries for SQL injection prevention
- Look for: Command injection protection
- Assess: Whether all input vectors are validated and sanitized
- Document: Input validation coverage by input type with protection status

### Data Protection
- Look for: Encryption at rest (database encryption, file encryption)
- Look for: Encryption in transit (TLS configuration, certificate management)
- Look for: Password hashing algorithm (bcrypt, argon2, PBKDF2 vs. MD5/SHA1)
- Look for: PII handling practices (masking in logs, data retention, right to deletion)
- Look for: Sensitive data in backups (encryption, access control)
- Assess: Data protection posture across storage, transit, and processing
- Document: Data protection assessment with encryption methods and PII handling practices

### Dependency Security
- Look for: Lock file presence (package-lock.json, yarn.lock, go.sum)
- Look for: Automated vulnerability scanning (Dependabot, Snyk, npm audit)
- Look for: Dependency update policy
- Look for: Critical/high severity vulnerabilities in current dependencies
- Assess: Dependency management maturity and current vulnerability exposure
- Document: Dependency security summary with scanning tool, vulnerability count by severity, and update policy

### Security Headers and Configuration
- Look for: Content-Security-Policy header
- Look for: X-Frame-Options header
- Look for: X-Content-Type-Options header
- Look for: Strict-Transport-Security header
- Look for: CORS policy (permissive vs. restrictive)
- Look for: Debug mode and error detail exposure in production config
- Assess: Whether security headers follow best practices
- Document: Security header checklist with current values and recommended settings

### Security in SDLC
- Look for: Security flags in story/epic templates (PCI, PII, auth, payments)
- Look for: Security review gates in the development process
- Look for: Threat modeling artifacts
- Look for: Security testing in CI pipeline (SAST, DAST)
- Assess: Whether security is shifted left or discovered late
- Document: Security in SDLC assessment with gate coverage and shift-left maturity

## Key Questions to Answer

1. What authentication method is used and is it securely implemented?
2. Is authorization consistently enforced across all protected resources?
3. How does the application perform against the OWASP Top 10?
4. Are secrets properly managed and not exposed in source code?
5. Is input validation applied to all user-controlled data?
6. How is sensitive data protected at rest and in transit?
7. What dependency vulnerabilities currently exist?
8. Are security headers properly configured?
9. Is security integrated into the SDLC or discovered late?
10. What are the most critical security risks requiring immediate attention?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Defense in Depth | Multiple security layers (WAF, auth, authz, validation, encryption) | Mature security posture |
| Zero Trust | No implicit trust, verify everything, least privilege | Strong security architecture |
| Security as Afterthought | No security scanning, no security headers, secrets in code | High risk, needs immediate attention |
| Shift-Left Security | Security scanning in CI, threat modeling, security flags in stories | Proactive security approach |
| Compliance-Driven Security | PCI/HIPAA/SOC2 controls implemented, audit logging | Regulatory compliance achieved |
| Token-Based Auth | JWT with proper validation, token rotation | Modern auth, check for proper implementation |
| API Key Only Auth | API keys as sole auth mechanism | May need additional auth layers |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| Hardcoded secrets in source code | String patterns matching API keys, passwords, tokens | HIGH |
| SQL injection vulnerability | String concatenation in SQL queries, no parameterized queries | HIGH |
| Missing authentication on sensitive endpoints | Routes handling data without auth middleware | HIGH |
| Weak password hashing | MD5 or SHA1 for password storage | HIGH |
| No input validation | Missing validation middleware, direct use of user input | HIGH |
| PII in log output | Personal data logged without masking | HIGH |
| No HTTPS enforcement | Missing HSTS header, HTTP allowed in production | MEDIUM |
| Overly permissive CORS | `Access-Control-Allow-Origin: *` in production | MEDIUM |
| No dependency scanning | Missing automated vulnerability scanning in CI | MEDIUM |
| Debug mode in production config | Error stack traces exposed, debug endpoints active | MEDIUM |
| No rate limiting | Missing throttle on auth endpoints, API abuse possible | MEDIUM |
| Missing security headers | No CSP, no X-Frame-Options | LOW |

## Output Guidance

### Must Include
- Authentication implementation summary with method, flows, and security assessment
- Authorization model with enforcement consistency assessment
- OWASP Top 10 assessment with pass/fail/partial per category
- Secret management status with exposure risks
- Critical and high security findings with remediation recommendations

### Should Include (if detected)
- Input validation coverage by input type
- Data protection assessment (encryption at rest and in transit)
- Dependency vulnerability summary by severity
- Security header checklist with current vs. recommended
- Security in SDLC maturity assessment
- PCI/PII/compliance flag status

### Related Areas
- [architecture](./architecture.md) -- security architecture, auth boundaries
- [backend-development](./backend-development.md) -- auth/authz implementation, input validation
- [devops-infrastructure](./devops-infrastructure.md) -- DevSecOps, secret management, image scanning
- [site-reliability](./site-reliability.md) -- security event monitoring, PII in logs
- [database-management](./database-management.md) -- data encryption, access control, PII storage
- [release-management](./release-management.md) -- security gates before release
