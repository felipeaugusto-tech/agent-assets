# Workflow: Generate Tests from Gherkin Feature

## Context
Transform a Gherkin-format feature specification into a comprehensive, multi-layer testing suite by analyzing the target repository's codebase and mapping each scenario to the components it exercises. This closes the gap between validated acceptance criteria and executable test code — the bridge from "what to test" to "tests that run."

> **Why this matters:** Teams invest heavily in writing Gherkin ACs (via `workflows/enhance-acceptance-criteria.md`) and validating testability (via `playbooks/on-demand/validate-acceptance-criteria.md`), but converting those ACs into actual unit, integration, and E2E tests remains manual. This workflow automates that conversion, ensuring every scenario has corresponding test coverage across all layers.

## Alignment with AI-in-SDLC Initiative
This workflow extends the testing pillar of {ORGANIZATION}'s AI-in-SDLC initiative:
1. Story Quality (shift-left) → `workflows/enhance-acceptance-criteria.md`
2. Test Gap Identification → `workflows/identify-test-gaps.md`
3. **Gherkin → Test Suite Generation** ← This workflow
4. Context Packs → `workflows/create-context-pack.md`

## Prerequisites
- Gherkin feature file or Gherkin-format acceptance criteria (Given-When-Then)
- Target repository cloned and accessible in Cursor
- Context Pack available (`@TargetRepo/.cursor/` with `testing.md`, `conventions.md`, `architecture.md`, `context.md`)
- Test framework installed in the target repository
- Understanding of which product/service the feature affects

## Related Templates
- **`templates/testing-standards.md`** — MUST/SHOULD/MAY requirement levels, naming, coverage targets
- **`templates/context-pack.md`** (File 4: testing.md) — Foundational naming, AAA, scenarios, mocking, coverage guidance

> **Key principles (from context-pack template):**
> - Test names must communicate intent (e.g., `Method_Scenario_ExpectedResult`)
> - Tests follow AAA pattern (Arrange, Act, Assert)
> - Required scenarios: happy path, invalid input, not found
> - Mock at boundaries (interfaces, external services), not internal classes
> - Domain-specific scenarios (payment, notification, auth) apply only when the code handles that domain
> - Multi-tenant isolation tests are required when code operates in a multi-tenant context

## When to Use This Workflow
- Gherkin acceptance criteria have been written and validated (manually or via `workflows/enhance-acceptance-criteria.md`)
- A new feature is ready for development and needs corresponding tests
- QA needs to pre-build the test harness before development begins (shift-left testing)
- After a sprint planning session when multiple stories have Gherkin ACs
- When converting manual test cases written in Gherkin into automated tests
- **After AC Validation** — Use validated ACs from `playbooks/on-demand/validate-acceptance-criteria.md` for best results

## Tooling Approach
**Cursor + repo-based Markdown context only.** No RAG, vector databases, embeddings, or additional platforms.

---

## Cursor Steps

### Phase 1: Parse and Understand the Gherkin Feature

#### 1. Provide the Gherkin Feature

Open Cursor Chat (Cmd+L / Ctrl+L) and paste the feature:

```
Read @GenDD-Flow/workflows/generate-tests-from-gherkin.md
Read @GenDD-Flow/templates/testing-standards.md
Read @TargetRepo/.cursor/testing.md
Read @TargetRepo/.cursor/conventions.md
Read @TargetRepo/.cursor/context.md
Read @TargetRepo/.cursor/architecture.md

I have a Gherkin feature that needs a comprehensive test suite generated.

## Gherkin Feature:
"""
{PASTE YOUR GHERKIN FEATURE HERE}
"""

## Context:
- Product: {PRODUCT_NAME}
- Tech Stack: {.NET | Go | React | Next.js | Python}
- Test Frameworks: {xUnit | NUnit | Jest | pytest | Playwright}
- Multi-tenant: {YES/NO}
- Branch: {BRANCH_NAME} (if working on a feature branch)

Parse this Gherkin feature and produce:

1. **Feature Summary**: One-sentence description of what this feature does
2. **Scenario Inventory**: Table of all scenarios with:
   | Scenario | Type (Happy/Edge/Error/Security) | Business Criticality (High/Med/Low) |
3. **Step Decomposition**: For each unique GIVEN/WHEN/THEN step, identify:
   - The action or state it represents
   - The system component it likely touches (UI, API, Service, Database)
   - Whether it requires test data setup, mocking, or external integration
4. **Implicit Requirements**: Requirements not stated but implied by the scenarios (e.g., authentication, authorization, multi-tenant isolation, validation)
5. **Test Data Requirements**: What test data is needed to execute all scenarios
```

