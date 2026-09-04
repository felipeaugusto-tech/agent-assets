---
id: DEV-002
title: Error Handling Standards
phase: development
extends: null
tech: null
summary: Rules for error and exception handling, boundaries, and fail-safe behaviour.
tags: [development, error-handling, exceptions, resilience, fail-safe]
applies_to: ["**/*.{js,ts,jsx,tsx,py,java,go,rb,cs,cpp,c,rs,kt,swift,php}"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Error Handling Standards (DEV-002)

## Purpose

Improper error handling is one of the top causes of data corruption, security vulnerabilities, and production incidents. These standards ensure errors are handled deliberately, logged consistently, and communicated safely.

---

## MUST

- **DEV-002-01** Every error or exception is handled explicitly by at least one of: logging with context and rethrowing, converting to an appropriate error type for the caller, returning an explicit error value, or taking a deliberate recovery action. An empty catch block with no log statement is never acceptable.
- **DEV-002-02** When logging an error, the log includes: the error message and original exception/stack trace, the correlation ID or request identifier (where available), and sufficient context to understand what operation was in progress. Sensitive data (passwords, PII, secrets) does not appear in error logs.

## MUST NOT

- **DEV-002-03** Use exceptions for expected, non-exceptional conditions (e.g. checking record existence). Use conditional checks, optional return types, or result types instead.
- **DEV-002-04** Include stack traces, internal class/method names, file system paths, database error messages or query fragments, or internal system identifiers in error responses returned to external callers. Use a safe generic message externally and log the full detail internally.

## SHOULD

- **DEV-002-05** On error, systems default to the most restrictive safe state: access control decisions deny on error (fail closed); data-mutating operations abort and roll back; background jobs retry with backoff rather than silently skipping work.
- **DEV-002-06** Error handling is concentrated at system boundaries (API handlers, message consumers, job entry points). Internal components throw/return errors upward; the boundary layer translates them to safe external representations.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| Java | [`java/error-handling.md`](java/error-handling.md) | `**/*.java` |
