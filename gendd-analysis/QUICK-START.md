# GenDD-Flow Quick Start

Copy-paste prompts for immediate use. See [README.md](README.md) for full documentation.

---

## Setup (One-Time)

Add both GenDD-Flow and your target repository to your AI IDE workspace.

**Usage pattern:**
```
Read @GenDD-Flow/workflows/{workflow}.md
Apply to @TargetRepo
```

---

## Quick Decision: What Do I Need?

| Situation | Use This |
|-----------|----------|
| **New repository** | [Full Analysis](#full-analysis-new-repos) |
| **Planned/new project (no code yet)** | [Greenfield Analysis](#greenfield-analysis-newplanned-project) |
| **Generate context + IDE rules** | [Full Analysis](#full-analysis-new-repos) |
| **Switch IDE or refresh rules** | [Generate IDE Rules](#generate-ide-rules) |
| **Need standards for any area** | [Generate Standards](#generate-standards) |
| **Enhance requirements** | [Story Quality](#story-quality) |
| **Find test gaps** | [Test Gaps](#test-gaps) |
| **Generate architecture diagrams** | [Architecture Diagrams](#architecture-diagrams) |
| **Update context after changes** | [Re-run Context](#re-run-context-for-specific-areas) |
| **Add missing SDLC area** | [Custom Area](#add-custom-sdlc-area) |
| **Refresh outdated context** | [Refresh Context](#refresh-context) |

---

## Core Workflows

### Full Analysis (New Repos)

The main entry point. Analyzes your codebase, detects applicable SDLC areas, generates context, checks standards, and creates IDE-specific rules.

```
Read @GenDD-Flow/workflows/analyze-and-generate.md

Analyze @TargetRepo and run the full GenDD-Flow pipeline:
1. Brownfield analysis (4-pass)
2. Detect applicable SDLC areas
3. Generate context per area
4. Check for standards gaps
5. Generate IDE rules for [Cursor / Claude Code / Antigravity / Copilot / Other]
```

**Time:** 2-4 hours (full analysis) | **Output:** `docs/context/`, `docs/standards/`, IDE rules

---

### Greenfield Analysis (New/Planned Project)

For projects that don't have an existing codebase yet. Create a project folder, add planning docs to `docs/specs/`, then run:

```
Read @GenDD-Flow/workflows/greenfield-analysis.md

Analyze the project specifications in @docs/specs/ and run the full
GenDD-Flow pipeline for this new project.

Generate context documents for all applicable SDLC areas.
```

If you don't have documents, describe the project directly:

```
Read @GenDD-Flow/workflows/greenfield-analysis.md

I'm planning a new project:
- **Name:** {name}
- **Tech stack:** {technologies}
- **Architecture:** {monolith/microservices/serverless/etc.}
- **Key services:** {list}

Analyze this specification and generate context documents for applicable
SDLC areas.
```

**Time:** 1-2 hours | **Output:** `docs/greenfield/`, `docs/context/`, `docs/standards/`, IDE rules

---

### Full Analysis (Existing Brownfield)

If you already have brownfield output from a previous run, skip Phase 1:

```
Read @GenDD-Flow/workflows/analyze-and-generate.md

Using the existing brownfield analysis in @TargetRepo/docs/brownfield/:
1. Skip Phase 1 (brownfield already exists)
2. Detect applicable SDLC areas
3. Generate context per area
4. Check for standards gaps
5. Generate IDE rules for [Cursor / Claude Code / Antigravity / Copilot / Other]
```

**Time:** 30-60 min

---

### Generate IDE Rules

Regenerate rules for a different IDE or refresh after format changes. Requires `docs/context/` to exist.

```
Read @GenDD-Flow/workflows/generate-ide-rules.md

Generate IDE-specific agent rules for @TargetRepo.

IDE: [Cursor / Claude Code / Antigravity / Copilot / Other]

Use the context areas in @TargetRepo/docs/context/ and standards in @TargetRepo/docs/standards/ as source material.
```

**Time:** 15-30 min | **Output:** IDE-specific rule files

---

### Generate Standards

Generate standards for any SDLC area — coding, product, delivery, testing, security, operations.

```
Read @GenDD-Flow/workflows/detect-and-generate-standards.md

Scan @TargetRepo for existing standards across all SDLC areas.
Report what exists and what's missing.

Then generate standards for: [coding / product / delivery / testing / security / operations / all]
Scope: [project / organization]
```

**Time:** 30-60 min | **Output:** `docs/standards/{area}.md`

---

### Story Quality (Shift-Left)

Transform vague requirements into detailed acceptance criteria.

```
Read @GenDD-Flow/workflows/enhance-acceptance-criteria.md

Transform this requirement into detailed acceptance criteria:
"""
[YOUR REQUIREMENT HERE]
"""

Context:
- Product: [PRODUCT NAME]
- User Persona: [USER TYPE]
- Multi-tenant: YES/NO
```

**Time:** 15 min | **Output:** Enhanced ACs in Gherkin format

---

### Test Gaps

Analyze test coverage and identify gaps.

```
Read @GenDD-Flow/workflows/identify-test-gaps.md

Analyze @TargetRepo for test coverage gaps:

Focus on:
1. Untested business logic
2. Missing error handling tests
3. Integration test coverage
4. Multi-tenant isolation tests (if applicable)

Generate remediation plan with priorities.
```

**Time:** 30-60 min | **Output:** Gap analysis with prioritized remediation plan

---

### Architecture Diagrams

Generate C4 model diagrams from codebase analysis.

```
Read @GenDD-Flow/workflows/generate-architecture-diagrams.md

Generate C4 architecture diagrams for @TargetRepo:

Project: [PROJECT NAME]
Tech Stack: [TECHNOLOGIES]

Generate:
1. Context Diagram (Level 1)
2. Container Diagram (Level 2)
3. Component Diagram (Level 3)
4. Deployment Diagram

Output as Mermaid diagrams.
Save to @TargetRepo/docs/architecture/
```

**Time:** 30-60 min | **Output:** Mermaid `.mmd` files

---

### Re-run Context for Specific Areas

After making changes to your project, regenerate context for affected areas only:

```
I've made changes to the project:
{describe what changed}

Using the existing analysis at @docs/brownfield/ and context at @docs/context/,
regenerate context documents for the affected areas only.

Affected areas: {list area names, or say "auto-detect"}
```

**Time:** 15-30 min | **Output:** Updated `docs/context/{area}.md` files

---

### Add Custom SDLC Area

Add an area that wasn't auto-detected:

```
I need to add a custom area that wasn't auto-detected:
- **Area name:** {name}
- **Why it applies:** {reasoning}

Generate a context document for this area using the template at
@GenDD-Flow/templates/context-area.md and save to @docs/context/{area-slug}.md
```

**Time:** 10-15 min | **Output:** `docs/context/{area-slug}.md`

---

### Refresh Context

Re-analyze after major changes (quarterly or after big features).

```
Read @GenDD-Flow/workflows/analyze-and-generate.md

Refresh the context for @TargetRepo:
1. Re-run brownfield analysis (or use existing if recent)
2. Re-detect SDLC areas (things may have changed)
3. Regenerate context per area
4. Update standards if needed
5. Regenerate IDE rules for [YOUR IDE]
```

**Time:** 1-2 hours

---

## On-Demand Playbooks

| Task | Playbook | Time |
|------|----------|------|
| Enhance requirements | `playbooks/on-demand/enhance-requirements.md` | 15m |
| Find test gaps | `playbooks/on-demand/identify-test-gaps.md` | 30-60m |
| Generate unit tests | `playbooks/on-demand/generate-unit-tests.md` | 30-60m |
| Generate integration tests | `playbooks/on-demand/generate-integration-tests.md` | 30-60m |
| E2E tests from live app | `playbooks/on-demand/run-assisted-testing.md` | 1-2h |
| Validate ACs against UI | `playbooks/on-demand/validate-acceptance-criteria.md` | 30m |
| Delta analysis (after PR) | `playbooks/on-demand/run-delta-analysis.md` | 15-30m |
| Database schema analysis | `playbooks/on-demand/analyze-database-schema.md` | 30-60m |
| CI/CD pipeline audit | `playbooks/on-demand/audit-ci-cd-pipeline.md` | 30-60m |
| Observability audit | `playbooks/on-demand/audit-observability.md` | 30-60m |
| UI patterns audit | `playbooks/on-demand/audit-ui-patterns.md` | 30-60m |
| Support documentation | `playbooks/on-demand/generate-support-documentation.md` | 1-2h |
| Generate IDE rules | `playbooks/on-demand/generate-ide-rules.md` | 15-30m |
| Generate standards | `playbooks/on-demand/generate-standards.md` | 30-60m |

---

## Reference Standards

Templates for standards and context generation:

| Template | Purpose |
|----------|---------|
| `templates/context-area.md` | Per-area context document structure |
| `templates/standards/*.md` | Standards templates (coding, product, delivery, testing, security, operations) |
| `templates/ide-rules/*.md` | IDE-specific rule file templates |
| `templates/requirements-enhancement.md` | AC rules and prompt templates |
| `templates/testing-standards.md` | MUST/SHOULD/MAY test requirements |

---

## Troubleshooting

### "Which workflow should I use?"

See [PLAYBOOK-GUIDE.md](playbooks/PLAYBOOK-GUIDE.md) for a decision tree.

### "Context window getting full?"

1. Run workflows in separate chat sessions per phase
2. Save outputs to `@TargetRepo/docs/`
3. Reference saved outputs in subsequent prompts

### "IDE rules look wrong?"

Run Phase 5 again — GenDD-Flow web searches for the latest IDE format. If offline, it uses baseline snapshots from `knowledge/ide-formats/`.

---

## Quick Reference Table

| Task | Workflow | Time |
|------|----------|------|
| Full analysis (new repo) | `workflows/analyze-and-generate.md` | 2-4h |
| Full analysis (existing brownfield) | `workflows/analyze-and-generate.md` (skip Phase 1) | 30-60m |
| Generate IDE rules only | `workflows/generate-ide-rules.md` | 15-30m |
| Generate standards | `workflows/detect-and-generate-standards.md` | 30-60m |
| Enhance requirements | `workflows/enhance-acceptance-criteria.md` | 15m |
| Find test gaps | `workflows/identify-test-gaps.md` | 30-60m |
| Generate C4 diagrams | `workflows/generate-architecture-diagrams.md` | 30-60m |
| Update docs after changes | `workflows/incremental-doc-update.md` | 15-30m |
| Refresh context areas | Recurring: `playbooks/recurring/refresh-context-areas.md` | 1-2h |
