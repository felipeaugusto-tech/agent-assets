# Quality Assurance -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Quality Assurance lens.
> This area combines manual QA engineering and test automation engineering perspectives.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Test directories and files | HIGH | `tests/`, `__tests__/`, `*.test.ts`, `*.spec.ts`, `*_test.go`, `test_*.py` |
| Test framework configuration | HIGH | `jest.config.js`, `vitest.config.ts`, `pytest.ini`, `xunit.runner.json`, `playwright.config.ts` |
| CI pipeline with test stages | HIGH | `.github/workflows/` with test steps, `Jenkinsfile` with test stages |
| E2E test configuration | HIGH | `playwright.config.ts`, `cypress.config.ts`, `e2e/` directory |
| Test coverage configuration | MEDIUM | `.nycrc`, `jest --coverage`, `coverageThreshold` in config |
| Test fixture files | MEDIUM | `fixtures/`, `factories/`, `__mocks__/`, `testdata/` |
| Page object pattern files | MEDIUM | `pages/` in test directory, `*Page.ts`, `*PageObject.ts` |
| Contract test files | LOW | `*.pact.ts`, `contract/`, Pact/contract test config |
| Test reporting configuration | LOW | JUnit XML output config, Allure config, test reporter plugins |

## What to Analyze

### Test Inventory
- Look for: All test files categorized by type (unit, integration, E2E, contract)
- Look for: Test count per category and framework used
- Look for: Last modification dates of test files
- Assess: Whether test inventory matches the application's complexity
- Document: Test inventory table with type, location, framework, count, and recency

### Coverage Analysis
- Look for: Coverage reports and thresholds in configuration
- Look for: Coverage per component/module (not just overall percentage)
- Assess: Whether critical business logic has adequate coverage
- Assess: Test pyramid balance (many units, fewer integration, fewest E2E)
- Document: Coverage by component with test pyramid analysis and balance assessment

### Test Gap Analysis
- Look for: Features or modules with no test coverage
- Look for: Critical paths (auth, payments, data mutations) without integration or E2E tests
- Assess: Business risk of each gap (what breaks if this code has a bug?)
- Document: Gap inventory prioritized by business impact with expected vs. actual coverage

### Test Quality Assessment
- Look for: Test naming conventions (descriptive, consistent)
- Look for: Arrange-Act-Assert (AAA) pattern adherence
- Look for: Test isolation (no shared mutable state, no ordering dependencies)
- Look for: Flaky test indicators (retry logic, timing-dependent assertions, external dependencies)
- Look for: Test data management (factories, builders, static fixtures)
- Look for: Mock usage (appropriate vs. over-mocking vs. under-mocking)
- Assess: Overall test reliability and maintainability
- Document: Quality assessment per dimension with issues found and examples

### Acceptance Criteria Testability
- Look for: Whether acceptance criteria follow Gherkin format (Given/When/Then)
- Look for: Whether ACs describe expected behavior vs. implementation steps
- Look for: Whether happy path and edge cases are covered
- Look for: Whether integration behavior expectations are documented
- Look for: Presence of data-testid attributes for automation
- Assess: Whether ACs are automatable as written
- Document: AC testability assessment with common quality issues

### E2E Test Infrastructure
- Look for: Browser automation framework (Playwright, Cypress, Selenium)
- Look for: Headless execution support
- Look for: Screenshot/video capture on failure
- Look for: Trace collection capability
- Look for: Cross-browser test configuration
- Look for: Page Object Pattern implementation
- Assess: E2E infrastructure reliability and completeness
- Document: E2E infrastructure summary with framework, capabilities, and patterns

### CI/CD Test Integration
- Look for: Which tests run at which pipeline stage (PR, merge, nightly)
- Look for: Test parallelization configuration
- Look for: Dependency caching for test runs
- Look for: Retry logic for flaky tests
- Look for: Test reporting format (JUnit XML, artifacts)
- Look for: Failure notification configuration
- Assess: Pipeline efficiency and reliability
- Document: Pipeline test integration with stages, duration, pass rate, and optimization opportunities

### Test Data Management
- Look for: Fixture patterns (factories, builders, static files, API seeding)
- Look for: Database state management (transactions, snapshots, fresh DB per test)
- Look for: Test isolation mechanisms
- Look for: Sensitive data handling in tests (masking, vaulting)
- Assess: Whether test data approach is maintainable and reliable
- Document: Test data strategy with patterns, isolation approach, and issues

