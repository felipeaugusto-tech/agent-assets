# GitHub Copilot -- IDE Rule Format Baseline

> Last verified: 2026-03

## Web Search Instructions

Before using this baseline, search the web for the latest GitHub Copilot custom instructions format:

**Search Queries:**
- `GitHub Copilot custom instructions copilot-instructions.md 2026`
- `GitHub Copilot project configuration instructions file`
- `copilot-instructions.md format site:docs.github.com`

If the search returns updated information, use that instead of this baseline. If the search fails or returns nothing relevant, proceed with this baseline.

## Baseline Format

### File Location

```
.github/
  copilot-instructions.md    # Single instruction file
```

GitHub Copilot uses a **single file** for all project-specific instructions. All rules, conventions, and context go into this one file.

### File Structure

The file is standard markdown. Copilot uses section headers to organize and reference relevant content. There is no frontmatter, no glob patterns, and no multi-file support for instructions.

```markdown
# {PROJECT_NAME} -- Copilot Instructions

## Project Identity
{Project description, tech stack}

## Coding Standards
{Naming, error handling, formatting}

## Testing Standards
{Test structure, naming, scenarios}

## Security Rules
{Non-negotiable security constraints}

## Area-Specific Guidelines
{Guidelines for specific parts of the codebase}

## Version Control
{Commit, branch, PR conventions}
```

### Key Behaviors

- **Single file:** All instructions go in `.github/copilot-instructions.md`. There is no multi-file or directory-based approach.
- **Always active:** All content in the file is available to Copilot at all times. There is no way to activate rules conditionally based on file patterns.
- **Markdown format:** Standard markdown with no special frontmatter or syntax.
- **Section-based organization:** Use clear markdown headers (##, ###) to organize content. Copilot uses headers for context relevance.
- **Automatic reading:** Copilot reads this file automatically when it exists in the repository. No additional configuration is needed.
- **No global instructions:** There is no user-level instruction file (unlike Claude Code's `~/.claude/CLAUDE.md` or Gemini's `~/.gemini/`).
- **No slash commands:** Copilot does not support custom slash commands defined in the repository (unlike Claude Code's `.claude/commands/`).

### Size Guidance

- Keep under 1000 lines. Copilot's context window is limited.
- Put the most important rules first (security, key constraints) since earlier content may have higher influence.
- Use concise phrasing -- this is instructions for an AI, not documentation for humans.
- If the file grows too large, prioritize rules that have the highest impact on code quality and security.

### Limitations Compared to Other IDEs

| Feature | Copilot | Cursor | Claude Code | Gemini |
|---------|---------|--------|-------------|--------|
| Multiple rule files | No | Yes (`.mdc`) | Partial (`CLAUDE.md` + commands) | Yes (multi-layer) |
| Glob-based activation | No | Yes | No | No |
| Custom commands/workflows | No | No | Yes (slash commands) | Yes (workflows) |
| Subdirectory scoping | No | No | Yes (subdirectory `CLAUDE.md`) | Yes (subdirectory `AGENTS.md`) |
| User-level global rules | No | No | Yes | Yes |
| Priority/override system | N/A | N/A | N/A | Yes (`GEMINI.md` > `AGENTS.md`) |

### Tips for Effective Copilot Instructions

1. **Lead with security rules** -- these are non-negotiable and should always be in context.
2. **Use consistent formatting** -- markdown tables and lists are more scannable than paragraphs.
3. **Include code examples** -- Copilot responds well to concrete examples of desired patterns.
4. **Be explicit about anti-patterns** -- "Do not" instructions are as valuable as "Do" instructions.
5. **Reference file paths** -- Help Copilot understand project structure by referencing actual paths.
