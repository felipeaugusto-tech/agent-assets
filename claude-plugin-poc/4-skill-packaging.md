# Packaging the Corpus as Skills — Status and Next Steps

**The plugin is growing from one skill to the whole GenDD workflow; this document is the handoff, written so a fresh session can resume with no chat history.**

| Field | Value |
|-------|-------|
| **Audience** | Anyone continuing the packaging work — human or agent |
| **Prerequisites** | This repo cloned; Claude Code installed |
| **Reading time** | ~7 minutes |
| **Related** | [1-plugin-overview.md](1-plugin-overview.md) · [2-distribution-guide.md](2-distribution-guide.md) · [3-token-benchmarks.md](3-token-benchmarks.md) · [../GenDD-Plugin-Blueprint.html](../GenDD-Plugin-Blueprint.html) — approved v2 architecture, full 34-skill sequencing |

## How to read the status markers

| Marker | Meaning |
|--------|---------|
| **[done]** | On disk and verified in this repo |
| **[next]** | The immediate next action |
| **[open]** | Decided but not started, or genuinely undecided |

---

## Table of Contents

- [Where things stand](#where-things-stand)
- [Start here](#start-here)
- [The architecture, in four sentences](#the-architecture-in-four-sentences)
- [What is on disk](#what-is-on-disk)
- [Testing run-brownfield-analysis](#testing-run-brownfield-analysis)
- [Adding skill #3](#adding-skill-3)
- [Decisions already made](#decisions-already-made)
- [Open items](#open-items)
- [Corpus problems found, not fixed](#corpus-problems-found-not-fixed)

---

## Where things stand

**[done]** Phase 0 — verified that the three `enhance-requirements` reference files are still byte-identical to their corpus sources. They are. That baseline is what everything else diffs against.

**[done]** `sync_references.py` — the copy map and the staleness check, in one file. Python rather than shell so it runs identically in PowerShell, Git Bash, macOS and Linux, with no line-ending trap and no `chmod`.

**[done]** Skill #2 — `run-brownfield-analysis`, authored but **not yet run against a real repository**.

**[done]** Skill #3 — `adr-writer`, vendored from `Claude Skills/Architecture/adr-writer.skill` into `vendor/adr-writer.skill`, unpacked by `sync_references.py`'s `VENDORED` map. **Smoke-tested**: `claude --plugin-dir ./claude-plugin-poc -p "/gendd:adr-writer ..."` loaded the skill, correctly resolved its package-relative `references/adr-template.md` path (vendored `.skill` bodies use relative paths, not `${CLAUDE_PLUGIN_ROOT}` — confirmed, not just assumed), produced a correct Nygard-format draft, and stopped at its approval gate without writing a file. This proves the vendor-import mechanic for the other twelve `.skill` packages.

**[done]** **Phase 1 is complete — all 18 corpus-wrapped skills are packaged.** 21 skills live in total: `enhance-requirements`, `run-brownfield-analysis`, `adr-writer`, `generate-context-areas`, `detect-and-generate-standards`, `generate-ide-rules`, `greenfield-analysis`, `run-delta-analysis`, `incremental-doc-update`, `audit-ui-patterns`, `analyze-and-generate`, `validate-acceptance-criteria`, `run-assisted-testing`, `review-test-coverage`, `generate-standards`, `analyze-database-schema`, `generate-unit-tests`, `audit-observability`, `generate-support-documentation`, `lookup-standard`, `compile-rules`. 189 total generated files (86 flat corpus refs + 103 mirrored tree files + 2 vendored), `--check` clean, `claude plugin validate --strict` clean.

**`sync_references.py` grew a third map, `TREES`**, alongside `REFS` and `VENDORED`: whole corpus subtrees (`sdlc/`, `governance/`) mirrored path-for-path into `references/lookup-standard/{sdlc,governance}/...`, needed because `lookup-standard` must resolve `rules-manifest.yaml`'s own `file:` paths verbatim, and a flat copy would collide on repeated basenames (`README.md` appears in nearly every `sdlc/` subdirectory). `compile-rules` reuses that same mirrored tree via `${CLAUDE_PLUGIN_ROOT}/references/lookup-standard/...` rather than duplicating 103 files under its own skill folder.

**Smoke-tested:** `generate-ide-rules` (dry-run, scratch repo — correctly used its one real source doc, refused to fabricate sections/commands, flagged a planted inconsistency); `lookup-standard` (resolved `ARC-001` from a plain-English question, loaded the mirrored `sdlc/architecture/decision-records.md`, and — after one fix — correctly declined to fabricate a resolved path for a cross-reference to `templates/adr-template.md`, which lives outside the mirrored tree). The rest are wired and validated but not yet exercised against real brownfield output.

**[done]** **Phase 2 is complete — all 11 remaining `.skill` packages are vendored.** `prd-writer`, `stories-from-source` (the `_v2` archive only — the non-`_v2` one is retired), `jira-story-estimator` (renamed from the stray `jira-story-estimator 1.skill`), `architecture-diagram-generator`, `release-evidence-packet`, `cicd-pipeline-audit` (all four win over their corpus-workflow equivalents per the "ships a working script" rule), and — re-zipped from the QA toolset's unzipped skill folders — `test-gap-analyzer`, `qa-test-case-writer`, `test-automation-implementer`, `testrail-publisher` (the TestRail **MCP server itself** stays out of this plugin, per the carve-out). 32 skills live in total now. `--check` and `claude plugin validate --strict` both clean; 31 vendored files across 11 packages, none needed corpus supplements — every one ships its own bundled references/scripts.

**Smoke-tested:** `test-gap-analyzer` (the one package I re-zipped myself, highest risk of a path mistake) — correctly analyzed a throwaway 1-file repo, stated every limitation explicitly (no git history, no coverage tooling) rather than glossing over them, and correctly deferred writing tests since that wasn't asked.

**Housekeeping — mostly done, one item doesn't apply as originally scoped:**
- ✅ `stories-from-source` / `_v2` collision resolved — only `_v2` is vendored.
- ✅ `jira-story-estimator 1.skill` stray filename resolved — vendored as `jira-story-estimator.skill`.
- ✅ `acceptance-criteria-enhancer.skill` / `requirements-enhancer.skill` collision — neither is vendored (superseded by the corpus's own `enhance-requirements`), so the collision can't reach this plugin.
- ⚠️ **The TestRail `.env` is not inside any git repository at all** — `QA/GenDD-QA-Toolset/` lives under a plain OneDrive-synced folder (`docs/OneDrive_2026-09-01/Claude Skills/`), not a git working tree. A `.gitignore` entry has nothing to attach to. The real exposure, if any, is that OneDrive syncs the populated `.env` to the cloud — worth someone checking sync scope/sharing settings on that folder, but that's outside what this plugin-packaging work can fix.

**[done]** **Phase 3 is complete — all 4 methodology gaps are authored.** `implementation-plan`, `spec-authoring`, `spike-doc`, `pr-pre-review` all now have a corpus workflow + template in `gendd-analysis/` (new methodology, written into the corpus first per the plan's own rule — not authored straight into the plugin) plus a thin `SKILL.md` wrapper. **35 skills live in total** — every skill named in `GenDD-Plugin-Blueprint.html` §06 now exists. `--check` and `claude plugin validate --strict` both clean; 95 flat corpus refs + 103 mirrored tree files + 31 vendored files.

New corpus files: `gendd-analysis/workflows/{implementation-plan,spec-authoring,spike-doc,pr-pre-review}.md` and `gendd-analysis/templates/{implementation-plan-template,spec-template,spike-template,pr-pre-review-template}.md`. `pr-pre-review` reuses `lookup-standard`'s mirrored `sdlc`/`governance` tree rather than duplicating 103 files under its own skill folder — same pattern `compile-rules` already used.

**Smoke-tested:** `implementation-plan`, in a throwaway scratch Express repo with only one existing route file and no `package.json` or entry point. It correctly refused to silently invent a working app around the gap — every missing piece (no Express dependency declared, no app entry point, no test framework) was named as an explicit, flagged assumption rather than quietly assumed away, and the resulting plan's file-level tasks, sequencing, and risks were all concrete and verifiable.

**[next]** Run `run-brownfield-analysis` on one real mid-size Accurate service, then chain `generate-context-areas` → `detect-and-generate-standards` → `generate-ide-rules` on its actual output as the first true end-to-end test against real (not scratch) code. Everything in the plugin build is done except Phase 4 (the Desktop build — a second output target with `disable-model-invocation` removed, deliberately deferred until a non-engineering user actually needs it). Nothing in this session has been committed yet.

---

## Start here

Works the same in PowerShell, Git Bash, cmd, or a terminal on macOS or Linux.

```
cd agent-assets

# 1. copy the 7 new reference files for run-brownfield-analysis
python claude-plugin-poc/sync_references.py

# 2. confirm the plugin matches the corpus  ->  "in sync -- 10 reference file(s)"
python claude-plugin-poc/sync_references.py --check

# 3. confirm the plugin itself is well-formed
claude plugin validate ./claude-plugin-poc --strict

# 4. load it without publishing anything
claude --plugin-dir ./claude-plugin-poc
```

Then `/gendd:run-brownfield-analysis` inside that session. After editing a `SKILL.md`, `/reload-plugins` picks it up without restarting.

If `python` is not on your PATH, try `py` on Windows or `python3` elsewhere. Python 3.8+, standard library only — nothing to install.

## The architecture, in four sentences

A Claude Code plugin **cannot read files outside its own directory** — no documented way to reach `../../gendd-analysis/`, and the `git-subdir` source type sparse-clones only the plugin folder, so on that path the rest of the repo provably is not there. So every corpus document a skill needs is **copied** into `references/`, and copies go stale silently — which is how `enhance-requirements` ended up existing in four places.

`sync_references.py` is the fix: its `REFS` list is the record of where each copy came from, and `--check` rebuilds into a temp directory and diffs, so CI fails when the corpus moves without the plugin. `skills/` is hand-written and the script never touches it; `references/` is generated and should never be hand-edited.

## What is on disk

```
claude-plugin-poc/
├── .claude-plugin/plugin.json                    name: gendd  →  /gendd: namespace
├── sync_references.py                            the two maps + the check. Run --help.
├── vendor/adr-writer.skill                       SOURCE — .skill package, versioned in git
├── skills/
│   ├── enhance-requirements/SKILL.md             shipping since v0.1.0
│   ├── run-brownfield-analysis/SKILL.md          new, untested against a real repo
│   └── adr-writer/                               GENERATED from vendor/ — smoke-tested, works
└── references/                                   GENERATED — do not hand-edit
    ├── enhance-requirements/                     3 files
    └── run-brownfield-analysis/                  7 files, 92 KB
```

Nothing outside `claude-plugin-poc/` has been added, moved or edited. `marketplace.json` and `plugin.json` are untouched, so `gendd@hatchworks` keeps working exactly as it does today for everyone who has it.

## Testing run-brownfield-analysis

The machinery is proven; the open question is whether an 87-line skill body plus 92 KB of methodology produces a `docs/brownfield/` pack a Tech Lead would accept.

Pick a **mid-size Java service**, not the largest one — the point is to judge the output, not to stress the context window.

The skill is designed to stop at each pass. Judge them separately:

| Pass | Output | The question to ask |
|------|--------|---------------------|
| 1 · Scan | `pass1-scan-findings.md` | Did it find every service and module? Anything invented? |
| 2 · Infer | `pass2-infer-findings.md` | Is the architecture classification right? Is every claim marked FACT or HYPOTHESIS? |
| 3 · Validate | `pass3-validation-packet.md` | Would you actually send these questions to an SME, or are they filler? |
| 4 · Document | `docs/brownfield/gendd/` | Could a new engineer navigate the service from this alone? |

**Pass 3 is a hard stop by design.** It writes questions for a human and the skill will not answer them itself. If validation gets skipped, everything downstream inherits unconfirmed hypotheses — the skill says so and marks output INFERRED.

If the output is wrong, the fix is almost always the **skill body**, not the corpus. The corpus documents are byte-identical copies and changing them changes the source of truth for everyone.

## Adding skill #3

Three steps, no ceremony:

1. Write `skills/<name>/SKILL.md` by hand.
2. Add its entries to the `REFS` list in `sync_references.py`, under a commented heading.
3. Run the sync, then `--check`.

Follow the `run-brownfield-analysis` body as the pattern: fix the target, load references **at the point of use** rather than all up front, name the human gates, list hard limits at the end.

All 18 Phase 1 skills are done (see "Where things stand" above). What's next is Phase 2: fold in the remaining 11 `.skill` packages under `vendor/`, following the `adr-writer` pattern — see `GenDD-Plugin-Blueprint.html` §06–07 for the lineage decision per capability (a `.skill` that ships a working script wins over the equivalent corpus workflow; a prose-only one loses to it).

## Decisions already made

Recorded so they are not relitigated. Each has a reason, and each can be reopened if the reason stops holding.

| Decision | Why |
|----------|-----|
| **One plugin, not one per occupation** | Managed settings apply org-wide and uniformly — per-group enablement is not available, which was the main argument for splitting. And `playbooks/on-demand/_index.md` shows most capabilities are already multi-role. |
| **Keep existing skill names** | `adr-writer`, not `write-adr`. Existing `.skill` name wins, then the corpus playbook filename. New names only where none exists. |
| **`references/` is generated, `skills/` is not** | One boundary. It means a hand-written body is never at risk from the script, and no authoring directory is needed. |
| **No `assembly.yaml`, no lockfile** | The `REFS` list is the map, so no parser is needed at all; and with the corpus in the same repo, `--check` rebuilds and diffs instead of comparing hashes. |
| **No `agents/` directory** | The pass files have no frontmatter — they are prompts, not Claude Code subagents. They ride as references. Revisit only if the context window becomes the binding constraint on a real repo. |
| **Guardrails parked** | A plugin's `settings.json` honours only `agent` and `subagentStatusLine`, so a permission deny-list cannot ship in a plugin at all. It belongs in managed settings, outside this repo. |

## Open items

**[open] Test the clone behaviour.** Whether a relative-path `source` clones the whole marketplace repo or only the plugin directory is undocumented. If the whole repo lands on disk, `${CLAUDE_PLUGIN_ROOT}/../../` would remove the copying entirely. Install the plugin from the marketplace and list the cache directory — about fifteen minutes. Keep the sync script either way; undocumented behaviour can change.

**[open] Measure the standing cost.** Every skill's name and description loads at session start. `scripts/benchmark-plugin.sh` already exists — run it at two skills and again at eight, and the slope tells you the real per-skill cost. That number, not a feeling, is what decides whether one plugin holds at thirty-four.

**[open] Mark `references/` as generated.** A `.gitattributes` entry marking it `linguist-generated` collapses the diffs in review, and a line in the README stops the next contributor hand-editing a copy.

**[open] Wire `--check` into CI**, beside `lint-standards.sh`, with `claude plugin validate --strict` in the same job.

**[open] The Desktop package.** Product and QA people reach skills through the chat console at `admin-settings/plugins`, which does **not** reach Claude Code — two consoles, two packages. The same skills need a second build with `disable-model-invocation` removed, because in chat the description is what makes a skill trigger. This is the first thing that needs more than a copy script.

## Corpus problems found, not fixed

Deliberately left alone — the rule for this work is that nothing outside `claude-plugin-poc/` gets edited. Worth someone's decision.

1. **`workflows/create-context-pack.md` is DEPRECATED** in its own header, superseded by Generate Context Areas, Generate IDE Rules and Detect & Generate Standards, with Analyze & Generate as the master flow. `templates/context-pack.md` carries the same note. **It was very nearly packaged as skill #2** — the deprecation was only caught by reading the file.

2. **`playbooks/on-demand/create-context-pack.md` is not marked deprecated** and still instructs the reader to paste Cursor prompts at the deprecated workflow. The workflow registry moved on; the playbook registry did not.

3. **`playbooks/onboarding/run-brownfield-analysis.md` links to it** under "What's Next". The packaged skill carries an explicit instruction not to follow that link — a workaround for a corpus bug, and it should be fixed at the source.

4. **The TO-BE canvas** names `create-context-pack` and `generate-context-areas` as the step-03 skills, which is now half wrong.

5. **Two files package the same skill name.** `acceptance-criteria-enhancer.skill` and `requirements-enhancer.skill` both contain `requirements-enhancer`; `stories-from-source.skill` and `_v2` both claim `stories-from-source`. Installing either pair is a name collision. Also `jira-story-estimator 1.skill` carries a stray copy marker.

6. **A live `.env` sits in the QA toolset** at `QA/GenDD-QA-Toolset/engine/mcp/testrail/.env`, beside its `.env.example`. If it holds real TestRail credentials it should not travel with a distributable toolset.

---

*This is tooling documentation, not a standard. It carries no standards frontmatter and is intentionally not registered in `rules-manifest.yaml` — consistent with the other documents in this folder.*
