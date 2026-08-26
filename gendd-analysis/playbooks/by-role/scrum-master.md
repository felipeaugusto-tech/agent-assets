# Role Playbook: Scrum Master

**Role:** Scrum Master (Functional Role)  
**Focus:** Delivery flow, coordination, bottleneck detection, execution hygiene, DoR/DoD enforcement  
**Time:** Continuous (embedded in delivery)

---

## Purpose

Analyze delivery execution from a Scrum Master perspective to:

- Make delivery flow visible and predictable
- Surface readiness gaps before work starts
- Identify bottlenecks across Jira, QA, and Release
- Expose systemic rework drivers (reopens, churn)
- Enforce Definition of Ready and Definition of Done
- Prepare teams for AI-assisted delivery (GenDD)

> At {ORGANIZATION}, this role exists **by function, not by title**, and is typically exercised by **Product Managers and Team Leads**.

---

## {ORGANIZATION} Definition of Ready/Done Standards

> **Reference:** This playbook aligns with {ORGANIZATION}'s **Definition of Ready (DoR)** and **Definition of Done (DoD)** standards.

### Definition of Ready (DoR) Checklist

A story is "Ready for Development" when it can be implemented without discovering the problem during the sprint:

| Readiness Criterion | Check | Notes |
|---------------------|-------|-------|
| Clear problem statement exists | [ ] | What is being solved and why |
| Acceptance Criteria in dedicated AC field | [ ] | Not in Description or comments |
| ACs describe expected behavior | [ ] | Not implementation steps |
| Scope boundaries are clear | [ ] | In scope / Out of scope defined |
| Integration impact identified | [ ] | Yes / No flag |
| Security review need identified | [ ] | Yes / No flag |
| Environment/data dependencies identified | [ ] | Specific requirements noted |
| Test data scenarios called out | [ ] | When applicable |
| Unknowns explicitly documented | [ ] | "Unknown" is OK; "Implicit" is not |

**Use DoR as a conversation checklist during refinement.**

### Definition of Done (DoD) Checklist

A story is "Done" when the agreed behavior has been validated, not just implemented:

| Done Criterion | Check | Notes |
|----------------|-------|-------|
| All Acceptance Criteria validated | [ ] | Verified against ACs |
| Expected behavior verified | [ ] | Not inferred |
| No known critical defects remain open | [ ] | Blocking issues resolved |
| Security concerns addressed or approved | [ ] | From earlier identification |
| Integration behavior verified | [ ] | Where applicable |
| Test evidence exists | [ ] | Manual or automated |
| User-visible changes documented | [ ] | Release notes or equivalent |
| Automation coverage addressed | [ ] | Implemented or deferred with reason |

**Use DoD as a shared agreement, not a gate.**

### Common Failure Modes This Addresses

- Stories entering sprints with "six bullet points"
- QA discovering requirements via bugs
- Security blocking work late in the sprint
- Reverts caused by undocumented integration behavior
- Metrics showing progress while rework grows

---

## Quick Prompt

```

Read @GenDD-Flow/playbooks/by-role/scrum-master.md
Analyze @TargetRepo and Jira workflows for delivery flow and coordination risks.

```

---

## Full Analysis Prompt

