# Pass 2: Brownfield Inference Analyst

## Mission

Using Pass 1 Scan artifacts and code evidence, infer:
- **System purpose** (hypotheses)
- **Architecture style**: Monorepo, microservices, event-driven (or hybrid)
- **Critical flows**: Request/response, async events, batch pipelines
- **Data ownership boundaries**
- **Operational behaviors** (deploy/run patterns)

**Critical Rule**: Separate **FACTS** (evidence-based) from **INFERENCES** (hypotheses).

## Required Reasoning Frames

### A) Architecture Classification

| Pattern | Indicators |
|---------|------------|
| **Monorepo** | Shared libs + multiple apps in one repo, workspace tooling, shared dependencies |
| **Microservices** | Multiple independently deployable services, separate Dockerfiles/Helm charts, independent CI pipelines |
| **Event-Driven** | Brokers/queues, explicit consumers, idempotency patterns, outbox, eventual consistency |
| **Hybrid** | Combination of above patterns |

### B) Flow Discovery (3 Types)

#### 1. Request Flows
```
UI/API → Controller/Handler → Domain Logic → Persistence → Response
```

#### 2. Event Flows
```
Producer → Broker/Topic → Consumer → Side Effects
```

#### 3. Batch Flows
```
Scheduler/Cron → Job → Processing → Persistence/Reporting
```

### C) Data & Ownership

Identify:
- Which service/module owns which tables/entities/events
- Shared DB vs per-service DB patterns
- Read models, caching, CQRS hints
- Data boundaries and coupling

## Output Artifacts

### 1. ARCHITECTURE HYPOTHESES
```markdown
## Architecture Hypotheses

### Primary Classification
**FACT/HYPOTHESIS (Confidence):** {Architecture Pattern}

**Evidence:**
- {File/path/code reference 1}
- {File/path/code reference 2}

**Why it matters:** {Impact on documentation and safe changes}

### Sub-Patterns
| Pattern | Confidence | Evidence | Impact |
|---------|------------|----------|--------|
| {pattern} | High/Med/Low | {evidence} | {impact} |

### Architecture Diagram (Text)
```
{ASCII diagram of high-level architecture}
```
```

### 2. SERVICE/MODULE CATALOG
```markdown
## Service/Module Catalog

### Service: {Name}

**Responsibility:** {Primary purpose}
**Type:** {API | Worker | Frontend | Library}
**Key Files:**
| File | Purpose |
|------|---------|
| {file} | {purpose} |

**Key Responsibilities:**
1. {Responsibility 1}
2. {Responsibility 2}

**Dependencies:**
- Internal: {services/modules it depends on}
- External: {third-party APIs, databases}

**Owns Data:**
- {Entity/table it owns}
```

### 3. CORE FLOWS
```markdown
## Core Flows

### Flow 1: {Name} (Request/Event/Batch)

**Type:** {Request | Event | Batch}
**Trigger:** {What initiates this flow}
**Criticality:** {High | Medium | Low}

**Flow Description:**
1. {Step 1}
2. {Step 2}
3. {Step 3}

**Code Path:**
- Entry: `{file}::{method}` (line X)
- Processing: `{file}::{method}` (line X)
- Exit: `{file}::{method}` (line X)

**Error Handling:**
- {How errors are handled}

**Flow Diagram (Text):**
```
{ASCII sequence diagram}
```

**Confidence:** {High/Med/Low}
**Evidence:** {File references}
```

### 4. DATA MAP
```markdown
## Data Map

### Entities

#### Entity: {Name}
**Location:** {file/path}
**Schema:**
| Field | Type | Description |
|-------|------|-------------|
| {field} | {type} | {description} |

**Owned By:** {Service/module}
**Storage:** {Database/In-memory/File}
**Persistence:** {Yes/No}

### Data Ownership Boundaries
| Entity/Table | Owner Service | Evidence |
|--------------|---------------|----------|
| {entity} | {service} | {file reference} |

### Data Flow Patterns
- {Shared DB vs per-service DB}
- {Caching approach}
- {CQRS if present}

### Data Risks
- {Cross-service coupling}
- {Missing persistence}
- {Inconsistency risks}
```

