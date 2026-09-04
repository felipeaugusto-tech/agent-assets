# The Packaging Plan — Corpus to Plugin

**How the whole GenDD workflow becomes one Claude Code plugin, assembled from this repo's corpus, without moving or rewriting any of it.**

| Field | Value |
|-------|-------|
| **Audience** | Anyone deciding or executing the packaging work |
| **Prerequisites** | Claude Code installed; [1-plugin-overview.md](1-plugin-overview.md) read |
| **Reading time** | ~15 minutes |
| **Related** | [4-skill-packaging.md](4-skill-packaging.md) — live status and next actions · [2-distribution-guide.md](2-distribution-guide.md) — how it reaches people |

## How to read the source markers

| Marker | Meaning |
|--------|---------|
| **[docs]** | Stated in official Anthropic documentation |
| **[undocumented]** | Genuinely absent from the docs — not merely unfound |
| **[verified]** | Observed in this repository, with the command that showed it |

Four rules hold throughout, and everything below follows from them:

1. **Nothing outside `claude-plugin-poc/` is moved or rewritten.** Not the corpus, not `marketplace.json`, not `plugin.json`.
2. **Every skill keeps the name it already has.** `adr-writer`, not `write-adr`.
3. **One namespace.** Everything is `/gendd:<name>`; `/gendd:enhance-requirements` keeps working unchanged.
4. **Copies are generated, never typed.**

---

## Table of Contents

