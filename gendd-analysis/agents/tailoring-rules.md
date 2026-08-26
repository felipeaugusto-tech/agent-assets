# Architecture Tailoring Rules

Use these tailoring rules in Scan/Infer/Document passes based on detected architecture pattern.

## If Monorepo Detected

### Scan Phase
Identify:
- Workspace tooling: nx/turbo/lerna/yarn/pnpm workspaces; Gradle/Maven multi-module
- Package boundaries and shared dependencies
- Build orchestration patterns

### Infer Phase
Produce:
- **Package boundary map** - Which packages exist and their purposes
- **Shared libs vs apps separation** - What's shared vs application-specific
- **Cross-package dependency hotspots** - High coupling areas

### Document Phase
Emphasize:
- How to run each app locally
- Shared library change impact analysis
- Enforced boundaries (if any)
- Package-level testing strategy

### Key Questions for Validation
1. Are package boundaries enforced by tooling?
2. What's the deployment model - together or independent?
3. Which packages can be changed in isolation?

---

## If Microservices Detected

### Scan Phase
Identify:
- Separate Dockerfiles/Helm charts/service manifests per service
- Independent CI pipelines
- Service-to-service communication patterns
- API gateway or service mesh

### Infer Phase
Produce:
- **Service catalog** with owners and responsibilities
- **API contracts** between services (REST, gRPC, GraphQL)
- **Cross-service tracing/logging** patterns
- **Service dependency graph**

### Document Phase
Emphasize:
- Integration testing strategy
- Backward compatibility risks
- Versioning and rollout concerns
- Service-level SLAs
- Circuit breaker and retry patterns

### Key Questions for Validation
1. Are services deployed independently?
2. What's the contract testing strategy?
3. How are breaking changes handled?
4. Who owns each service?

---

## If Event-Driven Detected

### Scan Phase
Identify:
- Brokers: Kafka/RabbitMQ/SQS/SNS/NATS
- Producers and consumers
- Message schemas and contracts
- Dead letter queues (DLQs)
- Idempotency patterns

### Infer Phase
Produce:
- **Event catalog:** topic/queue → message type → producer(s) → consumer(s)
- **Delivery guarantees:** exactly-once vs at-least-once assumptions
- **Replay/rerun behavior**
- **Event sourcing patterns** (if present)

### Document Phase
Emphasize:
- Failure modes (poison messages, consumer lag)
- Schema evolution and compatibility
- Outbox/CDC patterns if present
- Event ordering requirements
- Consumer group management

### Key Questions for Validation
1. What happens if a consumer fails?
2. Are messages idempotent?
3. How is schema evolution handled?
4. What are the replay capabilities?
5. Are there any ordering requirements?

---

## If Hybrid Architecture Detected

### Scan Phase
- Identify which parts follow which pattern
- Map the boundaries between patterns
- Note transition points

### Infer Phase
Produce:
- **Pattern map:** Which components use which pattern
- **Boundary documentation:** How patterns interact
- **Consistency model:** How data consistency is maintained across patterns

### Document Phase
Emphasize:
- Pattern-specific documentation for each section
- Interaction points between patterns
- Complexity hotspots at pattern boundaries
- Testing strategies for each pattern

### Key Questions for Validation
1. Why was each pattern chosen?
2. Are there plans to consolidate patterns?
3. What are the pain points at pattern boundaries?

---

## Pattern Detection Signals

### Monorepo Signals
| Signal | Confidence |
|--------|------------|
| `pnpm-workspace.yaml`, `lerna.json`, `turbo.json`, `nx.json` | High |
| Multiple `package.json` in subdirectories | High |
| Single `.git` with multiple apps/services | Medium |
| Shared `node_modules` or dependency hoisting | Medium |
| `packages/`, `apps/`, `libs/` folder structure | Medium |

### Microservices Signals
| Signal | Confidence |
|--------|------------|
| Multiple Dockerfiles in different directories | High |
| Separate deployment manifests (Helm, k8s) per service | High |
| Independent `package.json`/`pom.xml`/`.csproj` per service | High |
| Service mesh configuration (Istio, Linkerd) | High |
| API gateway configuration | Medium |
| Separate CI pipelines per service | Medium |

### Event-Driven Signals
| Signal | Confidence |
|--------|------------|
| Kafka/RabbitMQ/SQS client libraries | High |
| `consumers/`, `producers/`, `handlers/` directories | High |
| Message schema definitions (Avro, Protobuf) | High |
| Outbox pattern implementation | High |
| Topic/queue configuration files | Medium |
| Event sourcing framework usage | High |

---

## Documentation Templates by Pattern

### Monorepo: Package Map Template
```markdown
## Package Map

### Applications
| Package | Path | Purpose | Dependencies |
|---------|------|---------|--------------|
| {app} | {path} | {purpose} | {shared libs} |

### Shared Libraries
| Package | Path | Purpose | Used By |
|---------|------|---------|---------|
| {lib} | {path} | {purpose} | {apps} |

### Dependency Graph
```
app-a → shared-utils, shared-ui
app-b → shared-utils, shared-api-client
```
```

### Microservices: Service Catalog Template
```markdown
## Service Catalog

### {Service Name}
| Attribute | Value |
|-----------|-------|
| **Owner** | {team/person} |
| **Repository** | {path} |
| **API Type** | REST/gRPC/GraphQL |
| **Port** | {port} |
| **Deployment** | {method} |
| **Dependencies** | {services} |

#### API Endpoints
| Method | Path | Purpose |
|--------|------|---------|
| {method} | {path} | {purpose} |

#### Consumes From
| Service | API/Event | Purpose |
|---------|-----------|---------|
| {service} | {api} | {purpose} |

#### Produces To
| Consumer | API/Event | Purpose |
|----------|-----------|---------|
| {service} | {api} | {purpose} |
```

### Event-Driven: Event Catalog Template
```markdown
## Event Catalog

### Topic: {topic-name}

**Broker:** {Kafka/RabbitMQ/etc.}
**Partition Strategy:** {key/round-robin}
**Retention:** {duration}

#### Message Types
| Message | Schema | Purpose |
|---------|--------|---------|
| {type} | {schema-ref} | {purpose} |

#### Producers
| Service | Trigger | Rate |
|---------|---------|------|
| {service} | {trigger} | {rate} |

#### Consumers
| Service | Consumer Group | Processing |
|---------|----------------|------------|
| {service} | {group} | {at-least-once/exactly-once} |

#### Failure Handling
- **DLQ:** {yes/no, location}
- **Retry Policy:** {policy}
- **Poison Message Handling:** {approach}
```
