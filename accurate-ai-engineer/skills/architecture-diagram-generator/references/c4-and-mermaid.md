# C4 and Mermaid Reference

Contents:
1. The four levels — scope and audience
2. Per-level checklists
3. Mermaid C4 macro reference
4. Level 4 in Mermaid
5. Layout pitfalls
6. Worked examples

---

## 1. The four levels — scope and audience

C4 works because each level answers one question for one audience. Mixing levels
is the most common way a diagram becomes useless to everybody at once.

| Level | Answers | Audience | Shows | Never shows |
|---|---|---|---|---|
| L1 Context | What is this system and who touches it? | Everyone, including non-technical | One system box, people, external systems | Technology, internal structure |
| L2 Container | What are the moving parts and how do they talk? | Technical, including ops | Deployables, their tech, protocols | Internal code structure |
| L3 Component | How is *one* container organised? | Developers on that container | Components behind interfaces | Other containers' internals |
| L4 Code | How is *one* component built? | Whoever is about to change it | Classes, key relationships | Anything not in that component |
| Deployment | Where does it run? | Ops, SRE, security, ARB | Containers mapped to infrastructure | Application internals |

**Container** means a separately runnable or deployable unit: a server-side app, a
SPA, a mobile app, a database, a message broker, a serverless function. It does
*not* mean a Docker container, and it is not a code module.

**Component** means a grouping of related functionality behind a clean interface,
inside one container. Components are not independently deployable — if it deploys
on its own, it is a container.

Level 4 is optional in the C4 model and generally not worth maintaining by hand.
Prefer generating it on demand for a component someone is actively working on.

---

## 2. Per-level checklists

### L1 Context
- [ ] Exactly one system box is in scope, and its name matches what the org calls it
- [ ] Every human or system that interacts with it appears, and nothing else does
- [ ] External systems are marked external, with ownership clear
- [ ] No technology labels anywhere on this diagram
- [ ] Every relationship is a verb phrase reading source → target
- [ ] A non-technical stakeholder could read it without a walkthrough
- [ ] It fits on one screen

### L2 Container
- [ ] Every element is genuinely separately deployable
- [ ] Each container carries its technology (language, framework, runtime)
- [ ] Datastores and brokers appear as containers, with their engine named
- [ ] Every relationship states its protocol or mechanism (HTTPS/JSON, gRPC, SQL, AMQP)
- [ ] The system boundary wraps the containers in scope and excludes external systems
- [ ] Actors from L1 connect to the specific containers they reach
- [ ] Nothing here is a code module masquerading as a container

### L3 Component
- [ ] The title names which container is being decomposed
- [ ] Only that container's internals appear; others show as single boxes
- [ ] Each component has a technology and a one-line responsibility
- [ ] Components map to real code groupings, with paths in the ledger
- [ ] Relationships crossing the container boundary are shown but not expanded

### L4 Code
- [ ] Someone explicitly asked for it
- [ ] It covers exactly one component, named in the title
- [ ] It shows the types that matter, not every type
- [ ] Expressed as a Mermaid `classDiagram` (or `erDiagram` for a data model)

### Deployment
- [ ] Every node is grounded in IaC, CI config, or a confirmed answer
- [ ] The environment is named in the title
- [ ] Nodes nest the way the infrastructure nests (region → cluster → pod)
- [ ] Container instances are placed on nodes, with counts where they vary
- [ ] Unverified elements are visibly labeled as assumptions

---

## 3. Mermaid C4 macro reference

Mermaid's C4 support is **experimental**; syntax follows C4-PlantUML and may change
between releases. Five diagram types: `C4Context`, `C4Container`, `C4Component`,
`C4Dynamic`, `C4Deployment`.

**Elements** (alias, label, then technology and/or description depending on type):

```
Person(alias, "Label", "Description")
Person_Ext(alias, "Label", "Description")
System(alias, "Label", "Description")
SystemDb(alias, "Label", "Description")
SystemQueue(alias, "Label", "Description")
System_Ext(alias, "Label", "Description")
SystemDb_Ext(alias, "Label", "Description")
Container(alias, "Label", "Technology", "Description")
ContainerDb(alias, "Label", "Technology", "Description")
ContainerQueue(alias, "Label", "Technology", "Description")
Container_Ext(alias, "Label", "Technology", "Description")
Component(alias, "Label", "Technology", "Description")
ComponentDb(alias, "Label", "Technology", "Description")
```

