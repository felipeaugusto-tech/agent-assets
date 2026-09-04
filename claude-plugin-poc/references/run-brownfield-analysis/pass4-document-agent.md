# Pass 4: Brownfield Documentation Author

## Mission

Produce a **documentation pack** that enables new engineers to safely work in the repo:
- Understand what the system does
- Navigate modules/services
- Modify safely without breaking critical paths
- Operate/debug in production

**Critical:** Incorporate Human Validation results and clearly label what remains uncertain.

## Output Structure

The documentation pack MUST be written as an individual file per section inside the `docs/brownfield/gendd/` tree. This mirrors the GenDD Studio layout and is identical to what the `genddflow` CLI produces:

```
@TargetRepo/
└── docs/
    └── brownfield/
        ├── pass1-scan-findings.md          (from Pass 1)
        ├── pass2-infer-findings.md         (from Pass 2)
        ├── pass3-validation-responses.md   (from Pass 3)
        └── gendd/
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
                └── <kebab-case-flow-name>.md   # ONE file per core flow (dynamic count)
```

**Do NOT generate a single monolithic document.** Each section is its own file, cross-referencing others by their real relative path as needed. Do NOT invent flat numbered filenames (e.g. `NN-section-name.md`) — use exactly the paths shown above.

## Documentation Guidelines

**Reference:** `templates/documentation-guidelines.md`

### Key Rules
- ❌ **No code snippets** - Reference files instead: `Services/PaymentService.cs:ProcessPayment()`
- ❌ **No hard-coded counts** - Use patterns: "Services matching `*Service.cs`"
- ❌ **No duplication** - Each concept in ONE file, cross-reference others
- ✅ **Size limits** - Overview: 200 lines, Components: 150 lines, Flows: 150 lines

## Documentation Pack (Always Produce)

Produce one file per section below at the exact `gendd/` path shown. Filenames are fixed — do not renumber or rename them.

### `overview/system-summary.md` — System Summary
Merge what were previously the Executive Summary and System Overview into a single System Summary file. Cover: what the system does (1-2 paragraphs), key characteristics (architecture, communication, data, purpose, technology), confirmed vs. needs-validation facts, and a Quick Start commands block. Mark each claim as FACT or HYPOTHESIS with confidence. Max 200 lines.
```markdown
# System Summary: {System Name}

## What This System Does
{1-2 paragraph description}

## Key Characteristics
- **Architecture:** {Pattern}
- **Communication:** {Sync HTTP | Async Events | Hybrid}
- **Data:** {Persistence approach}
- **Purpose:** {Production | Educational | Internal}
- **Technology:** {Primary tech stack}

## Critical Facts
- ✅ **Confirmed (FACT):** {Key confirmed findings}
- ⚠️ **Needs Validation (HYPOTHESIS, confidence):** {Outstanding uncertainties}

## Quick Start
```bash
# Development setup
{commands}

# Running locally
{commands}
```
```

### `overview/tech-stack.md` — Tech Stack
Tables listing primary language(s), frameworks, runtime/build tooling, databases, message brokers, third-party services, and deployment targets. Cite evidence files for each entry.
```markdown
# Tech Stack

## Languages
| Language | Usage | Evidence |
|----------|-------|----------|
| {lang} | {where} | {file} |

## Frameworks
| Framework | Purpose | Evidence |
|-----------|---------|----------|
| {framework} | {purpose} | {file} |

## Runtime & Build Tooling
| Tool | Purpose | Evidence |
|------|---------|----------|
| {tool} | {purpose} | {file} |

## Databases & Message Brokers
| System | Type | Evidence |
|--------|------|----------|
| {system} | {db/broker} | {file} |

## Third-Party Services & Deployment Targets
| Service / Target | Purpose | Evidence |
|------------------|---------|----------|
| {service} | {purpose} | {file} |
```

### `architecture/overview.md` — Architecture Overview
```markdown
## Architecture Overview

### Architecture Classification

**FACT (Confirmed):** {Architecture pattern}
- Evidence: {Code references}

**NOT:** {What it's not}
- Evidence: {Why not}

### Architecture Pattern
**Pattern:** {Pattern name}
- {Description of how it works}

### Architecture Diagram
```
{ASCII diagram or reference to Mermaid diagram}
```

### Service Communication
| From | To | Protocol | Pattern |
|------|-----|----------|---------|
| {service} | {service} | {HTTP/Event} | {Sync/Async} |
```

### `architecture/components.md` — Component Catalog
Reference files by path, never paste code.
```markdown
## Component Catalog

### Service: {Name}

**Type:** {API | Worker | Frontend | Library}
**Purpose:** {What it does}
**Deployment Unit:** {Container name / deployment artifact}

#### Key Components
| Component | File | Responsibility |
|-----------|------|----------------|
| {name} | {path} | {what it does} |

#### Responsibilities
1. {Responsibility 1}
2. {Responsibility 2}

#### Dependencies
- **Internal:** {Other services/modules}
- **External:** {Third-party APIs, databases}

#### Data Ownership
**Owns:** {Entities/tables this service owns}

---

{Repeat for each service/module}
```

