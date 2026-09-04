---
name: greenfield-analysis
description: Analyze planning documents (or a described project) for a new codebase that doesn't exist yet, replacing the brownfield scan as the entry point into context/standards/IDE-rules generation. Manual invocation only.
disable-model-invocation: true
---

# Greenfield Analysis

For a project with no existing code: read whatever planning documents exist (or a direct description), and produce the same kind of inference result a brownfield scan would produce — so the rest of the pipeline (`generate-context-areas`, `detect-and-generate-standards`, `generate-ide-rules`) can run against a project that's still on paper.

## 1. Fix the target

The target is **the user's new/planned project**, not this plugin or the GenDD corpus.

Look for planning documents in `docs/specs/` under the current project folder (Markdown, PDF, plain text, architecture diagrams are all fine). If none exist, ask the user to describe the project directly: purpose, planned tech stack, high-level architecture, key services/modules. Either input, or a mix, is valid — the more given, the better later phases will be.

## 2. Load the reference (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/greenfield-analysis/greenfield-analysis.md` | **Primary task flow.** Short — this workflow only replaces the input-gathering step; everything past it hands off to the already-packaged pipeline skills. |

Reading it as it is: verbatim corpus copy, internal `@GenDD-Flow/...` links don't resolve here, describes a Cursor Chat workflow — adapt intent, ignore tool mechanics.

## 3. Run the process

1. **Analyze the specifications** (or the description given) and produce an inference result with the same shape as a brownfield inference: system purpose, architecture classification, service catalog, core flows, data map, risk hotspots (for the *planned* architecture), conventions, tech stack, and suggested SDLC areas.
2. **Save it** to `docs/greenfield/inference-result.md` in the project folder.
3. **Tell the user what's next**, rather than chaining automatically: `/gendd:generate-context-areas` (structural signals will be empty since there's no code yet — area detection relies on the suggested areas from step 1), then `/gendd:detect-and-generate-standards`, then `/gendd:generate-ide-rules`. Context documents produced this way describe *planned* state ("Planned State" instead of "Current State", planned file locations instead of existing ones) — say so explicitly so the next skill invocation doesn't get confused about tense.

## 4. Never invent

A planned architecture is not evidence of a built one. Every claim in the inference result must trace back to something the user actually wrote or said — do not fill gaps with a plausible-sounding default tech stack or service list. Where the planning documents are silent on something material, say so rather than guessing.

## 5. Hard limits

- Writes only `docs/greenfield/inference-result.md` in the project folder.
- No code changes — there's no code yet, and this skill doesn't scaffold any.
- No MCP tools.
- No tests, builds, or benchmarks.
