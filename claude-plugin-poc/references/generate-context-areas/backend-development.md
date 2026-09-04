# Backend Development -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Backend Development lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Server-side framework files | HIGH | `go.mod`, `package.json` with Express/Nest/Fastify, `*.csproj` with ASP.NET, `requirements.txt` with Django/Flask |
| API route definitions | HIGH | `routes/`, `controllers/`, `handlers/`, `*Controller.cs`, `*_handler.go` |
| ORM or data access configuration | HIGH | `prisma/schema.prisma`, `ormconfig.ts`, `models.py`, EF Core migrations |
| Service layer files | HIGH | `services/`, `*Service.ts`, `*_service.go`, `*Service.cs` |
| Middleware or request pipeline config | MEDIUM | `middleware/`, `app.use()`, `UseAuthentication()`, interceptors |
| Database migration files | MEDIUM | `migrations/`, `db/migrate/`, Flyway, Alembic files |
| API specification files | MEDIUM | `openapi.yaml`, `swagger.json`, `*.proto` (gRPC) |
| Repository pattern files | LOW | `repositories/`, `*Repository.ts`, `*_repo.go` |
| Background job/worker files | LOW | `jobs/`, `workers/`, `queues/`, Bull/Sidekiq/Hangfire config |

## What to Analyze

### Project Structure
- Look for: Directory layout and how backend code is organized (by feature, by layer, by domain)
- Assess: Whether the structure is consistent and follows a clear pattern
- Document: Directory map with purpose and key files per directory

### API Design and Patterns
- Look for: REST resource naming conventions (plural nouns, versioning, nesting depth)
- Look for: Request/response format (JSON envelope patterns, pagination, filtering, sorting)
- Look for: API versioning strategy (URL path, header, query param)
- Look for: Input validation approach (schema validation, decorators, middleware)
- Assess: Consistency of API design across all endpoints
- Document: API pattern table with endpoint conventions, request/response formats, and examples

### Service Layer Architecture
- Look for: Service classes/modules and their responsibilities
- Look for: Dependency injection patterns (constructor injection, DI containers, manual wiring)
- Assess: Single Responsibility adherence in services
- Assess: Service-to-service dependencies and potential circular references
- Document: Service inventory with responsibilities, dependencies, and key methods

### Data Access Patterns
- Look for: Repository pattern implementation
- Look for: Unit of Work pattern (transaction management)
- Look for: ORM usage patterns vs. raw SQL
- Look for: Migration tools and migration history
- Look for: Database seeding approach
- Assess: Query efficiency (N+1 queries, missing eager loading, SELECT *)
- Document: Data access patterns with implementation details and anti-patterns found

### Error Handling
- Look for: Global error handling middleware
- Look for: Custom error classes/types
- Look for: Error response format consistency
- Assess: Whether errors are properly categorized (validation, auth, not-found, server)
- Assess: Whether sensitive information leaks in error responses
- Document: Error handling patterns with response format per error type

### Authentication and Authorization
- Look for: Auth method (JWT, session-based, OAuth 2.0, API keys)
- Look for: Token storage and expiry configuration
- Look for: Permission model (RBAC, ABAC, custom)
- Look for: Auth middleware and how protected routes are defined
- Assess: Consistency of auth enforcement across endpoints
- Document: Auth implementation details with method, token handling, and permission model

### External Integrations
- Look for: HTTP client instances and their configuration
- Look for: Retry logic, circuit breakers, timeout settings
- Look for: API client wrappers for third-party services
- Assess: Error handling for external service failures
- Assess: Whether integrations are abstracted behind interfaces
- Document: Integration inventory with purpose, client pattern, and resilience mechanisms

### Testing Patterns
- Look for: Unit test framework and conventions
- Look for: Integration test setup (test databases, Docker containers)
- Look for: API/contract test patterns
- Look for: Mocking strategies and test doubles
- Assess: Coverage distribution across service, repository, and controller layers
- Document: Test pattern summary with framework, patterns, and coverage by layer

### Conventions and Standards
- Look for: Naming conventions (files, classes, functions, variables)
- Look for: File structure patterns (feature folders, layer folders)
- Look for: Logging approach (structured logging, log levels, correlation IDs)
- Look for: Configuration management (env vars, config files, secret handling)
- Document: Convention reference table with rules and examples

## Key Questions to Answer

1. What language and framework powers the backend, and what version?
2. How is the project structured and what pattern does it follow?
3. What API style is used and how are endpoints organized?
4. How does the service layer manage business logic and dependencies?
5. What ORM or data access pattern is used, and are there query anti-patterns?
6. How are errors handled and communicated to clients?
7. What authentication and authorization mechanisms are in place?
8. What external services does the backend integrate with?
9. What testing patterns exist and where are the coverage gaps?
10. What conventions should a new developer follow?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Repository Pattern | `*Repository` classes, interface + implementation separation | Clean data access abstraction, testable |
| CQRS | Separate command/query handlers, different read/write models | Complex but scalable, may indicate event sourcing |
| Mediator Pattern | MediatR, command/query handlers, pipeline behaviors | Decoupled request handling, good for complex domains |
| Event-Driven Services | Event publishers/subscribers, message handlers | Loose coupling, eventual consistency concerns |
| Monolithic Service Layer | Single large service handling multiple concerns | Needs refactoring, high change risk |
| Anemic Domain Model | Entities with only getters/setters, all logic in services | Business logic scattered, harder to maintain |
| Rich Domain Model | Entities with behavior, domain events, value objects | DDD approach, well-encapsulated business logic |
| API Gateway Pattern | Central routing, rate limiting, auth at gateway level | Microservices infrastructure, centralized cross-cutting concerns |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No input validation on API endpoints | Missing validation middleware, no schema validation | HIGH |
| SQL injection vulnerability | String concatenation in queries, no parameterized queries | HIGH |
| Missing auth on sensitive endpoints | Routes without auth middleware accessing protected data | HIGH |
| N+1 query patterns | Loop-based database calls, missing eager loading | MEDIUM |
| No error handling middleware | Unhandled exceptions reaching clients with stack traces | MEDIUM |
| Hardcoded configuration values | Connection strings, API keys in source code | MEDIUM |
| Missing retry/timeout on external calls | HTTP clients without timeout or retry configuration | MEDIUM |
| No database migration strategy | Schema changes applied manually, no migration files | LOW |
| Inconsistent API conventions | Mixed naming styles, inconsistent response formats | LOW |

## Output Guidance

### Must Include
- Language, framework, and runtime version
- Project structure map with directory purposes
- API design patterns with endpoint conventions and response format
- Service layer inventory with dependency graph
- Data access patterns and ORM/query approach
- Authentication and authorization implementation summary
- Error handling strategy and response format

### Should Include (if detected)
- External integration inventory with resilience patterns
- Testing patterns and coverage by layer
- Convention reference for new developers
- Query anti-patterns found (N+1, SELECT *, missing indexes)
- Background job/worker architecture

### Related Areas
- [architecture](./architecture.md) -- overall system architecture and C4 model
- [database-management](./database-management.md) -- schema design, migration strategy, query optimization
- [security](./security.md) -- auth implementation details, input validation, secret management
- [quality-assurance](./quality-assurance.md) -- test coverage, test patterns, gap analysis
- [fullstack-development](./fullstack-development.md) -- API contract between frontend and backend
