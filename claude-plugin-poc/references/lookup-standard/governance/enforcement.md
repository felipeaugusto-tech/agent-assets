---
id: GOV-ENFORCEMENT
title: Enforcement Model
phase: governance
summary: How rules are enforced, what conformance means, and how severity maps to agent behaviour.
tags: [governance, enforcement, compliance, conformance]
applies_to: ["**/*"]
tech: null
extends: null
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Enforcement Model

## Purpose

This document defines how rules in this repository are enforced, what constitutes conformance, and how the severity model maps to agent and human behaviour.

---

## How severity works

Severity is expressed by section membership, not by inline keywords. Every standard file groups its directives under section headings. The section is the single source of truth — directive text never repeats the severity level.

| Section | Binding level | Deviation |
|---|---|---|
| `## MUST` | Absolute requirement | Not permitted — the rule is followed as written |
| `## MUST NOT` | Absolute prohibition | Not permitted — the rule is followed as written |
| `## SHOULD` | Strong default | Allowed with a documented justification (PR, ADR, or ticket) |
| `## SHOULD NOT` | Strong discouragement | Allowed with a documented justification |
| `## MAY` | Optional guidance | No justification required |

These are the organisation's standards. There is no per-case waiver process. A `MUST`/`MUST NOT` directive is followed until the rule itself is changed through [`versioning-and-change.md`](versioning-and-change.md).

---

## How authority works

Authority tier is determined by file location. When two applicable rules conflict, the higher tier wins. See [`../AGENTS.md`](../AGENTS.md) for the canonical tier table and the overlay-tighten-only invariant.

---

## Who enforces

This repository is primarily consumed by AI agents. Enforcement happens at two points:

**Agent (primary):** The agent reads the applicable rules for the current task and applies them while generating or modifying code, configuration, and documentation. For MUST/MUST NOT directives the agent never deviates. For SHOULD/SHOULD NOT the agent applies the directive by default and surfaces any deviation with a reason. For MAY the agent uses judgment.

**Human review (secondary):** A human reviewer checks that the agent's output conforms to the applicable rules, particularly for directives that require judgment rather than mechanical verification. Reviewers MUST NOT approve output that violates a MUST/MUST NOT directive.

**Automated tooling (optional backstop):** Projects may add CI checks for directives that are mechanically verifiable (for example, no hardcoded secrets, cyclomatic complexity limits, formatter compliance). Automated checks are encouraged but not required by this framework — they are a project-level decision. Their presence does not change the directive's authority; their absence does not weaken it.

---

## Conformance levels

A project is conformant at one of three levels:

| Level | Requirements |
|---|---|
| **Baseline** | All MUST/MUST NOT directives for applicable phases are followed by the agent and confirmed in review. No open MUST/MUST NOT violations. |
| **Standard** | Baseline + all SHOULD/SHOULD NOT deviations are documented in the relevant PR, ADR, or ticket. |
| **Exemplary** | Standard + automated tooling enforces all mechanically verifiable MUST/MUST NOT directives. Tech overlays adopted for all technologies in use. |

New projects MUST reach Baseline before their first production deployment.

---

## Escalation

If a team believes a MUST directive is incorrect, outdated, or creates genuine hardship, raise a rule-change proposal via a pull request and the change process in [`versioning-and-change.md`](versioning-and-change.md). The directive is followed as written until the change is merged.

Bypassing or ignoring a MUST/MUST NOT directive is a policy violation regardless of how the rule is discovered.

---

## Audit

- Engineering Leadership reviews conformance status at minimum quarterly.
- Any MUST/MUST NOT violation that reaches production triggers a postmortem.
