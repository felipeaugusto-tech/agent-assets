# Workflow: Automate Integration Testing

## Context
Generate comprehensive test suites for third-party integrations.

## Prerequisites
- Access to integration code and documentation
- Cursor or similar AI IDE
- Test framework installed (xUnit, Jest, Playwright, Specflow)
- Test environment credentials (sandbox/test accounts)
- Understanding of integration's business purpose

## Related Templates
- **`templates/testing-standards.md`** - MUST/SHOULD/MAY levels, E2E rules, integration lifecycle
- **`templates/context-pack.md`** (File 4: testing.md) - Foundational naming, AAA, scenarios, mocking, coverage guidance

> **Key principles (from context-pack template):**
> - Tests follow AAA pattern (Arrange, Act, Assert) and have descriptive names
> - Mock external APIs in unit tests; use sandbox/test mode for integration tests
> - Required scenarios: happy path, invalid input, not found, external failure
> - Domain-specific: payment retry/idempotency, email deduplication/template data — when applicable
> - Multi-tenant isolation tests are required when code operates in a multi-tenant context

## When to Use This Workflow
- Implementing new third-party integration
- Existing integration lacks test coverage
- Integration causing production incidents
- Preparing for QA handoff
- Multi-tenant edge cases need validation
- Integration API version upgrade

## Test Types Covered

This workflow generates:
1. **Unit Tests**: Mock external API, test internal logic
2. **Integration Tests**: Hit real sandbox API, test end-to-end
3. **Contract Tests**: Verify API contract hasn't changed
4. **Edge Case Tests**: Timeouts, rate limits, errors
5. **Multi-Tenant Tests**: Data isolation validation

## Cursor Steps

### Phase 1: Understand the Integration

#### 1. Analyze Integration Code

Open Cursor in the integration file (e.g., `WorldPayClient.cs`):

```
Read @TargetRepo/.cursor/testing.md
Read @TargetRepo/.cursor/architecture.md

Analyze this integration code and describe:

1. **Purpose**: What does this integration do?
2. **Endpoints**: Which API endpoints are called?
3. **Authentication**: How does it authenticate?
4. **Data Flow**: What data is sent/received?
5. **Error Handling**: How are errors handled?
6. **Business Logic**: What processing happens?

For each method in this class:
- Method name
- Purpose
- Parameters
- Return type
- Error scenarios
- Dependencies

This will help me understand what needs to be tested.
```

#### 2. Identify Test Scenarios

```
Based on this integration code, identify all test scenarios needed.

Categories:
1. **Happy Path**: Normal successful operation
2. **Error Conditions**: API returns errors
3. **Edge Cases**: Nulls, empty responses, malformed data
4. **Performance**: Timeouts, slow responses
5. **Security**: Invalid credentials, expired tokens
6. **Multi-Tenant**: Data isolation (if applicable)
7. **Idempotency**: Retry scenarios
8. **Rate Limiting**: Throttling behavior
9. **Repeated Payment Prevention**: Duplicate submission within short window, same idempotency key
10. **Address Verification (AVS)**: Address data sent correctly to gateway, AVS response codes handled (match, partial match, no match, unavailable)
11. **Email/Notification Triggers**: Correct email dispatched on success, failure, and edge-case outcomes

For each scenario:
- Test name
- Preconditions
- Actions
- Expected outcome
- Test data needed

Prioritize by risk: What would cause the most damage if broken?
```

### Phase 2: Generate Unit Tests

#### 3. Create Unit Tests with Mocks

```
Generate unit tests for this integration class.

Requirements:
- Framework: {xUnit | NUnit | Jest | Pytest}
- Mocking: {Moq | jest.mock | unittest.mock}
- Follow Arrange-Act-Assert pattern
- Mock all external API calls
- Test each public method
- Cover happy path and error conditions
- Use descriptive test names (Given_When_Then format)

For each test:
1. Set up mocks (arrange)
2. Call method under test (act)
3. Verify outcome (assert)
4. Verify mock interactions

Generate complete test class with all tests.
```

See `templates/testing-standards.md` Unit Testing section for framework-specific examples following the AAA pattern.

#### 4. Review and Enhance Unit Tests

```
Review the generated unit tests and identify gaps:

Missing scenarios:
- What happens if HttpClient is null?
- What if the response is malformed JSON?
- What if the request timeout occurs?
- What about retry logic?
- Are all error codes covered?

Add tests for missing scenarios.
```

### Phase 3: Generate Integration Tests

#### 5. Create Integration Tests (Real API Calls)

```
Generate integration tests that call the real {API_NAME} sandbox environment.

Requirements:
- Use sandbox/test credentials
- Hit real API endpoints
- Validate end-to-end flow
- Clean up test data after each test
- Use test credit cards / test data
- Run independently (no shared state)

Test structure:
1. Setup (create test data)
2. Execute (call our integration, which calls external API)
3. Verify (check results)
4. Cleanup (delete test data)

Include:
- Happy path with real API
- Error scenarios (invalid card, expired card)
- Edge cases (minimum amount, maximum amount)
- Multi-tenant scenarios (if applicable)

Configuration needed:
- Sandbox URL: {URL}
- Test credentials: {KEY_VAULT_LOCATION}
- Test card numbers: {PROVIDE_TEST_CARDS}
```

See `templates/testing-standards.md` Integration Testing section for database lifecycle and external service testing patterns.

#### 6. Add Performance/Timeout Tests

