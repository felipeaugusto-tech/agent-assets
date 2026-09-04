---
name: architecture-diagram-generator
description: >-
  Generate C4 architecture diagrams — Context, Container, Component,
  optional Code, and Deployment — from an actual codebase, traced to
  file-level evidence rather than assumption. Recommends LikeC4
  (architecture-as-code: one validated model, many views) and falls back to
  hand-written Mermaid whenever the user prefers it. Use it whenever someone
  wants architecture diagrams or a C4 model, or says "diagram this repo,"
  "map the architecture," "show me how this system fits together,"
  "architecture docs for onboarding," "prep this for the Architecture Review
  Board," or wants an AS-IS/TO-BE pair for a migration — also to review C4
  diagrams that have drifted from the code. Reads the GenDD docs folder
  first, updates existing diagrams rather than duplicating them, and asks
  when the repo cannot answer (external system ownership, deployment
  topology with no IaC, intended target state). Do NOT use for recording a
  technical decision (use adr-writer) or writing acceptance criteria (use
  requirements-enhancer).
---

# Architecture Diagram Generator (C4 → Mermaid)

Produce C4 diagrams that describe the system as it actually is. The failure mode
worth designing against is not an ugly diagram — it is a *plausible* one: a tidy
three-tier picture that any reviewer would nod at, assembled from architectural
convention rather than from this repository. Such a diagram is worse than none,
because it gets committed, reviewed, and then quietly trusted.

So the governing rule is simple: **every element and every relationship traces to
something you actually read.** If it cannot, it is a question for a human, not a
box on a canvas.

## Step 0 — Read the docs folder first

In a GenDD project there is always a docs folder, and it matters here for three
distinct reasons.

```bash
ls -d docs .gendd 2>/dev/null
ls docs/architecture/ 2>/dev/null          # existing diagrams — update, don't duplicate
find . -maxdepth 3 \( -iname "architecture.md" -o -iname "context.md" \
  -o -iname "conventions.md" \) 2>/dev/null | grep -v node_modules
```

1. **`architecture.md` in the Context Pack** states the intended architecture:
   services, ownership, boundary rules. It is the design intent to check the code
   against — not a substitute for reading the code.
2. **`docs/architecture/` may already hold diagrams.** If it does, this run is an
   update. Read them first, diff against what the code now shows, and lead with
   what changed. Silently replacing a diagram someone hand-corrected destroys
   work and is hard to notice in review.
3. **Brownfield analysis, ADRs, and prior discovery output**, where present, are
   the cheapest available source of *why* the architecture looks as it does. A
   diagram that contradicts a recorded decision is worth a flag either way — the
   decision may have been reversed without the ADR being superseded.

Where the code and `architecture.md` disagree, **the code is what is deployed and
the document is what was intended.** Diagram the code, and report the drift
explicitly — that drift is often the single most valuable output of this whole
exercise, especially before an ARB.

## Step 1 — Choose the notation (LikeC4 recommended, Mermaid on request)

**Detect first, ask only if undetermined.**

```bash
ls docs/architecture/*.c4 docs/architecture/*.likec4 2>/dev/null
grep -rl "likec4" package.json */package.json 2>/dev/null
ls likec4.config.* 2>/dev/null
ls docs/architecture/*.mmd 2>/dev/null
```

If the repo already commits `.c4` sources, use LikeC4 and say nothing further —
asking a team to reconsider a tool they already adopted is noise. If it already
commits `.mmd` files and no `.c4`, stay on Mermaid unless the user raises it.

When neither exists, **recommend LikeC4 once, briefly, with the actual reason, and
accept the answer immediately.** Something close to:

> I'd suggest LikeC4 for this rather than hand-written Mermaid. One model, many
> views — so the Context, Container, and Component diagrams can't drift out of
> agreement with each other — and `likec4 validate` actually fails on a broken
> reference, where Mermaid silently renders a typo'd alias as a new empty box. It
> also generates Mermaid on demand, so nothing's lost. `npx likec4` needs no
> install. Want that, or plain Mermaid?