**Boundaries** (braces enclose members):

```
Enterprise_Boundary(alias, "Label") { ... }
System_Boundary(alias, "Label") { ... }
Container_Boundary(alias, "Label") { ... }
Boundary(alias, "Label", "type") { ... }
Deployment_Node(alias, "Label", "Type", "Description") { ... }   # C4Deployment
Node(alias, "Label", "Type", "Description") { ... }              # shorthand
```

**Relationships:**

```
Rel(from, to, "Label", "Technology")
Rel_U / Rel_D / Rel_L / Rel_R    # direction-pinned variants
BiRel(a, b, "Label", "Technology")
```

**Styling and layout** (place at the end; named params take a `$` prefix):

```
UpdateElementStyle(alias, $bgColor="...", $fontColor="...", $borderColor="...")
UpdateRelStyle(from, to, $offsetX="-40", $offsetY="20", $textColor="...", $lineColor="...")
UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="2")
```

Every diagram opens with its type and a `title` line.

Verify by rendering rather than trusting this list — macro availability varies with
the Mermaid version in play.

**Never backslash-escape a quote inside a label.** `"...the \"NewPlatform\" service..."`
looks fine to a human and to a naive brace/quote counter, but Mermaid's C4 grammar
does not treat `\"` as an escaped character — it sees a literal quote and ends the
string there, so everything after it is parsed as syntax and the diagram breaks.
This is silent in a plain read-through because the quote count still balances; it
only shows up when Mermaid actually parses the file. If a label needs an embedded
quoted term, use a single quote (`'NewPlatform'`) or drop the quoting and let the
word stand on its own — never `\"`. The bundled linter (`lint_c4.py`) flags this as
an ERROR.

**Never put a raw `<letter` inside a label**, e.g. `(dist-<env>-schdl target)`.
Mermaid renders C4 element labels through an HTML `foreignObject`, so `<env>` is
parsed as an opening HTML tag, not literal text — it can silently vanish from the
rendered box or break layout, without any parse error to flag it. Spell the
placeholder out in words instead (`the per-environment dist-*-schdl target`). The
linter flags a bare `<` followed by a letter as an ERROR outside `classDiagram`
files (where `<<stereotype>>` is legitimate Mermaid syntax).

**Every `Deployment_Node`/boundary body must contain at least one statement.**
`Deployment_Node(s3, "S3 Bucket", "AWS S3") { }` — braces immediately followed by
nothing — is a hard parse error in Mermaid's C4 grammar, confirmed against
mermaid-cli: `Expecting 'PERSON', 'CONTAINER', ... got 'RBRACE'`. This is easy to
write by accident for an infrastructure node that doesn't obviously "contain" one
of your system's containers (an S3 bucket, a CodeDeploy application, a load
balancer) — the instinct is to describe it and leave the body empty. Braces are
mandatory on these macros (a bare `Deployment_Node(...)` with no braces at all is
*also* a parse error — `Expecting 'LBRACE', got 'NODE'`), so the fix is never to
drop the braces, always to put something inside: model what that node actually
hosts as a `Container` (an S3 bucket hosts the deployment bundle as a `zip`
container; CodeDeploy hosts an orchestrator process; a load balancer hosts its
listener/endpoint). The linter's `check_empty_boundaries` flags this as an ERROR
for every boundary type, not just `Deployment_Node`.

**`Rel()` must target a `Person`/`System`/`Container`/`Component` alias, never a
boundary or `Deployment_Node` alias.** `Rel(s3, codedeploy, "Is pulled from by")`
where both `s3` and `codedeploy` are `Deployment_Node` aliases passes Mermaid's
parser but crashes the renderer at layout time (`TypeError: Cannot read
properties of undefined (reading 'x')` — the layout engine expects every `Rel`
endpoint to be a positioned leaf element, and a boundary has no single position).
Once every node has a `Container` inside it (per the rule above), point relationships
at those `Container` aliases instead: `Rel(bundleArtifact, codedeployAgent, ...)`,
not `Rel(s3, codedeploy, ...)`. The linter flags any `Rel` endpoint whose declared
kind is a boundary/`Deployment_Node`/`Node` as an ERROR.

