---
id: CICD-002
title: Build Reproducibility Standards
phase: cicd
extends: null
tech: null
summary: Rules for deterministic builds, artifact integrity, and software provenance.
tags: [cicd, builds, reproducibility, artifacts, provenance, integrity, supply-chain]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Build Reproducibility Standards (CICD-002)

## Purpose

Non-reproducible builds hide supply-chain attacks and make debugging production issues harder. Artefact signing and SBOM generation provide verifiable provenance.

---

## MUST

- **CICD-002-01** Build pipelines are deterministic: the same source commit, lock-file-pinned dependencies, and build environment produce identical or functionally identical artefacts. Builds do not include developer-local files, environment-specific paths, or untracked files.
- **CICD-002-02** Every published artefact (container image, binary, package) is accompanied by a cryptographic hash (SHA-256 or higher) or a digital signature generated in the CI pipeline, not manually.

## MUST NOT

- **CICD-002-03** Build production or staging artefacts from uncommitted or modified source. The CI pipeline verifies the working directory is clean before building. Manual builds from a developer workstation are not deployed to any shared environment.

## SHOULD

- **CICD-002-04** SBOM generation is part of the CI pipeline for every release artefact, published alongside the artefact in CycloneDX or SPDX format and retained for the lifetime of the artefact in production.
