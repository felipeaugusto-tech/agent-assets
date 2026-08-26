# Pass 1: Brownfield Repo Scanner

## Mission

Rapidly inventory the repository and map its shape:
- Monorepo vs multi-repo layout
- Service boundaries and modules
- Entry points (web, worker, CLI, event)
- Build and runtime scaffolding
- Dependency surfaces
- Event-driven cues (brokers, topics, consumers)

You must produce a **repo map** that enables deeper reasoning in Pass 2 (Infer).

## Output Guidelines

**Reference:** `templates/documentation-guidelines.md`

### Key Rules
- ❌ **No hard-coded counts** - Use patterns: "Services matching `*Service.cs`" not "15 services"
- ✅ **Reference files** - "Entry point: `Program.cs`" not embedded code
- ✅ **Patterns for discovery** - Include commands to get current counts

## What to Scan (Priority Order)

### 1. Top-Level Structure
```
Priority directories:
- packages/, services/, apps/, src/, libs/, modules/
- cmd/, internal/, pkg/ (Go)
- app/, config/, lib/ (Rails/Ruby)
```

### 2. Build and Tooling
| Pattern | Indicates |
|---------|-----------|
| `package.json` workspaces, `pnpm-workspace.yaml` | Node.js monorepo |
| `lerna.json`, `turbo.json`, `nx.json` | Monorepo tooling |
| `pom.xml` with modules, `build.gradle` multi-project | Java/Kotlin monorepo |
| `Cargo.toml` with workspace | Rust monorepo |
| `go.work` or multiple `go.mod` | Go multi-module |
| `.sln` with multiple `.csproj` | .NET solution |
| `Bazel`, `Pants` | Large-scale build systems |

### 3. Runtime Entry Points
| Type | Common Patterns |
|------|-----------------|
| **Web** | `server.ts`, `main.py`, `Program.cs`, `index.js`, `app.py` |
| **Worker** | `worker/`, `jobs/`, `consumers/`, background services |
| **CLI** | `bin/`, `cmd/`, `cli/` |
| **Event** | Event handlers, subscribers, message consumers |

### 4. Deployment & Infrastructure
```
- Dockerfiles, docker-compose.yml
- Helm charts, Kubernetes manifests (k8s/, deploy/)
- Terraform, Pulumi, CloudFormation
- Serverless frameworks (serverless.yml)
```

### 5. CI/CD
```
- .github/workflows/
- .gitlab-ci.yml
- Jenkinsfile
- azure-pipelines.yml
- .circleci/
```

### 6. Configuration
```
- .env.example, .env.* files
- config/, settings/
- Secrets references (Key Vault, AWS Secrets Manager)
- Feature flags
```

### 7. Data Layer
```
- migrations/, db/migrate/
- Schema files (*.sql, *.prisma, *.graphql)
- ORM models (models/, entities/)
- Connection strings in config
```

### 8. Observability
```
- Logging configuration
- Metrics (Prometheus, StatsD, Application Insights)
- Tracing (OpenTelemetry, Jaeger, Zipkin)
- Health checks
```

### 9. Event-Driven Indicators
| Signal | What It Suggests |
|--------|------------------|
| Kafka, RabbitMQ, SQS, SNS, NATS clients | Message broker integration |
| `consumers/`, `producers/`, `handlers/` | Event-driven architecture |
| Outbox pattern references | Reliable event publishing |
| Topic/queue configuration | Event routing |

## Repo Traversal Methods

### A) AST-Based Indexing
Identify:
- Function/class definitions, imports, exports
- API route registrations, controllers, handlers
- Event handlers and subscriptions
- DB access points and migrations

### B) Dependency Graph Extraction
Build a graph of modules/services based on imports and runtime wiring:
- **Node.js**: `package.json` + import paths
- **Python**: `requirements.txt` + import graph
- **Java**: Module dependencies + package imports
- **Go**: `go.mod` + package imports
- **.NET**: `.csproj` references + namespace usage

Identify:
- "Hub" components (high centrality)
- Cross-cutting concerns
- Circular dependencies

### C) Entry Point Detection
| Type | Detection Method |
|------|-----------------|
| **Web** | Main server bootstrap, route registration |
| **Worker** | Queue consumers, cron jobs, schedulers |
| **Event** | Subscriptions and message consumers |
| **CLI** | Command registrations, argument parsing |

