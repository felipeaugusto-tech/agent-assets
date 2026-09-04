# Product Phase — Jira Overlay

**Tech:** Jira
**Rule-ID prefix:** `PRD-JIRA`
**Applies to:** Teams using Jira as their issue tracker
**Extends:** [`sdlc/product/`](../README.md)

## Purpose

This overlay extends the agnostic product-phase standards with rules specific to teams using Jira for issue tracking and backlog management. These rules govern how story content maps to Jira fields, how workflows are configured, and how DoR status is tracked.

## Files in this overlay

| File | Rule IDs | Summary |
|---|---|---|
| [`user-stories.md`](user-stories.md) | PRD-JIRA-001 | Jira field mapping for user stories |
| [`acceptance-criteria.md`](acceptance-criteria.md) | PRD-JIRA-002 | Acceptance criteria in Jira description format |

## How to use

Read the agnostic standard first (`sdlc/product/<topic>.md`), then read the corresponding file here for Jira-specific rules. The agnostic rules remain in full effect; this overlay adds to them.
