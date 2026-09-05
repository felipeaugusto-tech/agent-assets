# Business / Feature PRD Structure

For defining a product or feature for a mixed audience — PMs, design, leadership,
and engineering. Lighter on architecture than the technical variant; heavier on
user value, the journey, and how success is measured. The reader is deciding
*whether and what* to build, not *how* to wire it.

## Section order

Numbered outline so sections and requirements are referenceable.

### Metadata header (table, first thing in the doc)

| Field | Value |
|---|---|
| Version | e.g. 1.0 |
| Date | ISO date |
| Status | Draft / For review / Approved |
| Owner | PM / team |
| Stakeholders | Design, Eng, GTM leads |

### 1. Overview / Summary
One paragraph: what the feature is, who it's for, and the value it delivers.
Readable in thirty seconds. Follow with the problem statement — the pain today,
who feels it, and why it matters now.

### 2. Goals, Non-Goals, Success Metrics
- **Goals** — the outcomes this feature drives (business and user).
- **Non-Goals** — explicitly out of scope for this release. Insist on these; they
  prevent the "why isn't X in here" review spiral.
- **Success Metrics** — a table of metric + target, tied to product outcomes:
  activation, retention, conversion, task-completion rate, support-ticket
  reduction. Each measurable, each with a target and ideally a baseline.

### 3. Users / Personas
A table: persona, description, their goal, and their current pain. Mark the
primary persona. Keep these grounded in real user types, not invented segments.

### 4. User Journey / Experience
The core of a feature PRD. Walk the primary flow step by step — what the user
does, sees, and gets at each step. Note entry points and the "happy path," then
key edge cases and empty/error states. Reference mockups or a design system if
they exist; describe the intended experience in words if they don't.

### 5. Functional Requirements
Group by area and give every requirement a **stable ID**: `F-<AREA>-<NN>`
(e.g. `F-FLOW-01`, `F-NOTIF-02`). Each is one testable statement of what the
product does. Order or tag by priority — Must / Should / Could — so a scope cut
is obvious. Example:

```
- **F-FLOW-01** (Must) — On first login, the user sees a 3-step onboarding
  checklist; completing all three dismisses it permanently.
- **F-FLOW-02** (Should) — The checklist is resumable across sessions.
```

### 6. Scope & Prioritization
What's in this release vs. explicitly deferred. A simple in/deferred table, or a
MoSCoW breakdown. Tie back to the Non-Goals so the boundary is unambiguous.

### 7. Dependencies & Rollout
- Dependencies — teams, systems, or prior work this relies on.
- Rollout plan — full launch, beta, phased %, or feature flag; the sequence and
  any gating criteria.
- GTM touchpoints — what marketing, sales, or support need to know or prepare.

### 8. Metrics & Instrumentation
Beyond the top-line success metrics: which events/properties must be tracked to
measure the feature, and any dashboards or experiment (A/B) design.

### 9. Open Questions / Decisions
A table: #, question, current default, who decides. Honest uncertainty, visible.

### 10. Risks & Mitigations
A table: risk, likelihood, impact, mitigation. Include adoption risk and user-
experience risk, not just delivery risk.

### Appendix (optional)
Competitive notes, research links, detailed wireframe references, FAQ.

## Traps to avoid
- Describing features but never the user journey — the reader can't picture it.
- Success metrics that are actually goals ("delight users"). Make them numbers.
- No priority signal, so a scope conversation has nothing to cut against.
- Drifting into implementation detail (schemas, endpoints). If the conversation
  keeps going there, this may actually want to be a Technical PRD — check.
- Missing Non-Goals. Add them.
