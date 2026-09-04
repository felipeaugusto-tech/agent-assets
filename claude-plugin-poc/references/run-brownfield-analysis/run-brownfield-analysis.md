# Run Brownfield Analysis

| Field | Value |
|-------|-------|
| **Category** | onboarding |
| **Target Roles** | Architect, Tech Lead, Backend Dev, Frontend Dev, Fullstack Dev, Engineering Manager |
| **Prerequisites** | Repository cloned locally, GenDD-Flow repo available, ability to build/run the project |
| **Inputs** | Path to the target repository (`@TargetRepo`) |
| **Outputs** | 4-pass brownfield analysis: scan findings, architecture inferences, validation packet, system documentation |

## When to Use

- You are onboarding onto an existing codebase for the first time
- Your team is adopting GenDD-Flow on a repository and needs a structured baseline
- A significant portion of the system is undocumented and you need to build understanding from code

## Before You Start

- [ ] Target repository is cloned and accessible locally
- [ ] You can build and run the project (or at least read the build config)
- [ ] GenDD-Flow repo is available at a known path
- [ ] You have access to CI/CD configuration (for operational context)
- [ ] Identify project size: **small/medium** (< 100 files) or **large** (100+ files)

## Steps

### Step 1: Determine your approach

- Do: Decide whether to run all 4 passes in a single session or split across sessions
- How: Check file count and complexity. If 100+ files or you expect context window pressure, use the multi-phase approach (separate chat sessions per pass)
- Expect: A decision — single session vs. multi-phase

> **Large projects (100+ files):** Use separate chat sessions per pass:
> - **Phase 1 Chat:** Run Pass 1 only, save to `pass1-scan-findings.md`
> - **Phase 2 Chat:** Read Pass 1 output, run Pass 2 only
> - **Phase 3+ Chat:** Continue with Pass 3-4

**Documentation Rules:**
- Do NOT embed code snippets (they get stale)
- DO reference files: `Services/PaymentService.cs:ProcessPayment()`
- Do NOT use hard-coded counts ("15 services")
- DO use patterns: "Services matching `*Service.cs`"
- Do NOT repeat information across files
- DO cross-reference: "See [Risk Hotspots](../risks/...)"

### Step 2: Run Pass 1 — Scan

- Do: Generate a raw inventory of the repository
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/agents/pass1-scan-agent.md
  Read @GenDD-Flow/templates/documentation-guidelines.md

  Analyze @TargetRepo and perform Pass 1: Scan.

  Generate:
  1. Repo Inventory (use patterns, not hard-coded counts)
  2. Layout Map (directory structure with purposes)
  3. Build + Run Book (commands to build/run)
  4. Entry Points List (APIs, workers, CLIs)
  5. Dependency Graph Summary (key edges only)
  6. Event Surface Summary (queues, topics)
  7. Open Questions for Pass 2

  Save to @TargetRepo/docs/brownfield/pass1-scan-findings.md
  ```
- Expect: `pass1-scan-findings.md` with a complete inventory. No analysis yet — just facts.

**Review checkpoint:** Verify all services and modules were identified before proceeding.

### Step 3: Run Pass 2 — Infer

- Do: Generate architecture hypotheses from the scan
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/agents/pass2-infer-agent.md
  Read @GenDD-Flow/templates/documentation-guidelines.md

  Using Pass 1 findings at @TargetRepo/docs/brownfield/pass1-scan-findings.md,
  perform Pass 2: Infer.

  Generate:
  1. Architecture Hypotheses (with confidence levels)
  2. Service/Module Catalog (file references, not code)
  3. Core Flows (2+ request, 2+ async) - step references
  4. Data Map (ownership, not schemas)
  5. Operational Model (how it runs)
  6. Risk Hotspots (prioritized)
  7. Human Validation Questions

  Save to @TargetRepo/docs/brownfield/pass2-infer-findings.md
  ```
- Expect: `pass2-infer-findings.md` with hypotheses marked as FACT or HYPOTHESIS with confidence levels.

**Review checkpoint:** Verify the architecture classification makes sense before validation.

### Step 4: Run Pass 3 — Validate

