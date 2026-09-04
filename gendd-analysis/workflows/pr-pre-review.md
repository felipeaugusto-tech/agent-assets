# Workflow: PR Pre-Review

## Overview

An automated first pass over a pull request, run before a human reviewer looks at it — catches what `rules-manifest.yaml`-routed standards already say plainly (PR size, description completeness, ticket linking) and, where an implementation plan exists for the change, flags where the diff has drifted from what was planned. It does not replace human review (`sdlc/version-control/code-review.md` VCS-004-02 still requires peer approval); it removes the mechanical part of it so the human reviewer spends their attention on judgment calls, not checklist items.

This is the workflow the GitHub Action calls on PR open/update.

## Prerequisites

- Access to the PR diff, description, and metadata (base/head refs, linked ticket if any).
- `rules-manifest.yaml` for standards routing.

## Process

### Step 1: Identify what changed

Categorize the changed files the same way `playbooks/on-demand/run-delta-analysis.md` does — by type (source, test, config, infra, docs) and by area, since the applicable standards differ by area.

### Step 2: Route the diff through the rules manifest

For every changed file's path, resolve which `rules-manifest.yaml` entries apply via their `applies_to` glob — the same resolution method `lookup-standard` uses. This always includes the org-wide version-control standards (`sdlc/version-control/pull-requests.md`, `sdlc/version-control/code-review.md`) plus any tech-specific overlay matched by the changed paths (e.g. `sdlc/version-control/github/pull-requests.md` on a GitHub repo, or a language-specific coding standard for the touched files).

### Step 3: Check the mechanical, always-checkable rules

From the routed standards, verify what can be verified without human judgment:
- **PR size** — flag if changed non-generated production code exceeds the standard's line-count threshold (generated code, lock files, and migrations excluded from the count).
- **Description completeness** — what changed, why, and how to test, all present.
- **Ticket linking** — a closing-keyword reference to a ticket/issue is present.
- **CI status** — required checks are passing, not just present.

Do not attempt the judgment-based checks from the code review standard (correctness, security reasoning, test adequacy) — those need a human or a deeper, separate review; this pass only checks what's mechanically verifiable.

### Step 4: Compare against the implementation plan, if one exists

If `docs/plans/{feature-slug}.md` exists for this change (see `workflows/implementation-plan.md`), diff the PR's actual file list against the plan's file-level task list:
- Files touched that aren't in the plan — flag as scope creep, not necessarily wrong, but worth the author explaining.
- Planned files that weren't touched — flag as either the plan being stale or the work being incomplete.
- If no plan exists, say so plainly rather than skipping this section silently — a missing plan is itself useful information for the reviewer.

### Step 5: Produce the pre-review report

One report, addressed to both the author (fix these before requesting review) and the reviewer (these are already checked, focus elsewhere):
- Standards violations found, each citing the specific rule ID.
- Plan-vs-diff comparison, if applicable.
- A clear "ready for human review" or "needs author action first" verdict.

## Never Invent

A violation not traceable to an actual rule ID in `rules-manifest.yaml` or an actual mismatch against a real implementation plan is noise a reviewer will learn to ignore. When a check genuinely requires judgment this pass can't make (is this correct, is this test meaningful), say that it needs human review rather than guessing at a verdict.

## Output Artifacts

Post as a PR comment (via the calling GitHub Action) and optionally save to `docs/reviews/pr-{number}-pre-review.md`.

## Verification Checklist

- [ ] Every changed file is categorized and routed through the manifest
- [ ] Every flagged violation cites a specific rule ID
- [ ] Mechanical checks (size, description, ticket link, CI status) are all covered
- [ ] Judgment-based checks (correctness, security, test quality) are explicitly deferred to human review, not attempted
- [ ] Plan-vs-diff comparison runs when a plan exists, and its absence is reported when it doesn't
- [ ] A clear ready/not-ready verdict is given

## Related Resources

> **Standards routed:** `sdlc/version-control/pull-requests.md` (VCS-003), `sdlc/version-control/code-review.md` (VCS-004), plus any tech overlay matched by changed paths.
> **Reviews against:** `workflows/implementation-plan.md` — the plan this compares the diff to, when one exists.
> **Routing method:** same resolution `lookup-standard` uses over `rules-manifest.yaml`.
> **Related:** `playbooks/on-demand/run-delta-analysis.md` — broader change-impact analysis, of which this is the PR-scoped, standards-focused slice.
