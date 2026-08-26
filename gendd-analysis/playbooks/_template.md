# How to Write a Playbook

> **Conventions for authors:**
> - Use imperative verbs for titles (e.g., "Analyze Test Gaps", not "Test Gap Analysis")
> - Reference existing `playbooks/` and `workflows/` instead of duplicating content
> - Always specify concrete inputs and outputs
> - Keep steps atomic — one action per step
> - Place the finished playbook in the correct category folder (`onboarding/`, `on-demand/`, or `recurring/`)
> - File name should be kebab-case matching the title (e.g., `analyze-test-gaps.md`)

---

# <!-- REPLACE: Imperative Action Title (e.g., "Onboard a New Repository") -->

| Field | Value |
|-------|-------|
| **Category** | <!-- REPLACE: onboarding / on-demand / recurring --> |
| **Target Roles** | <!-- REPLACE: e.g., Architect, Tech Lead, Backend Dev --> |
| **Prerequisites** | <!-- REPLACE: e.g., "Repo access granted", "Node 18+ installed" --> |
| **Inputs** | <!-- REPLACE: What the user provides — repo path, PR link, feature name, etc. --> |
| **Outputs** | <!-- REPLACE: Concrete deliverables — files, reports, diagrams --> |

## When to Use

<!-- REPLACE: 2-3 bullet points describing the trigger or situation -->
- ...
- ...

## Before You Start

<!-- REPLACE: Prerequisites verification checklist -->
- [ ] ...
- [ ] ...

## Steps

<!-- REPLACE: Numbered steps. Each step should include:
     1. **What to do** — the action
     2. **How to do it** — the prompt, command, or tool reference
     3. **What to expect** — the result or output
-->

1. **Step name**
   - Do: ...
   - How: Use `playbooks/...` or `workflows/...` or run `command ...`
   - Expect: ...

2. **Step name**
   - Do: ...
   - How: ...
   - Expect: ...

## Expected Output

<!-- REPLACE: Template or example of the final deliverable -->
<!-- REPLACE: File naming convention and where to save it -->

```
<!-- Example output structure -->
```

**Save to:** `<!-- REPLACE: path/to/output -->`

## What's Next

<!-- REPLACE: Links to logical follow-up playbooks -->
- [ ] [Follow-up playbook](../category/playbook-name.md)
- [ ] ...

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| <!-- REPLACE --> | `playbooks/...` | <!-- REPLACE --> |
| <!-- REPLACE --> | `workflows/...` | <!-- REPLACE --> |

---

# Example: Onboard a New Repository

> This filled-in example shows how a completed playbook looks.

# Onboard a New Repository

| Field | Value |
|-------|-------|
| **Category** | onboarding |
| **Target Roles** | Architect, Tech Lead, Backend Dev, Frontend Dev |
| **Prerequisites** | Repository cloned locally, GenDD-Flow available |
| **Inputs** | Path to the repository root |
| **Outputs** | Brownfield analysis report, initial architecture doc |

## When to Use

- You've just been added to an existing project and need to understand its structure
- Your team is adopting GenDD-Flow on a repo for the first time
- A new team member needs a structured onboarding path

## Before You Start

- [ ] Repository is cloned and you can build/run it locally
- [ ] You have read access to CI/CD configuration
- [ ] GenDD-Flow repo is available at a known path

## Steps

1. **Run brownfield analysis**
   - Do: Generate a full codebase analysis
   - How: Use `playbooks/onboarding/run-brownfield-analysis.md` with the repo path as input
   - Expect: A markdown report covering tech stack, architecture patterns, dependencies, and risks

2. **Review the analysis output**
   - Do: Read the generated report and flag areas that need clarification
   - How: Open the report and note any gaps or surprises
   - Expect: A list of follow-up questions or areas to investigate

3. **Generate initial architecture documentation**
   - Do: Produce architecture docs from the analysis
   - How: Use `workflows/generate-architecture-diagrams.md` targeting architecture
   - Expect: An architecture overview document with diagrams and component descriptions

## Expected Output

```
docs/
├── brownfield-analysis.md
└── architecture-overview.md
```

**Save to:** `docs/` in the target repository

## What's Next

- [ ] [Set Up Recurring Sprint Review](../recurring/sprint-review.md)
- [ ] [Analyze Test Gaps](../on-demand/analyze-test-gaps.md)

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Brownfield Analysis | `playbooks/onboarding/run-brownfield-analysis.md` | Full codebase analysis playbook |
| Architecture Diagrams | `workflows/generate-architecture-diagrams.md` | Architecture diagram generation |
