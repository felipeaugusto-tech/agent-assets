# Run Playwright Assisted Testing

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | QA Engineer, QA Automation, Frontend Dev |
| **Prerequisites** | Playwright MCP configured in Cursor, application running at accessible URL |
| **Inputs** | Application base URL, login credentials (if needed), pages/features to test |
| **Outputs** | Selector inventory (JSON), Page Object files, E2E test suite, test data fixtures |

## When to Use

- Need to generate E2E tests for a feature using real application discovery
- Building a Playwright test suite from scratch for an existing application
- Mapping UI elements and selectors for test automation
- Validating form behavior, navigation flows, and error states

## Before You Start

- [ ] Playwright MCP server is running and configured in Cursor
- [ ] Application is accessible at a known URL
- [ ] Login credentials are available for test accounts (if needed)
- [ ] You know which pages/features need test coverage

## Steps

### Step 1: Discover application pages and elements

- Do: Navigate the application and inventory all interactive elements
- How: Use Cursor with Playwright MCP:
  ```
  Read @GenDD-Flow/templates/testing-standards.md
  Read @TargetRepo/.cursor/testing.md

  Using Playwright MCP, navigate to [BASE_URL] and perform discovery:

  1. Take a screenshot of the current page
  2. List all interactive elements:
     - Buttons (with their text/labels)
     - Form inputs (with their types and names)
     - Links (with their destinations)
     - Data-testid attributes (PRIORITY - these are our selectors)

  3. Identify the page structure:
     - Header/Navigation
     - Main content area
     - Sidebar (if present)
     - Footer

  Output as structured JSON.
  ```

#### Quick Minimal Discovery

  ```
  Using Playwright MCP:
  1. Navigate to [URL]
  2. Screenshot the page
  3. List all data-testid attributes
  4. Output as JSON
  ```
- Expect: A JSON inventory of pages, elements, and selectors

### Step 2: Multi-page crawl and authentication flow

- Do: Discover key pages and the authentication flow
- How: Navigate to each key page and the login flow:
  ```
  Using Playwright MCP, starting from [BASE_URL]:

  1. Navigate to each key page and screenshot each
  2. Extract ALL [data-testid] attributes per page
  3. Map navigation paths between pages
  4. Analyze the authentication flow (login form elements, post-login state)

  Output: Page inventory JSON + screenshots
  ```
- Expect: Complete page inventory with selectors and navigation map

### Step 3: Generate selector inventory

- Do: Create a structured selector inventory following testing standards
- How: Based on discovered pages, organize selectors by page:
  ```
  Based on discovered pages, create a selector inventory:
  - Primary: [data-testid] selectors (MUST use when available)
  - Fallback: Alternative selectors (when data-testid missing)
  - Missing: Elements that SHOULD have data-testid but don't
  ```
- Expect: JSON selector inventory with primary, fallback, and missing testid lists

### Step 4: Generate Page Objects

- Do: Create TypeScript Page Object classes for each page
- How: Use the selector inventory to generate Page Objects:
  ```
  Read @GenDD-Flow/templates/testing-standards.md
  Read @TargetRepo/.cursor/testing.md

  Generate TypeScript Page Objects for all discovered pages:
  - One Page Object per logical page/component
  - MUST use data-testid selectors only
  - Include helper methods for common actions
  - Add JSDoc comments for clarity

  Example structure:
  // pages/checkout.page.ts
  import { Page, Locator, expect } from '@playwright/test';

  export class CheckoutPage {
    readonly page: Page;
    readonly cardNumberInput: Locator;
    readonly submitButton: Locator;
    readonly errorMessage: Locator;

    constructor(page: Page) {
      this.page = page;
      this.cardNumberInput = page.locator('[data-testid="card-number"]');
      this.submitButton = page.locator('[data-testid="submit-payment"]');
      this.errorMessage = page.locator('[data-testid="error-message"]');
    }

    async fillPaymentForm(card: string, expiry: string, cvv: string) { ... }
    async submitPayment() { await this.submitButton.click(); }
    async expectSuccess() { await expect(this.successMessage).toBeVisible(); }
  }
  ```
- Expect: Page Object files in `e2e/pages/*.page.ts`

### Step 5: Generate E2E test suite

- Do: Create the full Playwright test suite
- How: Generate tests across all categories:
  ```
  Generate Playwright test suite based on discovered elements:

  1. Happy Path Tests - Complete successful user journeys
  2. Validation Tests - Empty fields, invalid inputs, boundary conditions
  3. Error Handling Tests - API errors (mock with route interception), network failures
  4. Accessibility Tests - Keyboard navigation, focus management, ARIA attributes
  5. Responsive Design Tests - Verify layout at mobile (375px), tablet (768px), and desktop (1280px+)
  6. Sensitive Field Masking Tests - PIN and card number inputs are masked (type="password" or equivalent), values never appear in cleartext in the DOM
  7. Usability Tests - Error messages are actionable, form flows are intuitive, success states are clear

  MUST use ONLY [data-testid] selectors.
  MUST use waitForSelector/expect assertions, NOT waitForTimeout.
  Each test MUST be independent (beforeEach setup).
  ```
- Expect: Complete test files with all scenarios

### Step 6: Generate test data fixtures

- Do: Create structured test data for all scenarios
- How: Based on discovered forms and validation rules, generate test data JSON
- Expect: Test data fixtures in `e2e/fixtures/test-data.json`

## Expected Output

```
@TargetRepo/e2e/
├── pages/
│   ├── login.page.ts
│   ├── checkout.page.ts
│   └── account.page.ts
├── tests/
│   ├── happy-path.spec.ts
│   ├── validation.spec.ts
│   ├── error-handling.spec.ts
│   ├── responsive.spec.ts
│   ├── sensitive-masking.spec.ts
│   └── accessibility.spec.ts
└── fixtures/
    └── test-data.json
```

**Save to:** `@TargetRepo/e2e/`

## What's Next

- [ ] Add E2E tests to nightly CI/CD pipeline
- [ ] Review generated tests with QA team for additional scenarios

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Testing Standards | `templates/testing-standards.md` | MUST/SHOULD/MAY rules for tests |
| Context Pack Template | `templates/context-pack.md` (testing.md section) | Universal naming, AAA, scenarios |
| Integration Testing Workflow | `workflows/automate-integration-testing.md` | Run tests in CI/CD |
