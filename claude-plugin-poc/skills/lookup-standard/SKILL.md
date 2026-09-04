---
name: lookup-standard
description: Resolve a rule ID, topic, or file path/glob against the org's rules-manifest.yaml and load only the matching standard(s) -- not the whole 96-file corpus. Manual invocation only.
disable-model-invocation: true
---

# Lookup Standard

A router, not a library load. `rules-manifest.yaml` indexes 96 standards under `sdlc/` and `governance/`; this skill finds the one (or few) that actually apply to what the user is doing, and loads only those — the other ~90 files cost nothing because they were never opened.

## 1. Fix the target

The target is **whatever the user is working on** — a file, a task, a topic, or a rule ID they already know. This skill itself never analyses this plugin or the corpus as a subject; the corpus **is** the reference data it routes through.

## 2. Load the manifest (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/lookup-standard/rules-manifest.yaml` | **The routing table.** Each entry: `id`, `file` (path relative to `agent-assets/`), `phase`, `title`, `summary`, `tags`, `applies_to` (glob pattern(s)), `tech` (overlay technology or null), `extends` (base standard an overlay extends, or null). |

Do not load any standard file yet — resolve the match first.

## 3. Resolve the match

Given what the user asked for:

- **A rule ID** (e.g. `GOV-CHARTER`, `SEC-AUTHN`) — look it up directly.
- **A file path or glob** (e.g. `src/api/PaymentController.java`, `*.tsx`) — find every entry whose `applies_to` pattern matches it. A path can match more than one entry (an agnostic standard plus a `tech`-specific overlay that `extends` it) — load both, the overlay adds to the base, it doesn't replace it.
- **A topic or keyword** (e.g. "how do we handle secrets", "PR review rules") — search `tags`, `title`, and `summary` for the closest match(es). If more than one entry plausibly fits, list them and ask which, rather than guessing.

## 4. Load only what matched

For each matched entry, read `${CLAUDE_PLUGIN_ROOT}/references/lookup-standard/{entry.file}` — the manifest's `file` column maps directly onto this path (e.g. `sdlc/product/product-requirements-doc.md` → `${CLAUDE_PLUGIN_ROOT}/references/lookup-standard/sdlc/product/product-requirements-doc.md`). These are mirrored verbatim from the corpus, directory structure intact — resolve the path literally, don't guess a flattened name.

**Only `sdlc/` and `governance/` are mirrored here.** A standard's own text sometimes points at a path outside those two trees (e.g. `templates/adr-template.md`) — that path does **not** resolve under this skill's `references/` and must not be presented as if it does. Quote it as the corpus's own reference (informational — "the standard points to templates/adr-template.md in the source corpus") rather than fabricating a `${CLAUDE_PLUGIN_ROOT}/...` path for it.

Present the standard's content (or the relevant section, if the user's ask is narrow) directly — this skill's job ends at "here is the standard that applies," not applying it for them.

## 5. Never invent

If no manifest entry matches, say so plainly rather than fabricating a plausible-sounding rule. If several entries are a close call, name the ambiguity and ask rather than picking one silently — the whole point of routing through the manifest is precision, not a best guess.

## 6. Hard limits

- Read-only: loads standards, writes nothing.
- Never loads a standard the user's request doesn't actually match — resist the temptation to "helpfully" load related-looking entries.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
