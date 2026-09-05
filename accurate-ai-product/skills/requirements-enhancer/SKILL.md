---
name: requirements-enhancer
description: >-
  Expand vague product requirements into engineer-ready acceptance criteria
  — observable, testable, with scope control, edge cases, integration
  impacts, NFRs, test scenarios, and open questions. The shift-left
  story-quality pass, run before development and QA. Use it whenever someone
  wants a thin feature request turned into a real story, or says "flesh this
  out," "write the acceptance criteria," "this story is too vague," "add
  edge cases," "what are we missing here," "make these ACs testable," or
  "groom this before sprint planning" — also to rewrite ACs that state
  intent or implementation instead of observable behavior. Always reads the
  GenDD repository docs folder (Context Pack) first, checks it covers the
  requirement, and asks for clarification when it doesn't; never invents
  project facts. Do NOT use for authoring a PRD (use prd-writer), generating
  test cases from a finished story (use qa-test-case-writer), estimating
  (use jira-story-estimator), or recording a technical decision (use
  adr-writer).
---

# Requirements Enhancer (Shift-Left Story Quality)

Take a thin requirement — often two or three sentences from product — and turn it
into a story an engineer can build and a tester can verify without a hallway
conversation. The value is not volume. It is removing ambiguity early, where it
is cheap, instead of discovering it in code review, QA, or production.

**This skill is the reusable engine and is project-agnostic by design.** Project
truth — stack, integrations, tenancy model, compliance scope, personas, naming —
comes from context files, not from this file and not from your own assumptions.
That separation is what lets the same engine serve any engagement: to onboard a
new project you supply context, not a new skill.

## Step 0 — Load project context (every run, before anything else)

**In a GenDD project there is always a docs folder, and reading it is not
optional.** It is where the Context Pack lives, and it is the difference between a
story grounded in the actual system and a well-formatted guess. Never expand a
requirement on assumed project facts when the docs folder exists and simply was
not read.

Three parts: find and read it (0a), judge whether what you found is enough for
*this* requirement (0b), and ask when it is not (0c).

### 0a. Read the GenDD Context Pack — the repository `docs` folder

Find and read the Context Pack before asking the user anything. **Discover the
location; do not assume it.** Look for a docs folder and the Context Pack markdown
files within it:

```bash
# Locate candidate context locations (adjust root as needed)
ls -d docs .gendd context 2>/dev/null
find . -maxdepth 3 -iname "agents.md" -o -iname "context.md" -o -iname "conventions.md" \
  -o -iname "testing.md" -o -iname "architecture.md" 2>/dev/null | grep -v node_modules
```

The Context Pack conventionally comprises five repository-level files. Read
whichever exist, and use them for what each is actually good for:

| Context Pack file | What to take from it |
|---|---|
| `context.md` | Product purpose, domain language, personas, tenancy model, compliance scope |
| `architecture.md` | Services and boundaries — drives the Integration Impacts section |
| `conventions.md` | Naming, API shape, error-response format, status-code conventions |
| `testing.md` | Test layers and verification norms — drives the Verification lines and Test Scenarios |
| `agents.md` | How AI tooling is expected to operate in this repo; honor any constraints it sets |

If the folder holds other GenDD artifacts — prior stories, ADRs, discovery
output, a glossary — read what is relevant to the requirement at hand. **Reuse the
repo's own vocabulary.** A story that renames the team's existing concepts creates
new ambiguity while claiming to remove it.

Beyond the Context Pack, ground claims in the code itself where it is cheap to
do so. If the requirement touches an endpoint, a permission, or a schema, check
whether it already exists before writing an AC that presumes otherwise. A
grounded AC referencing a real route beats an invented one every time.

### 0b. Sufficiency check — is this enough for *this* requirement?

Reading the docs folder is step one; judging what you read is step two. The test
is not whether the Context Pack is complete in the abstract — it rarely is, and a
generic completeness audit produces noise. The test is narrower and more useful:

> **Does the docs folder answer the questions this specific requirement raises?**

Walk the requirement and check whether the context supports each of these. Only
the ones the requirement actually touches matter.

