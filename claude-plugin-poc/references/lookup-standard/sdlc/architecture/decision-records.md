---
id: ARC-001
title: Architecture Decision Records (ADR)
phase: architecture
extends: null
tech: null
summary: When and how to write ADRs and what they must contain.
tags: [architecture, adr, decisions, documentation]
applies_to: ["**/docs/adr/**", "**/adr/**", "**/*.adr.md"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Architecture Decision Records (ARC-001)

## Purpose

Architecture Decision Records capture the context, options, and rationale behind significant technical decisions. Without them, teams repeatedly rediscover the same trade-offs and new members cannot understand why the system is the way it is.

## Scope

An ADR is required when a decision meets one or more of the following triggers: the decision is difficult or expensive to reverse; it affects interfaces between two or more teams; it introduces a new technology, pattern, or dependency; it involves a security architecture choice; or it was contested and required explicit trade-off analysis.

---

## MUST

- **ARC-001-01** An ADR is written for every decision meeting a trigger, before or simultaneously with the first implementation — not retrospectively. Use [`templates/adr-template.md`](../../templates/adr-template.md).
- **ARC-001-02** Every ADR documents at least two options with explicit pros and cons, and states a specific reason for rejection for each non-chosen option.
- **ARC-001-03** ADRs are stored in `docs/adr/ADR-NNN-short-title.md` in the repository they affect.

## MUST NOT

- **ARC-001-04** Modify the Decision section of an accepted ADR — create a new ADR and update the old one's status to "Superseded by ADR-NNN" instead.

## SHOULD

- **ARC-001-05** An ADR is reviewed by at least one engineer not involved in writing it before reaching Accepted status.
