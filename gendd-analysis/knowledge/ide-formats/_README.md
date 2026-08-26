# IDE Formats -- Baseline Knowledge

## Purpose

The files in this directory are **baseline snapshots** of each IDE's AI rule format. They document the file structure, naming conventions, frontmatter syntax, and organizational patterns that each IDE expects.

## How These Baselines Are Used

The primary discovery method for IDE rule formats is **web search**. The `workflows/generate-ide-rules.md` workflow instructs the AI agent to:

1. **Search the web first** for the latest documentation on the target IDE's rule format
2. **Fall back to these baselines** if the web search fails or returns no results
3. **Merge discoveries** -- if the web search reveals updates, use the latest information but keep these baselines as a structural reference

This approach ensures that generated rules use the most current format, even as IDE vendors update their rule systems between GenDD-Flow releases.

## Files

| File | IDE | Format |
|------|-----|--------|
| `cursor.md` | Cursor | `.cursor/rules/*.mdc` with MDC frontmatter |
| `claude-code.md` | Claude Code | `CLAUDE.md` + `.claude/commands/*.md` |
| `antigravity.md` | Google Antigravity (Gemini) | `GEMINI.md` + `AGENTS.md` + `.agent/rules/*.md` |
| `copilot.md` | GitHub Copilot | `.github/copilot-instructions.md` |
| `generic.md` | Any / Unknown | `.ai-rules/` directory with plain markdown |

## Last Verified

All baselines in this directory were last verified against official documentation in **2026-03**.

## Updating These Baselines

When you discover that an IDE has changed its rule format:

1. Update the relevant file in this directory
2. Update the "Last verified" date in the file
3. Update the "Last Verified" date in this README
4. Note what changed in the file's changelog section (if present)

These baselines do not need to be exhaustively detailed -- they need to capture enough structure for the AI to generate valid rule files when a web search is unavailable.
