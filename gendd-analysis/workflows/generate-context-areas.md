# Workflow: Generate Context Areas

## Quick Start

```
Read @GenDD-Flow/workflows/generate-context-areas.md

Using the confirmed SDLC areas and the brownfield analysis at @docs/brownfield/,
generate context documents for each applicable area.

Confirmed areas:
- architecture (HIGH)
- backend-development (HIGH)
- database-management (HIGH)
- quality-assurance (HIGH)
- security (MEDIUM)
- technical-leadership (BASELINE)
```

## Overview

This workflow is **Phase 3** of the Analyze & Generate flow. It takes the confirmed list of SDLC areas from Phase 2 (Role Detector) and generates a focused context document for each area, grounded in the brownfield analysis findings and direct codebase evidence.

Each context document captures how a specific SDLC area applies to **this** codebase — not generic best practices, but concrete, project-specific guidance that an AI assistant can use when working in that area.

## Prerequisites

### Brownfield Prerequisites
- Completed Phase 1: Brownfield analysis at `docs/brownfield/`
- Completed Phase 2: Confirmed SDLC area list from role-detector-agent
- Access to the target codebase
- SDLC area knowledge files at `knowledge/sdlc-areas/`
- Context area template at `templates/context-area.md`

### Greenfield Prerequisites

For greenfield projects, the prerequisites are:
- Project folder created with planning documents in `docs/specs/`
- Completed greenfield analysis (`docs/greenfield/inference-result.md`)
- Inference result with suggestedAreas
- Confirmed SDLC area list (from role-detector with user confirmation)
- SDLC area knowledge files at `knowledge/sdlc-areas/`
- Context area template at `templates/context-area.md`

Note: Greenfield context documents reference planned files and architecture
rather than existing code. The same template structure applies, but sections
like "Current State Assessment" describe what is planned rather than what exists.

---

## User Modifications to Area List

Before generating context documents, the user may have:

1. **Toggled areas off** — Excluded from generation. Do not generate context
   for excluded areas.
2. **Added custom areas** — Areas not in the 16 standard set. These have
   confidence: MANUAL and signal: "Added manually by user". Generate context
   using the general template structure (no knowledge file exists for custom areas).
3. **Edited area names or descriptions** — Use the user-provided name and
   description. The areaId may not match AREA_NAMES for custom areas.
4. **Removed areas** — Completely deleted from the list. Do not generate.

Always respect the user's final area list as-is.

---

## Context Documents vs Standards Boundary

Context documents and coding standards are complementary, never overlapping:

- **Standards (Phase 4):** Prescriptive rules — "you MUST do X." Coding
  conventions, naming rules, formatting, testing requirements, security policies.
- **Context documents (this phase):** Descriptive state — "this project uses X,
  located at Y." Project-specific state, risks, file references, navigation guidance.

The AI Agent Guidelines section in context docs is scoped to navigation and
safety ("always check X before modifying Y"), NOT style or convention rules.
Standards handle those.

---

## Re-running Context Generation

Context can be regenerated for specific areas without re-running the full analysis:

**Describe a Change (fast):**
- User describes what changed (e.g., "Switched from Tailwind to shadcn")
- System identifies affected areas
- Regenerates context only for selected areas
- Change description is injected into the LLM prompt as additional context

**Re-scan Repository (brownfield only):**
- Re-runs full scan and inference
- Re-detects areas (may find new ones or change confidence)
- User confirms which areas to regenerate
- Regenerates selected area context documents

In both cases:
- Untouched areas keep their existing context documents
- Only selected areas are regenerated
- The context/README.md is always regenerated to reflect current state

---

## Process

### Step 1: Prepare Area Queue

Take the confirmed area list from Phase 2 and sort by generation order:

1. **BASELINE areas first** — `technical-leadership`, `architecture`
2. **HIGH confidence areas** — In dependency order (e.g., `backend-development` before `quality-assurance` since QA references backend patterns)
3. **MEDIUM confidence areas** — These can cross-reference HIGH areas
4. **LOW confidence areas** — Generated last, may reference all others

This ordering matters because later documents can reference earlier ones.

### Step 2: Generate Each Context Document

For each area in the queue:

#### 2a. Load the Analysis Framework

```
Read @GenDD-Flow/knowledge/sdlc-areas/{area}.md
```

This file defines:
- What aspects of the codebase to examine for this area
- What questions to answer
- What patterns to look for
- What the context document should cover

#### 2b. Apply Framework to Codebase

Using the brownfield analysis and direct codebase access:

1. Answer the framework questions with evidence from this specific codebase
2. Identify patterns, conventions, and decisions relevant to this area
3. Note gaps, risks, and areas of concern
4. Collect file references (not code snippets) as evidence

#### 2c. Generate Context Document

```
Read @GenDD-Flow/templates/context-area.md
```

Use the template structure to produce the context document. Fill each section with project-specific content derived from step 2b.

#### 2d. Save Output

Save to `docs/context/{area}.md` in the target repository.

### Step 3: Cross-Reference Pass

After all individual documents are generated, do a cross-reference pass:

1. Check that references between areas are consistent
2. Ensure no contradictions between documents
3. Verify that shared concepts (e.g., authentication) are described consistently
4. Add cross-references where one area's context informs another

---

## Content Guidelines

### Confidence-Driven Depth

The confidence level from Phase 2 determines how detailed each context document should be:

