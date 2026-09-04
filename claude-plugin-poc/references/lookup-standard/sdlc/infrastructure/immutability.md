---
id: INF-003
title: Immutable Infrastructure Standards
phase: infrastructure
extends: null
tech: null
summary: Rules for immutable infrastructure patterns and preventing manual configuration drift.
tags: [infrastructure, immutability, drift, pets-vs-cattle, containers]
applies_to: ["**/*.tf", "**/*.tfvars", "**/cloudformation/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Immutable Infrastructure Standards (INF-003)

## Purpose

Mutable infrastructure accumulates undocumented manual changes that diverge from the IaC definition. This drift makes incident recovery unpredictable and IaC unreliable as the source of truth.

---

## MUST

- **INF-003-01** Infrastructure changes are applied by replacing the infrastructure (deploy a new version), not by directly modifying a running instance. Configuration changes go through the IaC pipeline and result in a new deployment.

## MUST NOT

- **INF-003-02** Make direct changes to running production infrastructure (SSH, cloud console modifications, manual script execution against live instances) outside of a declared incident recovery procedure. Any emergency manual changes are followed by an IaC update within 2 business days.

## SHOULD

- **INF-003-03** Applications are deployed as container images or immutable machine images (AMI) with all application dependencies included. Configuration is injected at runtime, not baked into the image.
- **INF-003-04** IaC is the complete and sole specification of the production environment. Periodic IaC plan runs produce no unexpected diffs; diffs without a corresponding code change indicate drift and are investigated immediately.
