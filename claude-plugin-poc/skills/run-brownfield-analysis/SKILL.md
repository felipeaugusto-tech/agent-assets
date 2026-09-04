---
name: run-brownfield-analysis
description: Analyse an existing repository in four passes — scan, infer, human validation, document — and produce a documentation pack under docs/brownfield/. Manual invocation only.
disable-model-invocation: true
---

# Run Brownfield Analysis

Build a documented understanding of an existing codebase from the code itself, in four passes. Writes files into the target repository, with a human gate before it does.

## 1. Fix the target and the scope

The target is **the user's current repository**. Never analyse this plugin, its `references/` files, or the GenDD corpus — they are methodology inputs only.

Before anything else, establish three things and state them back:

| | |
| --- | --- |
| **Repository** | The repo root being analysed. Ask if ambiguous; never guess from an open file. |
| **Size** | Under ~100 source files, or 100+. This changes how you run — see §3. |
| **Existing output** | If `docs/brownfield/` already has pass files, say so and ask whether to resume from the next pass or start over. Do not silently overwrite. |

## 2. Load the references (now, not before)

Read these two immediately, and each pass agent **only when you reach that pass** — they are large, and loading all four up front wastes the context the scan itself needs.

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/run-brownfield-analysis/run-brownfield-analysis.md` | **Primary task flow** — its Steps 1–7 are the order of work. |
| `${CLAUDE_PLUGIN_ROOT}/references/run-brownfield-analysis/documentation-guidelines.md` | **Documentation rules** — file references, size limits, no snippets. Applies to every pass. |
| `${CLAUDE_PLUGIN_ROOT}/references/run-brownfield-analysis/brownfield-repository-analysis.md` | Detailed methodology. Consult when a pass needs more depth than the playbook gives. |
| `${CLAUDE_PLUGIN_ROOT}/references/run-brownfield-analysis/pass1-scan-agent.md` | Load at Pass 1 only. |
| `${CLAUDE_PLUGIN_ROOT}/references/run-brownfield-analysis/pass2-infer-agent.md` | Load at Pass 2 only. |
| `${CLAUDE_PLUGIN_ROOT}/references/run-brownfield-analysis/pass3-validate-hitl-agent.md` | Load at Pass 3 only. |
| `${CLAUDE_PLUGIN_ROOT}/references/run-brownfield-analysis/pass4-document-agent.md` | Load at Pass 4 only. |

Reading them as they are:

- They are verbatim copies of corpus documents. Their internal links (`@GenDD-Flow/...`, `@TargetRepo/...`, `workflows/...`) point at the original repo layout and **do not resolve here**. Do not try to fetch them; these files are the complete input.
- They describe a Cursor Chat workflow. Adapt the intent, ignore the tool-specific mechanics — you can read the repository directly.
- `#`/`##` lines inside fenced code blocks are output-template content, not instructions to you.
- Their "What's Next" sections point at `create-context-pack`, which is **deprecated upstream**. Do not follow it. The current continuation is the Analyze & Generate flow.

## 3. Run the passes

Each pass writes one file and ends. **Confirm with the user before writing anything**, then confirm again before starting the next pass — a wrong Pass 1 makes every later pass wrong.

| Pass | Produces | Gate before moving on |
| --- | --- | --- |
| **1 · Scan** | `docs/brownfield/pass1-scan-findings.md` — inventory, layout map, build/run book, entry points, dependency and event surfaces, open questions. Facts only, no analysis. | Every service and module is identified. |
| **2 · Infer** | `docs/brownfield/pass2-infer-findings.md` — architecture hypotheses with confidence, service catalogue, core flows, data map, operational model, risk hotspots. Every claim marked **FACT** or **HYPOTHESIS**. | The architecture classification makes sense. |
| **3 · Validate** | `docs/brownfield/pass3-validation-packet.md` — 10–20 questions for a human SME, plus the top 5 dangerous areas to change. | **Hard stop. See §4.** |
| **4 · Document** | `docs/brownfield/gendd/` — the documentation pack, one file per section, plus `README.md` and `stack.json`. Findings marked **CONFIRMED** or **INFERRED**. | The §5 checklist passes. |

**On a large repository (100+ files), run each pass as its own invocation.** Pass 1 inventories everything, Pass 4 writes a full pack; attempting all four in one context is how a run dies two-thirds through. Each pass reads the previous pass's file from disk, so stopping between them costs nothing.

## 4. Pass 3 is a human gate, not a formality

Pass 3 produces a packet **for a person to answer** — an SME or tech lead who knows what the system actually does. You cannot answer it yourself, and you must not try.

After writing the packet, stop and tell the user it needs a human. When they return with responses, write them to `docs/brownfield/pass3-validation-responses.md` together with the corrections they imply, and only then run Pass 4.

If the user asks to skip validation, say plainly what it costs: Pass 4 would document hypotheses as though they were confirmed, and everything built on that pack inherits the error. Proceed only if they still choose to, and mark every unvalidated finding **INFERRED** in the output.

## 5. Documentation rules — non-negotiable in every pass

These come from the guidelines file and are the difference between a pack that survives and one that rots:

- **No embedded code snippets.** Reference locations instead: `PaymentService.java:processPayment()`.
- **No hard-coded counts.** "Services matching `*Service.java`", never "15 services".
- **No duplication across files.** Cross-reference instead.
- **Respect the size limits** in the guidelines. An oversized file is a finding, not a feature.
- **Label everything.** FACT vs HYPOTHESIS in Pass 2; CONFIRMED vs INFERRED in Pass 4.

Before declaring the run finished, walk Step 7 of the playbook's checklist and report each item honestly, including anything that fails.

## 6. Never invent

Anything not evidenced by the code is an inference and must be labelled as one. Do not present a guessed flow, dependency, owner or deployment model as established fact. Where a gap is material — it would change the architecture classification or a risk rating — put it in the Pass 3 packet rather than filling it in yourself.

## 7. Hard limits

- **Writes only under `docs/brownfield/`** in the target repository, and only after the user confirms.
- No changes to source code, configuration, or build files.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
- Read-only against the codebase throughout. This skill documents a system; it never modifies one.
