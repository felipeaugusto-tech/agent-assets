# Role Playbook: Architect

**Role:** Software/Solutions Architect  
**Focus:** C4 diagrams, risk hotspots, tech debt, ADRs, integration and security impact assessment  
**Time:** 45-60 minutes

---

## Quick Start

```
Read @GenDD-Flow/playbooks/by-role/architect.md
Analyze @TargetRepo for architecture and technical debt.
```

---

## Purpose

Analyze a codebase from an Architect perspective to understand:
- System architecture and patterns
- Component relationships and boundaries
- Technical debt and risk areas
- Architectural decisions and trade-offs
- Integration impact for delivery readiness
- Security and compliance considerations

---

## Relevant Workflows

| Workflow | When to Use |
|----------|-------------|
| [Brownfield Analysis](../../workflows/brownfield-repository-analysis.md) | First-time codebase analysis |
| [Create Context Pack](../../workflows/create-context-pack.md) | Set up AI context files |
| [Generate C4 Architecture Diagrams](../../workflows/generate-architecture-diagrams.md) | Generate C4 model diagrams |

---

## {ORGANIZATION} Epic & Story Impact Standards

> **Reference:** Aligns with {ORGANIZATION}'s **Epic Template** and **Story Templates** for architectural inputs.

### Epic-Level Architecture Fields

| Field | Description | Architect Role |
|-------|-------------|----------------|
| **Integration Impact** | External systems involved (Skyward, Qmlativ, Powerschool, payment providers, etc.) | Identify and document |
| **Architecture Impact** | New flow or modification to existing flow? Link to C4 diagram if available | Assess and document |

### Story-Level Architecture Inputs

| Input | Architect Responsibility |
|-------|--------------------------|
| Integration & Risk Flags | Validate external integration involvement |
| Architecture Reference | Provide or update C4 diagram link |
| Security Review Need | Confirm if security review required |
| NFRs | Define performance, scalability, security requirements |

### Integration Impact Assessment

| Question | Answer | If Yes |
|----------|--------|--------|
| External systems involved? | Yes/No/Unknown | Document which systems |
| New integration or modification? | New/Modify/None | Link to existing integration docs |
| Payment or financial systems? | Yes/No | Flag PCI compliance |
| User data or PII involved? | Yes/No | Flag privacy/security review |
| Auth/authorization changes? | Yes/No | Flag security review |

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/architect.md

Analyze @TargetRepo from an Architect perspective:

## Context
- System Type: [Monolith | Microservices | Serverless | Hybrid]
- Scale: [Users/Requests per day]
- Criticality: [Business critical | Internal tool | Customer-facing]
- Age: [Years in production]

## Phase 1: Architecture Classification

### Pattern Identification
| Aspect | Pattern | Confidence | Evidence |
|--------|---------|------------|----------|
| Overall architecture | [Monolith/Microservices/etc] | High/Med/Low | [file refs] |
| Communication | [Sync REST/Async/Event-driven] | High/Med/Low | [file refs] |
| Data architecture | [Shared DB/DB per service/CQRS] | High/Med/Low | [file refs] |
| Frontend pattern | [Monolith/Micro-frontend/SPA] | High/Med/Low | [file refs] |

### Architectural Style
- [ ] Layered Architecture
- [ ] Clean Architecture  
- [ ] Hexagonal Architecture
- [ ] Event-Driven Architecture
- [ ] Microservices
- [ ] Modular Monolith
- [ ] Other: ___________

## Phase 2: C4 Model Analysis

### Level 1: System Context
| Element | Type | Description |
|---------|------|-------------|
| [System Name] | System | The system being analyzed |
| [Actor 1] | Person | [Description] |
| [External System 1] | External System | [Description] |

### Level 2: Container View
| Container | Technology | Responsibility |
|-----------|------------|----------------|
| [Web App] | [React/Vue/etc] | User interface |
| [API] | [Node/Go/.NET] | Business logic |
| [Database] | [PostgreSQL/etc] | Data persistence |

