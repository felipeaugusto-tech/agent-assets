# SDLC Area Knowledge Index

> These knowledge files are used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> Each file tells the AI what to look for, analyze, and document when evaluating a codebase through a specific SDLC area's lens.

## SDLC Areas

| # | Area | File | Description | Top Detection Signals |
|---|------|------|-------------|----------------------|
| 1 | Architecture | [architecture.md](./sdlc-areas/architecture.md) | System architecture, C4 model, tech debt, ADRs, integration impact | Multiple service dirs, ADR files, IaC alongside app code |
| 2 | Backend Development | [backend-development.md](./sdlc-areas/backend-development.md) | API patterns, service layer, data access, error handling, auth | Server-side framework, route files, ORM config, service layer |
| 3 | Frontend Development | [frontend-development.md](./sdlc-areas/frontend-development.md) | Component patterns, state management, styling, build tooling | Frontend framework config, component files, state management |
| 4 | Fullstack Development | [fullstack-development.md](./sdlc-areas/fullstack-development.md) | End-to-end data flow, API contract, cross-stack patterns | Frontend + backend in same repo, shared types, Docker Compose |
| 5 | Quality Assurance | [quality-assurance.md](./sdlc-areas/quality-assurance.md) | Test coverage, gaps, automation infrastructure, AC testability | Test dirs, test framework config, CI test stages, E2E config |
| 6 | DevOps & Infrastructure | [devops-infrastructure.md](./sdlc-areas/devops-infrastructure.md) | CI/CD pipeline, containers, deployment, IaC, environment management | CI config, Dockerfile, Terraform/Pulumi, K8s manifests |
| 7 | Site Reliability | [site-reliability.md](./sdlc-areas/site-reliability.md) | Observability, SLOs, alerting, incident response, reliability patterns | Metrics config, health endpoints, alert rules, structured logging |
| 8 | Security | [security.md](./sdlc-areas/security.md) | Auth/authz, OWASP Top 10, secret management, input validation | Auth middleware, security headers, encryption libs, RBAC config |
| 9 | Database Management | [database-management.md](./sdlc-areas/database-management.md) | Schema design, migrations, query patterns, indexes, data integrity | Migration files, ORM models, DB config, SQL files |
| 10 | Product Management | [product-management.md](./sdlc-areas/product-management.md) | Feature inventory, user journeys, domain model, business processes | User-facing routes, business logic services, domain entities |
| 11 | Delivery Management | [delivery-management.md](./sdlc-areas/delivery-management.md) | DORA metrics, bottlenecks, DoR/DoD compliance, rework signals | PR history, CI/CD stages, test coverage config, branch protection |
| 12 | Technical Leadership | [technical-leadership.md](./sdlc-areas/technical-leadership.md) | Code quality, conventions, PR standards, onboarding readiness | Linting config, PR template, CODEOWNERS, quality gates in CI |
| 13 | User Experience | [user-experience.md](./sdlc-areas/user-experience.md) | UI inventory, accessibility, design system, user flows | Component library, theme config, page routes, ARIA attributes |
| 14 | Technical Writing | [technical-writing.md](./sdlc-areas/technical-writing.md) | Documentation coverage, API docs, quality, infrastructure | docs/ directory, README, OpenAPI spec, doc build config |
| 15 | Release Management | [release-management.md](./sdlc-areas/release-management.md) | Versioning, changelog, release process, rollback, risk | Version files, CHANGELOG.md, release workflows, Git tags |
| 16 | Support Engineering | [support-engineering.md](./sdlc-areas/support-engineering.md) | Error messages, configuration, diagnostics, troubleshooting | Error definitions, health endpoints, logging config, FAQ docs |

## How Areas Are Selected

During Phase 2 (Detect Relevant Areas), the role-detector agent uses the **Detection Signals** table in each area file to determine which areas are relevant for a given codebase. Areas are selected when their signals match files and patterns found in the target repository.

## Cross-References

Areas are interconnected. Each area file includes a **Related Areas** section at the bottom that identifies which other areas have overlapping concerns. When analyzing a codebase, findings in one area often inform analysis in related areas.

### Common Groupings

- **Development Core:** Architecture + Backend + Frontend + Fullstack + Database
- **Quality & Testing:** Quality Assurance + Security + Site Reliability
- **Process & Delivery:** Product Management + Delivery Management + Release Management
- **Developer Experience:** Technical Leadership + Technical Writing + Support Engineering
- **User-Facing:** Frontend + User Experience + Support Engineering
