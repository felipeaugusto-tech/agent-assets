# GenDD-Flow: AI-Assisted Software Development Lifecycle

Production-ready workflows for AI-assisted requirements, testing, documentation, and architecture — designed for use with **any AI-powered IDE** (Cursor, Claude Code, Antigravity, GitHub Copilot, and more).

**License:** MIT

---

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start-5-minutes)
- [The Five-Phase Flow](#the-five-phase-flow)
- [Supported IDEs](#supported-ides)
- [The Seven Frameworks](#the-seven-frameworks)
- [Knowledge System](#knowledge-system)
- [Repository Structure](#repository-structure)
- [Integration Options](#integration-options)
- [MCP Setup](#mcp-setup)
- [How Frameworks Connect](#how-frameworks-connect)
- [Key Concepts](#key-concepts)
- [Troubleshooting](#troubleshooting)

---

## Overview

GenDD-Flow is an **IDE-agnostic toolkit** that brings structured SDLC practices to AI-assisted development. It works by providing Markdown-based workflows, knowledge files, templates, and agent definitions that your AI IDE reads during analysis. No RAG, no vector databases, no external platforms — everything lives as version-controlled Markdown files in this repository.

**What it does:**
1. **Analyzes your codebase** using a structured 4-pass brownfield analysis (or greenfield specification analysis)
2. **Detects which SDLC areas matter** using LLM-driven analysis with structural signals as supplement
3. **Generates context per area** — rich, codebase-specific documentation the AI uses to understand your project
4. **Detects or generates standards** for any SDLC area (coding, product, delivery, testing, security, operations)
5. **Creates IDE-specific agent rules** — in the exact format your IDE expects (Cursor rules, CLAUDE.md, GEMINI.md, Copilot instructions, etc.)

**Additional capabilities:**
- Transform vague requirements into detailed, testable acceptance criteria
- Systematically identify test gaps and generate remediation plans
- Generate C4 architecture diagrams from codebase analysis
- Generate E2E tests from live applications via Playwright MCP
- Integrate with Jira and Confluence via Atlassian MCP

### Area Detection

GenDD-Flow detects which SDLC areas apply to your codebase using a
three-layer approach:

1. **LLM Analysis (Primary)** — During inference, the AI analyzes your
   codebase and suggests applicable areas with confidence levels and reasoning.
   This handles novel frameworks and unusual architectures that pattern
   matching would miss.

2. **Structural Signals (Supplementary)** — File-existence checks for
   infrastructure (Docker, CI/CD, IaC), data layer (migrations, ORM),
   and event systems (brokers, topics).

3. **Manual Addition (Safety Net)** — Users can add any area not
   auto-detected, with custom names and descriptions.

This replaces the previous hardcoded signal-matching tables.

### Brownfield & Greenfield Support

GenDD-Flow works with both existing codebases and planned projects:

- **Brownfield:** Full 4-pass analysis (Scan → Infer → Validate → Document),
  then area detection and context generation.
- **Greenfield:** Create a project folder, place planning documents in
  `docs/specs/`, and run the greenfield workflow. Area detection uses LLM
  suggestions from the specification analysis. Context documents reference
  planned architecture.

Both flows produce the same output structure and use the same Phase 2-5 pipeline.

---

## Quick Start (5 Minutes)

### 1. Set up your workspace

Add both GenDD-Flow and your target repo to your AI IDE workspace.

### 2. Run the full analysis

```
Read @GenDD-Flow/workflows/analyze-and-generate.md

Analyze @TargetRepo and run the full GenDD-Flow pipeline:
1. Brownfield analysis (4-pass)
2. Detect applicable SDLC areas
3. Generate context per area
4. Check for standards gaps
5. Generate IDE rules for [YOUR IDE: Cursor/Claude Code/Antigravity/Copilot/Other]
```

**Result:** Your target repo gets `docs/context/` (per-area context), `docs/standards/` (detected or generated standards), and IDE-specific agent rules — all tailored to your codebase.

For more copy-paste prompts, see [QUICK-START.md](QUICK-START.md).

---

## The Five-Phase Flow

```
Phase 1: ANALYZE CODEBASE
    │  Brownfield 4-pass analysis (Scan → Infer → Validate → Document)
    │  Or: Greenfield specification analysis (wizard / document upload)
    │
Phase 2: DETERMINE SDLC AREAS
    │  LLM suggestions (primary) + structural signals (supplementary) + baselines
    │  User confirms/adjusts — can add, edit, remove, or toggle areas
    │
Phase 3: GENERATE CONTEXT PER AREA
    │  For each area, generates docs/context/{area}.md in target repo
    │
Phase 4: CHECK & GENERATE STANDARDS
    │  Scans for existing standards across all SDLC areas
    │  Offers to generate missing standards (project or org level)
    │
Phase 5: GENERATE IDE RULES
       Asks which IDE → web searches for latest format → generates rules
```

**Main entry point:** `workflows/analyze-and-generate.md`

---

## Supported IDEs

| IDE | Output Format | Rule Location |
|-----|---------------|---------------|
| **Cursor** | MDC with frontmatter | `.cursor/rules/*.mdc` |
| **Claude Code** | Markdown | `CLAUDE.md` + `.claude/commands/*.md` |
| **Antigravity (Google)** | Markdown (layered) | `GEMINI.md` + `AGENTS.md` + `.agent/rules/*.md` |
| **GitHub Copilot** | Single markdown file | `.github/copilot-instructions.md` |
| **Other** | Generic markdown | `.ai-rules/*.md` |

GenDD-Flow uses **web search** to verify the latest IDE format before generating rules, with baseline snapshots as fallback. This ensures rules stay current even as IDEs evolve.

---

## The Seven Frameworks

| # | Framework | Purpose | Entry Point |
|---|-----------|---------|-------------|
| 1 | **Story Quality** | Transform vague requirements into testable ACs | `playbooks/on-demand/enhance-requirements.md` |
| 2 | **Test Gap Analysis** | Identify missing tests and create remediation plans | `playbooks/on-demand/identify-test-gaps.md` |
| 3 | **Context Generation** | Generate per-area context docs + IDE rules for any repo | `workflows/analyze-and-generate.md` |
| 4 | **C4 Diagrams** | Generate C4 architecture diagrams (Mermaid) | `workflows/generate-architecture-diagrams.md` |
| 5 | **Brownfield Analysis** | Document legacy/undocumented systems (4-pass) | `playbooks/onboarding/run-full-analysis.md` |
| 6 | **Playwright MCP** | E2E tests from live applications | `playbooks/on-demand/run-assisted-testing.md` |
| 7 | **Atlassian Integration** | Jira tickets & Confluence docs via MCP | See [QUICK-START.md](QUICK-START.md) |

### Framework 1: Story Quality (Shift-Left)

Transform vague requirements into detailed, testable acceptance criteria.

| Resource | Description |
|----------|-------------|
| `workflows/enhance-acceptance-criteria.md` | Full step-by-step process |
| `playbooks/on-demand/enhance-requirements.md` | On-demand playbook |
| `templates/requirements-enhancement.md` | AC rules and prompt templates |

**Output:** User Story (Given-When-Then), Acceptance Criteria (Gherkin), Edge Cases (5+), Integration Impacts, Test Scenarios.

### Framework 2: Test Gap Identification

Identify what tests should exist vs what does exist, prioritized by business risk.

| Resource | Description |
|----------|-------------|
| `workflows/identify-test-gaps.md` | Full analysis workflow |
| `workflows/generate-unit-tests.md` | Unit test generation |
| `workflows/automate-integration-testing.md` | Integration test generation |
| `templates/testing-standards.md` | MUST/SHOULD/MAY requirements |

### Framework 3: Context Generation & IDE Rules

Analyze a codebase and generate per-area context documents plus IDE-specific agent rules.

| Resource | Description |
|----------|-------------|
| `workflows/analyze-and-generate.md` | Master orchestration (5-phase flow) |
| `workflows/generate-context-areas.md` | Context-per-area generation |
| `workflows/generate-ide-rules.md` | IDE-specific rules (web-search driven) |
| `workflows/detect-and-generate-standards.md` | Standards detection and generation |

**Output:**
```
target-repo/
├── docs/context/          # Context per SDLC area
│   ├── architecture.md
│   ├── backend-development.md
│   ├── quality-assurance.md
│   └── ...
├── docs/standards/        # Standards per area
│   ├── coding.md
│   ├── testing.md
│   └── ...
└── (IDE-specific rules)   # Based on your IDE
```

### Framework 4: C4 Architecture Diagrams

Generate standardized architecture diagrams at multiple levels of abstraction.

| Resource | Description |
|----------|-------------|
| `workflows/generate-architecture-diagrams.md` | Full C4 workflow |

**Output:** Context (L1), Container (L2), Component (L3), and Deployment diagrams in Mermaid format.

### Framework 5: Brownfield Repository Analysis

Document legacy/undocumented systems using a structured 4-pass approach with human-in-the-loop validation.

| Pass | Agent | Purpose |
|------|-------|---------|
| 1. Scan | `agents/pass1-scan-agent.md` | Rapid inventory of repository structure |
| 2. Infer | `agents/pass2-infer-agent.md` | Deduce architecture, flows, data ownership |
| 3. Validate | `agents/pass3-validate-hitl-agent.md` | Human confirmation of hypotheses |
| 4. Document | `agents/pass4-document-agent.md` | Produce comprehensive documentation pack |

Additional agents:
- `agents/tailoring-rules.md` — Architecture-specific rules (monorepo, microservices, event-driven, etc.)
- `agents/pass5-role-detector-agent.md` — Determines which SDLC areas apply to the codebase

### Framework 6: Playwright MCP (E2E Testing)

Generate E2E tests from live applications using browser automation.

| Resource | Description |
|----------|-------------|
| `playbooks/on-demand/run-assisted-testing.md` | E2E test generation from live app |
| `playbooks/on-demand/validate-acceptance-criteria.md` | AC validation against running UI |

### Framework 7: Atlassian Integration (Jira & Confluence)

Create Jira issues and Confluence documentation via MCP. See [QUICK-START.md](QUICK-START.md) for complete prompts.

---

## Knowledge System

The `knowledge/` directory replaces the old role-based playbooks with an AI-internal knowledge layer organized by SDLC area.

### SDLC Areas (`knowledge/sdlc-areas/`)

16 knowledge files covering the full SDLC, grouped by function:

| Category | Areas |
|----------|-------|
| **Development** | architecture, backend-development, frontend-development, fullstack-development |
| **Quality** | quality-assurance, security |
| **Operations** | devops-infrastructure, site-reliability |
| **Product & Delivery** | product-management, delivery-management, technical-leadership |
| **Data** | database-management |
| **Design** | user-experience |
| **Support** | technical-writing, release-management, support-engineering |

These files tell the AI **what to look for, analyze, and document** when examining a codebase through each area's lens. They are not user-facing — they are consumed internally during Phase 3 (Generate Context Per Area).

### IDE Formats (`knowledge/ide-formats/`)

Baseline snapshots of each IDE's rule configuration format. Used as **fallback** when web search is unavailable. The primary discovery method is web search to ensure formats stay current.

---

## Repository Structure

```
GenDD-Flow/
├── README.md                        ← You are here
├── QUICK-START.md                   ← Copy-paste prompts for all workflows
├── .cursorrules.md                  ← Cursor rules (auto-loaded by Cursor IDE)
│
├── workflows/                       ← Detailed step-by-step multi-phase guides
│   ├── analyze-and-generate.md             # Master orchestration (main entry)
│   ├── generate-context-areas.md           # Phase 3: context per area
│   ├── generate-ide-rules.md              # Phase 5: IDE-specific rules
│   ├── detect-and-generate-standards.md   # Phase 4: standards detection
│   ├── brownfield-repository-analysis.md   # Brownfield 4-pass master workflow
│   ├── greenfield-analysis.md              # Greenfield specification analysis
│   ├── enhance-acceptance-criteria.md      # Story Quality
│   ├── identify-test-gaps.md               # Test Gap Analysis
│   ├── generate-unit-tests.md              # Unit test generation
│   ├── automate-integration-testing.md     # Integration test generation
│   ├── generate-architecture-diagrams.md   # C4 architecture diagrams
│   ├── generate-tests-from-gherkin.md      # Tests from Gherkin ACs
│   └── incremental-doc-update.md           # Selective documentation updates
│
├── agents/                          ← Analysis agent definitions
│   ├── pass1-scan-agent.md                 # Repository inventory
│   ├── pass2-infer-agent.md                # Architecture inference
│   ├── pass3-validate-hitl-agent.md        # Human-in-the-loop validation
│   ├── pass4-document-agent.md             # Documentation generation
│   ├── tailoring-rules.md                  # Architecture-specific rules
│   └── pass5-role-detector-agent.md              # SDLC area detection
│
├── knowledge/                       ← AI-internal knowledge layer
│   ├── _index.md                           # Index of all SDLC areas
│   ├── sdlc-areas/                         # 16 area knowledge files
│   └── ide-formats/                        # IDE format baselines (fallback)
│
├── playbooks/                       ← Step-by-step playbooks by trigger type
│   ├── PLAYBOOK-GUIDE.md                   # Decision tree
│   ├── onboarding/                         # First-time setup
│   │   └── run-full-analysis.md
│   ├── on-demand/                          # Triggered playbooks (15)
│   └── recurring/                          # Periodic maintenance
│
├── templates/                       ← Output structure & standards templates
│   ├── context-area.md                     # Per-area context document template
│   ├── standards/                          # Standards templates per SDLC area
│   ├── ide-rules/                          # IDE-specific rule templates
│   ├── requirements-enhancement.md         # AC rules and prompt templates
│   ├── testing-standards.md                # MUST/SHOULD/MAY test requirements
│   ├── documentation-guidelines.md         # Documentation formatting rules
│   └── validation-packet.md                # HITL validation packet template
│
├── scripts/                         ← Automation scripts
│   └── setup-integration.sh                # Target repo integration setup
│
└── .github/                         ← GitHub integration
    └── pr-review-prompt.md                 # AI-assisted PR review checklist
```

---

## Integration Options

### Option A: Multi-Root Workspace (Recommended)

Add both GenDD-Flow and your target repo to your AI IDE's workspace. Reference workflows with `@GenDD-Flow/` prefix.

### Option B: Setup Script

```bash
./scripts/setup-integration.sh --all /path/to/target-repo
```

### Option C: Symbolic Link

```bash
cd /path/to/target-repo
ln -s /path/to/GenDD-Flow .genddflow
echo ".genddflow" >> .gitignore
```

### Option D: Git Submodule

```bash
cd /path/to/target-repo
git submodule add <repository-url> .sdlc
```

---

## MCP Setup

### Playwright MCP (Browser Automation)

Required for Framework 6 (E2E Testing) and AC validation.

```bash
npm install -g @playwright/mcp
npx playwright install chromium
```

Configure in your IDE's MCP settings:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": { "HEADLESS": "true" }
    }
  }
}
```

### Atlassian MCP (Jira & Confluence)

Required for Framework 7 (Atlassian Integration):
```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-atlassian"],
      "env": {
        "ATLASSIAN_URL": "your-org.atlassian.net",
        "ATLASSIAN_EMAIL": "your-email@company.com",
        "ATLASSIAN_API_TOKEN": "your-api-token"
      }
    }
  }
}
```

---

## How Frameworks Connect

```
                    ┌─────────────────┐
                    │   BROWNFIELD    │ (5)
                    │   ANALYSIS      │
                    └────────┬────────┘
                             │
      ┌──────────────────────┼──────────────────────┐
      │                      │                      │
      ▼                      ▼                      ▼
┌───────────┐      ┌─────────────────┐      ┌───────────────┐
│ TEST GAPS │ (2)  │  C4 DIAGRAMS    │ (4)  │ CONTEXT GEN   │ (3)
└─────┬─────┘      └─────────────────┘      │ + IDE RULES   │
      │                                     └─────┬─────────┘
      │                                           │
      ▼                                           ▼
┌───────────────┐                       ┌─────────────────┐
│ UNIT/INT TESTS│                       │ STORY QUALITY   │ (1)
└───────┬───────┘                       └────────┬────────┘
        │                                        │
        │         ┌─────────────────┐            │
        └────────▶│ PLAYWRIGHT MCP  │◀───────────┘
                  │ (6)             │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ ATLASSIAN MCP   │ (7)
                  │ Jira/Confluence │
                  └─────────────────┘
```

---

## Key Concepts

### Tooling Approach

**AI IDE + repo-based Markdown context only.** No RAG, vector databases, embeddings, or external platforms. All artifacts stay version-controlled.

### Documentation Guidelines

- **Reference files**, not code snippets (they get stale)
- **Use patterns**, not counts ("Services matching `*Service.cs`")
- **One concept per file** with cross-references
- **No duplication** — single source of truth

### Human-in-the-Loop (HITL)

Phase 2 (area detection) and Phase 4 (standards) include HITL validation gates. Always validate before generating artifacts.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| IDE can't find GenDD-Flow | Use `@GenDD-Flow/` prefix, verify workspace setup |
| Playwright MCP not working | Check MCP config, restart IDE, run `npx playwright install chromium` |
| Context window exhausted | Split into separate chat sessions per phase |
| "Which workflow should I use?" | See [PLAYBOOK-GUIDE.md](playbooks/PLAYBOOK-GUIDE.md) |
| IDE rules format looks wrong | Run Phase 5 again — it web searches for the latest format |
| Want to switch IDEs | Run `playbooks/on-demand/generate-ide-rules.md` with the new IDE |
| Standards already exist | Phase 4 detects them and summarizes; it won't overwrite |

---

## Next Steps

1. **Set up your workspace** — add GenDD-Flow and your target repo
2. **Run the full analysis** — see [QUICK-START.md](QUICK-START.md)
3. **Set up MCP tools** if needed (Playwright, Atlassian)
4. **Explore on-demand playbooks** for specific tasks

---

**Ready to start? See [QUICK-START.md](QUICK-START.md) for copy-paste prompts.**
