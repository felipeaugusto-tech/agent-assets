# Context Pack Template

> **DEPRECATED**: This template has been replaced by:
> - [Context Area Template](./context-area.md) -- for per-area context documents
> - [Standards Templates](./standards/) -- for standards per SDLC area
> - [IDE Rule Templates](./ide-rules/) -- for IDE-specific rule files

> **Related:** [Create Context Pack Workflow](../workflows/create-context-pack.md)

## Purpose
This template provides starter content for each Context Pack file. It embeds universal engineering principles that every Context Pack should inherit, alongside `{PLACEHOLDER}` values that must be customized for each repository.

**How to use:** Copy each file section into your repository's `.cursor/` folder, replace `{PLACEHOLDER}` values with repository-specific details, and add code examples from your actual codebase.

---

## File 1: agents.md

```markdown
# AI Agent Instructions

## Identity
You are an AI assistant helping develop {PRODUCT_NAME}, a {BRIEF_DESCRIPTION}.

## Your Role
- Generate code that follows our established patterns
- Help identify issues before they reach production
- Accelerate development while maintaining quality
- Ask clarifying questions when requirements are ambiguous

## Compliance Context

This repository may operate under one or more compliance regimes:

| Compliance | Applies When |
|------------|--------------|
| **PCI DSS** | Repository handles or transmits payment card data |
| **FERPA** | Repository handles student education records |
| **HIPAA** | Repository handles protected health information |
| **General Privacy** | Repository handles any personally identifiable information (PII) |

**This repository's compliance scope:** {COMPLIANCE_SCOPE}

## Security Rules (Non-Negotiable)

### Never Hardcode Secrets
Secrets, credentials, and sensitive configuration MUST NEVER appear in source code.

| Category | Examples |
|----------|----------|
| **Authentication** | Passwords, API keys, tokens, certificates, private keys |
| **Connection Strings** | Database credentials, service URLs with embedded passwords |
| **Encryption** | Encryption keys, signing keys, salt values |
| **External Services** | Third-party API keys, webhook secrets |

Use environment variables, secret management systems, or configuration files excluded from version control.

### Never Log Sensitive Data

| Category | Examples | Why |
|----------|----------|-----|
| **Authentication** | Passwords, API keys, tokens, session IDs, JWTs | Can be used to impersonate |
| **Payment** | Credit card numbers (full or partial), CVV, bank accounts | PCI compliance |
| **Personal Identifiers** | SSN, driver's license, passport numbers | Identity theft |
| **Health Information** | Medical records, diagnoses | HIPAA compliance |
| **Personal Contact** | Email + name combinations, physical addresses | Privacy regulations |

When referencing sensitive data in logs, mask it:
- Credit card: last 4 only (`****4242`)
- Email: partial (`j***@example.com`)
- Token: never log — use request ID instead

### Validate All Input
Never trust input from external sources (user input, APIs, files, URLs, environment). Validate type, format, length, range, and encoding. Use parameterized queries — never string concatenation in SQL.

### Multi-Tenant Data Isolation
Every backend database operation MUST include tenant context. Tenant context comes from the server, never from client-supplied IDs. Cross-tenant access must be architecturally impossible.

| Tenant Model | How It Works |
|-------------|-------------|
| **Database-per-tenant** | Each tenant gets its own database; tenant resolved from request context |
| **Schema-per-tenant** | Shared database, separate schemas per tenant |
| **Shared DB with tenant column** | Single database, every table has a `tenant_id` / `site_id` column |
| **Host-based routing** | Tenant derived from request hostname or subdomain |

**This repository's tenant model:** {TENANT_MODEL}

### Authentication and Authorization
- Verify auth on every request — don't cache authentication decisions
- Use standard protocols (OAuth2, OIDC, JWT with proper validation)
- Check authorization before every action; fail closed (deny if check fails)
- Log authorization failures

### Secure Error Handling
- End users: friendly message, action to take — never stack traces or internal details
- Logs: full details, stack trace, context — never sensitive data
- API responses: error code, safe message — never database schema, file paths, or internal IPs

## What You Can Help With
- Writing code following our patterns (see conventions.md)
- Generating tests following our standards (see testing.md)
- Understanding system architecture (see architecture.md)
- Enhancing requirements with edge cases
- Reviewing code for common issues

## What You Should Not Do
- Generate code that bypasses authentication or authorization
- Hardcode credentials, secrets, or API keys
- Create SQL without parameterization
- Skip error handling for external calls
- Ignore multi-tenant data isolation
- Log sensitive data (PII, cards, tokens, passwords)
- Expose internal details in API error responses

## Security Code Review Checklist

### Secrets
- [ ] No hardcoded secrets, keys, or passwords
- [ ] Secret files are in `.gitignore`
- [ ] Secrets are loaded from secure sources

### Input Handling
- [ ] All external input is validated
- [ ] SQL queries use parameterization
- [ ] User input is encoded before rendering

### Logging
- [ ] No sensitive data in logs
- [ ] Authentication failures are logged
- [ ] Errors don't leak internal details

### Multi-Tenant Isolation (Backend)
- [ ] Every database query includes tenant context
- [ ] Tenant context is derived server-side
- [ ] No code path allows cross-tenant data access

### Access Control
- [ ] Authentication is required for protected resources
- [ ] Authorization checks are in place
- [ ] Principle of least privilege is followed

### Dependencies
- [ ] No known vulnerabilities in dependencies
- [ ] Dependencies are from trusted sources

## Communication Style
- Be concise and specific
- Reference existing code patterns when relevant
- Highlight security/compliance concerns proactively
- Ask clarifying questions rather than assume
```