Then honor it. "Mermaid is fine" ends the discussion — do not re-pitch later in the
run, and do not treat the Mermaid path as degraded, because it is not: `.mmd` files
render natively in GitHub, GitLab, and many wikis with no toolchain at all, which
is a real advantage for a team that will not adopt a DSL.

**Recommending is not installing.** Never run an install, add a dependency, or
modify `package.json` without explicit consent. `npx likec4 validate` runs without
touching the project, and the VS Code extension is the user's choice to make.

Read `references/likec4.md` for the DSL, CLI, and level-to-view mapping before
writing `.c4`. Read `references/c4-and-mermaid.md` before writing `.mmd`. The C4
discipline in Step 4 applies identically to both — the notation changes, the
standard does not.

## Step 2 — Evidence sweep

Inventory before drawing. The goal is a defensible answer to three questions:
what is in scope, what runs separately, and what it talks to.

Start broad, then read the files that actually decide the answer:

```bash
# Shape of the thing
git ls-files | head -200
git ls-files | sed 's|/[^/]*$||' | sort -u | head -40

# Deployable units and their tech
find . -maxdepth 4 \( -name "package.json" -o -name "pom.xml" -o -name "build.gradle*" \
  -o -name "pyproject.toml" -o -name "requirements.txt" -o -name "go.mod" \
  -o -name "Cargo.toml" -o -name "*.csproj" -o -name "Gemfile" \) \
  -not -path "*/node_modules/*" 2>/dev/null

# Runtime topology and infrastructure
find . -maxdepth 3 \( -name "Dockerfile*" -o -name "docker-compose*.y*ml" \
  -o -name "*.tf" -o -name "serverless.y*ml" -o -name "Pulumi.y*ml" \
  -o -path "*/k8s/*" -o -path "*/.github/workflows/*" -o -name "*.bicep" \) 2>/dev/null

# External dependencies: what does it call out to?
grep -rIl --exclude-dir={node_modules,.git,dist,build} -E \
  "https?://[a-z0-9.-]+\.[a-z]{2,}" . 2>/dev/null | head -20
```

`references/evidence-sources.md` maps each diagram level to where its truth
lives, per ecosystem — read it when a stack is unfamiliar or the layout is
unusual.

**What counts as evidence for each level:**

| Level | Grounded in |
|---|---|
| Context (L1) | Auth config and roles (actors), outbound integrations, API clients, webhooks, SDK dependencies |
| Container (L2) | Separate manifests and entry points, Dockerfiles, compose/k8s services, datastore and broker connection config |
| Component (L3) | Module and package structure inside **one** container, route registrations, DI wiring, service classes |
| Code (L4) | The types in one component — only where genuinely warranted (see Step 3) |
| Deployment | IaC, CI/CD pipelines, k8s manifests, environment config, hosting settings |

Two distinctions that decide L2 correctness, and are routinely gotten wrong:

- **A container is a separately runnable or deployable unit** — an app, an API, a
  SPA, a mobile app, a database, a message broker, a serverless function. It is
  not a Docker container specifically, and not a code module.
- **A monorepo is not automatically multiple containers, and one repo is not
  automatically one.** Count deployables, not folders: three packages built into
  one image are one container; one repo deploying an API plus a worker plus a
  scheduled job is three.

Keep an **evidence ledger** as you go — element, and the path that justifies it.
It drives the grounding audit in Step 5 and the citations in the output.

## Step 3 — Sufficiency gate, then ask

Some things are simply not in the repository, and no amount of further reading
will produce them. Recognizing these fast is the difference between one good
question and an invented diagram.

Commonly absent, and what to do:

