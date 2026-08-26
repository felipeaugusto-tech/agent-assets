# Run Full Analysis

| Field | Value |
|-------|-------|
| **Category** | onboarding |
| **Prerequisites** | Repository cloned locally, GenDD-Flow repo available, ability to build/run the project |
| **Inputs** | Path to the target repository (`@TargetRepo`), target IDE (Cursor, Claude Code, Antigravity, Copilot, etc.) |
| **Outputs** | `docs/context/` per-area context files, `docs/standards/` coding and SDLC standards, IDE-specific agent rules |

## When to Use

- First-time analysis of a new repository
- Major refactor completed and documentation needs a full reset
- Switching IDE and need to regenerate everything from scratch
- Adopting GenDD-Flow on a repository for the first time

## Before You Start

- [ ] Target repository is cloned and accessible locally
- [ ] You can build and run the project (or at least read the build config)
- [ ] GenDD-Flow repo is available at a known path
- [ ] You have access to CI/CD configuration (for operational context)
- [ ] You know which IDE you will target for rule generation
- [ ] Identify project size: **small/medium** (< 100 files) or **large** (100+ files)

> **Shortcut:** If a brownfield analysis already exists at `@TargetRepo/docs/brownfield/`, you can skip directly to Phase 2 (30-60 min instead of 2-4 hours). The brownfield output serves as input for area detection.

## Steps

### Phase 1: Brownfield Analysis (if needed)

- Do: Generate a structured understanding of the repository via the 4-pass brownfield analysis
- How: Follow the steps in [Run Brownfield Analysis](run-brownfield-analysis.md)
- Expect: `@TargetRepo/docs/brownfield/` with scan findings, architecture inferences, validation packet, and system documentation
- Time: 1-2 hours

> **Large projects (100+ files):** Use separate chat sessions per pass to manage context window pressure. See the brownfield playbook for details.

**Skip condition:** If `@TargetRepo/docs/brownfield/` already exists and is current, proceed to Phase 2.

### Phase 2: Detect Context Areas

- Do: Identify which SDLC areas are relevant to this repository
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/analyze-and-generate.md

  Using the brownfield analysis at @TargetRepo/docs/brownfield/,
  detect which SDLC context areas apply to this repository.

  Consider areas such as:
  - Architecture, API design, data model
  - Frontend patterns, backend patterns
  - Testing strategy, CI/CD, deployment
  - Security, observability, error handling
  - Domain concepts, integrations

  Output a prioritized list of areas with rationale.
  ```
- Expect: A list of 5-15 context areas ranked by relevance

### Phase 3: Generate Context per Area

- Do: Create context documents for each detected area
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/generate-context-areas.md

  For each detected area, generate a context document at:
  @TargetRepo/docs/context/{area-name}.md

  Each document should include:
  1. Area overview and scope
  2. Current patterns found in the codebase
  3. Key files and references (no embedded code)
  4. Conventions and rules
  5. Known gaps or risks

  Follow documentation guidelines: file references only, no hard-coded counts, no content duplication.
  ```
- Expect: `@TargetRepo/docs/context/` with one file per area

**Review checkpoint:** Verify all detected areas have context documents and the content is accurate.

### Phase 4: Generate Standards

- Do: Create standards documents for relevant SDLC areas
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/detect-and-generate-standards.md

  Using the context areas at @TargetRepo/docs/context/,
  generate standards for this repository.

  Save to @TargetRepo/docs/standards/
  ```
- Expect: `@TargetRepo/docs/standards/` with standards documents per area

### Phase 5: Generate IDE Rules

- Do: Generate agent rules specific to your IDE
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/generate-ide-rules.md

  Using the context at @TargetRepo/docs/context/ and standards at @TargetRepo/docs/standards/,
  generate IDE-specific rules for: [YOUR IDE - e.g., Cursor, Claude Code, Antigravity, Copilot]

  Save to the appropriate location for the target IDE.
  ```
- Expect: IDE-specific rule files in the correct location (e.g., `.cursor/`, `.claude/`, `.antigravity/`, `.github/copilot/`)

### Step 6: Run quality checklist

