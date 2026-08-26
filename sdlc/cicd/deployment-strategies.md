---
id: CICD-004
title: Deployment Strategy Standards
phase: cicd
extends: null
tech: null
summary: Rules for blue/green, canary, rollback, and feature flag deployments.
tags: [cicd, deployment, blue-green, canary, rollback, feature-flags, progressive-delivery]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Deployment Strategy Standards (CICD-004)

## Purpose

Deployments that cannot be rolled back safely are the primary cause of prolonged outages. Progressive delivery limits the blast radius of a bad deployment.

---

## MUST

- **CICD-004-01** Every production deployment has a documented rollback procedure that can be executed within the service's RTO, has been tested at least once in staging, and does not require undoing database migrations.
- **CICD-004-02** High-risk changes — those affecting authentication, payment processing, data migrations, external API integrations, or any path estimated to affect more than 20% of users — use canary (5–10% traffic to new version before full rollout) or blue/green (parallel run, atomic traffic switch) deployment. The progressive rollout is monitored for error rate and latency increase before expanding.

## MUST NOT

- **CICD-004-03** Apply a full, immediate rollout of an untested change to 100% of production traffic for high-risk changes.
- **CICD-004-04** Make production changes through direct SSH access, manual config changes, or manual container updates outside of a declared incident recovery procedure. Any such emergency change is immediately followed by a corresponding change in version control.

## SHOULD

- **CICD-004-05** New features are deployed behind feature flags that are disabled by default, enabled for internal users first, then a percentage of external users, then the full population, and removed once the feature is stable.
