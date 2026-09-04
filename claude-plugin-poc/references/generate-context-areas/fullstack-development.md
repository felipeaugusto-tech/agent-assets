# Fullstack Development -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Fullstack Development lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Frontend and backend code coexisting | HIGH | `frontend/` + `backend/`, `client/` + `server/`, `apps/web/` + `apps/api/` |
| Monorepo with web and API packages | HIGH | `packages/`, `apps/` with both UI and server entries in workspace config |
| Full-stack framework config | HIGH | `next.config.js` with API routes, `nuxt.config.ts` with server middleware |
| Shared type/schema definitions | MEDIUM | `shared/`, `common/`, `types/` referenced by both frontend and backend |
| Docker Compose with frontend + backend services | MEDIUM | `docker-compose.yml` with web and API services |
| API client generation config | MEDIUM | OpenAPI codegen, GraphQL codegen, tRPC router definitions |
| Database + UI in same repo | LOW | Migration files alongside component files |

## What to Analyze

### Repository Structure
- Look for: How frontend and backend code are organized (monorepo, polyrepo, single directory)
- Look for: Shared code locations (types, utilities, validation schemas, constants)
- Look for: Infrastructure and configuration files
- Assess: Whether separation is clean or concerns are mixed
- Document: Full-stack layout map with tech stack per area

### End-to-End Data Flow
- Look for: Complete request lifecycle for key features (UI action to database and back)
- Look for: Data transformation points between layers
- Look for: Serialization/deserialization boundaries
- Assess: Whether data shapes are consistent across the stack or require mapping
- Document: Data flow traces for 2-3 key features showing each layer's role

### API Contract
- Look for: How frontend and backend agree on data shapes
- Look for: Type sharing mechanism (shared packages, code generation, manual sync)
- Look for: API client abstraction on the frontend side
- Look for: Route handler patterns on the backend side
- Assess: Whether contract drift is possible (e.g., no shared types, no generated client)
- Document: API contract approach with type sharing mechanism and drift risk

### Authentication Flow
- Look for: Login, persist, refresh, and logout flows across both frontend and backend
- Look for: Token storage on the frontend (localStorage, cookies, memory)
- Look for: Token validation on the backend (middleware, guards)
- Look for: Session refresh mechanism and rotation
- Assess: Security of the full auth flow end-to-end
- Document: Auth flow with frontend and backend responsibilities at each step

### Cross-Stack Error Handling
- Look for: How backend errors are formatted and sent to the frontend
- Look for: How the frontend interprets and displays errors to users
- Look for: Error boundary and global error handler implementations
- Assess: Whether error handling is consistent and user-friendly across the stack
- Document: Error handling strategy per error type (validation, auth, not-found, server) across both layers

### Development Workflow
- Look for: Commands to start the full stack locally
- Look for: Docker Compose or similar orchestration for local development
- Look for: API mocking for frontend-only development
- Look for: Test database setup for backend-only development
- Document: Development workflow with commands, prerequisites, and tips

### Shared Patterns
- Look for: Shared validation logic (same rules on frontend and backend)
- Look for: Shared date/time handling libraries
- Look for: Shared formatting utilities and constants
- Assess: Whether duplication exists where shared code could reduce inconsistency
- Document: Shared pattern inventory with frontend, backend, and shared code locations

### Feature Development Lifecycle
- Look for: What layers need changes when adding a full-stack feature
- Look for: Migration, model, service, endpoint, client, state, component pattern
- Assess: How many files/layers a typical feature touches
- Document: Feature development checklist with steps at each layer

## Key Questions to Answer

1. How is the repository structured for frontend and backend code?
2. What is the complete data flow for a key user action?
3. How do frontend and backend share type definitions and API contracts?
4. How does authentication work end-to-end?
5. How are errors handled across the full stack?
6. What commands start the full development environment?
7. What code is shared between frontend and backend?
8. What is the step-by-step process to add a new full-stack feature?
9. How are environment variables managed across frontend and backend?
10. What are the CORS and proxy configurations?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| tRPC / End-to-End Type Safety | tRPC router definitions, shared type inference | Full type safety, no API contract drift |
| OpenAPI Code Generation | `openapi-generator` config, generated client code | Strong contract, but generated code may need updates |
| GraphQL Schema Sharing | `.graphql` files, codegen config | Strong typing via schema, but adds complexity |
| Manual API Contract | Separate type definitions in frontend and backend | High risk of contract drift, needs discipline |
| Full-Stack Framework | Next.js API routes, Nuxt server routes, Remix loaders | Simplified architecture, co-located API and UI |
| BFF (Backend for Frontend) | Dedicated API layer tailored to frontend needs | Optimized frontend data fetching, extra layer to maintain |
| Shared Monorepo Package | `packages/shared/` with types, utils, validation | DRY across stack, but coupling risk |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No shared types between frontend and backend | Separate type definitions with no codegen or shared package | HIGH |
| CORS misconfiguration | Overly permissive CORS policy (`*` origin) or missing CORS | HIGH |
| Auth token in localStorage | Frontend storing JWT in localStorage instead of httpOnly cookies | MEDIUM |
| Inconsistent validation rules | Different validation on frontend vs backend for same input | MEDIUM |
| No API versioning | Breaking backend changes without frontend migration path | MEDIUM |
| Environment variable mismatch | Frontend and backend expecting different env var names for same config | LOW |
| No full-stack integration tests | Unit tests exist per layer but no end-to-end flow tests | MEDIUM |
| Duplicated business logic | Same calculation or rule implemented separately in frontend and backend | LOW |

## Output Guidance

### Must Include
- Repository structure showing frontend, backend, and shared code locations
- Tech stack per layer (framework, language, database, build tool)
- End-to-end data flow for at least one key feature
- API contract approach and type sharing mechanism
- Authentication flow across the full stack
- Cross-stack error handling strategy
- Development workflow commands and setup

### Should Include (if detected)
- Shared code inventory (types, validation, utilities)
- Feature development checklist with per-layer steps
- CORS and proxy configuration details
- Environment variable management per layer
- Integration testing strategy across the stack

### Related Areas
- [frontend-development](./frontend-development.md) -- detailed frontend patterns and conventions
- [backend-development](./backend-development.md) -- detailed backend patterns and conventions
- [architecture](./architecture.md) -- overall system architecture and C4 model
- [quality-assurance](./quality-assurance.md) -- cross-stack testing strategy
- [devops-infrastructure](./devops-infrastructure.md) -- full-stack deployment and environment management
