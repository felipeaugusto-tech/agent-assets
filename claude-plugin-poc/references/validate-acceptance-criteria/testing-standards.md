# Testing Standards Template

> This template provides implementation-specific testing standards. Foundational principles (naming, AAA pattern, required scenarios) are embedded in the Context Pack template at `templates/context-pack.md` (File 4: testing.md section).

## Purpose

Use this template to create repository-specific `testing.md` files. Copy and customize the sections below, filling in your specific frameworks and requirements.

---

## Requirement Levels

| Level | Meaning | Enforcement |
|-------|---------|-------------|
| **MUST** | Mandatory, non-negotiable | CI/CD blocks on failure |
| **SHOULD** | Recommended best practice | PR review feedback |
| **MAY** | Optional enhancement | Team discretion |

---

## Foundational Standards

The following foundational principles apply to all repositories (see `templates/context-pack.md` for full details):

- **Test Naming:** Test names must communicate intent. Common patterns include `{Method}_{Scenario}_{ExpectedResult}`, descriptive strings, or fixture-based grouping — choose what fits the repo's language and framework.
- **Test Structure:** Arrange-Act-Assert (AAA) pattern — every test has setup, execution, and verification sections.
- **Test Independence:** No shared mutable state, no order dependency, isolated side effects, independent setup.
- **Required Scenarios:** Happy path, invalid input, not found (always). Authorization, authentication, external failure, multi-tenant isolation (when applicable). Domain-specific scenarios (payment, notification, security, UI) only when the code handles that domain.
- **Mocking Guidelines:** Mock at boundaries (external APIs, databases in unit tests, file system, time/randomness). Do NOT mock the code under test, simple value objects, pure functions, or internal implementation.
- **Coverage:** Priority-based (critical business logic > public APIs > data access > infrastructure). Set numeric targets per repository based on maturity and risk.

---

## Unit Testing (.NET Example)

### Coverage Requirements (MUST)

| Area | Minimum | Rationale |
|------|---------|-----------|
| Payment/Financial code | 100% | Money-handling risk |
| Authentication/Authorization | 95% | Security risk |
| Business logic | 80% | Core functionality |
| Utilities/Helpers | 70% | Lower risk |

### Example

```csharp
[Fact]
public void ProcessPayment_ValidToken_ReturnsSuccess()
{
    // Arrange
    var mockGateway = new Mock<IPaymentGateway>();
    mockGateway.Setup(g => g.Charge(It.IsAny<ChargeRequest>()))
        .Returns(new ChargeResult { Success = true });
    var service = new PaymentService(mockGateway.Object);

    // Act
    var result = service.ProcessPayment("tok_valid", 2000);

    // Assert
    Assert.True(result.Success);
    mockGateway.Verify(g => g.Charge(It.Is<ChargeRequest>(
        r => r.Amount == 2000)), Times.Once);
}
```

### SHOULD (Recommended)

- Use test data builders for complex objects
- Group related tests in nested classes
- Include performance assertions for critical paths

---

## Integration Testing

### MUST (Enforced)

| Rule | Rationale |
|------|-----------|
| Start from clean database state | Prevents test pollution |
| No test order dependency | Tests run in any order |
| Clean up data after tests | Prevents accumulation |
| Use transactions where possible | Fast rollback |
| Isolate test tenants | Multi-tenant safety |

### Database Lifecycle Example

```csharp
public class PaymentIntegrationTests : IAsyncLifetime
{
    private readonly TestDatabase _db;
    
    public async Task InitializeAsync()
    {
        await _db.ResetAsync();
        await _db.SeedTestDataAsync();
    }
    
    public async Task DisposeAsync()
    {
        await _db.CleanupTestDataAsync();
    }
}
```

### External Service Testing

```csharp
// MUST: Use sandbox/test credentials
[Fact]
public async Task ProcessPayment_Integration_UsesTestMode()
{
    var config = new PaymentConfig 
    { 
        ApiKey = Environment.GetEnvironmentVariable("STRIPE_TEST_KEY"),
        IsSandbox = true  // MUST be true in tests
    };
    
    var result = await _paymentService.Charge("tok_visa", 2000);
    
    // MUST: Cleanup - void test transactions
    await _paymentService.Void(result.TransactionId);
}
```

---

## E2E Testing (Playwright/Cypress)

### Selector Rules (MUST)

| Do | Don't |
|----|-------|
| `[data-testid="submit-button"]` | `button:has-text("Submit")` |
| `[data-testid="email-input"]` | `.btn-primary`, `#submit` |
| Explicit data attributes | XPath, text selectors, CSS classes |

