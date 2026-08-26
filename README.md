# SDLC AI Governance — Rules & Standards

This repository is the single source of truth for the rules and standards that AI agents and developers MUST follow across every phase of the software development lifecycle (SDLC).

## Purpose

- Provide strong, enforceable, technology-agnostic standards for every SDLC phase.
- Enable AI agents to route to only the rules relevant for a given task, keeping context windows efficient.
- Allow teams to extend the agnostic core with technology-specific overlays (e.g. `development/java/`) without modifying the shared baseline.

## How this repository is organised

```
rules-and-standards/
├── README.md                  # This file
├── AGENTS.md                  # AI agent entrypoint — always read first
├── rules-manifest.yaml        # Compact routing manifest (globs + summaries)
├── templates/                 # Document skeletons used when authoring new rules
├── governance/                # Meta layer: how rules are authored, versioned, enforced
└── sdlc/                      # One folder per SDLC phase
    ├── product/
    ├── architecture/
    ├── development/
    ├── security/
    ├── database/
    ├── quality-assurance/
    ├── version-control/
    ├── cicd/
    ├── observability/
    ├── infrastructure/
    └── documentation/
```

Each SDLC phase folder contains:
- `README.md` — phase index, rule-ID prefix, and links to topic standards and tech overlays.
- Focused agnostic topic standards (e.g. `coding-standards.md`).
- Technology overlay subfolders (e.g. `development/java/`) with files that mirror and extend the agnostic topics.

## How to navigate

| Goal | Start here |
|---|---|
| AI agent starting a task | [`AGENTS.md`](AGENTS.md) |
| Find which rules apply to a file/task | [`rules-manifest.yaml`](rules-manifest.yaml) |
| Understand a specific SDLC phase | `sdlc/<phase>/README.md` |
| Author or modify a rule | [`governance/rule-authoring.md`](governance/rule-authoring.md) |
| Propose a rule change | [`governance/versioning-and-change.md`](governance/versioning-and-change.md) |
| Look up a term | [`governance/glossary.md`](governance/glossary.md) |

## Rule ID scheme

Every rule carries a stable ID: `<PREFIX>-<NNN>` for agnostic rules, `<PREFIX>-<TECH>-<NNN>` for tech overlays.

| Phase | Prefix |
|---|---|
| Product | `PRD` |
| Architecture | `ARC` |
| Development | `DEV` |
| Security | `SEC` |
| Database | `DAT` |
| Quality Assurance | `QA` |
| Version Control | `VCS` |
| CI/CD | `CICD` |
| Observability | `OBS` |
| Infrastructure | `INF` |
| Documentation | `DOC` |

## Severity model

Severity is expressed by which **section** a directive appears under in a standard file — not by keywords inside the directive text. The section heading is the single source of truth.

| Section | Meaning |
|---|---|
| `## MUST` | Absolute requirement. Deviation requires a formal exception. |
| `## MUST NOT` | Absolute prohibition. Deviation requires a formal exception. |
| `## SHOULD` | Strong default. Deviation allowed with documented justification. |
| `## SHOULD NOT` | Strongly discouraged. Including it requires documented justification. |
| `## MAY` | Optional guidance. |

Directive text is written in plain imperative voice. RFC 2119 keywords do not appear inside directive statements.

**Authority tiers** (highest to lowest): non-negotiable → governance → general → overlay. On conflict, the higher tier wins. See [`AGENTS.md`](AGENTS.md) for the full precedence rules.

## Contributing

See [`governance/rule-authoring.md`](governance/rule-authoring.md) for the full contribution process, including the requirement to add a `rules-manifest.yaml` entry for every new standard file.
