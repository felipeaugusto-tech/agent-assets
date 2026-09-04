# Workflow: Spec Authoring

## Overview

A spec documents the technical design of a change — the interfaces, data shapes, contracts, and edge-case behavior — separate from *why* the change is happening (that's an ADR) and separate from *how the work is sequenced* (that's an implementation plan). It's the "how" half of the design pair: `adr-writer` produces the decision and its trade-offs; a spec produces enough detail that two engineers implementing the same spec independently would build compatible things.

**When a spec earns its place:** a new API surface, a new data model, an integration with an external system, or any change where "what exactly does this do at the boundary" isn't obvious from the requirement alone. A small internal refactor doesn't need one — go straight to an implementation plan.

## When to Use

- After a decision is made (via ADR or otherwise) but before implementation-planning the work, when the decision doesn't yet specify enough detail to break into file-level tasks.
- When a spike (see `workflows/spike-doc.md`) produced findings that need to become a committed design rather than staying exploratory.
- When an interface will be consumed by more than one team or system, and drift between what was intended and what was built would be costly.

## Prerequisites

- The decision this spec implements — an ADR, or a clear statement of what's being built and why.
- Any spike findings that inform the design.

## Process

### Step 1: State what this spec covers and what it doesn't

A spec that tries to cover everything covers nothing precisely. Name the boundary: this endpoint, this data model, this integration — not "the whole feature."

### Step 2: Define the interface or contract

Whatever the boundary is — an API, a function signature, a schema, an event payload — define it precisely enough that someone else could implement against it without asking a follow-up question. Use file references for anything that already exists as a pattern to follow (e.g. "response envelope matches `ApiResponse<T>` in `shared/types/api.ts`").

### Step 3: Cover the edge cases explicitly

For each input or state that isn't the happy path: what happens. Empty input, not-found, unauthorized, concurrent modification, partial failure — whichever apply. A spec silent on error behavior forces the implementer to guess, and two implementers will guess differently.

### Step 4: Note what a spike resolved, if one preceded this

If a spike investigated an unknown (which library, which approach, whether an assumption holds), fold its conclusion in here as settled fact, with a pointer to the spike doc for the reasoning — don't make the reader re-derive it.

### Step 5: Flag open questions rather than guessing

If something genuinely isn't decided yet, list it under Open Questions rather than picking an answer silently. A spec with unresolved questions is more useful than a spec with confidently wrong answers.

### Step 6: Get review before it's treated as settled

A spec is a coordination tool — its value comes from more than one person agreeing it's right before code gets written against it.

## Never Invent

A field, endpoint, or behavior not grounded in the actual decision being implemented or an explicit requirement is a guess dressed as a spec. Where the source material (ADR, requirement, spike) doesn't answer a question the spec needs answered, that's an Open Question, not a place to improvise.

## Output Artifacts

Save to `docs/specs/{feature-slug}.md` in the target repository, using `templates/spec-template.md`.

## Verification Checklist

- [ ] Boundary of what this spec covers is explicit
- [ ] Interface/contract is precise enough to implement without follow-up questions
- [ ] Edge cases and error behavior are covered, not left to implementer judgment
- [ ] Spike conclusions (if any) are folded in as settled, with a pointer to the spike doc
- [ ] Open questions are listed, not silently resolved
- [ ] Reviewed before being treated as final

## Related Resources

> **Decision context:** `adr-writer` (vendored skill) — the what-and-why this spec assumes is settled.
> **Precedes:** `workflows/implementation-plan.md` — turns this spec into sequenced, file-level tasks.
> **Input:** `workflows/spike-doc.md` — when a spike's findings feed directly into this spec's design.
> **Template:** `templates/spec-template.md`.
