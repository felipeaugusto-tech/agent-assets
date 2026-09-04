# Workflow: Detect & Generate Standards

## Quick Start

```
Read @GenDD-Flow/workflows/detect-and-generate-standards.md

Scan @TargetRepo for existing standards and conventions.
Compare against the SDLC areas confirmed in Phase 2.
Identify gaps and present findings before generating anything.
```

## Overview

This workflow is **Phase 4** of the Analyze & Generate flow. It scans the target repository for existing standards, conventions, and policy documents across all confirmed SDLC areas. It then identifies gaps and offers to generate missing standards documents populated with patterns detected in the codebase and industry best practices.

The goal is to **preserve what exists** and **fill what is missing** — never overwrite existing standards.

## Prerequisites

- Completed Phase 1: Brownfield analysis at `docs/brownfield/`
- Completed Phase 2: Confirmed SDLC area list
- Completed Phase 3: Context documents at `docs/context/`
- Access to the target codebase

---

## Process

### Step 1: Scan for Existing Standards

Scan the target repository for standards-related files across all SDLC areas. Check the following locations and file patterns:

#### Coding Standards
| File Pattern | What It Contains |
|-------------|-----------------|
| `.editorconfig` | Editor formatting rules |
| `.eslintrc*`, `.eslintignore` | JavaScript/TypeScript linting rules |
| `.prettierrc*`, `.prettierignore` | Code formatting rules |
| `biome.json`, `biome.jsonc` | Biome linter/formatter config |
| `.stylelintrc*` | CSS/style linting rules |
| `tsconfig.json`, `tsconfig.*.json` | TypeScript compiler options |
| `pyproject.toml`, `setup.cfg` | Python project config and linting |
| `.golangci.yml` | Go linter configuration |
| `.rubocop.yml` | Ruby style guide enforcement |
| `CONTRIBUTING.md` | Contribution guidelines |
| `CODING_STANDARDS.md`, `STYLE_GUIDE.md` | Explicit coding standards |

#### Product Standards
| File Pattern | What It Contains |
|-------------|-----------------|
| `story-template*`, `.github/ISSUE_TEMPLATE/` | Story/issue templates |
| `DoR*`, `DoD*` | Definition of Ready / Definition of Done |
| `REQUIREMENTS.md` | Requirements documentation |
| `backlog-policy*` | Backlog management rules |
| `.github/PULL_REQUEST_TEMPLATE*` | PR template and expectations |

#### Delivery Standards
| File Pattern | What It Contains |
|-------------|-----------------|
| `SPRINT_CONVENTIONS.md` | Sprint process documentation |
| `ESTIMATION_GUIDE.md` | Estimation methodology |
| `RETRO_FORMAT.md` | Retrospective format |
| `BRANCHING_STRATEGY.md`, `GIT_WORKFLOW.md` | Git flow documentation |

#### Testing Standards
| File Pattern | What It Contains |
|-------------|-----------------|
| `TEST_PLAN.md` | Test strategy document |
| `COVERAGE_POLICY.md` | Coverage requirements |
| `QA_CHECKLIST.md` | Quality assurance checklist |
| `jest.config*`, `vitest.config*`, `pytest.ini` | Test framework configuration |
| `.nycrc*`, `codecov.yml` | Coverage configuration |

#### Security Standards
| File Pattern | What It Contains |
|-------------|-----------------|
| `SECURITY.md` | Security policy |
| `SECURITY_POLICY.md` | Detailed security standards |
| `THREAT_MODEL.md` | Threat modeling documentation |
| `.snyk`, `.trivyignore` | Security scanning configuration |
| `OWASP_COMPLIANCE.md` | OWASP compliance documentation |
| `codeql-config.yml`, `.github/codeql/` | Code analysis configuration |

#### Operations Standards
| File Pattern | What It Contains |
|-------------|-----------------|
| `RUNBOOK*`, `runbooks/` | Operational runbooks |
| `INCIDENT_RESPONSE.md` | Incident response procedures |
| `SLA.md`, `SLO.md` | Service level documentation |
| `ON_CALL.md` | On-call procedures |
| `MONITORING.md` | Monitoring standards |
| `DEPLOYMENT.md`, `RELEASE.md` | Deployment/release procedures |

#### Architecture Standards
| File Pattern | What It Contains |
|-------------|-----------------|
| `ADR/`, `adr/`, `docs/decisions/` | Architecture Decision Records |
| `ARCHITECTURE.md` | Architecture overview |
| `API_STANDARDS.md`, `API_GUIDELINES.md` | API design standards |

### Step 2: Catalog Findings

For each file found, record:

```markdown
## Existing Standards Inventory

### Found Standards
| Category | File | Description | Last Modified |
|----------|------|-------------|---------------|
| Coding | .eslintrc.json | ESLint rules with Airbnb base | {date} |
| Coding | .prettierrc | Prettier formatting config | {date} |
| Security | SECURITY.md | Security reporting policy | {date} |
| Testing | jest.config.ts | Jest test configuration | {date} |
...

### Standards by Area
| SDLC Area | Standards Found | Coverage |
|-----------|----------------|----------|
| backend-development | .eslintrc, tsconfig.json | Partial |
| security | SECURITY.md | Minimal |
| quality-assurance | jest.config.ts | Partial |
| devops-infrastructure | (none) | None |
...
```

