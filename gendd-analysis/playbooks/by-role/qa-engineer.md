# Role Playbook: QA Engineer

**Role:** QA Engineer
**Focus:** Test gaps, AC validation, E2E generation, coverage matrix, DoD verification
**Time:** 45-60 minutes

---

## Purpose

Analyze a codebase from a QA Engineer perspective to understand:
- Current test coverage and gaps
- Test quality and patterns
- Acceptance criteria testability
- Risk areas needing test attention
- Definition of Done verification

---

## {ORGANIZATION} Testing & Quality Standards

> **Reference:** This playbook aligns with {ORGANIZATION}'s **Story Templates**, **Bug Template**, and **Definition of Done** standards.

### Definition of Done - QA Responsibilities

QA Engineers are responsible for verifying the following DoD criteria:

| DoD Criterion | QA Responsibility |
|---------------|-------------------|
| All Acceptance Criteria validated | Verify against ACs in dedicated field |
| Expected behavior verified | Test against stated behavior, not inferred |
| No known critical defects remain open | Track and confirm resolution |
| Integration behavior verified | Test integration points where applicable |
| Test evidence exists | Document manual or automated test results |
| Automation coverage addressed | Confirm implemented or deferral documented |

### Bug Template (Lean)

When creating bugs, use this structure to eliminate "See STR" patterns:

| Field | Description | Required |
|-------|-------------|----------|
| **Observed Behavior** | What is happening now? | Yes |
| **Expected Behavior** | What should be happening? | Yes |
| **Steps to Reproduce** | Clear, numbered steps | Yes |
| **Environment / Data Context** | Environment, configuration, or data prerequisites | Yes |
| **Impact & Severity** | User impact and business risk | Yes |
| **Related Story / Release** | Link to originating change if known | Recommended |

### AC Validation Standards

Acceptance Criteria must be testable. QA should verify:

- [ ] ACs are in the dedicated Acceptance Criteria field (not Description)
- [ ] ACs use Gherkin format: Given [context] / When [action] / Then [outcome]
- [ ] ACs describe expected behavior (not implementation steps)
- [ ] Happy path scenarios covered
- [ ] At least one negative or edge case included
- [ ] Integration behavior expectations documented

---

## Quick Prompt

```
Read @GenDD-Flow/templates/testing-standards.md
Read @TargetRepo/.cursor/testing.md
Read @TargetRepo/.cursor/context.md

Analyze @TargetRepo for test gaps and coverage.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/workflows/identify-test-gaps.md
Read @GenDD-Flow/templates/testing-standards.md
Read @GenDD-Flow/templates/context-pack.md
Read @TargetRepo/.cursor/testing.md
Read @TargetRepo/.cursor/context.md

Analyze @TargetRepo from a QA Engineer perspective:

## Context
- Product: [PRODUCT NAME]
- Critical Features: [LIST - e.g., payments, auth, data export]
- Known Problem Areas: [Areas with recent bugs]
- Test Frameworks: [Jest, xUnit, Playwright, etc.]

## Phase 1: Test Inventory

Catalog all existing tests:
| Test Type | Location | Framework | Count | Last Modified |
|-----------|----------|-----------|-------|---------------|
| Unit | `tests/unit/` | Jest | 150 | Recent |
| Integration | `tests/integration/` | Supertest | 45 | 2 months ago |
| E2E | `tests/e2e/` | Playwright | 20 | Recent |
| Contract | `tests/contract/` | Pact | 0 | N/A |

## Phase 2: Coverage Analysis

### By Component
| Component | Unit | Integration | E2E | Overall Risk |
|-----------|------|-------------|-----|--------------|
| Auth | 80% | 60% | 3 flows | Low |
| Payments | 40% | 20% | 0 flows | HIGH |
| User Mgmt | 70% | 50% | 2 flows | Medium |

### By Test Pyramid
```
       E2E
      /    \
     /  20  \
    ──────────
   /    45    \
  / Integration \
 ────────────────
/      150       \
      Unit
