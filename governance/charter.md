---
id: GOV-CHARTER
title: AI Governance Charter
phase: governance
summary: Purpose, scope, roles, and guiding principles of AI governance in the SDLC.
tags: [governance, charter, roles, raci]
applies_to: ["**/*"]
tech: null
extends: null
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# AI Governance Charter

## Purpose

This charter establishes why AI governance exists in this organisation, what it covers, and how accountability is structured. Every rule and standard in this repository exists to serve the purpose stated here.

AI-assisted development increases the speed at which code, infrastructure, and decisions are produced. Without governance, this speed increases the rate at which defects, security vulnerabilities, and architectural inconsistencies accumulate. This repository provides a shared, enforceable baseline that keeps AI agents and human developers aligned on quality, security, and organisational standards throughout the entire software development lifecycle.

## Scope

This governance framework applies to:

- All AI coding agents and assistants used in any SDLC activity.
- All human developers, tech leads, architects, product managers, and QA engineers.
- All software projects, services, and infrastructure managed by the organisation.
- All SDLC phases: product definition, architecture, development, security, database, quality assurance, version control, CI/CD, observability, infrastructure, and documentation.

This framework does **not** apply to:

- Research or proof-of-concept work conducted in isolated sandbox environments that will never be promoted to production.
- Personal tooling used exclusively on a developer's local machine with no production artefacts produced.

## Guiding Principles

1. **Security and safety first.** No delivery timeline justifies circumventing security or data-privacy rules. When in doubt, the more secure option is correct.

2. **Agent autonomy must be bounded.** AI agents operate within defined scope. They MUST NOT make irreversible decisions, access systems outside their declared scope, or proceed when facing ambiguous requirements without human confirmation.

3. **Rules are defaults, not ceilings.** Standards define the minimum acceptable bar. Teams are encouraged to adopt higher standards for their domain where appropriate.

4. **Traceability over convenience.** Every significant architectural and engineering decision MUST be documented. Undocumented workarounds are not permitted.

5. **Living standards.** Rules are versioned and reviewed. Outdated rules are deprecated, not ignored. All contributors share responsibility for keeping standards current.

6. **Agnosticism where possible.** Standards are written to be technology-agnostic by default. Technology-specific rules extend the agnostic baseline; they do not replace it.

7. **Proportionality.** Governance overhead is proportional to risk. Low-risk, easily reversible changes require lighter process than high-risk, difficult-to-reverse ones.

## Roles and Responsibilities (RACI)

| Activity | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|
| Defining new standards | Engineering Leadership | Tech Leads / Architects | Affected teams, Security | All engineers |
| Enforcing standards | Tech Leads | All contributors + AI agents | N/A | Engineering Leadership |
| Proposing rule changes | Governance Owner | Requesting team | Security (for SEC rules), affected teams | All engineers |
| Reviewing and versioning standards | Governance Owner | Standard authors | Affected teams | All engineers |
| Onboarding new tools to overlays | Tech Leads | Individual contributors | Security | All engineers |

**Governance Owner:** The person or group with ultimate accountability for the standards in this repository. Responsible for scheduling periodic reviews, resolving conflicts between standards, and approving major version changes.

## Review Cadence

- **Minor updates** (new rules, clarifications, new tech overlays): as needed, following the process in [`rule-authoring.md`](rule-authoring.md).
- **Full review of all standards**: at minimum annually, or after any major organisational change affecting engineering practice.
- **Emergency reviews**: triggered by a critical security incident, a major technology migration, or a regulatory change.

## Relationship to Other Policies

This governance framework is an engineering implementation standard. It does not supersede legal, regulatory, or organisational policies. Where a conflict exists between a rule in this repository and a legal or regulatory obligation, the legal or regulatory obligation takes precedence and the relevant rule MUST be updated to reflect it.
