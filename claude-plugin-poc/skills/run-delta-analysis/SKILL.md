---
name: run-delta-analysis
description: Compare a base ref against a head ref (PR, branch, release) to produce a changed-files impact report, documentation-update mapping, and risk matrix. Manual invocation only.
disable-model-invocation: true
---

# Run Delta Analysis

Answer "what actually changed, and what does it affect" for a PR review, a post-merge doc-triage pass, or pre-release changelog prep. Chat output, saved as one report file.

## 1. Fix the target and get the comparison range

The target is **the user's current repository**, never this plugin or the GenDD corpus.

Before anything else, get both ends of the comparison from the user if not already stated:

- **Base** — main, a release tag, or a commit SHA.
- **Head** — a feature branch, a PR, or "current" (uncommitted/working state).

Ask if either is ambiguous. Do not guess a baseline from context.

## 2. Load the reference (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/run-delta-analysis/run-delta-analysis.md` | **Primary task flow and output format** — the phases and the report template. |

Reading it as it is: verbatim corpus copy, describes a Cursor Chat workflow — adapt intent (you can read the repo and diff directly), ignore tool-specific mechanics.

## 3. Run the process

1. **Identify changed files** and categorize them (services/business logic, API/contracts, database/migrations, tests, configuration, documentation, infrastructure/CI, frontend/UI).
2. **Analyze impact per significant change** — what changed, why it matters, what depends on it, and a High/Medium/Low risk level.
3. **Map changes to documentation** — which existing doc sections are now stale, prioritized Must/Should/Nice-to-have.
4. **Assess risk** — a risk matrix (likelihood × impact × mitigation) and recommended actions split into immediate (before merge), post-merge, and future/tech-debt.
5. **Present the report** in the structure: Executive Summary, Changes Overview, Detailed Analysis (high-risk changes), Documentation Updates Required, Risk Matrix, Recommendations.

Adapt depth to what was asked — a full PR review needs all of the above; a focused "what changed in payment processing" needs only the relevant slice.

## 4. Never invent

A risk rating or a dependency claim not backed by an actual diff or an actual reference in the code is a guess. If you can't tell whether a change is breaking without more context, say so and ask, rather than picking a plausible severity.

## 5. Save output

Save to `docs/updates/delta-{date}.md` in the target repository, after presenting it in chat. If the user only wants the chat output, skip the file.

## 6. Hard limits

- Writes only `docs/updates/delta-*.md`, and only if the user wants the file saved — chat output is always fine on its own.
- No changes to source code, configuration, or build files.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
