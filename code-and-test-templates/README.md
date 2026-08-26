# Accurate — Code Generation & Unit Test Generation Templates

Playbooks built on GenDD scaffolding artifacts, with illustrative examples for Java and Angular.

## How This Fits Accurate's GenDD Scaffolding

Every Accurate repository is expected to carry a `docs/` folder produced by the GenDD scaffolding process. This document set assumes that structure exists (or should exist) in the target repository, and shows how two of the on-demand GenDD playbooks — **Code Generation** and **Generate Unit Tests** — turn into concrete, ready-to-use templates once real repo context is loaded into them. The scaffolding shape looks like this:

```
<repository>/
  docs/
    brownfield/
      gendd/               system documentation pack (Pass 1-4 output):
                            overview/, architecture/, flows/, risks/,
                            onboarding/guide.md, stack.json, README.md
      pass3-validation-responses.md   SME-confirmed vs. still-INFERRED findings
    context/               SDLC-area context files (backend-development.md,
                            frontend-development.md, quality-assurance.md, ...)
    playbooks/
      _repo-context.md      shared repo context — read this before any
                             role/on-demand/recurring playbook below
      PLAYBOOK-GUIDE.md      decision tree for which playbook to run
      by-role/, on-demand/, onboarding/, recurring/
    standards/             coding.md, testing.md, standards-inventory.md
```

Two things about this shape matter when filling in a prompt template below:

- **The brownfield pack lives under `docs/brownfield/gendd/`**, split into topic subfolders rather than one flat file. `docs/brownfield/gendd/risks/risk-hotspots.md` and `docs/brownfield/gendd/onboarding/guide.md` are worth checking before touching a class/component that might be a known dangerous zone.
- **`docs/playbooks/_repo-context.md` is a short, always-present, repo-wide context file** (identity, key paths, architecture snapshot, integrations, risk hotspots) that every playbook reads first, before the deeper per-SDLC-area files under `docs/context/`. Where it exists, read it first in the prompt templates below.
- Brownfield facts carry a validation status (**CONFIRMED** vs. **INFERRED**/**PENDING**, tracked in `docs/brownfield/pass3-validation-responses.md` or equivalent). Treat an INFERRED-and-not-yet-confirmed "existing convention" as a hypothesis to verify against the actual reference files you were pointed at, not as settled fact.

## Purpose

These playbooks turn the generic GenDD on-demand playbooks into fully worked templates, grounded in patterns common across Accurate's Java services and Angular applications. Where a repository has formal `docs/standards/coding.md` and `testing.md` files, load those directly — they contain the authoritative rules for that repo. The illustrative conventions in these playbooks are a ready-to-use starting point for the prompt templates either way.

The "Typical Conventions" tables and prompt-template constraints in each playbook are additionally grounded in Accurate's cross-cutting engineering standards library (security, performance, reliability, database, accessibility, frontend UI, and testing standards). That library states the general rule (e.g. "parameterize SQL," "paginate unbounded lists," "retry with backoff and jitter," "give icon-only controls an accessible name"); these playbooks show what applying it looks like in a Java or Angular file. Where a repository's own `docs/standards/coding.md`/`testing.md` says something different, the repo's own standard wins — these playbooks still supply the prompt structure and worked examples unchanged.

## Format

Each playbook file follows the same shape:

- A metadata table (category, target roles, prerequisites, inputs, outputs)
- **What Is This Playbook?** / **When to Use This Playbook**
- **Typical Conventions** a formal coding/testing standard should capture for that stack
- **The Prompt Template (Full)** — copy-paste ready, with bracketed placeholders
- **Illustrative Example** — a worked example with realistic (invented) code
- **Review Checklist**

Table styling and code-fence conventions match Accurate's other coding-pattern reference documents so they read as one family.

## GenDD Artifacts These Templates Draw On

| GenDD artifact | Role in these templates |
|---|---|
| `docs/playbooks/_repo-context.md` | Shared repo identity, key paths, and risk hotspots — read first, before any area-specific context |
| `docs/context/backend-development.md` / `frontend-development.md` | Real layering, tech-stack, and file-location facts for the target repo |
| `docs/context/quality-assurance.md` | Real test coverage state and risk hotspots for the target repo |
| `docs/standards/coding.md` | Naming, layering, and error-handling standards to quote directly in a code-generation prompt |
| `docs/standards/testing.md` | Test frameworks, required scenarios, and anti-patterns to quote directly in a test-generation prompt |
| `docs/playbooks/on-demand/generate-unit-tests.md` | Baseline step structure for unit-test generation, specialized here per stack |
| `docs/standards/standards-inventory.md` | Confirms which formal coding/testing standards exist for the target repo |
| `docs/brownfield/gendd/risks/risk-hotspots.md` | Flags whether the target class/component is a known dangerous change zone before you start |

## Playbooks

| Playbook | Stack | Run it when | Produces |
|---|---|---|---|
| [Java Code Generation](code/java-code-generation.md) | Java | Adding a new endpoint, service, REST client, or data-access class | New production class(es) matching the target repo's conventions, testable by construction or with an explicit seam |
| [Java Unit Test Generation](test/java-unit-test-generation.md) | Java | Testing new Java code, or adding coverage to an existing high-risk class | Test class(es) covering success, edge cases, and error conditions, including controller-layer status checks |
| [Angular Code Generation](code/angular-code-generation.md) | Angular | Adding a new component, service, or route | New component(s)/service(s) matching the target app's conventions |
| [Angular Unit Test Generation](test/angular-unit-test-generation.md) | Angular | Testing new Angular code, or adding coverage to an existing component/service | Spec file(s) covering creation, inputs/outputs, branches, and success/error paths |

Each language's code-generation and test-generation playbooks are designed to be used as a pair: the code playbook builds in the testability seam (constructor injection, or an explicit setter/constructor overload) that the matching test playbook then relies on.

## Related Resources

| Resource | Path |
|---|---|
| Shared repo context (read first) | `docs/playbooks/_repo-context.md` |
| Backend/frontend/QA context for the target repo | `docs/context/*.md` |
| Coding/testing standards | `docs/standards/coding.md`, `docs/standards/testing.md` |
| Standards inventory | `docs/standards/standards-inventory.md` |
| Brownfield system documentation pack | `docs/brownfield/gendd/` (see `README.md`, `overview/`, `architecture/`, `flows/`, `risks/`, `onboarding/guide.md`, `stack.json`) |
| Brownfield validation status (confirmed vs. inferred) | `docs/brownfield/pass3-validation-responses.md` (or repo equivalent) |
| Cross-cutting engineering standards library these templates draw on | `agent-assets-main/standards/` (accessibility, api, code-quality, code-review, database, documentation, frontend, infrastructure, observability, performance, platform, product, reliability, security, testing) |
| Companion Accurate coding-pattern reference documents | Same visual/table format as this document set |

*Where a repository already has formal `docs/standards/coding.md` and `testing.md`, those take precedence over the illustrative conventions in these playbooks — the prompt templates and worked examples still apply unchanged; only the specific rules quoted into the prompt should come from the repo's real standards.*