---

## File 2: context.md

```markdown
# System Context

## Overview
{PRODUCT_NAME} is a {TYPE_OF_SYSTEM} that enables {KEY_VALUE_PROPOSITION} for {TARGET_USERS}.

## Domain Glossary

| Term | Definition | Example in Code |
|------|------------|-----------------|
| {TERM_1} | {DEFINITION_1} | `{CODE_REFERENCE_1}` |
| {TERM_2} | {DEFINITION_2} | `{CODE_REFERENCE_2}` |
| {TERM_3} | {DEFINITION_3} | `{CODE_REFERENCE_3}` |

## User Personas

### {PERSONA_1}
- **Goal**: {PRIMARY_GOAL}
- **Actions**: {KEY_ACTIONS}
- **Code Areas**: `{RELEVANT_CODE_AREAS}`

### {PERSONA_2}
- **Goal**: {PRIMARY_GOAL}
- **Actions**: {KEY_ACTIONS}
- **Code Areas**: `{RELEVANT_CODE_AREAS}`

## Key Integrations

| Integration | Purpose | Code Location |
|-------------|---------|---------------|
| {INTEGRATION_1} | {PURPOSE_1} | `{CODE_PATH_1}` |
| {INTEGRATION_2} | {PURPOSE_2} | `{CODE_PATH_2}` |
| {INTEGRATION_3} | {PURPOSE_3} | `{CODE_PATH_3}` |

## Business Rules

### {BUSINESS_AREA_1}
- {RULE_1}
- {RULE_2}
- {RULE_3}

### {BUSINESS_AREA_2}
- {RULE_1}
- {RULE_2}

## Compliance Requirements
- **{COMPLIANCE_1}**: {REQUIREMENT}
- **{COMPLIANCE_2}**: {REQUIREMENT}
```

---

## File 3: conventions.md

