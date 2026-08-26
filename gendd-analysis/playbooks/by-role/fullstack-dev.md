# Role Playbook: Full-Stack Developer

**Role:** Full-Stack Developer
**Focus:** End-to-end patterns, integration points, full data flow
**Time:** 45-60 minutes

---

## Purpose

Analyze a codebase from a Full-Stack Developer perspective to understand:
- Complete request/response flow from UI to database
- Integration points between frontend and backend
- Shared patterns and conventions
- Development workflow for full-stack features

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/fullstack-dev.md
Analyze @TargetRepo for end-to-end patterns.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/fullstack-dev.md

Analyze @TargetRepo from a Full-Stack Developer perspective:

## Context
- Frontend: [React | Vue | Angular | Other]
- Backend: [Node.js | Go | .NET | Python | Other]
- Database: [PostgreSQL | MongoDB | Other]
- Monorepo: [Yes/No]

## Phase 1: Repository Structure

Map the full-stack layout:
| Area | Location | Tech Stack |
|------|----------|------------|
| Frontend | [path] | [framework, tools] |
| Backend | [path] | [framework, tools] |
| Shared | [path] | [types, utils] |
| Database | [path] | [migrations, seeds] |
| Infrastructure | [path] | [Docker, K8s] |

## Phase 2: End-to-End Data Flow

For key features, trace the full flow:

### Feature: [Feature Name]
| Layer | Component | Action | Data |
|-------|-----------|--------|------|
| UI | `Component.tsx` | User clicks button | - |
| Frontend State | `store/slice.ts` | Dispatch action | Request payload |
| API Client | `api/client.ts` | HTTP POST | JSON body |
| Backend Route | `routes/api.ts` | Handle request | Validated input |
| Service | `services/X.ts` | Business logic | Domain objects |
| Repository | `repos/X.ts` | Database query | SQL/ORM |
| Database | Table X | Insert/Update | Row data |
| Response | ← | Return data | JSON response |
| UI Update | `Component.tsx` | Re-render | Updated state |

## Phase 3: API Contract

Document the frontend-backend contract:
| Endpoint | Frontend Consumer | Backend Handler | Shared Types |
|----------|-------------------|-----------------|--------------|
| `POST /api/users` | `useCreateUser()` | `UserController.Create` | `CreateUserRequest` |

Type sharing approach: [Shared package | Code gen | Manual sync]

## Phase 4: Authentication Flow

| Step | Frontend | Backend | Storage |
|------|----------|---------|---------|
| Login | [Component] | [Endpoint] | [Token storage] |
| Persist | [How] | [Validation] | [Session/Token] |
| Refresh | [Trigger] | [Endpoint] | [Rotation] |
| Logout | [Action] | [Endpoint] | [Cleanup] |

## Phase 5: Error Handling Across Stack

| Error Type | Frontend Handling | Backend Response | User Feedback |
|------------|-------------------|------------------|---------------|
| Validation | Form errors | `400 + details` | Field messages |
| Auth | Redirect to login | `401` | Toast/redirect |
| Not Found | Error page/message | `404` | "Not found" UI |
| Server Error | Error boundary | `500 + log` | Generic message |

## Phase 6: Development Workflow

| Task | Commands | Notes |
|------|----------|-------|
| Start all | [command] | Full stack dev |
| Frontend only | [command] | With API mock |
| Backend only | [command] | With test DB |
| Run tests | [command] | All tests |
| Build | [command] | Production build |

## Phase 7: Shared Patterns

| Pattern | Frontend | Backend | Shared Code |
|---------|----------|---------|-------------|
| Validation | [Library] | [Library] | [Shared schema?] |
| Date handling | [Library] | [Library] | [Shared utils?] |
| Formatting | [Utils] | [Utils] | [Shared?] |
| Constants | [Location] | [Location] | [Shared?] |

## Phase 8: Feature Development Checklist

When adding a full-stack feature:
- [ ] Database migration
- [ ] Backend model
- [ ] Repository method
- [ ] Service method
- [ ] API endpoint
- [ ] API client function
- [ ] Frontend state slice
- [ ] UI component
- [ ] Tests at each layer
```

---

## Output: Full-Stack Developer Guide

```markdown
# Full-Stack Developer Guide: [Project Name]
Generated: [Date]
Analyzed by: Full-Stack Dev Playbook

## Architecture Overview

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Frontend   │────▶│   Backend    │────▶│   Database   │
│   [Tech]     │◀────│   [Tech]     │◀────│   [Tech]     │
└──────────────┘     └──────────────┘     └──────────────┘
```

## Quick Start

### Full Stack Development
```bash
# Terminal 1: Backend
cd backend && [start command]

# Terminal 2: Frontend
cd frontend && [start command]

# Or use docker-compose
docker-compose up
```

## End-to-End Flow Example

### Creating a User
```
1. UI: UserForm.tsx submits form
2. State: userSlice.createUser() dispatched
3. API: POST /api/users with user data
4. Route: userRouter handles request
5. Service: userService.create() validates & creates
6. Repo: userRepository.insert() saves to DB
7. Response: Created user returned
8. State: User added to store
9. UI: UserList re-renders with new user
```

## API Contract

### Endpoints Overview
| Method | Endpoint | Frontend | Backend |
|--------|----------|----------|---------|

### Type Sharing
[How types are shared between frontend and backend]

## Adding a Feature

### 1. Database
```sql
-- migration
```

### 2. Backend Model
```go
// model
```
See `[backend model example]`

### 3. Backend Service
```go
// service method
```
See `[backend service example]`

### 4. API Endpoint
```go
// route handler
```
See `[backend route example]`

### 5. Frontend API Client
```typescript
// api client function
```
See `[frontend api example]`

### 6. Frontend State
```typescript
// state slice
```
See `[frontend state example]`

### 7. UI Component
```tsx
// component
```
See `[frontend component example]`

## Testing Strategy

| Layer | Test Type | Command |
|-------|-----------|---------|
| Frontend Unit | Jest/Vitest | `npm run test:unit` |
| Frontend E2E | Playwright | `npm run test:e2e` |
| Backend Unit | [framework] | `go test ./...` |
| Backend Integration | [framework] | `go test -tags=integration` |
| API Contract | [tool] | `npm run test:contract` |

## Common Gotchas

1. **CORS:** [How it's handled]
2. **Auth tokens:** [Where stored, how refreshed]
3. **API versioning:** [How managed]
4. **Environment variables:** [Frontend vs Backend]
```

---

## Follow-Up Actions

- For AI context setup: [Create Context Pack](../../workflows/create-context-pack.md) — so AI tools follow your conventions across the full stack
- For architecture diagrams: [Generate Architecture Diagrams](../../workflows/generate-architecture-diagrams.md) — C4 diagrams showing end-to-end system architecture
- For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
