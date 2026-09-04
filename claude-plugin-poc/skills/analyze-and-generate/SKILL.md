---
name: analyze-and-generate
description: Orchestrate the full 5-phase GenDD flow (analyze codebase, determine SDLC areas, generate context, check standards, generate IDE rules) by running the individual gendd skills in sequence with human gates between phases. Manual invocation only.
disable-model-invocation: true
---

# Analyze & Generate

The main entry point — walks a repository through all five phases, pausing at each gate for confirmation. Each phase is itself a separate `/gendd:` skill; this skill's job is sequencing and gating, not re-implementing their methodology.

## 1. Fix the target

The target is **the user's current repository**, never this plugin or the GenDD corpus.

## 2. Load the reference (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/analyze-and-generate/analyze-and-generate.md` | **The orchestration map** — phase order, gates, skip conditions, and the full output tree. Consult it for the "what happens" detail under each phase below; don't re-derive it. |

Reading it as it is: verbatim corpus copy, `@GenDD-Flow/...` links don't resolve here — the phase-by-phase invocations it shows as raw prompts are what the skills below already implement; don't paste them as literal prompts, just invoke the skills.

## 3. Run the phases

| Phase | Skill to invoke | Skip condition |
| --- | --- | --- |
| 1 · Analyze Codebase | `/gendd:run-brownfield-analysis` (existing repo) or `/gendd:greenfield-analysis` (new project) | Skip if `docs/brownfield/` (or `docs/greenfield/inference-result.md`) already exists and is current. |
| 2 · Determine SDLC Areas | Handled automatically inside `generate-context-areas` (it runs role-detection and asks for confirmation if no area list exists yet) | Never skip — area confirmation is mandatory. |
| 3 · Generate Context | `/gendd:generate-context-areas` | Never skip — this is the core deliverable. |
| 4 · Check & Generate Standards | `/gendd:detect-and-generate-standards` | Optional — skip if standards aren't needed or already exist. |
| 5 · Generate IDE Rules | `/gendd:generate-ide-rules` | Optional — skip if not needed or will be done manually. |

**Gate discipline:** after each phase, report what it produced and get the user's go-ahead before invoking the next skill. Phase 1 and Phase 2 (area confirmation, inside `generate-context-areas`) are **hard gates** — do not proceed past them without explicit confirmation, even if the user asked for "the full flow" up front. Phase 4's gate is recommended but the user may choose to skip generation there and still continue to Phase 5.

If brownfield/greenfield output already exists, tell the user you're skipping Phase 1 and confirm that's correct before moving on — don't skip silently.

## 4. Never invent

This skill adds no methodology of its own — every actual decision (what counts as an area, what standard to generate, what an IDE rule should say) happens inside the phase skill it invokes. Don't shortcut a phase by generating its output directly instead of invoking the skill; that's exactly the duplication this plugin's whole reference-copying design exists to prevent.

## 5. Hard limits

- Writes nothing itself — all writes happen inside the invoked phase skills, under their own hard limits.
- No MCP tools directly (Phase 5's `generate-ide-rules` uses web search on its own, per its own hard limits).
- No tests, builds, deploys, or benchmarks.
