---
name: prd-writer
description: >-
  Write, structure, or improve a Product Requirements Document (PRD). Use this
  skill whenever the user wants to create a PRD, spec, product spec, requirements
  doc, feature brief, PoC/proof-of-concept scope, or engineering design doc — and
  also when they describe a product, feature, or system they want to build and
  ask you to "write it up," "spec it out," "document the requirements," or "turn
  these notes into a proper doc." Trigger even when the user doesn't say the word
  "PRD" but is clearly trying to define what to build, for whom, and why (e.g.
  "we need a doc the eng team can build from," "help me scope this feature,"
  "draft the requirements for the new onboarding flow"). Do NOT use for pure
  project plans/timelines with no product definition, marketing copy, or code
  implementation itself.
---

# PRD Writer

A PRD earns its keep by making a team agree on the same thing before anyone
builds it. A good one is unambiguous enough to build from, honest about what it
*won't* do, and traceable — every requirement can be pointed at, argued about,
and checked off. A bad PRD is a wall of prose that sounds thorough but leaves
every hard decision implicit, so the team discovers the disagreements during
QA instead of during review.

This skill helps you produce the good kind, for any of three document types,
by interviewing the user for the decisions that actually matter and then writing
a tight, structured document.

## The workflow

1. **Pick the variant** (below). Ask if it's not obvious from context.
2. **Interview** the user for the essentials — don't write a PRD full of `[TBD]`.
3. **Confirm output format** — Markdown, Word (`.docx`), or both.
4. **Write** the document using the variant's structure.
5. **Flag what's still open** — unresolved questions become an Open Decisions
   section, not silent guesses.

### Step 1 — Pick the variant

Ask the user which kind of document they need, or infer it and confirm. The
three variants share DNA (goals, users, requirements, scope) but differ in
depth and audience:

| Variant | For | Signals | Reference |
|---|---|---|---|
| **Technical PRD** | Engineering-led build. Includes architecture, data model, APIs, NFRs. | "eng team will build from this," a system with backend/data/integrations, mentions of stack, scale, or security. | `references/technical-prd.md` |
| **Business / feature PRD** | Product/feature definition for a mixed audience. Lighter on architecture, heavier on user value, UX, and success metrics. | "new feature," "onboarding flow," GTM framing, stakeholders are PMs/design/leadership. | `references/business-prd.md` |
| **PoC / spike PRD** | A scoped-down proof of concept derived from (or ahead of) a larger build. Explicit about what's deliberately *stripped*. | "proof of concept," "prototype," "validate the approach," "single-tenant," "no enterprise hardening," time-boxed. | `references/poc-prd.md` |

If the user is genuinely between two (common between technical and PoC), ask a
single disambiguating question: *"Is this the full production build, or a
time-boxed proof of concept where we deliberately cut scope?"* The answer decides
it.

Read the matching reference file for the section-by-section structure before you
start writing. Don't rely on memory for the template — the references carry the
detail and the ordering.

### Step 2 — Interview before you write

The quality of a PRD is set before the first sentence, by whether you actually
know what's being built. Skipping this produces a confident-sounding document
that's wrong in ways nobody notices until build time.

Read `references/interview-questions.md` for the full question bank organized by
variant. The universal core, which you need for *every* PRD:

- **What is it, in one or two sentences?** If the user can't say it plainly,
  the PRD can't either — help them get there.
- **Who is it for?** Distinct user types / personas, and which one is primary.
- **Why now / what problem?** The pain being solved and how we'll know it's solved.
- **What's explicitly out of scope?** The single most-skipped, most-valuable
  question. Non-goals prevent scope creep and set reviewer expectations.
- **What are the hard constraints?** Deadline, budget, existing stack, compliance,
  team size, dependencies.

Ask these in a compact batch rather than one at a time — respect the user's time.
If the user has already provided rich context (a transcript, a brief, existing
notes), mine it first and only ask about the genuine gaps. Never interrogate the
user for something they already told you.

If the user insists on a draft *now* with little input, write it — but mark every
assumption inline and gather the guesses into the Open Decisions section so the
gaps are visible rather than buried.

### Step 3 — Confirm output format

Ask: Markdown, Word document, or both? Default to Markdown if the user doesn't
care — it's the most portable and easiest to iterate on.

- **Markdown** — write the `.md` directly.
- **Word (`.docx`)** — first draft the full content, then read the `docx` skill's
  `SKILL.md` and use it to produce the file. Don't hand-roll `.docx`.
- **Both** — write the `.md`, then generate the `.docx` from the same content.

## What makes these PRDs good (applies to every variant)

These principles are why the templates are shaped the way they are. Follow the
spirit, not just the section headers.

**Requirements get stable IDs.** Every functional requirement carries a short,
stable identifier — `F-AUTH-01`, `F-UI-03`, and so on, grouped by area. This is
the single highest-leverage habit in the whole document. IDs let people say
"F-AUTH-02 is wrong" in a review, let QA map tests to requirements, and let a
later revision say "F-AUTH-02 is removed" without ambiguity. Number within a
group (`AUTH`, `UI`, `API`…) so inserting a requirement later doesn't renumber
everything. Non-functional requirements get their own prefix (`NFR-SEC-01`).

**Non-goals are as important as goals.** A PRD that only says what it *will* do
invites everyone to imagine their favorite extra feature into scope. State what
you are deliberately *not* doing and, where useful, one clause on why. This is
where you prevent the expensive misunderstanding.

**Success is measurable.** "Improve engagement" is not a success metric; "P95
response < 8s" and "80% of users complete onboarding without support contact"
are. Push for numbers and targets. If a metric can't be measured, it's a goal,
not a metric — put it in the right place.

**Open questions are surfaced, not hidden.** Real products have undecided
things. A mature PRD lists them in an Open Decisions table with a current
default and who needs to decide — it does not paper over them with confident
prose. Reviewers trust a document more when it's honest about what's unresolved.

**Every claim is checkable.** Prefer tables and short declarative requirements
over paragraphs. If a reader can't tell whether a sentence has been satisfied by
looking at the built thing, rewrite it until they can.

**Right-size the document.** A two-week feature does not need a data model and an
API spec; a platform build does. Omit sections that don't apply rather than
padding them with filler — an empty "Architecture: N/A" section erodes trust in
the rest. The variant references tell you which sections are load-bearing for
each type.

**Lead with a metadata header and a one-paragraph "what this is."** Version,
date, status, owner, and scope up top; then a plain-language paragraph a busy
executive can read in thirty seconds and know what they're looking at. Everything
after that is detail for the people who need it.

## Output conventions

- Start with a metadata table: Version, Date, Status, Owner, and Scope.
- Use a numbered section outline so requirements and sections are referenceable.
- Prefer tables for personas, requirements, metrics, risks, and open decisions.
- Keep prose tight. The reader is scanning to build or to approve, not to enjoy.
- When revising an existing PRD, preserve requirement IDs and add a short
  "Changes from previous version" section noting what was added, changed, or cut.
