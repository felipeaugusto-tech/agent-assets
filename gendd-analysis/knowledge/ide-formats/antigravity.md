# Google Antigravity (Gemini) -- IDE Rule Format Baseline

> Last verified: 2026-03

## Web Search Instructions

Before using this baseline, search the web for the latest Gemini/Antigravity rule format:

**Search Queries:**
- `Google Gemini IDE agent rules GEMINI.md AGENTS.md 2026`
- `Antigravity AI coding agent rules format`
- `Gemini Code Assist custom instructions .agent rules`

If the search returns updated information, use that instead of this baseline. If the search fails or returns nothing relevant, proceed with this baseline.

## Baseline Format

### File Locations and Priority

Antigravity uses a layered file system with defined priority order:

```
project-root/
  GEMINI.md                     # 1. Highest priority -- IDE-specific
  AGENTS.md                     # 2. Cross-tool standard
  .agent/
    rules/
      security.md               # 3. Granular area rules
      testing.md
      {area-name}.md
    workflows/
      review-code.md            # 4. On-demand workflows (optional)
      {workflow-name}.md
    skills/
      generate-tests.md         # 5. Reusable skills (optional)
      {skill-name}.md
```

**Priority Order (Highest to Lowest):**

| Priority | File | Scope |
|----------|------|-------|
| 1 (highest) | `GEMINI.md` | IDE-specific rules for Gemini. Overrides everything below. |
| 2 | `AGENTS.md` | Cross-tool rules. Also works in Cursor and Claude Code. |
| 3 | `.agent/rules/*.md` | Granular, area-specific rules |
| 4 | `.agent/workflows/*.md` | On-demand workflows |
| 5 | `.agent/skills/*.md` | Reusable skill definitions |

### Global Rules (User-Level)

Users can define rules that apply across all projects:

```
~/.gemini/
  GEMINI.md    # User-level IDE-specific rules
  AGENTS.md    # User-level cross-tool rules
```

Project-level rules take priority over global (user-level) rules.

### GEMINI.md

- **Location:** Project root
- **Priority:** Highest
- **Format:** Standard markdown (no frontmatter)
- **Purpose:** Gemini-specific behavior, overrides, and project identity
- **Cross-tool:** No -- only read by Gemini

Use this file for:
- Gemini-specific output format preferences
- Overrides when `AGENTS.md` rules need Gemini-specific adjustments
- High-priority rules that must always apply in Gemini

### AGENTS.md

- **Location:** Project root (and optionally in subdirectories)
- **Priority:** Second to `GEMINI.md`
- **Format:** Standard markdown (no frontmatter)
- **Purpose:** Cross-tool rules that work in Gemini, Cursor, and Claude Code
- **Cross-tool:** Yes -- recognized by multiple AI coding tools

**Subdirectory Scoping:**
`AGENTS.md` can be placed in subdirectories to scope rules:

```
project-root/
  AGENTS.md                  # Root-level rules (apply everywhere)
  packages/
    api/
      AGENTS.md              # API-specific rules (apply in this directory)
    frontend/
      AGENTS.md              # Frontend-specific rules (apply in this directory)
```

Subdirectory `AGENTS.md` files are additive -- they do not replace root-level rules.

### .agent/rules/*.md

- **Location:** `.agent/rules/` directory
- **Format:** Standard markdown (no frontmatter)
- **Purpose:** Granular rules for specific areas, one file per area
- **Naming:** Lowercase with hyphens (`security.md`, `coding-standards.md`)

These files provide detailed guidance for specific SDLC areas without bloating the root-level files.

### .agent/workflows/*.md

- **Location:** `.agent/workflows/` directory
- **Format:** Standard markdown
- **Purpose:** On-demand workflows that can be invoked by the user
- **Optional:** Only create if the project needs specific workflows

Similar to Claude Code slash commands -- each file defines a workflow the AI can execute on request.

### .agent/skills/*.md

- **Location:** `.agent/skills/` directory
- **Format:** Standard markdown
- **Purpose:** Reusable skill definitions the agent can reference
- **Optional:** Only create if the project needs reusable skills

Skills differ from workflows in that they are capabilities the agent can use as building blocks, not standalone tasks.

### Key Behaviors

- **GEMINI.md overrides AGENTS.md:** If both files exist and contain conflicting rules, `GEMINI.md` wins within Gemini.
- **AGENTS.md is portable:** This file works across multiple IDEs, making it the best investment for cross-tool teams.
- **No glob-based activation:** Unlike Cursor, there is no frontmatter to control when rules apply based on file patterns. All rules are always available.
- **Subdirectory scoping:** Only `AGENTS.md` supports subdirectory placement. `GEMINI.md` is only read from the project root.
- **Additive rules:** Rules from different files and directories are combined, not replaced.

### Size Guidance

- `GEMINI.md`: Keep short (under 200 lines). Only Gemini-specific overrides and high-priority rules.
- `AGENTS.md`: Moderate length (under 500 lines). Core project rules.
- `.agent/rules/*.md`: Each file under 200 lines. One area per file.
- Prefer many focused files over few large files.
