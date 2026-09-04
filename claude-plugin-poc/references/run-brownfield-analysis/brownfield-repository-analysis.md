# Workflow: Brownfield Repository Analysis

## Context

Systematically analyze and document an existing (brownfield) repository that lacks current documentation. This workflow orchestrates a **4-pass analysis** to produce accurate documentation:

1. **Scan** - Rapid inventory of repository structure
2. **Infer** - Deduce architecture, flows, and data ownership
3. **Validate** - Human-in-the-Loop confirmation of hypotheses
4. **Document** - Produce comprehensive documentation pack

This addresses the common challenge of working with legacy systems, acquired codebases, or poorly documented repositories.

## Alignment with AI-in-SDLC Initiative

This workflow is **Framework 5** in {ORGANIZATION}'s AI-in-SDLC initiative. It enables understanding legacy systems before:
- Enhancement projects
- Migration efforts
- Documentation initiatives
- New team member onboarding
- Technical debt assessment

**How it feeds other frameworks:**

| Output | Feeds Into | Purpose |
|--------|------------|---------|
| Test Inventory | `workflows/identify-test-gaps.md` | Comprehensive test gap analysis |
| Architecture Hypotheses | `workflows/generate-architecture-diagrams.md` | Generate C4 diagrams |
| Documentation Pack | `workflows/create-context-pack.md` | Create AI context files |
| Core Flows | `workflows/enhance-acceptance-criteria.md` | Requirements for modifications |
| Integration Points | `workflows/automate-integration-testing.md` | Integration test generation |

## Prerequisites

- Access to the brownfield repository
- Cursor IDE with both GenDD-Flow and target repo in workspace
- 1-2 hours for full analysis (can be paused between passes)
- Access to a human validator (SME, tech lead, or original developer)

## Related Templates
- **`templates/documentation-guidelines.md`** - File references (not code snippets), multi-phase approach, size limits

## When to Use This Workflow

- **Inherited codebase** - Taking over a system from another team
- **Acquisition** - Integrating an acquired product
- **Legacy modernization** - Planning migration or updates
- **Missing documentation** - System exists but docs are stale/missing
- **New team member onboarding** - Creating documentation for future engineers
- **Technical debt assessment** - Understanding before refactoring

## Tooling Approach

**Cursor + repo-based Markdown context only.** No RAG, vector databases, embeddings, or additional platforms.

---

## Complete Workflow

### Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    BROWNFIELD ANALYSIS                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Pass 1: SCAN          Pass 2: INFER         Pass 3: VALIDATE  │
│   ┌─────────────┐       ┌─────────────┐       ┌─────────────┐   │
│   │ Inventory   │──────▶│ Hypotheses  │──────▶│ Human Q&A   │   │
│   │ Layout      │       │ Flows       │       │ Confirm     │   │
│   │ Entry Points│       │ Data Map    │       │ Correct     │   │
│   │ Dependencies│       │ Risks       │       │ Risk Warn   │   │
│   └─────────────┘       └─────────────┘       └─────────────┘   │
│         │                     │                     │           │
│         │                     │                     │           │
│         └─────────────────────┴─────────────────────┘           │
│                               │                                  │
│                               ▼                                  │
│                    ┌─────────────────────┐                      │
│                    │ Pass 4: DOCUMENT    │                      │
│                    │ ┌─────────────────┐ │                      │
│                    │ │ Executive Summary│ │                      │
│                    │ │ Architecture     │ │                      │
│                    │ │ Components       │ │                      │
│                    │ │ Flows            │ │                      │
│                    │ │ Onboarding       │ │                      │
│                    │ └─────────────────┘ │                      │
│                    └─────────────────────┘                      │
│                               │                                  │
│                               ▼                                  │
│                    ┌─────────────────────┐                      │
│                    │ FEED OTHER WORKFLOWS│                      │
│                    │ • Test Gaps         │                      │
│                    │ • C4 Diagrams       │                      │
│                    │ • Context Pack      │                      │
│                    └─────────────────────┘                      │
└─────────────────────────────────────────────────────────────────┘
```

### Flow Control Rules

#### Mandatory Validation Gates
1. **Do NOT proceed from Infer → Document** without at least one Human Validation checkpoint
2. **Force validation** if confidence < Medium on critical areas:
   - Authentication/Authorization
   - Payment/Financial processing
   - Data writes and ownership
   - Event producers/consumers
   - External integrations

#### Skip Conditions
- **Scan** cannot be skipped
- **Infer** cannot be skipped
- **Validate** can be minimal for non-production/tutorial systems
- **Document** can be scoped based on validation answers

### Operating Principles

#### Evidence-Based Analysis
- Prefer evidence from repository structure, dependency graphs, and code-level references
- Every finding must cite specific files, paths, or code patterns
- Distinguish between **FACTS** (confirmed by code) and **HYPOTHESES** (inferred)

#### Confidence Levels
- **High**: Multiple code signals confirm the finding
- **Medium**: Code signals suggest the finding, but some uncertainty exists
- **Low**: Limited evidence, hypothesis based on patterns

#### Human-in-the-Loop Gates
- Introduce validation checkpoints before finalizing critical findings
- Confirm intent, runtime realities, and business-critical flows with humans
- Optimize for minimal human effort with high-leverage questions

#### Safety-First Documentation
- Avoid assumptions that could mislead future engineers
- Mark uncertain areas explicitly
- Prioritize documenting risks and hotspots

### Agent Output Format

Each pass response should be structured as:

```markdown
## PASS STATUS: {Scan | Infer | Validate | Document}

