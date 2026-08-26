# Workflow: Create Context Packs

> **DEPRECATED**: This workflow has been replaced by:
> - [Generate Context Areas](./generate-context-areas.md) -- for context per SDLC area
> - [Generate IDE Rules](./generate-ide-rules.md) -- for IDE-specific agent rules
> - [Detect & Generate Standards](./detect-and-generate-standards.md) -- for coding and other standards
>
> See [Analyze & Generate](./analyze-and-generate.md) for the new master workflow.

## Quick Start

**Copy-paste this to create a complete Context Pack:**

```
Read @GenDD-Flow/workflows/create-context-pack.md

Analyze @TargetRepo and create a Context Pack:

Product: [PRODUCT NAME]
Purpose: [WHAT IT DOES]
Tech Stack: [TECHNOLOGIES]
Key Integrations: [EXTERNAL SYSTEMS]
Compliance: [PCI/HIPAA/none]

Generate:
1. agents.md - AI instructions and constraints
2. context.md - Domain knowledge and glossary
3. conventions.md - Coding standards and patterns
4. testing.md - Testing requirements
5. architecture.md - System architecture overview

Use @GenDD-Flow/templates/context-pack.md as the template — it contains universal principles for security, testing, code quality, logging, and version control.
Save to @TargetRepo/.cursor/
```

**Expected Output:**
```
@TargetRepo/
└── .cursor/
    ├── agents.md
    ├── context.md
    ├── conventions.md
    ├── testing.md
    └── architecture.md
```

---

## Context
Create **lightweight, versioned Markdown files** that live in the repository and capture system intent, workflows, conventions, and testing standards. Context Packs make Cursor effective at scale by providing the AI with the domain knowledge it needs to generate accurate, project-specific code.

## Alignment with AI-in-SDLC Initiative
This workflow is one of four initial high-impact areas focused on early SDLC quality:
1. Story Quality (shift-left)
2. Test Gap Identification
3. **Context Packs** ← This workflow
4. C4 Architecture Diagrams

## What Are Context Packs?

Context Packs are a structured set of Markdown files that:
- **Live in the repository** (versioned with code)
- **Describe the system** for AI tools like Cursor
- **Capture tribal knowledge** that exists in developers' heads
- **Standardize conventions** so AI generates consistent code
- **Reduce onboarding time** for both humans and AI

### Standard Context Pack Structure

```
.cursor/
├── agents.md           # AI agent instructions and capabilities
├── context.md          # System overview and domain knowledge
├── conventions.md      # Coding standards and patterns
├── testing.md          # Testing standards and requirements
└── architecture.md     # Architecture overview with C4 references
```

Alternatively (for visibility):
```
docs/
├── cursor/
│   ├── agents.md
│   ├── context.md
│   ├── conventions.md
│   ├── testing.md
│   └── architecture.md
```

## Context Pack Template

The Context Pack template at `templates/context-pack.md` contains all universal principles (security, code quality, logging, testing, version control) baked into each file section. When creating a Context Pack, use the template as a starting point and customize the `{PLACEHOLDER}` values for the specific repository.

## Tooling Approach
**Cursor + repo-based Markdown context only.** No RAG, vector databases, embeddings, or additional platforms.

## Prerequisites
- Access to codebase
- Cursor or similar AI IDE
- Understanding of system purpose and key stakeholders
- Access to existing documentation (if any)

## When to Use This Workflow
- Setting up a new project for AI-assisted development
- Onboarding a repository to Cursor
- After discovering AI is making repeated mistakes
- When multiple developers get inconsistent AI outputs
- Before starting major feature development
- Quarterly refresh of context documentation
- **After Brownfield Analysis** - Use documentation pack from `workflows/brownfield-repository-analysis.md` to create AI context

---

## Cursor Steps

### Phase 1: Create agents.md

#### 1. Generate Agent Instructions

Open Cursor Chat (Cmd+L / Ctrl+L) in your repository root:

