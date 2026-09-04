# Generate Standards

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Prerequisites** | Repository cloned locally, understanding of which SDLC areas need standards |
| **Inputs** | Path to the target repository (`@TargetRepo`), SDLC area(s) to generate standards for, scope (project or org level) |
| **Outputs** | Standards documents in `docs/standards/` |

## When to Use

- Team needs documented standards for a specific SDLC area (testing, API design, security, etc.)
- Organization wants to standardize practices across multiple repositories
- Compliance requirement demands documented engineering standards
- New area of the codebase needs conventions established before development begins
- Existing informal conventions need to be formalized

## Before You Start

- [ ] Target repository is cloned and accessible locally
- [ ] You know which SDLC area(s) need standards
- [ ] (Recommended) `docs/context/` exists with context area files
- [ ] You have decided on scope: project-level or organization-level
- [ ] GenDD-Flow repo is available at a known path

> **No context yet?** Standards can be generated standalone, but they are more accurate when context areas exist. Run [Full Analysis](../onboarding/run-full-analysis.md) Phases 2-3 first for best results.

## Available SDLC Areas

| Area | What It Covers |
|------|---------------|
| Coding | Naming, structure, error handling, logging |
| Testing | Frameworks, coverage, naming, required scenarios |
| API Design | REST conventions, response formats, versioning |
| Security | Authentication, authorization, data protection |
| CI/CD | Pipeline stages, quality gates, deployment |
| Observability | Logging, metrics, alerting, tracing |
| Data | Schema design, migrations, query patterns |
| Frontend | Component patterns, state management, accessibility |
| Documentation | Doc standards, ADRs, API docs |

## Steps

### Step 1: Choose area and scope

- Do: Decide which area(s) to generate standards for and at what scope
- How: Review the available areas above. Determine if standards apply to a single project or across the organization.
- Expect: A clear list of areas and the target scope

### Step 2: Generate standards

- Do: Create standards documents for the selected areas
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/detect-and-generate-standards.md

  Generate standards for the following area(s):
  - [AREA 1 - e.g., Testing]
  - [AREA 2 - e.g., API Design]

  Scope: [project / organization]

  Context:
  - Repository: @TargetRepo
  - Tech Stack: [TECHNOLOGIES]
  - Existing context: @TargetRepo/docs/context/ (if available)

  For each area, generate:
  1. Purpose and scope of the standard
  2. Rules and conventions (actionable, measurable)
  3. Examples from the codebase (file references, not embedded code)
  4. Anti-patterns to avoid
  5. Enforcement approach (linting, code review, CI checks)

  Save to @TargetRepo/docs/standards/{area}.md
  ```
- Expect: Standards documents for each selected area

### Step 3: Review and refine

- Do: Verify standards are actionable and not overly prescriptive
- How: Check each standard against these criteria:
  - Is it measurable? (Can you tell if code follows it?)
  - Is it practical? (Can developers follow it without excessive overhead?)
  - Is it consistent with existing codebase patterns?
  - Does it include concrete examples?
- Expect: Refined standards that the team can realistically adopt

### Step 4: Generate for all areas (optional)

- Do: Generate standards for all applicable areas at once
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/detect-and-generate-standards.md

  Detect all applicable SDLC areas for @TargetRepo and generate
  standards for each one. Use existing context at @TargetRepo/docs/context/
  to inform the standards.

  Save to @TargetRepo/docs/standards/
  ```
- Expect: Complete standards coverage across all relevant areas

### Step 5: Communicate and enforce

- Do: Share standards with the team and set up enforcement
- How: Add standards to onboarding materials, configure linters where applicable, reference in PR templates
- Expect: Team awareness and consistent adoption

## Expected Output

```
TargetRepo/
└── docs/standards/
    ├── coding.md           # Coding conventions and patterns
    ├── testing.md          # Testing standards and requirements
    ├── api-design.md       # API design standards
    ├── security.md         # Security standards
    └── {area}.md           # Additional area standards
```

**Save to:** `@TargetRepo/docs/standards/`

## What's Next

- [ ] [Generate IDE Rules](generate-ide-rules.md) to enforce standards through IDE agent rules
- [ ] [Refresh Context Areas](../recurring/refresh-context-areas.md) to keep context aligned with standards
- [ ] [Identify Test Gaps](identify-test-gaps.md) using the testing standards as a baseline
- [ ] Schedule periodic review to keep standards current

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Detect & Generate Standards Workflow | `workflows/detect-and-generate-standards.md` | Detailed standards generation workflow |
| Standards Templates | `templates/standards/` | Templates for standards documents |
| Full Analysis Playbook | `playbooks/onboarding/run-full-analysis.md` | Generates context that informs standards |