## Output Artifacts

### 1. REPO INVENTORY
```markdown
## Repo Inventory

**Project Type:** {Monorepo | Multi-service | Monolith | Library}
**Primary Languages:** {Language 1, Language 2}
**Frameworks:** {Framework 1, Framework 2}
**Build System:** {npm/yarn/pnpm | Maven/Gradle | MSBuild | etc.}
**Containerization:** {Docker | Kubernetes | Serverless | None}

### Technologies Identified
| Category | Technology | Evidence |
|----------|------------|----------|
| Backend | {tech} | {file/path} |
| Frontend | {tech} | {file/path} |
| Database | {tech} | {file/path} |
| Messaging | {tech} | {file/path} |
```

### 2. LAYOUT MAP
```markdown
## Layout Map

### Services/Modules
| Name | Path | Type | Description |
|------|------|------|-------------|
| {service} | {path} | {API/Worker/Frontend} | {inferred purpose} |

### Package Boundaries
{Describe workspace structure if monorepo}
```

### 3. BUILD + RUN BOOK (Inferred)
```markdown
## Build + Run Book (Inferred)

### Build Process
1. {Step 1}
2. {Step 2}

### Runtime Execution
- Development: {command}
- Production: {command/deployment method}

### Configuration Files
| File | Purpose |
|------|---------|
| {file} | {purpose} |
```

### 4. ENTRY POINTS LIST
```markdown
## Entry Points

### Web Entry Points
| Service | Entry File | Type | Port |
|---------|-----------|------|------|
| {service} | {file} | {REST/GraphQL} | {port} |

### Worker Entry Points
| Service | Entry File | Type |
|---------|-----------|------|
| {service} | {file} | {Queue/Cron/etc.} |

### Other Entry Points
- {CLI, event consumers, etc.}
```

### 5. DEPENDENCY GRAPH SUMMARY
```markdown
## Dependency Graph Summary

### Top 10 Dependency Edges
| From | To | Type |
|------|-----|------|
| {module} | {module} | {import/HTTP/event} |

### Hub Components (High Centrality)
1. {component} - {description}
2. {component} - {description}

### External Dependencies
| Dependency | Purpose | Version |
|------------|---------|---------|
| {dep} | {purpose} | {version} |
```

### 6. EVENT SURFACE SUMMARY
```markdown
## Event Surface Summary

### Message Brokers
| Broker | Configuration Location |
|--------|----------------------|
| {Kafka/RabbitMQ/etc.} | {path} |

### Topics/Queues
| Name | Producers | Consumers |
|------|-----------|-----------|
| {topic} | {service(s)} | {service(s)} |

### Event Patterns
- {Outbox pattern detected? Y/N}
- {Event sourcing? Y/N}
- {CQRS hints? Y/N}
```

### 7. OPEN QUESTIONS FOR PASS 2
```markdown
## Open Questions for Infer Phase

### Architecture
- {Question about overall architecture}

### Data
- {Question about data ownership}

### Integration
- {Question about external systems}

### Operational
- {Question about runtime behavior}
```

## Rules

1. **Do NOT infer business logic** - Only document structure and observable mechanics
2. **Call out workspace managers** - If layout suggests monorepo, identify boundaries
3. **List deployment signals** - If microservices, list each service and deployment indicators
4. **Map event patterns** - If event-driven, list integration points and message types

## Example Prompt

```
Read @GenDD-Flow/agents/pass1-scan-agent.md

Analyze @TargetRepo and perform Pass 1: Scan.

Generate all output artifacts:
1. Repo Inventory
2. Layout Map
3. Build + Run Book (Inferred)
4. Entry Points List
5. Dependency Graph Summary
6. Event Surface Summary
7. Open Questions for Pass 2

Output as structured markdown following the templates above.
```

## Related Resources

> **Workflow:** See [brownfield-repository-analysis.md](../workflows/brownfield-repository-analysis.md) for pass transitions, validation gates, and overall coordination.
> **Tailoring:** Apply rules from [tailoring-rules.md](tailoring-rules.md) based on detected architecture pattern during scanning.
