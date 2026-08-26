# Security Phase Standards

**Rule-ID prefix:** `SEC`

## Purpose

Security standards apply to every SDLC phase and every code change. They are not a phase that happens "at the end" — they are a continuous cross-cutting concern. This folder provides the rules for the security-specific activities that must be applied throughout development.

## Standards in this phase

| File | Rule IDs | Summary |
|---|---|---|
| [`authentication-authorization.md`](authentication-authorization.md) | SEC-001 | Authn/z implementation, sessions, tokens, least privilege |
| [`input-validation-output-encoding.md`](input-validation-output-encoding.md) | SEC-002 | Injection prevention, validation, encoding (OWASP A03) |
| [`secrets-management.md`](secrets-management.md) | SEC-003 | No hardcoded secrets, rotation, vault usage |
| [`data-protection.md`](data-protection.md) | SEC-004 | Encryption in transit and at rest, key management |
| [`data-privacy.md`](data-privacy.md) | SEC-005 | Privacy-by-design, data-subject rights, data minimisation |
| [`threat-modeling.md`](threat-modeling.md) | SEC-006 | When and how to threat model |
| [`vulnerability-management.md`](vulnerability-management.md) | SEC-007 | Scanning, patch SLAs, responsible disclosure |

## Tech overlays

| Technology | Folder | Applies to |
|---|---|---|
| Java | [`java/`](java/README.md) | `**/*.java` |

## OWASP alignment

These standards address the OWASP Top 10

| OWASP Top 10 Category | Primary standard |
|---|---|
| A01 Broken Access Control | `authentication-authorization.md` |
| A02 Cryptographic Failures | `data-protection.md` |
| A03 Injection | `input-validation-output-encoding.md` |
| A04 Insecure Design | `threat-modeling.md` |
| A05 Security Misconfiguration | `secrets-management.md` |
| A06 Vulnerable and Outdated Components | `vulnerability-management.md` |
| A07 Identification and Authentication Failures | `authentication-authorization.md` |
| A08 Software and Data Integrity Failures | `vulnerability-management.md` |
| A09 Security Logging and Monitoring Failures | See `sdlc/observability/logging.md` |
| A10 Server-Side Request Forgery | `input-validation-output-encoding.md` |
