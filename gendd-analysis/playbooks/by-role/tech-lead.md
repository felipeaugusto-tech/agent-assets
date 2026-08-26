# Role Playbook: Tech Lead

**Role:** Tech Lead / Technical Lead
**Focus:** Code review checklist, PR analysis, team conventions, code quality, DoD verification
**Time:** 30-45 minutes

---

## Purpose

Analyze a codebase from a Tech Lead perspective to understand:
- Code quality and conventions
- PR review standards
- Team development practices
- Onboarding requirements
- Technical excellence indicators
- Definition of Done verification for technical criteria

---

## {ORGANIZATION} Definition of Done - Tech Lead Responsibilities

> **Reference:** This playbook aligns with {ORGANIZATION}'s **Definition of Done** and **Story Templates** standards.

### DoD Technical Verification Checklist

Tech Leads are responsible for verifying the following DoD criteria:

| DoD Criterion | Tech Lead Responsibility |
|---------------|--------------------------|
| Expected behavior verified against ACs | Code review confirms implementation matches ACs |
| Security concerns addressed | Verify security-flagged items are resolved |
| Integration behavior verified | Review integration points, test coverage |
| Test evidence exists | Confirm adequate test coverage added |
| Automation coverage addressed | Verify tests added or deferral documented |

### Automation Expectations

Per {ORGANIZATION} DoD standards:

- **Automated tests are expected by default** for new or changed behavior
- A story may be Done without automation **only when a clear, explicit reason is documented** (e.g., legacy constraints, tooling gaps, excessive setup cost)
- Any automation deferral should be treated as **intentional debt**, not invisible backlog
- Repeated automation deferral is a signal for leadership review

### Story Quality Verification

Before approving PRs, verify story met Definition of Ready:

| Check | Question |
|-------|----------|
| ACs Clear | Were Acceptance Criteria in the dedicated AC field? |
| Behavior-Based | Did ACs describe expected behavior (not implementation)? |
| Integration Flagged | Was integration impact identified upfront? |
| Security Flagged | Was security review need identified upfront? |
| Unknowns Documented | Were assumptions explicitly stated? |

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/tech-lead.md
Analyze @TargetRepo for code quality and conventions.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/tech-lead.md

Analyze @TargetRepo from a Tech Lead perspective:

## Context
- Team Size: [Number of developers]
- Tech Stack: [Primary technologies]
- Code Review Process: [Required reviewers, tools]
- Development Style: [Trunk-based, GitFlow, etc]

## Phase 1: Code Quality Assessment

### Static Analysis

> **Note:** Coverage thresholds should be set per repository based on maturity, domain risk, and compliance requirements. See the Coverage Guidance section in `templates/context-pack.md` (testing.md). Prioritize meaningful coverage of critical business logic over a universal numeric target.

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Code coverage | [%] | [repo target] | Pass/Fail |
| Cyclomatic complexity (avg) | [n] | <10 | Pass/Fail |
| Code duplication | [%] | <5% | Pass/Fail |
| Linting errors | [n] | 0 | Pass/Fail |
| Type coverage | [%] | 95% | Pass/Fail |

### Code Smells
| Smell | Occurrences | Severity | Examples |
|-------|-------------|----------|----------|
| Long methods | [n] | High/Med/Low | [files] |
| God classes | [n] | High/Med/Low | [files] |
| Feature envy | [n] | High/Med/Low | [files] |
| Dead code | [n] | High/Med/Low | [files] |
| Magic numbers | [n] | High/Med/Low | [files] |

## Phase 2: Conventions Analysis

### Naming Conventions
| Element | Convention | Consistent? | Examples |
|---------|------------|-------------|----------|
| Files | [pattern] | Yes/No | [examples] |
| Classes | [PascalCase/etc] | Yes/No | [examples] |
| Functions | [camelCase/etc] | Yes/No | [examples] |
| Variables | [pattern] | Yes/No | [examples] |
| Constants | [UPPER_CASE/etc] | Yes/No | [examples] |

### Code Organization
| Aspect | Pattern | Documented? | Followed? |
|--------|---------|-------------|-----------|
| File structure | [pattern] | Yes/No | Yes/No |
| Import order | [pattern] | Yes/No | Yes/No |
| Export style | [named/default] | Yes/No | Yes/No |
| Test location | [co-located/__tests__] | Yes/No | Yes/No |

## Phase 3: PR/Code Review Standards

### Current State
| Aspect | Implementation | Quality |
|--------|----------------|---------|
| PR template | [Yes/No] | [assessment] |
| Required reviewers | [count] | [appropriate?] |
| CI checks | [list] | [complete?] |
| Size guidelines | [Yes/No] | [followed?] |
| Review SLA | [time] | [met?] |

### DoD-Aligned Review Checklist

| Category | Checks Present | DoD Alignment | Missing |
|----------|----------------|---------------|---------|
| **AC Verification** | [list] | ACs validated | [list] |
| **Behavior Match** | [list] | Expected behavior verified | [list] |
| **Security** | [list] | Security concerns addressed | [list] |
| **Integration** | [list] | Integration behavior verified | [list] |
| **Test Evidence** | [list] | Tests exist (manual/automated) | [list] |
| **Automation** | [list] | Coverage added or deferral documented | [list] |
| Code quality | [list] | - | [list] |
| Performance | [list] | - | [list] |
| Documentation | [list] | User-visible changes documented | [list] |

