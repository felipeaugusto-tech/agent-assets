# Role Playbook: Product Owner

**Role:** Product Owner
**Focus:** Backlog analysis, story prioritization, value mapping, feature inventory, work readiness
**Time:** 30-60 minutes

---

## Purpose

Analyze a codebase from the Product Owner perspective to understand:
- What features exist and their business value
- Backlog opportunities from technical debt
- User journey coverage gaps
- Feature completeness vs. roadmap
- Story and Epic quality for delivery readiness

---

## {ORGANIZATION} Story & Epic Standards

> **Reference:** This playbook aligns with {ORGANIZATION}'s **Story Templates** and **Definition of Ready/Done** standards.

### Epic Creation Checklist

When creating Epics, ensure these fields are complete:

| Field | Description | Required |
|-------|-------------|----------|
| **Business Capability** | What business problem or capability is being delivered? Link to Aha! if applicable | Yes |
| **Success Metrics** | How will we know this was successful? (e.g., reduced defects, faster flow, customer impact) | Yes |
| **In Scope / Out of Scope** | Clear boundaries to prevent scope creep | Yes |
| **Integration Impact** | External systems involved (Skyward, Qmlativ, Powerschool, etc.) - Yes/No/Unknown | Yes |
| **Architecture Impact** | New flow or modification to existing flow? Link to C4 diagram if available | Recommended |
| **Security/Compliance** | PCI / PII / Auth / Payments involved? (Yes/No) | Yes |

### User Story Quality Inputs

Product Owners are responsible for providing story inputs that enable Definition of Ready:

| Input | Guidance |
|-------|----------|
| **Problem Statement** | Clear articulation of what is being solved and why |
| **User Story Statement** | As a [user/role], I want [capability], So that [business value] |
| **Context & References** | Figma links, API/DB references, related Epic, current source of truth (code path, SME) |
| **Scope Boundaries** | What is in scope / out of scope for this story |
| **Integration Impact** | External integration involved? (Yes/No) |
| **Security Review Need** | Security review required? (Yes/No) |

### Definition of Ready Ownership

A story is "Ready for Development" when it can be implemented without discovering the problem during the sprint. Product Owners ensure:

- [ ] Clear problem statement exists (what is being solved and why)
- [ ] Acceptance Criteria are present in the dedicated AC field
- [ ] ACs describe expected behavior (not implementation steps)
- [ ] Scope boundaries are clear (what is in / out)
- [ ] Integration impact is identified (Yes / No)
- [ ] Security review need is identified (Yes / No)
- [ ] Environment, configuration, or data dependencies are identified
- [ ] Unknowns or assumptions are explicitly documented

> **Important:** "Unknown" is acceptable. "Implicit" is not.

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/product-owner.md
Analyze @TargetRepo for product insights.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/product-owner.md

Analyze @TargetRepo from a Product Owner perspective:

## Context
- Product: [PRODUCT NAME]
- Target Users: [USER PERSONAS]
- Business Domain: [DOMAIN - e.g., fintech, healthcare, e-commerce]

## Phase 1: Feature Inventory

Identify all features by analyzing:
- API endpoints and their purposes
- UI components and pages
- Business logic services
- User-facing functionality

Generate:
| Feature | Description | User Value | Technical Health |
|---------|-------------|------------|------------------|
| [Feature] | [What it does] | High/Med/Low | Good/Needs Work/Poor |

## Phase 2: User Journey Mapping

For each identified user persona:
1. Map the complete user journey through the system
2. Identify gaps or friction points
3. Note incomplete flows

| Journey | Steps | Gaps | Priority |
|---------|-------|------|----------|
| [Journey name] | [Steps count] | [Missing pieces] | P1/P2/P3 |

## Phase 3: Business Value Analysis

Assess each major component:
| Component | Business Value | User Impact | Revenue Impact |
|-----------|---------------|-------------|----------------|
| [Component] | High/Med/Low | [Description] | Direct/Indirect/None |

## Phase 4: Technical Debt as Backlog Items

Convert identified technical debt to product backlog:
| Technical Debt | User Impact | Story | Priority |
|----------------|-------------|-------|----------|
| [Debt item] | [How users are affected] | [User story format] | P1/P2/P3 |

## Phase 5: Roadmap Gaps

Based on common patterns for [DOMAIN]:
| Expected Feature | Current State | Gap | Effort Estimate |
|------------------|---------------|-----|-----------------|
| [Industry standard feature] | Present/Partial/Missing | [What's missing] | S/M/L/XL |

## Phase 6: Story Readiness Assessment

Evaluate backlog readiness against Definition of Ready:

| Story | Problem Statement | ACs in Field | Scope Clear | Integration ID'd | Security ID'd | Ready? |
|-------|-------------------|--------------|-------------|------------------|---------------|--------|
| [Story] | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No |

### Common Readiness Failures
- [ ] Stories entering sprints with "six bullet points" in description
- [ ] Acceptance Criteria in Description or comments (not AC field)
- [ ] "See STR" without expected behavior defined
- [ ] Integration logic known only by individuals
- [ ] Security requirements discovered late

## Phase 7: Epic Quality Audit

For existing Epics, verify completeness:

| Epic | Business Capability | Success Metrics | Scope Defined | Integration Impact | Security Flags |
|------|---------------------|-----------------|---------------|--------------------| ---------------|
| [Epic] | Present/Missing | Present/Missing | Clear/Vague | Yes/No/Unknown | Yes/No |

## Phase 8: Recommendations

Priority matrix for product decisions:
| Opportunity | Value | Effort | Recommendation |
|-------------|-------|--------|----------------|
| [Opportunity] | High/Med/Low | S/M/L/XL | Do Now/Plan/Backlog/Skip |

### Story Quality Improvements
| Issue | Stories Affected | Recommended Fix | Priority |
|-------|------------------|-----------------|----------|
| Missing ACs | [count] | Use Gherkin format in AC field | P1 |
| No scope boundaries | [count] | Add In/Out of Scope section | P1 |
| Undocumented integrations | [count] | Add Integration Impact flag | P2 |
```

---

## Output: Product Insights Report

```markdown
# Product Insights: [Product Name]
Generated: [Date]
Analyzed by: Product Owner Playbook

## Executive Summary
[2-3 sentences on product state and key opportunities]

## Feature Inventory
[Table of all features with value assessment]

## User Journey Analysis
[Journey maps with gaps identified]

## Value-Effort Matrix

        HIGH VALUE
            │
  Quick     │    Strategic
  Wins      │    Priorities
            │
────────────┼───────────────
            │
  Fill-Ins  │    Consider
            │    Later
            │
        LOW VALUE
    LOW EFFORT    HIGH EFFORT

## Top Backlog Recommendations
1. [Item] - [Rationale]
2. [Item] - [Rationale]
3. [Item] - [Rationale]

## Technical Debt Impact on Users
[How tech debt affects user experience]

## Roadmap Alignment
[Gaps vs. industry standards]
```

---

## Follow-Up Actions

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