```
Is this balanced? [Yes/No - analysis]

## Phase 3: Gap Analysis

### Critical Gaps (High Risk)
| Feature | Expected Tests | Actual Tests | Gap | Business Impact |
|---------|----------------|--------------|-----|-----------------|
| [Feature] | Unit + Int + E2E | Unit only | Int + E2E | Payment failures undetected |

### Medium Gaps
| Feature | Expected | Actual | Gap |
|---------|----------|--------|-----|

### Low Priority Gaps
| Feature | Expected | Actual | Gap |
|---------|----------|--------|-----|

## Phase 4: Test Quality Assessment

| Quality Aspect | Status | Issues Found |
|----------------|--------|--------------|
| Naming conventions | Good/Fair/Poor | [issues] |
| Arrange-Act-Assert | Good/Fair/Poor | [issues] |
| Test isolation | Good/Fair/Poor | [issues] |
| Flaky tests | None/Some/Many | [list] |
| Test data management | Good/Fair/Poor | [issues] |
| Mock usage | Appropriate/Over/Under | [issues] |

## Phase 5: E2E Test Analysis

### Existing E2E Coverage
| User Journey | Covered? | Test File | Last Run |
|--------------|----------|-----------|----------|
| User registration | Yes/Partial/No | [file] | [date] |
| Login flow | Yes/Partial/No | [file] | [date] |
| Main feature | Yes/Partial/No | [file] | [date] |

### Missing E2E Tests
| Journey | Priority | Reason | Effort |
|---------|----------|--------|--------|
| [Journey] | P1 | Critical flow, no coverage | Medium |

## Phase 6: Acceptance Criteria Testability

For key features, evaluate AC testability against {ORGANIZATION} standards:

| Feature | AC in Dedicated Field | Gherkin Format | Happy Path | Edge Case | Testable |
|---------|----------------------|----------------|------------|-----------|----------|
| [Feature] | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No |

### AC Quality Issues

| Issue | Count | Impact | Fix |
|-------|-------|--------|-----|
| ACs in Description/comments | [n] | Not visible to testers | Move to AC field |
| ACs describe implementation | [n] | Can't verify outcome | Rewrite as outcomes |
| Missing edge cases | [n] | Late discovery of failures | Add negative scenarios |
| "See STR" without expected behavior | [n] | QA discovers requirements | Define expected behavior |
| Missing data-testid attributes | [n] | Automation blocked | Add test hooks |
| Non-deterministic behavior | [n] | Flaky tests | Address root cause |

### AC Testability Checklist

For each story, verify:
- [ ] ACs are in the dedicated Acceptance Criteria field
- [ ] Each AC uses Gherkin: Given [context] / When [action] / Then [outcome]
- [ ] Expected behavior is stated (not "works correctly")
- [ ] Integration behavior expectations are documented
- [ ] Test data requirements are specified

## Phase 7: Domain-Specific Coverage (When Applicable)

Evaluate domain-specific test coverage against the required test scenarios in `templates/context-pack.md` (testing.md section). For each applicable domain, use this output format:

| Area | Test Exists? | Type | Notes |
|------|-------------|------|-------|
| [Scenario from testing-principles.md] | Yes/No | Unit/Int/E2E | [notes] |

**Domains to evaluate** (skip any that do not apply to this repository):

- **Payment / Financial** — Card validation, AVS, PIN, idempotency, anomaly detection, sensitive data masking
- **Email / Notifications** — Delivery triggers, template selection, data population, deduplication
- **Security / Auth** — Account lockout, password policy, session expiry
- **Regression / Sanity** — Smoke tests exist and run post-deploy, full regression suite current, stale tests removed, tests modularized by feature area
- **UI / Accessibility** — WCAG 2.1 AA compliance, responsive breakpoints, usability of key journeys
- **Cross-Layer** — Same feature tested at backend (unit), API (integration), and frontend (E2E)

## Phase 8: Recommendations

### Immediate Actions (P1)
| Action | Reason | Effort |
|--------|--------|--------|
| [Action] | [Risk] | [S/M/L] |

### Short-term (P2)
| Action | Reason | Effort |
|--------|--------|--------|

### Long-term (P3)
| Action | Reason | Effort |
|--------|--------|--------|
```

---

## Playwright MCP Integration

For live application testing:

```
Read @GenDD-Flow/playbooks/on-demand/validate-acceptance-criteria.md
Read @GenDD-Flow/templates/testing-standards.md
Read @TargetRepo/.cursor/testing.md

Using Playwright MCP on [APP_URL]:

1. Navigate through key user journeys
2. Document testable elements (data-testid)
3. Validate acceptance criteria are automatable
4. Identify missing test hooks
5. Generate E2E test recommendations
```

---

## Follow-Up Actions

For test generation, use the appropriate playbooks:
- `playbooks/on-demand/generate-unit-tests.md` - Unit test generation
- `playbooks/on-demand/generate-integration-tests.md` - Integration test generation
- `playbooks/on-demand/run-assisted-testing.md` - E2E test generation with Playwright

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.

---

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Identify Test Gaps Workflow | `workflows/identify-test-gaps.md` | 6-phase test gap analysis with output artifacts |
| Generate Unit Tests Workflow | `workflows/generate-unit-tests.md` | Unit test generation with standards and examples |
| Integration Testing Workflow | `workflows/automate-integration-testing.md` | 7-phase integration test generation with CI/CD |
| Enhance AC Workflow | `workflows/enhance-acceptance-criteria.md` | Shift-left story quality for testable ACs |
| Testing Standards Template | `templates/testing-standards.md` | MUST/SHOULD/MAY test requirement levels |
| Context Pack Template | `templates/context-pack.md` (testing.md section) | Universal naming, AAA, scenarios, coverage |
