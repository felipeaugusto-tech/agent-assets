# Template: Human-in-the-Loop Validation Packet

**Purpose:** Resolve ambiguity and get human sign-off BEFORE creating Jira tickets or documentation.

---

## When to Use

- Before creating Jira Epics/Tasks for a new feature
- Before generating technical documentation
- When requirements have multiple valid interpretations
- When technical decisions have significant trade-offs
- When integration impacts are unclear

---

## Validation Packet Structure

Generate the following sections for each feature:

### 1. FEATURE SUMMARY

```markdown
## Feature Summary

**Feature Name:** [Clear, descriptive name]
**Requester:** [Who requested this]
**Target Repository:** [Repository path]
**Priority:** [High/Medium/Low]

**One-Line Description:**
[Single sentence describing what this feature does]

**Business Value:**
[Why this feature matters to users/business]
```

### 2. SCOPE VALIDATION

```markdown
## Scope Validation

### In Scope (MUST complete for this feature)
- [ ] [Capability 1]
- [ ] [Capability 2]
- [ ] [Capability 3]

### Out of Scope (Future phases/separate tickets)
- [ ] [Deferred capability 1]
- [ ] [Deferred capability 2]

### Scope Questions Requiring Human Decision

| Question | Options | AI Recommendation | Your Decision |
|----------|---------|-------------------|---------------|
| Should [X] be included? | Yes / No / Phase 2 | [Recommendation with reasoning] | ☐ |
| What is the minimum viable version? | Option A / Option B | [Recommendation] | ☐ |
| Should we support [edge case]? | Yes / No / Later | [Recommendation] | ☐ |
```

### 3. TECHNICAL AMBIGUITY RESOLUTION

```markdown
## Technical Ambiguities

### Ambiguity 1: [Title]

**Question:** [What is unclear]

**Options:**
| Option | Pros | Cons | Effort |
|--------|------|------|--------|
| A: [Description] | [Benefits] | [Drawbacks] | [T-shirt size] |
| B: [Description] | [Benefits] | [Drawbacks] | [T-shirt size] |
| C: [Description] | [Benefits] | [Drawbacks] | [T-shirt size] |

**AI Recommendation:** Option [X] because [reasoning]

**Your Decision:** ☐ Option A  ☐ Option B  ☐ Option C  ☐ Other: _______

---

### Ambiguity 2: [Title]
[Same format]
```

### 4. ARCHITECTURE DECISION POINTS

```markdown
## Architecture Decisions

### Decision 1: [Title - e.g., "Service Placement"]

**Context:** [Why this decision matters]

**Options:**
1. **[Option A]:** [Description]
   - Impact: [What changes]
   - Risk: [Potential issues]
   
2. **[Option B]:** [Description]
   - Impact: [What changes]
   - Risk: [Potential issues]

**Recommendation:** [Option X] because [reasoning]

**Decision:** ☐ Option 1  ☐ Option 2  ☐ Needs Discussion

---

### Decision 2: [Database Schema]
[Same format]
```

### 5. INTEGRATION IMPACT ASSESSMENT

```markdown
## Integration Impact Assessment

### Affected Systems

| System/Service | Impact Type | Risk Level | Confirmed? |
|---------------|-------------|------------|------------|
| [Service A] | API Change / Schema Change / None | High/Med/Low | ☐ Yes ☐ No |
| [Service B] | API Change / Schema Change / None | High/Med/Low | ☐ Yes ☐ No |
| [Database X] | New Tables / Modified Tables / None | High/Med/Low | ☐ Yes ☐ No |
| [External API] | New Integration / Modified / None | High/Med/Low | ☐ Yes ☐ No |

### Breaking Changes

| Change | Affected Consumers | Migration Plan | Approved? |
|--------|-------------------|----------------|-----------|
| [Change 1] | [List of consumers] | [How to migrate] | ☐ Yes ☐ No |

### Dependencies

| Dependency | Status | Blocking? |
|------------|--------|-----------|
| [Team/System A must complete X] | Ready / In Progress / Not Started | ☐ Yes ☐ No |
```

### 6. ACCEPTANCE CRITERIA VALIDATION

```markdown
## Acceptance Criteria Review

Review each generated AC and approve or modify:

### AC1: [Title]
```gherkin
GIVEN [precondition]
WHEN [action]
THEN [expected outcome]
```

**Validation:**
- ☐ Approved as-is
- ☐ Needs modification: ________________________________
- ☐ Remove (out of scope)

---

### AC2: [Title]
[Same format for each AC]

---

### Missing ACs

Are there any scenarios not covered above?

| Scenario | Should be added? |
|----------|------------------|
| [Edge case 1] | ☐ Yes ☐ No |
| [Edge case 2] | ☐ Yes ☐ No |
```

