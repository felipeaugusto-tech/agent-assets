---
id: SEC-002
title: Input Validation and Output Encoding Standards
phase: security
extends: null
tech: null
summary: Rules for preventing injection attacks through input validation and output encoding.
tags: [security, input-validation, output-encoding, injection, xss, sql-injection, owasp]
applies_to: ["**/*.{js,ts,jsx,tsx,py,java,go,rb,cs,cpp,c,rs,kt,swift,php}"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Input Validation and Output Encoding Standards (SEC-002)

## Purpose

Injection (SQL, command, LDAP, XSS) remains one of the most prevalent and damaging vulnerability classes. These standards ensure untrusted input is validated and output is safely encoded before it reaches a rendering or execution context.

---

## MUST

- **SEC-002-01** All external input is validated at the system boundary before any processing: HTTP request bodies/headers/query parameters/path variables, message queue payloads, file uploads (type, size, content), and data from external files or APIs. Validation checks type, format, length, range, and allowed values.
- **SEC-002-02** All database queries use parameterised queries or prepared statements. String concatenation to build SQL query fragments with user-supplied values is never used.
- **SEC-002-03** All data rendered in an HTML context is HTML-encoded. All data embedded in JavaScript contexts is JavaScript-encoded. Context-aware encoding libraries are used rather than manual encoding.
- **SEC-002-04** User-supplied input is not passed to OS command execution functions. If OS command execution with dynamic arguments is unavoidable, arguments are passed as a list (not a shell string) and strictly validated against an allow-list.

## MUST NOT

- **SEC-002-05** Use deny-list (blocklist) validation as the primary or sole validation strategy. Allow-list rules are the primary strategy; deny-lists may supplement them.

## SHOULD

- **SEC-002-06** Validation uses allow-list rules: define the set of valid values, formats, and patterns and reject anything that does not match.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| Java | [`java/input-validation-output-encoding.md`](java/input-validation-output-encoding.md) | `**/*.java` |
