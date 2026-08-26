# Target Repository .cursorrules Template

> **DEPRECATED**: This template has been replaced by IDE-specific rule generation.
> See [Generate IDE Rules Workflow](../workflows/generate-ide-rules.md).
> GenDD-Flow now supports Cursor, Claude Code, Antigravity, Copilot, and other IDEs.

Copy this template to any repository you want to analyze with GenDD-Flow workflows.

---

## Usage

1. Copy this content to `.cursorrules` in your target repository
2. Replace all `[TODO: ...]` placeholders with repository-specific information
3. Update the GenDD-Flow path to match your setup

---

## Template

```markdown
# Cursor Rules for [Repository Name]

## GenDD-Flow Integration

This repository uses GenDD-Flow workflows for AI-assisted development.

**GenDD-Flow Location**: [Choose one]
- Workspace: @GenDD-Flow/
- Symlink: .genddflow/
- Absolute: /path/to/GenDD-Flow/

### The Five Frameworks

| Framework | When to Use | Workflow |
|-----------|-------------|----------|
| Story Quality | Requirements, acceptance criteria, edge cases | enhance-acceptance-criteria.md |
| Test Gaps | Coverage analysis, test planning | identify-test-gaps.md |
| Context Packs | AI context, conventions, patterns | create-context-pack.md |
| C4 Diagrams | Architecture documentation | generate-architecture-diagrams.md |
| Brownfield Analysis | Legacy/undocumented system understanding | brownfield-repository-analysis.md |

### How to Reference Workflows

```
Read @[GenDD-Flow-path]/workflows/[workflow-name].md

Then apply to this repository: [your request]
```

---

## Repository Context

### About This Repository
[TODO: What does this repository do? Who uses it?]

### Tech Stack
- **Language**: [TODO: e.g., Python 3.11, .NET 8, TypeScript]
- **Framework**: [TODO: e.g., Django, ASP.NET Core, React]
- **Database**: [TODO: e.g., PostgreSQL 15, SQL Server, MongoDB]
- **Cache**: [TODO: e.g., Redis, Memcached]
- **Message Queue**: [TODO: e.g., RabbitMQ, Kafka, Azure Service Bus]

### Key User Personas
[TODO: Who uses this system?]
- **[Persona 1]**: [What they do]
- **[Persona 2]**: [What they do]

### Key Integrations
[TODO: What external systems does this connect to?]
| Integration | Purpose | Code Location |
|-------------|---------|---------------|
| [Integration 1] | [Purpose] | [Path] |
| [Integration 2] | [Purpose] | [Path] |

### Domain Glossary
[TODO: Key terms in this codebase]
| Term | Definition |
|------|------------|
| [Term 1] | [Definition] |
| [Term 2] | [Definition] |

---

## Code Standards

### File Organization
[TODO: Describe folder structure]
```
src/
├── [folder1]/   # [purpose]
├── [folder2]/   # [purpose]
└── [folder3]/   # [purpose]
```

### Naming Conventions
| Element | Convention | Example |
|---------|------------|---------|
| [TODO] | [TODO] | [TODO] |

### Key Patterns
[TODO: What patterns does this codebase use?]
- Repository Pattern: Yes/No
- CQRS: Yes/No
- Event Sourcing: Yes/No
- Dependency Injection: Yes/No

---

## Multi-Tenant

[TODO: Is this multi-tenant?]
- **Multi-tenant**: Yes / No
- **Tenant ID Field**: [e.g., TenantId, OrganizationId]
- **Isolation Level**: [e.g., Row-level, Schema-level, Database-level]

⚠️ **If multi-tenant**: Every database query MUST filter by tenant

---

## Security & Compliance

[TODO: What compliance requirements apply?]
- **PCI DSS**: Yes/No (payment data)
- **HIPAA**: Yes/No (health data)
- **GDPR**: Yes/No (EU personal data)
- **SOC 2**: Yes/No
- **Other**: [TODO]

### Security Rules
- Never log: [TODO: sensitive fields]
- Always encrypt: [TODO: sensitive data]
- Auth required for: [TODO: which endpoints]

---

## Testing

### Test Frameworks
| Type | Framework | Location |
|------|-----------|----------|
| Unit | [TODO] | [TODO] |
| Integration | [TODO] | [TODO] |
| E2E | [TODO] | [TODO] |

### Coverage Requirements
- Minimum coverage: [TODO: e.g., 80%]
- Critical paths: [TODO: must be 100%]

### Test Naming
[TODO: What naming convention?]
- `[Method]_[Scenario]_[ExpectedResult]`
- or describe your convention

---

## Before Generating Code

1. ✅ Check if similar code exists in this repository
2. ✅ Reference the appropriate GenDD-Flow workflow
3. ✅ Follow patterns documented above
4. ✅ Include proper error handling
5. ✅ Consider multi-tenant isolation (if applicable)
6. ✅ Consider security/compliance requirements
7. ✅ Add appropriate tests

---

## Quick Prompts

### Enhance Requirements
```
Read @[GenDD-Flow]/workflows/enhance-acceptance-criteria.md
Transform this requirement into detailed acceptance criteria:
"[paste requirement]"
```

### Identify Test Gaps
```
Read @[GenDD-Flow]/workflows/identify-test-gaps.md
Analyze this repository for test gaps, focusing on [area].
```

### Generate C4 Diagrams
```
Read @[GenDD-Flow]/workflows/generate-architecture-diagrams.md
Generate C4 Context and Container diagrams for this repository.
```

### Create Context Pack
```
Read @[GenDD-Flow]/workflows/create-context-pack.md
Create a complete Context Pack for this repository.
```

### Brownfield Analysis (Legacy Systems)
```
Read @[GenDD-Flow]/workflows/brownfield-repository-analysis.md
Analyze this repository with the 4-pass brownfield approach.
```
```

---

## Customization Tips

1. **Be specific about your tech stack** - The more detail, the better AI outputs
2. **Document your patterns** - Show examples from your actual codebase
3. **List integrations** - AI needs to know what external systems exist
4. **Define your terms** - Domain glossary prevents confusion
5. **Specify compliance** - Security requirements shape code generation


