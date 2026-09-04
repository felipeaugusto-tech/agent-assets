# Implementation Plan: {FEATURE_OR_CHANGE_NAME}

> Status: {Draft / Approved / In Progress / Complete}
> Author: {NAME} | Date: {DATE}
> Related: {link to requirement, PRD, or ADR this implements}

## Goal

{One sentence: what does "done" look like.}

## Scope

### In Scope
- {item}

### Out of Scope
- {item — and why it's excluded, if not obvious}

## Existing Code Reviewed

{What was searched for before proposing new code, and what was found.}

| Existing Utility/Pattern | Location | Reused? |
|--------------------------|----------|---------|
| {name} | `{file reference}` | {Yes / No, and why} |

## File-Level Tasks

| # | File | Change Type | What Changes |
|---|------|-------------|---------------|
| 1 | `{path}` | New / Modify / Delete | {specific, verifiable against a diff} |

## Sequencing

{Order of tasks by dependency. Note anything that can be parallelized vs. anything that must be strictly sequential.}

1. {Task N} — blocks {Task M} because {reason}

## Risks

| Risk | How It Would Be Noticed | Mitigation |
|------|--------------------------|------------|
| {risk} | {monitoring, test, manual check} | {feature flag, migration step, rollback plan} |

## Testing Approach

{What proves this done: unit, integration, manual. Note any gaps being accepted deliberately, and why.}

## Approval

- [ ] Reviewed and approved by: {name/role}
- [ ] Date approved: {date}