```
Analyze @TargetRepo and create an agents.md file that defines:

1. **Identity**: What system is this? What does it do?
2. **Role**: How should the AI help with this codebase?
3. **Key Constraints**: Security rules, compliance requirements, data isolation
4. **What to help with**: Code generation, testing, reviews
5. **What NOT to do**: Security bypasses, hardcoded secrets, etc.

Context:
- This is a {PRODUCT_NAME} system
- Tech stack: {TECH_STACK}

For guidance on security and testing constraints, reference:
@GenDD-Flow/templates/context-pack.md (agents.md section for security, testing.md section for test standards)

Output as a complete agents.md file.
```

#### 2. Review and Customize agents.md

Expected structure:

```markdown
# AI Agent Instructions

## Identity
You are an AI assistant helping develop {PRODUCT_NAME}, a {DESCRIPTION}.

## Your Role
- Generate code that follows our established patterns
- Help identify issues before they reach production
- Accelerate development while maintaining quality
- Ask clarifying questions when requirements are ambiguous

## Key Constraints
- **Security First**: Never suggest storing sensitive data unencrypted
- **PCI Compliance**: All payment-related code must follow PCI DSS standards
- **Multi-Tenant**: Always consider tenant isolation in database queries
- **Accessibility**: UI components must meet WCAG 2.1 AA standards

## What You Can Help With
- Writing code following our patterns (see conventions.md)
- Generating tests following our standards (see testing.md)
- Understanding system architecture (see architecture.md)
- Enhancing requirements with edge cases
- Reviewing code for common issues

## What You Should Not Do
- Generate code that bypasses authentication
- Hardcode credentials or secrets
- Create SQL without parameterization
- Skip error handling for external calls
- Ignore multi-tenant data isolation

## Communication Style
- Be concise and specific
- Reference existing code patterns when relevant
- Highlight security/compliance concerns proactively
- Ask clarifying questions rather than assume
```

### Phase 2: Create context.md

#### 3. Generate System Context

```
Analyze this codebase and create a context.md file that explains:

1. **System Purpose**: What does this system do? Who uses it?
2. **Domain Concepts**: Key business terms and their meanings
3. **User Personas**: Who are the users and what do they need?
4. **Key Integrations**: What external systems does this connect to?
5. **Data Flow**: How does data move through the system?

This will help AI understand the business context when generating code.

Output as a complete context.md file with concrete examples from the codebase.
```

#### 4. Review and Enhance context.md

Expected structure:

```markdown
# System Context

## Overview
{PRODUCT_NAME} is a {TYPE_OF_SYSTEM} that enables {KEY_VALUE_PROPOSITION}.

## Domain Glossary

| Term | Definition | Example in Code |
|------|------------|-----------------|
| Tenant | A single organization using the platform | `TenantId` in all entities |
| Transaction | A payment or refund event | `PaymentTransaction` class |
| Vault | Secure storage for payment tokens | `VaultService` |

## User Personas

### School Administrator
- **Goal**: Manage payments for student fees
- **Actions**: Configure payment options, view reports, process refunds
- **Code Areas**: `AdminController`, `ReportService`

### Parent/Guardian
- **Goal**: Pay student fees quickly and securely
- **Actions**: Make payments, view history, save payment methods
- **Code Areas**: `PaymentController`, `CheckoutService`

## Key Integrations

| Integration | Purpose | Code Location |
|-------------|---------|---------------|
| WorldPay | Payment processing | `src/Integrations/WorldPay/` |
| Vault Service | Payment token storage | `src/Services/VaultClient.cs` |
| SendGrid | Email notifications | `src/Services/EmailService.cs` |

## Business Rules

### Payment Processing
- Transactions over $10,000 require additional verification
- Refunds can only be processed within 30 days
- Multi-tenant: School A cannot see School B's transactions

### Data Retention
- Payment records retained for 7 years (compliance)
- Audit logs never deleted
- User data deleted on request (GDPR/CCPA)

## Compliance Requirements
- **PCI DSS Level 1**: All payment handling
- **FERPA**: Student data privacy (education sector)
- **SOC 2**: Security controls and auditing
```

