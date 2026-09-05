# accurate-ai-product

Claude Code plugin bundling product & planning skills for Accurate AI: PRD
authoring, requirements/story generation from source material, acceptance-
criteria enhancement, and Jira story-point estimation.

## Skills

| Skill | What it does |
|---|---|
| `prd-writer` | Write, structure, or improve a Product Requirements Document (PRD) — technical, business/feature, or PoC/spike variants. |
| `stories-from-source` | Turn an unstructured source (meeting notes, a call transcript, a PRD, a discovery doc) into a traceable set of user stories with Gherkin acceptance criteria, edge cases, and NFRs, plus a coverage map. |
| `requirements-enhancer` | Expand vague product requirements into engineer-ready acceptance criteria — observable, testable, with scope control, edge cases, integration impacts, NFRs, and open questions. |
| `jira-story-estimator` | Agentically estimate Jira stories on the Fibonacci complexity scale (0.5–13), from ticket understanding through decomposition to a defensible point estimate. |

## Documentation

| Document | What it covers |
|---|---|
| [1-plugin-overview.md](../1-plugin-overview.md) | What a Claude Code plugin is, its anatomy, and the invocation-control decision behind these skills |
| [2-distribution-guide.md](../2-distribution-guide.md) | Sharing a plugin across an organization — the two admin systems, and which one reaches Claude Code |
| [3-token-benchmarks.md](../3-token-benchmarks.md) | Measured token/cost impact of installing and invoking a plugin skill (historical baseline from the original single-skill POC) |
| [marketplace.json](../.claude-plugin/marketplace.json) | Catalog entry for this plugin and its sibling, `accurate-ai-engineer` |

## Install locally

Session-scoped, no marketplace manifest required. From the repository root:

```bash
claude plugin validate ./accurate-ai-product      # add --strict to be strict
claude --plugin-dir ./accurate-ai-product
```

## Invoke

Every skill in this plugin is **model-invocable by default** — Claude can load
one on its own when a request matches its description, or you can force a
specific skill with its slash command:

```text
/accurate-ai-product:prd-writer
/accurate-ai-product:stories-from-source
/accurate-ai-product:requirements-enhancer
/accurate-ai-product:jira-story-estimator
```

## Install org-wide

For distributing this plugin to a whole organization (managed settings or a
marketplace), see [2-distribution-guide.md](../2-distribution-guide.md).

## Project context

`requirements-enhancer` ships a `Context.md` project-info template. Filling it
in with your project's real facts (repo, stack, conventions) makes its output
project-aware instead of generic — see the skill's own `Context.md` for what
to fill in.