### 7. NON-FUNCTIONAL REQUIREMENTS

```markdown
## Non-Functional Requirements Validation

| NFR Category | Proposed Target | Achievable? | Adjusted Target |
|--------------|-----------------|-------------|-----------------|
| Performance | [e.g., <200ms p95] | ☐ Yes ☐ No | _____________ |
| Availability | [e.g., 99.9%] | ☐ Yes ☐ No | _____________ |
| Security | [e.g., PCI compliant] | ☐ Yes ☐ No | _____________ |
| Scalability | [e.g., 10K users] | ☐ Yes ☐ No | _____________ |
| Accessibility | [e.g., WCAG 2.1 AA] | ☐ Yes ☐ No | _____________ |
```

### 8. RISK ACKNOWLEDGMENT

```markdown
## Risk Acknowledgment

### Identified Risks

| Risk | Likelihood | Impact | Mitigation | Acknowledged? |
|------|------------|--------|------------|---------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [How to mitigate] | ☐ Yes |
| [Risk 2] | High/Med/Low | High/Med/Low | [How to mitigate] | ☐ Yes |
| [Risk 3] | High/Med/Low | High/Med/Low | [How to mitigate] | ☐ Yes |

### High-Risk Areas Requiring Extra Review

- [ ] [Area 1]: [Why it's risky]
- [ ] [Area 2]: [Why it's risky]
```

### 9. QUESTIONS REQUIRING HUMAN INPUT

```markdown
## Questions Requiring Human Input

⚠️ **These questions MUST be answered before proceeding to Jira/Documentation creation.**

### Business Questions

1. **[Question about business logic]**
   - Context: [Why this matters]
   - Options: [A, B, C]
   - Answer: _________________________________

2. **[Question about user experience]**
   - Context: [Why this matters]
   - Answer: _________________________________

### Technical Questions

3. **[Question about implementation approach]**
   - Context: [Trade-offs involved]
   - Answer: _________________________________

4. **[Question about data handling]**
   - Context: [Compliance/security implications]
   - Answer: _________________________________

### Compliance/Security Questions

5. **[Question about regulatory requirements]**
   - Context: [What regulations apply]
   - Answer: _________________________________
```

### 10. SIGN-OFF

```markdown
## Sign-Off

### Validation Complete

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Product Owner | | | ☐ Approved |
| Tech Lead | | | ☐ Approved |
| Security (if applicable) | | | ☐ Approved |

### Proceed to Next Phase

☐ **All questions answered**
☐ **All ambiguities resolved**
☐ **All risks acknowledged**
☐ **Scope confirmed**

**Ready to create Jira tickets:** ☐ Yes ☐ No (reason: _____________)

**Ready to create documentation:** ☐ Yes ☐ No (reason: _____________)
```

---

## Example Prompt

```
Read @GenDD-Flow/templates/validation-packet.md

Generate a Human-in-the-Loop Validation Packet for this feature:

Feature: "Enable churches to generate and send IRS-compliant annual giving statements to their donors"

Repository: @mono

Generate all sections:
1. Feature Summary
2. Scope Validation (what's in vs out)
3. Technical Ambiguities (at least 5)
4. Architecture Decision Points
5. Integration Impact Assessment
6. Acceptance Criteria Review
7. NFR Validation
8. Risk Acknowledgment
9. Questions Requiring Human Input (at least 5)
10. Sign-Off Template

Format as an interactive questionnaire that can be completed by stakeholders.
```

---

## Integration with Other Workflows

**Before Validation:**
- `workflows/enhance-acceptance-criteria.md` → Generate initial ACs

**After Validation Approved:**
- Framework 7: Create Jira Epic and Tasks
- Framework 7: Create Confluence Documentation
- `playbooks/on-demand/run-assisted-testing.md` → Generate E2E tests

---

## Tips for Effective Validation

1. **Don't skip this step** - Unclear requirements cause 3x rework
2. **Be specific** - Vague questions get vague answers
3. **Offer options** - Easier to choose than create from scratch
4. **Include recommendations** - AI suggestions speed up decisions
5. **Track decisions** - Checkboxes create accountability
6. **Time-box reviews** - Set deadline for validation completion