### Phase 3: Create conventions.md

#### 5. Generate Coding Conventions

```
Analyze the coding patterns in this repository and create a conventions.md file.

Document:

1. **Naming Conventions**: Classes, methods, variables, files
2. **Code Structure**: How are files/folders organized?
3. **Patterns in Use**: Repository pattern? CQRS? MVC?
4. **Error Handling**: How are errors handled and logged?
5. **Dependency Injection**: How are dependencies managed?
6. **API Design**: REST conventions, response formats
7. **Database Access**: ORM usage, query patterns

For each convention, provide:
- The rule
- A code example from this codebase
- Why it matters

Output as a complete conventions.md file.
```

#### 6. Review and Enhance conventions.md

Expected structure:

```markdown
# Coding Conventions

## File Organization

```
src/
├── Controllers/     # API endpoints
├── Services/        # Business logic
├── Repositories/    # Data access
├── Models/          # Domain models
├── DTOs/            # Data transfer objects
├── Integrations/    # Third-party clients
└── Utilities/       # Helper classes
```

## Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Controllers | `{Entity}Controller` | `PaymentController` |
| Services | `{Entity}Service` | `PaymentService` |
| Repositories | `{Entity}Repository` | `PaymentRepository` |
| Interfaces | `I{Name}` | `IPaymentService` |
| DTOs | `{Entity}{Action}Dto` | `PaymentCreateDto` |

## Code Patterns

### Service Layer Pattern
All business logic goes in services, not controllers:

```csharp
// ✅ Correct
public class PaymentController
{
    private readonly IPaymentService _paymentService;
    
    public async Task<IActionResult> ProcessPayment(PaymentRequest request)
    {
        var result = await _paymentService.ProcessAsync(request);
        return Ok(result);
    }
}

// ❌ Incorrect - business logic in controller
public class PaymentController
{
    public async Task<IActionResult> ProcessPayment(PaymentRequest request)
    {
        // Don't put business logic here
        var amount = request.Amount * 1.1m; // tax calculation
        await _db.Payments.AddAsync(new Payment { Amount = amount });
    }
}
```

### Repository Pattern
All database access through repositories:

```csharp
public interface IPaymentRepository
{
    Task<Payment?> GetByIdAsync(Guid id, Guid tenantId);
    Task<IEnumerable<Payment>> GetByUserAsync(Guid userId, Guid tenantId);
    Task AddAsync(Payment payment);
}
```

### Error Handling
Use typed exceptions and middleware:

```csharp
// Custom exception
public class PaymentDeclinedException : BusinessException
{
    public string ErrorCode { get; }
    public PaymentDeclinedException(string errorCode, string message) 
        : base(message) => ErrorCode = errorCode;
}

// Throwing
throw new PaymentDeclinedException("INSUFFICIENT_FUNDS", "Card declined");
```

## Multi-Tenant Requirements

**Every database query MUST include TenantId:**

```csharp
// ✅ Correct
public async Task<Payment?> GetByIdAsync(Guid id, Guid tenantId)
{
    return await _context.Payments
        .Where(p => p.Id == id && p.TenantId == tenantId)
        .FirstOrDefaultAsync();
}

// ❌ SECURITY ISSUE - Missing tenant filter
public async Task<Payment?> GetByIdAsync(Guid id)
{
    return await _context.Payments
        .Where(p => p.Id == id)
        .FirstOrDefaultAsync();
}
```

## API Response Format

```json
{
  "success": true,
  "data": { ... },
  "errors": [],
  "meta": {
    "requestId": "...",
    "timestamp": "..."
  }
}
```

## Logging Standards

```csharp
_logger.LogInformation(
    "Payment processed: {TransactionId} for {Amount} by {UserId}",
    transaction.Id, 
    amount, 
    userId);
```

Never log:
- Full credit card numbers
- Passwords or tokens
- Personal identifiable information (PII)
```

