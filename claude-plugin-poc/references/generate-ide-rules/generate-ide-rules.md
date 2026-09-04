# Workflow: Generate IDE Rules

## Quick Start

```
Read @GenDD-Flow/workflows/generate-ide-rules.md

Using the context documents at @docs/context/ and standards at @docs/standards/,
generate IDE rules for my development environment.

I use: {Cursor | Claude Code | Antigravity | GitHub Copilot | Other}
```

## Overview

This workflow is **Phase 5** of the Analyze & Generate flow. It transforms the context documents and standards generated in Phases 3-4 into IDE-native rule files that guide AI assistants during development.

This is the final phase — it produces the files that developers interact with daily. The rules ensure that every AI-assisted coding session respects the project's architecture, conventions, security requirements, and quality standards.

## Prerequisites

- Completed Phase 3: Context documents at `docs/context/`
- Completed Phase 4 (optional): Standards at `docs/standards/`
- AI IDE with web search capability (for Step 2)
- Knowledge of which IDE the team uses

---

## Process

### Step 1: Identify Target IDE

Ask the user which IDE they use:

```
Which AI IDE do you use for development?

1. Cursor
2. Claude Code
3. Antigravity (Google)
4. GitHub Copilot
5. Other (please specify)

If your team uses multiple IDEs, I can generate rules for each.
```

### Step 2: Web Search for Latest Rule Format

IDE rule formats evolve frequently. Before generating, search for the current format to avoid producing outdated files.

#### Search Queries by IDE

| IDE | Search Query |
|-----|-------------|
| Cursor | `Cursor IDE rules configuration format site:docs.cursor.com OR site:cursor.com` |
| Claude Code | `Claude Code CLAUDE.md format configuration site:docs.anthropic.com` |
| Antigravity | `Google Antigravity GEMINI.md AGENTS.md rules format site:antigravity.google OR site:developers.googleblog.com` |
| GitHub Copilot | `GitHub Copilot instructions configuration site:docs.github.com` |

#### What to Extract from Search Results

- **Directory structure** — Where rule files live
- **File format** — Markdown, YAML, JSON, or custom format
- **Naming conventions** — File names, extensions, frontmatter
- **Metadata/frontmatter** — Required headers, tags, or configuration blocks
- **Scoping** — How to apply rules to specific file types or directories
- **Limitations** — Maximum file sizes, number of files, token limits

### Step 3: Handle Search Results

#### If web search returns current documentation:

1. Extract the format specification
2. Compare with the baseline in `knowledge/ide-formats/{ide}.md` (if it exists)
3. Use the **most current** format — prefer web search results over baseline
4. Note any breaking changes from previous format versions

#### If web search fails (offline, restricted, or no results):

1. Fall back to the baseline format in `knowledge/ide-formats/{ide}.md`
2. Warn the user:
   ```
   Note: I could not verify the latest IDE rule format via web search.
   Using the baseline format from GenDD-Flow knowledge base.
   The format may be outdated — please verify against your IDE's current
   documentation after generation.
   ```

### Step 4: Plan Rule File Structure

Map the context documents and standards into IDE-native rule files:

#### Rule Categories

| Rule File | Content Source | Scope |
|-----------|--------------|-------|
| General / Project Identity | `docs/context/technical-leadership.md`, `docs/context/architecture.md` | Always active |
| Coding Standards | `docs/standards/coding.md`, `docs/context/backend-development.md`, `docs/context/frontend-development.md` | All code files |
| Testing | `docs/standards/testing.md`, `docs/context/quality-assurance.md` | Test files (scope by glob if IDE supports it) |
| Security | `docs/standards/security.md`, `docs/context/security.md` | Always active |
| Database | `docs/context/database-management.md` | Migration and model files |
| Infrastructure | `docs/context/devops-infrastructure.md` | CI/CD and IaC files |
| Per-Area Rules | Remaining `docs/context/*.md` files | Relevant file scopes |

Not every category needs its own file. Consolidate based on IDE capabilities:
- If the IDE supports multiple rule files with scoping: use separate files
- If the IDE uses a single file: consolidate into sections

### Step 5: Transform Content to Rules

For each rule file, transform context and standards into directive-style instructions:

#### Transformation Guidelines

| Source Content | Transforms To |
|---------------|--------------|
| "The project uses Express.js with controller-service-repository pattern" | "When creating API endpoints, follow the controller-service-repository pattern. Controllers handle HTTP, services contain business logic, repositories handle data access." |
| "Authentication: JWT middleware in `middleware/auth.ts`" | "All new API routes under `/api/*` must include JWT authentication. Reference `middleware/auth.ts` for the authentication pattern." |
| "Test coverage required for all services" | "Write tests for all new service functions. Follow the existing test patterns in `__tests__/` using Jest. Test files should be co-located with source files." |

