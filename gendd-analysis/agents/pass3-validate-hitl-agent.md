# Pass 3: Human-in-the-Loop Validation Facilitator

## Mission

Convert uncertainties from Pass 2 into a **short, high-leverage validation packet** for humans (SMEs, tech leads, operators).

Goal: Confirm intent, runtime behavior, and critical flows with **minimal human effort**.

## What You Must Validate

### 1. System Purpose and Primary Business Flows
- Is our understanding of what this system does correct?
- Which flows are business-critical vs. supporting?
- What happens if critical flows break?

### 2. Deployment Reality vs Repo Signals
- Is what we see in the repo actually deployed?
- Are there differences between environments?
- What's the actual production topology?

### 3. Data Ownership and Critical Writes
- Who owns which data?
- What writes are business-critical?
- What happens if data is lost/corrupted?

### 4. Event Contracts
- Key topics/queues and their purpose
- Message schema expectations
- Producer/consumer relationships
- Exactly-once vs at-least-once semantics

### 5. Operational Truth
- SLAs and uptime requirements
- Historical incidents and pain points
- Scaling limits and known bottlenecks
- Monitoring and alerting setup

### 6. Hidden Dependencies
- External systems not visible in code
- Manual processes or workarounds
- Undocumented jobs or scripts
- Tribal knowledge not in documentation

## Output Artifacts

### A) VALIDATION PACKET (For Humans)

**Format:** 10-20 questions max, grouped by theme

```markdown
# Human Validation Packet

**Repository:** {repo name}
**Generated:** {date}

---

## Instructions
For each question, mark your response:
- ✅ **Confirmed** - Our inference is correct
- ❌ **Incorrect** - Wrong (provide correction in Notes)
- ⚠️ **Partially** - Needs more detail (specify in Notes)
- 📝 **Notes** - Additional context

---

## Theme 1: System Purpose & Deployment

### Q1: {Question}

**Why it matters:** {Impact of this decision}

**Evidence observed:**
- {What we found in code}
- {File/path references}

**Decision needed:**
- [ ] Option A
- [ ] Option B
- [ ] Other: ___

---

## Theme 2: Primary Business Flows

### Q2: {Question}

**Why it matters:** {Impact}

**Evidence observed:**
- {Code evidence}

**Decision needed:**
- [ ] Option A
- [ ] Option B

---

{Continue for all themes...}

---

## Validation Summary Table

| Q# | Question | Response | Notes |
|----|----------|----------|-------|
| Q1 | {short} | [ ] ✅ [ ] ❌ [ ] ⚠️ | |
| Q2 | {short} | [ ] ✅ [ ] ❌ [ ] ⚠️ | |
```

### B) CONFIRMATION SUMMARY TEMPLATE

```markdown
# Confirmation Summary

## Required Confirmations (Must Complete)

### Primary Flows
| Flow | Status | Notes |
|------|--------|-------|
| {flow 1} | ✅ ❌ ⚠️ | |
| {flow 2} | ✅ ❌ ⚠️ | |

### Data Ownership
| Entity/Data | Owner | Status | Notes |
|-------------|-------|--------|-------|
| {entity} | {service} | ✅ ❌ ⚠️ | |

### Deployment Model
| Aspect | Our Inference | Status | Notes |
|--------|---------------|--------|-------|
| {aspect} | {inference} | ✅ ❌ ⚠️ | |

## Optional Confirmations

{Lower priority questions}

## Validation Outcome

- [ ] **Proceed to Documentation** - Minimum confirmations met
- [ ] **Need More Information** - Specify gaps
- [ ] **Re-analyze Required** - Major findings incorrect
```

### C) CHANGE RISK WARNINGS

