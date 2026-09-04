---
id: INF-TERRAFORM-001
title: Infrastructure-as-Code Standards — Terraform
phase: infrastructure
extends: sdlc/infrastructure/infrastructure-as-code.md
tech: terraform
summary: Extends INF-001 with Terraform module, state, and workspace rules.
tags: [infrastructure, iac, terraform, modules, state, workspaces, security]
applies_to: ["**/*.tf", "**/*.tfvars"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Infrastructure-as-Code Standards — Terraform (INF-TERRAFORM-001)

> This overlay extends [`sdlc/infrastructure/infrastructure-as-code.md`](../infrastructure-as-code.md). All directives in INF-001 remain in full effect. Only Terraform-specific directives appear here.

## Purpose

Terraform has specific state management, version pinning, and CI pipeline conventions that prevent state corruption, plan inconsistencies, and supply-chain risks.

---

## MUST

- **INF-TERRAFORM-001-01** Terraform state is stored in a remote backend (e.g. S3 + DynamoDB, GCS, Terraform Cloud) with state locking enabled. Local state (`terraform.tfstate`) is not used for shared environments.
- **INF-TERRAFORM-001-02** Each environment (development, staging, production) has a separate Terraform state file, achieved via separate backend key/path or Terraform workspaces with appropriate state isolation.
- **INF-TERRAFORM-001-03** The `required_version` constraint is set in the `terraform {}` block; all providers have version constraints preventing automatic major-version upgrades; and `terraform.lock.hcl` is committed to version control.

## SHOULD

- **INF-TERRAFORM-001-04** CI pipelines for Terraform include in order: `terraform fmt -check`, `tfsec` or `checkov` (SAST for misconfigurations), `terraform validate`, and `terraform plan` with human review before apply.
- **INF-TERRAFORM-001-05** Terraform modules are sourced from the official Terraform Registry, internal module registries, or local paths — not direct GitHub references with mutable refs (`?ref=main`).
