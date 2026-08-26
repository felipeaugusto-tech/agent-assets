# Generate Architecture Diagrams

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | Architect, Tech Lead |
| **Prerequisites** | Repository cloned, understanding of project purpose and tech stack |
| **Inputs** | Path to target repository, project name, tech stack, key integrations, deployment environment |
| **Outputs** | C4 Mermaid diagrams: Context (L1), Container (L2), Component (L3), optional Code (L4), Deployment |

## When to Use

- Onboarding onto a project and need architecture visibility
- Preparing for Architecture Review Board (ARB)
- After significant architecture changes (new services, refactors, migrations)
- Documenting current vs. target state for a migration

## Before You Start

- [ ] Repository is cloned and accessible
- [ ] You know the project name, tech stack, and key integrations
- [ ] Optionally: brownfield analysis is complete (improves accuracy)

## Steps

### Step 1: Generate all C4 diagrams

- Do: Analyze the codebase and generate C4 architecture diagrams
- How: Use Cursor Chat:
  ```
  Read @GenDD-Flow/workflows/generate-architecture-diagrams.md

  Analyze @TargetRepo and generate C4 architecture diagrams:

  Project: [PROJECT NAME]
  Tech Stack: [TECHNOLOGIES]
  Key Integrations: [EXTERNAL SYSTEMS]

  Generate:
  1. C4 Context Diagram (Level 1)
  2. C4 Container Diagram (Level 2)
  3. C4 Component Diagram (Level 3)
  4. C4 Code Diagram (Level 4) - for core/complex components only
  5. C4 Deployment Diagram

  Output as Mermaid diagrams.
  Save to @TargetRepo/docs/architecture/
  ```
- Expect: Mermaid `.mmd` files for each diagram level in `docs/architecture/`

### Step 2: Review diagrams against C4 checklists

- Do: Validate each diagram meets C4 standards
- How: The workflow includes per-diagram checklists — verify scope statements, verb-phrase relationships, technology labels, and correct boundary usage
- Expect: Diagrams that accurately represent the system at each abstraction level

### Step 3: Store and share

- Do: Save diagrams and optionally export to Lucidchart/Confluence
- How: Commit `.mmd` files to `docs/architecture/`. Render PNGs via Mermaid CLI if needed.
- Expect: Version-controlled diagrams accessible to the team

## Expected Output

```
@TargetRepo/docs/architecture/
├── context-diagram.mmd
├── container-diagram.mmd
├── component-diagram.mmd
├── code-diagram-<ComponentName>.mmd   (optional)
└── deployment-diagram.mmd
```

**Save to:** `@TargetRepo/docs/architecture/`

## What's Next

- [ ] [Create Context Pack](create-context-pack.md) to include architecture.md referencing these diagrams
- [ ] [Run Delta Analysis](run-delta-analysis.md) after architecture changes to keep diagrams current
- [ ] [Update Documentation](../recurring/update-documentation.md) when architecture evolves

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Architecture Diagrams Workflow | `workflows/generate-architecture-diagrams.md` | Full workflow with C4 conventions, examples, and checklists |
| Architect Role Playbook | `playbooks/by-role/architect.md` | Role-specific architecture analysis |
| Brownfield Analysis | `playbooks/onboarding/run-brownfield-analysis.md` | Use as input for more accurate diagrams |
