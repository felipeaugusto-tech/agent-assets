# Workflow: Identify Test Gaps

## Context
Systematically identify what tests **should exist** versus what **does exist**, producing clear coverage maps and actionable recommendations across unit, integration, and end-to-end testing. This workflow directly addresses leadership priorities around testing rigor and reducing downstream surprises.

## Alignment with AI-in-SDLC Initiative
This workflow is one of four initial high-impact areas focused on early SDLC quality:
1. Story Quality (shift-left)
2. **Test Gap Identification** ← This workflow
3. Context Packs
4. C4 Architecture Diagrams

## Prerequisites
- Access to codebase via Cursor
- Understanding of the system's key user flows
- Access to existing test files (if any)
- Knowledge of critical business logic and integrations

## Related Templates
- **`templates/testing-standards.md`** - MUST/SHOULD/MAY requirement levels, E2E rules, integration lifecycle
- **`templates/context-pack.md`** (File 4: testing.md) - Foundational naming, AAA, scenarios, mocking, coverage guidance

> **Key principles (from context-pack template):**
> - Every feature needs: happy path, invalid input, and not-found tests
> - Conditional scenarios: authorization, authentication, external failure, concurrency, multi-tenant isolation — when applicable
> - Domain-specific scenarios: payment processing, notifications, security/access control, frontend/UI — only when the repo handles that domain
> - Coverage priority: critical business logic > public APIs > data access > infrastructure

## When to Use This Workflow
- Sprint planning (identify test work needed)
- Before major releases (validate coverage)
- When onboarding new QA resources
- After production incidents (prevent recurrence)
- During code reviews (identify untested changes)
- When leadership asks "are we confident in our testing?"
- **After Brownfield Analysis** - Use risk hotspots from `workflows/brownfield-repository-analysis.md` to prioritize test coverage

## Tooling Approach
**Cursor + repo-based Markdown context only.** No RAG, vector databases, embeddings, or additional platforms.

---

## Cursor Steps

### Phase 1: Inventory Current Tests

#### 1. Map Existing Test Files

Open Cursor Chat (Cmd+L / Ctrl+L) in your repository:

```
Read @TargetRepo/.cursor/testing.md
Read @TargetRepo/.cursor/context.md

Analyze this codebase and create a test inventory.

Find all test files and categorize by:
1. **Unit Tests**: Test individual functions/methods in isolation
2. **Integration Tests**: Test multiple components together or external APIs
3. **End-to-End Tests**: Test complete user flows (Playwright, Cypress, Specflow)
4. **Contract Tests**: API schema validation
5. **Performance Tests**: Load and stress tests

For each category, list:
- File paths
- Number of test cases
- What is being tested (class/service/component)
- Last modified date (if visible from imports/comments)

Output as a markdown table.
```

#### 2. Identify Test Framework and Patterns

```
Analyze the test files found and identify:

1. **Test Frameworks in Use**:
   - Unit: (xUnit, NUnit, Jest, pytest, etc.)
   - Integration: (TestContainers, WireMock, etc.)
   - E2E: (Playwright, Cypress, Specflow, Selenium, etc.)

2. **Test Patterns Used**:
   - Naming convention (MethodName_Scenario_ExpectedResult?)
   - Arrange-Act-Assert structure?
   - Mocking approach (Moq, jest.mock, etc.)
   - Test data management (fixtures, factories, builders?)

3. **Test Configuration**:
   - CI/CD integration (GitHub Actions, Azure Pipelines?)
   - Test categories/tags in use
   - Parallel execution enabled?

Document the current testing standards.
```

### Phase 2: Identify What Should Be Tested

#### 3. Map Critical Business Logic

```
Read @TargetRepo/.cursor/context.md
Read @TargetRepo/docs/brownfield/gendd/

Analyze this codebase and identify all critical business logic that MUST have test coverage.

Categories to identify (apply the Required Test Scenarios from `templates/context-pack.md` testing section for domain-specific checklists):
1. **Payment/Financial Logic**: Any code touching money, transactions, fees
2. **Authentication/Authorization**: Login, permissions, access control
3. **Data Transformation**: Import/export, format conversion, calculations
4. **Integration Points**: External API calls, webhooks, third-party services
5. **Email & Notifications**: Transactional emails, receipts, confirmations
6. **State Machines**: Workflow states, status transitions
7. **Validation Rules**: Input validation, business rules
8. **UI & Frontend** (when frontend exists): Sensitive field masking, responsive design, accessibility

For each identified area:
- File/class/method location
- Business criticality (High/Medium/Low)
- Risk if untested (What could go wrong?)
- Current test coverage (Yes/No/Partial based on Phase 1 findings)

Output as markdown grouped by criticality.
```

