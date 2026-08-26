---
id: OBS-003
title: Distributed Tracing Standards
phase: observability
extends: null
tech: null
summary: Rules for distributed tracing context propagation and span conventions.
tags: [observability, tracing, spans, distributed-tracing, context-propagation]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Distributed Tracing Standards (OBS-003)

## Purpose

Distributed tracing makes it possible to follow a single request across multiple services. Without it, diagnosing latency issues and errors in distributed systems is guesswork.

---

## MUST

- **OBS-003-01** Trace context is propagated across all service-to-service calls: outbound HTTP requests include W3C `traceparent` headers; inbound requests extract them; message queue producers include trace context in message headers; consumers extract it before processing.
- **OBS-003-02** A span is created for each outbound HTTP request, database query or transaction, message send to a queue or event stream, background job execution, and any operation expected to take more than 10ms. Span names identify the operation (e.g. `http.get /users/{id}`, `db.query users.findById`).

## MUST NOT

- **OBS-003-03** Include user names, email addresses, national identifiers, passwords, tokens, credentials, payment card data, account numbers, or full request/response bodies in span attributes — use pseudonymous identifiers (user ID, session ID) instead.

## SHOULD

- **OBS-003-04** Failed operations set the span status to ERROR and record the exception or error message as a span event before the span ends.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| OpenTelemetry | [`opentelemetry/tracing.md`](opentelemetry/tracing.md) | Services using OTEL SDK |
