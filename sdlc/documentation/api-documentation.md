---
id: DOC-002
title: API Documentation Standards
phase: documentation
extends: null
tech: null
summary: Rules for public API docs, examples, and contract-driven generation.
tags: [documentation, api-docs, openapi, swagger, examples, contract-first]
applies_to: ["**/api/**", "**/openapi/**", "**/*.yaml", "**/*.json"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# API Documentation Standards (DOC-002)

## Purpose

API consumers cannot use an API effectively without clear documentation. Stale documentation is worse than no documentation because it leads consumers to implement against the wrong behaviour.

---

## MUST

- **DOC-002-01** Every public API endpoint is documented with: a description of its purpose, all request parameters (path, query, header, body) with types and constraints, all possible response codes and their meanings, the response body structure, and authentication requirements.
- **DOC-002-02** Every endpoint has at least one example request body and one example response body, valid against the schemas they illustrate.
- **DOC-002-03** API documentation is updated in the same PR as any API code change that alters behaviour.

## MUST NOT

- **DOC-002-04** Publish API documentation that is out of sync with the actual API behaviour.

## SHOULD

- **DOC-002-05** API documentation is generated from the API contract specification (OpenAPI, GraphQL schema, or equivalent) rather than maintained as a separate manual document, with generation automated in CI.
- **DOC-002-06** Examples cover both the success case and a common error case.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| Docusaurus | [`docusaurus/api-documentation.md`](docusaurus/api-documentation.md) | `**/docs/**`, `**/website/**` |
