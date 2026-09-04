---
name: spec-authoring
description: Write the technical design for a boundary -- an API, schema, or contract -- precise enough that two engineers implementing it independently would build compatible things. Manual invocation only.
disable-model-invocation: true
---

# Spec Authoring

The "how" half of a design: `adr-writer` covers the decision and its trade-offs; this covers the interface, data shapes, and edge-case behavior precisely enough to implement without a follow-up question.

## 1. Fix the target and gather inputs

The target is **the user's current project**, never this plugin or the GenDD corpus.

Get the decision this spec implements — an ADR, or a clear statement of what's being built and why. If a spike (`/gendd:spike-doc`) already resolved an unknown feeding this design, get its conclusion before starting.

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/spec-authoring/spec-authoring.md` | **Primary task flow.** |
| `${CLAUDE_PLUGIN_ROOT}/references/spec-authoring/spec-template.md` | **Output template.** |

## 3. Run the process

1. **State the boundary** — what this spec covers, and explicitly what it doesn't. One boundary, precisely stated, not "the whole feature."
2. **Define the interface or contract** — API, function signature, schema, or event payload, precise enough to implement without asking a follow-up. Reference existing patterns by file where one is being followed.
3. **Cover edge cases explicitly** — empty input, not-found, unauthorized, concurrent modification, partial failure, whichever apply. Silence here forces the implementer to guess.
4. **Fold in spike conclusions**, if any — settled fact here, with a pointer to the spike doc for the reasoning.
5. **List open questions rather than guessing** — a spec with an honest gap is more useful than one with a confidently wrong answer.
6. **Present for review** before treating it as settled.

Fill `spec-template.md` and save to `docs/specs/{feature-slug}.md`.

## 4. Never invent

A field, endpoint, or behavior not grounded in the actual decision being implemented is a guess dressed as a spec. Where the ADR, requirement, or spike doesn't answer something the spec needs answered, that's an Open Question — not a place to improvise a plausible default.

## 5. Hard limits

- Writes only `docs/specs/{feature-slug}.md`.
- No code changes.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