### Domain-Specific Testing
- Look for: Payment/financial test scenarios (card validation, idempotency, anomaly detection)
- Look for: Email/notification test coverage (delivery triggers, template selection, deduplication)
- Look for: Security/auth test scenarios (lockout, password policy, session expiry)
- Look for: Regression/sanity test suites (smoke tests, post-deploy checks)
- Look for: UI/accessibility test scenarios (WCAG compliance, responsive breakpoints)
- Look for: Cross-layer testing (same feature tested at unit, API, and E2E levels)
- Document: Domain-specific coverage with gaps per applicable domain

### Test Performance and Scalability
- Look for: Unit test suite execution time
- Look for: Integration test execution time
- Look for: E2E test execution time
- Look for: Parallelization configuration and worker count
- Assess: Whether test execution time is within acceptable bounds for CI feedback
- Document: Test performance metrics with current times, targets, and optimization recommendations

## Key Questions to Answer

1. What test frameworks are used and how are tests organized?
2. What is the current test coverage and where are the critical gaps?
3. Is the test pyramid balanced (units > integration > E2E)?
4. Are tests reliable or are flaky tests a significant problem?
5. What CI pipeline stages run which tests, and what are the execution times?
6. Are acceptance criteria written in a testable format?
7. What test data management approach is used?
8. What E2E automation infrastructure exists and how mature is it?
9. Are domain-specific test scenarios adequately covered?
10. What are the highest-priority test gaps by business risk?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Inverted Test Pyramid | More E2E than unit tests | Slow feedback, brittle, hard to maintain |
| Test Desert | Large modules with zero test coverage | High risk, unknown behavior |
| Over-Mocking | Tests mock everything including the thing being tested | Tests pass but do not validate behavior |
| Snapshot Testing Overuse | Many `*.snap` files, snapshot tests for complex components | Brittle, approves changes without review |
| Shared Test State | Tests depend on execution order, global test setup | Flaky tests, hard to parallelize |
| Factory Pattern | `UserFactory.create()`, `build()` patterns | Good test data management |
| Page Object Pattern | `LoginPage`, `DashboardPage` classes in test code | Good E2E maintainability |
| Contract Testing | Pact files, consumer/provider test separation | Strong API contract verification |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| Zero test coverage on critical business logic | No tests in payment, auth, or data mutation paths | HIGH |
| No E2E tests for critical user journeys | Missing E2E tests for login, checkout, main feature flows | HIGH |
| Flaky test rate above 10% | Test retry counts, intermittent CI failures | HIGH |
| No integration tests | Missing test category between unit and E2E | MEDIUM |
| Tests not running in CI | No test steps in pipeline configuration | HIGH |
| Missing test data isolation | Shared database state between test runs | MEDIUM |
| No acceptance criteria defined | Stories without testable ACs | MEDIUM |
| Stale tests | Test files not modified in >6 months while source changed | MEDIUM |
| No test coverage reporting | Missing coverage configuration in CI | LOW |
| Missing data-testid attributes | UI elements without automation hooks | LOW |

## Output Guidance

### Must Include
- Test inventory by type with framework, count, and coverage
- Test pyramid analysis showing balance across unit, integration, and E2E
- Critical test gaps prioritized by business risk
- Test quality assessment (naming, isolation, flakiness, AAA adherence)
- CI pipeline test integration summary with stages and execution times

### Should Include (if detected)
- Acceptance criteria testability assessment
- E2E automation infrastructure analysis
- Test data management strategy
- Domain-specific test coverage (payments, auth, notifications)
- Test performance metrics with optimization recommendations
- Flaky test analysis with root causes

### Related Areas
- [backend-development](./backend-development.md) -- backend test patterns, service layer coverage
- [frontend-development](./frontend-development.md) -- component testing, E2E patterns
- [devops-infrastructure](./devops-infrastructure.md) -- CI pipeline test integration
- [security](./security.md) -- security testing, auth test scenarios
- [user-experience](./user-experience.md) -- accessibility testing, UI test coverage
- [delivery-management](./delivery-management.md) -- DoR/DoD compliance, AC quality