| Not derivable from code | Ask for |
|---|---|
| Who owns an external system, and whether it is in-house or third-party | Ownership, and whether it sits inside the enterprise boundary |
| Which human roles actually use the system | The real actor list — auth roles are a proxy, not an answer |
| Deployment topology when there is no IaC | Where this runs, how many instances, which regions |
| Whether a dependency is live or vestigial | Confirmation — dead config outlives dead integrations |
| Target state for a migration | The intended TO-BE, which is a decision, never an inference |
| System boundary for a monorepo or platform | Which system this diagram is about |

Ask well: name the gap and what it blocks, propose the answer you would default
to, keep it to one consolidated round, and ask only what the requested levels
need — a Context diagram does not require the deployment topology.

> "There's no IaC in the repo, so I can't ground the Deployment diagram. From the
> GitHub Actions workflow it looks like Cloud Run in us-east1, single region — is
> that right, and how many instances per environment? I can produce L1–L3 now and
> add Deployment once you confirm."

If the user says proceed without an answer, do — but mark the affected elements as
unverified in the diagram itself and list them under the output's Assumptions.
**Never invent infrastructure.** A confident deployment diagram with no IaC behind
it is the most dangerous artifact this skill can produce.

## Step 4 — Generate

The levels below are identical on both paths. What differs is what you write.

**On the LikeC4 path**, the order changes shape: build the model once
(`specification` → `model` → `deployment`), then define one view per level. There
is no per-level duplication, which is the point. LikeC4 does not enforce level
discipline, so hold it deliberately via the level-to-view mapping in
`references/likec4.md` — `view index` for L1, `view containers of <system>` for L2,
`view of <system>.<container>` for L3, a deployment view per environment.

**On the Mermaid path**, write one file per level, and note two things:

- **Mermaid's C4 support uses specific diagram types:** `C4Context` for L1,
  `C4Container` for L2, `C4Component` for L3, `C4Deployment` for deployment.
  Syntax follows C4-PlantUML, and layout depends on statement order — there is no
  auto-layout. **Using the wrong diagram type will make all diagrams look the same.**
- **There is no `C4Code` type.** Level 4 is a `classDiagram` (or `erDiagram` for a
  data model). Do not use C4 macros for it.

Generate levels in order, because each constrains the next. Use the **exact diagram
type** and **specific contents** for each level:

1. **Context (L1) — Use `C4Context` diagram type**
   - Exactly one system box in scope (no internals)
   - People/actors who interact with it (using `Person` or `Person_Ext`)
   - External systems it talks to (using `System_Ext`)
   - **NO technology labels anywhere**
   - **NO internal structure, containers, or components**
   - If this diagram needs a scrollbar, the system boundary is wrong.

2. **Container (L2) — Use `C4Container` diagram type**
   - The deployables inside the system boundary (using `Container`, `ContainerDb`,
     `ContainerQueue`)
   - Each container must carry its technology explicitly (language, framework)
   - A `System_Boundary` wrapping all containers in scope
   - External systems outside the boundary (using `System_Ext` or similar)
   - How they communicate, with protocol on every relationship (HTTPS/JSON, gRPC,
     SQL, AMQP)
   - Actors connecting to the containers they actually reach
   - **NO code-level details, no internal component structure**

3. **Component (L3) — Use `C4Component` diagram type**
   - Title must name which container is being decomposed
   - Components using `Component` or `ComponentDb` **only for the chosen container**
   - Other containers show as single boxes (not decomposed)
   - Components map to real code groupings, with paths in the evidence ledger
   - Each component must have technology and responsibility
   - Relationships crossing container boundary shown but not expanded
   - **NO other containers' internals, no code details**

4. **Code (L4) — Use `classDiagram` diagram type (never use C4 macros)**
   - **Default to skipping this.** Produce it only where someone explicitly asked
     and a component is genuinely intricate, because it decays fastest.
   - Covers exactly one component, named in the title
   - Shows key types and relationships that matter, not every class
   - For a data model, use `erDiagram` instead
   - **NO C4 macros or C4 styling**