```markdown
# Coding Conventions

## File Organization

```
src/
├── {FOLDER_1}/     # {PURPOSE_1}
├── {FOLDER_2}/     # {PURPOSE_2}
├── {FOLDER_3}/     # {PURPOSE_3}
└── {FOLDER_4}/     # {PURPOSE_4}
```

## Naming Conventions

### Universal Rules

| Element Type | Convention | Good Examples | Bad Examples |
|--------------|------------|---------------|--------------|
| **Variables/Fields** | Describe what it holds | `userEmail`, `orderTotal`, `isActive` | `x`, `temp`, `data` |
| **Functions/Methods** | Verb + noun (action) | `getUserById`, `calculateTotal`, `validateInput` | `process`, `doIt`, `handle` |
| **Classes/Types** | Noun (what it represents) | `User`, `PaymentService`, `OrderRepository` | `Manager`, `Helper`, `Util` |
| **Constants** | Indicate immutability | `MAX_RETRIES`, `DefaultTimeout`, `API_VERSION` | `val`, `num` |
| **Booleans** | Question form | `isValid`, `hasPermission`, `canProcess` | `flag`, `status`, `check` |

### Language-Specific Casing

Follow the established conventions for each language:

| Language | Variables | Functions/Methods | Classes/Types | Constants | Interfaces |
|----------|-----------|-------------------|---------------|-----------|------------|
| Go | camelCase | PascalCase (exported) / camelCase (unexported) | PascalCase | PascalCase or UPPER_SNAKE | N/A (implicit) |
| C# | camelCase, `_camelCase` (private fields) | PascalCase | PascalCase | PascalCase | `I` prefix (e.g., `IPaymentService`) |
| TypeScript/JavaScript | camelCase | camelCase | PascalCase | UPPER_SNAKE or PascalCase | PascalCase |
| Python | snake_case | snake_case | PascalCase | UPPER_SNAKE | PascalCase |
| Java | camelCase | camelCase | PascalCase | UPPER_SNAKE | PascalCase |
| Vue/React Components | PascalCase (files and tags) | camelCase | PascalCase | UPPER_SNAKE | N/A |

**This repository's language:** {LANGUAGE}

### Repository-Specific Naming

| Element | Convention | Example |
|---------|------------|---------|
| {ELEMENT_1} | {PATTERN_1} | `{EXAMPLE_1}` |
| {ELEMENT_2} | {PATTERN_2} | `{EXAMPLE_2}` |
| {ELEMENT_3} | {PATTERN_3} | `{EXAMPLE_3}` |

## Single Responsibility Principle

Each function does one thing. Each class has one reason to change.

```
✅ GOOD: Functions do one thing
   validateInput(request)      → Only validates
   saveToDatabase(entity)      → Only persists
   sendNotification(message)   → Only sends

❌ BAD: Functions do multiple things
   processAndSaveAndNotify(request)  → Does too much