### ARTIFACTS PRODUCED
- {List of deliverables created}

### TOP FINDINGS
- {Key discoveries, prioritized}

### CRITICAL UNCERTAINTIES
- {Items needing validation or clarification}

### NEXT ACTIONS
1. {Numbered action items}
2. {Including human validation needed}
```

---

## Pass 1: Scan

**Purpose:** Rapidly inventory the repository to understand its shape and structure.

**Invoke:**

```
Read @GenDD-Flow/agents/pass1-scan-agent.md

Analyze @TargetRepo and perform Pass 1: Scan.
```

**Review Checklist:**
- [ ] All major services/modules identified
- [ ] Entry points match your understanding
- [ ] Dependencies seem complete
- [ ] Test files are inventoried

**Output:** Save to `docs/brownfield/pass1-scan-findings.md`

For detailed instructions and output templates, see [pass1-scan-agent.md](../agents/pass1-scan-agent.md).

---

## Pass 2: Infer

**Purpose:** Using scan artifacts, infer architecture, flows, data ownership, and risks.

**Invoke:**

```
Read @GenDD-Flow/agents/pass2-infer-agent.md

Using the Pass 1 Scan findings in @docs/brownfield/pass1-scan-findings.md,
perform Pass 2: Infer on @TargetRepo.

Mark all findings as FACT or HYPOTHESIS with confidence levels.
```

**Review Checklist:**
- [ ] Architecture classification makes sense
- [ ] Core flows are accurately mapped
- [ ] Data ownership boundaries are clear
- [ ] Risks are prioritized appropriately

**Output:** Save to `docs/brownfield/pass2-infer-findings.md`

For detailed instructions and output templates, see [pass2-infer-agent.md](../agents/pass2-infer-agent.md).

---

## Pass 3: Validate

**Purpose:** Confirm critical hypotheses with humans who know the system.

**Invoke:**

```
Read @GenDD-Flow/agents/pass3-validate-hitl-agent.md

Using the Pass 2 Infer findings in @docs/brownfield/pass2-infer-findings.md,
generate the Human Validation Packet.

Keep questions short and high-leverage.
```

**Share Validation Packet with:**
- Original developer (if available)
- Current maintainer
- Subject matter expert
- Tech lead

**Process Responses:**

```
The human validation responses are:

{Paste responses here}

Update the Pass 2 findings based on these corrections and confirmations.
```

**Output:** Save to `docs/brownfield/pass3-validation-responses.md`

For detailed instructions and output templates, see [pass3-validate-hitl-agent.md](../agents/pass3-validate-hitl-agent.md).

---

## Pass 4: Document

**Purpose:** Produce comprehensive documentation that enables safe work in the repository.

**Invoke:**

```
Read @GenDD-Flow/agents/pass4-document-agent.md
Read @GenDD-Flow/agents/tailoring-rules.md

