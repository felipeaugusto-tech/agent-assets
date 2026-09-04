---
id: ARC-002
title: Technical Design Document Standard
phase: architecture
extends: null
tech: null
summary: Standard for writing technical design documents and the triggers for when one is required.
tags: [architecture, design-doc, technical-design, rfc]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Technical Design Document Standard (ARC-002)

## Purpose

Technical design documents prevent costly implementation rework by forcing explicit articulation of the approach, its trade-offs, and its impact on adjacent systems before code is written.

## Scope

A design document is required when any of the following triggers applies: work spans more than one service or team; work modifies or creates a public API; work requires a database schema change; work involves a new external dependency or integration; work is estimated at more than five story points or five engineering days; or a Tech Lead requests one.

---

## MUST

- **ARC-002-01** A design document is written and circulated for review before the first line of production code for that feature is written. Spike or proof-of-concept code written solely to inform the design is exempt.
- **ARC-002-02** Every design document contains these sections: Problem Statement, Goals and Non-Goals, Proposed Design, Alternatives Considered (at least one, with rejection reasons), API/Interface Changes (if applicable), Data Model Changes (if applicable), Security Considerations.

## MUST NOT

- **ARC-002-03** Begin implementation on a design that has not been acknowledged (read and no blocking objections) by at least one Tech Lead or Architect.

## SHOULD

- **ARC-002-04** The design document is kept current through the implementation phase; significant deviations from the design are noted in the document with a reason.
- **ARC-002-05** The design document includes: Operational Impact (observability, deployment, runbooks) and Open Questions (with owners and target resolution dates).
