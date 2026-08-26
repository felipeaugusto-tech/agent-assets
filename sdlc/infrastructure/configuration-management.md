---
id: INF-002
title: Configuration Management Standards
phase: infrastructure
extends: null
tech: null
summary: Rules separating config from code, per-environment config, and secrets exclusion.
tags: [infrastructure, configuration, environment, secrets, config, twelve-factor]
applies_to: ["**/*.env*", "**/config/**", "**/settings/**", "**/*.yaml", "**/*.toml"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Configuration Management Standards (INF-002)

## Purpose

Configuration that is baked into the build artefact prevents environment-specific deployment without rebuild. These standards enable a single artefact to be promoted through environments by swapping configuration.

---

## MUST

- **INF-002-01** Configuration values that differ between environments (connection strings, feature flags, API endpoints) are externalised from the build artefact and injected at deploy time. The same artefact is deployable to any environment by changing only the injected configuration.
- **INF-002-02** Every configuration value that differs between environments is declared per-environment. Configuration is validated to ensure all required values are present for the target environment.

## MUST NOT

- **INF-002-03** Store secret values (passwords, API keys, tokens, private keys) in configuration files. References to secrets (vault paths, secret manager ARNs) are acceptable. `.env` files are not committed to version control. See [`sdlc/security/secrets-management.md`](../security/secrets-management.md).

## SHOULD

- **INF-002-04** Applications validate all required configuration values at startup and fail fast with a clear error message naming the missing or invalid configuration key, before the service begins accepting traffic.
