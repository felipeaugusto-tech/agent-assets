# Workflow: Analyze & Generate

## Quick Start

Copy-paste this prompt into any AI IDE to run the full flow:

```
Read @GenDD-Flow/workflows/analyze-and-generate.md

Analyze @TargetRepo using the GenDD-Flow Analyze & Generate workflow.

Start from Phase 1 (or skip to Phase 2 if brownfield analysis already exists
at @docs/brownfield/).

Walk me through each phase, waiting for my confirmation at each gate
before proceeding to the next.
```

## Overview

This is the **main entry point** for GenDD-Flow. It replaces the old playbook-based approach with a streamlined 5-phase flow that analyzes any codebase and generates tailored context documents, standards, and IDE rules.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      ANALYZE & GENERATE FLOW                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   Phase 1              Phase 2              Phase 3                     │
│   ANALYZE CODEBASE     DETERMINE AREAS      GENERATE CONTEXT            │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐           │
│   │ 4-Pass       │────▶│ Role         │────▶│ Per-Area     │           │
│   │ Brownfield   │     │ Detector     │     │ Context      │           │
│   │ Analysis     │     │ Agent        │     │ Documents    │           │
│   └──────────────┘     └──────────────┘     └──────────────┘           │
│                              │ HITL              │                       │
│                              │ Gate              │                       │
│                              ▼                   ▼                       │
│                                                                          │
│   Phase 4              Phase 5                                          │
│   CHECK STANDARDS      GENERATE IDE RULES                               │
│   ┌──────────────┐     ┌──────────────┐                                │
│   │ Detect       │────▶│ Web Search   │                                │
│   │ Existing +   │     │ Format +     │                                │
│   │ Fill Gaps    │     │ Generate     │                                │
│   └──────────────┘     └──────────────┘                                │
│        │ HITL                │                                           │
│        │ Gate                ▼                                           │
│        ▼              ┌──────────────┐                                  │
│                       │ TARGET REPO  │                                  │
│                       │ Ready for    │                                  │
│                       │ AI-Assisted  │                                  │
│                       │ Development  │                                  │
│                       └──────────────┘                                  │
└─────────────────────────────────────────────────────────────────────────┘
```

## Prerequisites

- Access to the target codebase
- AI IDE with file reading capability (Cursor, Claude Code, Copilot, etc.)
- AI IDE with web search capability (for Phase 5 — IDE rules generation)
- 2-4 hours for full flow (can be paused between phases)

## Phase 1: Analyze Codebase

**Purpose:** Build a comprehensive understanding of the repository through systematic analysis.

**Reference:** `workflows/brownfield-repository-analysis.md`

### For New Repos (no existing analysis)

Run the full 4-pass brownfield analysis:

```
Read @GenDD-Flow/workflows/brownfield-repository-analysis.md

Analyze @TargetRepo using the brownfield repository analysis workflow.
Start with Pass 1: Scan and proceed through all 4 passes.
```

This produces:
- `docs/brownfield/pass1-scan-findings.md`
- `docs/brownfield/pass2-infer-findings.md`
- `docs/brownfield/pass3-validation-responses.md`
- `docs/brownfield/gendd/` (documentation pack — see `gendd/README.md`)

### For Repos with Existing Analysis

If brownfield output already exists at `docs/brownfield/`, skip directly to Phase 2:

```
Brownfield analysis already exists at @docs/brownfield/.
Skip to Phase 2: Determine SDLC Areas.
```

### Phase 1 Gate
- [ ] At minimum, Pass 1 (Scan) and Pass 2 (Infer) are complete
- [ ] Repo inventory identifies languages, frameworks, and infrastructure
- [ ] Entry points and service boundaries are mapped

---

## Phase 2: Determine Applicable SDLC Areas

**Agent:** `agents/pass5-role-detector-agent.md`

The inference output from Phase 1 (or greenfield analysis) now includes
`suggestedAreas` — LLM-suggested SDLC areas with confidence and reasoning.

The role detector merges:
1. LLM suggestions from inference (primary)
2. Structural signals from scan (supplementary)
3. Baseline areas (always included)

### Invoke

```
Read @GenDD-Flow/agents/pass5-role-detector-agent.md

