# Technical PRD Structure

For an engineering-led build: a system with real architecture, data, and
interfaces that a dev team will implement from. This is the most complete
variant. Include the sections that carry weight for the product in front of you
and omit the ones that don't — an empty "API Spec: N/A" is worse than no section.

## Section order

Use a numbered outline so every section and requirement is referenceable.

### Metadata header (table, first thing in the doc)

| Field | Value |
|---|---|
| Version | e.g. 1.0 |
| Date | ISO date |
| Status | Draft / For review / For build / Approved |
| Owner | Name / team |
| Scope | One line describing what this version covers |

If this supersedes or derives from another doc, note it here.

### 1. Executive Summary
One paragraph in plain language: what the system is, who it's for, and the core
approach. A busy exec should understand the shape of it in thirty seconds. Then
one short paragraph on the technical approach (stack, architecture pattern) with
a pointer to the detail below.

### 2. Goals, Non-Goals, Success Metrics
- **Goals** — numbered list of what this build achieves. Outcomes, not features.
- **Non-Goals** — what is explicitly out of scope, each with a clause on why or
  what handles it instead. Do not skip this.
- **Success Metrics** — a table of metric + target. Every row must be measurable
  (`P95 latency < 8s`, `zero manual steps in the pipeline`). Move anything
  unmeasurable up into Goals.

### 3. Personas / Users
A table: persona, description, and the surfaces/permissions they touch. Separate
internal from external users if that distinction matters. Mark the primary user.

### 4. Scope & Access Model (include if there's auth/RBAC)
Roles and a permission matrix (roles as columns, actions as rows, ✅/❌ cells).
Describe the unit of data partitioning (tenant, engagement, workspace, account).

### 5. Build Phases (include if phased)
A table: phase, theme, what's in scope, and the concrete **exit criterion** that
proves the phase is done. Exit criteria should be demonstrable, not vibes.

### 6. Functional Requirements
The heart of the document. Group by area and give every requirement a **stable
ID**: `F-<AREA>-<NN>` (e.g. `F-AUTH-01`, `F-UI-03`, `F-API-02`). Number within a
group so inserting later doesn't renumber everything.

Each requirement is one testable statement of behavior:

```
- **F-AUTH-01** — Google SSO via the identity provider, domain-restricted to
  the company domain. Server exchanges the ID token for an HTTP-only cookie.
- **F-AUTH-02** — Only @company.com emails may complete sign-in.
```

Write requirements a QA engineer could turn into a pass/fail test. If a
requirement needs rationale or a boundary clarification, add a short `>` note
beneath it. Flag PoC-critical or high-risk requirements inline.

### 7. Non-Functional Requirements
Prefix `NFR-<AREA>-<NN>`. Cover the categories that apply: Security, Privacy,
Reliability, Observability, Performance, Scalability, Compliance. Each is a
concrete, checkable statement with a number where possible.

### 8. System Architecture
- Logical architecture — a diagram (ASCII box diagram is fine) plus a paragraph
  explaining the shape and why it's shaped that way.
- Component/service mapping — a table of each service/component and its role.
- Key design decisions — call out anything load-bearing or non-obvious, with the
  reasoning. Link to an ADR if one exists.

### 9. Data Model
Main entities, their key fields, and relationships. A schema sketch (SQL,
TypeScript/ORM, or a table per entity) plus notes on partitioning, cascade/
deletion behavior, and any PII flags. Only as much precision as the build needs.

### 10. API / Interface Specification (include if it exposes/consumes interfaces)
A table: method, path, auth, purpose. Note the transport (REST/JSON, gRPC, SSE,
webhooks) and streaming behavior. Enough for a client to be built against it.

### 11. Model / Integration Strategy (include if relevant)
For AI/ML systems: per-component model assignments and why. For integration-heavy
systems: each external surface and how it's used, authed, and rate-limited.

### 12. Open Decisions
A table: #, decision, current default/notes, and who needs to decide. This is
where honest uncertainty lives. Mark resolved rows ✅ rather than deleting them,
so the history is visible.

### 13. Risks & Mitigations
A table: risk, likelihood, impact, mitigation. Cover technical, delivery, and
dependency risks. A PRD with no risks isn't reassuring — it's unfinished.

### Appendix (optional)
Inventories, glossaries, detailed enumerations (e.g. an agent/component list, a
full config-key list) that would clutter the body.

## Traps to avoid
- Requirements with no ID, or IDs that renumber when you insert one.
- "The system should be fast/secure/scalable" with no target — that's an NFR
  waiting to be made concrete.
- A data model or API spec invented from nothing. If the user didn't specify it,
  ask, or list it as an Open Decision — don't fabricate a schema and present it
  as settled.
- Non-Goals section missing. Add it.
