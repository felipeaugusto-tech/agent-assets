# Product Management -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Product Management lens.
> This area combines Product Owner and Business Analyst perspectives.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| User-facing routes and pages | HIGH | `pages/`, `routes/`, `views/` with user-facing content |
| Business logic services | HIGH | `services/` with domain-specific naming (PaymentService, OrderService) |
| Domain model entities | HIGH | `models/`, `entities/` with business domain objects (User, Order, Product) |
| Feature flag configuration | MEDIUM | LaunchDarkly, Unleash, feature toggle files |
| API endpoints revealing features | MEDIUM | REST resources mapping to product features |
| Workflow or process engine config | MEDIUM | State machine definitions, BPMN files, workflow engine config |
| Multi-tenant or role configuration | MEDIUM | Tenant config, role definitions, permission matrices |
| Analytics or tracking integration | LOW | Segment, Mixpanel, Google Analytics, event tracking code |
| User onboarding flows | LOW | Onboarding components, setup wizards, tutorial code |
| Internationalization config | LOW | `i18n/`, locale files, translation keys |

## What to Analyze

### Feature Inventory
- Look for: All user-facing features by analyzing API endpoints, UI pages, and service classes
- Look for: Feature completeness indicators (fully implemented vs. partial vs. stubbed)
- Assess: Business value of each feature (high/medium/low based on domain context)
- Assess: Technical health of feature implementations
- Document: Feature inventory table with description, value, and technical health

### User Journey Mapping
- Look for: User-facing page/screen routes and their navigation flow
- Look for: User authentication and onboarding flows
- Look for: Key task completion paths (CRUD operations, checkout, reporting)
- Look for: Error and edge case handling in user flows
- Assess: Journey completeness and friction points
- Document: User journey map per persona with steps, gaps, and priority

### Domain Model Discovery
- Look for: Business entities and their relationships in code
- Look for: Business rules encoded in service logic, validators, and constraints
- Look for: Domain-specific terminology used in code (variable names, class names, comments)
- Look for: Workflow and state transitions (order status, approval flows, lifecycle management)
- Assess: Whether the domain model is well-structured or contains anemic entities
- Document: Domain entity table with relationships, business rules, and behavioral richness

### Business Process Mapping
- Look for: Process flows implemented in code (state machines, workflow engines, sequential steps)
- Look for: Decision points (conditional logic based on business rules)
- Look for: Process triggers (events, user actions, scheduled jobs)
- Look for: Process actors (user roles, external systems)
- Assess: Whether processes are well-structured and documented or buried in code
- Document: Process inventory with trigger, steps, actors, decision points, and outcome

### Requirements Reverse Engineering
- Look for: Implicit requirements encoded in validation rules, constraints, and business logic
- Look for: Non-functional requirements in configuration (rate limits, timeouts, pagination)
- Look for: Integration requirements (external API calls, webhooks, data sync)
- Assess: Whether requirements are documented or only exist in code
- Document: Inferred requirements mapped to code with type (functional/NFR) and documentation status

### Gap Analysis
- Look for: Industry-standard features missing for the domain
- Look for: Incomplete user journeys (abandoned flows, missing edge cases)
- Look for: Missing data validation or business rule enforcement
- Assess: Impact of each gap on user experience and business outcomes
- Document: Gap inventory with expected capability, current state, and effort estimate

### Data Dictionary
- Look for: Key business terms used in the codebase
- Look for: Entity/field names that map to business concepts
- Look for: Terminology inconsistencies (same concept, different names)
- Document: Business term glossary with code references and usage context

### Integration Points (Business View)
- Look for: External system interactions and their business purpose
- Look for: Data flow direction (inbound, outbound, bidirectional)
- Look for: Business rules applied during integration (validation, transformation)
- Assess: Business criticality of each integration
- Document: Integration map with purpose, data flow, and business rules

### Story and Epic Quality Assessment
- Look for: Whether acceptance criteria follow Gherkin format (Given/When/Then)
- Look for: Whether stories have clear problem statements and scope boundaries
- Look for: Whether integration and security impacts are identified
- Look for: Whether Definition of Ready criteria are met
- Assess: Story readiness for development
- Document: Story readiness assessment with common quality issues and recommendations

### Epic Quality Audit
- Look for: Business capability definition in epics
- Look for: Success metrics defined for epics
- Look for: Scope boundaries (in scope / out of scope)
- Look for: Integration and security impact flags
- Assess: Epic completeness for delivery planning
- Document: Epic quality assessment with field completeness per epic

## Key Questions to Answer

1. What features exist in the system and what is their business value?
2. What are the key user journeys and where are the gaps?
3. What domain model and business rules are encoded in the codebase?
4. What business processes are implemented and how are they triggered?
5. What requirements can be reverse-engineered from the code?
6. What industry-standard features are missing for this domain?
7. What external integrations exist and what is their business purpose?
8. What is the data dictionary for key business terms?
9. Are stories and epics ready for development per Definition of Ready standards?
10. What product improvements would deliver the highest value with the least effort?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Feature-Complete Module | Full CRUD + validation + tests + UI | Mature, production-ready feature |
| Partially Implemented Feature | API exists but UI incomplete, or vice versa | Technical debt or abandoned work |
| Domain-Driven Design | Bounded contexts, aggregates, domain events | Well-modeled business domain |
| Anemic Domain Model | Entities as data containers, all logic in services | Business rules scattered, harder to maintain |
| Feature Flags | Toggle-based feature activation | Progressive rollout capability |
| Multi-Tenant Architecture | Tenant isolation in data and config | Supports multiple customers/organizations |
| Workflow Engine | State machine or BPMN engine integration | Structured business process management |
| Analytics Integration | Event tracking, conversion funnels | Data-driven product decisions |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| Abandoned features | Incomplete implementations, commented-out code, unused routes | MEDIUM |
| Missing business rule enforcement | Business logic only in UI, no backend validation | HIGH |
| No user journey for critical paths | Missing UI flows for core features | HIGH |
| Inconsistent domain terminology | Same concept with different names across codebase | MEDIUM |
| No analytics or tracking | Missing event tracking, no user behavior data | MEDIUM |
| Stories without testable acceptance criteria | ACs missing, vague, or in wrong format | HIGH |
| Undocumented integration dependencies | External API calls with no documentation | MEDIUM |
| No scope boundaries on epics/stories | Scope creep risk, ambiguous requirements | MEDIUM |
| Implicit business rules | Critical business logic without documentation | HIGH |

## Output Guidance

### Must Include
- Feature inventory with business value and technical health
- User journey map for key personas with gaps identified
- Domain model summary with entity relationships and business rules
- Business process inventory with triggers and actors
- Gap analysis with missing capabilities prioritized by value and effort

### Should Include (if detected)
- Requirements reverse-engineered from code with traceability
- Data dictionary of key business terms
- Integration map with business purpose per external system
- Story and epic readiness assessment against Definition of Ready
- Value-effort matrix for improvement recommendations

### Related Areas
- [architecture](./architecture.md) -- system boundaries, C4 context diagram
- [backend-development](./backend-development.md) -- API endpoints, service layer revealing features
- [frontend-development](./frontend-development.md) -- UI pages and user-facing components
- [user-experience](./user-experience.md) -- UI flow analysis, accessibility
- [delivery-management](./delivery-management.md) -- DoR/DoD compliance, sprint readiness
- [technical-writing](./technical-writing.md) -- documentation coverage for features
