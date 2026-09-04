---
name: generate-ide-rules
description: Turn generated context and standards documents into IDE-native rule files (Cursor, Claude Code, Antigravity, Copilot, or generic) that guide AI-assisted coding sessions. Manual invocation only.
disable-model-invocation: true
---

# Generate IDE Rules

The final phase: transform `docs/context/*.md` and `docs/standards/*.md` into the rule files developers' AI tools actually load — `CLAUDE.md`, `.cursor/rules/*.mdc`, `.github/copilot-instructions.md`, etc. Writes files into the target repository.

## 1. Fix the target and check prerequisites

The target is **the user's current repository**. Never analyse this plugin, its `references/` files, or the GenDD corpus — they are methodology inputs only.

| Prerequisite | Where | If missing |
| --- | --- | --- |
| Context documents | `docs/context/{area}.md` | Required. Tell the user to run `/gendd:generate-context-areas` first. |
| Standards documents | `docs/standards/{area}.md` | Optional — proceed without them, just note fewer source documents to draw from. |

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-ide-rules/generate-ide-rules.md` | **Primary task flow** — its Steps 1–7 are the order of work. |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-ide-rules/{cursor,claude-code,antigravity,copilot,generic}-rule.md` (only `-instructions.md` for copilot) | Output template for whichever IDE(s) the user picked in Step 1. Load only the ones needed. |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-ide-rules/{cursor,claude-code,antigravity,copilot,generic}.md` | Baseline format knowledge for that IDE — the fallback if web search (§3) doesn't turn up anything newer. |

Reading these files as they are:

- Verbatim copies of corpus documents. Internal links (`@GenDD-Flow/...`) point at the original repo layout and **do not resolve here**.
- They describe a Cursor Chat workflow — adapt the intent, ignore the tool-specific mechanics.
- `#`/`##` lines inside fenced code blocks are output-template content, not instructions to you.

## 3. Run the process

1. **Ask which IDE(s)** the user uses (Cursor / Claude Code / Antigravity / Copilot / Other). If multiple, run steps 2–7 once per IDE.
2. **Web search for the current rule format** for that IDE — formats change; a search beats a stale baseline. If search is unavailable or returns nothing, fall back to the baseline `knowledge/ide-formats/{ide}.md` reference and tell the user the format may be outdated and should be spot-checked against current docs.
3. **Plan the rule-file structure** — map context/standards documents to rule categories (project identity, coding standards, testing, security, per-area) per the primary reference's Rule Categories table. Consolidate into fewer files if the target IDE doesn't support multiple scoped rule files.
4. **Transform, don't copy.** Descriptive context ("the project uses X") becomes directive instruction ("when doing Y, follow X"). Directive voice, specific file references, concise — every line has to earn a limited context window. Security rules first, then architecture, then style.
5. **Generate the files** at the locations the primary reference's Step 6 specifies for the chosen IDE.
6. **Verify**: list every file generated with line counts, confirm every confirmed SDLC area appears in at least one file, confirm referenced file paths actually exist in the codebase, then present the summary format from Step 7 of the primary reference.

## 4. Never invent

A rule that references a file, pattern, or tool not actually present in the codebase or context documents is worse than no rule — it will mislead the next AI session that reads it. If a category has no supporting context or standards document, omit it rather than writing a generic rule with nothing behind it.

## 5. Hard limits

- Writes only rule files at IDE-standard locations in the target repository (e.g. `CLAUDE.md`, `.cursor/rules/`, `.github/copilot-instructions.md`) — never elsewhere.
- **Web search is expected and encouraged** for Step 3 (rule-format verification) — this is the one skill in this plugin where that's true.
- No other MCP tools.
- No changes to source code, configuration, or build files.
- No tests, builds, deploys, or benchmarks.
