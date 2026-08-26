# Role Playbook: Engineering Manager

**Role:** Engineering Manager
**Focus:** Health metrics, velocity patterns, tech debt prioritization, DoR/DoD compliance
**Time:** 30-45 minutes

---

## Purpose

Analyze a codebase from an Engineering Manager perspective to understand:
- Team productivity and code health indicators
- Technical debt impact on velocity
- Risk areas requiring attention
- Resource allocation insights
- DoR/DoD compliance and rework signals

---

## {ORGANIZATION} Delivery Health Standards

> **Reference:** This playbook aligns with {ORGANIZATION}'s **Story Templates** and **Definition of Ready/Done** for delivery metrics.

### Key Metrics from DoR/DoD Analysis

The following metrics indicate upstream quality issues tied to Definition of Ready:

| Metric | Healthy | Warning | Critical | Root Cause |
|--------|---------|---------|----------|------------|
| Story reopen rate | <5% | 5-15% | >15% | Weak DoR enforcement |
| QA-discovered requirements | <10% | 10-20% | >20% | ACs missing or vague |
| Security-blocked releases | 0 | 1-2/quarter | >2/quarter | Security flags missed in DoR |
| Reverts from integration issues | <2% | 2-5% | >5% | Integration impact not identified |
| Late scope changes | <5% | 5-10% | >10% | Scope boundaries not defined |

### Rework Signals to Monitor

Analysis of Jira data confirms primary SDLC constraint is **input quality, not engineering speed**:

| Signal | Evidence | Action |
|--------|----------|--------|
| <15% of stories use AC field effectively | AC in Description/comments | BA training, tooling |
| 10-15% active work is rework/reversions | Reopen, revert patterns | DoR enforcement |
| QA as discovery phase | Bugs contain requirements | Shift-left AC quality |
| Late security discovery | "In Secure Code Review" blocks | Security flags in DoR |
| Integration surprises | Stories flagged late for integration | Integration impact in Epic/Story |

### Automation Deferral Tracking

Per {ORGANIZATION} DoD standards:
- Automation expected by default for new behavior
- Deferral acceptable only with documented reason
- Repeated deferral is a signal for leadership review

| Team | Automation Deferral Rate | Reason Distribution | Action |
|------|--------------------------|---------------------|--------|
| [Team] | [%] | Legacy/Tooling/Setup | Review if >20% |

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/engineering-manager.md
Analyze @TargetRepo for engineering health metrics.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/engineering-manager.md

Analyze @TargetRepo from an Engineering Manager perspective:

## Context
- Team Size: [Number of developers]
- Sprint Length: [1/2/3 weeks]
- Key Business Goals: [Current priorities]
- Known Pain Points: [If any]

## Phase 1: Codebase Health Metrics

### Overall Health
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Code coverage | [%] | 80% | Good/Warning/Critical |
| Tech debt ratio | [%] | <10% | Good/Warning/Critical |
| Dependency freshness | [months avg] | <6 months | Good/Warning/Critical |
| Build time | [minutes] | <5 min | Good/Warning/Critical |
| Test suite time | [minutes] | <10 min | Good/Warning/Critical |

### Trend Indicators
| Metric | 3 Months Ago | Now | Trend |
|--------|--------------|-----|-------|
| Coverage | [%] | [%] | ↑/→/↓ |
| Build time | [min] | [min] | ↑/→/↓ |
| PR merge time | [hours] | [hours] | ↑/→/↓ |

## Phase 2: Complexity & Risk Analysis

### Hotspot Analysis
| Area | Change Frequency | Complexity | Risk Score |
|------|------------------|------------|------------|
| [File/Module] | High/Med/Low | High/Med/Low | [1-10] |

### Bus Factor Assessment
| Area | Contributors | Risk | Action |
|------|--------------|------|--------|
| [Area] | 1-2 | High | Document, cross-train |
| [Area] | 3-5 | Medium | Continue monitoring |
| [Area] | 5+ | Low | Good coverage |

## Phase 3: Technical Debt Impact

### Debt Inventory
| Category | Items | Estimated Effort | Velocity Impact |
|----------|-------|------------------|-----------------|
| Architecture debt | [n] | [story points] | [%] slowdown |
| Code quality debt | [n] | [story points] | [%] slowdown |
| Test debt | [n] | [story points] | [%] rework |
| Documentation debt | [n] | [story points] | [onboarding days] |
| Infrastructure debt | [n] | [story points] | [%] incident time] |

### Debt Interest Calculation
| Debt Item | Monthly Interest | Payoff Effort | ROI |
|-----------|------------------|---------------|-----|
| [Item] | [hours/month] | [days] | [months to ROI] |

## Phase 4: Development Velocity Indicators