### Phase 4: Create testing.md

#### 7. Generate Testing Standards

```
Analyze the test files in this repository and create a testing.md file.

Document:

1. **Test Framework**: What frameworks are used?
2. **Test Organization**: How are tests structured?
3. **Naming Convention**: How are tests named?
4. **Mocking Strategy**: How are dependencies mocked?
5. **Test Data**: How is test data managed?
6. **Coverage Requirements**: What coverage is expected?
7. **CI/CD Integration**: How do tests run in pipeline?

For each standard, provide:
- The rule
- A code example from this codebase
- When to apply it

Output as a complete testing.md file.
```

#### 8. Review and Enhance testing.md

Expected structure:

```markdown
# Testing Standards

## Test Frameworks

| Type | Framework | Location |
|------|-----------|----------|
| Unit Tests | xUnit + Moq | `tests/Unit/` |
| Integration Tests | xUnit + TestContainers | `tests/Integration/` |
| E2E Tests | Playwright | `tests/E2E/` |

## Test Organization

```
tests/
├── Unit/
│   ├── Services/
│   │   └── PaymentServiceTests.cs
│   └── Repositories/
│       └── PaymentRepositoryTests.cs
├── Integration/
│   └── WorldPayClientTests.cs
└── E2E/
    └── CheckoutFlow.spec.ts
```

## Naming Convention

Test methods follow: `{Method}_{Scenario}_{ExpectedResult}`

```csharp
// ✅ Correct
[Fact]
public async Task ProcessPayment_ValidCard_ReturnsSuccess()

[Fact]
public async Task ProcessPayment_ExpiredCard_ThrowsPaymentDeclinedException()

// ❌ Incorrect - unclear what's being tested
[Fact]
public async Task Test1()
```

## Test Structure (Arrange-Act-Assert)

```csharp
[Fact]
public async Task ProcessPayment_ValidCard_ReturnsSuccess()
{
    // Arrange
    var request = new PaymentRequest { Amount = 1000, CardToken = "tok_123" };
    var expectedResponse = new PaymentResponse { Status = "AUTHORIZED" };
    _mockGateway.Setup(x => x.Authorize(It.IsAny<AuthRequest>()))
        .ReturnsAsync(new GatewayResponse { Approved = true });

    // Act
    var result = await _sut.ProcessPaymentAsync(request);

    // Assert
    Assert.NotNull(result);
    Assert.Equal("AUTHORIZED", result.Status);
    _mockGateway.Verify(x => x.Authorize(It.IsAny<AuthRequest>()), Times.Once);
}
```

## Mocking Guidelines

### What to Mock
- External API clients (WorldPay, Vault, Email)
- Database context (for unit tests)
- Time/date providers
- File system access

### What NOT to Mock
- The class under test
- Simple value objects
- Framework classes (unless testing integration)

```csharp
// Standard mock setup
public class PaymentServiceTests
{
    private readonly Mock<IPaymentGateway> _mockGateway;
    private readonly Mock<IPaymentRepository> _mockRepository;
    private readonly Mock<ILogger<PaymentService>> _mockLogger;
    private readonly PaymentService _sut;

    public PaymentServiceTests()
    {
        _mockGateway = new Mock<IPaymentGateway>();
        _mockRepository = new Mock<IPaymentRepository>();
        _mockLogger = new Mock<ILogger<PaymentService>>();
        
        _sut = new PaymentService(
            _mockGateway.Object,
            _mockRepository.Object,
            _mockLogger.Object);
    }
}
```

## Test Data Management

Use builders for complex test data:

```csharp
public class PaymentRequestBuilder
{
    private decimal _amount = 1000;
    private string _cardToken = "tok_test";
    
    public PaymentRequestBuilder WithAmount(decimal amount)
    {
        _amount = amount;
        return this;
    }
    
    public PaymentRequest Build()
    {
        return new PaymentRequest { Amount = _amount, CardToken = _cardToken };
    }
}