### Step 3: Identify Gaps

For each confirmed SDLC area, determine:

1. **Full coverage** — Comprehensive standards exist, no action needed
2. **Partial coverage** — Some standards exist but key areas are missing
3. **No coverage** — No standards found for this area

Produce a gap analysis:

```markdown
## Gap Analysis

### Areas with Standards
- backend-development — Linting and formatting covered via ESLint + Prettier
- quality-assurance — Test framework configured, but no test strategy document

### Areas Missing Standards
- devops-infrastructure — No deployment or infrastructure standards found
- security — Only a basic SECURITY.md, no threat model or security policy
- site-reliability — No runbooks, SLA, or monitoring standards
- architecture — No ADRs or architecture decision documentation
```

### Step 4: Present Findings to User

Present the inventory and gap analysis, then ask:

```
I've scanned your repository for existing standards. Here's what I found:

## Existing Standards
{inventory from Step 2}

## Gaps Identified
{gap analysis from Step 3}

Standards exist for: {list of areas with coverage}
Standards missing for: {list of areas without coverage}
Partial coverage for: {list of areas with partial coverage}

Would you like me to generate standards for any of the missing areas?
If yes, please specify:
1. Which areas to generate standards for
2. Scope: project-level (this repo only) or organization-level (meant to be shared)
3. Any specific preferences or constraints
```

Do NOT generate anything until the user responds.

### Step 5: Determine Scope

If the user requests standards generation, clarify scope:

| Scope | Characteristics |
|-------|----------------|
| **Project-level** | Specific to this repo, references actual patterns found, names specific tools and versions |
| **Organization-level** | More general, covers principles over tools, meant to apply across multiple repos |

### Step 6: Generate Missing Standards

For each requested area, generate a standards document:

#### Input Sources (in priority order)
1. **Codebase patterns** — What the team is actually doing (from brownfield analysis)
2. **Context documents** — Area-specific findings from Phase 3 (`docs/context/{area}.md`)
3. **Existing partial standards** — Extend rather than replace
4. **Industry best practices** — Fill gaps where no codebase pattern exists
5. **User preferences** — Any specific requirements stated by the user

#### Generation Rules
- Start from patterns already in the codebase — standards should codify existing good practices, not impose alien ones
- Use the tech stack identified in brownfield analysis — do not reference tools the team does not use
- Mark sections that are recommendations vs requirements
- Keep documents actionable — each standard should be verifiable
- Include rationale — explain WHY, not just WHAT
- Target 100-200 lines per standards document

#### Document Structure

Each generated standards document should follow this structure:

```markdown
# {Area} Standards

## Scope
{What this document covers and who it applies to}

## Core Principles
{3-5 guiding principles for this area}

## Standards

### {Category 1}
| Standard | Requirement Level | Rationale |
|----------|------------------|-----------|
| {standard} | MUST / SHOULD / MAY | {why} |
...

### {Category 2}
...

## Tooling
{Tools configured in this project that enforce these standards}

## Exceptions
{When and how to request exceptions to these standards}

## References
- {Link to context document}
- {Link to relevant external standards}
```

### Step 7: Save Output

Save generated standards to `docs/standards/{area}.md` in the target repository.

Do NOT overwrite any existing standards files found in Step 1. If a file already exists:
- Reference it from the new standards document
- Note any gaps in the existing file
- Suggest additions rather than replacements

---

## Output Artifacts

```
docs/standards/
├── coding.md                    # If coding standards gaps exist
├── testing.md                   # If testing standards gaps exist
├── security.md                  # If security standards gaps exist
├── operations.md                # If operations standards gaps exist
├── architecture.md              # If architecture standards gaps exist
├── delivery.md                  # If delivery standards gaps exist
├── product.md                   # If product standards gaps exist
└── standards-inventory.md       # Always generated — catalog of all found standards
```

The `standards-inventory.md` file is always generated as a reference to all existing and newly created standards.

---

## Verification Checklist

- [ ] All existing standards files in the repo have been identified
- [ ] Gap analysis covers every confirmed SDLC area
- [ ] User has been consulted before generating anything
- [ ] Generated standards reference actual codebase patterns
- [ ] No existing files have been overwritten
- [ ] Each generated document is 100-200 lines
- [ ] Standards use the project's actual tech stack and tools
- [ ] Requirement levels (MUST/SHOULD/MAY) are used consistently
- [ ] `standards-inventory.md` catalogs everything

---

## Related Resources

> **Workflow:** This is Phase 4 of [analyze-and-generate.md](analyze-and-generate.md).
> **Previous Phase:** Context documents from [generate-context-areas.md](generate-context-areas.md).
> **Next Phase:** IDE rules generation at [generate-ide-rules.md](generate-ide-rules.md).
> **Templates:** Standards templates at `templates/standards/`.