Using:
- Pass 1 Scan: @docs/brownfield/pass1-scan-findings.md
- Pass 2 Infer: @docs/brownfield/pass2-infer-findings.md
- Pass 3 Validation: @docs/brownfield/pass3-validation-responses.md

Generate the complete Documentation Pack.
Apply tailoring rules for {monorepo | microservices | event-driven}.
```

**Review Checklist:**
- [ ] All confirmed findings marked as FACT
- [ ] Inferred findings have confidence levels
- [ ] Risks are clearly highlighted
- [ ] Onboarding guide is actionable

**Output:** Save the documentation pack under `docs/brownfield/gendd/` (mirrors the GenDD Studio layout):

```
docs/brownfield/gendd/
├── README.md                   # index/manifest of the tree
├── stack.json                  # machine-readable tech stack
├── overview/
│   ├── system-summary.md
│   └── tech-stack.md
├── architecture/
│   ├── overview.md
│   ├── components.md
│   └── data-ownership.md
├── risks/
│   ├── risk-hotspots.md
│   └── open-questions.md
├── onboarding/
│   └── guide.md
└── flows/
    └── <kebab-case-flow-name>.md   # one file per core flow
```

For detailed instructions and output templates, see [pass4-document-agent.md](../agents/pass4-document-agent.md).

> **Tailoring:** Apply rules from [tailoring-rules.md](../agents/tailoring-rules.md) based on detected architecture pattern.

---

## Baseline Principles

When evaluating a brownfield repository, use these principles from the Context Pack template (`templates/context-pack.md`) as baseline expectations:

> **Key principles to evaluate against:**
> - **Security**: No hardcoded secrets, multi-tenant isolation enforced, input validated, sensitive data not logged
> - **Code quality**: Descriptive naming, SRP, errors handled with context, DI used
> - **Testing**: Tests follow AAA, required scenarios covered, coverage prioritized by risk
> - **Logging**: Appropriate log levels, no PII/credentials logged, sufficient context for debugging
> - **Version control**: Branch protection, meaningful commits, .gitignore covers secrets

---

## Feeding Other Workflows

After completing brownfield analysis, use outputs in other workflows:

### Feed: Test Gap Identification

```
Read @GenDD-Flow/workflows/identify-test-gaps.md

Use the brownfield analysis from @docs/brownfield/ to perform
comprehensive test gap analysis.

Focus on:
- Risk hotspots identified in Pass 2/4
- Core flows that need coverage
- Integration points lacking tests
```

### Feed: C4 Architecture Diagrams

```
Read @GenDD-Flow/workflows/generate-architecture-diagrams.md

Using the architecture hypotheses from @docs/brownfield/pass2-infer-findings.md
and the confirmed architecture from @docs/brownfield/gendd/architecture/overview.md,
generate C4 diagrams:
1. Context Diagram
2. Container Diagram
3. Component Diagram (for key containers)
```

### Feed: Context Pack

```
Read @GenDD-Flow/workflows/create-context-pack.md
Read @GenDD-Flow/templates/context-pack.md

Using the brownfield documentation at @docs/brownfield/gendd/,
create a Context Pack:
1. agents.md - AI instructions and constraints
2. context.md - Domain knowledge
3. conventions.md - Coding patterns
4. testing.md - Test standards
5. architecture.md - System design

Use @GenDD-Flow/templates/context-pack.md as the template for universal principles.
```

### Feed: Change Requirements

```
Read @GenDD-Flow/workflows/enhance-acceptance-criteria.md

Using the core flows documented in @docs/brownfield/gendd/flows/,
enhance the requirements for:

Requirement: "{New feature or change}"

