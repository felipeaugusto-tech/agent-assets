---
id: INF-001
title: Infrastructure-as-Code Standards
phase: infrastructure
extends: null
tech: null
summary: Rules requiring IaC for all infrastructure with modularity and state management rules.
tags: [infrastructure, iac, modularity, state, version-control, reproducibility]
applies_to: ["**/*.tf", "**/*.tfvars", "**/cloudformation/**", "**/cdk/**", "**/pulumi/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Infrastructure-as-Code Standards (INF-001)

## Purpose

Manually provisioned infrastructure is untraceable, unreproducible, and unmaintainable at scale. IaC makes infrastructure reproducible, reviewable, and auditable.

---

## MUST

- **INF-001-01** All cloud resources in shared environments (staging, production) are defined and managed through IaC. Resources created manually for incident recovery are replaced by IaC within 2 business days.
- **INF-001-02** All IaC is stored in version control and goes through the same PR review process as application code. Infrastructure changes affecting production are reviewed by at least one engineer with infrastructure expertise.
- **INF-001-03** IaC is organised into focused, reusable modules. Each module manages one logical component (e.g. a network, a database cluster, an application service) with defined inputs and outputs.

## MUST NOT

- **INF-001-04** Apply IaC changes to production directly from a developer's workstation without going through the CI/CD pipeline with a plan review step.
- **INF-001-05** Create or modify shared-environment resources via cloud console or CLI directly.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| Terraform | [`terraform/infrastructure-as-code.md`](terraform/infrastructure-as-code.md) | `**/*.tf` |
