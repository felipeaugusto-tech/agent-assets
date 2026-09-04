---
id: PRD-JIRA-001
title: User Story Standards — Jira
phase: product
extends: sdlc/product/user-stories.md
tech: jira
summary: Extends PRD-001 with Jira field mapping and workflow rules for user stories.
tags: [product, user-stories, jira, workflow]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# User Story Standards — Jira (PRD-JIRA-001)

> This overlay extends [`sdlc/product/user-stories.md`](../user-stories.md). All directives in PRD-001 remain in full effect. Only Jira-specific directives appear here.

## Purpose

Jira has specific field constraints that affect where and how story content is stored. These directives ensure consistency across board views, sprint reports, and audit trails.

---

## MUST

- **PRD-JIRA-001-01** The Jira **Summary** field contains either the full "As a [persona], I want [action]" phrase or a concise action-oriented title that unambiguously represents the story goal (e.g. "Allow registered users to reset their password via email"). Task/implementation language and vague labels are not acceptable.
- **PRD-JIRA-001-02** Acceptance criteria are recorded in the Jira **Description** field under a clearly labelled section, not in comments or sub-task descriptions.
- **PRD-JIRA-001-03** Every story is linked to an active Epic via the Epic Link (or Parent in next-gen projects) field before it is added to a sprint.

## SHOULD

- **PRD-JIRA-001-04** Stories are estimated in Story Points using the team's agreed scale (e.g. Fibonacci: 1, 2, 3, 5, 8, 13) rather than time-based estimates in the Story Points field.
