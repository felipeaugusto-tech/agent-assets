# Requirements Enhancement Template (Shift-Left Story Quality)

## Context for AI
Transform vague, high-level product requirements into detailed, engineer-ready acceptance criteria with edge cases, integration impacts, and test scenarios. **Use AI ahead of development and QA** to strengthen requirements, explicitly surface edge cases, and reduce ambiguity.

## Alignment with AI-in-SDLC Initiative
This template supports the **Story Quality (shift-left)** framework—one of four initial high-impact areas.

## Tooling Approach
**Cursor + repo-based Markdown context only.** No RAG, vector databases, embeddings, or additional platforms.

## Use Case
When product management provides 2-3 sentence feature requests that lack technical detail, use this template to expand them into comprehensive user stories with testable acceptance criteria.

---

## Acceptance Criteria Rules

### Rule 1: Observable and Testable (MUST)

ACs must describe **observable behavior**, not intent. QA must be able to verify both UI and API.

| ❌ Intent (not testable) | ✅ Behavior (testable) |
|--------------------------|------------------------|
| "Only users with AdminWrite can create orders" | "Users WITHOUT AdminWrite: (1) Cannot see 'Create Order' button, (2) Receive 403 when calling POST /api/orders" |
| "The system prevents duplicate orders" | "When user submits order for patient with pending order: (1) Submission is blocked, (2) Error displays: 'Order already in progress for this patient'" |
| "Data is secured" | "Unauthorized users receive 401, audit log records access attempt with timestamp and IP" |

### Rule 2: Outcomes, Not Solutions (MUST)

ACs describe **what the user experiences**, not how engineering implements it.

| ❌ Technical Solution | ✅ Observable Outcome |
|-----------------------|----------------------|
| "MRN locking prevents conflicts" | "When two users create orders for same patient simultaneously, only one succeeds; the other sees 'Order in progress' error" |
| "Use Redis for caching" | "Page loads in under 200ms on subsequent views" |
| "Implement optimistic locking" | "User sees 'Data changed by another user, please refresh' when saving stale data" |

### Rule 3: Scope Control (MUST)

Separate in-scope work from follow-up stories to keep estimates accurate.

**Format:**
```
## In This Story (MUST complete for acceptance):
- [ ] Core functionality
- [ ] Error handling for common cases
- [ ] Basic validation

## Follow-Up Stories (create separate tickets):
- [ ] Advanced edge case (describe)
- [ ] Inline creation of related entities
- [ ] Bulk operations
```

---

## Generation Prompt
```
I have a product requirement that needs to be expanded into detailed acceptance criteria for engineering.

Original Requirement:
{PASTE_PRODUCT_REQUIREMENT}

Context:
- Product: {PRODUCT_NAME}
- User Persona: {TARGET_USER} (e.g., school administrator, donor, payment processor)
- Existing Integrations: {LIST_INTEGRATIONS} (e.g., WorldPay, First Data, SSO providers)
- Multi-tenant: {YES/NO}

Please generate:

1. **User Story** (Given-When-Then format)
   - Clear actor, action, and outcome

2. **Detailed Acceptance Criteria** (Gherkin format)
   - GIVEN preconditions
   - WHEN action occurs
   - THEN expected outcomes (OBSERVABLE behavior, not intent)
   - AND additional conditions
   
   **Important**: Each AC must be:
   - Observable (QA can see/verify it)
   - Testable (both UI and API verification possible)
   - Outcome-focused (not describing technical implementation)

3. **Scope Control**
   - **In This Story**: What MUST be completed
   - **Follow-Up Stories**: Edge cases that expand scope significantly

4. **Edge Cases** to consider (in-scope only):
   - Null/empty input scenarios
   - Boundary conditions
   - Multi-tenant isolation issues
   - Integration failure scenarios
   - Accessibility requirements (WCAG 2.1 AA)

5. **Integration Impacts**
   - Which systems/services are affected?
   - Does this change API contracts?
   - Are there downstream dependencies?

6. **Non-Functional Requirements (NFRs)**
   - Performance targets (response time, throughput)
   - Security requirements
   - Accessibility standards
   - Compliance requirements (PCI, data privacy)

7. **Test Scenarios** (3-5 key tests)
   - Happy path
   - Error conditions
   - Edge cases (in-scope only)

8. **Technical Questions** for clarification
   - List any ambiguities that need product team input

Output in a format ready to paste into Jira.
```

---

## Example Input
```
Add ability for users to save payment methods for future use.
```

