# Claude Code -- IDE Rule Format Baseline

> Last verified: 2026-03

## Web Search Instructions

Before using this baseline, search the web for the latest Claude Code documentation:

**Search Queries:**
- `Claude Code CLAUDE.md format 2026`
- `Claude Code project instructions slash commands`
- `Claude Code .claude commands configuration site:docs.anthropic.com`

If the search returns updated information, use that instead of this baseline. If the search fails or returns nothing relevant, proceed with this baseline.

## Baseline Format

### File Locations

```
project-root/
  CLAUDE.md                    # Primary instruction file (read automatically)
  .claude/
    commands/
      review-pr.md             # Slash command: /review-pr
      generate-tests.md        # Slash command: /generate-tests
      {command-name}.md        # Slash command: /{command-name}
    skills/
      {skill-name}/
        SKILL.md               # Project skill (YAML frontmatter + body)
```

### CLAUDE.md (Primary Instructions)

- **Location:** Project root (`./CLAUDE.md`)
- **Read automatically:** Yes -- Claude Code reads this file on every interaction without any user action
- **Format:** Standard markdown (no frontmatter required)
- **Purpose:** Persistent project-wide instructions, constraints, and context

**Structure:**

```markdown
# {PROJECT_NAME}

{Brief project description}

## Tech Stack
{Language, framework, database, infrastructure}

## Key Rules
{Non-negotiable constraints: security, multi-tenant, compliance}

## Coding Conventions
{Naming, error handling, formatting}

## Testing
{Test structure, naming, required scenarios}

## Project Structure
{Directory layout}

## Further guidance
{Summarize important rules here; do not list paths to files that do not exist in this repository. Prefer slash commands under `.claude/commands/` for workflows.}
```

**Key Behaviors:**
- Claude Code reads `CLAUDE.md` from the project root
- In monorepos, `CLAUDE.md` files in subdirectories also apply when working in that directory (additive, not overriding)
- Content is injected into Claude's context on every interaction
- Keep concise -- long files consume context window

**Size Guidance:**
- Target under 500 lines
- For detailed guidance, reference **paths that exist in this repository** (or use slash commands); do not point at documentation trees that only existed in another repo or in the prompt bundle
- Focus on high-impact rules (security, key patterns) over exhaustive documentation

### .claude/commands/*.md (Slash Commands)

- **Location:** `.claude/commands/{command-name}.md`
- **Invocation:** User types `/{command-name}` in Claude Code
- **Format:** Standard markdown (no frontmatter)
- **Purpose:** On-demand workflows triggered by the user

**File Naming:**
- Filename (without `.md`) becomes the command name
- Use lowercase with hyphens: `review-pr.md` -> `/review-pr`
- Keep names short and descriptive

**Content:**
- Each file contains instructions for Claude to execute when the command is invoked
- Instructions should be self-contained -- include all context needed for the workflow
- Can reference files in the codebase by path

**Example:**

```markdown
# File: .claude/commands/review-pr.md
# Invoked as: /review-pr

Review the current PR for security, code quality, testing, and pattern consistency.

Check for:
1. Hardcoded secrets, missing input validation, SQL injection
2. Naming violations, missing error handling
3. Test coverage, AAA pattern, descriptive names
4. Consistency with existing codebase patterns

Output findings grouped by severity.
```

### Recommended Commands

| File | Command | Purpose |
|------|---------|---------|
| `review-pr.md` | `/review-pr` | Comprehensive PR review |
| `generate-tests.md` | `/generate-tests` | Generate tests for specified code |
| `check-security.md` | `/check-security` | Security audit |
| `explain.md` | `/explain` | Explain a module or area |
| `refactor.md` | `/refactor` | Suggest and implement refactoring |

### `.claude/skills/{skill-name}/SKILL.md` (Project skills)

- **Location:** `.claude/skills/{skill-name}/SKILL.md` (one directory per skill).
- **Format:** YAML frontmatter (`name`, `description`, optional fields) then markdown instructions.
- **Purpose:** Reusable capabilities; see Anthropic Claude Code “Skills” documentation for the current schema.

### Additional Features

- **User-level instructions:** Users can place a `CLAUDE.md` in `~/.claude/` for global instructions that apply to all projects.
- **No glob-based activation:** Unlike Cursor, there is no way to activate rules based on file patterns. All rules in `CLAUDE.md` are always active.
- **No priority system:** There is no override mechanism between root `CLAUDE.md` and subdirectory `CLAUDE.md` files -- they are additive.
