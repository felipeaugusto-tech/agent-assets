---
name: stories-from-source
description: >-
  Turn an unstructured source — meeting notes, a call transcript, a PRD, a
  discovery doc, an email thread, or pasted context — into a traceable set of
  user stories with Gherkin acceptance criteria, edge cases, and NFRs, plus a
  coverage map proving nothing in the source was silently dropped. The
  decomposition pass: it decides what the stories ARE, where one ends and the
  next begins, and which lines were decisions versus someone thinking out loud.
  Use it whenever someone says "turn these notes into stories," "write user
  stories from this PRD," "break this into a backlog," "what stories come out of
  this call," or hands over any
  document and asks what to build — even if they never say "user story." Also
  use it to review a story set against its source. Do NOT use for
  deepening a single already-identified story (use requirements-enhancer),
  writing the PRD itself (use prd-writer), manual test cases from a finished
  story (use qa-test-case-writer), or sizing (use jira-story-estimator).
---

# Stories From Source

Take raw, messy input and produce a story set a team can plan against. The hard
part is not writing stories — it is **deciding what the stories are**. A
transcript contains decisions, half-ideas, tangents, constraints, and open
questions all in the same voice. Promoting a tangent to a requirement is the
single most expensive mistake this skill can make, because it looks
authoritative and lands in a backlog nobody re-reads against the source.

Two properties make the output trustworthy:

1. **Every story traces to something in the source.** No invented requirements.
2. **Every source item is accounted for.** Became a story, became an open
   question, or was deliberately parked — with a reason.

**This skill is the reusable engine and is project-agnostic.** Project truth —
stack, personas, tenancy, compliance, naming — comes from context files, never
from this file and never from assumption.

## Step 0 — Load project context

Read the project's context before reading the source. Without it you will write
stories that rename the team's existing concepts and invent endpoints that
already exist.

```bash
ls -d docs .gendd context 2>/dev/null
find . -maxdepth 3 \( -iname "context.md" -o -iname "architecture.md" \
  -o -iname "conventions.md" -o -iname "testing.md" -o -iname "agents.md" \) \
  2>/dev/null | grep -v node_modules
```

| Context Pack file | What to take from it |
|---|---|
| `context.md` | Product purpose, domain language, personas, tenancy, compliance scope |
| `architecture.md` | Services and boundaries — which stories cross which seams |
| `conventions.md` | Naming, API shape, error-response format |
| `testing.md` | Test layers — shapes the verification lines |
| `agents.md` | Constraints on how AI tooling operates in this repo |

Also read this skill's `Context.md` if present — engagement-level facts that do
not live in a client repo: scope boundaries, Jira project keys and issue types,
confirmed decisions, named stakeholders who own open questions.

**Reuse the source's and repo's own vocabulary.** A story set that renames
existing concepts creates ambiguity while claiming to remove it.

**When there is no repo** — presales, a workshop, a pasted transcript — say so
plainly, ask for the handful of facts that most change the output (product,
personas, key integrations, tenancy, compliance), and label every
project-specific claim. This is common for this skill and is fine; it is not a
reason to invent.

## Step 1 — Set scope and depth before generating

Two questions, asked together in one turn, not drip-fed:

**Depth.** How far to take each story. This is the user's call, because it
trades review effort against completeness:

| Depth | Per story | Use when |
|---|---|---|
| **Lean** | Story statement, In Scope / Out of Scope, 2–4 Gherkin ACs (happy path + primary failure) | Early shaping, backlog seeding, a large source, sprint-zero planning |
| **Solid** *(default)* | Lean + edge cases + NFRs + verification lines | Stories going into a sprint or a client deliverable |
| **Full** | Solid + integration impacts, assumptions, per-story open questions | A small, high-stakes set; regulated or contract-bound work |

Offer the default rather than asking an open question: *"I'll go Solid unless
you'd rather go Lean for a first cut — there are about 14 candidate stories in
here."* Depth can differ per story; if the source clearly has two or three
load-bearing stories among a dozen minor ones, say so and propose Full on those.

**Scope.** Confirm what the source is and what the boundary is — one feature,
one release, one epic, everything. Also ask whether there is an existing backlog
to check against, so this run adds stories rather than duplicating them.

## Step 2 — Triage the source

Read the whole source before classifying anything. Then walk it line by line and
put every substantive statement in exactly one bucket. This step is where the
skill earns its keep.

