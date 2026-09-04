---
id: SEC-006
title: Threat Modeling Standards
phase: security
extends: null
tech: null
summary: When and how to perform threat modeling and document findings.
tags: [security, threat-modeling, stride, risk, design-review]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Threat Modeling Standards (SEC-006)

## Purpose

Threat modeling identifies security risks at design time, when they are cheapest to address. Systems that have not been threat-modelled frequently contain architectural vulnerabilities that cannot be fixed without major refactoring.

---

## MUST

- **SEC-006-01** A threat model is produced for: any new service exposed to the internet or untrusted clients; any feature handling authentication, authorisation, or session management; any feature processing, storing, or transmitting PII, financial, or health data; any integration with a third-party service involving data sharing; and any significant change to an existing security boundary.
- **SEC-006-02** All identified threats are documented with: a description of the threat, likelihood (High/Medium/Low) with rationale, potential impact (High/Medium/Low) with rationale, and the mitigation (an existing control, a planned control with owner and target date, or an explicit acceptance with justification). Threats accepted without mitigation are reviewed and re-accepted at minimum annually.

## SHOULD

- **SEC-006-03** Threat modeling uses STRIDE to enumerate threats: Spoofing (Authentication), Tampering (Integrity), Repudiation (Non-repudiation), Information Disclosure (Confidentiality), Denial of Service (Availability), Elevation of Privilege (Authorisation).
- **SEC-006-04** Threat modeling is conducted as part of the technical design document review process (see [`sdlc/architecture/design-documents.md`](../architecture/design-documents.md)), with a security engineer participating in or reviewing the threat model.