## Example Output Structure
```markdown
# User Story
AS A school administrator
WHEN I make a payment for student fees
I WANT TO save my payment method securely
SO THAT I can make future payments faster without re-entering card details

---

# Scope Control

## In This Story (MUST complete):
- [ ] Checkbox to opt-in to saving payment method
- [ ] Store tokenized payment method in vault
- [ ] Display saved methods on return visit
- [ ] Select saved method to auto-populate
- [ ] Basic error handling (vault unavailable)

## Follow-Up Stories (create separate tickets):
- [ ] Delete saved payment methods
- [ ] Edit expiration date on saved methods
- [ ] Set default payment method
- [ ] Maximum saved methods limit enforcement

---

# Acceptance Criteria

## AC1: Opt-in to Save Payment Method
GIVEN I am logged in as a school administrator
AND I am on the payment checkout page
WHEN I check "Save payment method for future use"
AND I complete the payment successfully
THEN:
- The checkbox selection is preserved during payment
- My payment method token is stored in the vault
- I see confirmation: "Payment method saved for future use"
- The saved method appears in "My Account > Payment Methods"

**Verification:**
- UI: Checkbox visible and functional
- API: POST /api/vault/payment-methods returns 201
- Database: Token stored with user association

## AC2: Use Saved Payment Method
GIVEN I have previously saved payment methods
WHEN I return to make another payment
THEN:
- I see a list of my saved payment methods (last 4 digits, card type, expiry)
- I can select one to auto-populate the payment form
- I can still choose to enter a new payment method

**Verification:**
- UI: Saved methods dropdown visible
- API: GET /api/vault/payment-methods returns user's methods only
- Multi-tenant: User A cannot see User B's methods (verified via API)

## AC3: Vault Service Unavailable
GIVEN the vault service is temporarily unavailable
WHEN I attempt to save a payment method
THEN:
- The payment still processes successfully
- I see warning: "Unable to save payment method. Please try again later."
- No error prevents payment completion

**Verification:**
- UI: Warning message displayed (not blocking error)
- API: Payment endpoint returns 200, vault error logged

---

# Edge Cases (In-Scope)

| Scenario | Expected Behavior |
|----------|-------------------|
| Payment fails after opt-in | Payment method NOT saved; user sees payment error only |
| Vault timeout (>5s) | Payment proceeds; save skipped with warning |
| Duplicate card | "This card is already saved" message; no duplicate created |
| Multi-tenant isolation | API returns 404 for other tenant's payment methods |

---

# Integration Impacts

| Service | Change | Type |
|---------|--------|------|
| Vault Service | New endpoint: POST/GET /api/vault/payment-methods | New |
| Payment Gateway | Add tokenization parameter | Modified |
| User Service | Link vault IDs to user profile | Modified |
| Audit Service | Log vault operations | Modified |

---

# Non-Functional Requirements

| Category | Requirement | Verification |
|----------|-------------|--------------|
| Performance | Vault lookup < 200ms p95 | Load test |
| Security | PCI DSS Level 1 compliant | Audit |
| Security | Tokens only (no raw card data) | Code review |
| Accessibility | WCAG 2.1 AA | Automated + manual test |
| Audit | All vault access logged | Log review |

---

# Test Scenarios

| # | Scenario | Steps | Expected |
|---|----------|-------|----------|
| 1 | Happy path | Check save, complete payment, return | Saved method available |
| 2 | Vault down | Mock vault 503, complete payment | Payment succeeds, warning shown |
| 3 | Multi-tenant | User A saves card, User B queries | User B sees only their cards |
| 4 | Duplicate | Save same card twice | Second attempt shows "already saved" |
| 5 | Accessibility | Keyboard-only flow | All interactions work |

---

# Technical Questions

1. **Retention**: How long to keep saved methods? (Suggest: 2 years inactive)
2. **Limit**: Maximum saved methods per user? (Suggest: 5)
3. **Gateways**: Which payment gateways support tokenization?
4. **Compliance**: Any state-specific data retention laws?
```

---

## Quality Checklist

### Acceptance Criteria
- [ ] Each AC is **observable** (QA can verify via UI and API)
- [ ] Each AC describes **outcomes**, not technical solutions
- [ ] Verification method specified for each AC
- [ ] Multi-tenant isolation explicitly tested

### Scope Control
- [ ] Clear separation of in-scope vs follow-up work
- [ ] Follow-up items are separate ticket candidates
- [ ] Story is estimable (not open-ended)

### Standard Checks
- [ ] User story follows Given-When-Then format
- [ ] Acceptance criteria use Gherkin syntax
- [ ] At least 5 edge cases identified
- [ ] Integration impacts documented
- [ ] NFRs include performance, security, accessibility
- [ ] Test scenarios cover happy path and failures
- [ ] Technical questions list ambiguities

---

## Context Engineering Tips
For better results, provide:
- **Product context**: Which {ORGANIZATION} product (e.g., {PRODUCT_NAME})
- **Integration list**: Existing third-party systems
- **Tech stack**: .NET, Python, React, Angular
- **Compliance needs**: PCI scope, data privacy requirements
- **User personas**: School admin, donor, payment processor, etc.

---

## Follow-Up Workflows
After generating enhanced requirements:
1. Use `workflows/enhance-acceptance-criteria.md` for product team review
2. Use `workflows/identify-test-gaps.md` to ensure test coverage is planned
3. Use `workflows/generate-unit-tests.md` to create test suite from criteria
4. Use `workflows/generate-architecture-diagrams.md` if architectural context is needed