| Needed for | Sufficient when the docs folder tells you |
|---|---|
| The story actor | Who the persona is, and what they are entitled to do |
| Observable outcomes | The system's error-response and status-code conventions |
| Integration impacts | Which services own the affected behavior, and their boundaries |
| Integration failure ACs | Each dependency's failure contract — or that it is undefined |
| Tenancy ACs | Whether the system is multi-tenant, and what a cross-tenant request returns |
| NFRs | Compliance regime in scope, and standing performance or accessibility baselines |
| Verification lines | Test layers in use, and how verification is normally expressed |
| Vocabulary | The domain terms this feature area already uses |

Also check the code, not just the prose, where it is cheap: if the requirement
touches an endpoint, a permission, or a schema, confirm whether it already exists
before writing an AC that presumes otherwise. A grounded AC citing a real route
beats an invented one every time, and the docs folder can lag the code.

### 0c. Ask when the context falls short

When the sufficiency check comes up short — or the docs folder is missing, stale,
or holds only placeholders — **stop and ask.** Do not quietly downgrade to
assumptions, and do not expand the requirement anyway with a caveat at the bottom.
An unread or insufficient context folder is a recoverable problem that costs one
question; a story built on invented facts is not, because it looks authoritative
and propagates into tickets, tests, and code.

Ask well:

- Name the specific gap and what it blocks: *"`architecture.md` doesn't say which
  service owns notification delivery — I can't write the integration impacts or a
  failure-path AC without it."*
- Ask only what this requirement needs. A requirement touching one endpoint does
  not need the whole tenancy model explained.
- Consolidate into one round of questions, not a drip of one-at-a-time asks.
- Offer the likely answer where you have a defensible one, so confirming is faster
  than composing: *"I'd assume cross-tenant reads return 404 rather than 403 —
  correct?"*
- Say where you looked. If `docs/` exists but the Context Pack files are absent,
  that is worth flagging on its own — it usually means the pack was never
  generated or has drifted, which affects more than this story.

If the user says to proceed without the missing context, do it — but every
resulting gap becomes a labeled assumption in the output, and the story is marked
as grounded on unconfirmed facts. **Never invent project specifics to close a
gap.** A fabricated endpoint, service name, or compliance boundary is worse than
an honest flag, because it reads as authoritative and quietly misleads everyone
downstream.

### 0d. Companion `Context.md` (optional, engagement-level)

Read `Context.md` from this skill's directory if present. It carries facts that do
not belong in a client repo or are not there yet: engagement scope boundaries,
confirmed product decisions, an open-contradiction log, delivery-team conventions,
Jira project keys and issue-type conventions, and named stakeholders who own open
questions. It supplements the docs folder; it does not substitute for it.

**Precedence when sources disagree:** the repo Context Pack wins on technical
reality (what the system is and does). `Context.md` wins on engagement reality
(what was decided, by whom, and what is in scope). If they conflict on the same
fact, do not pick a winner silently — surface the conflict as an open question
naming both sources, and flag any AC that depends on it as an assumption.

### 0e. When there is no repository at all

Occasionally the requirement arrives with no repo in reach — a presales
conversation, a workshop, a requirement pasted in isolation. Say so plainly, ask
for the handful of facts that most change the output (product, persona,
integrations, tenancy, compliance scope), and proceed with every project-specific
claim explicitly labeled. This is the exception, not a fallback to reach for when
reading the docs folder is inconvenient.

## The three rules that make an AC useful

These are the substance of the skill. Everything else is structure.

### Rule 1 — Observable, not intended

An AC must describe behavior someone can watch happen, at the UI and at the API.
Intent cannot fail a test, so it cannot gate a release.

| Intent (not testable) | Observable behavior (testable) |
|---|---|
| "Only users with AdminWrite can create orders" | "A user without AdminWrite: (1) does not see the Create Order button, (2) receives 403 from POST /api/orders" |
| "The system prevents duplicate orders" | "Submitting an order for a patient with one pending: submission is blocked and the message reads 'Order already in progress for this patient'" |
| "Data is secured" | "An unauthenticated request receives 401 and the audit log records the attempt with timestamp and source IP" |

Quote user-facing message text exactly. "Shows an error" is not verifiable — two
engineers will build two different errors and QA cannot fail either one.