#### 2. Review the Parsed Feature

Verify:
- [ ] All scenarios are captured
- [ ] Scenario types are correctly classified
- [ ] Business criticality makes sense
- [ ] Implicit requirements are reasonable
- [ ] No scenarios are missing (compare with original AC)

---

### Phase 2: Analyze Target Repository Components

#### 3. Map Feature to Codebase Components

```
Based on the Gherkin feature I provided, analyze the target repository to identify which components this feature touches.

Search @TargetRepo for:

1. **Entry Points**: Controllers, API endpoints, handlers, or pages that would receive the user actions described in WHEN steps
2. **Service Layer**: Services, use cases, or business logic classes that implement the behavior described in THEN steps
3. **Data Layer**: Repositories, stores, database access code, or models involved in GIVEN preconditions and THEN outcomes
4. **Integration Points**: External API clients, message queues, email services, or third-party integrations referenced or implied
5. **Shared/Cross-Cutting**: Middleware, validators, authorization checks, tenant resolution that apply to this feature
6. **UI Components** (if frontend): Pages, components, forms, or views involved in the user interactions

For each identified component, provide:
| Component | File Path | Layer | Gherkin Steps Mapped | Existing Tests? |
|-----------|-----------|-------|---------------------|-----------------|

If the feature requires NEW components that don't yet exist, list them separately as "To Be Created" with suggested file paths following the repository's conventions.
```

#### 4. Identify Existing Test Patterns

```
Analyze the existing test files in @TargetRepo to understand:

1. **Test Structure**: How are tests organized? (by feature, by layer, by class?)
2. **Naming Convention**: What naming pattern do tests follow?
3. **Mocking Approach**: What mocking library and patterns are used?
4. **Test Data Setup**: How is test data created? (builders, factories, fixtures, inline?)
5. **Assertion Patterns**: What assertion libraries and patterns are used?
6. **Test Configuration**: How are tests configured? (DI, test servers, database setup?)

Provide 2-3 example test files that are most similar to what we'll need to generate for this feature. These will serve as style references.
```

---

### Phase 3: Map Gherkin Scenarios to Test Layers

#### 5. Create the Scenario-to-Test Mapping

```
Based on:
- The parsed Gherkin feature (Phase 1)
- The identified codebase components (Phase 2)
- The existing test patterns (Phase 2)

Create a SCENARIO-TO-TEST MAPPING that shows exactly which tests need to be generated at each layer.

For EACH Gherkin scenario, determine:

## Scenario: {SCENARIO_NAME}

### Unit Tests Needed:
| Test Name | Class Under Test | What It Verifies | Mocks Required |
|-----------|-----------------|------------------|----------------|

### Integration Tests Needed:
| Test Name | Components Involved | What It Verifies | Setup Required |
|-----------|-------------------|------------------|----------------|

### E2E Tests Needed:
| Test Name | User Journey | What It Verifies | Test Data Required |
|-----------|-------------|------------------|-------------------|

### Mapping Rationale:
- Why this scenario needs unit/integration/E2E coverage (or why a layer can be skipped)
- Which GIVEN steps map to test setup (Arrange)
- Which WHEN steps map to test execution (Act)
- Which THEN steps map to assertions (Assert)

Include a summary count:
| Test Layer | Count | Coverage |
|------------|-------|----------|
| Unit       | X     | Which scenarios covered |
| Integration| X     | Which scenarios covered |
| E2E        | X     | Which scenarios covered |
| **Total**  | X     | |
```

