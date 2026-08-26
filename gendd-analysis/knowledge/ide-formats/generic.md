# Generic -- IDE Rule Format Baseline

> Last verified: 2026-03

## Web Search Instructions

No web search is needed for this format. This **is** the fallback format for IDEs that do not have a specific rule system or whose format is unknown.

## Purpose

The generic format provides a portable, IDE-agnostic way to store AI coding rules. It uses plain markdown files in a `.ai-rules/` directory. Any AI assistant can be pointed to this directory, and the format also serves as human-readable documentation.

Use this format when:
- The target IDE is not one of the known formats (Cursor, Claude Code, Gemini, Copilot)
- The target IDE's rule format is not yet documented
- The team wants a portable format that works across any tool
- The team wants to maintain rules in one place and adapt to specific IDE formats as needed

## Baseline Format

### Directory Structure

```
.ai-rules/
  README.md               # Explains the directory and how to use the files
  general.md              # Project identity, tech stack, key constraints
  coding-standards.md     # Naming, error handling, formatting, logging
  testing.md              # Test structure, naming, scenarios, mocking
  security.md             # Security rules (non-negotiable)
  {area-name}.md          # Additional area-specific files as needed
```

### File Format

- **Format:** Standard markdown
- **No frontmatter:** No YAML or special syntax required
- **No special naming:** Use descriptive lowercase filenames with hyphens
- **Self-contained:** Each file covers one area completely

### README.md

The README explains what the directory contains and how to use it with different IDEs. It should include:

1. Purpose of the directory
2. List of files with descriptions
3. Instructions for adapting to specific IDEs (Cursor, Claude Code, Copilot, Gemini)
4. Maintenance notes (how to regenerate/update)

### Key Characteristics

| Characteristic | Value |
|---------------|-------|
| File location | `.ai-rules/` directory |
| File format | Plain markdown |
| Frontmatter | None |
| Glob support | None |
| Auto-detection | None -- must be manually referenced |
| Subdirectory scoping | None |
| Multi-file | Yes -- one file per area |
| Cross-tool compatible | Yes -- portable to any tool |
| Human readable | Yes -- also serves as documentation |

### How to Use with Specific IDEs

| IDE | Adaptation |
|-----|-----------|
| Cursor | Copy content into `.cursor/rules/*.mdc` files, add MDC frontmatter |
| Claude Code | Consolidate into `CLAUDE.md`, extract workflows into `.claude/commands/` |
| Copilot | Consolidate into `.github/copilot-instructions.md` |
| Gemini | Copy into `AGENTS.md` (consolidated) or `.agent/rules/` (granular) |
| Other | Point the AI assistant to the `.ai-rules/` directory |

### When to Use This vs. IDE-Specific Formats

- **Use generic** when the team uses multiple IDEs and wants a single source of truth
- **Use generic** as a starting point, then generate IDE-specific formats from it
- **Use IDE-specific** when the team standardizes on one IDE and wants optimal integration
- **Use both** -- maintain generic as the source, generate IDE-specific as outputs