### `flows/<kebab-case-flow-name>.md` — Core Flows (ONE file per flow)
Identify **every** core flow in the system (request flows, event flows, batch jobs). Produce **one file per flow**, named with the kebab-case flow name (e.g. `flows/command-processing.md`). Do NOT put multiple flows in a single file, and do NOT hard-code how many flows there are — the count is dynamic. Reference files by path — never paste code. Each flow file uses this template:
```markdown
# Core Flow: {Name}

**Type:** {Request | Event | Batch}
**Trigger:** {What initiates}
**Status:** {✅ Confirmed | ⚠️ Inferred}

## Sequence Diagram
```
{ASCII sequence diagram}
```

## Step-by-Step
1. **{Step}:** {Description}
   - Entry: `{file}::{method}`
2. **{Step}:** {Description}
   - Code: `{file}::{method}`

## Error Handling
- {How errors are handled}
- {Fallback behavior}

## Code References
| Step | File | Line |
|------|------|------|
| {step} | {file} | {line} |
```

### `architecture/data-ownership.md` — Data Model & Ownership
```markdown
## Data Model & Ownership

### Data Entities

#### Entity: {Name}
**Location:** {file/path}
**Owner:** {Service}
**Storage:** {Database type}

**Schema:**
| Field | Type | Description |
|-------|------|-------------|
| {field} | {type} | {description} |

### Data Ownership Boundaries

**FACT (Confirmed):** {Ownership description}

| Entity | Owner | Storage | Persistence |
|--------|-------|---------|-------------|
| {entity} | {service} | {db} | {yes/no} |

### Data Flow
```
{ASCII diagram of data flow}
```

### Data Risks
- {Risk 1}
- {Risk 2}
```

### `risks/risk-hotspots.md` — Risk & Hotspot Map
```markdown
## Risk & Hotspot Map

### High-Risk Areas

#### 🚨 {Risk Title}
**Location:** `{file/path}`
**Risk Level:** High
**Impact:** {What could go wrong}

**Why Dangerous:**
- {Reason 1}
- {Reason 2}

**Safe Changes:**
- ✅ {What's safe}

**Dangerous Changes:**
- ❌ {What's dangerous}

---

### Risk Summary
| Category | High | Medium | Low |
|----------|------|--------|-----|
| {category} | {n} | {n} | {n} |
```

### `onboarding/guide.md` — Onboarding Guide
Cover Safe First Changes, Dangerous Zones (senior review), Development Setup, and Common Tasks.

**CRITICAL — no hard-coded numbered filenames.** Do NOT write a "Reading Order" section that links to invented flat numbered files (e.g. `NN-section-name.md`). Instead, build the reading order / manifest from the files that **actually exist** in this `gendd/` tree — the section files above plus the per-flow files under `flows/` — linking each by its real relative path (relative to `onboarding/`, e.g. `../overview/system-summary.md`, `../architecture/overview.md`, `../flows/command-processing.md`). List a flow entry only if that flow file exists.
```markdown
## Onboarding Guide

### Reading Order
{Ordered list linking ONLY to files that exist in this tree, by real relative path.
 Example — adapt to the files you actually produced:}
1. **System Summary** — [../overview/system-summary.md](../overview/system-summary.md)
2. **Tech Stack** — [../overview/tech-stack.md](../overview/tech-stack.md)
3. **Architecture Overview** — [../architecture/overview.md](../architecture/overview.md)
4. **Core Flows** — [command processing](../flows/command-processing.md){, one link per flow file}
5. **This Onboarding Guide** — the sections below

### Safe First Changes
These are **low-risk** changes good for learning:
1. {Safe change type 1}
2. {Safe change type 2}

### Dangerous Zones
⚠️ **Do NOT modify without senior review:**
1. {Dangerous area 1}
2. {Dangerous area 2}

### Development Setup
```bash
# Prerequisites
{prereqs}

# Setup
{setup commands}

# Running
{run commands}
```

### Common Tasks
#### {Task 1}
```bash
{commands}
```

#### {Task 2}
1. {Step 1}
2. {Step 2}
```

### `risks/open-questions.md` — Open Questions / Future Work
```markdown
## Open Questions / Future Work

### Pending Validation
{Questions that still need human confirmation}

### Known Gaps
| Gap | Impact | Priority |
|-----|--------|----------|
| {gap} | {impact} | {priority} |

### Recommended Improvements
#### High Priority
1. {Improvement 1}
2. {Improvement 2}

#### Medium Priority
{List}

#### Low Priority
{List}
```

### `stack.json` — Machine-readable Tech Stack
Write a single JSON object (no markdown, no fences) capturing the stack. Unknown values must be empty arrays.
```json
{
  "language": "string or array of strings",
  "frameworks": [],
  "runtimes": [],
  "datastores": [],
  "messaging": [],
  "infrastructure": [],
  "build": [],
  "package_managers": []
}
```