Using the brownfield analysis output at @docs/brownfield/,
determine which SDLC areas apply to this codebase.

Present the area map with confidence levels and evidence,
then wait for my confirmation before proceeding.
```

### What Happens

1. Agent reads inference output and extracts `suggestedAreas` (primary detection)
2. Checks structural signals from scan output (supplementary)
3. Adds baseline areas (architecture, technical-leadership)
4. Deduplicates and keeps highest confidence per area
5. Identifies areas not in the standard 16 that might apply
6. Presents findings for **human confirmation** (mandatory gate)

**HITL Gate:** Present detected areas to user for confirmation.
User can:
- Confirm or exclude areas
- Add custom areas not in the standard 16
- Edit area names and descriptions
- Remove areas entirely

Do NOT proceed to Phase 3 until user confirms.

### Phase 2 Gate (HITL — Mandatory)
- [ ] User has reviewed the area map
- [ ] User has confirmed, added, or removed areas
- [ ] Final area list is agreed upon before proceeding

---

## Phase 3: Generate Context Per Area

**Purpose:** For each confirmed SDLC area, generate a context document that captures how that area applies to this specific codebase.

**Reference:** `workflows/generate-context-areas.md`

### Invoke

```
Read @GenDD-Flow/workflows/generate-context-areas.md

Using the confirmed SDLC areas from Phase 2 and the brownfield analysis
at @docs/brownfield/, generate context documents for each area.

Confirmed areas:
{paste confirmed area list from Phase 2}
```

### What Happens

1. For each confirmed area, loads the analysis framework from `knowledge/sdlc-areas/{area}.md`
2. Applies the framework against the codebase and brownfield findings
3. Generates a context document using `templates/context-area.md` as structure
4. Saves each document to `docs/context/{area}.md` in the target repo

### Phase 3 Gate
- [ ] Context document exists for every confirmed area
- [ ] Each document is 150-200 lines (not bloated, not sparse)
- [ ] Cross-references between areas are consistent
- [ ] HIGH confidence areas have detailed, specific content
- [ ] LOW confidence areas have high-level guidance

---

## Phase 4: Check & Generate Standards

**Purpose:** Detect existing standards in the codebase, identify gaps, and offer to generate missing standards documents.

**Reference:** `workflows/detect-and-generate-standards.md`

### Invoke

```
Read @GenDD-Flow/workflows/detect-and-generate-standards.md

Scan @TargetRepo for existing standards and conventions.
Compare against the SDLC areas confirmed in Phase 2.
Identify gaps and present findings.
```

### What Happens

1. Scans for existing standards files (`.editorconfig`, `CONTRIBUTING.md`, `SECURITY.md`, etc.)
2. Summarizes what already exists
3. Identifies which confirmed areas lack standards
4. Presents gap analysis to user
5. If user requests, generates missing standards using brownfield analysis + best practices

### Phase 4 Gate (HITL — Optional but Recommended)
- [ ] Existing standards have been cataloged
- [ ] Gaps have been identified
- [ ] User has decided which gaps to fill
- [ ] Generated standards reflect actual codebase patterns

---

## Phase 5: Generate IDE Rules

**Purpose:** Transform context documents and standards into IDE-native rule files that guide AI assistants during development.

**Reference:** `workflows/generate-ide-rules.md`

### Invoke

```
Read @GenDD-Flow/workflows/generate-ide-rules.md