5. **Deployment — Use `C4Deployment` diagram type**
   - Containers mapped onto infrastructure nodes
   - Nodes nested to match infrastructure hierarchy (region → cluster → pod)
   - Container instances placed on nodes with counts
   - Environment named in the title
   - Unverified elements visibly labeled as assumptions
   - Requires Step 2 to have resolved infrastructure topology

For a migration, produce AS-IS and TO-BE as **separate files** with the state in
the title. Use the same diagram type for each state: `C4Container` for both
container-as-is and container-to-be. Do not overlay them; a diagram showing both
current and future state reliably confuses every audience it meets.

**Common mistake to avoid:** Using `C4Container` for all diagrams, or using
`C4Context` macro elements (Person, System) in a `C4Container` diagram. Each level
uses its own macro set, and mixing them produces identical-looking outputs.

Every relationship label is a verb phrase reading from source to target, with the
technology on it: "Reads crew availability from, via HTTPS/JSON" — not "connects
to." An unlabeled arrow tells a reviewer nothing they could not have guessed.

## Step 5 — Validate

Three passes, in this order.

**Grounding audit.** Walk the evidence ledger. Every element and relationship
either cites a path or is marked as an assumption. Anything that survives without
either gets deleted — including elements that are almost certainly present. That
is the whole discipline of this skill.

**C4 checklists.** Run the per-level checklists in
`references/c4-and-mermaid.md`: scope statement present, no mixed abstraction
levels, technology on containers and components, verb-phrase relationships,
correct boundary type, consistent naming with the repo's own vocabulary.

**Mechanical validation — the command depends on the path.**

*LikeC4:* this is the notation's main advantage over hand-written files, so use it.

```bash
npx likec4 validate          # syntax errors and layout drift; non-zero exit on failure
npx likec4 format --check    # optional, CI-friendly
```

It catches broken references, which is precisely what Mermaid cannot: a typo'd
alias there renders as a new empty box and looks correct. Neither command needs a
browser, so both work in restricted sandboxes.

*Mermaid:* run the bundled linter, which checks what a renderer cannot — whether
the diagram obeys the C4 model:

```bash
python3 scripts/lint_c4.py docs/architecture/*.mmd
# --strict promotes missing relationship protocols from warning to error
```

It catches missing titles, containers without a technology, vague relationship
labels ("uses", "connects to"), arrows pointing at undeclared aliases, orphaned
elements, a container diagram with no boundary, technology leaking into an L1
Context diagram, and a deployment diagram with no nodes. Fix every ERROR. Treat
each WARN as a question to answer rather than noise to clear — an orphaned element
usually means a missing arrow or an element that does not belong.

**Actually attempt a render before claiming a diagram is correct — do not assume
it is blocked.** `lint_c4.py` (or a manual read-through when Python is absent)
checks C4 *convention*; only a real render checks Mermaid *grammar*, and the two
diverge in ways a careful read cannot catch: a `Deployment_Node` with an empty
`{ }` body, or a `Rel()` pointed at a boundary alias instead of a leaf element,
both read as fine, both have balanced braces, and both are hard parser/renderer
failures (see `references/c4-and-mermaid.md`). `npx --yes @mermaid-js/mermaid-cli`
downloads and runs Chromium on demand and has been observed to work in sandboxes
with no prior Node/browser setup — it is worth trying even when you expect it to
fail, and its absence is a fact to establish by attempting it, not to assume from
missing tooling elsewhere (e.g. no Python does not imply no Chromium/npx).

```bash
npx likec4 serve                                   # LikeC4: interactive preview on :5173
npx likec4 export png -o ./assets                  # LikeC4: needs Playwright
npx --yes @mermaid-js/mermaid-cli -i docs/architecture/container-diagram.mmd -o /tmp/check.svg   # Mermaid
```

If the attempt genuinely fails (network policy, no browser available at all),
**say the diagrams were validated but not rendered.** Those are different claims,
and asserting the stronger one is exactly the unfounded confidence this skill
exists to prevent. Offer the source for a live editor instead, or `likec4 serve`
for the user to run locally. But reach that fallback by trying first, not by
assuming.

