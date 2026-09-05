---
name: adr-writer
description: >-
  Capture an architectural or technical decision as an Architecture Decision
  Record (ADR) through collaborative dialogue. Use this skill whenever the user
  wants to write, draft, or record an ADR, a decision record, a "why we chose X"
  doc, or a technical design decision — and also when they've just made or are
  making a consequential engineering choice (database, framework, cloud provider,
  auth approach, architecture pattern, build-vs-buy) and say things like "let's
  document this decision," "record why we went with X," "write this up so the
  team remembers," or "add an ADR for this." Trigger even when the user doesn't
  say "ADR" but is clearly recording a decision that was hard to make or hard to
  reverse. Do NOT use for product requirements (that's a PRD), general
  documentation, or decisions that carry no trade-off worth remembering.
---

# ADR Writer

An Architecture Decision Record captures what was decided, why, what else was
considered, and what it costs — so the team, and future-you, can understand the
reasoning long after the conversation that produced it is forgotten. This skill
uses the lean **Nygard format**: Title, Status, Context, Decision, Consequences.

The value of an ADR is the *reasoning*, not the conclusion. A record that says
"we chose PostgreSQL" with no defense is worthless in six months when someone
asks "why not DynamoDB?" The alternatives and the trade-offs *are* the document.

## The one rule that matters most

**Do not write the ADR file until you have (1) gathered the decision's context,
(2) surfaced the alternatives that were actually considered, and (3) shown the
user a draft they approve.** Ask questions one at a time.

This holds for *every* decision, no matter how obvious it looks. Reasoning
cannot be guessed — the forces that shaped a choice (a deadline, a bad past
experience, the team's existing skills, a cost ceiling, an existing contract)
live only in people's heads, not in the code. If you skip the dialogue you will
produce a confident, hollow record. The interview is the skill.

### Why not just infer it and write?

Two failure modes are worth naming, because they're tempting:

- **"The decision is obvious, just write it down."** If it were truly obvious
  there'd be nothing to record. ADRs exist for choices where a reasonable
  engineer could have gone another way. Skipping the alternatives produces a
  record no one can evaluate later. Always capture the roads not taken.
- **"I'll infer the context from the code."** The code shows *what* was built,
  never *why*. The forces that shaped the decision aren't in the repo. Ask.

## Process

Work through these in order. Create a task for each if you're tracking tasks.

### 1–2. Locate the ADR home and pick the next number

Look for an existing ADR directory before creating one. Check, in order:
`docs/adr/`, `docs/decisions/`, `adr/`, `docs/architecture/decisions/`. If one
exists, **match its naming and numbering convention** — don't impose `ADR-001-`
on a repo that already uses `0001-`. If nothing exists, default to `docs/adr/`
with filenames like `ADR-001-short-kebab-title.md`.

Pick the next number as the highest existing number + 1, zero-padded to the
existing width (or 3 digits by default).

### 3. Confirm the decision in one sentence

Before gathering anything, get one crisp sentence from the user: *"What is the
decision you're making?"*

- "We will use PostgreSQL for the primary datastore" is a **decision** — proceed.
- "We need a database" is a **problem**, not a decision. If you get a problem,
  the decision hasn't been made yet — help them think it through first rather
  than recording a non-decision.

### 4. Gather context — one question at a time

Ask, don't assume. Prefer multiple-choice questions where you can; they're
faster for the user. Probe the *forces* — the things in tension that make this a
real decision:

- What problem or requirement triggered this?
- What constraints bound the choice — performance, scale, budget, compliance,
  deadline?
- What does the team already know or already operate? (skills and operational
  familiarity are real forces)
- How reversible is it — a one-way door, or easy to change later?
- Any external commitments — existing contracts, mandated platforms, prior ADRs?

One question per message. If a topic needs depth, take several turns on it. The
goal is a Context section built from what the user actually knows, not a plausible
-sounding paragraph you invented.

### 5. Surface the alternatives and their trade-offs

This is the part teams skip and later regret. For each serious option that was
considered, capture what it offered and the *specific* reason it lost. "We
considered DynamoDB but the team has no operational experience with it and our
access patterns are relational" is worth more than the decision itself.

If the user says there were no alternatives, push gently once — there is almost
always a do-nothing option or an obvious default that got rejected. Name it.

### 6. Establish the status

- **Proposed** — under discussion, not yet adopted.
- **Accepted** — decided and in effect.
- **Deprecated** — no longer recommended, not yet replaced.
- **Superseded by ADR-NNN** — replaced by a later decision. Link it, and update
  the *old* ADR's status when you supersede it.

### 7–9. Draft, get approval, then write

Fill the template in `references/adr-template.md`. Then:

- Keep **Context** factual and force-focused — the problem and the pressures, no
  solution-talk.
- Keep **Decision** active and specific — "We will…", verifiable, not "we should
  consider…".
- Make **Consequences** honest — list the negative and neutral outcomes, not just
  the wins. A consequences section with only benefits is a red flag that the
  analysis was shallow; every architectural choice has costs, so find and name
  them.

Present the draft. Revise until the user approves. **Only then** run the
self-review below, write the file with the correct numbered filename, and tell
the user the path.

## Self-review before writing

Scan the draft for each of these and fix inline:

| Check | What you're looking for |
|---|---|
| No placeholders | No "TBD", "TODO", or bracketed stubs left in the file. |
| Context is forces, not solution | Context describes the problem and pressures, not the chosen tech. |
| Alternatives present | At least one real alternative with a concrete reason it lost. |
| Honest consequences | Negative/neutral consequences listed, not only benefits. |
| Decision is active | "We will X" — specific and verifiable. |
| Status is set | One of Proposed / Accepted / Deprecated / Superseded. |
| Filename + number | Correct next number, zero-padded, kebab-case title, in the ADR dir. |

## Red flags

If you catch yourself thinking any of these, stop — you're about to produce a
weak ADR:

- *"This decision is too small for an ADR."* → If it's hard to reverse or someone
  will ask "why?", it earns a record.
- *"I'll just list why we chose it."* → Without the rejected alternatives, the ADR
  can't be evaluated later.
- *"The consequences are all positive."* → Every architectural choice has costs.
- *"I can fill in the context myself."* → Forces live in people's heads. Ask.
- *"Let me write it and they'll edit."* → Draft → approve → write. Don't skip the
  approval gate.

## Key principles

- **One question at a time** — build the picture incrementally, don't overwhelm.
- **The trade-offs are the document** — alternatives and consequences carry the
  value, not the conclusion.
- **Immutable record** — ADRs aren't edited after acceptance; a new decision
  supersedes an old one with a new ADR.
- **Concise and durable** — a good ADR fits on a page or two and reads cleanly
  years later.
- **Match the project** — respect existing ADR conventions; don't impose your own.