Using the context documents at @docs/context/ and standards at @docs/standards/,
generate IDE rules for my development environment.
```

### What Happens

1. Asks which IDE the user works with
2. Web searches for the latest IDE rule format (to avoid outdated formats)
3. Transforms context and standards into IDE-native rule files
4. Generates files in the correct location for the chosen IDE

### Phase 5 Gate
- [ ] IDE rules generated in correct format and location
- [ ] Rules cover: general project identity, coding standards, testing, and major SDLC areas
- [ ] User can verify by starting a new AI chat session

---

## Greenfield Flow

For greenfield projects (no existing codebase):
- User creates a project folder and places planning documents in `docs/specs/`
- Phase 1 is replaced by greenfield specification analysis — see `workflows/greenfield-analysis.md`
- Phase 2 works identically — LLM suggestions from greenfield inference
- Phase 3 generates context referencing planned architecture, not existing code
- Phase 4 generates standards based on planned tech stack and patterns
- Phase 5 generates IDE rules from context + standards (identical)

---

## Re-running After Changes

When the project evolves, users can re-run context generation without
repeating the full 5-phase flow:

**Option A: Describe a Change**
- Fast — no scan or inference needed
- User describes what changed
- System regenerates context for affected areas only

**Option B: Re-scan Repository** (brownfield only)
- Re-runs scan + inference
- Re-detects areas with potentially new results
- User selects which areas to regenerate

Both options preserve untouched area context documents.

---

## Output Summary

After running the full Analyze & Generate flow, the target repo will contain:

```
target-repo/
├── docs/
│   ├── brownfield/                          # Phase 1 output
│   │   ├── pass1-scan-findings.md
│   │   ├── pass2-infer-findings.md
│   │   ├── pass3-validation-responses.md
│   │   └── gendd/                        # Pass 4 documentation pack
│   │       ├── README.md
│   │       ├── stack.json
│   │       ├── overview/
│   │       ├── architecture/
│   │       ├── risks/
│   │       ├── onboarding/
│   │       └── flows/
│   │
│   ├── context/                             # Phase 3 output
│   │   ├── architecture.md
│   │   ├── backend-development.md
│   │   ├── frontend-development.md
│   │   ├── database-management.md
│   │   ├── quality-assurance.md
│   │   ├── security.md
│   │   ├── technical-leadership.md
│   │   └── {other-applicable-areas}.md
│   │
│   └── standards/                           # Phase 4 output
│       ├── coding.md
│       ├── testing.md
│       ├── security.md
│       └── {other-applicable-areas}.md
│
├── .cursor/rules/*.mdc                      # Phase 5 output (Cursor)
├── CLAUDE.md                                # Phase 5 output (Claude Code)
├── GEMINI.md                                # Phase 5 output (Antigravity)
└── .github/copilot-instructions.md          # Phase 5 output (Copilot)
```

Note: Only the IDE rules for the user's chosen IDE will be generated. The listing above shows all possible outputs.

---

## Time Estimates

| Phase | Effort | Dependencies |
|-------|--------|--------------|
| Phase 1: Analyze Codebase | 1-2 hours | Repository access, human validator |
| Phase 2: Determine SDLC Areas | 10-15 min | Phase 1 complete |
| Phase 3: Generate Context | 30-60 min | Phase 2 confirmed |
| Phase 4: Check Standards | 20-40 min | Phase 3 complete |
| Phase 5: Generate IDE Rules | 15-30 min | Phase 4 complete, web access |

**Total:** 2-4 hours for complete flow (can be paused between phases)

---

## Skip Conditions

| Phase | Can Skip? | When |
|-------|-----------|------|
| Phase 1 | Yes | Brownfield analysis already exists at `docs/brownfield/` |
| Phase 2 | No | Area detection is always required |
| Phase 3 | No | Context generation is the core deliverable |
| Phase 4 | Yes | If standards are not needed or already exist |
| Phase 5 | Yes | If IDE rules are not needed or will be done manually |

---

## Tips for Best Results

### Start with Good Brownfield Output
Phase 1 quality drives everything downstream. Take time to validate findings in Pass 3.

### Be Honest at HITL Gates
If an area does not apply, remove it. If something is missing, add it. The AI cannot know your team's priorities without your input.

### Iterate Rather Than Perfect
Run the full flow once, review outputs, then re-run specific phases to refine. It is faster than trying to get everything perfect in one pass.

### Keep Context Documents Focused
Each context document should be 150-200 lines. If it is longer, the area may need splitting. If shorter, it may need merging with a related area.

---

## Related Resources

- **Brownfield Analysis:** `workflows/brownfield-repository-analysis.md`
- **Role Detection:** `agents/pass5-role-detector-agent.md`
- **Context Generation:** `workflows/generate-context-areas.md`
- **Standards Detection:** `workflows/detect-and-generate-standards.md`
- **IDE Rules:** `workflows/generate-ide-rules.md`
- **SDLC Area Definitions:** `knowledge/sdlc-areas/`
- **Templates:** `templates/context-area.md`, `templates/standards/`