#### 4. Map User Journeys

```
Based on the codebase, identify the key user journeys that should have end-to-end test coverage.

For each journey:
1. **Journey Name**: (e.g., "Complete Payment", "User Registration")
2. **Steps**: Numbered sequence of user actions
3. **Entry Points**: Where does this flow start in the code?
4. **Exit Points**: What are the success/failure outcomes?
5. **Integrations Touched**: Which external systems are involved?
6. **E2E Test Exists?**: Yes/No based on Phase 1 findings

Prioritize by:
- Revenue impact (affects payments/transactions)
- User frequency (how often is this used)
- Complexity (how many things can go wrong)
```

#### 5. Map Integration Points

```
Identify all external integration points that need integration test coverage.

For each integration:
1. **Integration Name**: (e.g., "WorldPay", "SendGrid", "SSO Provider")
2. **Type**: Payment Gateway / Email / Auth / Data Sync / Other
3. **Methods/Endpoints**: List of API calls made
4. **Error Scenarios**: What failures are possible?
5. **Integration Test Exists?**: Yes/No/Partial based on Phase 1 findings
6. **Sandbox Available?**: Yes/No (for real integration tests)

Categorize by:
- Business-critical (payments, auth)
- Data integrity (sync, import/export)
- User-facing (email, notifications)
```

### Phase 3: Generate Gap Analysis

#### 6. Create Coverage Gap Matrix

```
Based on my analysis of:
- Existing tests (Phase 1)
- Critical business logic (Phase 2)
- User journeys (Phase 2)
- Integration points (Phase 2)

Create a TEST GAP MATRIX in this format:

| Component/Feature | Should Have | Currently Has | Gap | Priority |
|-------------------|-------------|---------------|-----|----------|
| {Component} | Unit, Integration | Unit only | Integration | High |

Include:
- All critical business logic areas
- All key user journeys
- All external integrations

Calculate:
- Total gaps by test type (Unit, Integration, E2E)
- Percentage coverage by area
- Risk score (High/Medium/Low based on gaps)
```

#### 7. Generate Actionable Recommendations

```
Based on the test gap matrix, generate prioritized recommendations.

Format each recommendation as:

## Recommendation {N}: {Title}

**Gap Identified**: {What's missing}
**Risk Level**: {High/Medium/Low}
**Business Impact**: {What could go wrong without this test}

**Recommended Tests**:
1. {Specific test to add}
   - Type: {Unit/Integration/E2E}
   - What it tests: {Description}
   - Estimated effort: {Hours}

**Acceptance Criteria for Test**:
- [ ] Covers happy path
- [ ] Covers error conditions
- [ ] Follows team testing patterns
- [ ] Integrated into CI/CD

---

Prioritize recommendations by:
1. Revenue/payment impact (highest priority)
2. Security/compliance impact
3. User experience impact
4. Developer confidence impact
```

### Phase 4: Create Test Coverage Map

#### 8. Generate Visual Coverage Map

```
Create a visual test coverage map showing:
1. **Coverage by Layer**: UI, API, Business Logic, Data Access, Integration — each with a percentage bar
2. **Coverage by Test Type**: Unit, Integration, E2E — each with a percentage bar
3. **Risk Heat Map**: High risk (untested critical), Medium risk (partially tested), Low risk (well tested) — with specific method/class names

Output as markdown for inclusion in documentation.
```

### Phase 5: Generate Test Specifications

#### 9. Create Test Specifications for Top Gaps

```
For the top 5 highest-priority test gaps, generate a test specification per gap:
- What we're testing (component + business purpose)
- Test scenarios in Given/When/Then format (happy path, error condition, edge case)
- Mocking requirements
- Integration requirements (sandbox credentials, test data setup)
- Automation notes (framework, estimated effort, prerequisites)
```

### Phase 6: Create Implementation Roadmap

