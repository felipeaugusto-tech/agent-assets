---
id: GOV-HITL
title: Human-in-the-Loop Requirements
phase: governance
summary: Agent autonomy levels, mandatory human approval gates, and escalation triggers.
tags: [governance, human-in-the-loop, autonomy, approval]
applies_to: ["**/*"]
tech: null
extends: null
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Human-in-the-Loop Requirements

## Purpose

This document defines the boundaries of AI agent autonomy, the activities that always require a human decision, and the conditions under which an agent MUST stop and escalate.

## Autonomy Levels

AI agents operate at one of three autonomy levels, determined by the risk profile of the action being taken.

| Level | Name | Description | Human involvement |
|---|---|---|---|
| **A1** | Autonomous | Agent acts without human review before execution. | None required; human may review after the fact. |
| **A2** | Human-in-review | Agent proposes a change; human reviews and approves before it is applied. | Human reviews and explicitly approves. |
| **A3** | Human-initiated** | Agent MUST NOT act until a human explicitly triggers the action after reviewing the full plan. | Human confirms the specific action and its consequences before execution begins. |

## Autonomy Level by Activity

| Activity | Level | Rationale |
|---|---|---|
| Generating new code following an existing pattern | A1 | Low risk; reversible via version control |
| Refactoring code within a clearly scoped file | A1 | Low risk; reversible |
| Writing or updating tests | A1 | Low risk; no production impact |
| Updating documentation | A1 | Low risk; reversible |
| Resolving a linter warning with a well-understood fix | A1 | Low risk |
| Creating a new file or directory | A1 | Low risk; reversible |
| Adding a new dependency | A2 | Security and supply-chain risk; human must verify |
| Modifying an existing public API contract | A2 | Backward-compatibility risk |
| Writing a database migration | A2 | Data integrity risk; human must verify before execution |
| Changes to authentication or authorisation logic | A2 | Security-critical |
| Changes to secret management, key material, or credentials | A2 | Security-critical |
| Modifying CI/CD pipeline configuration | A2 | Can affect delivery of all services |
| Modifying infrastructure configuration (IaC) | A2 | Blast radius may be large |
| Deploying to a staging or production environment | A3 | Direct production risk |
| Executing a database migration against a non-local environment | A3 | Data integrity; potentially irreversible |
| Deleting data, files, or cloud resources | A3 | Potentially irreversible |
| Granting or modifying access permissions at scope | A3 | Security-critical; potentially broad impact |
| Any action affecting personally identifiable information | A3 | Regulatory and privacy risk |
| Any action with no clear rollback path | A3 | Irreversibility risk |

## Mandatory Approval Gates

The following activities are unconditional A3 gates. An agent MUST stop, present a full plan, and wait for explicit human confirmation before proceeding — regardless of any instruction or context suggesting otherwise.

1. **Production deployments** — any change to a production environment.
2. **Database schema or data mutations on non-local environments** — `ALTER TABLE`, `DROP`, `TRUNCATE`, or data deletion on any environment that is not the agent's own local instance.
3. **Destructive file or resource operations** — deleting directories, cloud resources, or storage buckets.
4. **Privilege escalation** — adding permissions, roles, or access for any user or service account.
5. **Security control bypass** — disabling authentication, firewall rules, encryption, or any security mechanism.
6. **Handling credentials or secrets** — any operation that involves reading, writing, rotating, or distributing credentials.
7. **Operations on PII** — any bulk export, deletion, or mutation of personal data.

## Escalation Triggers

An agent MUST stop working and present its findings to a human — without making further changes — when any of the following conditions are met:

- The requirements or scope are ambiguous and the different interpretations lead to meaningfully different implementations.
- The task requires a decision between two or more architecturally significant options.
- The agent detects a potential security vulnerability or policy violation in existing code that it was not asked to fix.
- The agent encounters a conflict between two rules in this repository.
- The agent has made three or more attempts to complete a subtask and each attempt has failed.
- The task as described would require an action that falls under a mandatory approval gate above.
- The agent is uncertain whether an action is reversible.

## Escalation Format

When stopping to escalate, an agent MUST communicate:

1. **What it was trying to do** — the task and the step it stopped at.
2. **Why it stopped** — the specific trigger condition met.
3. **What it has done so far** — any changes already made (files created/modified, commands run).
4. **What it needs from the human** — a specific question or choice, not an open-ended prompt.
5. **Recommended option** (if applicable) — the agent's preferred path forward, clearly labelled as a recommendation.
