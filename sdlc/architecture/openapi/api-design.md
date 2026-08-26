---
id: ARC-OPENAPI-001
title: API Design Standards — OpenAPI
phase: architecture
extends: sdlc/architecture/api-design.md
tech: openapi
summary: Extends ARC-003 with contract-first API design rules for OpenAPI specifications.
tags: [architecture, api, openapi, contract-first, specification]
applies_to: ["**/openapi.yaml", "**/openapi.json", "**/*.oas.yaml", "**/*.oas.json"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# API Design Standards — OpenAPI (ARC-OPENAPI-001)

> This overlay extends [`sdlc/architecture/api-design.md`](../api-design.md). All directives in ARC-003 remain in full effect. Only OpenAPI-specific directives appear here.

## Purpose

OpenAPI specifications require specific structural conventions to support code generation, documentation, mock servers, and contract testing.

---

## MUST

- **ARC-OPENAPI-001-01** The OpenAPI specification passes validation (e.g. `spectral lint`, `redocly lint`) before it is committed. CI includes a lint/validation step that blocks merge on validation failures.
- **ARC-OPENAPI-001-02** All reusable object schemas are defined in `components/schemas` and referenced via `$ref`. Inline schema definitions are only acceptable for simple scalar types that are genuinely not reused.
- **ARC-OPENAPI-001-03** Every request body and every non-empty response body includes at least one example that is valid against the schema it illustrates.
- **ARC-OPENAPI-001-04** Every operation has a unique `operationId` in camelCase format that clearly describes the operation (e.g. `createUser`, `listOrdersByCustomer`).
- **ARC-OPENAPI-001-05** All operations that require authentication declare the applicable security scheme. Operations that are intentionally unauthenticated (e.g. health check) explicitly declare `security: []`.

## SHOULD

- **ARC-OPENAPI-001-06** New OpenAPI specifications use OpenAPI 3.1.x (`openapi: "3.1.0"`). Existing 3.0.x specifications may remain at 3.0.x; migration to 3.1.x is planned for the next major API version.
- **ARC-OPENAPI-001-07** Examples cover both the happy path and a common error case.
