---
name: review-test-coverage
description: Recurring test-health review -- refresh the test gap analysis, compare against the previous review, update coverage metrics, and produce a sprint-level remediation plan. Manual invocation only.
disable-model-invocation: true
---

# Review Test Coverage

For sprint boundaries, pre-release checks, post-incident verification, or quarterly review. Produces an updated gap matrix and a prioritized, sprint-sized remediation plan — not just a fresh inventory.

## 1. Fix the target and gather inputs

The target is **the user's current repository**, never this plugin or the GenDD corpus.

Useful before starting, ask if not already known: the product name, critical integrations, and known problem areas — the gap analysis in §3 needs this context to prioritize correctly.

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/review-test-coverage/review-test-coverage.md` | **Primary task flow** — the six steps below follow it. |
| `${CLAUDE_PLUGIN_ROOT}/references/review-test-coverage/identify-test-gaps.md` | The gap-analysis method Step 1 runs. If `/gendd:test-gap-analyzer` exists in this plugin, prefer invoking it instead — this bundled copy is the standalone fallback. |
| `${CLAUDE_PLUGIN_ROOT}/references/review-test-coverage/testing.md` | Foundational testing principles used to assess regression/sanity suite health in Step 4. |

Reading these as they are: verbatim corpus copies, `@TargetRepo/...` links don't resolve here.

## 3. Run the process

1. **Re-run the gap analysis** (via the bundled method or `/gendd:test-gap-analyzer` if available) using the product/integration/problem-area context gathered in §1.
2. **Compare with the previous analysis**, if `docs/test-gap-matrix.md` and `docs/test-recommendations.md` already exist: what closed, what's new, is the trend improving or declining, which past recommendations landed vs. are still pending.
3. **Update coverage metrics** — unit, integration, E2E, and critical-path coverage numbers, pulled from CI/CD if accessible.
4. **Assess regression/sanity suite health** — do sanity tests run post-deploy, is the regression suite current, are stale tests removed after feature changes, can tests run independently by feature area.
5. **Generate a sprint remediation plan** — prioritize remaining gaps by business risk, sized as sprint-level tasks with effort estimates.
6. **Prepare the stakeholder summary** — coverage trend, critical remaining gaps, the sprint plan, risk areas needing attention.

## 4. Never invent

A coverage number not pulled from an actual test run, CI report, or direct file inspection is a guess and must be labelled as an estimate. A "gap closed" claim needs an actual test found covering it — don't infer closure from a ticket being marked done.

## 5. Hard limits

- Writes only under `docs/` in the target repository: `test-inventory.md`, `test-gap-matrix.md`, `test-coverage-map.md`, `test-recommendations.md`, `test-roadmap.md`.
- No changes to source code or test files themselves — this reviews coverage, it doesn't write tests (see `/gendd:generate-unit-tests` for that).
- No MCP tools.
- No test runs, builds, deploys, or benchmarks initiated by this skill — it reads existing CI output rather than triggering new runs.
