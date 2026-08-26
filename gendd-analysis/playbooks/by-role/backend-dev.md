# Role Playbook: Backend Developer

**Role:** Backend Developer
**Focus:** API patterns, service conventions, data access, error handling
**Time:** 30-45 minutes

---

## Purpose

Analyze a codebase from a Backend Developer perspective to understand:
- API design and patterns
- Service layer architecture
- Data access patterns
- Error handling conventions
- Authentication and authorization

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/backend-dev.md
Analyze @TargetRepo for backend patterns and conventions.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/backend-dev.md

Analyze @TargetRepo from a Backend Developer perspective:

## Context
- Language/Framework: [Go | .NET | Node.js | Python | Java | Other]
- API Style: [REST | GraphQL | gRPC | Mixed]
- Database: [PostgreSQL | MySQL | MongoDB | Other]
- ORM/Data Access: [EF Core | GORM | Prisma | Sequelize | Raw SQL]

## Phase 1: Project Structure

Map the backend architecture:
| Directory | Purpose | Key Files |
|-----------|---------|-----------|
| `src/api/` | API endpoints | [patterns] |
| `src/services/` | Business logic | [patterns] |
| `src/repositories/` | Data access | [patterns] |
| `src/models/` | Data models | [patterns] |
| `src/middleware/` | Request pipeline | [patterns] |
| `src/utils/` | Utilities | [patterns] |

## Phase 2: API Design

Document API patterns:
| Endpoint Pattern | Example | Convention |
|------------------|---------|------------|
| REST resources | `GET /api/users/:id` | [plural nouns] |
| Versioning | `/api/v1/` | [URL path] |
| Request format | JSON body | [validation] |
| Response format | `{data, error, meta}` | [envelope] |
| Pagination | `?page=1&limit=20` | [offset/cursor] |
| Filtering | `?status=active` | [query params] |

## Phase 3: Service Layer

Analyze service patterns:
| Service | Responsibility | Dependencies | Key Methods |
|---------|---------------|--------------|-------------|
| [UserService] | User management | UserRepo, EmailService | Create, Update, Delete |
| [AuthService] | Authentication | UserRepo, TokenService | Login, Logout, Refresh |

Dependency injection: [Pattern used]

## Phase 4: Data Access

Document data patterns:
| Pattern | Implementation | Example |
|---------|----------------|---------|
| Repository | [Yes/No] | `UserRepository.FindById()` |
| Unit of Work | [Yes/No] | [Transaction handling] |
| Migrations | [Tool] | `migrations/` |
| Seeding | [Approach] | `seeds/` |

## Phase 5: Error Handling

| Error Type | Handling | Response Format |
|------------|----------|-----------------|
| Validation | [approach] | `{errors: [...]}` |
| Not Found | [approach] | `404` |
| Auth errors | [approach] | `401/403` |
| Server errors | [approach] | `500 + logging` |

## Phase 6: Authentication & Authorization

| Aspect | Implementation | Files |
|--------|----------------|-------|
| Auth method | [JWT/Session/OAuth] | [files] |
| Token storage | [Where] | [files] |
| Permission model | [RBAC/ABAC/Custom] | [files] |
| Middleware | [Implementation] | [files] |

## Phase 7: External Integrations

| Integration | Purpose | Client Pattern | Error Handling |
|-------------|---------|----------------|----------------|
| [Service] | [Why] | HTTP client | Retry + Circuit breaker |

## Phase 8: Testing Patterns

| Test Type | Framework | Pattern | Coverage |
|-----------|-----------|---------|----------|
| Unit | [framework] | Mocked dependencies | [%] |
| Integration | [framework] | Test database | [%] |
| API/Contract | [framework] | Request tests | [endpoints] |

## Phase 9: Conventions

| Convention | Rule | Example |
|------------|------|---------|
| Naming | [style] | `userService` |
| File structure | [pattern] | `feature/` folders |
| Logging | [library] | Structured JSON |
| Config | [approach] | Env vars + config file |
```

---

## Output: Backend Developer Guide

```markdown
# Backend Developer Guide: [Project Name]
Generated: [Date]
Analyzed by: Backend Dev Playbook

## Quick Start for Backend Devs

### Setup
```bash
[Setup commands]
```

### Key Directories
- API: `src/api/`
- Services: `src/services/`
- Data: `src/repositories/`
- Models: `src/models/`

## Architecture Overview

### Request Flow
```
Request → Middleware → Controller → Service → Repository → Database
                ↓
            Response ← [Transform] ← Result
```

### Service Dependencies
```
[Dependency diagram]
```

## API Conventions

### Creating an Endpoint
```go
// [Example following project conventions]
```
See `[example file path]` for reference.

### Request Validation
```go
// [Pattern for validation]
```
See `[example file path]` for reference.

### Error Responses
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "...",
    "details": [...]
  }
}
```

## Data Access

### Repository Pattern
```go
// [Example following project conventions]
```
See `[example file path]` for reference.

### Migrations
```bash
[Migration commands]
```

## Common Tasks

| Task | How To |
|------|--------|
| Add endpoint | [steps] |
| Add service | [steps] |
| Add migration | [steps] |
| Add integration | [steps] |

## Authentication

### Protected Endpoints
```go
// [Pattern for auth middleware]
```

### Permission Checks
```go
// [Pattern for authorization]
```

## Testing

### Running Tests
```bash
[test commands]
```

### Writing Tests
See `[example test file]` for pattern.

## Gotchas & Tips
1. [Important gotcha]
2. [Helpful tip]
3. [Common mistake to avoid]
```

---

## Reference Templates

This playbook's analysis areas align with the universal principles in the Context Pack template. Reference them for baseline expectations:

| Template | Relevant Sections |
|----------|-------------------|
| `templates/context-pack.md` (conventions.md section) | Naming conventions, SRP, error handling, DI, logging (levels, what never to log) |
| `templates/context-pack.md` (agents.md section) | Multi-tenant isolation, input validation, parameterized queries, secret handling |
| `templates/context-pack.md` (testing.md section) | AAA pattern, test naming, mocking guidelines, required scenarios |

---

## Follow-Up Actions

- For AI context setup: [Create Context Pack](../../workflows/create-context-pack.md) — so AI tools follow your backend conventions and patterns
- For architecture overview: [Generate Architecture Diagrams](../../workflows/generate-architecture-diagrams.md) — understand system context and container relationships
- For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
