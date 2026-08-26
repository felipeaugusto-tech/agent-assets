# Workflow: Enhance Acceptance Criteria (Shift-Left Story Quality)

## Context
Transform vague product requirements into detailed, engineer-ready acceptance criteria. This addresses the #1 bottleneck identified across teams: unclear requirements causing rework loops. **Use AI ahead of development and QA** to strengthen acceptance criteria, explicitly surface edge cases, and reduce ambiguity.

> **Reference:** This workflow aligns with {ORGANIZATION}'s **Story Templates** and **Definition of Ready** standards.

## Alignment with AI-in-SDLC Initiative
This workflow is one of four initial high-impact areas focused on early SDLC quality:
1. **Story Quality (shift-left)** ← This workflow
2. Test Gap Identification
3. Context Packs
4. C4 Architecture Diagrams

## {ORGANIZATION} Story Quality Standards

### Definition of Ready Alignment

This workflow helps stories meet Definition of Ready by ensuring:

| DoR Criterion | How This Workflow Helps |
|---------------|-------------------------|
| Clear problem statement | Extracts and clarifies from raw requirements |
| ACs in dedicated field | Generates Gherkin-format ACs for AC field |
| ACs describe expected behavior | Uses Given-When-Then, not implementation steps |
| Scope boundaries clear | Explicitly asks for in/out of scope |
| Integration impact identified | Surfaces integration questions |
| Security review need identified | Flags PCI/PII/Auth concerns |
| Environment/data dependencies | Calls out test data needs |
| Unknowns documented | Generates technical questions for clarification |

### Story Template Alignment

Generated output follows {ORGANIZATION} Story Template structure:

1. **User Story Statement**: As a [user/role], I want [capability], So that [business value]
2. **Context & References**: Links, related epic, source of truth
3. **Acceptance Criteria**: Gherkin format in dedicated field
4. **Integration & Risk Flags**: External integration? Security review?
5. **Environment & Test Data**: Dependencies and prerequisites
6. **Testing & Automation Notes**: Planned coverage
7. **Release Notes**: User-visible behavior summary

### Common Anti-Patterns This Workflow Prevents

| Anti-Pattern | Problem | How This Workflow Fixes It |
|--------------|---------|---------------------------|
| ACs in Description | Not visible, not tracked | Generates for dedicated AC field |
| "See STR" patterns | Expected behavior undefined | Explicitly documents expected behavior |
| Missing edge cases | QA discovers via bugs | Generates 5+ edge cases |
| Implicit integration | Late discovery | Surfaces integration questions |
| Vague scope | Scope creep | Asks for in/out of scope |

## Tooling Approach
**Cursor + repo-based Markdown context only.** No RAG, vector databases, embeddings, or additional platforms.

## Prerequisites
- Product requirement document or feature request
- Understanding of which {ORGANIZATION} product this affects (e.g., {PRODUCT_NAME})
- List of existing integrations for that product
- Access to Cursor or similar AI IDE

## When to Use This Workflow
- Product manager provides high-level feature request (2-3 sentences)
- Requirements lack technical detail or edge cases
- Before sprint planning or backlog refinement
- When creating Jira tickets for development team
- When preparing for technical design discussions
- **After Brownfield Analysis** - Use core flows from `workflows/brownfield-repository-analysis.md` to understand existing system before adding features

## Cursor Steps

### 1. Gather Context

Before opening Cursor, collect:
- Original product requirement (email, doc, verbal request)
- Target product (e.g., "{PRODUCT_NAME}")
- User persona (e.g., "school administrator", "donor")
- List of integrations that might be affected
- Whether multi-tenant considerations apply

### 2. Open Cursor Chat (Cmd+L / Ctrl+L)

Paste the following prompt:

```
I have a product requirement that needs to be expanded into detailed acceptance criteria for engineering.

Original Requirement:
"""
{PASTE THE PRODUCT REQUIREMENT HERE}
"""

Context:
- Product: {PRODUCT_NAME}
- User Persona: {TARGET_USER} (e.g., school administrator, donor, payment processor)
- Existing Integrations: {LIST_INTEGRATIONS} (e.g., WorldPay, First Data, Northstar Schools)
- Multi-tenant: {YES/NO}
- Tech Stack: {.NET | Python | React | Angular}

Please generate:

1. User Story (Given-When-Then format)
2. Detailed Acceptance Criteria (Gherkin format for automation)
3. Edge Cases (at least 5)
4. Integration Impacts (which systems affected?)
5. Non-Functional Requirements (performance, security, accessibility)
6. Test Scenarios (3-5 key tests)
7. Technical Questions for product team clarification

Format output as Jira-ready markdown.
```