- Do: Verify the output meets GenDD-Flow requirements
- How: Check these items against the output:
  - [ ] No embedded code snippets (file references only)
  - [ ] No hard-coded counts (patterns instead)
  - [ ] No content duplication across context files (cross-references used)
  - [ ] Context files cover all relevant SDLC areas
  - [ ] Standards are actionable and measurable
  - [ ] IDE rules reference the context and standards correctly
  - [ ] New engineers can understand the system from the docs
- Expect: All items checked. Fix any gaps before considering the analysis complete.

## Expected Output

### Small/Medium Projects
```
TargetRepo/
├── docs/
│   ├── brownfield/          # Phase 1 output (if run)
│   │   ├── pass1-scan-findings.md
│   │   ├── pass2-infer-findings.md
│   │   ├── pass3-validation-responses.md
│   │   └── gendd/
│   │       ├── README.md
│   │       ├── stack.json
│   │       ├── overview/
│   │       │   ├── system-summary.md
│   │       │   └── tech-stack.md
│   │       ├── architecture/
│   │       │   ├── overview.md
│   │       │   ├── components.md
│   │       │   └── data-ownership.md
│   │       ├── risks/
│   │       │   ├── risk-hotspots.md
│   │       │   └── open-questions.md
│   │       ├── onboarding/
│   │       │   └── guide.md
│   │       └── flows/
│   │           └── {flow-name}.md
│   ├── context/             # Phase 3 output
│   │   ├── architecture.md
│   │   ├── api-design.md
│   │   ├── testing.md
│   │   ├── security.md
│   │   └── {area}.md
│   └── standards/           # Phase 4 output
│       ├── coding.md
│       ├── testing.md
│       └── {area}.md
└── .cursor/                 # Phase 5 output (IDE-specific)
    └── rules.md
```

### Large Projects
```
TargetRepo/
├── docs/
│   ├── brownfield/          # Phase 1 output
│   │   ├── pass1-scan-findings.md
│   │   ├── pass2-infer-findings.md
│   │   ├── pass3-validation-responses.md
│   │   └── gendd/
│   │       ├── README.md
│   │       ├── stack.json
│   │       ├── overview/
│   │       │   ├── system-summary.md
│   │       │   └── tech-stack.md
│   │       ├── architecture/
│   │       │   ├── overview.md
│   │       │   ├── components.md
│   │       │   └── data-ownership.md
│   │       ├── risks/
│   │       │   ├── risk-hotspots.md
│   │       │   └── open-questions.md
│   │       ├── onboarding/
│   │       │   └── guide.md
│   │       └── flows/
│   │           └── {flow-name}.md
│   ├── context/             # Phase 3 output
│   │   ├── architecture.md
│   │   ├── api-design.md
│   │   ├── frontend.md
│   │   ├── backend.md
│   │   ├── data-model.md
│   │   ├── testing.md
│   │   ├── ci-cd.md
│   │   ├── security.md
│   │   ├── observability.md
│   │   └── {area}.md
│   └── standards/           # Phase 4 output
│       ├── coding.md
│       ├── testing.md
│       ├── api.md
│       ├── security.md
│       └── {area}.md
└── .cursor/                 # Phase 5 output (or IDE-specific location)
    └── rules.md
```

**Time Estimate:** 2-4 hours (full analysis) or 30-60 min (skip to Phase 2 if brownfield exists)

## What's Next

- [ ] [Generate IDE Rules](../on-demand/generate-ide-rules.md) for additional IDEs
- [ ] [Generate Standards](../on-demand/generate-standards.md) for specific SDLC areas not covered
- [ ] [Generate Architecture Diagrams](../on-demand/generate-architecture-diagrams.md) from the context
- [ ] [Identify Test Gaps](../on-demand/identify-test-gaps.md) from the context and standards
- [ ] Schedule quarterly [Refresh Context Areas](../recurring/refresh-context-areas.md)

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Brownfield Analysis | `playbooks/onboarding/run-brownfield-analysis.md` | 4-pass brownfield analysis (Phase 1) |
| Analyze & Generate Workflow | `workflows/analyze-and-generate.md` | Master workflow for the 5-phase flow |
| Generate Context Areas | `workflows/generate-context-areas.md` | Context document generation |
| Generate IDE Rules | `workflows/generate-ide-rules.md` | IDE-specific rule generation |
| Detect & Generate Standards | `workflows/detect-and-generate-standards.md` | Standards generation |
| Documentation Guidelines | `templates/documentation-guidelines.md` | File reference and size rules |
