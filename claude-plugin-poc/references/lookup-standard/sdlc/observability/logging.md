---
id: OBS-001
title: Logging Standards
phase: observability
extends: null
tech: null
summary: Rules for structured logging, log levels, correlation IDs, and sensitive-data exclusion.
tags: [observability, logging, structured-logs, correlation-ids, log-levels, pii]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Logging Standards (OBS-001)

## Purpose

Logs are the first line of investigation during an incident. Unstructured logs, missing context, and PII in logs are the three most common reasons logs fail when they are most needed.

---

## MUST

- **OBS-001-01** All application logs are emitted in structured JSON format containing at minimum: `timestamp` (ISO 8601), `level`, `message`, `service`, and `trace_id` / `correlation_id`.
- **OBS-001-02** Log levels follow these semantics: `ERROR` for unrecoverable conditions requiring immediate attention; `WARN` for abnormal but self-recovered conditions; `INFO` for normal significant business events; `DEBUG` for verbose diagnostic information (disabled by default in production); `TRACE` only enabled deliberately for short-term debugging.
- **OBS-001-03** Every log entry includes a `trace_id` or `correlation_id` generated at the entry point (API handler, message consumer) and propagated through all downstream calls and log entries.
- **OBS-001-04** The project's configured structured logger is used — not `System.out.println()`, `console.log()`, or bare `print()`.

## MUST NOT

- **OBS-001-05** Include passwords, tokens, API keys, or any secret value in any log entry.
- **OBS-001-06** Include full names, email addresses, national identifiers, financial data, health data, full credit card numbers, or full account numbers in any log entry — use pseudonymous identifiers (user ID, session ID) instead.

## SHOULD

- **OBS-001-07** Log entry masking is applied at the logging framework level rather than relying on individual developers to exclude sensitive fields.