**HITL Checkpoint**: Review this mapping before proceeding. Ask:
- Are there scenarios that need more test coverage?
- Are any tests unnecessary or redundant?
- Does the mapping align with your team's testing strategy?

---

### Phase 4: Generate Unit Tests

#### 6. Generate Unit Tests from Gherkin Scenarios

```
Read @GenDD-Flow/templates/testing-standards.md
Read @TargetRepo/.cursor/testing.md

Based on the scenario-to-test mapping, generate unit tests for each identified class.

Requirements:
- Framework: {xUnit | NUnit | Jest | pytest}
- Mocking: {Moq | jest.mock | unittest.mock | gomock}
- Follow Arrange-Act-Assert pattern
- Use naming convention: {Method}_{Scenario}_{ExpectedResult}
- Map directly to Gherkin scenarios (add a comment referencing the scenario)

For EACH unit test:
1. **Comment**: Reference the Gherkin scenario it validates
   // Validates: Scenario "AC1: Opt-in to Save Payment Method"
   // WHEN: User checks "Save payment method" checkbox and completes payment
   // THEN: Payment method is securely tokenized and stored

2. **Arrange**: Set up mocks and test data matching GIVEN preconditions
3. **Act**: Execute the method matching WHEN steps
4. **Assert**: Verify outcomes matching THEN expectations

Include:
- Happy path tests (from happy path scenarios)
- Error condition tests (from error scenarios)
- Edge case tests (from edge case scenarios)
- Validation tests (from implicit requirements)
- Multi-tenant isolation tests (if multi-tenant: YES)

Generate complete, compilable test files following the style of existing tests in the repository.
```

#### 7. Review Unit Tests

Check:
- [ ] Every Gherkin scenario has at least one unit test
- [ ] Tests follow existing naming conventions
- [ ] Mocks are set up correctly
- [ ] Arrange-Act-Assert pattern used consistently
- [ ] Multi-tenant isolation tested (if applicable)
- [ ] Error scenarios included

---

### Phase 5: Generate Integration Tests

#### 8. Generate Integration Tests from Gherkin Scenarios

```
Read @GenDD-Flow/workflows/automate-integration-testing.md
Read @GenDD-Flow/templates/testing-standards.md
Read @TargetRepo/.cursor/testing.md

Based on the scenario-to-test mapping, generate integration tests for component interactions and external integrations.

Requirements:
- Framework: {xUnit | NUnit | Jest | pytest | Playwright}
- Reference the Gherkin scenario in each test comment
- Follow the integration testing lifecycle (setup → execute → verify → cleanup)
- Isolate test tenants (if multi-tenant)

For EACH integration test:

1. **Comment**: Reference the Gherkin scenario and the integration being tested
2. **Setup**: Create test data, configure test tenant, prepare sandbox credentials
3. **Execute**: Call the integration point as the scenario describes
4. **Verify**: Assert the end-to-end outcome matches THEN expectations
5. **Cleanup**: Remove test data, void test transactions

Categories:
- **Service-to-Service**: Tests where multiple internal services interact
- **Database Integration**: Tests that verify data persistence from scenarios
- **External API Integration**: Tests that hit sandbox APIs (payment, email, etc.)
- **Contract Tests**: Verify API request/response schemas haven't changed

Generate complete test files following existing integration test patterns in the repository.
```

---

### Phase 6: Generate E2E Tests from Gherkin Scenarios

#### 9. Generate Playwright E2E Tests

