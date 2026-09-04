# Worked Example — Meeting Notes to Story Set

A compressed end-to-end run at **Solid** depth. Use it to calibrate section
shape and depth, not to copy domain content.

## Contents

- [The source](#the-source)
- [Step 2 — Triage](#step-2--triage)
- [Step 3 — Requirement inventory](#step-3--requirement-inventory)
- [Step 4 — Decomposition rationale](#step-4--decomposition-rationale)
- [Step 5 — Stories](#step-5--stories)
- [Step 7 — Coverage map, parking lot, open questions](#step-7--coverage-map-parking-lot-open-questions)
- [What this example demonstrates](#what-this-example-demonstrates)

---

## The source

> **Checkout working session — 12 Mar, notes by Ana**
>
> Priya (Product): biggest drop-off is people re-entering card details. We
> agreed last week we're doing saved payment methods this quarter.
>
> Dan (Eng): fine, but card data can't hit our servers — we tokenize through
> the PSP. Non-negotiable, PCI scope.
>
> Priya: right. Members should be able to save a card at checkout and pick it
> next time.
>
> Dan: they'll want to delete them too. And what happens when a saved card
> expires?
>
> Priya: good question, I don't think we've decided. Maybe we prompt at
> checkout?
>
> Marco (Design): we could also let them nickname cards, "personal" vs "work".
>
> Priya: park that, phase two.
>
> Dan: how many cards can someone save?
>
> Priya: no strong view. Five?
>
> Dan: also — refunds against a deleted card. That's a real problem.
>
> Priya: let's take that offline with Finance.
>
> Ana: action — Dan to confirm PSP tokenization API supports listing stored
> cards.

## Step 2 — Triage

| Statement | Bucket | Why |
|---|---|---|
| Saved payment methods this quarter | Decision | "We agreed last week" |
| Card data can't hit our servers, PSP tokenization | Constraint | Stated non-negotiable, PCI scope |
| Save a card at checkout | Requirement | Stated, uncontested |
| Pick a saved card next time | Requirement | Stated, uncontested |
| Delete saved cards | Requirement | Raised by Dan, Priya did not dispute |
| Expired card behavior | Question | Priya: "I don't think we've decided" |
| Nickname cards | Proposal | Explicitly parked to phase two |
| Max five cards | Requirement (Low confidence) | "No strong view. Five?" — a floated default |
| Refunds against a deleted card | Question | Explicitly taken offline |
| Confirm PSP listing API | Context / dependency | An action item, not a story |
| Drop-off is the motivation | Context | Rationale — informs "so that," is not a story |

Note the two judgment calls. *Delete saved cards* becomes a requirement because
it was raised and went unchallenged in a working session with the decision
owner present. *Max five cards* becomes a Low-confidence requirement, not a
parked proposal, because Priya answered the question herself — but the question
mark makes it an assumption to confirm rather than a settled number.

## Step 3 — Requirement inventory

| # | Requirement | Source anchor | Type | Confidence |
|---|---|---|---|---|
| R1 | Members can save a payment method during checkout | Priya, ¶3 | Requirement | High |
| R2 | Members can select a saved method at checkout | Priya, ¶3 | Requirement | High |
| R3 | Members can delete a saved method | Dan, ¶4 | Requirement | Medium |
| R4 | Card data is tokenized by the PSP; PAN never reaches our servers | Dan, ¶2 | Constraint | High |
| R5 | Maximum five saved methods per member | Priya, ¶8 | Requirement | Low |
| R6 | Behavior when a saved card expires | Priya, ¶5 | Question | — |
| R7 | Refund against a deleted card | Dan/Priya, ¶10 | Question | — |
| R8 | Card nicknames | Marco, ¶6 | Proposal | Parked |

## Step 4 — Decomposition rationale

R1, R2, and R3 are the same feature but split cleanly by **CRUD lifecycle** —
each delivers value alone and each has distinct failure behavior. R4 is a
constraint, so it becomes an NFR on S1 rather than a story of its own: nobody
demos "we tokenize." R5 is a rule inside S1, expressed as an AC and flagged as
an assumption.

Three stories, not one. A single "manage saved payment methods" story would
need eleven-plus ACs and could not be demoed in one sitting.

## Step 5 — Stories

### S1: Save a payment method at checkout

**As a** returning member
**I want** to save the card I'm paying with
**So that** I don't re-enter it on my next order

**Traces to:** R1, R4, R5

#### Acceptance Criteria

```gherkin
Background:
  Given a signed-in member is on the checkout payment step

Scenario: Member opts to save a new card
   When the member enters valid card details and chooses to save the card
    And completes the purchase
   Then the purchase completes
    And the card appears in their saved payment methods, shown as brand plus last four digits
    And no full card number is stored in our systems

Scenario: Member does not opt to save
   When the member enters valid card details without choosing to save the card
    And completes the purchase
   Then the purchase completes
    And no payment method is added to their saved methods

Scenario: Tokenization fails at the payment provider
  Given the payment provider is unavailable
   When the member enters valid card details and chooses to save the card
   Then the purchase is not completed
    And the member sees "We couldn't process that card. Please try again."
    And no payment method is saved

Scenario: Member is already at the saved-card limit
  Given the member has five saved payment methods
   When the member reaches the payment step
   Then the option to save a card is unavailable
    And the member sees "You've saved the maximum of 5 cards. Remove one to save another."
```

**Verification:** UI: saved card visible in account after purchase · API: `POST /payment-methods` returns 201 with a token reference and no PAN · Data: stored record contains token, brand, last four, expiry — never the full number

#### Edge Cases

| Scenario | Expected behavior |
|---|---|
| Card already saved by this member | Purchase completes; no duplicate is created |
| Member's session expires between entry and submit | Purchase fails; member is re-authenticated; nothing is saved |
| Purchase declines after tokenization succeeds | No payment method is saved |
| Two checkouts submitted concurrently by the same member | At most one save per card; the five-card limit is not exceeded |
| Card expiring next month | Save succeeds; expiry stored for downstream handling (see Open Question 1) |

#### Non-Functional Requirements

| Category | Requirement | Verification |
|---|---|---|
| Compliance | PCI DSS SAQ-A: PAN never transits or persists on our infrastructure | Provider-hosted fields; log and payload review |
| Security | Stored token is unusable outside our merchant account | Provider configuration review |
| Accessibility | Save-card control meets WCAG 2.1 AA — labeled, keyboard reachable | Automated scan plus keyboard walkthrough |
| Performance | Tokenization adds under 500 ms to checkout submit at p95 | Load test against provider sandbox |

*Latency figure is an assumption — see Assumptions.*

#### Assumptions

| # | Assumption | Basis | Confirm with |
|---|---|---|---|
| A1 | Five saved methods is the limit | Priya floated "five?" without deciding | Priya |
| A2 | 500 ms p95 tokenization budget | No budget in the source or Context Pack | Dan |

---

### S2: Pay with a saved payment method

**As a** returning member
**I want** to pick a card I've already saved
**So that** I can check out without typing card details

**Traces to:** R2

#### Acceptance Criteria

```gherkin
Background:
  Given a signed-in member with two saved payment methods is at the checkout payment step

Scenario: Member pays with a saved card
   When the member selects a saved card and confirms payment
   Then the purchase completes using that card
    And the member is not asked to re-enter the card number

Scenario: Saved card is declined
  Given the selected card will be declined by the provider
   When the member confirms payment
   Then the purchase does not complete
    And the member sees "That card was declined. Try another card or payment method."
    And the member remains on the payment step with their cart intact

Scenario Outline: Additional authentication is required
  Given the selected card requires <challenge>
   When the member confirms payment
   Then the member is taken through the provider's authentication step
    And on success the purchase completes

  Examples:
    | challenge |
    | 3-D Secure |
    | one-time passcode |

Scenario: Member has no saved cards
  Given the member has no saved payment methods
   When the member reaches the payment step
   Then the new-card form is shown by default
```

**Verification:** UI: saved cards listed masked; selection persists through confirm · API: `POST /orders` accepts a payment-method reference, not a PAN · Data: order records which saved method was used

#### Edge Cases

| Scenario | Expected behavior |
|---|---|
| Card deleted in another tab before confirm | Purchase fails with a clear message; member is prompted to choose another method |
| Saved card has expired | Selection is blocked with a message; see Open Question 1 |
| Provider times out mid-authorization | Order is not double-charged; member sees a retry path |
| Member has the maximum five saved cards | All five are selectable |

#### Non-Functional Requirements

| Category | Requirement | Verification |
|---|---|---|
| Security | A member can only see and use their own saved methods | Authorization test using another member's method reference |
| Accessibility | Card selection is a labeled, keyboard-navigable group — WCAG 2.1 AA | Automated scan plus keyboard walkthrough |
| Performance | Saved methods render within 300 ms of reaching the payment step | Front-end timing at p95 |

---

### S3: Delete a saved payment method

**As a** member
**I want** to remove a card I no longer use
**So that** it isn't offered at checkout

**Traces to:** R3

#### Acceptance Criteria

```gherkin
Background:
  Given a signed-in member with two saved payment methods is in account settings

Scenario: Member deletes a saved card
   When the member deletes one card and confirms
   Then that card no longer appears in their saved methods
    And the provider token for that card is revoked
    And the remaining card is unaffected

Scenario: Member cancels the deletion
   When the member starts to delete a card and cancels
   Then both cards remain saved

Scenario: Deleting the last saved card
  Given the member has one saved payment method
   When the member deletes it and confirms
   Then they have no saved methods
    And the account page shows "You have no saved payment methods."
```

**Verification:** UI: card removed from the list without a page reload · API: `DELETE /payment-methods/{id}` returns 204; a subsequent `GET` omits it · Data: token revoked at the provider

#### Edge Cases

| Scenario | Expected behavior |
|---|---|
| Card deleted while an order using it is mid-authorization | That order completes; the card is removed afterward |
| Deleting a card attached to an unfulfilled order | Deletion succeeds; refund path is unresolved — see Open Question 2 |
| Same card deleted from two sessions | Second deletion is a no-op, not an error |
| Delete requested for another member's method | Request is rejected as not found |

#### Non-Functional Requirements

| Category | Requirement | Verification |
|---|---|---|
| Security | Deletion is authorized against the owning member | Cross-member authorization test |
| Audit | Deletion is recorded with member, method reference, and timestamp | Audit-log inspection |
| Data retention | Token revoked at the provider; no PAN existed to delete | Provider API confirmation |

## Step 7 — Coverage map, parking lot, open questions

### Coverage Map

| # | Requirement | Source anchor | Disposition |
|---|---|---|---|
| R1 | Save a payment method at checkout | Priya, ¶3 | S1 |
| R2 | Select a saved method at checkout | Priya, ¶3 | S2 |
| R3 | Delete a saved method | Dan, ¶4 | S3 |
| R4 | PSP tokenization; PAN never on our servers | Dan, ¶2 | NFR on S1, S2, S3 |
| R5 | Maximum five saved methods | Priya, ¶8 | AC in S1 — Assumption A1 |
| R6 | Expired card behavior | Priya, ¶5 | Open Question 1 — blocks an S2 edge case |
| R7 | Refund against a deleted card | Dan, ¶10 | Open Question 2 — blocks an S3 edge case |
| R8 | Card nicknames | Marco, ¶6 | Parked — phase two |

### Parking Lot

| # | Item | Why parked | Who raised it |
|---|---|---|---|
| R8 | Nickname saved cards | Explicitly deferred to phase two | Marco |

### Open Questions

1. **Expired saved cards** — what happens when a member's saved card expires
   before checkout? Blocks: S2 edge case, S1 storage behavior. Ask: Priya.
   (Recommendation: block selection with a prompt to update, and notify 30 days
   ahead — cheapest option that avoids a failed authorization.)
2. **Refund against a deleted card** — where does a refund go when the original
   method has been deleted? Blocks: S3 edge case, and possibly a fourth story.
   Ask: Priya with Finance — already taken offline in the session.
3. **Five-card limit** — confirm or replace. Blocks: S1 AC and error copy. Ask: Priya.
4. **PSP stored-card listing** — Dan's action item. If the provider cannot list
   stored cards, S2 needs a different approach. Ask: Dan.

## What this example demonstrates

- A **proposal was parked, not written as a story** (nicknames), and a
  **hedged answer became a flagged assumption, not a fact** (five cards).
- **Two unresolved items became Open Questions with owners**, rather than
  stories that would have picked a winner silently.
- **A constraint became an NFR across three stories**, not a story of its own.
- **Gherkin stays declarative** — no clicking, no table names, exact user-facing
  copy where the wording is part of the behavior.
- **Every story has a failure scenario**, and every inventory item has a
  disposition. Nothing from the source went unaccounted for.
