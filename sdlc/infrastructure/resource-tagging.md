---
id: INF-004
title: Resource Tagging and Naming Standards
phase: infrastructure
extends: null
tech: null
summary: Rules for ownership, cost, and environment tags on all cloud resources.
tags: [infrastructure, tagging, naming, cost, ownership, governance]
applies_to: ["**/*.tf", "**/*.tfvars", "**/cloudformation/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Resource Tagging and Naming Standards (INF-004)

## Purpose

Untagged resources cannot be attributed to a team, assigned a cost, or identified as stale. Tag standards make every resource traceable and cost-attributable.

---

## MUST

- **INF-004-01** Every cloud resource has all mandatory tags applied: `Environment` (enum: `production`, `staging`, `development`), `Service` (owning service name), `Team` (owning team name), `ManagedBy` (enum: `terraform`, `cloudformation`), `CostCentre` (billing code).
- **INF-004-02** Resource names follow the pattern `<environment>-<service>-<resource-type>[-<optional-descriptor>]` in lowercase with hyphens (e.g. `prod-order-service-db`). Underscores are not used in resource names.

## SHOULD

- **INF-004-03** Tag compliance is enforced via a policy-as-code tool (e.g. OPA/Conftest, Checkov) as part of the IaC CI pipeline, blocking the pipeline on tag validation failures.
