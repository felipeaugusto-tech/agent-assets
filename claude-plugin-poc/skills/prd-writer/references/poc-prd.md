# PoC / Spike PRD Structure

For a proof of concept or spike: a deliberately scoped-down build whose job is to
*prove something* — a hypothesis, a technical approach, a risky integration —
fast, without production hardening. What separates a good PoC PRD from a
technical one is that it is loud and explicit about what it is **not** building
and why cutting that is safe. That honesty is what earns stakeholder trust to
ship a stripped build.

A PoC PRD is usually a technical PRD with two things added up front (what it is,
what's stripped) and much of the enterprise depth removed. Read
`technical-prd.md` too if the PoC still has real architecture and data.

## Section order

### Metadata header (table, first thing in the doc)

| Field | Value |
|---|---|
| Version | e.g. PoC-1.0 |
| Date | ISO date |
| Status | For build |
| Owner | Name / team |
| Scope of this PRD | One line: what the PoC covers and, crucially, what it doesn't |
| Derived from | Link to the full/parent PRD if one exists; note this supersedes it for PoC scope only |

### What this PoC is (short prose block, right after metadata)
Two or three sentences describing the end-to-end thing that will actually work.
Concrete: a person does X, the system does Y, the demo shows Z. This anchors
everyone on the single golden path the PoC proves.

### What's stripped / changed from the full build
The signature section of a PoC PRD. Group the cuts and, for each, say *why it's
safe to defer* — ideally noting whether re-adding it is additive or a
rearchitecture. Example groupings:

- **Stripped — enterprise items** (multi-tenancy, RLS, CMEK, audit sinks,
  compliance control matrices). *"Re-introducing tenancy later is additive — a
  column and a policy, not a refactor."*
- **Stripped — per build constraints** (CI/CD, multi-env matrix, heavy IaC).
- **Stripped — optional adapters/integrations** not needed for the golden path.
- **Changed** — where the PoC does something differently than the full build
  (e.g. simpler auth, a single approval mechanism replacing many gates). State
  the change and the reasoning.

This section is what makes the scope defensible. Spend real effort here.

### 1. Executive Summary
One paragraph: what the PoC proves and the core approach. Point at the parent
PRD / ADR for the full picture.

### 2. Goals, Non-Goals, Success Metrics
- **Goals** — the specific things this PoC must demonstrate end to end.
- **Non-Goals (this PoC)** — everything deliberately out of scope. This overlaps
  the "stripped" section but framed as commitments, not deltas.
- **Success Metrics** — a table with concrete pass/fail targets. For a PoC these
  are often binary ("fixture completes a full session: Yes/No") plus one or two
  performance numbers.

### 3. Personas (trimmed)
Only the personas the PoC actually exercises. Note which roles are stubbed vs.
fully functional.

### 4. Build Phases (lean)
A collapsed phase table — PoCs phase to order the work, not to gate releases.
Each phase gets a demonstrable exit criterion.

### 5. Functional Requirements
Same discipline as the technical PRD: group by area, **stable IDs**
(`F-<AREA>-<NN>`), one testable statement each. Mark PoC-critical requirements.
Where a requirement is a deliberately simplified version of the full build's,
note that inline.

### 6. Non-Functional Requirements (PoC-level)
Prefix `NFR-<AREA>-<NN>`. Keep the ones that still matter (basic security, the
one or two real performance targets, durability of the thing being proved) and
explicitly note which full-build NFRs are out of scope and why.

### 7. Architecture (as needed)
Only the parts real in the PoC. If a piece of infrastructure is "load-bearing"
(genuinely required even in the PoC) vs. "enterprise scaffolding" (cut), say so —
justifying why the surviving complexity survived is as important as justifying
the cuts.

### 8. Data Model (as needed)
The tables/entities the PoC uses, minus the enterprise columns/policies that were
stripped. Note that removed items are additive later.

### 9. Open Decisions
Table: #, decision, current default, who decides. PoCs generate lots of "confirm
before first real use" items — capture them.

### 10. Risks & Mitigations
Table: risk, likelihood, impact, mitigation. Include the PoC-specific risk that
a cut corner turns out *not* to be safe to defer.

### Appendix (optional)
Inventory of what's built vs. explicitly out of scope, so the boundary is a
single glanceable list.

## Traps to avoid
- Writing a full technical PRD and calling it a PoC. If there's no "what's
  stripped" section, it isn't a PoC PRD.
- Cutting scope without saying why it's safe — that reads as sloppiness, not
  strategy.
- Vague success criteria. A PoC's whole point is a clear pass/fail.
- Forgetting the path back to production — stakeholders want to know the cuts
  aren't permanent dead ends.