#### Rule Writing Principles

- **Directive voice** — "Do X" and "Do not Y", not "The project does X"
- **Specific over general** — Reference actual files and patterns
- **Actionable** — Each rule should directly guide AI behavior
- **Concise** — IDE context windows are limited; every line must earn its place
- **Prioritized** — Most important rules first (security, then architecture, then style)

### Step 6: Generate Files by IDE

#### Cursor

```
.cursor/
└── rules/
    ├── project.mdc           # Project identity + architecture
    ├── coding-standards.mdc  # Coding conventions + style
    ├── testing.mdc           # Test patterns + requirements
    ├── security.mdc          # Security rules (always active)
    └── {area}.mdc            # One per major SDLC area
```

Each `.mdc` file follows Cursor's rule format:
- Frontmatter with description and glob patterns (if scoping is supported)
- Markdown body with directive-style rules

#### Claude Code

```
CLAUDE.md                        # Main rules file (always loaded)
.claude/
└── commands/
    ├── review.md               # Code review command
    ├── test.md                 # Test generation command
    └── {custom-command}.md     # Custom commands per area
```

`CLAUDE.md` contains:
- Project identity and architecture overview
- Coding standards and conventions
- Security requirements
- Key file references

#### Antigravity (Google)

```
GEMINI.md                        # Main rules file
AGENTS.md                        # Agent definitions
.agent/
└── rules/
    ├── coding.md               # Coding standards
    ├── testing.md              # Test standards
    ├── security.md             # Security rules
    └── {area}.md               # Per-area rules
```

#### GitHub Copilot

```
.github/
└── copilot-instructions.md     # Single instructions file
```

Since Copilot uses a single file, consolidate all rules into sections:
- Project Overview
- Architecture
- Coding Standards
- Testing Requirements
- Security Rules

#### Other IDEs

```
.ai-rules/
├── project.md                  # Project identity
├── coding-standards.md         # Coding conventions
├── testing.md                  # Test patterns
├── security.md                 # Security rules
└── {area}.md                   # Per-area rules
```

Use generic Markdown format that can be manually imported into any IDE.

### Step 7: Verify Output

After generating all files:

1. **List all generated files** with their paths and sizes
2. **Confirm format compliance** — Check against the format spec from Step 2/3
3. **Check for completeness** — Every confirmed SDLC area should be represented
4. **Validate references** — File paths mentioned in rules should exist in the codebase

Present a summary to the user:

```
Generated IDE rules for {IDE}:

Files created:
- {path} ({lines} lines) — {description}
- {path} ({lines} lines) — {description}
...

Coverage:
- Architecture: covered in {file}
- Backend: covered in {file}
- Security: covered in {file}
...

To verify: Start a new AI chat session in your IDE and ask it about
your project. It should reference the conventions and patterns from
these rules.
```

---

## Multi-IDE Support

If the team uses multiple IDEs, run Steps 4-7 for each IDE. The content is the same; only the file format and location change.

```
Read @GenDD-Flow/workflows/generate-ide-rules.md

Generate IDE rules for both Cursor and Claude Code using the context
at @docs/context/ and standards at @docs/standards/.
```

---

## Updating Rules

When the codebase evolves, rules should be updated:

1. Re-run Phase 1 (or the incremental update workflow) to refresh brownfield analysis
2. Re-run Phase 3 to update context documents
3. Re-run Phase 5 to regenerate IDE rules

Alternatively, edit rules directly — they are just Markdown files.

---

## Output Artifacts

Depends on IDE choice. See Step 6 for the full listing per IDE.

---

## Verification Checklist

- [ ] IDE format verified via web search or baseline knowledge
- [ ] Rule files generated in correct location for the chosen IDE
- [ ] Rules are directive-style, not descriptive
- [ ] Security rules are always active (not scoped to specific files)
- [ ] File references in rules point to actual files in the codebase
- [ ] Each rule file is concise (under 200 lines)
- [ ] All confirmed SDLC areas are represented in at least one rule file
- [ ] User has been shown a summary of generated files

---

## Related Resources

> **Workflow:** This is Phase 5 of [analyze-and-generate.md](analyze-and-generate.md).
> **Previous Phase:** Standards detection at [detect-and-generate-standards.md](detect-and-generate-standards.md).
> **Knowledge:** IDE format baselines at `knowledge/ide-formats/`.
> **Context Input:** Documents at `docs/context/` from [generate-context-areas.md](generate-context-areas.md).
> **Standards Input:** Documents at `docs/standards/` from [detect-and-generate-standards.md](detect-and-generate-standards.md).