### Waiting Rules (MUST)

| Do | Don't |
|----|-------|
| `waitForSelector('[data-testid="..."]')` | `waitForTimeout(3000)` |
| `waitForResponse(...)` | `sleep(5000)` |
| `expect(...).toBeVisible()` | Arbitrary delays |

### Example

```typescript
describe('Order Creation', () => {
    beforeEach(async () => {
        await resetTestData();
        await loginAsTestUser();
    });
    
    test('creates order successfully', async () => {
        await page.click('[data-testid="new-order-btn"]');
        await page.fill('[data-testid="amount-input"]', '100');
        await page.click('[data-testid="submit-btn"]');
        
        await expect(page.locator('[data-testid="success-message"]')).toBeVisible();
    });
});
```

---

## Domain-Specific Test Scenarios (Inherited)

The following scenario checklists apply when your repository touches the relevant domain. See `templates/context-pack.md` (File 4: testing.md section) for the full tables with "Applies When" guidance.

| Domain | Key Scenarios | Principles Section |
|--------|---------------|--------------------|
| **Payment / Financial** | Card validation (Luhn, length, prefix), AVS, PIN masking, idempotency, anomaly detection | Section 4 — Payment-Domain Scenarios |
| **Email / Notifications** | Delivery triggers, template data population, receipt accuracy, deduplication | Section 4 — Email & Notification Scenarios |
| **Security / Auth** | Account lockout, password policy, session expiry | Section 4 — Security & Access Control Scenarios |
| **Regression / Sanity** | Health endpoint, critical-path smoke test, full regression suite | Section 4 — Regression & Sanity Scenarios |
| **UI / Accessibility** | Responsive breakpoints, WCAG 2.1 AA, keyboard navigation | Section 4 — UI & Usability Scenarios |

### Enforcement Levels for This Template

When customizing for your repository, assign MUST/SHOULD/MAY levels to each applicable scenario:

- **MUST** — Payment input validation, email delivery triggers, account lockout, sanity/smoke tests
- **SHOULD** — Anomaly detection, full regression suite, responsive design, accessibility (WCAG 2.1 AA)
- **MAY** — Frequency anomaly flagging, usability/user-acceptance testing

---

## Test Data Management

### Test Cards Reference

| Card Number | Scenario |
|-------------|----------|
| 4111111111111111 | Success |
| 4000000000000002 | Declined |
| 4000000000000341 | Insufficient funds |

### Data Patterns

For test data builders, fixtures, and guidance on avoiding magic values, see the Test Data Management section in `templates/context-pack.md` (File 4: testing.md).

```typescript
// Example: Data factory pattern
const testUser = TestDataFactory.createUser({
    role: 'admin',
    tenant: 'test-tenant-1'
});
```

---

## CI/CD Integration

| Stage | Tests Run | Blocking |
|-------|-----------|----------|
| PR | Unit + Fast Integration | Yes |
| Merge to main | Full Integration | Yes |
| Nightly | E2E + Load | No (alerts) |

### Commands

```bash
# Unit tests (MUST pass for PR)
dotnet test --filter "Category=Unit"

# Integration tests (MUST pass for merge)
dotnet test --filter "Category=Integration"

# E2E tests (nightly)
npx playwright test
```

---

## Usage

1. Copy this template to your repository's `testing.md`
2. Replace framework examples with your specific frameworks
3. Customize coverage requirements for your risk profile
4. Review with QA team
5. Integrate into CI/CD pipeline

## Related Templates

- [Context Pack Template](context-pack.md) - Foundational testing principles (File 4: testing.md section)

## Used By

| Resource | Path | How It's Used |
|----------|------|---------------|
| Identify Test Gaps Workflow | `workflows/identify-test-gaps.md` | Defines MUST/SHOULD/MAY levels for gap assessment |
| Generate Unit Tests Workflow | `workflows/generate-unit-tests.md` | Naming, AAA, and coverage standards for generated tests |
| Generate Tests from Gherkin Workflow | `workflows/generate-tests-from-gherkin.md` | Standards for Gherkin-to-test conversion |
| Integration Testing Workflow | `workflows/automate-integration-testing.md` | Integration lifecycle and E2E rules |
| QA Engineer Playbook | `playbooks/by-role/qa-engineer.md` | Test quality assessment criteria |
| Run Assisted Testing Playbook | `playbooks/on-demand/run-assisted-testing.md` | Selector rules and E2E patterns |
| Validate AC Playbook | `playbooks/on-demand/validate-acceptance-criteria.md` | Selector naming standards |
