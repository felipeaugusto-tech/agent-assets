# GenDD-Flow Playbook Guide

**Decision tree for "which playbook to run when" - select the right analysis for your situation.**

---

## {ORGANIZATION} Story & Delivery Standards

> All playbooks align with {ORGANIZATION}'s **Story Templates** and **Definition of Ready/Done** standards.
> 
> **Reference Documents:**
> - `002_Story Templates.docx` - Epic, Story, and Bug templates
> - `003_Definition of Ready_Definition of Done.docx` - DoR/DoD checklists

### Quick Reference: Definition of Ready

A story is "Ready for Development" when:
- [ ] Clear problem statement (what and why)
- [ ] ACs in dedicated Acceptance Criteria field (Gherkin format)
- [ ] Scope boundaries clear (In/Out of scope)
- [ ] Integration impact identified (Yes/No)
- [ ] Security review need identified (Yes/No)
- [ ] Unknowns explicitly documented

### Quick Reference: Definition of Done

A story is "Done" when:
- [ ] All ACs validated
- [ ] No critical defects remain
- [ ] Security concerns addressed
- [ ] Integration behavior verified
- [ ] Test evidence exists
- [ ] User-visible changes documented

---

## Quick Decision Matrix

| Situation | Playbook | Time |
|-----------|----------|------|
| New repository, first-time analysis | [Run Full Analysis](onboarding/run-full-analysis.md) | 2-4 hours |
| Switching IDE or refreshing IDE rules | [Generate IDE Rules](on-demand/generate-ide-rules.md) | 15-30 min |
| Need standards for an SDLC area | [Generate Standards](on-demand/generate-standards.md) | 30-60 min |
| Context areas outdated | [Refresh Context Areas](recurring/refresh-context-areas.md) | 1-2 hours |
| Major refactor completed | [Run Full Analysis](onboarding/run-full-analysis.md) | 2-4 hours |
| PR opened or code merged | [Delta Analysis](on-demand/run-delta-analysis.md) | 15-30 min |
| Incremental documentation updates | Incremental Doc Update | 30-45 min |
| Story readiness issues | Scrum Master Playbook | 30-45 min |
| AC quality problems | Business Analyst + QA Playbooks | 45-60 min |
| Gherkin ACs need automated tests | Generate Tests from Gherkin Workflow | 1-2 hours |

---

## Decision Flowchart

```
START: What do you need?
│
├─► Is this a NEW repository or MAJOR REFACTOR?
│     │
│     YES → Run FULL ANALYSIS (5-phase: brownfield + context + standards + IDE rules)
│           └─► playbooks/onboarding/run-full-analysis.md
│
├─► Are you SWITCHING IDEs or need to REFRESH IDE RULES?
│     │
│     YES → Generate IDE Rules (requires docs/context/ to exist)
│           └─► playbooks/on-demand/generate-ide-rules.md
│
├─► Do you need STANDARDS for a specific SDLC area?
│     │
│     YES → Generate Standards
│           └─► playbooks/on-demand/generate-standards.md
│
├─► Are CONTEXT AREAS outdated (quarterly check)?
│     │
│     YES → Refresh Context Areas (re-detect + regenerate + update IDE rules)
│           └─► playbooks/recurring/refresh-context-areas.md
│
├─► Is this triggered by a PR or code merge?
│     │
│     YES → Run DELTA ANALYSIS
│           └─► playbooks/on-demand/run-delta-analysis.md
│           │
│           ├─► Architecture changes detected?
│           │     YES → Also run: Refresh Context Areas
│           │
│           ├─► Test file changes detected?
│           │     YES → Also run: QA Engineer Playbook
│           │
│           ├─► API/Schema changes detected?
│           │     YES → Also run: Pass 2 on affected service
│           │
│           └─► Minor changes only?
│                 YES → Document summary only
│
├─► Need to update only affected documentation?
│     │
│     YES → Run INCREMENTAL DOC UPDATE
│           └─► workflows/incremental-doc-update.md
│
└─► Need scheduled maintenance check?
      │
      YES → Run TEST GAP ANALYSIS + doc freshness check
            └─► playbooks/on-demand/identify-test-gaps.md
```