### Level 3: Component View (for key container)
| Component | Responsibility | Dependencies |
|-----------|----------------|--------------|
| [Component] | [What it does] | [Other components] |

## Phase 3: Dependency Analysis

### External Dependencies (Integration Impact)
| Integration | Purpose | Coupling | Security Flags | Story Impact |
|-------------|---------|----------|----------------|--------------|
| Skyward | [Why] | Tight/Loose | PCI/PII/None | Flag in Stories |
| Qmlativ | [Why] | Tight/Loose | PCI/PII/None | Flag in Stories |
| Payment providers | [Why] | Tight/Loose | PCI | Flag in Stories |

### Dependency Health
| Metric | Value | Status |
|--------|-------|--------|
| Circular dependencies | [count] | Good/Warning |
| Coupling score | [value] | Good/Warning |
| Cohesion score | [value] | Good/Warning |

## Phase 4: Technical Debt Inventory

### Debt Categories
| Category | Items | Total Effort | Priority |
|----------|-------|--------------|----------|
| Code quality | [list] | [days] | P1/P2/P3 |
| Architecture | [list] | [days] | P1/P2/P3 |
| Infrastructure | [list] | [days] | P1/P2/P3 |
| Dependencies | [list] | [days] | P1/P2/P3 |

### Top Debt Items
| Item | Type | Impact | Effort | Interest Rate |
|------|------|--------|--------|---------------|
| [Debt item] | [Type] | High/Med/Low | [days] | [monthly impact] |

## Phase 5: Risk Hotspots

### High-Risk Areas
| Area | Risk Type | Evidence | Mitigation |
|------|-----------|----------|------------|
| [Area] | Complexity | Cyclomatic complexity > 20 | Refactor |
| [Area] | Change frequency | Modified in 80% of PRs | Extract service |
| [Area] | Bug density | High defect rate | Add tests |

## Phase 6: Architectural Decisions

### Existing ADRs
| ADR | Decision | Status | Impact |
|-----|----------|--------|--------|
| [ADR-001] | [Decision] | Accepted/Superseded | [Components] |

### Inferred Decisions (No ADR)
| Decision | Evidence | Rationale | Should Document? |
|----------|----------|-----------|------------------|
| [Decision] | [Files] | [Assumed reason] | Yes/No |

## Phase 7: Quality Attributes Assessment

| Attribute | Current State | Target | Gap |
|-----------|---------------|--------|-----|
| Performance | [assessment] | [target] | [gap] |
| Scalability | [assessment] | [target] | [gap] |
| Maintainability | [assessment] | [target] | [gap] |
| Security | [assessment] | [target] | [gap] |

## Phase 8: Recommendations

### Architecture Improvements
| Priority | Improvement | Effort | Impact |
|----------|-------------|--------|--------|
| P1 | [Improvement] | [weeks] | [impact] |

### Tech Debt Paydown Plan
| Sprint | Focus | Items | Effort |
|--------|-------|-------|--------|
| 1 | [Area] | [Items] | [days] |
```

---

## Expected Output

```markdown
# Architecture Assessment: [Project Name]
Generated: [Date]

## Architecture Overview
- Style: [Architectural Style]
- Key Patterns: [List]

## C4 Diagrams
- Context Diagram (link or embed)
- Container Diagram (link or embed)

## Technical Debt Summary
Top 5 items with effort and impact

## Risk Hotspots
Critical areas requiring attention

## Quality Attributes
Score card for performance, scalability, security, etc.

## Recommended ADRs
Decisions that should be documented

## Roadmap
Phased improvement plan
```

---

## Follow-Up Actions

- For detailed C4 diagrams: [Generate Architecture Diagrams](../../workflows/generate-architecture-diagrams.md)
- For full codebase analysis: [Brownfield Analysis](../../workflows/brownfield-repository-analysis.md)
