---
name: implementation-plan
description: Break a requirement or decision into a file-level, dependency-ordered task list with named risks -- the artifact a PR gets reviewed against later. Manual invocation only.
disable-model-invocation: true
---

# Implementation Plan

The bridge between "we know what to build" and "here is the code." Produces a plan a reviewer can later diff the actual PR against — that's what `/gendd:pr-pre-review` does with it.

## 1. Fix the target and gather inputs

The target is **the user's current project**, never this plugin or the GenDD corpus.

Get the requirement or decision this implements before starting — a requirement (from `/gendd:enhance-requirements`), a PRD, or an ADR (from the `adr-writer` skill). If none exists yet and the change is non-trivial, say so and suggest producing one first rather than planning against an unstated goal.

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/implementation-plan/implementation-plan.md` | **Primary task flow** — the eight steps below follow it. |
| `${CLAUDE_PLUGIN_ROOT}/references/implementation-plan/implementation-plan-template.md` | **Output template.** |

## 3. Run the process

1. **Restate the goal** in one sentence. If it can't be, the scope isn't settled — go back to the requirement first.
2. **Search the codebase** for existing functions, components, or patterns that already do something close to this. Note what's reused and what isn't sufficient, and why.
3. **Define scope** explicitly — in scope and out of scope, as a plain list a reviewer can check a diff against later.
4. **Break into file-level tasks** — for each file, what changes, specific enough to verify against an actual diff. Never "update the service"; always "add a `validateInput` guard to `PaymentService.processPayment`."
5. **Sequence by dependency**, not convenience — note what blocks what.
6. **Name the risks** — what could break, how it would be noticed, what mitigates it. An empty risks section is a sign of shallow analysis, not a safe change.
7. **State the testing approach**, including any gaps being accepted deliberately.
8. **Present the plan and wait for approval** before considering it final — a plan nobody agreed to is a guess with formatting.

Fill `implementation-plan-template.md` with the result and save to `docs/plans/{feature-slug}.md`.

## 4. Never invent

A task, risk, or scope boundary not grounded in the actual requirement or an actual codebase search is a guess. Where the requirement doesn't specify something the plan needs, ask rather than picking a plausible default and writing it down as if it were decided.

## 5. Hard limits

- Writes only `docs/plans/{feature-slug}.md`, and only after the user approves the plan.
- No code changes — this plans the work, it doesn't do it.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