> **Note:** Role-specific playbooks (`playbooks/by-role/`) are being migrated to `knowledge/sdlc-areas/`. See the role playbooks section below for current references.

---

## Playbook Categories

### Category 1: Full Analysis (Onboarding)

**When:** New repository, major refactor, first-time documentation
**What:** 5-phase flow: brownfield analysis + context areas + standards + IDE rules
**Time:** 2-4 hours (or 30-60 min if brownfield already exists)

See [Run Full Analysis](onboarding/run-full-analysis.md) playbook.

| Resource | Purpose |
|----------|---------|
| `playbooks/onboarding/run-full-analysis.md` | Full 5-phase playbook |
| `playbooks/onboarding/run-brownfield-analysis.md` | Phase 1: 4-pass brownfield analysis |
| `workflows/analyze-and-generate.md` | Master workflow |
| `workflows/generate-context-areas.md` | Phase 3: Context per area |
| `workflows/detect-and-generate-standards.md` | Phase 4: Standards generation |
| `workflows/generate-ide-rules.md` | Phase 5: IDE rule generation |

---

### Category 2: On-Demand Generation

**When:** Need IDE rules, standards, or specific outputs without re-running full analysis
**What:** Targeted generation for a specific need
**Time:** 15-60 minutes

| Playbook | When to Use | Time |
|----------|-------------|------|
| [Generate IDE Rules](on-demand/generate-ide-rules.md) | Switching IDEs, refreshing rules | 15-30 min |
| [Generate Standards](on-demand/generate-standards.md) | Need standards for an SDLC area | 30-60 min |
| [Delta Analysis](on-demand/run-delta-analysis.md) | PR opened, code merged | 15-30 min |
| [Enhance Requirements](on-demand/enhance-requirements.md) | Story needs detailed ACs | 30-60 min |
| [Identify Test Gaps](on-demand/identify-test-gaps.md) | Need test coverage analysis | 30-60 min |
| [Generate Architecture Diagrams](on-demand/generate-architecture-diagrams.md) | Need C4 diagrams | 30-60 min |
| [Generate Unit Tests](on-demand/generate-unit-tests.md) | Need unit tests for existing code | 30-60 min |
| [Generate Integration Tests](on-demand/generate-integration-tests.md) | Need integration tests | 30-60 min |
| [Create Context Pack](on-demand/create-context-pack.md) | Legacy context pack workflow | 30-60 min |

---

### Category 3: Recurring Maintenance

**When:** Periodic refresh to keep documentation current
**What:** Re-detect, regenerate, and validate context and rules
**Time:** 1-2 hours

| Playbook | Frequency | Purpose |
|----------|-----------|---------|
| [Refresh Context Areas](recurring/refresh-context-areas.md) | Quarterly or after major changes | Re-detect areas, regenerate context, update IDE rules |
| [Refresh Context Pack](recurring/refresh-context-pack.md) | Quarterly | Update legacy context pack files |
| [Review Test Coverage](recurring/review-test-coverage.md) | Quarterly | Verify test coverage meets standards |
| [Update Documentation](recurring/update-documentation.md) | After major changes | Broader documentation refresh |

---

### Category 4: PR/Merge Updates

**When:** PR opened, code merged to main, incremental changes
**What:** Delta analysis and selective doc updates
**Time:** 15-45 minutes

See [Run Delta Analysis](on-demand/run-delta-analysis.md) playbook.

| Resource | Purpose |
|----------|---------|
| `playbooks/on-demand/run-delta-analysis.md` | Change impact analysis |
| `workflows/incremental-doc-update.md` | Selective updates |

---

### Category 5: Role-Specific Analysis

> **Migration note:** Role-specific playbooks are being migrated to `knowledge/sdlc-areas/`. The files below remain available during the transition.

**When:** Manual trigger by team member for their perspective
**What:** Role-focused analysis with specialized outputs
**Time:** 30-60 minutes per role