| Bucket | Looks like | Becomes |
|---|---|---|
| **Decision** | Agreed, settled, stated as fact about what will be built | A requirement in the inventory |
| **Requirement** | Stated need, unambiguous, not visibly contested | A requirement in the inventory |
| **Constraint** | Must run on X, must comply with Y, must respond within Z | An NFR, or a scope boundary |
| **Proposal** | Floated by one person, no visible agreement | Parking lot, with who raised it |
| **Question** | Explicitly unresolved, or resolution not captured | Open Questions |
| **Context** | Background, history, rationale, current-state description | Informs stories; is not a story |
| **Noise** | Scheduling, pleasantries, tangents | Dropped |

**Transcripts and meeting notes need a stricter test than documents.** In a
document, presence implies intent. In a transcript it does not — someone saying
*"we could also let admins bulk-export"* is a proposal, not a requirement, until
someone agrees. Look for the agreement signal: a second speaker confirming, an
action item, a "let's do that," a decision log line. Absent that signal, it is a
proposal and goes to the parking lot.

Signals worth reading carefully:

- **Hedged language** — "maybe," "eventually," "nice to have," "phase two." Park it.
- **Disagreement left unresolved** — two participants wanted different behavior
  and nobody closed it. That is an open question, never a story. Writing a story
  picks a winner silently.
- **Implied requirements** — "obviously they'd need to log in first." Real, but
  flag it as inferred rather than stated.
- **Someone else's scope** — work owned by another team or vendor. Note it as a
  dependency, not a story.

**Never resolve a contradiction in the source silently.** If page 4 of the PRD
contradicts page 9, both go into Open Questions naming both locations.

## Step 3 — Build the requirement inventory

Before any story is written, produce a numbered inventory. This is the spine of
the coverage map, and it makes the whole output checkable by someone who was in
the room.

| # | Requirement | Source anchor | Type | Confidence |
|---|---|---|---|---|
| R1 | Users can save a payment method for reuse | Notes §2, "agreed we store cards" | Decision | High |
| R2 | Card data must never touch our servers | Notes §2, Priya | Constraint | High |
| R3 | Admins may bulk-export members | Notes §4, Dan (no agreement) | Proposal | Parked |

**Source anchor** is a section reference, timestamp, speaker, or short phrase —
enough that a reviewer can find it in seconds. Keep quoted fragments short;
paraphrase rather than transcribing passages.

**Confidence** is High (explicit), Medium (implied but well-supported), or Low
(inferred — needs confirmation). Low-confidence items can still become stories,
but they arrive flagged.

Show the inventory to the user before writing stories when the source is large
or the stakes are high. Correcting a misread line here costs one turn;
correcting it after fifteen stories exist costs an afternoon.

## Step 4 — Decompose into stories

A story is a **vertical slice**: something a user can do end to end that
delivers value on its own. Not a layer, not a component, not a sprint's worth of
plumbing.

### How to slice

Try these in order and take the first that yields independently valuable pieces:

| Heuristic | Split by | Example |
|---|---|---|
| **Workflow steps** | Sequential stages of a journey | Search → select → configure → pay → confirm |
| **Business rule variations** | Different rules for different cases | Domestic vs. international shipping rates |
| **Persona** | Who is doing it | Member submits request / manager approves it |
| **CRUD operations** | Lifecycle stage | Create a saved card / list them / delete one |
| **Happy vs. exception path** | Main flow vs. recovery | Complete payment / recover from a declined card |
| **Data variation** | Input types or volumes | Single upload / bulk CSV import |
| **Interface** | Where it happens | Self-service UI / public API |

### When to split, when to stop

Split when a candidate story: needs more than about seven ACs; contains an "and"
joining two distinct user goals; mixes personas; or can't be demoed in one sitting.

Stop splitting when a piece delivers no standalone value — "build the database
table" is a task inside a story, not a story. Prefer a slightly large story over
a horizontal slice that ships nothing.

### Group and order

