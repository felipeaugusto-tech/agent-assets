# Review Test Coverage

| Field | Value |
|-------|-------|
| **Category** | recurring |
| **Target Roles** | QA Engineer, QA Automation, Tech Lead, Engineering Manager |
| **Prerequisites** | Repository access, previous test gap analysis (optional), knowledge of critical flows |
| **Inputs** | Path to target repository, product name, critical integrations, known problem areas |
| **Outputs** | Updated test inventory, coverage gap matrix, risk heat map, sprint-level remediation plan |

## When to Use

- At sprint boundaries to assess test health and plan test work
- Before major releases to validate coverage completeness
- After production incidents to verify gaps are being closed
- Quarterly review to track test coverage trends
- When onboarding new QA resources to understand current state

## Before You Start

- [ ] Repository is accessible in Cursor
- [ ] You know the critical business flows and integrations
- [ ] Previous test gap analysis is available for comparison (if exists)
- [ ] Coverage metrics from CI/CD are accessible (if available)

## Steps

### Step 1: Re-run test gap analysis

- Do: Generate a fresh test inventory and gap analysis
- How: Use the [Identify Test Gaps](../on-demand/identify-test-gaps.md) playbook with your current context (product name, critical integrations, known problem areas)
- Expect: Full test gap analysis output (inventory, gap matrix, coverage map, recommendations, roadmap)

### Step 2: Compare with previous analysis

- Do: Identify what improved and what regressed since last review
- How: Compare current gap matrix with previous version:
  ```
  Read @TargetRepo/docs/testing/test-gap-matrix.md
  Read @TargetRepo/docs/testing/test-recommendations.md

  Compare the current analysis with the previous gap matrix and recommendations.

  Identify:
  - Gaps closed since last review
  - New gaps introduced
  - Coverage trend (improving or declining)
  - Recommendations that have been implemented vs. still pending
  ```
- Expect: A delta showing progress and regressions

### Step 3: Update coverage metrics

- Do: Record current coverage numbers for tracking
- How: Collect coverage data from CI/CD and the analysis:
  - Unit test coverage percentage
  - Integration test coverage
  - E2E test coverage
  - Critical path coverage
- Expect: Updated metrics for reporting

### Step 4: Assess regression and sanity test health

- Do: Verify regression and sanity test suites are current and effective
- How: Evaluate against the Regression & Sanity Scenarios in the testing standards (see `templates/context-pack.md` testing.md section). Key questions: Do sanity tests exist and run post-deploy? Is the full regression suite current? Are stale tests removed after feature changes? Can tests run by feature area independently?
- Expect: Assessment of regression health with specific maintenance actions

### Step 5: Generate sprint remediation plan

- Do: Create actionable test work items for the next sprint
- How: Prioritize remaining gaps by business risk and create sprint tasks
- Expect: A list of test tasks with effort estimates ready for sprint planning

### Step 6: Report to stakeholders

- Do: Share findings with engineering leadership
- How: Prepare a summary with:
  - Coverage trend (improving/declining)
  - Critical gaps remaining
  - Sprint plan for remediation
  - Risk areas that need attention
- Expect: Stakeholder awareness and support for test investment

## Expected Output

```
@TargetRepo/docs/
├── test-inventory.md          # Updated test inventory
├── test-gap-matrix.md         # Updated gap matrix
├── test-coverage-map.md       # Updated visual coverage
├── test-recommendations.md    # Updated prioritized recommendations
└── test-roadmap.md            # Updated sprint plan
```

**Save to:** `@TargetRepo/docs/`

## What's Next

- [ ] [Generate Unit Tests](../on-demand/generate-unit-tests.md) for high-priority gaps identified
- [ ] [Generate Integration Tests](../on-demand/generate-integration-tests.md) for integration gaps
- [ ] Schedule next coverage review (end of sprint or quarterly)

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Test Gap Analysis Playbook | `playbooks/on-demand/identify-test-gaps.md` | Full analysis playbook with focused variant |
| Identify Test Gaps Workflow | `workflows/identify-test-gaps.md` | 6-phase workflow with output artifacts |
| Testing Standards Template | `templates/testing-standards.md` | MUST/SHOULD/MAY test requirement levels |
| Context Pack Template | `templates/context-pack.md` (testing.md section) | Universal naming, AAA, scenarios, coverage |
