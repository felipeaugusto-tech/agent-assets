# Architecture -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Architecture lens.

## Detection Signals

What in a codebase indicates architecture analysis is relevant. Used by the role-detector agent.

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Multiple service directories or repos | HIGH | `services/`, `apps/`, `packages/` in monorepo |
| C4 or architecture diagram files | HIGH | `docs/architecture/`, `*.c4`, `*.puml`, `*.mmd` with C4 keywords |
| ADR (Architecture Decision Record) files | HIGH | `docs/adr/`, `adr/`, `ADR-*.md` |
| Infrastructure-as-code alongside application code | HIGH | `infra/`, `terraform/`, `pulumi/`, `k8s/` |
| Multiple data stores configured | MEDIUM | Multiple DB connection strings, Redis + PostgreSQL + S3 |
| API gateway or service mesh configuration | MEDIUM | `gateway.yml`, Envoy, Istio, Kong config |
| Dependency injection containers | MEDIUM | `container.ts`, `di/`, `IServiceCollection`, `wire.go` |
| Event/message broker configuration | MEDIUM | Kafka, RabbitMQ, SQS, NATS config files |
| Shared library or package references | LOW | Internal package registries, `@org/` scoped packages |
| Docker Compose with multiple services | LOW | `docker-compose.yml` with 3+ services |

## What to Analyze

### Architecture Classification
- Look for: Overall architecture style (monolith, microservices, modular monolith, serverless, hybrid)
- Assess: Communication patterns (sync REST, async messaging, event-driven, gRPC)
- Assess: Data architecture (shared database, database per service, CQRS, event sourcing)
- Assess: Frontend architecture (monolith SPA, micro-frontends, server-rendered)
- Document: Architectural style with confidence level and evidence files

### C4 Model Mapping
- Look for: System context -- external actors, external systems, the system boundary
- Look for: Container view -- web apps, APIs, databases, message brokers, file stores
- Look for: Component view for key containers -- modules, services, controllers, repositories
- Assess: Whether existing C4 diagrams match the actual codebase
- Document: C4 levels 1-3 with technology choices and responsibilities per container/component

### Dependency and Coupling Analysis
- Look for: External integrations (third-party APIs, payment providers, identity providers, SIS systems)
- Assess: Coupling level between components (tight vs. loose, shared databases, direct calls vs. events)
- Assess: Cohesion within modules (single responsibility adherence)
- Assess: Circular dependency presence and severity
- Document: Dependency map with coupling scores and security flags (PCI, PII) per integration

### Technical Debt Inventory
- Look for: Code quality debt (long methods, god classes, duplication)
- Look for: Architecture debt (inappropriate coupling, missing abstractions, bypassed layers)
- Look for: Infrastructure debt (manual processes, missing automation)
- Look for: Dependency debt (outdated packages, unsupported frameworks)
- Assess: Each debt item by impact, effort to resolve, and interest rate (ongoing cost of not fixing)
- Document: Categorized debt inventory with priority and estimated effort

### Risk Hotspots
- Look for: Files with high cyclomatic complexity (>20)
- Look for: Files changed in >50% of recent PRs (change coupling)
- Look for: Areas with high bug density based on commit messages referencing fixes
- Look for: Areas with no test coverage that handle critical business logic
- Document: Risk map with type, evidence, and recommended mitigation

### Architectural Decisions
- Look for: Existing ADR files and their status (accepted, superseded, deprecated)
- Look for: Inferred decisions with no ADR (framework choices, database selection, auth approach)
- Assess: Whether key decisions are documented or only exist as tribal knowledge
- Document: Both explicit and inferred decisions with rationale and impact

### Quality Attributes Assessment
- Assess: Performance characteristics (response time indicators, caching, query optimization)
- Assess: Scalability approach (horizontal vs. vertical, stateless services, connection pooling)
- Assess: Maintainability (modularity, test coverage, documentation, onboarding ease)
- Assess: Security posture at architecture level (defense in depth, auth boundaries, data flow)
- Document: Current state vs. target for each quality attribute with gap analysis