## Phase 4: Development Workflow

### Branching Strategy
| Aspect | Current | Recommendation |
|--------|---------|----------------|
| Strategy | [GitFlow/Trunk/etc] | [assessment] |
| Branch naming | [pattern] | [assessment] |
| Commit messages | [style] | [assessment] |
| Merge strategy | [Squash/Rebase/Merge] | [assessment] |

### Automation
| Process | Automated? | Tool | Gap |
|---------|------------|------|-----|
| Formatting | Yes/No | [Prettier/etc] | |
| Linting | Yes/No | [ESLint/etc] | |
| Type checking | Yes/No | [TypeScript/etc] | |
| Testing | Yes/No | [Jest/etc] | |
| Security scan | Yes/No | [Tool] | |

## Phase 5: Documentation Assessment

### Code Documentation
| Type | Coverage | Quality |
|------|----------|---------|
| README | Present/Missing | Good/Fair/Poor |
| API docs | [%] | Good/Fair/Poor |
| Code comments | [%] | Good/Fair/Poor |
| Architecture docs | Present/Missing | Good/Fair/Poor |
| Onboarding guide | Present/Missing | Good/Fair/Poor |

### Knowledge Gaps
| Area | Documentation | Risk |
|------|---------------|------|
| [Area] | Missing/Outdated | High/Med/Low |

## Phase 6: Team Productivity Indicators

### Code Health
| Indicator | Value | Trend |
|-----------|-------|-------|
| PR merge time | [hours] | Improving/Stable/Declining |
| PR size (avg lines) | [lines] | Improving/Stable/Declining |
| Revert rate | [%] | Improving/Stable/Declining |
| Hotfix frequency | [/month] | Improving/Stable/Declining |

### Development Experience
| Aspect | Assessment | Improvement |
|--------|------------|-------------|
| Build time | [time] | [possible improvement] |
| Test time | [time] | [possible improvement] |
| Dev environment setup | [time] | [possible improvement] |

## Phase 7: Onboarding Readiness

### New Developer Checklist
| Item | Exists? | Quality | Priority |
|------|---------|---------|----------|
| Setup guide | Yes/No | Good/Fair/Poor | High |
| Architecture overview | Yes/No | Good/Fair/Poor | High |
| Coding standards | Yes/No | Good/Fair/Poor | High |
| Common tasks guide | Yes/No | Good/Fair/Poor | Med |
| Debugging guide | Yes/No | Good/Fair/Poor | Med |

## Phase 8: Recommendations

### Immediate Actions
| Action | Impact | Effort |
|--------|--------|--------|
| [Action] | High/Med | S/M/L |

### Process Improvements
| Improvement | Benefit | Implementation |
|-------------|---------|----------------|
| [Improvement] | [Benefit] | [Steps] |

### Documentation Needs
| Document | Purpose | Priority |
|----------|---------|----------|
| [Document] | [Purpose] | P1/P2/P3 |
```

---

## Output: Tech Lead Assessment

```markdown
# Tech Lead Assessment: [Project Name]
Generated: [Date]
Analyzed by: Tech Lead Playbook

## Code Quality Score: [X/10]

## Quality Metrics

| Metric | Value | Status |
|--------|-------|--------|
| Coverage | [%] | |
| Complexity | [n] | |
| Duplication | [%] | |
| Linting | [n] | |

## Conventions

### Documented Standards
- [Standard 1]
- [Standard 2]

### Gaps
- [Gap 1]
- [Gap 2]

## PR Review Checklist

### Recommended Checklist
```markdown
## PR Review Checklist

### Functionality
- [ ] Code does what it claims to do
- [ ] Edge cases handled
- [ ] Error handling appropriate

### Code Quality
- [ ] Follows project conventions
- [ ] No unnecessary complexity
- [ ] DRY principle followed
- [ ] Clear naming

### Testing
- [ ] Tests added/updated
- [ ] Tests pass locally
- [ ] Coverage maintained

### Security
- [ ] No sensitive data exposed
- [ ] Input validation present
- [ ] Auth/authz correct

### Documentation
- [ ] Code comments where needed
- [ ] README updated if needed
- [ ] API docs updated if needed
```

## Onboarding Guide

### Getting Started
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Key Conventions
[Summary of conventions]

### Common Tasks
[How to do common things]

## Recommendations

### Priority 1 (This Sprint)
- [ ] [Action]

### Priority 2 (This Quarter)
- [ ] [Action]
```

---

## Reference Templates

This playbook's analysis areas align with the universal principles in the Context Pack template. Reference them for baseline expectations:

| Template | Relevant Sections |
|----------|-------------------|
| `templates/context-pack.md` (conventions.md section) | Naming conventions, SRP, error handling, formatting/linting, version control (commits, branches, PRs, code review) |
| `templates/context-pack.md` (testing.md section) | AAA pattern, test naming, coverage guidance, required scenarios, CI/CD gating |
| `templates/context-pack.md` (agents.md section) | Security code review checklist |

---

## Follow-Up Actions

- For AI context setup: [Create Context Pack](../../workflows/create-context-pack.md) — ensures AI tools follow your team's conventions
- For architecture documentation: [Generate Architecture Diagrams](../../workflows/generate-architecture-diagrams.md) — C4 diagrams from codebase analysis
- For full codebase analysis: [Brownfield Analysis](../../workflows/brownfield-repository-analysis.md)
- For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
