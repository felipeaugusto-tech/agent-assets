# Generate Unit Tests

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | Backend Dev, Frontend Dev, Fullstack Dev, QA Automation |
| **Prerequisites** | Code file to test exists, test framework installed, understanding of business logic |
| **Inputs** | Path to the source file to test, test framework name, specific methods to focus on (optional) |
| **Outputs** | Complete test file with unit tests covering happy path, edge cases, and error conditions |

## When to Use

- Writing tests for new or existing code that lacks coverage
- After identifying test gaps via the test gap analysis workflow
- During development when you need comprehensive tests for a class or module
- Before code review to ensure adequate test coverage

## Before You Start

- [ ] Source file to test is identified and accessible
- [ ] Test framework is installed and configured (xUnit, Jest, pytest, etc.)
- [ ] You know the mocking library in use (Moq, jest.mock, unittest.mock, etc.)
- [ ] You understand the business logic of the code being tested

## Steps

### Step 1: Open the source file

- Do: Navigate to the file you want to generate tests for
- How: Open the file in Cursor (e.g., `PaymentService.cs`, `checkout.ts`)
- Expect: Full visibility of the class, its methods, and dependencies

### Step 2: Generate comprehensive unit tests

- Do: Use AI to generate a complete test suite
- How: Open Cursor Chat and use:
  ```
  Read @GenDD-Flow/workflows/generate-unit-tests.md
  Read @GenDD-Flow/templates/testing-standards.md
  Read @TargetRepo/.cursor/testing.md
  Read @TargetRepo/.cursor/conventions.md

  Analyze @TargetRepo/[path/to/file.cs|ts|py] and generate comprehensive unit tests.

  Requirements:
  - Framework: [xUnit | NUnit | Jest | pytest | Moq | etc.]
  - Naming: MethodName_Scenario_ExpectedResult
  - Pattern: Arrange-Act-Assert
  - Coverage: All public methods

  Test Scenarios (for each method):
  1. Happy path - normal successful operation
  2. Edge cases - null, empty, boundary values
  3. Error conditions - exceptions, failures
  4. Multi-tenant scenarios (if applicable)
  5. Integration failure scenarios (mocked)

  Generate complete test class with:
  - Proper mock setup
  - Test data builders (if complex data)
  - Clear comments explaining each test
  - Async handling where needed
  ```

#### Quick Version

  ```
  Read @GenDD-Flow/workflows/generate-unit-tests.md
  Read @TargetRepo/.cursor/testing.md

  Generate unit tests for @TargetRepo/[path/to/file]:
  - Framework: [FRAMEWORK]
  - Focus: [SPECIFIC METHODS or "all public methods"]
  - Include: Happy path, errors, edge cases
  ```

- Expect: A complete test file with tests for all public methods

### Step 3: Review generated tests

- Do: Verify the generated tests meet quality standards
- How: Check against this list:
  - [ ] Naming follows `{Method}_{Scenario}_{ExpectedResult}`
  - [ ] Arrange-Act-Assert pattern used consistently
  - [ ] Dependencies are properly mocked
  - [ ] Tests are isolated (no shared mutable state)
  - [ ] All public methods have at least one test
  - [ ] Error scenarios and edge cases are included
- Expect: Tests pass review or specific gaps identified for iteration

### Step 4: Iterate on gaps

- Do: Add tests for any missing scenarios
- How: Ask Cursor to fill specific gaps:
  ```
  Add tests for the edge case where [SCENARIO].
  Ensure the mock setup for [DEPENDENCY] handles [CONDITION].
  ```
- Expect: Additional tests covering identified gaps

### Step 5: Run tests and verify coverage

- Do: Execute the tests locally and check coverage
- How: Run the test and coverage commands for your framework (see `templates/testing-standards.md` CI/CD section for examples)
- Expect: All tests pass and coverage meets project thresholds (80%+ business logic)

## Expected Output

```
@TargetRepo/tests/Unit/
└── [ClassName]Tests.[ext]    # Complete test file with all scenarios
```

**Save to:** `@TargetRepo/tests/Unit/` (following project test organization)

## What's Next

- [ ] [Generate Integration Tests](generate-integration-tests.md) for external service interactions
- [ ] Add tests to CI/CD pipeline if not already configured
- [ ] Review with team for additional edge cases

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Unit Test Workflow | `workflows/generate-unit-tests.md` | Detailed workflow with test standards and examples |
| Testing Standards Template | `templates/testing-standards.md` | MUST/SHOULD/MAY test requirement levels |
| Context Pack Template | `templates/context-pack.md` (testing.md section) | Universal naming, AAA, scenarios, coverage |
