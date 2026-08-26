# Identify Test Gaps

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | QA Engineer, QA Automation, Tech Lead |
| **Prerequisites** | Repository access, knowledge of critical business flows and integrations |
| **Inputs** | Path to target repository, product name, critical integrations, known problem areas |
| **Outputs** | Test inventory, coverage gap matrix, risk heat map, prioritized recommendations, implementation roadmap |

## When to Use

- During sprint planning to identify test work needed
- Before major releases to validate coverage completeness
- After production incidents to prevent recurrence
- When leadership asks "are we confident in our testing?"
- After brownfield analysis to prioritize test coverage for risk hotspots

## Before You Start

- [ ] Repository is accessible in Cursor
- [ ] You know the critical business flows (payments, auth, data sync)
- [ ] You know the key external integrations
- [ ] You have access to existing test files (if any)

## Steps

### Step 1: Run the 6-phase test gap analysis

- Do: Map all existing test files and identify gaps using the identify-test-gaps workflow
- How: Use Cursor Chat:
  ```
  Read @GenDD-Flow/workflows/identify-test-gaps.md
  Read @GenDD-Flow/templates/testing-standards.md
  Read @TargetRepo/.cursor/testing.md
  Read @TargetRepo/.cursor/context.md

  Analyze @TargetRepo for test gaps:

  Context:
  - Product: [PRODUCT NAME]
  - Critical Integrations: [LIST - e.g., WorldPay, Vault, SMS systems]
  - Known Problem Areas: [ANY AREAS WITH RECENT BUGS]

  Follow all 6 phases from the identify-test-gaps workflow.
  Output as structured markdown.
  ```

#### Focused Analysis (Specific Area)

  ```
  Read @GenDD-Flow/workflows/identify-test-gaps.md
  Read @GenDD-Flow/templates/testing-standards.md
  Read @TargetRepo/.cursor/testing.md
  Read @TargetRepo/.cursor/context.md

  Analyze @TargetRepo/[specific/path] for test gaps:

  Focus on: [PAYMENT PROCESSING | AUTHENTICATION | DATA SYNC | etc.]

  Generate:
  1. Current test inventory for this area
  2. What tests SHOULD exist
  3. Gap analysis
  4. Top 5 recommended tests to add
  5. Effort estimates
  ```
- Expect: Complete 6-phase analysis covering inventory, gap matrix, coverage map, recommendations, and implementation roadmap

## Expected Output

```
@TargetRepo/docs/
├── test-inventory.md          # Current test files and coverage
├── test-gap-matrix.md         # What should exist vs. what does
├── test-coverage-map.md       # Visual coverage by layer
├── test-recommendations.md    # Prioritized tests to add
└── test-roadmap.md            # Sprint-by-sprint implementation plan
```

**Save to:** `@TargetRepo/docs/`

## What's Next

- [ ] [Generate Unit Tests](generate-unit-tests.md) for high-priority gaps
- [ ] [Generate Integration Tests](generate-integration-tests.md) for integration gaps
- [ ] [Review Test Coverage](../recurring/review-test-coverage.md) on a regular cadence
- [ ] Share roadmap with engineering manager for sprint planning

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Identify Test Gaps Workflow | `workflows/identify-test-gaps.md` | 6-phase workflow with examples and output artifacts |
| Testing Standards Template | `templates/testing-standards.md` | MUST/SHOULD/MAY test requirement levels |
| Context Pack Template | `templates/context-pack.md` (testing.md section) | Universal naming, AAA, scenarios, coverage |