### Integration Impact Assessment
- Look for: External systems involved (payment providers, SIS, identity providers)
- Assess: Whether integrations are new or modifications to existing flows
- Assess: PCI compliance needs (payment or financial systems)
- Assess: PII handling (user data, privacy requirements)
- Assess: Auth/authorization boundary changes
- Document: Integration impact table with security flags and story-level implications

## Key Questions to Answer

1. What is the overall architecture style, and is it consistently applied?
2. What are the system boundaries and who/what interacts with the system?
3. What containers (deployable units) exist and what technologies do they use?
4. How do components communicate, and where are the coupling hotspots?
5. What architectural decisions have been made, and which are undocumented?
6. Where are the highest-risk areas in terms of complexity, change frequency, and test coverage?
7. What technical debt exists and what is its ongoing cost to the team?
8. What external integrations exist and what compliance flags do they carry?
9. How do quality attributes (performance, scalability, security, maintainability) compare to targets?
10. What improvements would have the highest ROI if addressed first?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Layered Architecture | Separate `controllers/`, `services/`, `repositories/` dirs | Clear separation of concerns, easy to understand |
| Clean/Hexagonal Architecture | `domain/`, `ports/`, `adapters/` dirs, interface-heavy design | Strong domain isolation, testable, but may be over-engineered for simple apps |
| Event-Driven Architecture | Message broker configs, event handlers, pub/sub patterns | Loose coupling, eventual consistency, complex debugging |
| Modular Monolith | Single deployable with well-defined module boundaries | Good balance of simplicity and modularity |
| Distributed Monolith | Multiple services sharing a database or tightly coupled via sync calls | Worst of both worlds -- complexity of microservices without independence |
| Big Ball of Mud | No clear structure, mixed concerns, circular dependencies | High risk, difficult to change, needs refactoring plan |
| Strangler Fig | New and legacy systems coexisting, adapter layers | Active migration in progress |
| CQRS | Separate read/write models, projection handlers | Complex but scalable for read-heavy workloads |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No architecture documentation | Missing `docs/architecture/`, no ADRs, no C4 diagrams | HIGH |
| Circular dependencies between modules | Import analysis showing bidirectional dependencies | HIGH |
| Single points of failure | Critical path components with no redundancy or fallback | HIGH |
| Undocumented external integrations | API calls to external services with no integration docs | MEDIUM |
| Inconsistent architecture patterns | Mixed styles within same layer (some REST, some GraphQL, some raw SQL) | MEDIUM |
| High coupling between services | Shared databases, synchronous call chains across services | MEDIUM |
| Missing quality attribute targets | No SLOs, no performance benchmarks, no scalability plan | MEDIUM |
| Outdated architecture decisions | ADRs referencing deprecated technologies still in use | LOW |

## Output Guidance

### Must Include
- Architecture classification with style, communication patterns, and data architecture
- C4 model at levels 1-2 minimum (system context and container views)
- External dependency map with coupling assessment and security flags
- Technical debt inventory categorized by type with effort and priority
- Top 5 risk hotspots with evidence and recommended mitigation
- Quality attributes scorecard (performance, scalability, maintainability, security)

### Should Include (if detected)
- C4 level 3 component view for the most critical container
- Existing and inferred ADRs with status and impact
- Integration impact assessment with PCI/PII/auth flags
- Recommended architecture improvements with phased roadmap
- Debt interest calculations showing monthly cost of inaction

### Related Areas
- [backend-development](./backend-development.md) -- API design, service layer, data access patterns
- [frontend-development](./frontend-development.md) -- frontend architecture, component patterns
- [devops-infrastructure](./devops-infrastructure.md) -- deployment architecture, IaC, container strategy
- [security](./security.md) -- security posture at architecture level, auth boundaries
- [database-management](./database-management.md) -- data architecture, schema design
- [site-reliability](./site-reliability.md) -- reliability patterns, SLOs, observability
