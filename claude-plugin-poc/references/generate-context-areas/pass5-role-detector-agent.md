# Pass 5: SDLC Role Detector

## Mission

This pass runs **immediately after Pass 4 (Documentation)** for brownfield projects, or after greenfield analysis for new projects. Analyze the inference output and any available scan data to determine which SDLC areas apply. The primary detection mechanism is LLM-suggested areas from the inference step, supplemented by structural signals. Produce an ordered list of applicable areas with confidence levels, suggest custom areas where needed, and present findings for human confirmation before proceeding.

You must produce an **SDLC area map** that drives context generation, standards detection, and IDE rules generation in the subsequent phases.

## Output Guidelines

**Reference:** `templates/documentation-guidelines.md`

### Key Rules
- **Evidence-based** - Every area determination must cite specific files, patterns, or findings from brownfield output
- **Reference files** - "CI/CD detected: `.github/workflows/deploy.yml`" not embedded pipeline contents
- **Confidence-driven** - Use HIGH / MEDIUM / LOW / BASELINE to rank each area
- **No assumptions** - If evidence is ambiguous, downgrade confidence rather than guessing

## Input

### Brownfield Projects
Analysis documentation produced by Passes 1-4:
- `docs/brownfield/pass1-scan-findings.md` — Repository inventory, layout, entry points
- `docs/brownfield/pass2-infer-findings.md` — Architecture hypotheses, flows, data ownership (includes `suggestedAreas`)
- `docs/brownfield/pass3-validation-responses.md` — Human-confirmed findings
- `docs/brownfield/gendd/**/*.md` — Documentation pack from Pass 4 (System Summary, Tech Stack, Architecture, Components, Data Ownership, Risks, Open Questions, Onboarding, Flows; includes `suggestedAreas`)

### Greenfield Projects
Inference result from greenfield analysis:
- `docs/greenfield/inference-result.md` — produced from documents in `docs/specs/`
- Includes `suggestedAreas`
- No scan output available — structural signals will be empty

In both cases, the critical input is the `suggestedAreas` field from the inference step.

## Detection Hierarchy

Area detection uses three sources, in priority order:

### 1. LLM Suggestions (Primary)

The inference step (Pass 2 or Pass 4) now includes `suggestedAreas` in its output.
Each suggestion has an areaId, confidence level (high/medium/low), and reasoning.

Map LLM confidence to detection confidence:
- "high" → HIGH
- "medium" → MEDIUM
- "low" → LOW

For each valid suggestion (areaId matches one of the 16 standard areas),
add the area with its mapped confidence and reasoning as the signal.

Invalid areaIds (not in the 16 standard areas) are silently ignored.

### 2. Structural Signals (Supplementary)

These are factual file-existence checks from the scan output.
They supplement LLM suggestions but do not replace them.

| Signal | Area | Confidence |
|--------|------|------------|
| Docker detected | devops-infrastructure | HIGH |
| Kubernetes detected | devops-infrastructure | HIGH |
| CI/CD configs present | devops-infrastructure | HIGH |
| IaC files present | devops-infrastructure | HIGH |
| Database migrations exist | database-management | HIGH |
| ORM models detected | database-management | HIGH |
| Database schemas found | database-management | MEDIUM |
| Event brokers configured | architecture | HIGH |
| Event topics defined | architecture | HIGH |

### 3. Baseline Areas (Always Included)

These areas are always included regardless of detection:
- `architecture` — every codebase has architecture decisions
- `technical-leadership` — every codebase benefits from leadership context

If already detected at a higher confidence, keep the higher confidence.
Otherwise, add at BASELINE confidence.

### Confidence Ranking

When an area is triggered by multiple sources, keep the highest confidence:

HIGH > MEDIUM > LOW > BASELINE > MANUAL

MANUAL is reserved for areas added by the user (not detected).

### Deduplication

If the same area appears from multiple sources:
- Keep the highest confidence level
- Collect ALL signals (from every source that triggered it)

### Greenfield Projects

For greenfield (planned) projects, structural signals will be empty since there
is no codebase to scan. Area detection relies entirely on:
1. LLM suggestions from the inference step (based on tech stack, architecture,
   and requirements specified by the user)
2. Baseline areas

This is expected and correct — the LLM has already analyzed the project
specifications and can suggest areas accurately from planning documents.

## Detection Process

