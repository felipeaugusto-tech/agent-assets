# Update Documentation Incrementally

| Field | Value |
|-------|-------|
| **Category** | recurring |
| **Target Roles** | Technical Writer, Tech Lead, Architect |
| **Prerequisites** | Existing documentation in the repository, identifiable baseline for changes |
| **Inputs** | Target repository path, baseline reference (commit/tag/branch), existing docs location |
| **Outputs** | Updated documentation files, delta analysis record, validation checklist |

## When to Use

- After a PR is merged that includes significant code changes
- After a release to bring documentation up to date
- When documentation drift is detected during reviews
- On a regular maintenance cadence (e.g., end of sprint)

## Before You Start

- [ ] Repository has existing documentation (if not, run full brownfield analysis first)
- [ ] You know the baseline (last documented state, release tag, or commit)
- [ ] Less than 30% of codebase changed since baseline (otherwise run full brownfield)
- [ ] No major architectural changes occurred (otherwise run full brownfield)

## Steps

### Step 1: Run delta analysis

- Do: Identify what changed since the last documented state
- How: Use Cursor Chat:
  ```
  Read @GenDD-Flow/workflows/incremental-doc-update.md
  Read @GenDD-Flow/playbooks/on-demand/run-delta-analysis.md

  Perform incremental documentation update for @TargetRepo:

  Changes since: [BASELINE - commit/tag/branch]

  1. Run delta analysis to identify changes
  2. Map changes to existing documentation
  3. Identify update priority (Critical/Important/Minor)
  ```
- Expect: Delta analysis with changed files categorized and mapped to documentation sections

### Step 2: Map changes to documentation sections

- Do: Create a mapping of code changes to affected doc files
- How: Review the delta output and create:
  ```
  | Changed Component | Existing Doc File | Section | Update Type |
  |-------------------|-------------------|---------|-------------|
  ```
- Expect: Clear mapping of which doc sections need updating

### Step 3: Run targeted analysis on affected areas

- Do: Analyze only the changed components, not the entire repository
- How: Use targeted prompts for each change type:
  - Service changes: Update service descriptions, dependencies, flows
  - API changes: Update endpoint documentation, request/response changes
  - Data model changes: Update entity relationships, migration notes
- Expect: Updated content for each affected section

### Step 4: Update specific documentation files

- Do: Apply the targeted analysis to update docs
- How: For each affected file, update the relevant sections while preserving unchanged content
- Expect: Documentation files updated with current information

### Step 5: Validate documentation updates

- Do: Verify updates meet documentation standards
- How: Check the validation checklist:
  - [ ] All file references exist and are correct
  - [ ] No outdated code snippets embedded
  - [ ] Cross-references point to valid sections
  - [ ] Breaking changes highlighted
  - [ ] New features have examples
  - [ ] Proper markdown formatting
- Expect: All checklist items pass

## Expected Output

```
@TargetRepo/docs/
├── updates/
│   └── delta-[date].md           # Delta analysis record
├── brownfield/                   # Updated files (if needed)
├── architecture/                 # Updated architecture docs
├── flows/                        # Updated flow docs
└── risks/                        # Updated risk docs
```

**Save to:** `@TargetRepo/docs/`

## What's Next

- [ ] [Run Delta Analysis](../on-demand/run-delta-analysis.md) for deeper change impact assessment
- [ ] [Refresh Context Pack](refresh-context-pack.md) if conventions or architecture changed
- [ ] [Generate Architecture Diagrams](../on-demand/generate-architecture-diagrams.md) if architecture evolved
- [ ] Schedule next documentation review cycle

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Incremental Doc Update Workflow | `workflows/incremental-doc-update.md` | Full 5-step workflow with automation hooks |
| Delta Analysis Playbook | `playbooks/on-demand/run-delta-analysis.md` | Change impact analysis playbook |
