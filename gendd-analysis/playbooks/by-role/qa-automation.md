# Role Playbook: QA Automation Engineer

**Role:** QA Automation Engineer
**Focus:** Test framework setup, CI test integration, fixture patterns, automation infrastructure
**Time:** 45-60 minutes

---

## Purpose

Analyze a codebase from a QA Automation Engineer perspective to understand:
- Test automation framework architecture
- CI/CD test integration
- Test data and fixture management
- Automation patterns and anti-patterns
- Infrastructure for reliable test execution

---

## Quick Prompt

```
Read @GenDD-Flow/templates/testing-standards.md
Read @TargetRepo/.cursor/testing.md
Read @TargetRepo/.cursor/conventions.md

Analyze @TargetRepo for test automation opportunities.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/templates/testing-standards.md
Read @GenDD-Flow/templates/context-pack.md
Read @TargetRepo/.cursor/testing.md
Read @TargetRepo/.cursor/conventions.md

Analyze @TargetRepo from a QA Automation Engineer perspective:

## Context
- Test Frameworks: [Jest | xUnit | pytest | Playwright | Cypress]
- CI Platform: [GitHub Actions | GitLab CI | Jenkins | CircleCI]
- Test Environments: [Local | Docker | Cloud]
- Current Automation: [%] of tests automated

## Phase 1: Test Framework Architecture

### Current Framework Setup
| Aspect | Implementation | Files | Health |
|--------|----------------|-------|--------|
| Unit test runner | [Jest/xUnit/etc] | `jest.config.js` | Good/Fair/Poor |
| Integration runner | [Framework] | [config file] | Good/Fair/Poor |
| E2E runner | [Playwright/Cypress] | [config file] | Good/Fair/Poor |
| Mock framework | [Library] | [usage pattern] | Good/Fair/Poor |
| Assertion library | [Library] | [usage pattern] | Good/Fair/Poor |

### Test Organization
| Pattern | Current State | Recommendation |
|---------|---------------|----------------|
| File structure | [pattern] | [suggestion] |
| Naming conventions | [pattern] | [suggestion] |
| Test grouping | [tags/folders] | [suggestion] |
| Parallel execution | [Yes/No/Partial] | [suggestion] |

## Phase 2: CI/CD Integration

### Current Pipeline
| Stage | Tests Run | Trigger | Duration | Pass Rate |
|-------|-----------|---------|----------|-----------|
| PR | Unit only | On PR | 5 min | 98% |
| Merge | Unit + Int | On merge | 15 min | 95% |
| Nightly | All | Scheduled | 45 min | 90% |

### Pipeline Configuration
| Aspect | Current | Best Practice | Gap |
|--------|---------|---------------|-----|
| Test parallelization | [state] | Max parallel | [gap] |
| Caching | [state] | Dependencies cached | [gap] |
| Retry logic | [state] | Flaky retry only | [gap] |
| Reporting | [state] | JUnit + artifacts | [gap] |
| Failure notifications | [state] | Slack/Teams | [gap] |

## Phase 3: Test Data Management

### Current Approach
| Aspect | Implementation | Issues |
|--------|----------------|--------|
| Fixtures | [Static files/Factories/API] | [issues] |
| Database state | [Seeds/Snapshots/Fresh] | [issues] |
| Test isolation | [Transactions/Cleanup/None] | [issues] |
| Sensitive data | [Masked/Vaulted/Hardcoded] | [issues] |

### Fixture Patterns
| Pattern | Used? | Location | Example |
|---------|-------|----------|---------|
| Factory pattern | Yes/No | [files] | `UserFactory.create()` |
| Builders | Yes/No | [files] | `new UserBuilder().build()` |
| Static fixtures | Yes/No | [files] | `fixtures/users.json` |
| API seeding | Yes/No | [files] | `seedData()` |

## Phase 4: Reliability Analysis

### Flaky Test Assessment
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Flaky test rate | [%] | <5% | Pass/Fail |
| Avg retry count | [n] | <1.5 | Pass/Fail |
| Timeout failures | [%] | <2% | Pass/Fail |

### Common Flakiness Causes
- [ ] Timing-dependent assertions
- [ ] Shared state between tests
- [ ] External service dependencies
- [ ] Race conditions in async code
- [ ] Database ordering assumptions

## Phase 5: E2E Automation Infrastructure

### Current Setup
| Component | Implementation | Notes |
|-----------|----------------|-------|
| Browser automation | [Playwright/Selenium/Cypress] | [version] |
| Headless support | [Yes/No] | [issues] |
| Screenshot on failure | [Yes/No] | [location] |
| Video recording | [Yes/No] | [location] |
| Trace collection | [Yes/No] | [location] |
| Cross-browser | [Browsers supported] | [issues] |

### Page Object Pattern
| Status | Implementation | Files |
|--------|----------------|-------|
| [Used/Not used/Partial] | [Pattern details] | `pages/` |

## Phase 6: Performance & Scalability

| Metric | Current | Target | Improvement Needed |
|--------|---------|--------|-------------------|
| Unit test suite time | [time] | <2 min | [action] |
| Integration test time | [time] | <10 min | [action] |
| E2E test time | [time] | <20 min | [action] |
| Parallelization | [level] | 4+ workers | [action] |

## Phase 7: Recommendations

### Infrastructure Improvements
| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
| P1 | [Item] | [S/M/L] | [High/Med] |
| P2 | [Item] | [S/M/L] | [High/Med] |

### Framework Enhancements
| Priority | Item | Effort | Impact |
|----------|------|--------|--------|

### CI/CD Optimizations
| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
```

---

## Follow-Up Actions

After completing this analysis:
- `playbooks/on-demand/identify-test-gaps.md` - Identify coverage gaps
- `playbooks/on-demand/generate-unit-tests.md` - Generate unit tests for gaps
- `playbooks/on-demand/generate-integration-tests.md` - Generate integration tests
- `playbooks/on-demand/run-assisted-testing.md` - Generate E2E tests with Playwright
- `playbooks/recurring/review-test-coverage.md` - Recurring coverage tracking

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.

---

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Identify Test Gaps Workflow | `workflows/identify-test-gaps.md` | 6-phase test gap analysis |
| Generate Unit Tests Workflow | `workflows/generate-unit-tests.md` | Unit test generation with standards |
| Integration Testing Workflow | `workflows/automate-integration-testing.md` | 7-phase integration test workflow |
| Testing Standards Template | `templates/testing-standards.md` | MUST/SHOULD/MAY test requirement levels |
| Context Pack Template | `templates/context-pack.md` (testing.md section) | Universal naming, AAA, scenarios |