// Usage
var request = new PaymentRequestBuilder()
    .WithAmount(5000)
    .Build();
```

## Coverage Requirements

| Type | Minimum | Target |
|------|---------|--------|
| Business Logic | 80% | 90% |
| Controllers | 70% | 80% |
| Integrations | 60% | 80% |
| Utilities | 50% | 70% |

## Required Test Scenarios

Every feature MUST have tests for:

- [ ] Happy path
- [ ] Invalid input (null, empty, out of range)
- [ ] Authentication/authorization failures
- [ ] External service failures
- [ ] Multi-tenant isolation

## CI/CD Integration

Tests run automatically:
- **On PR**: Unit tests (required to pass)
- **On merge to main**: Unit + Integration tests
- **Nightly**: Full E2E suite
- **Pre-release**: All tests + performance

```yaml
# .github/workflows/test.yml
- name: Run Unit Tests
  run: dotnet test --filter Category=Unit
  
- name: Run Integration Tests
  if: github.event_name == 'push'
  run: dotnet test --filter Category=Integration
```
```

### Phase 5: Create architecture.md

#### 9. Generate Architecture Overview

```
Analyze this codebase and create an architecture.md file.

Include:

1. **System Overview**: High-level description of the system
2. **C4 Context**: What systems and users interact with this?
3. **C4 Container**: What are the major components?
4. **Key Decisions**: Important architectural choices made
5. **Security Boundaries**: Where are the trust boundaries?

Reference the C4 diagrams generated by generate-architecture-diagrams workflow.

Output as a complete architecture.md file.
```

#### 10. Review and Enhance architecture.md

Expected structure:

```markdown
# Architecture Overview

## System Purpose
{PRODUCT_NAME} provides {VALUE_PROPOSITION} for {TARGET_USERS}.

## C4 Context (Level 1)

See: `docs/architecture/context-diagram.mmd`

### Users
- **School Administrators**: Configure and manage payments
- **Parents/Guardians**: Make payments for students

### External Systems
- **WorldPay**: Payment gateway
- **Vault Service**: Secure token storage
- **School Management Systems**: Student data sync (24 integrations)

## C4 Container (Level 2)

See: `docs/architecture/container-diagram.mmd`

| Container | Technology | Purpose |
|-----------|------------|---------|
| Web Application | React 18 | User interface |
| API Application | .NET Core 8 | Business logic and orchestration |
| Background Worker | .NET Core 8 | Async processing (reports, notifications) |
| Database | PostgreSQL 15 | Primary data store |
| Cache | Redis | Session and data caching |

## Security Boundaries

```
┌──────────────────────────────────────────┐
│ Public Internet                          │
│  ┌────────────────┐                      │
│  │ Web Application│ (React)              │
│  └────────┬───────┘                      │
│           │ HTTPS                        │
└───────────┼──────────────────────────────┘
            │
┌───────────┼──────────────────────────────┐
│ DMZ       │                              │
│  ┌────────┴───────┐                      │
│  │ API Gateway    │ (Auth, Rate Limiting)│
│  └────────┬───────┘                      │
└───────────┼──────────────────────────────┘
            │
┌───────────┼──────────────────────────────┐
│ Private Network (PCI Scope)              │
│  ┌────────┴───────┐   ┌─────────────┐    │
│  │ API Application│───│ Vault Svc   │    │
│  └────────┬───────┘   └─────────────┘    │
│           │                              │
│  ┌────────┴───────┐                      │
│  │ Database       │                      │
│  └────────────────┘                      │
└──────────────────────────────────────────┘
```

## Key Architectural Decisions

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Multi-tenant with TenantId | Data isolation, single deployment | All queries must filter by tenant |
| Token-based auth | Stateless, scalable | JWT validation on every request |
| Async processing | Don't block payments | Background worker for reports |

## Related Documentation
- [C4 Diagrams](docs/architecture/)
- [ADR Records](docs/adr/)
- [API Documentation](docs/api/)
```