```
Read @GenDD-Flow/playbooks/on-demand/run-assisted-testing.md
Read @GenDD-Flow/templates/testing-standards.md
Read @TargetRepo/.cursor/testing.md

Based on the Gherkin scenarios, generate Playwright E2E tests that directly translate the Given-When-Then steps into executable test code.

Requirements:
- MUST use [data-testid] selectors exclusively
- MUST use explicit waits (waitForSelector, expect), NEVER waitForTimeout
- Each test MUST be independent (beforeEach setup)
- Map GIVEN → test setup, WHEN → user actions, THEN → assertions

For EACH Gherkin scenario, generate a Playwright test:

```typescript
// Feature: {FEATURE_NAME}
// Scenario: {SCENARIO_NAME}
// Source: Gherkin AC

test('{Scenario name in plain English}', async ({ page }) => {
  // GIVEN {precondition from Gherkin}
  // ... setup code ...

  // WHEN {action from Gherkin}
  // ... user interaction code ...

  // THEN {expected outcome from Gherkin}
  // ... assertion code ...
});
```

Generate:
1. **Page Objects** for any new pages/components (following `e2e/pages/*.page.ts` pattern)
2. **Happy Path Tests** → `e2e/tests/{feature}-happy-path.spec.ts`
3. **Validation Tests** → `e2e/tests/{feature}-validation.spec.ts`
4. **Error Handling Tests** → `e2e/tests/{feature}-error-handling.spec.ts`
5. **Accessibility Tests** → `e2e/tests/{feature}-accessibility.spec.ts`
6. **Test Data Fixtures** → `e2e/fixtures/{feature}-test-data.json`

Each test file should include a header comment listing which Gherkin scenarios it covers.
```

#### 10. Review E2E Tests

Check:
- [ ] Every Gherkin scenario has a corresponding E2E test
- [ ] Only `data-testid` selectors used
- [ ] No `waitForTimeout` or arbitrary delays
- [ ] Tests are independent (no shared state)
- [ ] Page Objects created for new UI components
- [ ] Test data fixtures are complete

---

### Phase 7: Generate Test Inventory

#### 11. Create the Test Inventory Report

```
Based on all the tests generated in Phases 4-6, create a comprehensive TEST INVENTORY that maps every Gherkin scenario to its test coverage.

## Test Inventory: {FEATURE_NAME}

### Coverage Summary

| Metric | Value |
|--------|-------|
| Gherkin Scenarios | {N} |
| Total Tests Generated | {N} |
| Unit Tests | {N} |
| Integration Tests | {N} |
| E2E Tests | {N} |
| Scenarios with Full Coverage (Unit + Integration + E2E) | {N}/{N} |
| Scenarios with Partial Coverage | {N}/{N} |

### Scenario-to-Test Traceability Matrix

| Gherkin Scenario | Unit Tests | Integration Tests | E2E Tests | Coverage Status |
|-----------------|------------|-------------------|-----------|-----------------|
| {Scenario 1}   | {test names} | {test names} | {test names} | Full / Partial / None |
| {Scenario 2}   | ... | ... | ... | ... |

### Test Files Generated

| File Path | Test Type | Tests Count | Scenarios Covered |
|-----------|-----------|-------------|-------------------|
| tests/Unit/{Feature}Tests.{ext} | Unit | {N} | AC1, AC2, AC3 |
| tests/Integration/{Feature}IntegrationTests.{ext} | Integration | {N} | AC1, AC3 |
| e2e/tests/{feature}-happy-path.spec.ts | E2E | {N} | AC1, AC2 |
| e2e/tests/{feature}-validation.spec.ts | E2E | {N} | AC4, AC5 |
| e2e/tests/{feature}-error-handling.spec.ts | E2E | {N} | AC3 |
| e2e/tests/{feature}-accessibility.spec.ts | E2E | {N} | AC1 (a11y) |

### Test Data Files

| File Path | Purpose | Scenarios Using It |
|-----------|---------|-------------------|
| e2e/fixtures/{feature}-test-data.json | E2E test data | All E2E tests |
| tests/Fixtures/{feature}-data.json | Unit/Integration data | All unit/integration tests |

### Gaps and Recommendations

| Gap | Risk Level | Recommendation |
|-----|------------|----------------|
| {Any scenario without full coverage} | {High/Med/Low} | {What to add} |
| {Missing test data for edge case} | {High/Med/Low} | {What to create} |

### CI/CD Integration Notes

| Test Suite | When to Run | Blocking? |
|------------|-------------|-----------|
| Unit Tests | Every PR | Yes |
| Integration Tests | Before merge to main | Yes |
| E2E Tests | Nightly / Pre-release | No (alerts) |
```

---

### Phase 8: Validate with User (HITL Checkpoint)

#### 12. Present Test Suite for Review

Present the complete test suite to the user for validation:

```
I've generated a complete test suite from your Gherkin feature. Here's a summary for your review:

## Generated Test Suite Summary

**Feature**: {FEATURE_NAME}
**Total Tests**: {N} across {N} files
**Coverage**: {N}/{N} Gherkin scenarios have full coverage

### Files Created:
{List all generated test files}

### What I'd Like You to Verify:

1. **Completeness**: Are all Gherkin scenarios covered?
2. **Accuracy**: Do the test assertions match your expected behavior?
3. **Priorities**: Should any tests be marked as MUST vs. SHOULD vs. MAY?
4. **Test Data**: Is the test data realistic for your domain?
5. **Missing Scenarios**: Are there implicit scenarios I should add?
   - Multi-tenant isolation?
   - Performance/load considerations?
   - Security edge cases?
   - Accessibility requirements?

### Next Steps After Your Review:
- [ ] Run the unit tests locally to verify they compile/pass
- [ ] Review integration test setup (sandbox credentials, test DB)
- [ ] Validate E2E selectors against the actual application
- [ ] Add tests to CI/CD pipeline
```

#### 13. Iterate Based on Feedback

```
Based on your review feedback, I'll update the test suite:

Feedback received:
{LIST_FEEDBACK_ITEMS}

For each item:
1. Identify which test files need changes
2. Apply the changes
3. Update the test inventory
4. Verify traceability matrix is still complete
```

---

## Output Artifacts

After completing this workflow, you will have:

1. **Test Suite — Unit Tests** (`@TargetRepo/tests/Unit/{Feature}Tests.{ext}`)
   - Unit tests for all service/business logic components

2. **Test Suite — Integration Tests** (`@TargetRepo/tests/Integration/{Feature}IntegrationTests.{ext}`)
   - Integration tests for component interactions and external APIs

3. **Test Suite — E2E Tests** (`@TargetRepo/e2e/tests/{feature}-*.spec.ts`)
   - Playwright E2E tests mapping directly to Gherkin scenarios

4. **Page Objects** (`@TargetRepo/e2e/pages/{feature}.page.ts`)
   - Page Object classes for new UI components

5. **Test Data Fixtures** (`@TargetRepo/e2e/fixtures/{feature}-test-data.json`)
   - Structured test data for all scenarios

6. **Test Inventory Report** (`@TargetRepo/docs/test-inventory-{feature}.md`)
   - Complete traceability matrix from Gherkin scenarios to tests

---

## Example: Save Payment Method Feature

### Gherkin Input

```gherkin
Feature: Save Payment Method
  As a school administrator
  I want to save my payment method securely
  So that I can make future payments faster

  Scenario: AC1 - Opt-in to save payment method
    Given I am logged in as a school administrator
    And I am on the payment checkout page
    When I check the "Save payment method for future use" checkbox
    And I complete the payment successfully
    Then my payment method is securely tokenized and stored
    And I see a confirmation message "Payment method saved"
    And the saved method appears in my account settings

  Scenario: AC2 - View saved payment methods
    Given I have previously saved payment methods
    When I navigate to "My Account" > "Payment Methods"
    Then I see a list of my saved payment methods
    And each method shows last 4 digits, card type, expiration date
    And I see options to use for payment, delete, set as default

  Scenario: AC3 - Vault service unavailable
    Given the vault service is unavailable
    When I complete a payment with "Save payment method" checked
    Then the payment succeeds
    And I see a warning "Unable to save payment method, please try again later"

  Scenario: AC4 - Multi-tenant isolation
    Given User A from School 1 has saved a card ending in 1111
    And User B from School 2 has saved a card ending in 2222
    When User A views their saved payment methods
    Then User A sees only the card ending in 1111
    And User A does not see the card ending in 2222
```

### Generated Output Structure

```
@TargetRepo/
├── tests/
│   ├── Unit/
│   │   ├── PaymentMethodServiceTests.cs        # 12 unit tests (AC1-AC4)
│   │   └── VaultClientTests.cs                 # 6 unit tests (AC1, AC3)
│   ├── Integration/
│   │   ├── SavePaymentIntegrationTests.cs      # 4 integration tests (AC1, AC3)
│   │   └── TenantIsolationTests.cs             # 3 integration tests (AC4)
│   └── Fixtures/
│       └── payment-method-test-data.json
├── e2e/
│   ├── pages/
│   │   ├── checkout.page.ts                    # Page Object for checkout
│   │   └── payment-methods.page.ts             # Page Object for account settings
│   ├── tests/
│   │   ├── save-payment-happy-path.spec.ts     # 3 E2E tests (AC1, AC2)
│   │   ├── save-payment-error-handling.spec.ts # 2 E2E tests (AC3)
│   │   └── save-payment-accessibility.spec.ts  # 2 E2E tests (AC1 a11y)
│   └── fixtures/
│       └── save-payment-test-data.json
└── docs/
    └── test-inventory-save-payment-method.md   # Traceability matrix
```

### Generated Test Inventory (excerpt)

| Gherkin Scenario | Unit Tests | Integration Tests | E2E Tests | Status |
|-----------------|------------|-------------------|-----------|--------|
| AC1: Opt-in to save | `SaveMethod_ValidToken_Stores`, `SaveMethod_PaymentFails_DoesNotStore`, `Tokenize_ValidCard_ReturnsToken` | `SavePayment_EndToEnd_TokenizedAndStored` | `save-payment-happy-path#opt-in` | Full |
| AC2: View saved | `GetMethods_HasSaved_ReturnsList`, `GetMethods_NoSaved_ReturnsEmpty` | — | `save-payment-happy-path#view-saved` | Partial (no integration) |
| AC3: Vault down | `SaveMethod_VaultDown_PaymentSucceeds`, `SaveMethod_VaultDown_ReturnsWarning` | `SavePayment_VaultUnavailable_GracefulDegradation` | `save-payment-error-handling#vault-down` | Full |
| AC4: Multi-tenant | `GetMethods_WrongTenant_ReturnsEmpty`, `SaveMethod_IsolatesTenants` | `TenantIsolation_CrossAccess_Blocked` | — | Partial (no E2E) |

---

## Success Metrics
- **Traceability**: 100% of Gherkin scenarios mapped to at least one test
- **Coverage**: 80%+ of scenarios have tests at all applicable layers
- **Time Saved**: 60-70% reduction in test authoring time vs. manual conversion
- **Consistency**: All tests follow repository conventions and naming patterns
- **Rework Reduction**: Fewer test rewrites due to clear Gherkin-to-test mapping

---

## Tips for Best Results

### Start with Validated ACs
Run `playbooks/on-demand/validate-acceptance-criteria.md` first to ensure Gherkin scenarios reference real UI elements and are testable. This prevents generating E2E tests that can't find selectors.

### Provide Rich Repository Context
Ensure the Context Pack (`@TargetRepo/.cursor/`) exists and is current. The more the AI knows about testing patterns, conventions, and architecture, the better the generated tests will be.

### Review Before Running
Generated tests are a starting point. Review and adjust:
- Mock configurations for your specific DI setup
- Database setup/teardown for your specific ORM
- Selector names for your specific UI component library
- Test data values for your specific business domain

### Iterate Layer by Layer
If the context window gets large, run each phase in a separate Cursor Chat session:
1. Session 1: Phases 1-3 (parse, analyze, map) — save output to `docs/`
2. Session 2: Phase 4 (unit tests) — reference saved mapping
3. Session 3: Phase 5 (integration tests) — reference saved mapping
4. Session 4: Phases 6-7 (E2E tests + inventory) — reference saved mapping

### Use Existing Tests as Templates
Point the AI at the best existing test file in your repo as a style reference. This ensures generated tests match your team's patterns exactly.

---

## Common Pitfalls to Avoid

- ❌ **Skipping the mapping phase**: Jumping straight to code generation produces scattered, unmapped tests
- ❌ **Generating all layers for every scenario**: Some scenarios only need unit tests (e.g., validation rules); not every scenario needs E2E
- ❌ **Ignoring existing test patterns**: Generated tests that don't match repo style will be rewritten
- ❌ **Not validating selectors**: E2E tests will fail if selectors don't match the actual UI
- ❌ **Over-mocking in integration tests**: Integration tests should test real interactions, not mocked ones
- ❌ **Skipping the HITL checkpoint**: Always validate the mapping before generating code
- ❌ **Forgetting multi-tenant**: If multi-tenant: YES, every data operation test needs tenant isolation
- ❌ **No cleanup in integration tests**: Tests that leave data behind will cause flaky subsequent runs

---

## Integration with Other Workflows

### Inputs From Other Workflows

**From Enhance Acceptance Criteria** (`workflows/enhance-acceptance-criteria.md`):
- **Gherkin ACs** → Direct input to this workflow
- **Edge cases** → Ensure edge case scenarios are included
- **Integration impacts** → Guide which integration tests to generate

**From Validate Acceptance Criteria** (`playbooks/on-demand/validate-acceptance-criteria.md`):
- **Testability status** → Know which ACs are automatable
- **Selector inventory** → Use real selectors in E2E tests
- **Missing data-testid list** → Know what to stub or skip

**From Brownfield Repository Analysis** (`workflows/brownfield-repository-analysis.md`):
- **Core flows** → Understand existing behavior being modified
- **Risk hotspots** → Prioritize test coverage for high-risk components
- **Integration points** → Focus integration test effort

**From Identify Test Gaps** (`workflows/identify-test-gaps.md`):
- **Existing test inventory** → Avoid duplicating tests that already exist
- **Coverage gaps** → Prioritize test generation for uncovered areas

### Outputs To Other Workflows

1. **Identify Test Gaps** (`workflows/identify-test-gaps.md`)
   - Use the test inventory to update coverage maps

2. **Automate Integration Testing** (`workflows/automate-integration-testing.md`)
   - Use generated integration tests as starting point for CI/CD configuration

3. **Run Assisted Testing** (`playbooks/on-demand/run-assisted-testing.md`)
   - Use generated Page Objects and E2E tests as a base for Playwright MCP validation

4. **Review Test Coverage** (`playbooks/recurring/review-test-coverage.md`)
   - Use the traceability matrix to track coverage over time

```
# Recommended end-to-end flow:

# Step 1: Create Gherkin ACs from requirements
Read @GenDD-Flow/workflows/enhance-acceptance-criteria.md

# Step 2: Validate ACs are testable against live app
Read @GenDD-Flow/playbooks/on-demand/validate-acceptance-criteria.md

# Step 3: Generate complete test suite from validated ACs
Read @GenDD-Flow/workflows/generate-tests-from-gherkin.md

# Step 4: Run and validate generated tests
Read @GenDD-Flow/playbooks/on-demand/run-assisted-testing.md
```