### Step 1: Parse Brownfield Output
Read all available brownfield analysis documents. Extract:
- Technologies identified (from Repo Inventory)
- File patterns found (from Layout Map)
- Entry points detected (from Entry Points List)
- Dependencies cataloged (from Dependency Graph)
- Infrastructure identified (from Build + Run Book)
- Event patterns (from Event Surface Summary)

### Step 2: Apply Detection Hierarchy
For each source in the detection hierarchy:
1. Process LLM suggestions from inference output (primary source)
2. Check structural signals from scan output (supplementary)
3. Add baseline areas
4. Collect evidence (file paths, config names, technology references, LLM reasoning)

### Step 3: Aggregate and Deduplicate
- If an area is triggered multiple times, use the highest confidence level
- Collect all evidence across triggers for the same area
- Count the number of distinct signals per area (more signals = stronger case)

### Step 4: Identify Custom Areas
Look for patterns not covered by the standard 16 areas:
- Domain-specific tooling (ML pipelines, data engineering, embedded systems)
- Specialized integrations (payment processing, healthcare compliance, real-time systems)
- Uncommon architecture patterns (CQRS, saga orchestration, cell-based architecture)

### Step 5: Determine Exclusions
For each of the 16 standard areas NOT triggered:
- Confirm absence of signals
- Provide reasoning for exclusion
- Note if the area might become relevant later

## Output Format

```markdown
## Applicable SDLC Areas

### Analysis Summary
- **Brownfield passes analyzed:** {Pass 1, Pass 2, Pass 3, Pass 4}
- **Total signals detected:** {count}
- **Areas identified:** {count} of 16 standard + {count} custom

### Required (HIGH confidence)
1. architecture — {evidence summary}
2. backend-development — {evidence summary}
3. database-management — {evidence summary}
...

### Recommended (MEDIUM confidence)
1. site-reliability — {evidence summary}
2. technical-writing — {evidence summary}
...

### Optional (LOW confidence)
1. product-management — {evidence summary}
...

### Baseline (Always Included)
1. technical-leadership — Included for all codebases
2. architecture — Included for all codebases (may also appear in Required)

### Suggested Custom Areas
- {custom-area-name} — {evidence and reasoning}
...

### Excluded Areas (with reasoning)
- {area-name} — {why it does not apply to this codebase}
...
```

## Human-in-the-Loop Validation

After generating the area map, present it to the user for confirmation:

```
I've analyzed the brownfield output and identified the following SDLC areas
for your codebase. Please review and adjust:

{Output from above}

Questions:
1. Are there any areas I've marked as Required that you'd like to remove?
2. Are there any Recommended/Optional areas you'd like to upgrade to Required?
3. Are there SDLC concerns specific to your project not captured above?
4. Any excluded areas that should actually be included?

Please confirm or adjust, and I'll proceed to generate context documents
for the confirmed areas.
```

Do NOT proceed to context generation until the user has confirmed the area selection.

## Rules

1. **Do NOT fabricate signals** - Only cite evidence actually present in brownfield output
2. **BASELINE areas are non-negotiable** - technical-leadership and architecture are always included unless the user explicitly removes them
3. **Confidence levels drive depth** - HIGH areas get full context documents; LOW areas get lighter treatment
4. **Custom areas are suggestions** - Always explain why and let the user decide
5. **Wait for confirmation** - The HITL step is mandatory, not optional

## Example Prompt

```
Read @GenDD-Flow/agents/pass5-role-detector-agent.md

Using the brownfield analysis output at @TargetRepo/docs/brownfield/,
determine which SDLC areas apply to this codebase.

Present the area map with confidence levels and evidence,
then wait for my confirmation before proceeding.
```

## Next Steps: After User Confirms Areas

Once the user confirms the SDLC area map, continue through the remaining phases:

1. **Generate context per area** → `workflows/generate-context-areas.md`
2. **Detect & generate standards** → `workflows/detect-and-generate-standards.md`
3. **Generate IDE rules** → `workflows/generate-ide-rules.md`

## Related Resources

> **Previous pass:** See [pass4-document-agent.md](pass4-document-agent.md) — produces the documentation pack this agent reads.
> **Workflow:** See [analyze-and-generate.md](../workflows/analyze-and-generate.md) for the full orchestration flow.
> **Knowledge:** SDLC area definitions live in `knowledge/sdlc-areas/` — each area file describes what to look for and how to document it.
> **Templates:** Context documents are generated using `templates/context-area.md` as structure.
