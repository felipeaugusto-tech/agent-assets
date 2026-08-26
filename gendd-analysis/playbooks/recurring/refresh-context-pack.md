# Refresh Context Pack

| Field | Value |
|-------|-------|
| **Category** | recurring |
| **Target Roles** | Tech Lead, Architect |
| **Prerequisites** | Existing context pack in `.cursor/` folder, significant changes since last refresh |
| **Inputs** | Path to target repository, list of changes since last context pack update |
| **Outputs** | Updated context pack files (`agents.md`, `context.md`, `conventions.md`, `testing.md`, `architecture.md`) |

## When to Use

- After significant architecture changes (new services, changed patterns)
- When AI tools are making repeated mistakes due to stale context
- When new integrations are added or removed
- When coding conventions or testing standards change
- Quarterly maintenance to keep context pack current

## Before You Start

- [ ] Existing context pack files are in `@TargetRepo/.cursor/` or `@TargetRepo/docs/cursor/`
- [ ] You know what changed since the last context pack update
- [ ] You have access to the codebase to verify current patterns

## Steps

### Step 1: Identify what changed

- Do: Determine which context pack files need updates
- How: Review recent changes and map to context files:
  - Architecture changes -> `architecture.md`
  - New conventions or patterns -> `conventions.md`
  - New integrations or domain concepts -> `context.md`
  - New test frameworks or standards -> `testing.md`
  - New security/compliance constraints -> `agents.md`
- Expect: A list of files that need updating

### Step 2: Refresh affected files

- Do: Re-generate or update the stale context pack files
- How: Use Cursor Chat:
  ```
  Read @GenDD-Flow/workflows/create-context-pack.md

  The existing context pack at @TargetRepo/.cursor/ needs refreshing.

  Changes since last update:
  - [LIST CHANGES]

  Review and update the affected files:
  - [LIST FILES TO UPDATE]

  Ensure:
  1. Use actual code examples from the current codebase
  2. Preserve accurate existing content
  3. Update outdated information
  ```
- Expect: Updated context pack files reflecting current codebase

### Step 3: Validate updated context

- Do: Test that the refreshed context produces accurate AI output
- How: Ask Cursor to generate code using the updated context and verify it follows current patterns
- Expect: AI-generated code that matches current conventions

### Step 4: Commit and communicate

- Do: Commit the updated context pack and notify the team
- How: Commit changes, note what was updated in the commit message, and inform team members
- Expect: Team aware of context pack refresh and any notable changes

## Expected Output

```
@TargetRepo/.cursor/
├── agents.md           # Updated AI constraints
├── context.md          # Updated domain knowledge
├── conventions.md      # Updated coding patterns
├── testing.md          # Updated test standards
└── architecture.md     # Updated architecture overview
```

**Save to:** `@TargetRepo/.cursor/`

## What's Next

- [ ] [Generate Architecture Diagrams](../on-demand/generate-architecture-diagrams.md) if architecture.md changed significantly
- [ ] [Update Documentation](update-documentation.md) for broader documentation refresh
- [ ] Schedule next refresh (quarterly or after major changes)

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Context Pack Workflow | `workflows/create-context-pack.md` | Full creation workflow |
| Context Pack Template | `templates/context-pack.md` | Universal principles (security, testing, code quality, logging, version control) |