- Do: Generate a human validation packet
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/agents/pass3-validate-hitl-agent.md

  Using Pass 2 findings at @TargetRepo/docs/brownfield/pass2-infer-findings.md,
  generate the Human Validation Packet.

  Generate:
  1. Validation Packet (10-20 questions max)
  2. Confirmation Summary Template
  3. Change Risk Warnings (top 5 dangerous areas)

  Save to @TargetRepo/docs/brownfield/pass3-validation-packet.md
  ```
- Expect: `pass3-validation-packet.md` with targeted questions for a subject matter expert.

**Human checkpoint:** Send the validation packet to a SME or tech lead. Collect their responses.

### Step 5: Apply validation responses

- Do: Feed the human responses back to update the inferences
- How: Use the following prompt:
  ```
  The human validation responses are:

  [PASTE RESPONSES HERE]

  Update Pass 2 findings based on corrections.
  Save to @TargetRepo/docs/brownfield/pass3-validation-responses.md
  ```
- Expect: `pass3-validation-responses.md` with corrected and confirmed findings.

### Step 6: Run Pass 4 — Document

- Do: Generate final system documentation from all previous passes
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/agents/pass4-document-agent.md
  Read @GenDD-Flow/templates/documentation-guidelines.md

  Using:
  - @TargetRepo/docs/brownfield/pass1-scan-findings.md
  - @TargetRepo/docs/brownfield/pass2-infer-findings.md
  - @TargetRepo/docs/brownfield/pass3-validation-responses.md

  Generate documentation following structure guidelines.

  Produce the documentation pack as an individual file per section under
  docs/brownfield/gendd/ (overview/, architecture/, risks/, onboarding/, flows/),
  plus gendd/README.md and gendd/stack.json. Keep each file within its size limit.

  Save to @TargetRepo/docs/brownfield/
  ```
- Expect: Final documentation with findings marked as CONFIRMED or INFERRED. File references only — no embedded code.

### Step 7: Run quality checklist

- Do: Verify the output meets GenDD-Flow documentation requirements
- How: Check these items against the output:
  - [ ] No embedded code snippets (file references only)
  - [ ] No hard-coded counts (patterns instead)
  - [ ] No content duplication (cross-references used)
  - [ ] Files under size limits
  - [ ] New engineers can understand the system from the docs
  - [ ] Critical risks documented
  - [ ] Core flows mapped and validated
- Expect: All items checked. Fix any gaps before proceeding to follow-up workflows.

## Expected Output

### Output Tree
```
TargetRepo/
└── docs/brownfield/
    ├── pass1-scan-findings.md
    ├── pass2-infer-findings.md
    ├── pass3-validation-responses.md
    └── gendd/
        ├── README.md
        ├── stack.json
        ├── overview/
        │   ├── system-summary.md
        │   └── tech-stack.md
        ├── architecture/
        │   ├── overview.md
        │   ├── components.md
        │   └── data-ownership.md
        ├── risks/
        │   ├── risk-hotspots.md
        │   └── open-questions.md
        ├── onboarding/
        │   └── guide.md
        └── flows/
            └── {flow-name}.md
```

**Save to:** `@TargetRepo/docs/brownfield/`

## What's Next

- [ ] [Create context pack](../../workflows/create-context-pack.md) for IDE integration
- [ ] [Generate C4 architecture diagrams](../on-demand/generate-architecture-diagrams.md) from the system documentation
- [ ] [Identify test gaps](../on-demand/identify-test-gaps.md) from the risk hotspots
- [ ] Share the validation packet with team leads for ongoing alignment

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Pass 1 Agent | `agents/pass1-scan-agent.md` | Scan agent instructions |
| Pass 2 Agent | `agents/pass2-infer-agent.md` | Inference agent instructions |
| Pass 3 Agent | `agents/pass3-validate-hitl-agent.md` | Validation agent instructions |
| Pass 4 Agent | `agents/pass4-document-agent.md` | Documentation agent instructions |
| Documentation Guidelines | `templates/documentation-guidelines.md` | File reference and size rules |
| Context Pack Template | `templates/context-pack.md` | Universal principles for security, testing, logging, code quality |