### Rule 2 — Outcomes, not solutions

An AC states what the user experiences. How it is built is the engineer's call,
and naming a mechanism in an AC both constrains a decision that is not yours and
produces something QA cannot verify from outside the system.

| Technical solution | Observable outcome |
|---|---|
| "MRN locking prevents conflicts" | "When two users create orders for the same patient simultaneously, one succeeds; the other sees 'Order in progress'" |
| "Use Redis for caching" | "Subsequent page views load in under 200ms at p95" |
| "Implement optimistic locking" | "Saving stale data shows 'Data changed by another user, please refresh' and the save is rejected" |

A genuine technical constraint is real, but it belongs in the NFR table or a note
to engineering — not in an AC where it masquerades as verifiable behavior.

### Rule 3 — Scope control

An enhanced story that swallows every edge case becomes unestimable, and the
team's actual response is to ignore the AC list. Split explicitly: what must be
done for this story to be accepted, and what becomes a follow-up ticket. Every
follow-up item must be specific enough to file as-is. "Handle edge cases later"
is not a ticket.

## Workflow

```
[0. Load context] → [1. Intake] → [2. Ambiguity gate] → [3. Generate]
→ [4. Self-check] → [5. Deliver / optional Jira push]
```

Work one requirement at a time. To batch, confirm the full list up front, then
carry each requirement all the way through before starting the next.

## Step 1 — Intake

Accept a pasted requirement, an uploaded spec, or a ticket ID via a connector.
When given a ticket ID, fetch the description, the full comment thread, and
attachments before asking anything — scope walk-backs and clarifications live in
comments far more often than in the description.

Then extract what is already answerable from the requirement plus Step 0 context.
Ask only for what genuinely remains, as one consolidated list.

| Input | Why it matters |
|---|---|
| The requirement itself | The thing being expanded |
| Product / system area | Anchors terminology and the affected services |
| User persona | Drives the story actor and which flows matter |
| Existing integrations | Determines integration-failure edge cases |
| Multi-tenant? | Tenancy isolation ACs are mandatory when yes |
| Compliance scope | Drives NFRs (payment, health data, privacy regimes) |
| Tech stack | Shapes realistic verification lines |

Most of these should come from Step 0. Asking the user for a fact that sits in
`architecture.md` wastes their time and signals the context was not read.

## Step 2 — Ambiguity gate

Not all ambiguity is equal, and treating it as if it were either blocks work
needlessly or ships guesses as requirements.

**Structural gaps block generation.** If the requirement lacks a clear actor, a
clear outcome, or any indication of what success means, stop. Expanding it would
produce plausible-looking fiction that is expensive to unwind once it is in Jira.
Name precisely what is missing, propose the specific question to put to product,
and offer to draft that message.

**Detail gaps do not block.** Missing retention windows, exact limits, precise
copy, specific thresholds — proceed, choose a defensible default, label it
visibly as an assumption, and carry it into the Open Questions section with a
recommendation. Product can accept the default in seconds; they cannot answer a
question nobody wrote down.

Every assumption that survives into the output appears in Open Questions. An
assumption that is not surfaced becomes an undocumented decision.

## Step 3 — Generate

Use this section order. Omit a section only when it genuinely does not apply, and
say why rather than dropping it silently.

```markdown
# [Story title]

## User Story
AS A [persona]
WHEN [context or trigger]
I WANT TO [capability]
SO THAT [outcome that matters to them]

## Scope Control
### In this story (required for acceptance)
- [ ] [core capability]
- [ ] [error handling for the common failure]
- [ ] [validation]

### Follow-up stories (file separately)
- [ ] [specific, fileable item]

## Acceptance Criteria

### AC1: [name]
GIVEN [precondition]
AND [precondition]
WHEN [action]
THEN:
- [observable outcome, with exact user-facing text where applicable]
- [observable outcome]

**Verification:**
- UI: [what a tester sees or does]
- API: [method, path, expected status]
- Data: [what persists, or tenancy expectation]

## Edge Cases (in scope)
| Scenario | Expected behavior |
|---|---|

## Integration Impacts
| Service | Change | Type | Contract change? |
|---|---|---|---|

## Non-Functional Requirements
| Category | Requirement | Verification |
|---|---|---|

## Test Scenarios
| # | Scenario | Steps | Expected |
|---|---|---|---|

## Assumptions
| # | Assumption | Basis | Confirm with |
|---|---|---|---|

## Open Questions
1. **[Topic]**: [question] (recommendation: [default applied])
```

