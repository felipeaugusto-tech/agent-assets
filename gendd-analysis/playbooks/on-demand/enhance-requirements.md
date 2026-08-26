# Enhance Acceptance Criteria

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | Product Owner, Business Analyst, QA Engineer |
| **Prerequisites** | Product requirement or feature request available, knowledge of target product and user persona |
| **Inputs** | Original requirement text, product name, user persona, integrations list, multi-tenant status, tech stack |
| **Outputs** | Jira-ready markdown with user story, Gherkin acceptance criteria, edge cases, integration impacts, NFRs, test scenarios |

## When to Use

- Product manager provides a high-level feature request that lacks technical detail
- Before sprint planning or backlog refinement to ensure story readiness
- When creating Jira tickets and you need comprehensive acceptance criteria
- When QA needs testable requirements before development begins

## Before You Start

- [ ] You have the original product requirement (email, doc, or verbal request)
- [ ] You know the target product (e.g., {PRODUCT_NAME})
- [ ] You know the user persona (e.g., school administrator, donor)
- [ ] You have a list of integrations that might be affected
- [ ] You know whether multi-tenant considerations apply

## Steps

### Step 1: Gather context

- Do: Collect all relevant information about the requirement
- How: Document the original requirement, target product, user persona, existing integrations, multi-tenant status, and tech stack
- Expect: A complete context block ready for the prompt

### Step 2: Generate enhanced acceptance criteria

- Do: Transform the vague requirement into detailed, engineer-ready acceptance criteria
- How: Open Cursor Chat and use:
  ```
  Read @GenDD-Flow/workflows/enhance-acceptance-criteria.md

  Transform this requirement into detailed acceptance criteria:

  Original Requirement:
  """
  [PASTE YOUR REQUIREMENT HERE]
  """

  Context:
  - Product: [PRODUCT NAME]
  - User Persona: [TARGET USER - e.g., school administrator, donor]
  - Existing Integrations: [LIST - e.g., WorldPay, SendGrid, SSO]
  - Multi-tenant: [YES/NO]
  - Tech Stack: [e.g., .NET Core 8, React, PostgreSQL]

  Generate:

  1. **User Story** (Given-When-Then format)
     - Clear actor, action, outcome
     - Business value articulated

  2. **Acceptance Criteria** (Gherkin format)
     - GIVEN preconditions
     - WHEN action occurs
     - THEN expected outcomes
     - Cover happy path and errors

  3. **Edge Cases** (minimum 5)
     - Null/empty inputs
     - Boundary conditions
     - Multi-tenant isolation
     - Integration failures
     - Accessibility (WCAG 2.1 AA)

  4. **Integration Impacts**
     - Affected services
     - API contract changes
     - Downstream dependencies

  5. **Non-Functional Requirements**
     - Performance targets
     - Security requirements
     - Accessibility standards
     - Compliance (PCI, GDPR)

  6. **Test Scenarios** (3-5 key tests)
     - Happy path
     - Error conditions
     - Edge cases

  7. **Technical Questions**
     - Ambiguities needing product team input

  Format as Jira-ready markdown.
  ```

#### Example

  **Input:**
  ```
  Add ability for users to save payment methods for future use.
  ```

  **Expected Output Structure:**
  - User Story with Given-When-Then
  - 3-4 acceptance criteria in Gherkin
  - 5+ edge cases
  - Integration impacts (Vault, Payment Gateway, User Service)
  - NFRs (performance, security, accessibility)
  - Test scenarios
  - Technical questions for product team
- Expect: Comprehensive output with all 7 sections

### Step 3: Review and refine edge cases

- Do: Verify edge cases cover all critical scenarios
- How: Check for missing scenarios:
  ```
  Review the acceptance criteria and edge cases. Are we missing scenarios for:
  - Multi-tenant data isolation
  - Integration failures
  - Expired credentials or tokens
  - Rate limiting or throttling
  - Concurrent user actions
  - Accessibility (WCAG 2.1 AA)
  ```
- Expect: Additional edge cases identified and added

### Step 4: Validate NFRs for architecture readiness

- Do: Ensure non-functional requirements are measurable and testable
- How: Review each NFR and verify it has a measurable target, verification method, and architecture impact
- Expect: NFR table with concrete targets (e.g., "<200ms p95" not just "fast")

### Step 5: Clarify technical questions with product team

- Do: Send generated technical questions to the product team
- How: Schedule a quick sync or send the questions asynchronously. Update requirements based on answers.
- Expect: Resolved ambiguities and updated acceptance criteria

### Step 6: Create Jira ticket

- Do: Format the final output for Jira
- How: Copy enhanced requirements into a new Jira ticket with labels: `ai-enhanced`, product name, feature type
- Expect: A complete, Jira-ready ticket with all sections

## Expected Output

```markdown
# User Story
AS A [persona] WHEN [action] I WANT TO [goal] SO THAT [business value]

# Acceptance Criteria (Gherkin)
## AC1: [Scenario Name]
GIVEN [precondition] WHEN [action] THEN [expected outcome]

# Edge Cases (5+)
# Integration Impacts
# Non-Functional Requirements
# Test Scenarios
# Technical Questions
# Estimated Complexity
```

**Save to:** Jira ticket or `@TargetRepo/docs/requirements/`

## What's Next

- [ ] [Validate Acceptance Criteria](validate-acceptance-criteria.md) with Playwright against the live application
- [ ] [Identify Test Gaps](identify-test-gaps.md) to plan test coverage
- [ ] [Generate Unit Tests](generate-unit-tests.md) once development starts
- [ ] [Generate Architecture Diagrams](generate-architecture-diagrams.md) for complex features

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Enhance AC Workflow | `workflows/enhance-acceptance-criteria.md` | 13-step workflow with review checklists |