### `gendd/README.md` — Index / Manifest
An index that mirrors the tree: grouped sections (Overview, Architecture, Risks, Onboarding) each linking to their files, a Flows section linking each flow file that exists, and a Machine-readable section linking `stack.json`.
```markdown
# GenDD Brownfield Documentation

Generated by the GenDD brownfield analysis. This tree mirrors the GenDD Studio layout.

## Overview
- [overview/system-summary.md](overview/system-summary.md)
- [overview/tech-stack.md](overview/tech-stack.md)

## Architecture
- [architecture/overview.md](architecture/overview.md)
- [architecture/components.md](architecture/components.md)
- [architecture/data-ownership.md](architecture/data-ownership.md)

## Risks
- [risks/risk-hotspots.md](risks/risk-hotspots.md)
- [risks/open-questions.md](risks/open-questions.md)

## Onboarding
- [onboarding/guide.md](onboarding/guide.md)

## Flows
- [flows/{flow-name}.md](flows/{flow-name}.md)   {one line per flow file that exists}

## Machine-readable
- [stack.json](stack.json)
```

## Suggested SDLC Areas

As part of the documentation process, analyze which SDLC areas apply to this codebase and include `suggestedAreas` in your output. This is used by Pass 5 (Role Detector) as the primary detection mechanism.

```json
"suggestedAreas": [
  {
    "areaId": "one of: architecture, backend-development, frontend-development, fullstack-development, quality-assurance, devops-infrastructure, site-reliability, security, database-management, product-management, delivery-management, technical-leadership, user-experience, technical-writing, release-management, support-engineering",
    "confidence": "high | medium | low",
    "reasoning": "Why this SDLC area applies based on evidence found in the codebase"
  }
]
```

**SDLC Area Suggestions:** Analyze which of the 16 standard SDLC areas apply to this codebase based on the technologies, patterns, architecture, and concerns you identify. Include each applicable area with a confidence level and specific reasoning tied to evidence in the code. This replaces hardcoded signal matching — your analysis is the primary detection mechanism.

## Output Rules

### FACTS vs INFERENCES
- **FACT (Confirmed):** "Confirmed by code/humans"
- **HYPOTHESIS (Confidence):** "Inferred from code signals"
- Always mark validation status

### Diagram Format
When images not possible, use ASCII:
```
┌─────────┐     ┌─────────┐
│ Service │────▶│ Service │
└─────────┘     └─────────┘
```

### Tone
- Clear and operational
- Safety-first (highlight risks)
- Actionable (tell people what to do)

## Architecture-Specific Tailoring

> **Reference:** See [tailoring-rules.md](tailoring-rules.md) for detailed architecture-specific guidance on what to include for monorepo, microservices, and event-driven systems.

## Example Prompt

```
Read @GenDD-Flow/agents/pass4-document-agent.md

Using:
- Pass 1 Scan: @docs/brownfield/pass1-scan-findings.md
- Pass 2 Infer: @docs/brownfield/pass2-infer-findings.md
- Pass 3 Validation: @docs/brownfield/pass3-validation-responses.md

Generate the complete Documentation Pack as individual files in the
@TargetRepo/docs/brownfield/gendd/ tree:
1. gendd/overview/system-summary.md
2. gendd/overview/tech-stack.md
3. gendd/architecture/overview.md
4. gendd/architecture/components.md
5. gendd/architecture/data-ownership.md
6. gendd/flows/<one file per core flow>.md
7. gendd/risks/risk-hotspots.md
8. gendd/risks/open-questions.md
9. gendd/onboarding/guide.md
10. gendd/stack.json
11. gendd/README.md

Mark all sections as CONFIRMED or INFERRED based on validation responses.
Then continue to Phase 2 (SDLC area detection).
```

## Related Resources

> **Workflow:** See [brownfield-repository-analysis.md](../workflows/brownfield-repository-analysis.md) for pass transitions, validation gates, and overall coordination.

## Quality Checklist

Before finalizing:
- [ ] All confirmed findings marked as FACT
- [ ] All inferred findings marked with confidence
- [ ] All high-risk areas documented
- [ ] Onboarding path is clear
- [ ] Development setup instructions work
- [ ] No speculative content presented as fact
- [ ] Each section saved as an individual file in the `docs/brownfield/gendd/` tree
- [ ] Onboarding reading order links only to files that exist (no invented numbered filenames)
- [ ] `stack.json` and `gendd/README.md` produced

## Next Step: Continue to Pass 5 (SDLC Role Detection)

After completing the documentation pack, **automatically proceed** to Pass 5:

```
Read @GenDD-Flow/agents/pass5-role-detector-agent.md

Using the brownfield analysis output at @TargetRepo/docs/brownfield/,
determine which SDLC areas apply to this codebase.

Present the area map with confidence levels and evidence,
then wait for my confirmation before proceeding.
```

After the user confirms SDLC areas, continue through:
- **Generate context per area** → `workflows/generate-context-areas.md`
- **Detect & generate standards** → `workflows/detect-and-generate-standards.md`
- **Generate IDE rules** → `workflows/generate-ide-rules.md`

> See [analyze-and-generate.md](../workflows/analyze-and-generate.md) for the full orchestration flow.
