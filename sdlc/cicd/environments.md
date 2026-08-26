---
id: CICD-005
title: Environment Standards
phase: cicd
extends: null
tech: null
summary: Rules for environment parity and promotion from development to production.
tags: [cicd, environments, parity, promotion, staging, production]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Environment Standards (CICD-005)

## Purpose

Environment inconsistencies are a primary cause of "works in staging, broken in production" incidents. These standards reduce environment-related failures by making environments consistent and promotion deterministic.

---

## MUST

- **CICD-005-01** Every service has at minimum three environments: development/local (initial testing), staging (production-equivalent for integration, performance, and acceptance testing), and production.
- **CICD-005-02** The same versioned artefact (container image, binary, or package) is promoted through staging to production without rebuilding. Environment-specific configuration is injected at deploy time via configuration management — not baked into the artefact.
- **CICD-005-03** Staging matches production in: application configuration and feature flags, infrastructure tier (same cloud provider, same or equivalent instance sizes), and network topology and security group configuration. Staging may differ in data volume, instance count, and cost controls.

## MUST NOT

- **CICD-005-04** Use real production data in non-production environments. Staging databases use synthetic or masked data. See [`sdlc/database/pii-handling.md`](../database/pii-handling.md).