### 3. Review Generated Output

AI will generate comprehensive requirements. Review for:

#### Check User Story
- [ ] Follows Given-When-Then format
- [ ] Clear actor identified
- [ ] Action and outcome specified
- [ ] Business value articulated

#### Check Acceptance Criteria
- [ ] Uses Gherkin syntax (GIVEN-WHEN-THEN-AND)
- [ ] Testable and unambiguous
- [ ] Covers happy path
- [ ] Includes error conditions
- [ ] Addresses edge cases

#### Check Edge Cases
- [ ] Multi-tenant isolation considered
- [ ] Null/empty input scenarios
- [ ] Integration failure scenarios
- [ ] Accessibility requirements
- [ ] Security/compliance impacts

### 4. Identify Missing Information

If AI generated technical questions, use Cursor to:

```
For each technical question you listed, provide:
1. Why this information is needed
2. What the development impact is if we make the wrong assumption
3. Suggested default/best practice if product team doesn't have an answer
```

### 5. Refine Edge Cases

If you spot missing edge cases, ask:

```
Review the acceptance criteria and edge cases. Are we missing any scenarios related to:
- Multi-tenant data isolation (School A seeing School B's data)
- Integration failures (what if WorldPay is down?)
- Expired credentials or tokens
- Rate limiting or throttling
- Concurrent user actions
- Browser/device compatibility
- Accessibility (keyboard-only, screen readers)
```

### 6. Add Technical Context

For {ORGANIZATION}-specific technical considerations:

```
Based on this requirement, identify:

1. Which {ORGANIZATION} services will need changes:
   - VaultService (payment storage)
   - PaymentGateway (transaction processing)
   - UserService (authentication/profile)
   - AuditService (logging)
   - ReportingService (analytics)

2. Database changes required:
   - New tables
   - Schema modifications
   - Migration complexity

3. API contract changes:
   - New endpoints
   - Modified endpoints
   - Versioning needed

4. PCI compliance considerations:
   - Does this touch card data?
   - Audit logging requirements
   - Encryption needs
```

### 7. Generate Test Scenarios

Use Cursor to create specific test cases:

```
Generate detailed test scenarios for each acceptance criterion in this format:

Test Case: {NAME}
Preconditions: {SETUP_REQUIRED}
Steps:
1. {ACTION_1}
2. {ACTION_2}
3. {ACTION_3}
Expected Result: {WHAT_SHOULD_HAPPEN}
Test Data: {SPECIFIC_DATA_TO_USE}

Include scenarios for:
- Happy path
- Invalid input
- Integration failure
- Multi-tenant isolation
- Accessibility
```

### 8. Create Jira-Ready Output

Format for easy copy-paste to Jira:

```
Take all the information we've generated and format it as a complete Jira ticket with these sections:

# User Story
{GIVEN-WHEN-THEN}

# Acceptance Criteria
{GHERKIN_FORMAT_CRITERIA}

# Edge Cases
{BULLET_LIST}

# Integration Impacts
{AFFECTED_SERVICES_AND_CHANGES}

# Non-Functional Requirements
- Performance: {TARGETS}
- Security: {REQUIREMENTS}
- Accessibility: {WCAG_STANDARDS}
- Compliance: {PCI_GDPR_ETC}

# Test Scenarios
{DETAILED_TEST_CASES}

# Technical Questions for Product Team
{QUESTIONS_NEEDING_ANSWERS}

# Estimated Complexity
{T_SHIRT_SIZE_OR_STORY_POINTS_ESTIMATE}

Use markdown formatting suitable for Jira.
```

### 9. Validate with Tech Lead

Before finalizing:

1. **Review with Tech Lead**: Share generated requirements
2. **Verify integration impacts**: Confirm affected services
3. **Validate edge cases**: Are we missing any?
4. **Check NFRs**: Are performance/security targets realistic?

### 10. Validate NFRs for Architecture (Before Solutioning)

Before proceeding to architecture/solutioning, validate each NFR:

```
Review the Non-Functional Requirements and validate they are architecture-ready:

| NFR | Target | Measurable? | Testable? | Architecture Impact |
|-----|--------|-------------|-----------|---------------------|
| Performance | [value] | ✅/❌ | [how to verify] | [what it drives] |
| Security | [requirement] | ✅/❌ | [how to verify] | [what it drives] |
| Availability | [uptime %] | ✅/❌ | [how to verify] | [what it drives] |
| Scalability | [users/load] | ✅/❌ | [how to verify] | [what it drives] |

For each NFR, identify:
1. Does it have a measurable target? (not "fast" but "<200ms p95")
2. How will it be verified? (load test, audit, code review)
3. What architecture decisions does it drive?
   - Performance → Caching, async processing, CDN
   - Security → Encryption, auth patterns, network isolation
   - Availability → Redundancy, failover, multi-region
   - Scalability → Horizontal scaling, service boundaries, queues
```

**Pass this NFR table to architecture workflows** to ensure diagrams reflect these constraints.

### 11. Clarify with Product Team

For any technical questions generated:

1. **Schedule quick sync** with product manager
2. **Walk through questions** one by one
3. **Update requirements** based on answers
4. **Re-run Cursor** if major changes needed

```
Update the acceptance criteria based on these answers from product team:

Question 1: {QUESTION}
Answer: {PRODUCT_RESPONSE}

Question 2: {QUESTION}
Answer: {PRODUCT_RESPONSE}

Regenerate the affected sections with this new information.
```

### 12. Create Jira Ticket

1. Copy enhanced requirements into new Jira ticket
2. Add labels: `ai-enhanced`, `{product-name}`, `{feature-type}`
3. Link related tickets (dependencies)
4. Assign appropriate epic
5. Set sprint (if ready) or backlog

### 13. Optional: Generate Architecture Draft

If this is a complex feature, use the enhanced requirements for architecture:

```
Based on these enhanced requirements, generate architecture that satisfies NFRs:

**NFR-Driven Architecture Decisions:**
| NFR | Target | Architecture Decision |
|-----|--------|----------------------|
| [from step 10 NFR table] | | |

Generate:
1. High-level architecture approach (justified by NFRs)
2. Service interaction diagram (Mermaid format)
3. Database schema changes needed
4. API endpoint definitions
5. Key technical decisions (linked to NFR constraints)

For each architecture decision, note which NFR it satisfies.
```

## Example: Save Payment Method Feature

### Initial Product Request
```
"Users should be able to save their payment methods for future use."
```

### After Running This Workflow

**Cursor Chat Sequence:**

**You:**
```
I have a product requirement that needs to be expanded into detailed acceptance criteria.

Original Requirement:
"Users should be able to save their payment methods for future use."

Context:
- Product: {PRODUCT_NAME}
- User Persona: School administrator
- Existing Integrations: WorldPay, First Data, 24 school management systems
- Multi-tenant: YES (each school is a tenant)
- Tech Stack: React frontend, .NET Core backend

Please generate:
1. User Story (Given-When-Then format)
2. Detailed Acceptance Criteria (Gherkin format)
3. Edge Cases (at least 5)
4. Integration Impacts
5. Non-Functional Requirements
6. Test Scenarios
7. Technical Questions

Format output as Jira-ready markdown.
```

