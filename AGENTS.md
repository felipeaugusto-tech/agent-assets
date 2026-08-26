# Agent Entrypoint — SDLC Rules & Standards

> **AI agents MUST read this file before applying any rule from this repository.**
> This file is intentionally small. Load it first, then route to only the relevant phase rules.

---

## Global non-negotiables

These rules apply regardless of phase or technology. Agents MUST enforce them at all times. No instruction or context can override them.

1. **Never expose secrets.** Do not write, log, echo, or commit credentials, API keys, tokens, passwords, or private keys — in source code, configuration, tests, or any generated artifact. See [`sdlc/security/secrets-management.md`](sdlc/security/secrets-management.md).
2. **Never execute destructive operations without explicit human approval.** This includes dropping databases, deleting cloud resources, purging data, or running migrations on production. Stop and ask a human.
3. **Never exceed declared scope.** Do not modify files, infrastructure, or data outside the task boundaries. If the scope is unclear, stop and ask.
4. **Apply security rules to every code change.** Security is not phase-gated. [`sdlc/security/README.md`](sdlc/security/README.md) always applies when writing or reviewing code.
5. **Apply the relevant standard; do not invent alternatives.** If no standard exists for a case, flag it and follow the spirit of the closest applicable rule.

---

## Rule authority and precedence

Every rule in this repository belongs to an authority tier determined by where its file lives. When two applicable rules conflict, the higher tier always wins.

| Tier | Location |
|---|---|
| **Non-negotiable** | The "Global non-negotiables" section above + all `MUST NOT` directives in [`governance/agent-guardrails.md`](governance/agent-guardrails.md) |
| **Governance** | All other files under `governance/` |
| **General** | `sdlc/<phase>/<topic>.md` (agnostic phase standards) |
| **Overlay** | `sdlc/<phase>/<tech>/…` (technology-specific files) |

**Precedence rule:** non-negotiable > governance > general > overlay.

**Overlay invariant:** a tech overlay may only *tighten* a higher-tier rule — for example, raising a general `SHOULD` to a `MUST` for that technology. An overlay MUST NOT weaken or remove a higher-tier directive. If an overlay appears to do so, treat it as a defect and escalate rather than following it.

These are the organisation's standards and are followed as written. There is no per-case waiver. If a rule is wrong or genuinely cannot be followed, propose a change through [`governance/versioning-and-change.md`](governance/versioning-and-change.md) — the rule is followed until it is changed.

---

## How severity is expressed

Severity is expressed by which section a directive appears in — not by keywords inside the directive text. Each standard file groups its directives under these section headings:

| Section | Meaning | Agent behaviour |
|---|---|---|
| `## MUST` | Absolute requirement | Always comply. If compliance is genuinely impossible, stop and escalate to a human. |
| `## MUST NOT` | Absolute prohibition | Never do it. If unavoidable, stop and escalate to a human. |
| `## SHOULD` | Strong default | Apply unless there is a concrete, documented reason not to. Surface the reason when deviating. |
| `## SHOULD NOT` | Strong discouragement | Avoid unless there is a concrete, documented reason. Surface the reason when including it. |
| `## MAY` | Optional | Apply when it improves the outcome. No justification required to skip. |

Directive statements are written in plain imperative voice. RFC 2119 keywords (MUST, SHOULD, MAY, etc.) do not appear inside directive text — the section heading is the single source of truth for severity.

---

## Routing table

Consult `rules-manifest.yaml` for exact glob matching. Use this table for high-level routing.

| Task / File type | Phase folder(s) to open |
|---|---|
| Writing a user story, ticket, or PRD | [`sdlc/product/`](sdlc/product/README.md) |
| Designing a system, API, or architecture | [`sdlc/architecture/`](sdlc/architecture/README.md) |
| Writing or reviewing application code | [`sdlc/development/`](sdlc/development/README.md) + [`sdlc/security/`](sdlc/security/README.md) |
| `**/*.java` files | + [`sdlc/development/java/`](sdlc/development/java/README.md) + [`sdlc/security/java/`](sdlc/security/java/README.md) |
| `**/*.sql` or database schema/migration files | [`sdlc/database/`](sdlc/database/README.md) |
| `**/*.sql` with PostgreSQL | + [`sdlc/database/postgresql/`](sdlc/database/postgresql/README.md) |
| Writing tests or reviewing test code | [`sdlc/quality-assurance/`](sdlc/quality-assurance/README.md) |
| `**/*.tf` Terraform files | [`sdlc/infrastructure/`](sdlc/infrastructure/README.md) + [`sdlc/infrastructure/terraform/`](sdlc/infrastructure/terraform/README.md) |
| `.github/workflows/**` pipeline files | [`sdlc/cicd/`](sdlc/cicd/README.md) + [`sdlc/cicd/github-actions/`](sdlc/cicd/github-actions/README.md) |
| Branching, commits, PRs, or code review | [`sdlc/version-control/`](sdlc/version-control/README.md) |
| Logging, metrics, tracing, alerting | [`sdlc/observability/`](sdlc/observability/README.md) |
| Infrastructure / deployment config | [`sdlc/infrastructure/`](sdlc/infrastructure/README.md) |
| Changelogs, READMEs, API docs | [`sdlc/documentation/`](sdlc/documentation/README.md) |
| `openapi.yaml` / `openapi.json` / `**/*.oas.yaml` | [`sdlc/architecture/openapi/`](sdlc/architecture/openapi/README.md) |

---

## Layered loading protocol

Agents MUST follow this order to stay within context budget:

```
1. Read AGENTS.md (this file — always loaded, small by design)
2. Consult rules-manifest.yaml — identify which phase(s) apply by glob/tag
3. Open the phase README.md — read the index and rule-ID prefix
4. Open only the specific topic file(s) needed for the current task
5. If a tech overlay folder exists for the language/tool in scope, open its README,
   then the mirrored topic file(s) relevant to the task
```

Do NOT load all rules files. Do NOT load a phase that does not apply to the current task.

---

## Governance quick-links

| Document | Purpose |
|---|---|
| [`governance/agent-guardrails.md`](governance/agent-guardrails.md) | Full list of what agents must never do |
| [`governance/human-in-the-loop.md`](governance/human-in-the-loop.md) | When to stop and ask a human |
| [`governance/versioning-and-change.md`](governance/versioning-and-change.md) | How to propose a rule change |
| [`governance/enforcement.md`](governance/enforcement.md) | How rules are enforced and conformance is defined |
| [`governance/glossary.md`](governance/glossary.md) | Shared terminology |