#### 10. Generate Test Implementation Roadmap

```
Create a phased roadmap to close the identified test gaps:
- Sprint-by-sprint table: | Test | Type | Effort | Owner | Status |
- Acceptance criteria per sprint
- Regression & sanity checkpoints (smoke tests post-deploy, full regression before releases, stale tests removed, modularized by feature)
- Success metrics: current vs. target coverage for unit, integration, E2E, and critical paths
```

---

## Output Artifacts

After completing this workflow, you will have:

1. **Test Inventory** (`docs/test-inventory.md`)
   - Current test files and their coverage

2. **Coverage Gap Matrix** (`docs/test-gap-matrix.md`)
   - What should exist vs. what does exist

3. **Test Coverage Map** (`docs/test-coverage-map.md`)
   - Visual representation of coverage by layer

4. **Prioritized Recommendations** (`docs/test-recommendations.md`)
   - Actionable list of tests to add

5. **Test Specifications** (`docs/test-specifications/`)
   - Detailed specs for highest-priority gaps

6. **Implementation Roadmap** (`docs/test-roadmap.md`)
   - Sprint-by-sprint plan to close gaps

---

## Example Output Summary

For a payment service codebase with WorldPay/First Data integrations, the workflow typically produces:

| Area | Risk | Gap |
|------|------|-----|
| PaymentProcessor | High | No unit or integration tests |
| Gateway Client | High | No integration tests |
| Refund Service | High | No tests at all |
| Vault integration | Medium | Unit tests only |
| Checkout flow | High | No E2E tests |

---

## Tips for Best Results

### Provide Rich Context
Include:
- Product purpose and key user personas
- Known critical integrations
- Compliance requirements (PCI affects test needs)
- Recent production incidents (what should have been caught)

### Focus on Business Risk
Prioritize gaps by:
1. What could lose money (payments)
2. What could expose data (security)
3. What could break user experience
4. What could violate compliance

### Use Existing Knowledge
If you know areas that are problematic:
```
Focus particularly on the RefundService - we've had 3 production incidents there.
Also check the multi-tenant data isolation in PaymentRepository.
```

### Validate with QA Team
Share findings with QA for:
- Manual test knowledge (what's tested manually but not automated)
- Known problem areas
- Historical incident data

---

## Integration with Other Workflows

### Inputs From Other Workflows

**From Brownfield Repository Analysis** (`workflows/brownfield-repository-analysis.md`):
- **Risk hotspots** → Prioritize test coverage for high-risk areas
- **Core flows** → Ensure critical paths have coverage
- **Integration points** → Focus integration test effort
- **Data ownership** → Test data isolation boundaries

```
# Using brownfield analysis to inform test gap analysis
Read @GenDD-Flow/workflows/identify-test-gaps.md

Use the brownfield analysis from @docs/brownfield/:
- Risk hotspots in pass2-infer-findings.md → prioritize testing
- Core flows in gendd/flows/ → ensure flow coverage
- Integration points → focus integration tests

Generate prioritized test gap recommendations.
```

### Outputs To Other Workflows

1. **Generate Unit Tests** (`workflows/generate-unit-tests.md`)
   - Use test specifications from Phase 5 as input

2. **Automate Integration Testing** (`workflows/automate-integration-testing.md`)
   - Use integration gap analysis as input

3. **Story Quality (shift-left)** (`workflows/enhance-acceptance-criteria.md`)
   - Ensure new stories include test requirements upfront

4. **Context Packs** (`workflows/create-context-pack.md`)
   - Include testing standards in context documentation

---

## Success Metrics

- **Visibility**: Leadership can see test coverage status at a glance
- **Prioritization**: Team knows which tests to write first
- **Confidence**: Reduced downstream surprises from untested code
- **Efficiency**: Test effort focused on highest-risk areas
- **Compliance**: Coverage maps support audit requirements

---

## Common Pitfalls to Avoid

- ❌ **Chasing 100% coverage**: Focus on business-critical paths, not vanity metrics
- ❌ **Ignoring integration tests**: Unit tests alone don't catch integration failures
- ❌ **Outdated analysis**: Re-run this workflow quarterly or after major changes
- ❌ **No ownership**: Each test gap needs an owner and deadline
- ❌ **Ignoring manual tests**: Document what QA tests manually to avoid duplication