**Cursor Response:**
```markdown
# User Story
AS A school administrator
WHEN I make a payment for student fees
I WANT TO save my payment method securely
SO THAT I can make future payments faster without re-entering card details

# Acceptance Criteria

## AC1: Opt-in to Save Payment Method
GIVEN I am logged in as a school administrator
AND I am on the payment checkout page
WHEN I check the "Save payment method for future use" checkbox
AND I complete the payment successfully
THEN my payment method is securely tokenized and stored
AND I see a confirmation message "Payment method saved"
AND the saved method appears in my account settings

## AC2: View Saved Payment Methods
GIVEN I have previously saved payment methods
WHEN I navigate to "My Account" > "Payment Methods"
THEN I see a list of my saved payment methods
AND each method shows: last 4 digits, card type, expiration date
AND I see options to: use for payment, delete, set as default

## AC3: Use Saved Payment Method
GIVEN I have saved payment methods
WHEN I return to make another payment
THEN I see my saved payment methods as payment options
AND I can select one to auto-populate payment form
AND I can still enter a new payment method if desired

# Edge Cases
1. **Payment fails after opt-in to save**: Should NOT save the payment method
2. **Card expires**: Display "Expired" badge, prompt user to update
3. **Vault service unavailable**: Gracefully degrade - allow payment but don't save, show warning
4. **Multi-tenant**: School A admin cannot see/access School B's saved payment methods
5. **Maximum saved methods**: Limit to 5 per user, prompt to delete if at limit
6. **Duplicate detection**: Don't save same card twice, show "Already saved"
7. **PCI compliance**: Never store raw card numbers, only tokens
8. **Accessibility**: Checkbox keyboard-accessible, screen reader announces save confirmation

# Integration Impacts

## VaultService (NEW)
- Need new endpoint: POST /api/vault/payment-methods
- Stores encrypted payment tokens
- Returns vault ID for retrieval

## PaymentGateway (Modified)
- Tokenization must happen before save
- Add parameter: `saveForFutureUse: boolean`
- Return token ID in response

## UserService (Modified)
- Link vault IDs to user profile
- New table: UserPaymentMethods
- Fields: UserId, VaultId, IsDefault, CreatedAt, ExpiresAt

## AuditService (Modified)
- Log all vault operations
- Required for PCI compliance
- Fields: UserId, Action (save/delete/use), Timestamp, SchoolId

# Non-Functional Requirements

## Performance
- Vault lookup: <200ms p95
- Token creation: <500ms
- Page load with saved methods: <1s

## Security
- PCI DSS Level 1 compliance required
- All card data tokenized (never stored)
- Encryption at rest: AES-256
- TLS 1.2+ in transit
- Audit all vault operations

## Accessibility
- WCAG 2.1 AA compliant
- Keyboard navigation functional
- Screen reader tested
- Focus management proper

## Scalability
- Support 10,000 users with saved methods
- Handle 1,000 concurrent save operations

# Test Scenarios

## Test 1: Happy Path - Save and Reuse
Preconditions: User logged in, has not saved any payment methods
Steps:
1. Navigate to checkout
2. Enter card: 4111111111111111, exp 12/26, cvv 123
3. Check "Save payment method"
4. Complete payment
5. Verify success message
6. Navigate to "My Account" > "Payment Methods"
7. Verify card ending in 1111 is listed
8. Make another payment
9. Select saved card
10. Complete payment
Expected: Both payments successful, second payment faster
Test Data: Card 4111111111111111 (test card)

## Test 2: Vault Service Down
Preconditions: Vault service unavailable
Steps:
1. Navigate to checkout
2. Enter card details
3. Check "Save payment method"
4. Complete payment
Expected: Payment succeeds, warning shown "Unable to save payment method, please try again later"
Test Data: Mock vault service to return 503

## Test 3: Multi-Tenant Isolation
Preconditions: Two users from different schools
Steps:
1. User A (School 1) saves card ending in 1111
2. User B (School 2) saves card ending in 2222
3. User A views saved methods
Expected: User A sees only card ending in 1111
Test Data: Users from different tenantIds

## Test 4: Expired Card Handling
Preconditions: User has saved card expiring this month
Steps:
1. Navigate to "Payment Methods"
2. Verify card marked as "Expired"
3. Attempt to use for payment
Expected: Error message "Card expired, please update or use different method"
Test Data: Card with expiration date in past

## Test 5: Accessibility - Keyboard Only
Preconditions: User using keyboard only (no mouse)
Steps:
1. Tab to "Save payment method" checkbox
2. Press Space to check
3. Tab through form, fill with keyboard
4. Press Enter to submit
5. Tab to "Payment Methods" link in account
6. Press Enter to navigate
7. Tab to saved card, press Enter to select
Expected: All interactions work via keyboard
Test Data: Standard test card

# Technical Questions for Product Team

1. **Retention Period**: How long should we keep saved payment methods? Forever or expire after X months of inactivity?
   - Impact: Storage costs, PCI scope
   - Suggestion: 2 years of inactivity, then auto-delete with email warning

2. **Maximum Saved Methods**: Should we limit how many methods a user can save?
   - Impact: Storage, UI complexity
   - Suggestion: 5 methods max (industry standard)

3. **Delete Confirmation**: Should users confirm before deleting a saved method?
   - Impact: UX friction vs. accidental deletion
   - Suggestion: Yes, confirm with modal

4. **Default Payment Method**: Can users set a default? Auto-selected at checkout?
   - Impact: UX convenience vs. accidental charges
   - Suggestion: Yes for default, but require CVV re-entry for security

5. **Update Payment Method**: Can users update expiration date, or must delete and re-add?
   - Impact: User experience, vault API complexity
   - Suggestion: Allow update of expiration date only

# Estimated Complexity
**Story Points**: 8 (Large)
**Reasoning**:
- New VaultService integration (3 points)
- Database schema changes (2 points)
- UI components (2 points)
- Security/PCI compliance validation (1 point)

**Dependencies**:
- VaultService must be deployed first
- Database migration needed

**Timeline Estimate**: 2 sprints (4 weeks)
```

