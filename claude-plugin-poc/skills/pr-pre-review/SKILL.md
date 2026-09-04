---
name: pr-pre-review
description: Run an automated first pass over a PR -- route the diff through rules-manifest.yaml, check mechanical standards (size, description, ticket link), and compare against an implementation plan if one exists. Manual invocation only.
disable-model-invocation: true
---

# PR Pre-Review

Catches what standards already say plainly, before a human reviewer spends time on it. Does not replace human review — `sdlc/version-control/code-review.md` still requires peer approval for correctness, security, and test-quality judgment; this pass only handles what's mechanically checkable. This is also the skill a CI Action calls on PR open/update.

## 1. Fix the target and gather inputs

The target is **the PR being reviewed**, in the user's current repository — never this plugin or the GenDD corpus.

Get the PR diff, description, and metadata (base/head refs, linked ticket if any) before starting.

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/pr-pre-review/pr-pre-review.md` | **Primary task flow.** |
| `${CLAUDE_PLUGIN_ROOT}/references/pr-pre-review/pr-pre-review-template.md` | **Report template.** |
| `${CLAUDE_PLUGIN_ROOT}/references/pr-pre-review/rules-manifest.yaml` | **Routing table** — same as `lookup-standard`'s. |
| `${CLAUDE_PLUGIN_ROOT}/references/lookup-standard/{sdlc,governance}/**` | The standards content itself. Shared with `/gendd:lookup-standard` rather than duplicated — resolve the manifest's `file:` column the same way: `sdlc/version-control/pull-requests.md` → `${CLAUDE_PLUGIN_ROOT}/references/lookup-standard/sdlc/version-control/pull-requests.md`. |

## 3. Run the process

1. **Categorize the changed files** by type and area, same as `/gendd:run-delta-analysis` does.
2. **Route through the rules manifest** — for every changed path, resolve which entries' `applies_to` glob matches, the same resolution `/gendd:lookup-standard` uses. This always pulls in the org-wide version-control standards (`sdlc/version-control/pull-requests.md`, `sdlc/version-control/code-review.md`) plus any matched tech overlay.
3. **Check only what's mechanically verifiable**: PR size against the routed standard's threshold (generated code, lock files, migrations excluded from the count), description completeness (what/why/how-to-test present), ticket linking, CI status. **Do not** attempt correctness, security-reasoning, or test-adequacy judgment — defer those to human review explicitly rather than guessing at a verdict.
4. **Compare against the implementation plan**, if `docs/plans/{feature-slug}.md` exists for this change: files touched but not planned (flag as possible scope creep), planned files not touched (flag as plan-stale or work-incomplete). If no plan exists, say so plainly — don't skip this section silently.
5. **Produce the report** using `pr-pre-review-template.md`: violations with specific rule IDs, the plan comparison (or its absence), judgment items explicitly deferred to human review, and a clear ready/not-ready verdict.

## 4. Never invent

A violation not traceable to a specific rule ID, or a plan mismatch not backed by an actual file-list diff, is noise a reviewer will learn to ignore. When a check needs judgment this pass can't make, say it needs human review — never guess at a pass/fail.

## 5. Hard limits

- Writes only a PR comment and, optionally, `docs/reviews/pr-{number}-pre-review.md`.
- Never approves or merges a PR — produces a report only.
- No MCP tools beyond what's needed to read the PR/diff/CI status.
- No source code changes.