Consider the existing flows, data ownership, and risk hotspots.
```

---

## Output Artifacts Summary

After completing all 4 passes:

```
docs/brownfield/
├── pass1-scan-findings.md          # Repository inventory
├── pass2-infer-findings.md         # Architecture hypotheses
├── pass3-validation-responses.md   # Human validation results
└── gendd/                          # Documentation pack from Pass 4
    ├── README.md                   # index/manifest of the tree
    ├── stack.json                  # machine-readable tech stack
    ├── overview/
    │   ├── system-summary.md
    │   └── tech-stack.md
    ├── architecture/
    │   ├── overview.md
    │   ├── components.md
    │   └── data-ownership.md
    ├── risks/
    │   ├── risk-hotspots.md
    │   └── open-questions.md
    ├── onboarding/
    │   └── guide.md
    └── flows/
        └── <kebab-case-flow-name>.md   # one file per core flow

From feeding other workflows:
├── test-gap-analysis.md           # From identify-test-gaps.md
├── c4-diagrams/                   # From generate-architecture-diagrams.md
│   ├── context.mmd
│   ├── container.mmd
│   └── component.mmd
└── .cursor/                       # From create-context-pack.md
    ├── agents.md
    ├── context.md
    ├── conventions.md
    ├── testing.md
    └── architecture.md
```

---

## Time Estimates

| Pass | Effort | Dependencies |
|------|--------|--------------|
| Pass 1: Scan | ~15-30 min | Repository access |
| Pass 2: Infer | ~30-45 min | Pass 1 complete |
| Pass 3: Validate | ~30 min + human time | Human validator available |
| Pass 4: Document | ~30-45 min | Pass 3 complete |

---

## Tips for Best Results

### Provide Context
When starting, share:
- Known integrations
- Business domain
- Compliance requirements
- Known pain points

### Focus on Critical Paths
Prioritize documenting:
- Revenue-impacting flows
- Security-critical paths
- High-change areas
- Common failure modes

### Validate Early
Don't skip Pass 3 validation:
- Prevents documenting wrong information
- Catches runtime vs code discrepancies
- Identifies tribal knowledge

### Iterate
It's better to:
1. Complete all passes quickly
2. Identify major gaps
3. Deep-dive on specific areas

Than to:
1. Try to document everything in Pass 1
2. Never reach documentation

---

## Success Criteria

A successful brownfield analysis:
- [ ] New engineers can understand the system in < 1 day
- [ ] Critical risks and hotspots are documented
- [ ] Data ownership boundaries are clear
- [ ] Core flows are mapped and validated
- [ ] Onboarding guide exists
- [ ] Context Pack can be generated from outputs

## Common Pitfalls

- **Skipping validation**: Critical findings need human confirmation
- **Over-documenting**: Focus on what enables safe changes
- **Missing event flows**: Check for message brokers and async patterns
- **Ignoring tests**: Test inventory reveals what the team values
- **Assuming from names**: Code behavior > file/class names

---

## Integration with Existing Workflows

| This Workflow | Feeds | Why |
|---------------|-------|-----|
| Brownfield Analysis | Test Gap Identification | Risk hotspots → test priorities |
| Brownfield Analysis | Generate Architecture Diagrams | Hypotheses → C4 diagrams |
| Brownfield Analysis | Create Context Pack | Documentation → AI context |
| Brownfield Analysis | Enhance Acceptance Criteria | Core flows → change requirements |
| Brownfield Analysis | Automate Integration Testing | Integration points → test generation |

| Other Workflow | Feeds This | Why |
|----------------|-----------|-----|
| None | Brownfield Analysis | This is typically the starting point |

---

## Example: Analyzing mslearn-dotnetmicroservices

See the `examples/brownfield-analysis/` folder for a complete worked example:
- `examples/brownfield-analysis/pass1-scan-findings.md` - Repository inventory
- `examples/brownfield-analysis/pass2-infer-findings.md` - Architecture hypotheses
- `examples/brownfield-analysis/pass3-validation-packet.md` - Human validation
- `examples/brownfield-analysis/pass4-final-documentation.md` - Final documentation

### Quick Summary
- **Repository**: .NET microservices tutorial
- **Architecture**: Microservices (2 services)
- **Pattern**: API Gateway (Frontend as Gateway)
- **Time to Analyze**: ~2 hours
- **Key Finding**: Educational project, not production system
- **Main Risks**: No persistence, no auth, no tests
