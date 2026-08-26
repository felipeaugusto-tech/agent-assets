# Generate Integration Tests

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | Backend Dev, Fullstack Dev, QA Automation, QA Engineer |
| **Prerequisites** | Integration code exists, test framework installed, sandbox/test credentials available |
| **Inputs** | Path to integration client code, integration name and type, test framework, sandbox URL and credentials |
| **Outputs** | Unit tests (mocked), integration tests (sandbox), edge case tests, multi-tenant tests, test data fixtures |

## When to Use

- Implementing a new third-party integration that needs test coverage
- Existing integration lacks tests and is causing production incidents
- Preparing for QA handoff on integration-heavy features
- Integration API version upgrade requires regression testing

## Before You Start

- [ ] Integration code is identified (e.g., `WorldPayClient.cs`, `sendgrid-service.ts`)
- [ ] Test framework is installed (xUnit, Jest, pytest, Playwright)
- [ ] Sandbox/test environment credentials are available (Key Vault or config)
- [ ] You know the integration type (Payment Gateway, Email, Auth, Data Sync, API)

## Steps

### Step 1: Analyze the integration code

- Do: Understand what the integration does and how it works
- How: Open the integration file in Cursor and ask:
  ```
  Analyze this integration code and describe:
  1. Purpose and endpoints called
  2. Authentication method
  3. Data flow (sent/received)
  4. Error handling approach
  5. Business logic and processing
  ```
- Expect: A clear understanding of all methods, their parameters, return types, and error scenarios

### Step 2: Generate unit tests with mocks

- Do: Create unit tests that mock the external API
- How: Use Cursor Chat:
  ```
  Read @GenDD-Flow/workflows/automate-integration-testing.md
  Read @GenDD-Flow/templates/testing-standards.md
  Read @TargetRepo/.cursor/testing.md
  Read @TargetRepo/.cursor/architecture.md

  Generate integration tests for @TargetRepo/[path/to/integration-client]:

  Integration: [NAME - e.g., WorldPay, SendGrid, Vault]
  Type: [Payment Gateway | Email | Auth | Data Sync | API]

  Generate:

  ## 1. Unit Tests (Mocked)
  - Mock external API responses
  - Test internal logic
  - Cover error handling
  - Cover retry logic

  ## 2. Integration Tests (Real Sandbox)
  - Use sandbox/test credentials
  - Hit real API endpoints
  - Validate end-to-end flow
  - Clean up test data

  ## 3. Edge Case Tests
  - API timeout handling
  - Rate limiting behavior
  - Malformed responses
  - Invalid credentials

  ## 4. Multi-Tenant Tests (if applicable)
  - Data isolation validation
  - Cross-tenant access prevention

  ## 5. Test Data Fixtures
  - Valid test cases
  - Invalid test cases
  - Edge case data

  Framework: [xUnit | Jest | pytest]
  Sandbox URL: [URL if known]
  Test credentials: [Key Vault location or placeholder]
  ```

#### Payment Integration Variant

  Add to the prompt above:
  ```
  Payment Gateway: [WorldPay | First Data | Stripe]
  Focus on: authorize, capture, void, refund, timeout handling, multi-tenant isolation
  Use test cards from testing-standards.md Test Data Management section.
  Include cleanup to void test transactions.
  ```

#### API Integration Variant

  Add to the prompt above:
  ```
  API: [NAME], Base URL: [URL], Auth: [API Key | OAuth | Basic]
  Focus on: success, auth failure, rate limiting (429), server error (500), timeout, retry logic
  Include contract validation for response schema.
  ```
- Expect: Complete test suites across all categories

### Step 3: Generate sandbox integration tests

- Do: Create tests that call the real sandbox API
- How: Configure sandbox credentials and generate real API tests:
  ```
  Generate integration tests that call the real [API_NAME] sandbox:

  - Use sandbox/test credentials from Key Vault
  - Hit real API endpoints
  - Validate end-to-end flow
  - Clean up test data after each test
  - Run independently (no shared state)
  ```
- Expect: Tests that validate real API behavior including happy path, errors, and edge cases

### Step 4: Add performance and timeout tests

- Do: Generate tests for timeout handling, retry logic, and circuit breakers
- How: Ask Cursor to add performance-related test scenarios
- Expect: Tests covering API timeout, retry logic, rate limiting (429), and circuit breaker behavior

### Step 5: Create test data fixtures

- Do: Generate structured test data for all scenarios
- How: Create JSON fixtures or code constants for valid, invalid, and edge case data
- Expect: Reusable test data files with documented purpose for each test case

### Step 6: Configure CI/CD integration

- Do: Set up tests to run in the pipeline
- How: Configure test categories:
  - Unit tests: Run on every PR
  - Integration tests (sandbox): Run before merge to main
  - E2E tests: Run nightly
- Expect: CI/CD pipeline configuration that runs appropriate test suites at each stage

## Expected Output

```
@TargetRepo/tests/
├── Unit/
│   └── [Integration]ClientTests.[ext]      # Mocked unit tests
├── Integration/
│   └── [Integration]IntegrationTests.[ext]  # Sandbox API tests
└── Fixtures/
    └── [integration]-test-data.json         # Test data fixtures
```

**Save to:** `@TargetRepo/tests/` following project test organization

## What's Next

- [ ] Set up test credentials in Key Vault for CI/CD
- [ ] Add integration tests to nightly test suite
- [ ] Review with team for additional edge cases

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Integration Testing Workflow | `workflows/automate-integration-testing.md` | Full 7-phase workflow with CI/CD configuration |
| Testing Standards Template | `templates/testing-standards.md` | MUST/SHOULD/MAY test requirement levels |
| Context Pack Template | `templates/context-pack.md` (testing.md section) | Universal naming, AAA, scenarios, coverage |