```
Generate tests for performance and timeout scenarios:

1. **Response Time Test**: Verify API responds within acceptable time
2. **Timeout Test**: Verify our code handles API timeout gracefully
3. **Retry Test**: Verify retry logic works when API returns 503
4. **Circuit Breaker Test**: Verify circuit breaker opens after failures (if implemented)

For each test, use appropriate timing and mocking to simulate conditions.
```

### Phase 4: Generate UI/E2E Tests (Playwright/Specflow)

#### 7. Create End-to-End Tests

For UI integrations (e.g., payment forms):

```
Generate Playwright tests for the end-to-end payment flow.

Scenario: User makes a payment using WorldPay integration

Steps:
1. Navigate to checkout page
2. Fill in payment form
3. Submit payment
4. Verify success message
5. Verify transaction appears in database
6. Verify confirmation email sent (optional)

Test data:
- Test card: 4111111111111111
- Amount: $10.00
- User: test+{GUID}@{COMPANY_DOMAIN}

Generate TypeScript Playwright test.
```

Follow the E2E selector and waiting rules from `templates/testing-standards.md`. Use `data-testid` selectors exclusively and explicit waits (never `waitForTimeout`).

### Phase 5: Contract Testing

#### 8. Generate Contract Tests

```
Generate contract tests to verify the API contract hasn't changed.

Contract tests verify:
1. Request schema matches expectation
2. Response schema matches expectation
3. Required fields are present
4. Data types are correct
5. Error responses follow expected format

Use Pact or similar contract testing framework.

For each API endpoint:
- Define expected request schema
- Define expected response schema
- Generate test that validates schema

This is critical for {ORGANIZATION} because third-party APIs change without notice.
```

### Phase 5b: Email & Notification Integration Testing

If the integration triggers transactional emails, generate tests covering the Email & Notification Scenarios from the testing standards (delivery triggers, template selection, data population, deduplication, edge cases). Mock the email provider in unit tests; use sandbox/test mode for integration tests. Never send to real email addresses in tests.

### Phase 6: Test Data and Configuration

#### 9. Create Test Data Fixtures

```
Generate test data fixtures for common scenarios.

Create:
1. **Valid test cases**: Cards, amounts, user data
2. **Invalid test cases**: Expired cards, over-limit amounts
3. **Edge cases**: Zero amount, maximum amount, special characters
4. **Multi-tenant data**: Separate data per tenant

Format: JSON files or code constants

Include documentation:
- What each test case represents
- Expected outcome
- Where to use it
```

For test card numbers, see `templates/testing-standards.md` Test Data Management section.

#### 10. Configure Test Environments

```
Generate configuration files for test environments.

Create:
1. **appsettings.Test.json** (or equivalent)
   - Sandbox URLs
   - Test credentials location (Key Vault)
   - Test merchant IDs
   - Timeouts
   - Retry settings

2. **docker-compose.test.yml**
   - Test database
   - Mock external services (if needed)
   - Test Redis cache

3. **CI/CD test configuration**
   - Environment variables
   - Test secrets
   - Test execution settings

Document:
- How to run tests locally
- How tests run in CI/CD
- How to add new test credentials
```

### Phase 7: Test Organization and CI/CD

#### 11. Organize Tests for CI/CD

```
Create a test organization strategy for CI/CD.

Test Categories:
1. **Unit Tests**: Fast, run on every commit
2. **Integration Tests (Sandbox)**: Slower, run before merge
3. **E2E Tests**: Slowest, run nightly or before release
4. **Contract Tests**: Run daily to detect API changes

Generate CI/CD configuration:
- Run unit tests on every PR
- Run integration tests before merge to main
- Run E2E tests nightly
- Fail build if coverage drops below threshold

For {GitHub Actions | Azure Pipelines | GitLab CI}, generate workflow file.
```

Generate a CI/CD workflow file for your platform. See `templates/testing-standards.md` CI/CD Integration section for stage definitions and example commands.

## Success Metrics
- **Test Coverage**: 80%+ for integration code
- **Test Execution Time**: Unit tests <5min, integration tests <15min
- **Test Reliability**: <5% flaky tests
- **Defect Detection**: Catch integration issues before production
- **Time Saved**: 70% reduction in manual testing effort

## Tips for Best Results

### Start with High-Risk Integrations
- Payment gateways (WorldPay, First Data)
- Authentication providers (SSO)
- Integrations with high failure rates

### Use Real Sandbox APIs
- More confidence than mocks alone
- Catches real API behavior changes
- Validates authentication flows

### Maintain Test Data
- Keep test cards/credentials current
- Document test data purpose
- Clean up after tests

### Monitor Test Health
- Track flaky tests
- Fix or disable unreliable tests
- Review test failures promptly

## Common Pitfalls to Avoid
- ❌ **Only unit tests**: Need real API integration tests too
- ❌ **Shared test data**: Tests interfere with each other
- ❌ **No cleanup**: Test data accumulates in sandbox
- ❌ **Hardcoded credentials**: Use Key Vault / secrets
- ❌ **Ignoring multi-tenant**: Critical for {ORGANIZATION}'s architecture
- ❌ **Flaky tests**: Fix or remove unreliable tests

## Follow-Up Workflows
After generating integration tests:
1. Use `workflows/generate-unit-tests.md` for additional unit tests
2. Use `workflows/identify-test-gaps.md` to verify remaining coverage gaps
3. Set up monitoring/alerting for integration failures in production
4. Create runbook for troubleshooting integration issues