| Confidence | Document Depth | Target Length |
|------------|---------------|---------------|
| HIGH | Full detail — specific patterns, file references, conventions, risks | 150-200 lines |
| MEDIUM | Moderate detail — known patterns, key references, open questions | 100-150 lines |
| LOW | High-level only — general observations, minimal specifics | 50-100 lines |
| BASELINE | Standard template with project-specific customization | 100-150 lines |
| MANUAL | User-added area — generate based on available evidence and user description | 100-150 lines |

### Documentation Rules

Follow these rules for all context documents:

- **Reference files, not snippets** — Write `Authentication middleware: middleware/auth.ts` not embedded code blocks
- **Describe patterns, not counts** — Write "Services follow controller-service-repository pattern" not "47 services found"
- **Be specific to this codebase** — Every statement should be verifiable against the actual code
- **Mark uncertainties** — If something was inferred but not confirmed, say so
- **Include actionable guidance** — An AI reading this document should know how to work in this area

### File Size Limits

Each context document should be **150-200 lines** for HIGH confidence areas. This is not arbitrary:
- Under 100 lines: Likely too shallow to be useful
- 150-200 lines: Enough detail to guide AI behavior without overwhelming context windows
- Over 250 lines: Too long — consider splitting the area or removing generic content

### What to Include

For each context document:

| Section | Content |
|---------|---------|
| Purpose | What this area covers in the context of this project |
| Current State | How the codebase currently handles this area |
| Key Patterns | Conventions, patterns, and approaches used |
| File References | Important files, directories, and configurations |
| Constraints | Rules, limitations, and non-negotiables |
| Risks | Known issues, tech debt, and areas of concern |
| Cross-References | Links to related context areas |

### What NOT to Include

- Generic best practices not specific to this codebase
- Code snippets (reference files instead)
- Historical context unless it impacts current decisions
- Aspirational content ("we should do X") — focus on what IS, not what should be
- Duplicate content already covered in another area's document

---

## Handling Edge Cases

### Area with Minimal Evidence

If a confirmed area has very little evidence in the brownfield output:

1. Generate a shorter document (50-100 lines)
2. Focus on what IS known
3. Include a "Gaps" section listing what could not be determined
4. Suggest the user provide additional context

### Overlapping Areas

Some areas naturally overlap (e.g., `backend-development` and `architecture`):

1. Each document should have its own focus
2. Use cross-references rather than duplicating content
3. Architecture focuses on system-level decisions; backend focuses on implementation patterns

### Custom Areas from Phase 2

For custom areas suggested by the role-detector and confirmed by the user:

1. There will be no `knowledge/sdlc-areas/{custom-area}.md` file
2. Use the general template structure from `templates/context-area.md`
3. Draw content from brownfield findings related to the custom area
4. Be explicit that this is a custom area not part of the standard 16

---

## Output Artifacts

After completing this workflow, the target repo should contain:

```
docs/context/
├── technical-leadership.md      # BASELINE
├── architecture.md              # BASELINE / HIGH
├── backend-development.md       # HIGH (if applicable)
├── frontend-development.md      # HIGH (if applicable)
├── database-management.md       # HIGH (if applicable)
├── quality-assurance.md         # HIGH (if applicable)
├── security.md                  # HIGH/MEDIUM (if applicable)
├── devops-infrastructure.md     # HIGH (if applicable)
├── site-reliability.md          # MEDIUM (if applicable)
├── technical-writing.md         # MEDIUM (if applicable)
├── release-management.md        # MEDIUM (if applicable)
├── user-experience.md           # HIGH/MEDIUM (if applicable)
├── product-management.md        # LOW (if applicable)
├── fullstack-development.md     # HIGH (if applicable)
└── {custom-area}.md             # If custom areas were confirmed
```

Only areas confirmed in Phase 2 will have documents generated. Not all 16 standard areas will be present for every codebase.

---

## Verification Checklist

After generating all context documents:

- [ ] Every confirmed area has a corresponding `docs/context/{area}.md` file
- [ ] Each document follows the template structure
- [ ] File references point to actual files in the codebase
- [ ] No code snippets embedded (file references only)
- [ ] Document lengths are within guidelines for their confidence level
- [ ] Cross-references between documents are consistent
- [ ] No contradictions between area documents
- [ ] BASELINE areas include project-specific content, not just generic templates

---

## Example: Generating backend-development Context

Given brownfield output showing:
- Express.js REST API with 12 route files
- Controller-Service-Repository pattern
- JWT authentication middleware
- PostgreSQL via Prisma ORM

The generated `docs/context/backend-development.md` would include:
- API framework: Express.js with route-level middleware
- Pattern: Controller delegates to Service, Service uses Repository
- Auth: JWT validation in `middleware/auth.ts`, applied to all `/api/*` routes
- ORM: Prisma with migrations in `prisma/migrations/`
- Error handling: Centralized error handler in `middleware/errorHandler.ts`
- Validation: Zod schemas co-located with route handlers

All as file references, not code blocks.

---

## Related Resources

> **Workflow:** This is Phase 3 of [analyze-and-generate.md](analyze-and-generate.md).
> **Agent:** Areas determined by [pass5-role-detector-agent.md](../agents/pass5-role-detector-agent.md) in Phase 2.
> **Knowledge:** Area frameworks at `knowledge/sdlc-areas/`.
> **Templates:** Document structure at `templates/context-area.md`.
> **Next Phase:** Standards detection at [detect-and-generate-standards.md](detect-and-generate-standards.md).