See [Role Playbooks](#role-playbooks-complete-reference) section below.

---

## File Change → Playbook Mapping

Use this table when a PR triggers documentation updates:

| Changed Files Pattern | Playbook | Scope |
|----------------------|----------|-------|
| `src/services/*`, `*Service.*` | Delta Analysis → Pass 2 | Affected service only |
| `src/api/*`, `*.proto`, `openapi.*` | Delta + Architect Playbook | API contracts |
| `tests/*`, `*.spec.*`, `*.test.*` | QA Engineer Playbook | Test inventory update |
| `docker*`, `k8s/*`, `.github/*` | DevOps Engineer Playbook | Deployment section |
| `package.json`, `*.csproj`, `go.mod` | Delta Analysis | Dependencies section |
| `README*`, `docs/*` | Skip (already docs) | - |
| `migrations/*`, `schema/*` | Delta + DBA Playbook | Data model section |
| `src/components/*`, `*.tsx`, `*.vue` | Frontend Dev Playbook | UI patterns |
| `src/security/*`, `auth/*` | Security Engineer Playbook | Security review |

---

## Role Playbooks: Complete Reference

### Product & Planning Roles

| Role | File | Focus Areas |
|------|------|-------------|
| **Product Owner** | `playbooks/by-role/product-owner.md` | Backlog analysis, story prioritization, value mapping, feature inventory |
| **Business Analyst** | `playbooks/by-role/business-analyst.md` | Requirements elicitation, process flows, gap analysis, domain modeling |
| **Scrum Master** | `playbooks/by-role/scrum-master.md` | Delivery flow, coordination, bottleneck detection, execution hygiene |
| **UX Designer** | `playbooks/by-role/ux-designer.md` | UI inventory, accessibility audit, component patterns, user flows |

### Development Roles

| Role | File | Focus Areas |
|------|------|-------------|
| **Frontend Developer** | `playbooks/by-role/frontend-dev.md` | Component patterns, UI conventions, state management, styling |
| **Backend Developer** | `playbooks/by-role/backend-dev.md` | API patterns, service conventions, data access, error handling |
| **Full-Stack Developer** | `playbooks/by-role/fullstack-dev.md` | End-to-end patterns, integration points, full data flow |

### Quality Roles

| Role | File | Focus Areas |
|------|------|-------------|
| **QA Engineer** | `playbooks/by-role/qa-engineer.md` | Test gaps, AC validation, E2E generation, coverage matrix |
| **QA Automation** | `playbooks/by-role/qa-automation.md` | Test framework setup, CI test integration, fixture patterns |

### Operations Roles

| Role | File | Focus Areas |
|------|------|-------------|
| **DevOps Engineer** | `playbooks/by-role/devops-engineer.md` | CI/CD analysis, deployment patterns, infrastructure review |
| **SRE** | `playbooks/by-role/sre.md` | Observability, SLOs, incident patterns, runbooks |
| **Security Engineer** | `playbooks/by-role/security-engineer.md` | Security scan, OWASP checklist, auth/authz review |

### Architecture & Leadership Roles

| Role | File | Focus Areas |
|------|------|-------------|
| **Architect** | `playbooks/by-role/architect.md` | C4 diagrams, risk hotspots, tech debt, ADRs |
| **Tech Lead** | `playbooks/by-role/tech-lead.md` | Code review checklist, PR analysis, team conventions |
| **Engineering Manager** | `playbooks/by-role/engineering-manager.md` | Health metrics, velocity patterns, tech debt prioritization |

### Support Roles

| Role | File | Focus Areas |
|------|------|-------------|
| **DBA** | `playbooks/by-role/dba.md` | Schema analysis, query patterns, migration review |
| **Technical Writer** | `playbooks/by-role/technical-writer.md` | Doc audit, API docs, user guides |
| **Release Manager** | `playbooks/by-role/release-manager.md` | Release checklist, changelog, version strategy |
| **Support Engineer** | `playbooks/by-role/support-engineer.md` | Troubleshooting guides, FAQ generation, known issues |

---

## Quick Prompts by Role

### Product & Planning

```
# Product Owner
Read @GenDD-Flow/playbooks/by-role/product-owner.md
Analyze @TargetRepo for product insights.

# Business Analyst
Read @GenDD-Flow/playbooks/by-role/business-analyst.md
Analyze @TargetRepo for requirements and process flows.

# Scrum Master
Read @GenDD-Flow/playbooks/by-role/scrum-master.md
Analyze @TargetRepo and Jira workflows for delivery flow and coordination risks.

# UX Designer
Read @GenDD-Flow/playbooks/by-role/ux-designer.md
Analyze @TargetRepo for UI patterns and accessibility.
```

### Development

```
# Frontend Developer
Read @GenDD-Flow/playbooks/by-role/frontend-dev.md
Analyze @TargetRepo for frontend patterns and conventions.

# Backend Developer
Read @GenDD-Flow/playbooks/by-role/backend-dev.md
Analyze @TargetRepo for backend patterns and conventions.

# Full-Stack Developer
Read @GenDD-Flow/playbooks/by-role/fullstack-dev.md
Analyze @TargetRepo for end-to-end patterns.
```

### Quality

```
# QA Engineer
Read @GenDD-Flow/playbooks/by-role/qa-engineer.md
Analyze @TargetRepo for test gaps and coverage.

# QA Automation Engineer
Read @GenDD-Flow/playbooks/by-role/qa-automation.md
Analyze @TargetRepo for test automation opportunities.
```

### Operations

```
# DevOps Engineer
Read @GenDD-Flow/playbooks/by-role/devops-engineer.md
Analyze @TargetRepo for CI/CD and deployment patterns.

# SRE
Read @GenDD-Flow/playbooks/by-role/sre.md
Analyze @TargetRepo for observability and reliability.

# Security Engineer
Read @GenDD-Flow/playbooks/by-role/security-engineer.md
Analyze @TargetRepo for security posture.
```

### Architecture & Leadership

```
# Architect
Read @GenDD-Flow/playbooks/by-role/architect.md
Analyze @TargetRepo for architecture and technical debt.

# Tech Lead
Read @GenDD-Flow/playbooks/by-role/tech-lead.md
Analyze @TargetRepo for code quality and conventions.

# Engineering Manager
Read @GenDD-Flow/playbooks/by-role/engineering-manager.md
Analyze @TargetRepo for engineering health metrics.
```

### Support

```
# DBA
Read @GenDD-Flow/playbooks/by-role/dba.md
Analyze @TargetRepo for database patterns and health.

# Technical Writer
Read @GenDD-Flow/playbooks/by-role/technical-writer.md
Analyze @TargetRepo for documentation gaps.

# Release Manager
Read @GenDD-Flow/playbooks/by-role/release-manager.md
Analyze @TargetRepo for release readiness.

# Support Engineer
Read @GenDD-Flow/playbooks/by-role/support-engineer.md
Analyze @TargetRepo for supportability and troubleshooting.
```

---

## Combining Playbooks

For complex scenarios, combine multiple playbooks:

### New Team Member Onboarding
```
# Run in sequence:
1. Run playbooks/onboarding/run-brownfield-analysis.md (Pass 1-2 only)
2. Read @GenDD-Flow/playbooks/by-role/{their-role}.md
3. Create onboarding checklist from outputs
```

### Pre-Release Audit
```
# Run in parallel:
- Read @GenDD-Flow/playbooks/by-role/qa-engineer.md
- Read @GenDD-Flow/playbooks/by-role/security-engineer.md
- Read @GenDD-Flow/playbooks/by-role/release-manager.md
```

### Technical Debt Sprint
```
# Run in sequence:
1. Read @GenDD-Flow/playbooks/by-role/architect.md
2. Read @GenDD-Flow/playbooks/by-role/tech-lead.md
3. Read @GenDD-Flow/playbooks/by-role/engineering-manager.md
4. Prioritize identified debt items
```

### API Contract Review
```
# Run in sequence:
1. Read @GenDD-Flow/playbooks/by-role/architect.md
2. Read @GenDD-Flow/playbooks/by-role/backend-dev.md
3. Read @GenDD-Flow/playbooks/by-role/technical-writer.md (for API docs)
```

### Repository AI Setup (Context Pack + Architecture)
```
# Run in sequence:
1. Read @GenDD-Flow/workflows/create-context-pack.md → Generate .cursor/ context files
2. Read @GenDD-Flow/workflows/generate-architecture-diagrams.md → Generate C4 diagrams
3. architecture.md will reference the C4 diagrams generated in step 2
```

### Post-Architecture Change
```
# Run in sequence:
1. Read @GenDD-Flow/playbooks/on-demand/run-delta-analysis.md (assess impact)
2. Read @GenDD-Flow/workflows/generate-architecture-diagrams.md (update C4 diagrams)
3. Read @GenDD-Flow/playbooks/recurring/refresh-context-pack.md (update architecture.md)
```

---

## Troubleshooting

### Which playbook for my situation?

| Symptom | Recommended Playbook |
|---------|---------------------|
| "I don't understand this codebase" | [Run Full Analysis](onboarding/run-full-analysis.md) |
| "I need to document my changes" | [Delta Analysis](on-demand/run-delta-analysis.md) |
| "I'm switching IDEs" | [Generate IDE Rules](on-demand/generate-ide-rules.md) |
| "I need standards for my team" | [Generate Standards](on-demand/generate-standards.md) |
| "Context is outdated" | [Refresh Context Areas](recurring/refresh-context-areas.md) |
| "I'm reviewing a PR" | Tech Lead Playbook |
| "Delivery feels blocked or unpredictable" | Scrum Master Playbook |
| "I need to find test gaps" | QA Engineer Playbook |
| "I have Gherkin ACs and need tests" | Generate Tests from Gherkin Workflow |
| "I'm worried about security" | Security Engineer Playbook |
| "I need to deploy this" | DevOps Engineer Playbook |
| "I need architecture diagrams" | Architect Playbook + [Generate Architecture Diagrams](../workflows/generate-architecture-diagrams.md) |
| "AI keeps generating wrong patterns" | [Refresh Context Areas](recurring/refresh-context-areas.md) or [Generate IDE Rules](on-demand/generate-ide-rules.md) |
| "Documentation is outdated" | Technical Writer Playbook |

### Story Quality Issues

| Symptom | Root Cause | Recommended Action |
|---------|------------|-------------------|
| "Stories keep getting reopened" | Weak DoR enforcement | Scrum Master Playbook → DoR checklist |
| "QA discovers requirements via bugs" | ACs missing or vague | Business Analyst Playbook → AC enhancement |
| "Security blocks us late in sprint" | Security not flagged early | Product Owner Playbook → Epic/Story flags |
| "Integration surprises during dev" | Integration impact not identified | Architect Playbook → Dependency analysis |
| "We can't agree when something is done" | DoD not aligned | Scrum Master Playbook → DoD checklist |
| "ACs aren't testable" | ACs describe implementation, not behavior | QA Engineer Playbook → AC testability |

### DoR/DoD Enforcement

| Issue | Playbook | Phase |
|-------|----------|-------|
| Stories entering sprints unprepared | Scrum Master | Phase 2: Work Entry & Readiness |
| ACs in wrong field | Business Analyst | Story Crafting Standards |
| Missing integration flags | Architect | Phase 3: Dependency Analysis |
| Missing security flags | Product Owner | Epic/Story Quality Inputs |
| No test evidence for Done | QA Engineer | Phase 6: AC Testability |
| Automation deferred without reason | Tech Lead | DoD Technical Verification |

### Context window getting full?

1. Run playbooks in separate chat sessions
2. Save intermediate outputs to `@TargetRepo/docs/playbook-outputs/`
3. Reference saved outputs in subsequent playbooks

### Output not actionable?

1. Provide more context about your tech stack
2. Specify exact areas of concern
3. Reference specific files: `@TargetRepo/src/services/PaymentService.cs`

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| `002_Story Templates.docx` | Epic, Story, and Bug templates |
| `003_Definition of Ready_Definition of Done.docx` | DoR/DoD checklists and standards |
| `workflows/create-context-pack.md` | Create AI context files (agents.md, context.md, conventions.md, testing.md, architecture.md) |
| `workflows/generate-architecture-diagrams.md` | Generate C4 architecture diagrams (Context, Container, Component, Deployment) |
| `workflows/enhance-acceptance-criteria.md` | Shift-left story quality workflow |
| `workflows/generate-tests-from-gherkin.md` | Generate test suites from Gherkin ACs |
| [QUICK-START.md](../QUICK-START.md) | Copy-paste prompts |
| [README.md](../README.md) | Framework overview |
| [templates/documentation-guidelines.md](../templates/documentation-guidelines.md) | Output formatting rules |
