# Create Context Pack

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | Architect, Tech Lead, Backend Dev, Frontend Dev, Fullstack Dev |
| **Prerequisites** | Repository cloned, understanding of system purpose and tech stack |
| **Inputs** | Path to target repository, product name, tech stack, key integrations, compliance requirements |
| **Outputs** | Context Pack files: `agents.md`, `context.md`, `conventions.md`, `testing.md`, `architecture.md` |

## When to Use

- Setting up a new project for AI-assisted development
- Onboarding a repository to Cursor for the first time
- AI tools are making repeated mistakes due to missing context
- Multiple developers are getting inconsistent AI outputs
- After brownfield analysis, to create IDE-ready context from the findings

## Before You Start

- [ ] Repository is cloned and accessible
- [ ] You know the product name, tech stack, and key integrations
- [ ] You know compliance requirements (PCI, HIPAA, none, etc.)

## Steps

### Step 1: Generate the Context Pack

- Do: Analyze the codebase and create all five context files
- How: Use Cursor Chat:
  ```
  Read @GenDD-Flow/workflows/create-context-pack.md

  Analyze @TargetRepo and create a Context Pack:

  Product: [PRODUCT NAME]
  Purpose: [WHAT IT DOES]
  Tech Stack: [TECHNOLOGIES]
  Key Integrations: [EXTERNAL SYSTEMS]
  Compliance: [PCI/HIPAA/none]

  Generate:
  1. agents.md - AI instructions and constraints
  2. context.md - Domain knowledge and glossary
  3. conventions.md - Coding standards and patterns
  4. testing.md - Testing requirements
  5. architecture.md - System architecture overview

  Use @GenDD-Flow/templates/context-pack.md as the template.
  Save to @TargetRepo/.cursor/
  ```
- Expect: Five Markdown files in `.cursor/` with project-specific content

### Step 2: Validate the Context Pack

- Do: Test that the context produces accurate AI output
- How: Ask Cursor to generate a small piece of code using the new context and verify it follows conventions
- Expect: AI-generated code that matches actual project patterns

### Step 3: Commit and communicate

- Do: Commit the context pack and inform the team
- How: Commit to version control. Note in the commit message which files were created.
- Expect: Team members benefit from improved AI context on their next pull

## Expected Output

```
@TargetRepo/.cursor/
├── agents.md
├── context.md
├── conventions.md
├── testing.md
└── architecture.md
```

**Save to:** `@TargetRepo/.cursor/`

## What's Next

- [ ] [Generate Architecture Diagrams](generate-architecture-diagrams.md) so architecture.md can reference C4 diagrams
- [ ] [Refresh Context Pack](../recurring/refresh-context-pack.md) quarterly or after major changes
- [ ] [Identify Test Gaps](identify-test-gaps.md) using the testing standards defined in testing.md

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Context Pack Workflow | `workflows/create-context-pack.md` | Full workflow with per-file phases, examples, and maintenance guidance |
| Context Pack Template | `templates/context-pack.md` | Universal principles for security, testing, code quality, logging, version control |
| Refresh Context Pack | `playbooks/recurring/refresh-context-pack.md` | Periodic refresh of existing context packs |
