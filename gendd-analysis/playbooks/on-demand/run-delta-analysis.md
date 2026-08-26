# Run Delta Analysis on Changes

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | Architect, Tech Lead, Engineering Manager |
| **Prerequisites** | Repository access, identifiable baseline (commit SHA, branch, or release tag) |
| **Inputs** | Target repository path, base reference (main/tag/SHA), head reference (branch/PR/current), existing docs location |
| **Outputs** | Delta analysis report: changed files, impact assessment, documentation mapping, risk matrix, action recommendations |

## When to Use

- A PR is opened and you need to understand the full impact of changes
- After merging to main, to identify what documentation needs updating
- Before a release, to generate changelog and identify breaking changes
- When assessing risk of a set of changes across the codebase

## Before You Start

- [ ] Repository is accessible in Cursor
- [ ] You know the baseline to compare against (main, release tag, or commit SHA)
- [ ] You know the head to compare (feature branch, PR, or current state)
- [ ] Existing documentation location is known (e.g., `@TargetRepo/docs/`)

## Steps

### Step 1: Run delta analysis

- Do: Identify all changed files and categorize them
- How: Use Cursor Chat:
  ```
  Analyze @TargetRepo for changes:

  ## Input Context
  - Compare: [BASE] -> [HEAD]
    - Base: [main | release/v1.2 | commit SHA]
    - Head: [feature/xyz | PR #123 | current]
  - Existing docs location: @TargetRepo/docs/

  ## Phase 1: Identify Changed Files

  Categorize all changed files:

  | Category | Files Changed | Type |
  |----------|---------------|------|
  | Services/Business Logic | | Added/Modified/Deleted |
  | API/Contracts | | |
  | Database/Migrations | | |
  | Tests | | |
  | Configuration | | |
  | Documentation | | |
  | Infrastructure/CI | | |
  | Frontend/UI | | |

  ## Phase 2: Analyze Change Impact

  For each significant change:

  ### Change: [Filename or Component]
  - **What changed:** [Brief description]
  - **Why it matters:** [Business/technical impact]
  - **Dependencies affected:** [Other components that rely on this]
  - **Risk level:** [High | Medium | Low]
  ```

#### Focused Delta Analysis (Specific Area)

  ```
  Analyze changes to @TargetRepo/src/services/ only:

  Focus: [AREA - e.g., "payment processing", "authentication"]

  Generate:
  1. What changed in this area
  2. Impact on related components
  3. Test coverage for changes
  4. Documentation updates needed
  ```

#### PR Review Delta Analysis

  ```
  Analyze PR #[NUMBER] or branch [BRANCH_NAME] in @TargetRepo:

  Generate PR review with:
  1. Summary of changes
  2. Risk assessment
  3. Missing tests identification
  4. Documentation impact
  5. Suggested improvements
  ```

#### On Release Preparation

  ```
  Analyze all changes in @TargetRepo since [last-release-tag].
  Generate:
  1. Changelog entries
  2. Breaking changes list
  3. Migration guide items
  4. Documentation updates
  ```
- Expect: Categorized file changes with impact assessment per change

### Step 2: Map changes to documentation

- Do: Identify which documentation sections are affected by the changes
- How: Continue the analysis:
  ```
  Phase 3: Map changes to documentation sections:

  | Changed Area | Affected Doc Section | Update Needed |
  |--------------|---------------------|---------------|

  Phase 4: Generate prioritized update recommendations:
  - Priority 1: Must Update (breaking/critical)
  - Priority 2: Should Update (significant)
  - Priority 3: Nice to Have (minor)
  ```
- Expect: Documentation update checklist sorted by priority

### Step 3: Assess risk

- Do: Generate a risk matrix for the changes
- How: Request risk assessment:
  ```
  Phase 5: Risk Assessment:

  | Risk | Likelihood | Impact | Mitigation |
  |------|------------|--------|------------|

  Phase 6: Recommended actions:
  1. Immediate (before merge)
  2. Post-merge
  3. Future (tech debt/follow-up)
  ```
- Expect: Risk matrix with mitigations and phased action recommendations

### Step 4: Review and distribute findings

- Do: Share the delta analysis with relevant stakeholders
- How: Save the report and distribute to:
  - Tech lead: For architecture impact review
  - QA: For test coverage of changes
  - Documentation: For doc update assignments
- Expect: All stakeholders aware of change impact and assigned actions

## Expected Output

```markdown
# Delta Analysis: [Feature/PR Name]
Generated: [Date]
Compare: [base] -> [head]

## Executive Summary
## Changes Overview (by category)
## Detailed Analysis (high-risk changes)
## Documentation Updates Required
## Risk Matrix
## Recommendations (before merge, after merge, future)
```

**Save to:** `@TargetRepo/docs/updates/delta-[date].md`

## What's Next

- [ ] [Update Documentation](../recurring/update-documentation.md) for affected sections
- [ ] [Generate Unit Tests](generate-unit-tests.md) for uncovered changes
- [ ] [Generate Architecture Diagrams](generate-architecture-diagrams.md) if architecture changed
- [ ] [Identify Test Gaps](identify-test-gaps.md) for changed components

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Incremental Doc Update Workflow | `workflows/incremental-doc-update.md` | Update documentation based on delta analysis |