### 5. OPERATIONAL MODEL (Inferred)
```markdown
## Operational Model (Inferred)

### Deployment Units
| Unit | Build | Ports | Dependencies |
|------|-------|-------|--------------|
| {unit} | {Dockerfile/method} | {ports} | {deps} |

### Configuration Management
| Source | Purpose | Environment |
|--------|---------|-------------|
| {file/source} | {purpose} | {dev/prod} |

### Environment Variables (Detected)
| Variable | Purpose | Source |
|----------|---------|--------|
| {var} | {purpose} | {source} |

### Scaling Signals
- {Stateless/stateful}
- {Horizontal scaling possible?}
- {Session management}

### Startup Dependencies
```
{Service dependency graph}
```
```

### 6. RISK HOTSPOTS
```markdown
## Risk Hotspots

### 🚨 High Risk: {Title}
**Location:** `{file/path}`
**Risk Level:** High
**Issue:** {Description}

**Why Dangerous:**
- {Reason 1}
- {Reason 2}

**Safe Changes:**
- ✅ {What's safe to change}

**Dangerous Changes:**
- ❌ {What NOT to change without review}

**Recommendation:** {Mitigation}

---

### ⚠️ Medium Risk: {Title}
{Same format}

---

### Risk Summary
| Category | High | Medium | Low |
|----------|------|--------|-----|
| {category} | {count} | {count} | {count} |
```

### 7. SUGGESTED SDLC AREAS
```markdown
## Suggested SDLC Areas

Based on the technologies, patterns, architecture, and concerns identified during inference,
suggest which SDLC areas apply to this codebase.

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
```

### 8. HUMAN VALIDATION QUESTIONS
```markdown
## Human Validation Questions

### Priority 1: Critical Architecture Decisions
1. **{Question}**
   - Why: {Why this matters}
   - Evidence: {What we observed}
   - Decision Impact: {High/Medium/Low}

### Priority 2: Business Logic & Domain
2. **{Question}**
   - Why: {Why this matters}
   - Evidence: {What we observed}

### Priority 3: Operational Concerns
3. **{Question}**
   - Why: {Why this matters}
   - Evidence: {What we observed}

### Minimum Required Confirmations
- [ ] Primary flow confirmed
- [ ] Data ownership confirmed
- [ ] Deployment model confirmed
```

## Inference Rules

### Evidence Citation
Every inference **MUST** cite evidence:
- Filenames and line numbers
- Import edges
- Route registration points
- Message topics

### Confidence Marking
Mark uncertain inferences:
```
**Hypothesis (Medium Confidence):** {Statement}
**Evidence:** {What supports this}
**Uncertainty:** {What we're unsure about}
```

### Contradiction Surfacing
When code contradicts naming or documentation:
```
⚠️ **Contradiction Detected:**
- Code says: {behavior}
- Naming suggests: {different behavior}
- Resolution needed: {question for validation}
```

## Example Prompt

```
Read @GenDD-Flow/agents/pass2-infer-agent.md

Using the Pass 1 Scan findings in @docs/pass1-scan-findings.md,
perform Pass 2: Infer on @TargetRepo.

Generate all output artifacts:
1. Architecture Hypotheses
2. Service/Module Catalog
3. Core Flows (at least 2 request flows, 2 async/batch if present)
4. Data Map
5. Operational Model
6. Risk Hotspots
7. Suggested SDLC Areas
8. Human Validation Questions

Mark all findings as FACT or HYPOTHESIS with confidence levels.
```

## Related Resources

> **Workflow:** See [brownfield-repository-analysis.md](../workflows/brownfield-repository-analysis.md) for pass transitions, validation gates, and overall coordination.
> **Tailoring:** Apply rules from [tailoring-rules.md](tailoring-rules.md) based on detected architecture pattern during inference.

## Proceeding to Pass 3

**Required before Pass 3:**
- [ ] All major components cataloged
- [ ] At least 2 core flows documented
- [ ] Critical risks identified
- [ ] Validation questions prioritized

**If confidence < Medium on critical areas, force Pass 3 validation.**