```

## Error Handling

### Principles
- Never ignore errors — handle or propagate every error
- Fail fast — check preconditions early
- Provide context — error messages should help diagnose the problem
- Clean up resources — always release resources, even on error paths

### Repository-Specific Error Pattern

```{LANGUAGE}
{ERROR_HANDLING_PATTERN}
```

## Dependency Injection

Dependencies should be injected, not created internally:

| Approach | Common In |
|----------|-----------|
| Constructor injection | C#, Java, TypeScript |
| Constructor functions | Go |
| Context-based injection | Go, Python |
| Framework DI container | .NET, Spring, NestJS |
| Provide/inject, stores | Vue, React |

**This repository's DI approach:** {DI_APPROACH}

## API Response Format

```json
{
  "success": true,
  "data": { },
  "errors": [],
  "meta": { }
}
```

## Formatting and Linting

Formatting is enforced by tooling, not code review. New code must pass the repository's linter without warnings.

**This repository's tools:** {LINTING_TOOLS}

## Logging

### Log Levels

| Level | When to Use | Examples |
|-------|-------------|----------|
| **ERROR** | Operation failed, requires attention | Payment failed, database connection lost |
| **WARN** | Unexpected but handled situation | Retry succeeded, deprecated API used |
| **INFO** | Significant business events | User logged in, order completed |
| **DEBUG** | Diagnostic details for troubleshooting | Function entry/exit, variable values |
| **TRACE** | Very detailed debugging (rarely used) | Loop iterations, internal state |

**Environment rules:** Production: ERROR/WARN/INFO enabled, DEBUG/TRACE disabled. Frontend: silent or error-only in production builds.

### What to Log

| Field | When |
|-------|------|
| Timestamp, level, message, service/component | Always |
| Request/correlation ID | Cross-service tracing |
| User ID, tenant ID | User-initiated / multi-tenant actions |
| Duration | Performance tracking |
| Error details (type, code, stack trace) | On failures |

### What NEVER to Log

| Category | Examples |
|----------|----------|
| **Authentication Credentials** | Passwords, API keys, tokens, session IDs, JWTs |
| **Payment Card Data** | Full card numbers, CVV, PINs |
| **Personal Identifiers** | SSN, driver's license, passport |
| **Health Information** | Medical records, diagnoses |
| **Financial Details** | Full bank account numbers |
| **Private Keys/Secrets** | Encryption keys, certificates |
| **Connection Strings with Credentials** | Database passwords, service account tokens |

### Repository-Specific Logging

```{LANGUAGE}
{LOGGING_EXAMPLE}
```

## Version Control

### Commit Messages
- Be descriptive — explain what changed and why
- Use imperative mood — "Add", "Fix", not "Added", "Fixed"
- Reference tickets when available
- Keep subject line ≤ 72 characters
- Be consistent within the repository

**This repository's commit format:** {COMMIT_FORMAT}

### Branch Naming
- Identifiable — indicates who and/or what ticket
- Descriptive — short description of the change's purpose
- Consistent within repo — all contributors use the same pattern

**This repository's branch format:** {BRANCH_FORMAT}

### Pull Requests
Every PR should communicate: what changed, why, how to test, and risk areas.

### Code Review Etiquette
- Authors: provide context, keep PRs small, self-review first
- Reviewers: be constructive, explain why, approve when ready, differentiate must-fix from nice-to-have
```

---

## File 4: testing.md

```markdown
# Testing Standards

## Test Frameworks

| Type | Framework | Location |
|------|-----------|----------|
| Unit Tests | {UNIT_FRAMEWORK} | `{UNIT_PATH}` |
| Integration Tests | {INT_FRAMEWORK} | `{INT_PATH}` |
| E2E Tests | {E2E_FRAMEWORK} | `{E2E_PATH}` |

## Test Organization

```
tests/
├── Unit/
│   └── {STRUCTURE}
├── Integration/
│   └── {STRUCTURE}
└── E2E/
    └── {STRUCTURE}
```

## Test Naming Convention

Test names must communicate intent — a reader should understand the test's purpose from its name alone.

| Pattern | Typical Languages | Example |
|---------|-------------------|---------|
| `Method_Scenario_ExpectedResult` | Go, C# (xUnit), Java | `TestGetUser_ValidID_ReturnsUser` |
| Descriptive string | JavaScript, TypeScript, Python (pytest) | `'getUser with valid ID returns user'` |
| Class + descriptive method | C# (nested classes), Java | `GetUserTests.ReturnsUser_WhenIdIsValid()` |
| Fixture-based grouping | C# (NUnit), Java (JUnit suites) | `UserServiceFixture.ReturnsNotFound()` |
| `test_` prefix with snake_case | Python | `test_get_user_valid_id_returns_user()` |

**This repository's naming pattern:** {TEST_NAMING_PATTERN}

```{LANGUAGE}
// ✅ Correct
{GOOD_TEST_NAME_EXAMPLE}

