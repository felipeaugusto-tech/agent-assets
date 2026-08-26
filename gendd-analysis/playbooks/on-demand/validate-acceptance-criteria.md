# Validate Acceptance Criteria with Playwright

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | QA Engineer, QA Automation, Frontend Dev |
| **Prerequisites** | Playwright MCP configured in Cursor, application running at accessible URL, acceptance criteria written in Gherkin |
| **Inputs** | Gherkin acceptance criteria, application URL, test credentials (if needed), feature area name |
| **Outputs** | AC Validation Report with testability status, element selectors, missing data-testid list, refined ACs |

## When to Use

- After enhancing acceptance criteria to verify they are testable against the real application
- Before sprint planning to validate story feasibility
- When QA questions the testability of requirements
- When developers report acceptance-criteria-to-UI mismatches

## Before You Start

- [ ] Playwright MCP is configured in Cursor (see INTEGRATION-GUIDE.md)
- [ ] Application is running at an accessible URL (staging or local)
- [ ] Acceptance criteria are written in Gherkin format (GIVEN-WHEN-THEN)
- [ ] Test credentials are available if the feature requires authentication

## Steps

### Step 1: Prepare acceptance criteria and application details

- Do: Collect the Gherkin ACs and application information
- How: Gather the acceptance criteria, application URL, test credentials, and feature area name
- Expect: All inputs ready for the validation prompt

### Step 2: Run AC validation with Playwright MCP

- Do: Validate each acceptance criterion against the live application
- How: Use Cursor Chat with Playwright MCP:
  ```
  Read @GenDD-Flow/workflows/enhance-acceptance-criteria.md
  Read @GenDD-Flow/templates/testing-standards.md
  Read @TargetRepo/.cursor/testing.md
  Read @TargetRepo/.cursor/context.md

  I have acceptance criteria that need validation against the live application.

  ## Acceptance Criteria to Validate:
  [PASTE GHERKIN ACS HERE]

  ## Application Details:
  - URL: [APP_URL]
  - Test Credentials: [USER] / [PASS] (if needed)
  - Feature Area: [FEATURE_NAME]

  ## Using Playwright MCP:

  ### Step 1: Navigate to Relevant Pages
  Navigate to the pages referenced in the ACs and screenshot each.

  ### Step 2: Element Verification
  For each action in the WHEN clauses, verify:
  - Does the referenced element exist?
  - What is its actual selector (prefer data-testid)?
  - Is it visible/enabled in the expected state?

  ### Step 3: Outcome Verification  
  For each THEN clause, verify:
  - Can this outcome be asserted programmatically?
  - What selector shows success/failure?
  - Are error messages accessible?

  ### Step 4: Generate Validation Report
  Output AC Validation Report with status per AC (Fully Testable / Partially Testable / Not Testable)
  ```

#### Bulk AC Validation

  For validating multiple ACs at once:
  ```
  Using Playwright MCP, validate these acceptance criteria against [APP_URL]:

  [PASTE_ALL_ACS]

  For each AC, provide:
  1. Testability Status
  2. Missing selectors list
  3. Suggested data-testid additions
  4. Test data requirements

  Output as a summary table:

  | AC | Status | Missing Selectors | Action Required |
  |----|--------|-------------------|-----------------|
  ```

#### Before Sprint Planning

  ```
  Validate all ACs for Sprint [N] stories against [STAGING_URL].
  Generate a report of:
  1. Ready-to-develop stories (all ACs testable)
  2. Blocked stories (missing selectors or test data)
  3. Action items for unblocking
  ```
- Expect: Validation report with status per AC (Fully Testable / Partially Testable / Not Testable)

### Step 3: Review element verification results

- Do: Check each element referenced in the ACs
- How: Review the report for:
  - Elements that exist with proper `data-testid` attributes
  - Elements missing `data-testid` (needs developer action)
  - Elements that do not exist yet (pending development)
- Expect: A list of missing selectors and required `data-testid` additions

### Step 4: Update acceptance criteria based on findings

- Do: Refine ACs to be more specific and testable
- How: Use the validation findings to:
  - Reference actual element names and selectors
  - Add specific assertion values
  - Include discovered edge cases
- Expect: Refined Gherkin ACs that are specific, testable, and complete

### Step 5: Create action items for unblocking

- Do: Document what needs to change before ACs are fully automatable
- How: List missing `data-testid` attributes, test data requirements, and API mocks needed
- Expect: Actionable backlog items for developers to unblock test automation

## Expected Output

```markdown
# AC Validation Report

## AC-1: [Scenario Name]
**Status**: Fully Testable / Partially Testable / Not Testable

**GIVEN**: [precondition]
- Verification: [how to set up state]

**WHEN**: [action]
- Element exists: yes/no
- Selector: [data-testid="..."]

**THEN**: [expected outcome]
- Assertable: yes/no
- Assertion selector: [data-testid="..."]

**Issues Found**: [list]
**Recommendations**: [list]
```

**Save to:** `@TargetRepo/docs/requirements/` or attach to Jira ticket

## What's Next

- [ ] [Generate Tests from Gherkin](../../workflows/generate-tests-from-gherkin.md) to generate a complete multi-layer test suite from validated ACs
- [ ] [Run Assisted Testing](run-assisted-testing.md) to generate full E2E test suites from validated ACs
- [ ] [Generate Integration Tests](generate-integration-tests.md) for backend integration validation
- [ ] Create backlog items for missing `data-testid` attributes
- [ ] [Enhance Requirements](enhance-requirements.md) if ACs need rework

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Enhance AC Workflow | `workflows/enhance-acceptance-criteria.md` | Generate ACs before validation |
| Generate Tests from Gherkin | `workflows/generate-tests-from-gherkin.md` | Generate test suites from validated ACs |
| Testing Standards | `templates/testing-standards.md` | Selector naming rules |
| Context Pack Template | `templates/context-pack.md` (testing.md section) | Universal naming, AAA, scenarios |