## Step 6 — Save and hand off

Write to `docs/architecture/` in the target repo.

*LikeC4* — split by concern, since all sources merge into one model anyway:

```
docs/architecture/
├── specs.c4         # element and deployment node kinds
├── model.c4         # elements, hierarchy, relationships
├── deployment.c4    # nodes and instanceOf bindings
└── views.c4         # one view per C4 level
```

*Mermaid* — one file per diagram:

```
docs/architecture/
├── context-diagram.mmd
├── container-diagram.mmd
├── component-diagram-<container-name>.mmd
├── code-diagram-<component-name>.mmd        (rare)
└── deployment-diagram-<environment>.mmd
```

For a migration, suffix the state: `container-diagram-as-is.mmd` and
`container-diagram-to-be.mmd`, or on LikeC4 a pair of views with the state in each
title.

If Mermaid is wanted for a README or wiki while the model lives in LikeC4,
**generate it rather than hand-writing it** — `likec4 gen mmd -o docs/architecture/mermaid/`
keeps the model as the single source of truth. Note in the repo that those files
are build output, so nobody hand-edits them. Two caveats worth stating to the user:
the generated output is flowchart syntax rather than C4 macros (so the bundled
linter does not apply to it), and it drops element technology and descriptions. When
technology must be visible in Mermaid specifically, hand-write that one diagram.

Alongside the files, report in chat: what each diagram covers, **every drift found
between `architecture.md` and the code**, the assumption list, and the questions
still open. The prose findings are frequently more valuable than the diagrams,
and they are the part a reviewer will actually act on.

Then name the next step rather than doing it unasked: refresh the Context Pack so
`architecture.md` references these diagrams; run delta analysis after the next
significant change; `adr-writer` if the work surfaced an undocumented decision
worth recording. Offer PNG rendering or a Confluence page only if asked — and
never commit, push, or open a PR without explicit confirmation.

## Hard rules

1. Always read the docs folder before generating, and check `docs/architecture/`
   for diagrams to update rather than duplicate.
2. Every element and relationship traces to a file you read, or is explicitly
   marked as an assumption. No exceptions, however obvious the element seems.
3. Never invent infrastructure, external systems, or deployment topology. Absent
   IaC is a question, not a blank to fill.
4. Never mix abstraction levels within one diagram.
5. Never generate Level 4 by default — it must be asked for and justified.
6. Report drift between `architecture.md` and the code; never quietly diagram one
   and imply the other.
7. Never overwrite existing diagrams without showing what changed first.
8. Never claim a diagram renders unless it was actually rendered — linted and
   rendered are different claims.
9. Use the repository's own vocabulary for element names.
10. **Use the correct Mermaid diagram type for each level: `C4Context` for L1,
    `C4Container` for L2, `C4Component` for L3, `classDiagram` for L4,
    `C4Deployment` for deployment.** Using the wrong type will produce identical-
    looking diagrams. This is the most common bug in this skill.
11. Recommend LikeC4 once when nothing is established, then honor the answer. Never
    re-pitch it, and never treat the Mermaid path as second-class.
12. Never install a dependency, add a package, or modify `package.json` without
    explicit consent. Recommending a tool is not installing one.
13. Never commit or push without explicit confirmation.

## Bundled files

- `scripts/lint_c4.py` — C4 convention linter. No dependencies, no network, no
  browser. Run it on every generated diagram in Step 5 (Mermaid path).
- `references/likec4.md` — LikeC4 DSL (`specification`, `model`, `views`,
  `deployment`), CLI commands, and the C4-level-to-view mapping. Read before
  writing `.c4`.
- `references/c4-and-mermaid.md` — C4 level definitions, per-level checklists,
  Mermaid C4 macro reference, layout pitfalls, Level 4 handling. Read before
  writing `.mmd`.
- `references/evidence-sources.md` — where each level's truth lives in a
  repository, by ecosystem and by artifact type.
