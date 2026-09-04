---
name: generate-standards
description: Generate standards documents for specific SDLC areas the user names directly (testing, API design, security, etc.), at project or organization scope. Manual invocation only.
disable-model-invocation: true
---

# Generate Standards

For when the user already knows which area(s) need standards and just wants them written — the direct, user-driven counterpart to `/gendd:detect-and-generate-standards`'s scan-first approach.

## 1. Fix the target and gather inputs

The target is **the user's current repository**, never this plugin or the GenDD corpus.

Collect before generating:
- Which SDLC area(s) — see the reference's Available SDLC Areas table (Coding, Testing, API Design, Security, CI/CD, Observability, Data, Frontend, Documentation).
- Scope: project-level (names actual tools/versions in this repo) or organization-level (principles over specific tools).

Context documents at `docs/context/{area}.md` improve accuracy but aren't required — proceed without them if absent, noting less grounding.

## 2. Load the reference (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-standards/generate-standards.md` | **Primary task flow** — steps and the per-area content structure. |

Reading it as it is: verbatim corpus copy, `@GenDD-Flow/...`/`@TargetRepo/...` links don't resolve here.

## 3. Run the process

For each requested area, generate a standards document covering: purpose and scope, rules/conventions (actionable, measurable — not vague aspiration), examples via file references (never embedded code), anti-patterns to avoid, and an enforcement approach (linting, code review, CI checks).

Then self-check each one: is it measurable (can you tell if code follows it)? Is it practical (can developers actually follow it)? Is it consistent with what the codebase already does? Does it have concrete examples?

Save each to `docs/standards/{area}.md`.

## 4. Never invent

A rule not grounded in either an actual codebase pattern or a defensible industry practice is a guess. Where the codebase gives no signal, say so and default to widely-accepted practice rather than presenting a personal preference as a settled standard.

## 5. Hard limits

- Writes only under `docs/standards/` in the target repository, only for areas the user named.
- Never overwrites an existing standards file without being told to — check first, and if one exists, treat this as a revision, not a silent replace.
- No changes to source code, configuration, or build files.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
