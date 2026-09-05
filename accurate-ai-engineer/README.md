# accurate-ai-engineer

Claude Code plugin bundling engineering & QA skills for Accurate AI: ADRs,
C4 architecture diagrams, CI/CD pipeline security audits, QA test-case
authoring, TestRail publishing, test-gap analysis, test-automation
implementation, and release-evidence packets.

## Skills

| Skill | What it does |
|---|---|
| `adr-writer` | Capture an architectural or technical decision as an Architecture Decision Record (ADR) through collaborative dialogue, using the lean Nygard format. |
| `architecture-diagram-generator` | Generate C4 architecture diagrams (Context, Container, Component, optional Code, Deployment) from an actual codebase, traced to file-level evidence — LikeC4 or Mermaid. |
| `cicd-pipeline-audit` | Audit a Jenkinsfile, Jenkins pipeline, or GitHub Actions workflow for security vulnerabilities and misconfigurations, producing a severity-rated report mapped to the OWASP CI/CD Top 10. |
| `qa-test-case-writer` | Turn a user story or ticket into verified, structured manual test cases — system-aware, ready for human review and optional export. |
| `release-evidence-packet` | Assemble a change-evidence packet from one or more commits (diff, metadata, acceptance-criteria mapping) into one dated, integrity-checked artifact. |
| `test-automation-implementer` | Turn GenDD's "Automate Now" decisions plus their linked test cases into real, executable test code written into the actual repo, using its real test stack. |
| `test-gap-analyzer` | Find where a codebase is untested and rank the gaps by risk using evidence — test-file inventory, coverage data, and change history — rather than intuition. |
| `testrail-publisher` | Publish structured test cases into TestRail via the first-party MCP bridge, always also generating a CSV suitable for manual import. |

## Documentation

| Document | What it covers |
|---|---|
| [1-plugin-overview.md](../1-plugin-overview.md) | What a Claude Code plugin is, its anatomy, and the invocation-control decision behind these skills |
| [2-distribution-guide.md](../2-distribution-guide.md) | Sharing a plugin across an organization — the two admin systems, and which one reaches Claude Code |
| [3-token-benchmarks.md](../3-token-benchmarks.md) | Measured token/cost impact of installing and invoking a plugin skill (historical baseline from the original single-skill POC) |
| [marketplace.json](../.claude-plugin/marketplace.json) | Catalog entry for this plugin and its sibling, `accurate-ai-product` |

## Install locally

Session-scoped, no marketplace manifest required. From the repository root:

```bash
claude plugin validate ./accurate-ai-engineer      # add --strict to be strict
claude --plugin-dir ./accurate-ai-engineer
```

## Invoke

Every skill in this plugin is **model-invocable by default** — Claude can load
one on its own when a request matches its description, or you can force a
specific skill with its slash command:

```text
/accurate-ai-engineer:adr-writer
/accurate-ai-engineer:architecture-diagram-generator
/accurate-ai-engineer:cicd-pipeline-audit
/accurate-ai-engineer:qa-test-case-writer
/accurate-ai-engineer:release-evidence-packet
/accurate-ai-engineer:test-automation-implementer
/accurate-ai-engineer:test-gap-analyzer
/accurate-ai-engineer:testrail-publisher
```

## Install org-wide

For distributing this plugin to a whole organization (managed settings or a
marketplace), see [2-distribution-guide.md](../2-distribution-guide.md).

## Project context

`qa-test-case-writer` ships a `Context.md` project-info template. Filling it
in with your project's real facts (repo, stack, conventions) makes its output
project-aware instead of generic — see the skill's own `Context.md` for what
to fill in.