### Phase 6: Finalize and Maintain

#### 11. Validate Context Pack Content

After creating all files, validate overall quality:

```
Review the Context Pack files I've created:
- agents.md
- context.md
- conventions.md
- testing.md
- architecture.md

Check for:
1. Consistency across files
2. Missing important information
3. Accuracy against the actual codebase
4. Clarity for AI and humans

Suggest any improvements.
```

#### 12. Add Context Pack to .cursorrules (Optional)

Create or update `.cursorrules` to reference the Context Pack:

```markdown
# Cursor Rules

## Context Pack Location
Before generating code, read the Context Pack files in `.cursor/` or `docs/cursor/`:
- agents.md - Your instructions and constraints
- context.md - System overview and domain knowledge
- conventions.md - Coding patterns to follow
- testing.md - Testing requirements
- architecture.md - System architecture

## Quick Reference
- This is {PRODUCT_NAME}
- Tech stack: {TECH_STACK}
- Key constraint: {IMPORTANT_RULE}
```

---

## Output Artifacts

After completing this workflow, you will have:

```
@TargetRepo/
├── .cursor/ (or docs/cursor/)
│   ├── agents.md            # AI instructions and constraints
│   ├── context.md           # Domain knowledge
│   ├── conventions.md       # Coding standards and patterns
│   ├── testing.md           # Test requirements
│   └── architecture.md      # Architecture overview
└── .cursorrules             # Quick reference (optional)
```

---

## Maintenance

### When to Update Context Packs

- **After major architectural changes**: Update architecture.md
- **When conventions change**: Update conventions.md
- **When new integrations added**: Update context.md
- **After adding test frameworks**: Update testing.md
- **Quarterly review**: Ensure all files are current

### Version Control

Context Packs are versioned with the code:
- Include in code reviews when modified
- Track changes over time
- Different branches can have different context

---

## Tips for Best Results

### Keep Files Concise
- AI context windows are limited
- Focus on what's most important
- Link to detailed docs rather than duplicating

### Use Concrete Examples
- Code snippets from the actual codebase
- Real class and method names
- Actual file paths

### Update Proactively
- When AI makes repeated mistakes, update context
- When new patterns emerge, document them
- When team conventions change, reflect immediately

### Test the Context Pack
After creating:
```
Using the context from the Context Pack, generate a new service that follows our conventions.
```
Verify the output matches your expectations.

---

## Integration with Other Workflows

### Inputs From Other Workflows

**From Brownfield Repository Analysis** (`workflows/brownfield-repository-analysis.md`):
- **System documentation** → Seed context.md with domain knowledge
- **Component catalog** → Feed into architecture.md
- **Coding patterns discovered** → Populate conventions.md
- **Risk hotspots** → Include in agents.md constraints

```
# Using brownfield analysis to create Context Pack
Read @GenDD-Flow/workflows/create-context-pack.md
Read @GenDD-Flow/templates/context-pack.md

Use the brownfield analysis from @docs/brownfield/gendd/:
- System Overview (`overview/system-summary.md`) → context.md
- Component Catalog (`architecture/components.md`) → architecture.md
- Risk Hotspots (`risks/risk-hotspots.md`) → agents.md constraints
- Core Flows (`flows/`) → context.md business rules

Generate Context Pack files for .cursor/ folder.
```

### Context Packs Support All Other Workflows

1. **Story Quality** - AI understands domain terms
2. **Test Gap Identification** - AI knows test standards
3. **C4 Diagrams** - Architecture context is documented
4. **Code Generation** - AI follows conventions automatically
5. **Brownfield Analysis** - Existing context informs deeper analysis

---

## Common Pitfalls to Avoid

- ❌ **Too much detail**: AI context is limited, be concise
- ❌ **Stale content**: Update when code changes
- ❌ **Missing examples**: Abstract rules without code examples don't work
- ❌ **Conflicting info**: Ensure consistency across files
- ❌ **Ignoring security**: Always include security constraints in agents.md