**Coverage expectations.** One AC per distinct behavior, including the failure
paths. At least five edge cases, drawn from: empty and null input, boundary
values, permission and role variations, concurrency, integration failure
(timeout, unavailable, error response), and — whenever the system is multi-tenant
— explicit cross-tenant isolation. Accessibility belongs in the NFR table as
WCAG 2.1 AA with a stated verification method, not as a vague aspiration.

Integration failure deserves a decision, not a placeholder: state whether the
primary flow degrades gracefully or fails hard. That single choice is one of the
most common sources of rework, and it is nearly free to settle here.

Cite the source for any grounded claim — file, endpoint, or Context Pack section
— so a reviewer can check it. Where a claim is not grounded, it is an assumption
and belongs in that table.

## Step 4 — Self-check before showing the user

Run this and fix what fails. Do not present the checklist as output; present the
story, and mention only what remains genuinely unresolved.

- Every AC is observable and states exact user-facing text where relevant.
- No AC names an implementation mechanism.
- Every AC has a verification line covering UI and API.
- Multi-tenant isolation is explicitly tested when tenancy applies.
- In-scope and follow-up work are cleanly split; every follow-up is fileable.
- The story is estimable — it is not open-ended.
- At least five edge cases, including one integration failure.
- NFRs cover performance, security, accessibility, and any compliance regime in scope.
- Test scenarios cover happy path, a failure, and an edge case.
- Every assumption appears in both the Assumptions table and Open Questions.
- No invented endpoint, service, or field name; every specific is grounded or flagged.

## Step 5 — Deliver

Default output is Jira-ready Markdown, presented in chat for review. Then offer:

- **Markdown file** — for the repo, a doc, or a paste into Jira.
- **Push to Jira** — only via a genuinely available Atlassian connector, and only
  after the user confirms. Confirm the project key, issue type, and parent epic
  first; map the User Story to the description, ACs to the AC field if the
  project has one, and Open Questions to a comment addressed to the story owner.
  Report the created key. Never create or edit a ticket without explicit
  confirmation in that turn — an earlier "yes, expand this" is not approval to
  write to Jira.

Do not push follow-up stories as tickets unless the user asks for that
separately, and confirm each one. Silently spawning a backlog is not helpful.

**Human review is mandatory.** This output is a strong draft that removes
ambiguity a person would otherwise chase down — it is not an approved
requirement. Say so when handing it over.

### Handoff

Name the natural next step rather than doing it unasked: `qa-test-case-writer`
once ACs are confirmed, `jira-story-estimator` for sizing, `adr-writer` if the
work surfaced a real architectural decision.

## Hard rules

1. Always read the repository docs folder before expanding anything. In a GenDD
   project it exists; not reading it is never acceptable.
2. When the docs folder does not cover what the requirement needs, ask. Do not
   substitute assumptions for a question you could have asked in one turn.
3. Never invent project facts — endpoints, service names, compliance scope,
   personas. Ground them in Step 0 context or flag them.
4. Never write an AC that describes intent rather than observable behavior.
5. Never write an AC that prescribes implementation.
6. Never proceed past a structural gap. Detail gaps proceed with a labeled
   assumption; structural gaps stop and ask.
7. Never let an assumption stay invisible — it appears in the output every time.
8. Never write to Jira without explicit confirmation in the same turn.
9. Never silently resolve a contradiction between context sources — surface both.
10. Never inflate scope to look thorough. Everything in the in-scope list must be
   required for acceptance.

## Reference

`references/worked-example.md` — a full input-to-output example (a saved payment
method requirement, expanded end to end). Read it when the expected shape of a
section is unclear, or to calibrate depth.

## Maintenance

The engine above should rarely change. Project facts change in the repo Context
Pack or in `Context.md`, not here. Edit this file only to improve the reusable
workflow itself.
