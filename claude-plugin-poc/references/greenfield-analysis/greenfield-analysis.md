# Workflow: Greenfield Analysis

## Overview

This workflow handles analysis of new/planned projects that don't have an
existing codebase. The user creates a project folder, places any planning
documents inside it, and runs this workflow from that folder. It replaces
Phase 1 (brownfield scanning) with specification analysis, then feeds into
the same Phase 2-5 pipeline.

## Setup

### Step 1: Create a Project Folder

Create an empty folder for the new project. This is where all generated
artifacts (context docs, standards, IDE rules) will be saved.

```bash
mkdir my-new-project
cd my-new-project
```

### Step 2: Add Planning Documents

Place any available documentation into a `docs/specs/` subfolder:

```
my-new-project/
└── docs/
    └── specs/
        ├── requirements.md
        ├── architecture.pdf
        ├── prd.md
        ├── tech-stack.md
        └── ... (any relevant planning docs)
```

Accepted formats: Markdown, PDF, plain text, images (architecture diagrams).

The more context you provide, the better the area detection and context
generation will be. At minimum, include:
- Project purpose and goals
- Planned tech stack
- High-level architecture (monolith, microservices, serverless, etc.)
- Key services or modules

If you have no documents, you can describe the project directly in the
prompt (see Quick Start below).

### Step 3: Run Greenfield Analysis

From the project folder, invoke the workflow. The AI reads everything in
`docs/specs/` and uses it as input for specification analysis.

## Process

### Step 1: Analyze Specifications

Read all documents in `docs/specs/` and any description provided in the
prompt. Produce an inference result with the same structure as brownfield
analysis:
- systemPurpose
- architectureClassification
- serviceCatalog
- coreFlows
- dataMap
- riskHotspots (potential risks for planned architecture)
- conventions (planned conventions)
- techStack
- **suggestedAreas** (LLM-suggested SDLC areas)

Save the inference result to `docs/greenfield/inference-result.md`.

### Step 2: Continue with Phase 2

Feed the inference result into the standard Phase 2-5 pipeline:
- Phase 2: Area detection (LLM suggestions are the sole source since
  structural signals produce nothing without a codebase)
- Phase 3: Context generation (references planned files, not existing ones)
- Phase 4: Standards generation (based on planned tech stack)
- Phase 5: IDE rules generation

## Output Structure

After running the full flow, the project folder will contain:

```
my-new-project/
├── docs/
│   ├── specs/                    # User-provided (input)
│   │   ├── requirements.md
│   │   └── ...
│   ├── greenfield/               # Greenfield analysis output
│   │   └── inference-result.md
│   ├── context/                  # Phase 3 output
│   │   ├── architecture.md
│   │   ├── backend-development.md
│   │   └── ...
│   └── standards/                # Phase 4 output
│       ├── coding.md
│       └── ...
└── (IDE-specific rules)          # Phase 5 output
```

## Context Document Differences

Greenfield context documents differ from brownfield in tone:
- "Current State" becomes "Planned State"
- File references point to planned locations, not existing ones
- Risks focus on architectural decisions not yet validated
- "What's Missing" focuses on what hasn't been specified yet

## Quick Start

### With Planning Documents

```
Read @GenDD-Flow/workflows/greenfield-analysis.md

Analyze the project specifications in @docs/specs/ and run the full
GenDD-Flow pipeline for this new project.

Generate context documents for all applicable SDLC areas.
```

### With Direct Description (No Documents)

```
Read @GenDD-Flow/workflows/greenfield-analysis.md

I'm planning a new project:
- **Name:** {project name}
- **Tech stack:** {list technologies}
- **Architecture:** {describe architecture}
- **Key features:** {list features}

Analyze this specification and generate context documents for applicable
SDLC areas.
```

### Hybrid (Documents + Additional Context)

```
Read @GenDD-Flow/workflows/greenfield-analysis.md

Analyze the project specifications in @docs/specs/.

Additional context not in the documents:
- {any extra details}

Generate context documents for all applicable SDLC areas.
```
