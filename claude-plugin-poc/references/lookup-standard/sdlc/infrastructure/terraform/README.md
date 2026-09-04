# Infrastructure Phase — Terraform Overlay

**Tech:** Terraform
**Rule-ID prefix:** `INF-TERRAFORM`
**Applies to:** `**/*.tf`, `**/*.tfvars`
**Extends:** [`sdlc/infrastructure/`](../README.md)

## Purpose

This overlay extends the agnostic infrastructure standards with Terraform-specific rules for module structure, state management, workspace configuration, and security scanning.

## Files in this overlay

| File | Rule IDs | Summary |
|---|---|---|
| [`infrastructure-as-code.md`](infrastructure-as-code.md) | INF-TERRAFORM-001 | Terraform module, state, and workspace rules |

## How to use

Read the agnostic infrastructure standards first, then read this overlay for Terraform-specific rules.
