---
name: incremental-doc-update
description: Update only the documentation sections affected by recent code changes, without a full brownfield re-analysis. Manual invocation only.
disable-model-invocation: true
---

# Incremental Doc Update

For a repo with existing documentation that's drifted from the code after a PR, a release, or routine maintenance. Targeted re-analysis of what changed, not a full re-scan.

## 1. Fix the target and check it's the right tool

The target is **the user's current repository**, never this plugin or the GenDD corpus.

**Do NOT use this skill when:**
- The repository has no existing documentation — run `/gendd:run-brownfield-analysis` instead.
- Major architectural changes occurred (new services, changed patterns at the system level) — run full brownfield analysis instead.
- More than ~30% of the codebase changed — the targeted approach below assumes most of the doc set is still accurate; past that threshold, treat it as a fresh brownfield pass.

If any of these hold, say so and stop rather than producing a partial update that looks complete.

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/incremental-doc-update/incremental-doc-update.md` | **Primary task flow** — the five-step process below follows it. |
| `${CLAUDE_PLUGIN_ROOT}/references/incremental-doc-update/pass2-infer-agent.md` | Load at Step 3 — the targeted re-analysis method, applied only to changed components, not the whole repo. |
| `${CLAUDE_PLUGIN_ROOT}/references/incremental-doc-update/documentation-guidelines.md` | Load at Steps 4–5 — file-reference rules, size limits, the validation checklist. |

Reading these as they are: verbatim corpus copies, `@GenDD-Flow/...` and `@TargetRepo/...` links don't resolve here, describe a Cursor Chat workflow — adapt intent, ignore tool mechanics.

## 3. Run the process

1. **Run delta analysis first**, if it hasn't been already — this skill assumes it exists. Run `/gendd:run-delta-analysis` (base → head) if there's no delta report yet, or reuse an existing one.
2. **Map changes to documentation sections** — for each changed component, find the existing doc file and section it corresponds to, classified Critical (breaking/removed/security) / Important (new/significant) / Minor (typos/clarifications).
3. **Run a targeted re-analysis** on *only* the changed services, APIs, or data models — never the whole repository — using the existing documentation as baseline for what's still accurate.
4. **Update the specific affected files**, section by section: state what changed, reference the actual changed files, and follow the documentation-guidelines rules (no embedded code snippets, patterns not hard-coded counts, cross-references kept current).
5. **Validate**: every file reference resolves, no stale snippets, breaking changes are highlighted, format rules are respected.

## 4. Never invent

An update to a section you didn't actually re-analyze is a guess dressed as a fact. Touch only the sections the delta analysis and targeted re-analysis actually cover — leave everything else exactly as it was rather than "tidying" untouched areas.

## 5. Hard limits

- Writes only under `docs/` in the target repository, only to files/sections identified as affected in Step 2.
- Does not touch source code, configuration, or build files.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
- Does not re-run a full brownfield scan — that's a different skill, for a different situation (see §1).
