---
id: SEC-001
title: Authentication and Authorization Standards
phase: security
extends: null
tech: null
summary: Rules for authn/z implementation, sessions, tokens, and least privilege.
tags: [security, authentication, authorization, sessions, jwt, rbac, least-privilege]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Authentication and Authorization Standards (SEC-001)

## Purpose

Broken access control is the OWASP Top 10's most prevalent category. These standards provide the baseline that prevents authentication and authorisation failures from reaching production.

---

## MUST

- **SEC-001-01** Every endpoint that accesses non-public data or performs a non-public action requires authentication. Endpoints that are intentionally public are explicitly documented as such and do not inadvertently expose sensitive data.
- **SEC-001-02** Authorisation checks are implemented in the service or domain layer, not only at the API gateway. Every service enforces that the calling identity has permission for the requested operation on the requested resource before performing it.
- **SEC-001-03** Every user, service account, and process is granted only the minimum permissions necessary: database users have only the permissions required for their queries; service-to-service calls use scoped, short-lived tokens; admin permissions are not granted to operational service accounts.
- **SEC-001-04** Session tokens are generated with cryptographically secure random number generators, transmitted only over HTTPS, have `HttpOnly` and `Secure` flags set on cookies, have a reasonable expiry time, and are invalidated server-side on logout.

## MUST NOT

- **SEC-001-05** Use custom cryptographic algorithms or implementations for authentication, session management, or token generation. Use established, audited libraries and protocols (OAuth 2.0, OpenID Connect, industry-standard JWT libraries).

## SHOULD

- **SEC-001-06** Access tokens have a short lifespan (15 minutes to 1 hour). Refresh tokens rotate on use. Refresh token reuse is treated as a potential token theft event and triggers session revocation.