```

Read @GenDD-Flow/playbooks/by-role/scrum-master.md

Analyze delivery execution from a Scrum Master perspective:

## Context

* Team / Product Area: [NAME]
* Jira Board: [BOARD NAME / LINK]
* Delivery Model: [Scrum | Hybrid | Compliance-driven Agile]
* Release Cadence: [Weekly / Bi-weekly / On-demand]
* Primary Constraints: [QA / Compliance / Architecture / Environments]

## Phase 1: Flow Ownership Mapping

Identify who actually owns delivery control points:

| Flow Area          | Owner in Practice | Evidence |
| ------------------ | ----------------- | -------- |
| Sprint commitments |                   |          |
| Backlog readiness  |                   |          |
| Daily unblocking   |                   |          |
| QA gating          |                   |          |
| Release approval   |                   |          |

Flag ownership gaps or overlaps.

## Phase 2: Work Entry & Readiness

Assess how work enters development against {ORGANIZATION} DoR standards:

* Is Definition of Ready enforced? (Yes / Weak / No)
* Do stories start with missing ACs or edge cases?
* Who compensates when requirements are vague?
* Are ACs in the dedicated field or scattered in Description/comments?

Generate:

| Readiness Signal            | Current State | DoR Alignment | Delivery Impact |
| --------------------------- | ------------- | ------------- | --------------- |
| Problem statement clarity   |               | Required      |                 |
| Acceptance Criteria in AC field |           | Required      |                 |
| ACs describe behavior (not steps) |         | Required      |                 |
| Scope boundaries defined    |               | Required      |                 |
| Integration impact flagged  |               | Required      |                 |
| Security review need flagged |              | Required      |                 |
| Test data/environment deps  |               | When applicable |               |
| Unknowns explicitly documented |            | Required      |                 |

### Readiness Gap Analysis

| Gap Type | Frequency | Who Compensates | Rework Cost |
|----------|-----------|-----------------|-------------|
| Missing ACs | [%] | QA/Engineering | High |
| Vague scope | [%] | Tech Lead | Medium |
| Undocumented integrations | [%] | Senior devs | High |
| "See STR" patterns | [%] | QA | High |

## Phase 3: Ceremony Effectiveness

Evaluate ceremonies by outcomes, not attendance:

| Ceremony      | Facilitator | Actual Output | Risk if Missing |
| ------------- | ----------- | ------------- | --------------- |
| Planning      |             |               |                 |
| Refinement    |             |               |                 |
| Daily         |             |               |                 |
| Review        |             |               |                 |
| Retrospective |             |               |                 |

Identify which ceremony acts as the last safeguard against unclear work.

## Phase 4: Jira Flow & Control

Analyze Jira as an execution system:

| Aspect                | Observed Behavior | Risk |
| --------------------- | ----------------- | ---- |
| Ticket movement       |                   |      |
| Blocking behavior     |                   |      |
| Reopen patterns       |                   |      |
| DoR / DoD enforcement |                   |      |

Classify Jira usage:

* [ ] Backlog tracker
* [ ] Coordination tool
* [ ] Governance mechanism
* [ ] Metric system

## Phase 5: Bottlenecks & Queues

Identify where work queues up:

| Handoff                    | Severity | Root Cause |
| -------------------------- | -------- | ---------- |
| Product → Engineering      |          |            |
| Engineering → QA           |          |            |
| QA → Release               |          |            |
| Engineering → Architecture |          |            |

Distinguish Scrum Master interventions vs structural issues.

## Phase 6: Metrics That Drive Action

Identify metrics that trigger real decisions:

| Metric           | Reviewed By | Action Taken |
| ---------------- | ----------- | ------------ |
| Defect leakage   |             |              |
| Reopen rate      |             |              |
| Velocity         |             |              |
| Release failures |             |              |

Separate signal metrics from reporting-only metrics.

## Phase 7: AI & GenDD Readiness

Assess delivery governance with AI in the loop:

| Area                     | Current State | Risk |
| ------------------------ | ------------- | ---- |
| AI usage consistency     |               |      |
| Context provided to AI   |               |      |
| Prompt / template reuse  |               |      |
| Human-in-the-loop checks |               |      |

Identify missing ownership for AI guardrails.

## Phase 8: Authority & Escalation

Clarify decision boundaries:

| Conflict               | Resolution Path |
| ---------------------- | --------------- |
| Speed vs Quality       |                 |
| Product vs Tech risk   |                 |
| Compliance vs Delivery |                 |

Document where Scrum Master influence ends.

## Phase 9: Recommendations

| Area          | Recommendation | Priority |
| ------------- | -------------- | -------- |
| Flow          |                | P1/P2/P3 |
| Readiness     |                | P1/P2/P3 |
| QA / Release  |                | P1/P2/P3 |
| AI governance |                | P1/P2/P3 |

```

---

## Output: Delivery Flow Assessment

```

# Delivery Flow Assessment: [Team / Product]

Generated: [Date]
Analyzed by: Scrum Master Playbook

## Execution Summary

[High-level delivery health and primary risks]

## Flow Ownership Gaps

[Missing or unclear ownership]

## Readiness & Rework Signals

[Where unclear work causes churn]

## Bottleneck Summary

[Queues and constraints]

## Metric Signals

[Metrics that actually drive behavior]

## AI & GenDD Exposure

[Current risk assessment]

## Recommendations

### Priority 1

* [Action]

### Priority 2

* [Action]

### Priority 3

* [Action]

```

---

## Follow-Up Actions

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
