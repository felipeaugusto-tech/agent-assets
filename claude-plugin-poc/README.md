# GenDD Claude Code Plugin — Proof of Concept

A minimal Claude Code plugin that packages **one** manually invoked skill:
`/gendd:enhance-requirements`.

## Documentation

| Document | What it covers |
|---|---|
| [1-plugin-overview.md](1-plugin-overview.md) | What a Claude Code plugin is, its anatomy, and the invocation-control decision behind this one |
| [2-distribution-guide.md](2-distribution-guide.md) | Sharing a plugin across an organization — the two admin systems, and which one reaches Claude Code |
| [3-token-benchmarks.md](3-token-benchmarks.md) | Measured token and cost impact of installing and invoking the plugin |

## What it does

Takes a vague requirement and returns a structured, testable specification in chat:
problem and goal, actors/personas, assumptions and scope, functional requirements,
non-functional requirements (when relevant), ambiguities/risks/open questions, and
Given/When/Then acceptance criteria.

The skill targets **your current project**. It makes no code changes, creates no files,
uses no MCP servers, and runs no tests — the result is returned in chat only.

Its methodology comes from three repository documents copied verbatim into
`references/enhance-requirements/`:

| File | Role |
| --- | --- |
| `enhance-requirements.md` | Primary task flow (playbook) |
| `enhance-acceptance-criteria.md` | Detailed methodology (workflow) |
| `requirements-enhancement.md` | Required output format (template) |

## Install locally

Session-scoped, no marketplace manifest required. From the repository root:

```bash
claude plugin validate ./claude-plugin-poc      # optional: add --strict
claude --plugin-dir ./claude-plugin-poc
```

## Invoke

Inside that session, type:

```text
/gendd:enhance-requirements
```

Optionally pass the requirement inline:

```text
/gendd:enhance-requirements users should be able to save a payment method
```

If no requirement is supplied, the skill asks for one before doing anything else.

## Methodology loads only after explicit invocation

The skill sets `disable-model-invocation: true`, so Claude cannot trigger it on its own —
only a typed slash command starts it. The three reference documents (~1,100 lines) are read
**after** invocation, not at session startup, so the plugin adds no skill-description or
workflow-context cost to a normal session.

## The original repository files are unchanged

This directory is additive. The three source files under `gendd-analysis/` were copied
byte-for-byte (SHA-256 verified) and nothing outside `claude-plugin-poc/` was created,
edited, moved, or deleted.

This proof of concept is packaging/tooling rather than a standard, so it is intentionally
not registered in `rules-manifest.yaml` and carries no standards frontmatter — a deliberate
choice, not an omission.
