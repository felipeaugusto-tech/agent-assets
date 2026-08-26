---
id: ARC-003
title: API Design Standards
phase: architecture
extends: null
tech: null
summary: Rules for API versioning, backward compatibility, error model, and pagination.
tags: [architecture, api, rest, versioning, error-model, pagination, backward-compatibility]
applies_to: ["**/api/**", "**/openapi/**", "**/*.yaml", "**/*.json"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# API Design Standards (ARC-003)

## Purpose

Consistent API design reduces integration costs, prevents breaking changes from reaching consumers, and makes APIs predictable enough to be consumed without reading all documentation.

## Scope

Applies to all APIs exposed to external consumers (other services, front-ends, third parties). Internal-only APIs should follow these standards; deviations require documented justification.

---

## MUST

- **ARC-003-01** All external APIs include a major version identifier in the URL path (e.g. `/v1/resources`) as an integer. A major version increment (`v1` → `v2`) is required for any breaking change.
- **ARC-003-02** Within a major version, APIs remain backward-compatible. Breaking changes that require a version increment: removing or renaming a field; changing a field's data type; changing a field from optional to required; removing an endpoint; changing the meaning of an existing status code; adding a new required request field.
- **ARC-003-03** All error responses use the structure: `{ "error": { "code": "SCREAMING_SNAKE_CASE_STRING", "message": "Human-readable, safe-to-display description.", "details": [] } }`. HTTP status codes correctly reflect the error category (4xx client, 5xx server). `message` never contains stack traces, internal identifiers, or system paths.
- **ARC-003-04** Collection endpoints that can return more than 100 items implement pagination, including the current page of results and a way to retrieve the next page.

## SHOULD

- **ARC-003-05** APIs are designed by writing the contract specification (e.g. OpenAPI document) before implementation begins, with the contract reviewed and approved before the first implementation line is written.
- **ARC-003-06** PUT and PATCH operations are idempotent; POST operations that create resources support idempotency keys to prevent duplicate creation on retry.
- **ARC-003-07** Cursor-based pagination is preferred over offset-based pagination for large or frequently updated datasets.

## MAY

- **ARC-003-08** `v0` is used for pre-release APIs that have not yet reached stability; consumers of `v0` have no breaking-change guarantees.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| OpenAPI | [`openapi/api-design.md`](openapi/api-design.md) | `openapi.yaml`, `openapi.json`, `*.oas.yaml` |