Both of the above were only caught by actually rendering with mermaid-cli
(`npx --yes @mermaid-js/mermaid-cli -i file.mmd -o /tmp/check.svg` — works without
any project install and without a full browser download failing in most sandboxes)
— they pass a naive brace-count and read fine to a human, which is exactly why a
real render matters and "the braces balance" is not the same claim as "this parses."

---

## 4. Level 4 in Mermaid

There is no `C4Code` diagram type. Use a standard class diagram:

```
classDiagram
    title Code diagram — DispatchAssignmentService
    class DispatchAssignmentService {
        +assign(jobId, crewId) AssignmentResult
        -validateRegion(job, dispatcher) void
    }
    class JobRepository {
        +findById(id) Job
        +save(job) void
    }
    DispatchAssignmentService --> JobRepository : reads and persists Jobs
```

For a data model, `erDiagram` is the better fit.

---

## 5. Layout pitfalls

Mermaid does not auto-layout C4 diagrams intelligently. Practical consequences:

- **Statement order determines position.** If the result looks tangled, reorder the
  element definitions before reaching for styling.
- **Use the direction-pinned `Rel_U/D/L/R` variants** to stop long arrows crossing
  the diagram.
- **`UpdateLayoutConfig`** controls shapes per row — the most effective single fix
  for a diagram that renders too wide.
- **Split rather than cram.** A fifty-service architecture is several focused
  diagrams; one exhaustive diagram communicates nothing.
- **Styling is limited by design.** C4 in Mermaid has fixed styling; the point is
  communication, not visual polish.
- Long labels widen boxes aggressively. Keep descriptions to one clause.

---

## 6. Worked examples

### L1 Context

```
C4Context
    title System Context — Fieldwork Ops Platform
    Person(dispatcher, "Dispatcher", "Assigns jobs to crews within their region")
    Person(crewLead, "Crew Lead", "Receives and completes assigned jobs in the field")
    System(fieldwork, "Fieldwork Ops Platform", "Scheduling and dispatch for utility field crews")
    System_Ext(twilio, "Twilio", "Third-party SMS and push delivery")
    Rel(dispatcher, fieldwork, "Assigns Jobs and monitors progress using")
    Rel(crewLead, fieldwork, "Receives assignments from, updates status in")
    Rel(fieldwork, twilio, "Sends crew notifications via", "HTTPS/REST")
```

### L2 Container

```
C4Container
    title Container Diagram — Fieldwork Ops Platform
    Person(dispatcher, "Dispatcher", "Assigns jobs within their region")
    System_Boundary(fieldwork, "Fieldwork Ops Platform") {
        Container(web, "Dispatcher Console", "React, TypeScript", "Job assignment and monitoring UI")
        Container(dispatchApi, "dispatch-api", "Node.js, Express", "Owns Job and Dispatch Run lifecycle")
        Container(crewSvc, "crew-svc", "Node.js", "Crew roster, availability, skills matrix")
        Container(notifySvc, "notify-svc", "Node.js", "Delivers SMS and push to crew devices")
        ContainerDb(db, "Operational Store", "PostgreSQL 15", "Jobs, Dispatch Runs, crew assignments")
        ContainerQueue(bus, "Event Bus", "Cloud Pub/Sub", "Domain events consumed by audit-log")
    }
    System_Ext(twilio, "Twilio", "Third-party SMS and push delivery")
    Rel(dispatcher, web, "Assigns Jobs using", "HTTPS")
    Rel(web, dispatchApi, "Makes API calls to", "HTTPS/JSON")
    Rel(dispatchApi, db, "Reads from and writes to", "SQL/TCP")
    Rel(dispatchApi, crewSvc, "Checks crew availability via", "HTTPS/JSON")
    Rel(dispatchApi, bus, "Publishes Job events to", "Pub/Sub")
    Rel(notifySvc, twilio, "Sends messages via", "HTTPS/REST")
    UpdateLayoutConfig($c4ShapeInRow="3")
```

Note what these examples do: technology on every container, protocol on every
relationship, verb phrases reading source → target, external systems outside the
boundary, and no internals of any single container.