### PR Metrics
| Metric | Value | Benchmark |
|--------|-------|-----------|
| Avg PR size (lines) | [n] | <400 |
| Avg review time | [hours] | <24h |
| Avg merge time | [hours] | <48h |
| PR rejection rate | [%] | <10% |
| Revert rate | [%] | <2% |

### Deployment Frequency
| Metric | Value | Benchmark |
|--------|-------|-----------|
| Deploys per week | [n] | [target] |
| Lead time for changes | [days] | <1 day |
| Change failure rate | [%] | <15% |
| MTTR | [hours] | <1 hour |

## Phase 5: Quality Indicators

### Production Health
| Metric | Value | Trend |
|--------|-------|-------|
| Bug rate (per release) | [n] | ↑/→/↓ |
| Critical bugs (last 30 days) | [n] | ↑/→/↓ |
| Customer-reported issues | [n] | ↑/→/↓ |
| Incident frequency | [n/month] | ↑/→/↓ |

### Test Health
| Metric | Value | Status |
|--------|-------|--------|
| Flaky test rate | [%] | Good/Warning |
| Test maintenance burden | [hours/sprint] | Good/Warning |
| Missing critical tests | [n areas] | Good/Warning |

## Phase 6: Resource & Capacity Insights

### Team Allocation Indicators
| Activity | Code Evidence | Estimated % |
|----------|---------------|-------------|
| Feature development | New features | [%] |
| Bug fixes | Bug commits | [%] |
| Tech debt | Refactoring | [%] |
| Infrastructure | DevOps changes | [%] |
| Documentation | Doc updates | [%] |

### Capacity Drains
| Drain | Evidence | Impact | Mitigation |
|-------|----------|--------|------------|
| [Issue] | [Evidence] | [hours/sprint] | [Action] |

## Phase 7: Risk Assessment

### Technical Risks
| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| [Risk] | High/Med/Low | High/Med/Low | [Action] | [TBD] |

### Timeline Risks
| Area | Risk Factor | Impact on Delivery |
|------|-------------|-------------------|
| [Area] | [Factor] | [Days/weeks delay] |

## Phase 8: Recommendations

### Strategic Priorities
| Priority | Investment | Expected Outcome |
|----------|------------|------------------|
| 1 | [Investment] | [Outcome] |
| 2 | [Investment] | [Outcome] |
| 3 | [Investment] | [Outcome] |

### Tech Debt Paydown Recommendation
| Quarter | Focus Area | Investment | Expected ROI |
|---------|------------|------------|--------------|
| Q1 | [Area] | [%] capacity | [benefit] |
| Q2 | [Area] | [%] capacity | [benefit] |

### Team Development
| Area | Recommendation | Benefit |
|------|----------------|---------|
| [Area] | [Recommendation] | [Benefit] |
```

---

## Output: Engineering Health Report

```markdown
# Engineering Health Report: [Project Name]
Generated: [Date]
Analyzed by: Engineering Manager Playbook

## Executive Summary
[2-3 sentence summary of engineering health]

## Health Dashboard

### Overall Score: [X/10]

| Category | Score | Trend |
|----------|-------|-------|
| Code Quality | [/10] | ↑/→/↓ |
| Velocity | [/10] | ↑/→/↓ |
| Stability | [/10] | ↑/→/↓ |
| Tech Debt | [/10] | ↑/→/↓ |

## DORA Metrics

| Metric | Value | Elite | Status |
|--------|-------|-------|--------|
| Deploy frequency | [x/week] | Multiple/day | |
| Lead time | [days] | <1 day | |
| Change failure rate | [%] | <15% | |
| MTTR | [hours] | <1 hour | |

## Tech Debt Summary

### Debt Distribution
```
Architecture: ████████░░ 80%
Code Quality: █████░░░░░ 50%
Testing:      ███░░░░░░░ 30%
Docs:         ██░░░░░░░░ 20%
```

### Top Items to Address
1. [Item] - ROI: [X months]
2. [Item] - ROI: [X months]

## Risk Summary

### High Priority
| Risk | Impact | Mitigation |
|------|--------|------------|

## Investment Recommendation

### Next Quarter
- [X]% Feature development
- [X]% Tech debt paydown
- [X]% Infrastructure
- [X]% Documentation

## Action Items

### This Sprint
- [ ] [Action]

### This Quarter
- [ ] [Action]
```

---

## Follow-Up Actions

- For AI context setup: [Create Context Pack](../../workflows/create-context-pack.md) — reduces onboarding time and improves AI-generated code quality
- For architecture documentation: [Generate Architecture Diagrams](../../workflows/generate-architecture-diagrams.md) — standardized C4 diagrams for onboarding and ARB reviews
- For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
