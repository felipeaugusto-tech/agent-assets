# ADR Template (Nygard format)

The five core sections — **Title, Status, Context, Decision, Consequences** —
are the whole record. Everything below the core is optional and used only when a
decision genuinely warrants it. Keep the whole thing to a page or two; length is
not a proxy for quality.

## Core template

```markdown
# ADR-NNN: <short decision title>

**Status:** <Proposed | Accepted | Deprecated | Superseded by ADR-MMM>
**Date:** <YYYY-MM-DD>

## Context

<The forces at play. What problem or requirement triggered this decision? What
constraints bound it — performance, scale, budget, compliance, deadline, team
skills, existing contracts, prior ADRs? Write this so a reader who wasn't in the
room understands the pressures. Factual and force-focused — do NOT describe the
chosen solution here.>

## Decision

<The decision, stated actively and specifically: "We will …". One or a few
paragraphs, or a short structured list if the decision has several parts. Specific
and verifiable — a reader can check whether the built system matches it.>

## Consequences

<What becomes true once this is adopted — the good, the bad, and the neutral.
Be honest about the costs and the new constraints, not just the benefits. A
useful pattern is three groups:>

**What gets easier / better**
- …

**What gets harder / what we give up**
- …

**What to watch**
- <risks this introduces and how they'll be caught or mitigated>
```

## The Consequences section is where honesty lives

An ADR whose Consequences are all upside was not thought through. Every real
architectural choice trades something away — cost, flexibility, a new dependency,
operational burden, a skill the team has to acquire. Name those explicitly. If
you truly can't find a downside, you may be recording a non-decision.

## Alternatives — don't lose them

The lean template folds alternatives into Context or Decision, but they must
appear *somewhere*, because they're the main reason the ADR has value later. Use
whichever fits:

- A short **"Alternatives considered"** subsection under Decision, or
- Inline in Context ("We evaluated X, Y, and Z…").

For each serious alternative, give the concrete reason it lost:

```markdown
### Alternatives considered

- **DynamoDB** — rejected. Our access patterns are relational (multi-table joins
  for reporting) and the team has no operational experience with it.
- **Managed MySQL** — rejected. Viable, but we already run Postgres elsewhere and
  want one database technology to operate.
- **Do nothing / SQLite** — rejected. Won't survive the concurrency we expect
  within two quarters.
```

## Optional extended sections (only when warranted)

Larger or higher-stakes decisions sometimes justify more than the lean five. Add
these *only* when they earn their place — an empty or padded section erodes trust
in the rest of the document.

**Metadata header table** — for ADRs with authors, scope, or a companion doc:

```markdown
| | |
|---|---|
| **Status** | Accepted |
| **Date** | 2026-06-01 |
| **Authors** | Name / team |
| **Scope** | One line on what this decision covers |
| **Companion** | Link to the PRD or design doc, if any |
```

**"What changed" delta** — when this ADR supersedes or derives from an earlier
one, a short section listing what was removed, changed, kept, and added makes the
supersession legible at a glance. (Remember to update the superseded ADR's status.)

**References** — links to prior ADRs, external docs, tickets, or specs that
informed the decision.

Deeper artifacts — project structure, code sketches, cost estimates — belong in a
design doc or the companion PRD, not the ADR. Include them in an ADR only if they
are genuinely part of *the decision itself* and a reader can't understand the
choice without them. When in doubt, link out and keep the ADR lean.
