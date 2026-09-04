---
name: detect-and-generate-standards
description: Scan a repository for existing coding/product/security/testing/etc. standards, find gaps against the confirmed SDLC areas, and generate missing standards documents on request. Manual invocation only.
disable-model-invocation: true
---

# Detect & Generate Standards

Preserve what exists, fill what is missing. Scans for standards-related files across SDLC areas, produces a gap analysis, and only generates new `docs/standards/{area}.md` documents after the user says which gaps to fill. Never overwrites an existing standards file.

## 1. Fix the target and check prerequisites

The target is **the user's current repository**. Never analyse this plugin, its `references/` files, or the GenDD corpus — they are methodology inputs only.

This skill assumes two things already exist — check before scanning:

| Prerequisite | Where | If missing |
| --- | --- | --- |
| A confirmed SDLC area list | Wherever the user has it | Ask which areas matter, or run `/gendd:generate-context-areas` first if none exists — this skill's gap analysis is organized by area. |
| Context documents (recommended, not required) | `docs/context/{area}.md` | Proceed without them if absent, but note in the gap analysis that context is missing for a given area — it's an input, not a hard blocker. |

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/detect-and-generate-standards/detect-and-generate-standards.md` | **Primary task flow** — its Steps 1–7 are the order of work. |
| `${CLAUDE_PLUGIN_ROOT}/references/detect-and-generate-standards/_template.md` | Generic standards-document skeleton. |
| `${CLAUDE_PLUGIN_ROOT}/references/detect-and-generate-standards/{architecture,coding,delivery,operations,product,security,testing}.md` | One filled worked-example per domain — load only the ones matching the areas the user asks you to generate, as a structure/depth reference, not to copy content from. |

Reading these files as they are:

- Verbatim copies of corpus documents. Internal links (`@GenDD-Flow/...`, `workflows/...`) point at the original repo layout and **do not resolve here**.
- They describe a Cursor Chat workflow — adapt the intent, ignore the tool-specific mechanics.
- `#`/`##` lines inside fenced code blocks are output-template content, not instructions to you.

## 3. Run the process

### Step 1 — Scan for existing standards

Check the target repo for standards-related files across all confirmed areas: linter/formatter configs (`.eslintrc*`, `.prettierrc*`, `tsconfig.json`, `pyproject.toml`, `.golangci.yml`, `.rubocop.yml`...), `CONTRIBUTING.md`, issue/PR templates, `SECURITY.md`, `SLA.md`/`SLO.md`, runbooks, ADR directories, `ARCHITECTURE.md`, test-framework configs, coverage configs, and sprint/branching-strategy docs. The primary reference file lists the full pattern table per category — consult it rather than relying on memory.

### Step 2 — Catalog findings

Record every file found: category, path, one-line description. Then roll that up per confirmed SDLC area as Full / Partial / No coverage.

### Step 3 — Identify gaps

For each confirmed area, classify coverage as full, partial, or none, and produce a gap analysis listing which areas have standards and which don't.

### Step 4 — Present findings, then stop

Show the inventory and gap analysis, then ask which missing areas (if any) to generate standards for, at what scope, and any constraints. **Do not generate anything until the user responds** — this is the human gate.

### Step 5 — Determine scope

For each area the user asks for: project-level (names actual tools/versions in this repo) or organization-level (principles over specific tools, meant to apply across repos).

### Step 6 — Generate missing standards

Priority order for content: codebase patterns (from brownfield/context) → existing partial standards (extend, don't replace) → industry best practice to fill remaining gaps → user preferences. Follow the template structure (Scope, Core Principles, Standards table with MUST/SHOULD/MAY + rationale, Tooling, Exceptions, References). Target 100–200 lines per document. Never invent a tool the codebase doesn't actually use.

### Step 7 — Save output

Save to `docs/standards/{area}.md`. **Never overwrite an existing standards file** — if one exists, reference it, note its gaps, and suggest additions instead. Always (re)generate `docs/standards/standards-inventory.md` cataloging everything found and created.

## 4. Never invent

A standard not grounded in either an actual codebase pattern or a stated best practice is a guess, and guessed standards get ignored. Where the codebase gives no signal for a MUST/SHOULD/MAY call, say so and default to industry practice rather than presenting a preference as settled.

## 5. Hard limits

- Writes only under `docs/standards/` in the target repository, and only for areas the user explicitly asked for in Step 4's response.
- Never overwrites an existing standards file, ever.
- No changes to source code, configuration, or build files.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
