---
id: DOC-DOCUSAURUS-001
title: API Documentation Standards — Docusaurus
phase: documentation
extends: sdlc/documentation/api-documentation.md
tech: docusaurus
summary: Extends DOC-002 with Docusaurus-specific structure and plugin rules for API documentation.
tags: [documentation, api-docs, docusaurus, openapi, redoc]
applies_to: ["**/docs/**", "**/website/**", "docusaurus.config.*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# API Documentation Standards — Docusaurus (DOC-DOCUSAURUS-001)

> This overlay extends [`sdlc/documentation/api-documentation.md`](../api-documentation.md). All directives in DOC-002 remain in full effect. Only Docusaurus-specific directives appear here.

## Purpose

Docusaurus projects require specific plugin configuration and versioning conventions to keep API reference documentation generated from the OpenAPI spec and aligned with API versions.

---

## MUST

- **DOC-DOCUSAURUS-001-01** API reference documentation is rendered from the OpenAPI specification using a plugin (e.g. `docusaurus-plugin-openapi-docs`, `@scalar/docusaurus`, or `redoc`). Manually authored API endpoint pages are not the primary source of truth.
- **DOC-DOCUSAURUS-001-02** When the API uses versioned URLs (e.g. `/v1/`, `/v2/`), the Docusaurus site uses Docusaurus versioning to maintain documentation for each supported API version, with older versions clearly labelled.

## SHOULD

- **DOC-DOCUSAURUS-001-03** The sidebar separates API Reference (generated from OpenAPI, grouped by tag or endpoint) from Guides/Concepts (manually authored) and Tutorials/Getting Started.
- **DOC-DOCUSAURUS-001-04** The Docusaurus build runs in CI and fails the pipeline on build errors, with broken-link checking enabled.