// ❌ Incorrect
{BAD_TEST_NAME_EXAMPLE}
```

## Test Structure (Arrange-Act-Assert)

Every test has three distinct sections:

```
ARRANGE - Set up the test scenario (create test data, configure mocks)
ACT     - Execute the code being tested (call the method/function)
ASSERT  - Verify the results (check return values, verify side effects)
```

```{LANGUAGE}
{AAA_EXAMPLE}
```

## Test Independence

| Rule | Description |
|------|-------------|
| **No shared mutable state** | Each test creates its own data and cleans up |
| **No order dependency** | Tests can run in any order |
| **Isolated side effects** | Database changes rolled back or isolated |
| **Independent setup** | Each test sets up what it needs |

## Required Test Scenarios

### Core Scenarios (Always Required)

| Scenario | Description |
|----------|-------------|
| **Happy Path** | Normal successful operation — valid input returns expected output |
| **Invalid Input** | Null, empty, out-of-range values return validation errors |
| **Not Found** | Unknown ID or missing resource returns appropriate error |

### Conditional Scenarios (When the Code Does This)

| Scenario | Applies When |
|----------|--------------|
| **Authorization** | Code checks permissions — user without role gets denied |
| **Authentication** | Code requires auth — missing token returns 401 |
| **External Failure** | Code calls external service — timeout handled gracefully |
| **Concurrency** | Code handles parallel requests — no data loss |
| **Boundary Conditions** | Numeric or size limits — max, min, exactly at limit |
| **Multi-Tenant Isolation** | Multi-tenant context — Tenant A cannot see Tenant B's data |

### Domain-Specific Scenarios (Only When Applicable)

**Payment Processing:**

| Scenario | Description |
|----------|-------------|
| Card/input validation | Format checks enforced |
| Declined/failed transactions | Errors handled gracefully, no double-charge |
| Retry logic | Backoff and idempotency work correctly |
| Sensitive field masking | Card/PIN fields never appear in logs or cleartext |

**Notifications:**

| Scenario | Description |
|----------|-------------|
| Correct trigger | Right event triggers right notification |
| Template data | Variables populated correctly |
| Deduplication | Same event does not trigger duplicate sends |

**Security & Access Control:**

| Scenario | Description |
|----------|-------------|
| Account lockout | Locked after N failed attempts |
| Session/token expiry | Expired sessions rejected |
| Password policy | Complexity requirements enforced |

**Frontend / UI:**

| Scenario | Description |
|----------|-------------|
| Responsive design | Renders across standard breakpoints |
| Accessibility (a11y) | Keyboard nav, screen reader, WCAG 2.1 AA |
| Key user journeys | Critical flows completable without confusion |

### Regression & Sanity

| Scenario | When to Apply |
|----------|---------------|
| **Smoke tests** | Every deployment — service starts, health endpoints respond |
| **Full regression** | Before major releases, nightly, or after large refactors |

## Mocking Guidelines

### What to Mock

| Category | Examples | Why Mock |
|----------|----------|----------|
| **External APIs** | Payment gateways, third-party services | Unreliable, slow, cost money |
| **Databases** (unit tests) | Repository calls | Isolate business logic |
| **File System** | File reads/writes | Avoid test pollution |
| **Time/Randomness** | Current time, random values | Reproducible tests |
| **Network** | HTTP clients, message queues | Avoid flaky tests |

### What NOT to Mock

| Category | Examples | Why Not Mock |
|----------|----------|--------------|
| **Code under test** | The class/function being tested | Defeats the purpose |
| **Simple value objects** | DTOs, data classes | No benefit, adds complexity |
| **Pure functions** | Math, string manipulation | Deterministic, fast |
| **Internal implementation** | Private methods | Test behavior, not implementation |

**Principle:** Mock at boundaries (interfaces, external services), not internals.

## Coverage Guidance

Coverage is a tool, not a goal. Prioritize meaningful coverage:

| Component Type | Priority | Notes |
|----------------|----------|-------|
| **Critical business logic** | Highest | Payment, auth, core domain features |
| **Public APIs / Controllers** | High | Entry points, request handling |
| **Data access** | Moderate | Repositories, queries |
| **Infrastructure** | Lower | Logging, metrics, utilities |
| **Generated code** | Skip | Not your code |

Set numeric targets per repository based on maturity, domain risk, and compliance requirements.

## Test Data Management

Use builders or factories for complex test data. Avoid magic values — use named constants.

## CI/CD Integration

| Stage | Tests Run | Failure Action |
|-------|-----------|----------------|
| **PR Created** | Unit tests, linting | Block merge |
| **PR Approved / Merge** | Unit + Integration | Block deploy |
| **Pre-production** | E2E + Smoke | Block production deploy |
| **Post-deploy** | Smoke tests | Alert / rollback |

Tests must be: deterministic, fast (unit < 1s, integration < 30s), isolated, and have clear failure messages.

**Repository-specific commands:**
- **On PR**: {PR_TESTS}
- **On merge**: {MERGE_TESTS}
- **Nightly**: {NIGHTLY_TESTS}

## Test Code Review Checklist

- [ ] Tests follow AAA pattern
- [ ] Test names communicate intent
- [ ] Tests are independent (no shared state, no order dependency)
- [ ] Happy path, error cases, and edge cases covered
- [ ] Tests are not flaky
- [ ] Mocks used at boundaries, not over-mocked
- [ ] Test data is clear (builders/fixtures for complex data)
```

