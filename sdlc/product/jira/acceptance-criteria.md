---
id: PRD-JIRA-002
title: Acceptance Criteria Standards — Jira
phase: product
extends: sdlc/product/acceptance-criteria.md
tech: jira
summary: Extends PRD-002 with Jira-specific acceptance-criteria location and formatting conventions.
tags: [product, acceptance-criteria, jira]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Acceptance Criteria Standards — Jira (PRD-JIRA-002)

> This overlay extends [`sdlc/product/acceptance-criteria.md`](../acceptance-criteria.md). All directives in PRD-002 remain in full effect. Only Jira-specific directives appear here.

## Purpose

Jira-specific conventions for where and how acceptance criteria are stored to ensure consistent visibility during review, QA, and sprint retrospectives.

---

## MUST

- **PRD-JIRA-002-01** Acceptance criteria appear under a heading titled exactly **"Acceptance Criteria"** in the Jira Description field. The heading precedes the criteria list and is not merged with any other section.

## MUST NOT

- **PRD-JIRA-002-02** Represent individual acceptance criteria as Jira sub-tasks — sub-tasks are reserved for independently assignable implementation tasks.

## SHOULD

- **PRD-JIRA-002-03** Acceptance criteria are formatted as a checklist in the Description field so each criterion can be ticked off as it is verified during testing.
