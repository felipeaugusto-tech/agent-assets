# Cursor -- IDE Rule Format Baseline

> Last verified: 2026-03

## Web Search Instructions

Before using this baseline, search the web for the latest Cursor rules documentation:

**Search Queries:**
- `Cursor IDE rules format .mdc 2026`
- `Cursor AI rules configuration site:docs.cursor.com`
- `Cursor .cursor/rules mdc frontmatter`

If the search returns updated information, use that instead of this baseline. If the search fails or returns nothing relevant, proceed with this baseline.

## Baseline Format

### File Location

```
.cursor/
  rules/
    general.mdc
    coding-standards.mdc
    testing.mdc
    {area-name}.mdc
```

All rule files are placed in `.cursor/rules/` with the `.mdc` extension (Markdown Configuration).

### MDC Frontmatter

Every `.mdc` file starts with YAML frontmatter enclosed in `---` delimiters:

```yaml
---
description: Short description of when/why this rule applies
globs: "**/*.ts"          # File pattern(s) or empty for always-on
alwaysApply: true          # true = always active, false = Cursor decides
---
```

**Frontmatter Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | string | Yes | Cursor uses this to decide when to apply the rule. Write it as a concise statement of the rule's purpose. |
| `globs` | string or array | No | File glob patterns that activate this rule. Omit or leave empty for rules that apply everywhere. |
| `alwaysApply` | boolean | Yes | `true` = rule is always injected into context. `false` = Cursor decides based on relevance to the current task. |

**Globs Examples:**

```yaml
# Single pattern
globs: "**/*.ts"

# Multiple patterns (array)
globs:
  - "src/**/*.py"
  - "tests/**/*.py"

# No pattern (always-on rule)
globs:
```

### Content After Frontmatter

After the frontmatter, the rest of the file is standard markdown. Cursor reads this content and uses it as instructions for its AI assistant.

```markdown
---
description: Core project rules
alwaysApply: true
---

# Project Rules

Content here is read by Cursor's AI as instructions.
Use markdown formatting -- headers, lists, tables, code blocks.
```

### File Organization

Recommended file structure for a typical project:

| File | alwaysApply | globs | Purpose |
|------|-------------|-------|---------|
| `general.mdc` | true | (none) | Project identity, tech stack, security rules, key constraints. Always active. |
| `coding-standards.mdc` | true | (none) | Naming conventions, error handling, formatting, logging. Always active. |
| `testing.mdc` | false | `["**/*_test.*", "**/*.test.*", "**/*.spec.*", "tests/**/*"]` | Test naming, AAA pattern, mocking, scenarios. Active when working with test files. |
| `security.mdc` | true | (none) | Security rules. Always active because security applies everywhere. |
| `api.mdc` | false | `["src/api/**/*", "src/controllers/**/*", "src/routes/**/*"]` | API design rules. Active when working with API code. |
| `database.mdc` | false | `["src/models/**/*", "src/repositories/**/*", "migrations/**/*"]` | Database patterns, tenant isolation. Active when working with data layer. |
| `frontend.mdc` | false | `["src/components/**/*", "src/pages/**/*", "src/views/**/*"]` | Component patterns, accessibility, styling. Active when working with UI. |

### Key Behaviors

- **Context window:** Cursor injects active rules into the AI's context. Keep rules concise to avoid consuming too much context.
- **Relevance matching:** When `alwaysApply` is `false`, Cursor uses the `description` and `globs` to decide if a rule is relevant to the current task. Write clear descriptions.
- **No inheritance:** Rules do not inherit from each other. Each file is self-contained.
- **No subdirectory scoping:** Rules in `.cursor/rules/` apply project-wide (filtered by globs). There is no subdirectory-level scoping.
- **Order:** Multiple active rules are combined. If rules conflict, the behavior is undefined -- avoid contradictions between rule files.

### Size Guidance

- Keep individual rule files under 200 lines for optimal context usage.
- Use `alwaysApply: false` with specific globs for area-specific rules to reduce noise.
- The `general.mdc` (always-on) file should be the most concise since it is always in context.
