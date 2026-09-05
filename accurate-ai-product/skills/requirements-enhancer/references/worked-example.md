# Worked Example

One requirement, expanded end to end. Use this to calibrate depth and the shape of
each section — not as a template to copy content from. The specifics here are
illustrative; a real run grounds them in the repo Context Pack.

---

## Input

> Add ability for users to save payment methods for future use.

Context supplied by Step 0: payments product, persona is a school administrator,
existing integrations are a tokenization vault and a payment gateway, system is
multi-tenant, PCI scope applies.

---

## Output

# Save payment method for future use

## User Story
AS A school administrator
WHEN I make a payment for student fees
I WANT TO save my payment method securely
SO THAT future payments do not require re-entering card details

## Scope Control

### In this story (required for acceptance)
- [ ] Opt-in checkbox on the checkout page
- [ ] Tokenized payment method stored in the vault
- [ ] Saved methods listed on return visit
- [ ] Selecting a saved method populates the payment form
- [ ] Graceful handling when the vault is unavailable

### Follow-up stories (file separately)
- [ ] Delete a saved payment method
- [ ] Update expiration date on a saved method
- [ ] Set a default payment method
- [ ] Enforce a maximum number of saved methods per user

## Acceptance Criteria

### AC1: Opt in to saving a payment method
GIVEN I am signed in as a school administrator
AND I am on the payment checkout page
WHEN I select "Save payment method for future use"
AND the payment completes successfully
THEN:
- The selection persists through the payment flow
- A payment method token is stored in the vault, associated with my user
- I see: "Payment method saved for future use"
- The method appears under My Account → Payment Methods

**Verification:**
- UI: checkbox present, selectable, state survives submission
- API: POST /api/vault/payment-methods returns 201
- Data: token persisted with user association; no raw card data stored

### AC2: Pay with a saved method
GIVEN I have at least one saved payment method
WHEN I return to make another payment
THEN:
- I see my saved methods listed by card type, last four digits, and expiry
- Selecting one populates the payment form
- I can still enter a new payment method instead

**Verification:**
- UI: saved-method selector visible with the three display fields
- API: GET /api/vault/payment-methods returns only the requesting user's methods
- Data: a request scoped to another tenant's method returns 404, not 403

### AC3: Vault unavailable
GIVEN the vault service is unavailable
WHEN I attempt to save a payment method during checkout
THEN:
- The payment still completes successfully
- I see: "Unable to save payment method. Please try again later."
- No blocking error interrupts payment completion

**Verification:**
- UI: message renders as a non-blocking warning
- API: payment endpoint returns 200; vault failure is logged with correlation ID

*Note the decision made explicit in AC3: the primary flow degrades rather than
failing. That is the single most valuable line in this story.*

## Edge Cases (in scope)

| Scenario | Expected behavior |
|---|---|
| Payment fails after opt-in | Method not saved; user sees the payment error only |
| Vault times out (>5s) | Payment proceeds; save skipped with the AC3 warning |
| Card already saved | "This card is already saved"; no duplicate created |
| Cross-tenant access attempt | 404 for another tenant's method |
| Expired card selected | Blocked at selection with "This card has expired" |

## Integration Impacts

| Service | Change | Type | Contract change? |
|---|---|---|---|
| Vault service | POST/GET /api/vault/payment-methods | New | Yes — new endpoints |
| Payment gateway | Tokenization parameter added | Modified | Yes — request shape |
| User service | Vault ID linked to user profile | Modified | No |
| Audit service | Vault operations logged | Modified | No |

## Non-Functional Requirements

| Category | Requirement | Verification |
|---|---|---|
| Performance | Vault lookup under 200ms p95 | Load test |
| Security | Tokens only; no raw card data persisted or logged | Code review + log audit |
| Compliance | PCI DSS scope maintained | Compliance review |
| Accessibility | WCAG 2.1 AA | Automated scan + keyboard-only pass |
| Auditability | All vault access logged with actor and timestamp | Log review |

## Test Scenarios

| # | Scenario | Steps | Expected |
|---|---|---|---|
| 1 | Happy path | Opt in, pay, return to checkout | Saved method available and selectable |
| 2 | Vault down | Mock vault 503, complete payment | Payment succeeds, warning shown |
| 3 | Tenant isolation | User A saves, User B requests it | 404 for User B |
| 4 | Duplicate card | Save the same card twice | "This card is already saved" |
| 5 | Keyboard only | Complete the flow without a mouse | All controls reachable and operable |

## Assumptions

| # | Assumption | Basis | Confirm with |
|---|---|---|---|
| A1 | Retention of 2 years after last use | Common default; not specified | Product |
| A2 | Vault timeout threshold of 5s | Matches gateway timeout in architecture.md | Engineering |
| A3 | Cross-tenant reads return 404, not 403 | Avoids existence disclosure | Security |

## Open Questions

1. **Retention**: How long should saved methods persist when unused? (recommendation: 2 years, per A1)
2. **Limit**: Maximum saved methods per user? (recommendation: 5, enforced in a follow-up story)
3. **Gateway coverage**: Which configured gateways support tokenization? Behavior on ones that do not is undefined.
4. **Jurisdiction**: Any state-level retention constraints that override A1?
