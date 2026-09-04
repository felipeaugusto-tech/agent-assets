# Workflow: Generate Unit Tests

## Context
Generate comprehensive unit tests for existing code, following established patterns and standards.

## Prerequisites
- Code file to test
- Understanding of business logic
- Test framework installed

## Related Templates
- **`templates/testing-standards.md`** - MUST/SHOULD/MAY requirement levels, naming conventions, coverage targets
- **`templates/context-pack.md`** (File 4: testing.md) - Foundational naming, AAA, scenarios, mocking, coverage guidance

> **Key principles (from context-pack template):**
> - Test names must communicate intent (e.g., `Method_Scenario_ExpectedResult` or equivalent)
> - Tests follow AAA pattern (Arrange, Act, Assert)
> - Required scenarios: happy path, invalid input, not found
> - Mock at boundaries (interfaces, external services), not internal classes
> - Domain-specific scenarios (payment, notification, auth) apply only when the code handles that domain

---

## Cursor Steps

### 1. Open the file to test
Example: `PaymentService.cs`

### 2. Use Cursor Chat (Cmd+L)

```
Read @GenDD-Flow/templates/testing-standards.md
Read @TargetRepo/.cursor/testing.md
Read @TargetRepo/.cursor/conventions.md

Analyze this code and generate comprehensive unit tests.

Requirements:
- Framework: xUnit with Moq
- Coverage: All public methods
- Naming: {Method}_{Scenario}_{ExpectedResult}
- Pattern: Arrange-Act-Assert

Test scenarios (MUST cover):
* Happy path
* Edge cases (null, empty, boundary values)
* Error conditions
* Multi-tenant scenarios (if applicable)
* Integration failure scenarios (mocked)
* Domain-specific scenarios from testing standards (payment, email, security — when applicable)

Follow the MUST/SHOULD/MAY levels from testing-standards.md.
```

### 3. Review generated tests

Check for:
- [ ] Naming follows `{Method}_{Scenario}_{ExpectedResult}`
- [ ] Arrange-Act-Assert pattern used
- [ ] Mock dependencies properly
- [ ] Test isolation (no shared state)
- [ ] Descriptive test names
- [ ] All public methods covered
- [ ] Error scenarios included

### 4. Iterate if needed

```
Add tests for the edge case where {SCENARIO}.
Ensure the mock setup for {DEPENDENCY} handles {CONDITION}.
```

### 5. Run tests and verify coverage

```bash
# Run tests
dotnet test --filter "Category=Unit"

# Check coverage
dotnet test --collect:"XPlat Code Coverage"
```

---

## Test Standards

For MUST/SHOULD/MAY requirement levels, coverage targets, and framework-specific examples, see `templates/testing-standards.md`.

---

## Follow-Up
After generating tests:
1. Run tests locally to verify they pass
2. Check coverage meets thresholds
3. Add to CI/CD pipeline
4. Review with team for edge cases

## Related Workflows
- **`workflows/identify-test-gaps.md`** - Upstream: use gap analysis to identify which files need tests
- **`workflows/automate-integration-testing.md`** - For integration test generation