Group related stories under epics only when the source supports the grouping.
Give a suggested sequence, and name hard dependencies explicitly (*"S4 requires
S2 — the token from S2 is what S4 charges against"*). Never number stories to
imply a priority the source never established; if priority was discussed, say
where it came from.

### Check against the existing backlog

If a backlog is reachable and the user consented, search it before finalizing.
Mark each story **New**, **Duplicate of KEY-123**, or **Extends KEY-123**.
Proposing a story the team already has costs credibility in the review.

## Step 5 — Write each story

```markdown
### S[n]: [Story title]

**As a** [persona]
**I want** [capability]
**So that** [outcome that matters to them]

**Traces to:** R1, R4

#### In Scope
- [Behavior or capability that IS included]
- [Another included behavior]

#### Out of Scope
- [Behavior explicitly NOT included in this story]
- [Related work assigned to a different story or parked]

#### Acceptance Criteria

```gherkin
Scenario: [name describing the behavior, not the test]
  Given [precondition]
    And [precondition]
   When [action]
   Then [observable outcome]
    And [observable outcome]
```

**Verification:** UI: [what a tester sees] · API: [method, path, status] · Data: [what persists]

#### Edge Cases            <!-- Solid and Full -->
| Scenario | Expected behavior |
|---|---|

#### Non-Functional Requirements   <!-- Solid and Full -->
| Category | Requirement | Verification |
|---|---|---|

#### Integration Impacts   <!-- Full only -->
| Service | Change | Contract change? |
|---|---|---|

#### Assumptions           <!-- Full only, or any Low-confidence trace -->
| # | Assumption | Basis | Confirm with |
|---|---|---|---|
```

### Scope boundaries in each story

**In Scope** lists the specific behaviors, data types, personas, or workflows this story covers. Be concrete: *"member saves a card for future purchases"* not *"payment functionality."*

**Out of Scope** names work that was considered but belongs in a different story, was parked, or is explicitly deferred. This prevents the question *"why doesn't this story cover X?"* from arriving in code review. Typical out-of-scope patterns:

- **Sibling workflow** — *"Deleting a saved card"* is a separate story (S2), not this one
- **Parked proposal** — *"Bulk export of card data"* was proposed but parked (see Parking Lot, item P3)
- **Admin variant** — *"Admin override to add cards for members"* is out of scope; only members can self-serve here
- **Future phase** — *"Recurring charges using saved cards"* deferred to phase 2
- **Integration owned elsewhere** — *"PCI audit coordination"* is handled by Security team

Scope sections are not apologies — they are clarity. A well-placed **Out of Scope** entry closes a conversation before it starts.

### Gherkin discipline

Gherkin is only useful when it is declarative. Imperative Gherkin — clicking
buttons and filling fields — is a test script wearing a requirement's clothes,
and it breaks the moment the UI changes.

| Weak | Strong |
|---|---|
| `When the user clicks the "Save" button` | `When the member saves the payment method` |
| `Then the system should work correctly` | `Then the card appears in their saved methods, masked to the last four digits` |
| `Then it validates the input` | `Then the form shows "Card number must be 16 digits" beneath the card field` |
| `Given the DB has a row in tbl_cards` | `Given the member has one saved payment method` |

Rules that keep scenarios usable:

- **One `When` per scenario.** Two actions means two scenarios.
- **`Then` states an observable outcome**, with exact user-facing text where the
  wording matters. Intent cannot fail a test, so it cannot gate a release.
- **No implementation in steps** — no table names, no framework, no internal
  function. If a step names *how*, rewrite it as *what*.
- **Use `Scenario Outline` with an `Examples` table** for the same behavior
  across varying data. Three near-identical scenarios should be one outline.
- **Use `Background`** for preconditions shared by every scenario in a story —
  and only those.
- **Name scenarios after the behavior**, not "Test 1" or "Happy path."
- **Cover the negative paths.** A story whose ACs are all success is
  half-specified; the failure behavior is what gets argued about in QA.

## Step 6 — Run the three checks

These are checks on your own output, run before showing anyone. Fix what fails;
present the stories, not the checklist.

### AC check — every scenario

- Observable by a person or a test, not a statement of intent.
- Names no implementation mechanism.
- Exactly one `When`.
- Exact user-facing text given wherever copy is part of the behavior.
- Traces to a requirement in the inventory — nothing arrived from nowhere.
- The story has at least one non-happy-path scenario.

### Edge case sweep *(Solid and Full)*

Walk these categories and include the ones that genuinely apply. Four to six
real edge cases beat twelve generic ones. See
`references/edge-case-catalog.md` for prompts within each category.

Empty and null input · boundary values · permissions and roles · concurrent
action by two users · integration failure (timeout, unavailable, error
response) · duplicate submission · state already changed · cross-tenant access
where the system is multi-tenant.

**Integration failure deserves a decision, not a placeholder.** State whether
the flow degrades gracefully or fails hard. That one choice is among the most
common sources of rework and is nearly free to settle here.

### NFR sweep *(Solid and Full)*

NFRs are triggered by what the story touches, not applied uniformly. See
`references/nfr-catalog.md` for the full trigger table.

| If the story touches | Consider |
|---|---|
| Personal or payment data | Encryption, retention, access control, applicable regime (PCI, HIPAA, GDPR) |
| A user-facing screen | WCAG 2.1 AA with a stated verification method, responsive behavior |
| A list or search | Pagination, response time at realistic volume |
| An external service | Timeout, retry policy, fallback behavior |
| Authentication or roles | Session handling, privilege boundaries, audit logging |
| Bulk or batch work | Throughput, partial-failure behavior, idempotency |

Only carry NFRs the source or the Context Pack supports. An invented latency
budget is worse than a flagged gap, because it reads as agreed.

## Step 7 — Coverage map and open questions

This closes the loop and is what makes the output defensible in a review.

```markdown
## Coverage Map
| # | Requirement | Source anchor | Disposition |
|---|---|---|---|
| R1 | Users can save a payment method | Notes §2 | S1, S2 |
| R2 | Card data never touches our servers | Notes §2 | NFR on S1 |
| R3 | Admins may bulk-export members | Notes §4 | Parked — proposal, no agreement |
| R4 | Refund window length | Notes §6 | Open Question 2 — unresolved in source |

## Parking Lot
| # | Item | Why parked | Who raised it |
|---|---|---|---|

## Open Questions
1. **[Topic]** — [question]. Blocks: S3. Ask: [name or role]. (Recommendation: [defensible default])
```

**Every inventory item gets a disposition.** Silence is the failure mode this
table exists to prevent. If something was dropped as out of scope, say so and
say why.

Open Questions carry who to ask and what they block. A question with no owner
does not get answered.

## Step 8 — Deliver and hand off

Default output is a single Markdown document with Gherkin ACs inline, presented
in chat for review. Each story includes **In Scope** and **Out of Scope** sections
to clarify boundaries at the story level. Lead with a short orientation — how many 
stories, how they group, what is unresolved — then the stories.

Then offer, without doing any of it unasked:

- **Markdown file** for the repo or a doc.
- **`.feature` files**, one per story, when the team runs Cucumber, SpecFlow,
  Behave, or similar.
- **Push to Jira**, only through a genuinely available Atlassian connector and
  only after explicit confirmation *in that turn*. Confirm project key, issue
  type, and parent epic first. Map the story statement to the description,
  Gherkin to the AC field where one exists, and Open Questions to a comment.
  Report the created keys. An earlier "yes, write the stories" is not approval
  to write to Jira. Never push parking-lot items.

**Human review is mandatory, and say so on handover.** This is a strong draft
that removes ambiguity someone would otherwise chase down in a hallway. It is
not an approved backlog.

### Handoff

Name the next step rather than doing it:

- **`requirements-enhancer`** — the deep pass on any single story that is
  contested, high-risk, or heading into a sprint. This skill produces the set;
  that one hardens one story.
- **`qa-test-case-writer`** — once ACs are confirmed.
- **`jira-story-estimator`** — for sizing.
- **`adr-writer`** — if the source surfaced a real architectural decision that
  is being recorded nowhere.

## Hard rules

1. Read the whole source before classifying any part of it. Early classification
   is how tangents become requirements.
2. Never turn a proposal into a story. No agreement signal means parking lot.
3. Never resolve a contradiction or an unresolved disagreement silently — both
   sides go to Open Questions.
4. Never invent project facts — endpoints, service names, personas, compliance
   scope, thresholds. Ground them or flag them.
5. Every story traces to a numbered requirement; every requirement gets a
   disposition in the coverage map.
6. Never write an AC that states intent or prescribes implementation.
7. Every story has at least one non-happy-path scenario.
8. Every story has explicit **In Scope** and **Out of Scope** sections. Use them
   to name related work and prevent scope creep during review.
9. Never write to Jira without explicit confirmation in the same turn.
10. Never inflate the story count to look thorough. Fewer, well-sliced stories
    beat a padded backlog.
11. Say what the source did not cover. An honest gap is worth more than a
    confident guess.

## References

- `references/worked-example.md` — a full meeting-notes-to-stories run. Read it
  to calibrate depth and section shape.
- `references/edge-case-catalog.md` — prompts per edge-case category.
- `references/nfr-catalog.md` — trigger-to-NFR table with verification methods.

## Maintenance

The engine above should rarely change. Project facts belong in the repo Context
Pack or in `Context.md`, not here. Edit this file only to improve the reusable
workflow.
