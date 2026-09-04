# Workflow: Implementation Plan

## Overview

An implementation plan is the bridge between "we know what to build" and "here is the code." It breaks a change into file-level tasks, orders them by dependency, and names the risks up front — so a reviewer can later judge the actual PR against what was intended, instead of reconstructing intent from a diff after the fact.

This is a **Build phase** artifact. It assumes the decision to build something has already been made — by a PRD, an enhanced requirement, or an ADR — and focuses on *how the work gets sequenced*, not what or why. A spec (see `workflows/spec-authoring.md`) covers the technical design in between: interfaces, data shapes, contracts. An implementation plan covers execution: which files, in what order, with what risk.

**Why this exists:** without a written plan, "does this PR match what we agreed to build" has no artifact to check against — reviewers either trust the diff blindly or reconstruct intent from memory. `workflows/pr-pre-review.md` is designed to diff the actual PR against this document.

## When to Use

- Before starting a change that touches more than one file, or that a reviewer would reasonably ask "did you consider X" about.
- After a spec or ADR exists for the *what*, before writing code for the *how*.
- Skip it for a genuinely trivial change (a one-line fix, a typo, a config value) — the plan should never cost more than the change it's planning.

## Prerequisites

- A clear statement of the requirement or decision being implemented (from `enhance-requirements`, a PRD, or an ADR).
- Read access to the target codebase, to find existing patterns and utilities before proposing new ones.

## Process

### Step 1: Restate the goal in one sentence

Before touching files, confirm what "done" looks like. If this can't be said in one sentence, the scope probably isn't settled yet — go back to the requirement or spec first.

### Step 2: Search before proposing

Look for existing functions, components, or patterns that already do something close to what's needed. A plan that proposes a new helper where one already exists is a plan that will be rejected in review. Note what was found and why it's reused or why it isn't sufficient.

### Step 3: Define scope explicitly

State what's **in scope** and what's **out of scope**, as a plain list. A reviewer should be able to tell, from this section alone, whether something in the diff is scope creep.

### Step 4: Break the work into file-level tasks

For each file that will change or be created:
- What changes, at a level of detail a reviewer can verify against the diff (not "update the service" — "add a `validateInput` guard to `PaymentService.processPayment`").
- Whether it's a new file, a modification, or a deletion.

### Step 5: Sequence the tasks

Order tasks by dependency, not by convenience. If task 3 can't be tested until task 1 lands, say so. This is what lets someone else pick up the plan mid-way and know what's safe to do next.

### Step 6: Name the risks

For each risk that's more than hypothetical: what could break, how it would be noticed, and what mitigates it (a feature flag, a migration step, a rollback path). A risks section with nothing in it is a sign the analysis was shallow, not that the change is safe.

### Step 7: State the testing approach

What level of testing proves this done — unit, integration, manual verification — and where the gaps are, if any are being accepted deliberately.

### Step 8: Get confirmation before implementation starts

Present the plan and wait for explicit approval before writing code. Treat this the same way `adr-writer` treats its approval gate — a plan nobody agreed to isn't a plan, it's a guess with formatting.

## Output Artifacts

Save to `docs/plans/{feature-slug}.md` in the target repository, using `templates/implementation-plan-template.md`.

## Verification Checklist

- [ ] Goal stated in one sentence
- [ ] Existing code searched for reuse before proposing new code
- [ ] Scope explicitly separates in vs. out
- [ ] Every file-level task is concrete enough to verify against a diff
- [ ] Tasks are sequenced by dependency, not convenience
- [ ] Risks include a way to notice and a mitigation, not just a name
- [ ] Testing approach is stated, including accepted gaps
- [ ] Plan was approved before implementation started

## Related Resources

> **Precedes:** `workflows/spec-authoring.md` for the technical "how" when the design itself needs documenting, not just the task breakdown.
> **Followed by:** `workflows/pr-pre-review.md` — reviews the actual PR against this plan.
> **Decision context:** `workflows/adr-writer` (vendored skill) — covers the "what and why" this plan assumes is already settled.
> **Template:** `templates/implementation-plan-template.md`.