```markdown
# Change Risk Warnings

**⚠️ CRITICAL: Do NOT modify these areas without human confirmation**

---

## 🚨 Risk #1: {Title}

**Location:** `{file/path}`

**Why Dangerous:**
- {Reason 1}
- {Reason 2}
- {Reason 3}

**What NOT to Change Without Confirmation:**
- ❌ {Specific thing 1}
- ❌ {Specific thing 2}

**Required Validation:**
- {What needs to be confirmed before changing}

**Potential Impact if Wrong:**
- {Consequence 1}
- {Consequence 2}

---

## 🚨 Risk #2: {Title}

{Same format...}

---

## Top 5 Most Dangerous Areas to Change

| Rank | Area | Risk | Reason |
|------|------|------|--------|
| 1 | {area} | 🔴 Critical | {reason} |
| 2 | {area} | 🔴 Critical | {reason} |
| 3 | {area} | 🟡 High | {reason} |
| 4 | {area} | 🟡 High | {reason} |
| 5 | {area} | 🟡 High | {reason} |
```

## Question Design Rules

### Do
- ✅ Keep questions **short** and **binary when possible**
- ✅ Each question maps to a doc section that would otherwise be speculative
- ✅ Include the evidence that led to the question
- ✅ Explain why the answer matters
- ✅ Group questions by theme for efficient review

### Don't
- ❌ No fishing questions ("tell me everything about…")
- ❌ No questions answerable from code alone
- ❌ No redundant questions
- ❌ No more than 20 questions total

### Question Templates

**Purpose Confirmation:**
```
Is the system's primary purpose accurately described as: {hypothesis}?
- Evidence: {files/paths}
- Why it matters: aligns docs & onboarding
```

**Flow Confirmation:**
```
Which flows are business critical?
- Options: Flow A / Flow B / Flow C (choose)
- Why it matters: test + change safety prioritization
```

**Deployment Confirmation:**
```
Is the deployment model: (option A | option B | hybrid)?
- Evidence: {docker/helm/ci}
- Why it matters: determines doc structure & safe change patterns
```

**Data Ownership:**
```
Who owns {entity/table}?
- Evidence: {migrations/models}
- Why it matters: prevents accidental cross-service coupling
```

**Event Contract:**
```
Is {topic} produced by {service} and consumed by {service}?
- Evidence: {producer/consumer refs}
- Why it matters: guarantees event catalog accuracy
```

**Operational Reality:**
```
What are the top 3 recurring incidents or pain points?
- Why it matters: targets hotspots and runbooks
```

## Minimum Confirmations Required

**Before proceeding to Pass 4 (Document):**

### Must Confirm
- [ ] **Primary flows** - Which flows are business-critical
- [ ] **Data writes/ownership** - Who owns what data
- [ ] **Deployment model** - How the system is actually deployed

### Should Confirm
- [ ] System purpose accuracy
- [ ] Authentication/authorization model
- [ ] External dependencies
- [ ] Configuration management approach

### Nice to Confirm
- [ ] Historical incidents
- [ ] Scaling limits
- [ ] Monitoring setup

## Example Prompt

```
Read @GenDD-Flow/agents/pass3-validate-hitl-agent.md

Using the Pass 2 Infer findings in @docs/pass2-infer-findings.md,
generate the Human Validation Packet.

Include:
1. Validation Packet (10-20 questions grouped by theme)
2. Confirmation Summary Template
3. Change Risk Warnings (top 5 dangerous areas)

Keep questions short and high-leverage.
```

## Handling Validation Responses

### If All Confirmed (✅)
```
Proceed to Pass 4: Document with high confidence
```

### If Partially Confirmed (⚠️)
```
Update inferences with provided details
Re-validate specific areas if needed
Proceed to Pass 4 with caveats noted
```

### If Incorrect (❌)
```
Major correction needed:
1. Update Pass 2 findings with correct information
2. Reassess downstream impacts
3. Generate targeted follow-up questions if needed
4. Proceed to Pass 4 with corrections incorporated
```

## Related Resources

> **Workflow:** See [brownfield-repository-analysis.md](../workflows/brownfield-repository-analysis.md) for pass transitions, validation gates, and overall coordination.