**Next Step - Tech Lead Review:**

You then share with tech lead, who suggests:
- "Add consideration for ACH bank accounts, not just cards"
- "VaultService already exists from CXP team, coordinate with David Hines"

**You refine with Cursor:**
```
Update the requirements to:
1. Include ACH bank accounts in addition to credit cards
2. Note that VaultService already exists (owned by David Hines, CXP team)
3. Update integration section to reflect coordination needed
```

**Final Output**: Comprehensive, Jira-ready ticket that took 15 minutes instead of 2-3 hours.

## Success Metrics
- **Time saved**: 70-80% reduction in requirements elaboration time
- **Rework reduced**: Fewer "missed scenarios" found in QA
- **Developer clarity**: Fewer clarification questions during refinement
- **Test coverage**: All edge cases documented upfront

## Tips for Best Results

### Provide Rich Context
The more context you give Cursor, the better:
- Product name and user persona
- Existing integrations
- Multi-tenant status
- Compliance requirements (PCI, GDPR, FERPA)

### Iterate on Edge Cases
First pass might miss edge cases. Ask:
- "What could go wrong?"
- "What if the integration fails?"
- "What about multi-tenant isolation?"

### Validate Technical Questions
AI-generated questions might miss domain-specific concerns. Add your own based on {ORGANIZATION} experience.

### Use with Other Templates
Combine with:
- `templates/requirements-enhancement.md` for the prompt structure
- `workflows/generate-unit-tests.md` after requirements approved
- `templates/architecture-decision-record.md` for complex features

## Common Pitfalls to Avoid
- ❌ **Accepting first output**: Always review and refine
- ❌ **Skipping tech lead review**: They'll catch missed integration impacts
- ❌ **Not clarifying with product**: Technical questions need answers
- ❌ **Over-reliance on AI**: Use judgment to add domain-specific edge cases
- ❌ **Forgetting accessibility**: Always explicitly ask about WCAG compliance
- ❌ **ACs in Description**: Always put ACs in the dedicated Acceptance Criteria field
- ❌ **Implementation as ACs**: ACs must describe expected behavior, not steps
- ❌ **Missing edge cases**: Include at least one negative/edge case per AC

## Definition of Ready Validation

Before finalizing the enhanced story, verify it meets the DoR checklist in `playbooks/PLAYBOOK-GUIDE.md`.

> **Remember:** "Unknown" is acceptable. "Implicit" is not.

## Integration with Other Workflows

### Inputs From Other Workflows

**From Brownfield Repository Analysis** (`workflows/brownfield-repository-analysis.md`):
- **Core flows** → Understand existing behavior before changing
- **Data ownership** → Know which services to modify
- **Risk hotspots** → Avoid dangerous areas or plan carefully
- **Integration points** → Consider downstream impacts

```
# Using brownfield analysis when enhancing requirements
Read @GenDD-Flow/workflows/enhance-acceptance-criteria.md

For modifying an existing system, first reference:
- Core flows from @docs/brownfield/gendd/flows/
- Risk hotspots from @docs/brownfield/pass2-infer-findings.md

Then enhance the requirements considering existing patterns.
```

### Follow-Up Workflows
After enhancing acceptance criteria:
1. Use `workflows/generate-tests-from-gherkin.md` to generate a full test suite directly from the Gherkin ACs
2. Use `workflows/identify-test-gaps.md` to ensure test coverage is planned
3. Use `workflows/generate-architecture-diagrams.md` for complex features
4. Use `workflows/generate-unit-tests.md` once development starts
5. Use `workflows/create-context-pack.md` to document patterns for AI context



