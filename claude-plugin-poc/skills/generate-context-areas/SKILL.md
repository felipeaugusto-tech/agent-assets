---
name: generate-context-areas
description: Generate one project-specific context document per applicable SDLC area (architecture, backend, database, security, etc.), grounded in a prior brownfield analysis. Manual invocation only.
disable-model-invocation: true
---

# Generate Context Areas

Produce `docs/context/{area}.md` for each SDLC area that applies to the target codebase — descriptive state ("this project uses X, at Y"), not prescriptive rules. Writes files into the target repository, with a human gate before generation starts.

## 1. Fix the target and check prerequisites

The target is **the user's current repository**. Never analyse this plugin, its `references/` files, or the GenDD corpus — they are methodology inputs only.

This skill needs two things to already exist. Check for them before doing anything else:

| Prerequisite | Where | If missing |
| --- | --- | --- |
| Brownfield (or greenfield) analysis output | `docs/brownfield/` (brownfield) or `docs/greenfield/inference-result.md` (greenfield) | Tell the user to run `/gendd:run-brownfield-analysis` first. Do not proceed without it — there is nothing to ground the context documents in. |
| A **confirmed** SDLC area list with confidence levels | Wherever the user has it (often just the conversation) | Run the area-detection step yourself — see §2's role-detector reference — present the map, and **wait for the user to confirm or adjust it** before generating anything. |

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-context-areas/generate-context-areas.md` | **Primary task flow** — its Steps 1–3 are the order of work. |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-context-areas/context-area.md` | **Output template** — the structure every context document must follow. |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-context-areas/pass5-role-detector-agent.md` | Load **only if** no confirmed area list exists yet (see §1). Produces the HIGH/MEDIUM/LOW/BASELINE map and the confirmation prompt to show the user. |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-context-areas/{area}.md` | The 16 area-framework files (`architecture.md`, `backend-development.md`, `database-management.md`, `delivery-management.md`, `devops-infrastructure.md`, `frontend-development.md`, `fullstack-development.md`, `product-management.md`, `quality-assurance.md`, `release-management.md`, `security.md`, `site-reliability.md`, `support-engineering.md`, `technical-leadership.md`, `technical-writing.md`, `user-experience.md`). Load **one at a time, per area, when you reach it** in the queue (§3) — not all sixteen up front. Defines what to examine and what questions to answer for that specific area. |

Reading these files as they are:

- They are verbatim copies of corpus documents. Internal links (`@GenDD-Flow/...`, `workflows/...`) point at the original repo layout and **do not resolve here** — do not try to fetch them.
- They describe a Cursor Chat workflow. Adapt the intent, ignore the tool-specific mechanics.
- `#`/`##` lines inside fenced code blocks are output-template content, not instructions to you.
- `{AREA_NAME}`, `{DATE}` and similar bracketed placeholders in the template get filled with real values, not left in the output.

## 3. Run the process

### Step 1 — Prepare the area queue

Order the confirmed areas: BASELINE first (`technical-leadership`, `architecture`), then HIGH, then MEDIUM, then LOW/MANUAL. Later documents may reference earlier ones, so generate in this order.

### Step 2 — Generate each context document

For every area in the queue:

1. Load that area's `knowledge/sdlc-areas/{area}.md` framework (or, for a custom area with no framework file, use the template's general structure).
2. Apply the framework to the actual codebase using the brownfield findings plus direct inspection — answer its questions with evidence, note patterns and gaps, collect **file references, not code snippets**.
3. Fill `context-area.md`'s structure with that evidence and save to `docs/context/{area}.md`.

Depth follows confidence: HIGH areas run 150–200 lines, MEDIUM 100–150, LOW 50–100, BASELINE/MANUAL 100–150. Thinner than that is usually too shallow; past 250 lines, split the area instead of padding it.

### Step 3 — Cross-reference pass

After all documents exist, check consistency across them: no contradictions, shared concepts (e.g. authentication) described the same way everywhere, and cross-references added where one area informs another.

## 4. Never invent

Anything not evidenced by the code (or, for greenfield, by the planning documents) is an inference and must be labelled as one. Where evidence is thin for an area, write a shorter document and add a "Gaps" section rather than filling it in from general best practices — context documents describe what **is**, never what should be.

## 5. Hard limits

- Writes only under `docs/context/` in the target repository, and only after the area list is confirmed (§1).
- No changes to source code, configuration, or build files.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
- Read-only against the codebase otherwise.
