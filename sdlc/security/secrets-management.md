---
id: SEC-003
title: Secrets Management Standards
phase: security
extends: null
tech: null
summary: Rules prohibiting hardcoded secrets and governing rotation and vault usage.
tags: [security, secrets, credentials, vault, rotation, hardcoded]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Secrets Management Standards (SEC-003)

## Purpose

Hardcoded or improperly stored secrets are among the most exploited vulnerabilities in software systems. A single committed credential can lead to a full account or system compromise.

---

## MUST

- **SEC-003-01** All runtime secrets are fetched from a secrets manager (e.g. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager). Environment variables may pass the reference path or token to the secrets manager, but do not contain the secret value itself.
- **SEC-003-02** All secrets are rotated on the organisation's security policy schedule (at minimum annually for low-risk; every 90 days for high-risk) and immediately upon: suspected or confirmed compromise, personnel changes where the individual had access, or decommissioning of a system that used the secret.

## MUST NOT

- **SEC-003-03** Include passwords, API keys, tokens, private keys, certificates, database connection strings containing credentials, OAuth client secrets, or any value providing system access in source code, configuration files, test fixtures, CI/CD pipeline definitions, Dockerfiles, IaC files, or any other versioned artefact. Pre-commit hooks and CI scanning detect secret patterns using tools such as `git-secrets`, `truffleHog`, or `gitleaks`.
- **SEC-003-04** Write secrets to any log, console, debug output, or observability pipeline — even at DEBUG level.