- [The finding that shapes everything](#the-finding-that-shapes-everything)
- [Why one plugin, not one per occupation](#why-one-plugin-not-one-per-occupation)
- [The structure](#the-structure)
- [How the copying stays honest](#how-the-copying-stays-honest)
- [The thirty-four skills](#the-thirty-four-skills)
- [Sequence](#sequence)
- [What is deliberately absent](#what-is-deliberately-absent)
- [Related Resources](#related-resources)

---

## The finding that shapes everything

**A plugin cannot read a file outside its own root.** There is no documented way for a skill to reach `../../gendd-analysis/`. **[undocumented]**

The variables a plugin gets are `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}` and `${CLAUDE_PROJECT_DIR}`; none reaches a sibling directory in the marketplace repo. **[docs]** Traversal out of the plugin root is undocumented, symlink survival after install is undocumented, and the `git-subdir` source type — the one built for monorepos — **sparse-clones only the plugin's own subdirectory**, so on that path the rest of the repo provably is not there. **[docs]**

So the corpus content each skill needs has to be physically inside the plugin. This POC already reached that conclusion and solved it by copying three files byte-for-byte, verified with `cmp`. That was right, and it produced the exact problem worth designing out: `enhance-requirements` now exists in four places and the copies do not follow an edit to the source. Thirty-four skills means roughly seventy copied files with the same failure mode.

**So: keep the copying, and add a check.** The corpus stays the single source of truth and is never touched; `references/` becomes generated output; and one command proves the output still matches. Byte-fidelity, no drift, nothing maintained twice.

## Why one plugin, not one per occupation

An earlier version of this plan proposed five plugins split by occupation — `gendd-product`, `gendd-engineering`, `gendd-qa` and so on. It was wrong, for three reasons.

**The main argument for splitting is not available.** Server-managed settings apply org-wide and uniformly — per-group configuration is not supported. **[docs]** So `gendd-engineering` could never have been enabled for engineers and `gendd-qa` for QA through the channel actually in use. Splitting would only have bought opt-in through project-level `.claude/settings.json`, which is a far smaller benefit.

**The corpus argues against partitioning.** `gendd-analysis/playbooks/on-demand/_index.md` lists target roles per playbook, and nearly every one crosses occupations: `create-context-pack` is Architect + Tech Lead + Backend + Frontend + Fullstack; `enhance-requirements` is PO + BA + QA Engineer; `generate-unit-tests` is three dev roles plus QA Automation. Per-occupation plugins would force an arbitrary home for each, and a frontend dev needing `validate-acceptance-criteria` would have to install the QA plugin to get it.

**One plugin means zero edits and zero retraining.** The marketplace entry already points at `./claude-plugin-poc`, so `marketplace.json` needs no change and `enabledPlugins` stays as it is. **[verified]** And because namespacing is by plugin name, `/gendd:enhance-requirements` remains exactly what people already type. The five-plugin plan required renaming the one command currently in the field.

### What is given up

| Cost | Assessment |
|------|------------|
| **Independent release cadence** | One plugin, one version — a QA skill and a PO skill ship together. This is the real argument for splitting later, and the signal to watch for: the first time you want to hold one area back while shipping another. |
| **~2,000 tokens of standing cost** | Every skill's name and description loads at session start. At the ~59 tokens projected for a manual-only skill, thirty-four skills is roughly 2,000 tokens in every session, including for a PO who will never call `generate-unit-tests`. **Measure it with `scripts/benchmark-plugin.sh` before treating it as a problem** — see [3-token-benchmarks.md](3-token-benchmarks.md). |
| **A longer `/` menu** | Thirty-four entries under one namespace. Tolerable. |

### One carve-out

**Keep the TestRail MCP server out of this plugin.** MCP tool schemas are always-on for anyone who has the plugin, unlike references which cost nothing until invoked. Bundling it taxes every PO and architect with tool definitions they will never call. Configure it per project, or make it the one small second plugin, enabled only where QA works.

## The structure

```
agent-assets/                                 ← source of truth · read-only to the sync script
├── .claude-plugin/marketplace.json           NO EDIT — already points at ./claude-plugin-poc
├── gendd-analysis/                           14 workflows · 24 playbooks · 5 pass agents · 20 templates
├── sdlc/  governance/  templates/            96 standards · guardrails source · doc skeletons
├── code-and-test-templates/                  Java + Angular codegen and test-gen prompts
├── rules-manifest.yaml                       32 KB glob → rule router
├── scripts/                                  benchmark-plugin.sh · lint-standards.sh
│
└── claude-plugin-poc/                        ← the gendd plugin root
    ├── .claude-plugin/plugin.json            NO EDIT — name: gendd, sets the /gendd: namespace
    ├── 1-  2-  3-  4-  5-  README            the reasoning, the status, this plan
    ├── sync_references.py                    the map and the check, in one file
    ├── skills/                               HAND-WRITTEN, in place — the script never touches this
    │   ├── enhance-requirements/SKILL.md
    │   └── run-brownfield-analysis/SKILL.md
    └── references/                           GENERATED — do not hand-edit
        ├── enhance-requirements/             3 files
        └── run-brownfield-analysis/          7 files, 92 KB
```

Three zones, and the boundary between them is the design:

| Zone | Rule |
|------|------|
| **The corpus** | Read, never written. An edit here is the only way methodology changes. |
| **`skills/`** | Hand-written, in place. A `SKILL.md` is never derived from anything, so it does not belong in a pipeline. It says what the steps are and which references to load; it never restates the method. |
| **`references/`** | Generated, but committed anyway — installation is a git clone with no build hook. Treat a hand edit here the way you would treat editing `node_modules`. |

## How the copying stays honest

One file: `sync_references.py`. Run `--help` for its own explanation. Python rather than shell, because the engineers are on Windows and this repo already depends on Python — the TestRail MCP server, `lint_c4.py`, `scan_pipeline.py` and `qa-orchestrator.py` are all Python. It runs unchanged in PowerShell, Git Bash, macOS and Linux, with no `chmod` and no CRLF trap. **[verified]**

**Why a map is irreducible.** You cannot infer which corpus file a reference came from. `create-context-pack.md` exists in **both** `workflows/` and `playbooks/on-demand/` — as do `generate-ide-rules.md`, `generate-unit-tests.md`, `identify-test-gaps.md` and `generate-architecture-diagrams.md`. Five deliberate basename collisions, because the workflow/playbook pairing is the corpus's own design. **[verified]** A generic "find the file with the same name and diff it" check would silently compare against the wrong source for exactly the capabilities most likely to be packaged.

**Why there is no separate map file.** An `assembly.yaml` read by a build script needs a parser to describe something whose entire content is "copy this file there." As a `REFS` list inside the script, the map *is* the code — reviewable as a diff, greppable, and with nothing between the declaration and the action.

**Why there is no lockfile.** Because the corpus and the plugin live in the same repository, verification needs no hashes — `--check` rebuilds into a temp directory and diffs. One mechanism, both failure modes:

- **A corpus file changed and nobody re-synced.** The temp build differs from the committed copies, so the plugin is shipping stale text. This is the failure that already happened.
- **Someone hand-edited a generated file.** Same diff, opposite direction — worth catching, because the next sync would silently wipe their change.

Wire `--check` into CI beside `lint-standards.sh`, with `claude plugin validate --strict` in the same job.

**Adding a skill** is a new `skills/<name>/SKILL.md` plus two or three `REFS` entries. That is the whole authoring loop.

## The thirty-four skills

Grouping is editorial — they all live in one plugin and all answer to `/gendd:`. Names are kept, never reinvented: the existing `.skill` name wins, then the corpus playbook filename, and a new name is coined only for the five capabilities that have none.

| Lineage | Meaning |
|---------|---------|
| **CORPUS** | Wrap a `gendd-analysis/` document. No authoring — the highest-return work. |
| **IMPORT** | Bring in an existing `.skill` package from the `Claude Skills/` folder. |
| **AUTHOR** | Write from nothing. Five of these. |
| **DONE** | On disk in this repo. |

### Phase 1 · Plan & Requirements

| Skill | Lineage | Built from | Step |
|-------|---------|-----------|------|
| `enhance-requirements` | **DONE** | Shipping since v0.1.0 | 04 |
| `prd-writer` | IMPORT | `prd-writer.skill` (4 reference docs incl. interview questions) + `sdlc/product/product-requirements-doc.md` | 01 |
| `stories-from-source` | IMPORT | `stories-from-source_v2.skill` — retire the non-`_v2` copy first | 01 |
| `jira-story-estimator` | IMPORT | `jira-story-estimator.skill` + `sdlc/product/definition-of-ready.md` | 08 |
| `audit-ui-patterns` | CORPUS | `playbooks/on-demand/audit-ui-patterns.md` | 02 |

### Phase 2 · Design & Architecture

**Note:** `create-context-pack` is **not** on this list. `workflows/create-context-pack.md` is marked DEPRECATED in its own header, superseded by the Analyze & Generate flow. It was very nearly packaged as skill #2.

| Skill | Lineage | Built from | Step |
|-------|---------|-----------|------|
| `run-brownfield-analysis` | **DONE** | `playbooks/onboarding/run-brownfield-analysis.md` + `workflows/brownfield-repository-analysis.md` + `templates/documentation-guidelines.md` + the four pass agents. Untested against a real repo. | 03 |
| `generate-context-areas` | CORPUS | `workflows/generate-context-areas.md` + `templates/context-area.md` + the 16 `knowledge/sdlc-areas/*`. Phase 3 — needs brownfield output. | 03 |
| `detect-and-generate-standards` | CORPUS | `workflows/detect-and-generate-standards.md` + `templates/standards/*`. Phase 4. | 03 · 11 |
| `analyze-and-generate` | CORPUS | `workflows/analyze-and-generate.md` — the corpus's own master entry point, five phases with human gates. **Package last**, once its phases exist as skills. | 03 |
| `greenfield-analysis` | CORPUS | `workflows/greenfield-analysis.md` — 4 KB against brownfield's 18, so expect to write into it | 03 |
| `adr-writer` | IMPORT | `adr-writer.skill` (ships its own `adr-template.md`) + `sdlc/architecture/decision-records.md` | 06 · 10 |
| `architecture-diagram-generator` | IMPORT | Two lineages: the `.skill` ships `lint_c4.py` and LikeC4 references; the corpus ships `workflows/generate-architecture-diagrams.md`. Pick one. | 06 |
| `run-delta-analysis` | CORPUS | `playbooks/on-demand/run-delta-analysis.md` | 20 |

### Phase 3 · Build

Three of the five real gaps live here.

| Skill | Lineage | Built from | Step |
|-------|---------|-----------|------|
| `implementation-plan` | AUTHOR | **Nothing exists.** Write it first — step 14 is defined as reviewing against this artifact, so its absence breaks two steps. | 09 |
| `spec-authoring` | AUTHOR | **The "how" half.** `adr-writer` covers what and why; nothing covers files, tasks and spike results. | 10 |
| `spike-doc` | AUTHOR | **Nothing exists.** Nearest shape is `templates/tech-debt-template.md`. | 12 |
| `generate-ide-rules` | CORPUS | `workflows/generate-ide-rules.md` + all five `templates/ide-rules/*` + `knowledge/ide-formats/*`. Also the generator for `.claude/rules/*.md`. | 11 |
| `generate-unit-tests` | CORPUS | `workflows/generate-unit-tests.md` + `code-and-test-templates/test/java-` and `angular-unit-test-generation.md` | 11 · 17 |
| `generate-standards` | CORPUS | `playbooks/on-demand/generate-standards.md` + `templates/standards/*` | 11 |
| `analyze-database-schema` | CORPUS | `playbooks/on-demand/analyze-database-schema.md` + `sdlc/database/**` | 11 |

### Phase 4 · Code Review & Merge

| Skill | Lineage | Built from | Step |
|-------|---------|-----------|------|
| `pr-pre-review` | AUTHOR | **New name, nothing to import.** The standards exist — `sdlc/version-control/code-review.md`, `github/pull-requests.md`, `rules-manifest.yaml` to route the diff — but no automation is wired to them. Also the skill the GitHub Action calls. | 13 |

### Phase 5 · Test & QA

| Skill | Lineage | Built from | Step |
|-------|---------|-----------|------|
| `test-gap-analyzer` | IMPORT | The `.skill` ships `scripts/` and `references/`, so it wins over `workflows/identify-test-gaps.md` | 16 |
| `review-test-coverage` | CORPUS | `playbooks/recurring/review-test-coverage.md` + `sdlc/quality-assurance/coverage.md` | 16 |
| `qa-test-case-writer` | IMPORT | `qa-test-case-writer` (21 KB SKILL.md + Context.md) + `workflows/generate-tests-from-gherkin.md` | 17 |
| `test-automation-implementer` | IMPORT | `test-automation-implementer` + `workflows/automate-integration-testing.md` + the 7 stack testing guides | 17 |
| `testrail-publisher` | IMPORT | `testrail-publisher`. The MCP server goes in a **separate** plugin, and the live `.env` must not travel. | 17 |
| `validate-acceptance-criteria` | CORPUS | `playbooks/on-demand/validate-acceptance-criteria.md` — drives Playwright MCP | 18 |
| `run-assisted-testing` | CORPUS | `playbooks/on-demand/run-assisted-testing.md` | 18 |

### Phase 6 · Release & Deploy

| Skill | Lineage | Built from | Step |
|-------|---------|-----------|------|
| `release-evidence-packet` | IMPORT | `release-evidence-packet.skill` (ships `verify_evidence.py`) + `gendd-analysis/templates/validation-packet.md` | 19 |
| `incremental-doc-update` | CORPUS | `workflows/incremental-doc-update.md` + `playbooks/recurring/refresh-context-pack.md` + `refresh-context-areas.md`. The skill the CI Action calls. | 20 |
| `cicd-pipeline-audit` | IMPORT | `cicd-pipeline-audit.skill` (ships `scan_pipeline.py` + the OWASP CI/CD checklist) + `playbooks/on-demand/audit-ci-cd-pipeline.md` | 22 |
| `audit-observability` | CORPUS | `playbooks/on-demand/audit-observability.md` + `sdlc/observability/**` | 22 |
| `generate-support-documentation` | CORPUS | `playbooks/on-demand/generate-support-documentation.md` | 22 |

### Cross-cutting

| Skill | Lineage | Built from | Step |
|-------|---------|-----------|------|
| `lookup-standard` | AUTHOR | New name. A thin skill over `rules-manifest.yaml` that resolves a rule ID or file glob and loads **only** the matching standard. Carries all 96 `sdlc/**` files — which cost nothing until invoked. | all |
| `compile-rules` | AUTHOR | New name. Turns `rules-manifest.yaml` into `.claude/rules/*.md` with `paths:` frontmatter for a target repo. The standards already carry `applies_to: ["**/*"]`, so this is largely a field rename. | 11 |

## Sequence

### Phase 0 — verify, build nothing · **complete**

No script, no directory, no move. Confirm the three `enhance-requirements` copies still match their corpus sources, so that every later phase has a known-good baseline to diff against.

**Result: all three are byte-identical.** **[verified]** Had one differed, the finding would have been that the corpus had already moved on without the plugin.

### Phase 1 — package what is already written · **in progress**

The six steps whose method exists in full and cannot be invoked: **02, 03, 05, 11, 18, 20**. Wrappers only, no authoring — the highest return in the plan.

Order: `run-brownfield-analysis` → `generate-context-areas` → `incremental-doc-update` → `generate-ide-rules` → the rest. Context in, context maintained, then everything else.

Run `scripts/benchmark-plugin.sh` at two skills and again at eight. Two data points give the real per-skill standing cost, which is the number that decides whether one plugin holds at thirty-four.

Publish when the first three produce output a Tech Lead accepts — one commit and a push, since `autoUpdate` is already on.

### Phase 2 — fold in the `.skill` packages

Nine `.skill` packages plus the QA toolset come from a different lineage than the corpus, and six capabilities are covered by both. **Decide the canonical lineage per capability first**, or you ship two answers to the same question in one namespace.

Rule of thumb: where a `.skill` ships working scripts — `test-gap-analyzer`, `cicd-pipeline-audit`, `release-evidence-packet`, `architecture-diagram-generator` — it wins. Where it is prose duplicating a workflow, the corpus wins.

Housekeeping that must land here: the duplicate `requirements-enhancer` packages, the `stories-from-source` / `_v2` pair, the stray `jira-story-estimator 1.skill` filename, and the live `.env` in the TestRail MCP folder.

### Phase 3 — author the five gaps

`implementation-plan`, `spec-authoring`, `spike-doc`, `pr-pre-review`, and the `lookup-standard` / `compile-rules` pair.

This is the one phase that **should** add to `gendd-analysis/`: new methodology belongs in the corpus as a workflow, with the skill as its wrapper. Write it straight into the plugin and the source of truth develops a hole.

Start with `implementation-plan` — it unblocks step 14, which is defined as judging a PR against the implementation plan.

### Phase 4 — the Desktop build

Product, design and QA people reach skills through the chat console at `admin-settings/plugins`, which does **not** reach Claude Code. **[verified]** Two consoles, two packages — see [2-distribution-guide.md](2-distribution-guide.md).

Same references, a second output target, and one field flipped: `disable-model-invocation` is right for an engineer typing a command and wrong for chat, where the description is what makes a skill trigger. **This is the first thing that genuinely needs more than a copy script**, so a source-for-bodies earns its place here and not before.

### Later — split, only on a signal

Two signals, both measurable rather than felt: the benchmarked standing cost of the skill descriptions becomes material, or you want to hold one area's release back while shipping another. Until one of those happens, one plugin is the simpler system.

Splitting later is cheap on the build side and expensive on the human side, because the namespace changes. Use the marketplace entry's `renames` field to carry identity across when the day comes.

## What is deliberately absent

| Absent | Why |
|--------|-----|
| **`assembly.yaml`** | The `REFS` list is the map. No parser needed, and the declaration sits next to the code that acts on it. |
| **A lockfile or provenance file** | Corpus and plugin share a repo, so `--check` rebuilds and diffs. Reading the script is the trace. |
| **A `build/` directory** | One file does not need a directory. |
| **An authoring zone for skill bodies** | A `SKILL.md` is never derived. Needed only when the Desktop build requires different frontmatter — phase 4. |
| **`agents/`** | The pass files have no frontmatter — they are prompts, not Claude Code subagents. **[verified]** They ride as references. Revisit only if the context window becomes the binding constraint on a real repo. |
| **Guardrails** | A plugin's `settings.json` honours only `agent` and `subagentStatusLine`. **[docs]** A permission deny-list cannot ship in a plugin at all; it belongs in managed settings, outside this repo. |
| **Six plugins** | See above. Revisit on a signal, not on a schedule. |

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Live status and next actions | [4-skill-packaging.md](4-skill-packaging.md) | What is on disk, how to run it, open items, corpus bugs |
| Plugin anatomy and invocation control | [1-plugin-overview.md](1-plugin-overview.md) | What a plugin is, and the `disable-model-invocation` decision |
| Distribution | [2-distribution-guide.md](2-distribution-guide.md) | The two admin consoles, and which one reaches Claude Code |
| Measured cost | [3-token-benchmarks.md](3-token-benchmarks.md) | 0 tokens idle, +45,450 when invoked |
| The sync script | `sync_references.py` | Run `--help`. Python 3.8+, stdlib only. |
| Official: plugins reference | https://code.claude.com/docs/en/plugins-reference | plugin.json schema, component paths, settings.json keys |
| Official: plugin marketplaces | https://code.claude.com/docs/en/plugin-marketplaces | Nested sources, `git-subdir`, `renames` |
| Official: server-managed settings | https://code.claude.com/docs/en/server-managed-settings | Org-wide, no per-group scoping; the `claudeMd` key |
| Official: memory and CLAUDE.md | https://code.claude.com/docs/en/memory | Precedence, `.claude/rules` and `paths:`, `@path` imports |

---

*This is tooling documentation, not a standard. It carries no standards frontmatter and is intentionally not registered in `rules-manifest.yaml` — consistent with the other documents in this folder.*