---

## File 5: architecture.md

```markdown
# Architecture Overview

## System Purpose
{PRODUCT_NAME} provides {VALUE_PROPOSITION} for {TARGET_USERS}.

## C4 Context (Level 1)

See: `docs/architecture/context-diagram.mmd`

### Users
- **{USER_TYPE_1}**: {DESCRIPTION}
- **{USER_TYPE_2}**: {DESCRIPTION}

### External Systems
- **{SYSTEM_1}**: {PURPOSE}
- **{SYSTEM_2}**: {PURPOSE}
- **{SYSTEM_3}**: {PURPOSE}

## C4 Container (Level 2)

See: `docs/architecture/container-diagram.mmd`

| Container | Technology | Purpose |
|-----------|------------|---------|
| {CONTAINER_1} | {TECH_1} | {PURPOSE_1} |
| {CONTAINER_2} | {TECH_2} | {PURPOSE_2} |
| {CONTAINER_3} | {TECH_3} | {PURPOSE_3} |

## Key Architectural Decisions

| Decision | Rationale | Impact |
|----------|-----------|--------|
| {DECISION_1} | {WHY_1} | {IMPACT_1} |
| {DECISION_2} | {WHY_2} | {IMPACT_2} |

## Security Boundaries

{SECURITY_DIAGRAM_OR_DESCRIPTION}

## Related Documentation
- [C4 Diagrams](docs/architecture/)
- [API Documentation](docs/api/)
```

---

## File 6: .cursorrules (Optional Quick Reference)

```markdown
# Cursor Rules for {PRODUCT_NAME}

## Context Pack
Read Context Pack files in `.cursor/` before generating code:
- agents.md - AI instructions and security rules
- context.md - Domain knowledge  
- conventions.md - Code patterns, logging, version control
- testing.md - Test standards and required scenarios
- architecture.md - System design

## Quick Rules
- Tech Stack: {TECH_STACK}
- Multi-tenant: Always filter by tenant context
- {COMPLIANCE}: {KEY_RULE}
- Tests: Follow AAA pattern, descriptive names, required scenarios
- Naming: {NAMING_CONVENTION}
- Security: No hardcoded secrets, no PII in logs, parameterized queries

## Before You Generate
1. Check if similar code exists
2. Follow existing patterns
3. Include error handling with context
4. Consider multi-tenant isolation
5. Add appropriate tests
```

---

## Usage Instructions

1. **Copy this template** to your repository
2. **Replace `{PLACEHOLDER}` values** with your specific details
3. **Add code examples** from your actual codebase
4. **Keep the universal principles** (security rules, naming tables, testing scenarios, logging rules) — these are the baseline every Context Pack must include
5. **Review with team** for accuracy
6. **Keep updated** as codebase evolves

See `workflows/create-context-pack.md` for the detailed workflow.
