 GenDD-Flow Playbook System - Implementation Plan                                                                      │
│                                                                                                                      │
│ Problem Statement                                                                                                    │
│                                                                                                                      │
│ The full 4-pass brownfield analysis is designed for initial repository discovery but is wasteful for incremental     │
│ changes. Teams need:                                                                                                 │
│ - Trigger-based playbooks that run only what's needed                                                                │
│ - CI/CD integration for automated documentation updates                                                              │
│ - Role-specific prompts for QA, Dev, PM, Architect                                                                   │
│ - MCP integration for Confluence publishing                                                                          │
│                                                                                                                      │
│ ---                                                                                                                  │
│ Playbook Classification System                                                                                       │
│                                                                                                                      │
│ Category 1: Initial Discovery (Existing)                                                                             │
│                                                                                                                      │
│ When: New repository, major refactor, first-time documentation                                                       │
│ What: Full 4-pass brownfield analysis                                                                                │
│ Files: agents/pass1-4-agent.md, prompts/brownfield-analysis.md                                                       │
│                                                                                                                      │
│ Category 2: PR/Merge Updates (NEW)                                                                                   │
│                                                                                                                      │
│ When: PR opened, code merged to main                                                                                 │
│ What: Delta analysis → selective doc updates                                                                         │
│ Trigger: GitHub Action on PR/push                                                                                    │
│                                                                                                                      │
│ Category 3: Release Documentation (NEW)                                                                              │
│                                                                                                                      │
│ When: Release tag created                                                                                            │
│ What: Release notes, Confluence update, changelog                                                                    │
│ Trigger: GitHub Action on tag                                                                                        │
│                                                                                                                      │
│ Category 4: On-Demand by Role (NEW)                                                                                  │
│                                                                                                                      │
│ When: Manual trigger by team member                                                                                  │
│ What: Role-specific analysis (QA, Dev, PM, Architect, Tech Lead)                                                     │
│                                                                                                                      │
│ ---                                                                                                                  │
│ New Files to Create                                                                                                  │
│                                                                                                                      │
│ 1. Playbook Guide                                                                                                    │
│                                                                                                                      │
│ File: playbooks/PLAYBOOK-GUIDE.md                                                                                    │
│ Purpose: Decision tree for "which playbook to run when"                                                              │
│ Contents:                                                                                                            │
│ - Trigger → Playbook mapping table                                                                                   │
│ - Visual decision flowchart                                                                                          │
│ - Role-based quick reference                                                                                         │
│                                                                                                                      │
│ 2. Delta Analysis Prompt                                                                                             │
│                                                                                                                      │
│ File: prompts/delta-analysis.md                                                                                      │
│ Purpose: Analyze PR changes, identify documentation impact                                                           │
│ Inputs: Git diff, existing documentation                                                                             │
│ Outputs:                                                                                                             │
│ - Changed components list                                                                                            │
│ - Affected documentation sections                                                                                    │
│ - Recommended updates (prioritized)                                                                                  │
│ - Risk assessment                                                                                                    │
│                                                                                                                      │
│ 3. Incremental Update Workflow                                                                                       │
│                                                                                                                      │
│ File: workflows/incremental-doc-update.md                                                                            │
│ Purpose: Update only affected documentation sections                                                                 │
│ Steps:                                                                                                               │
│ 1. Run delta-analysis.md                                                                                             │
│ 2. Map changes to doc sections                                                                                       │
│ 3. Run targeted Pass 1/2 on affected areas only                                                                      │
│ 4. Update specific doc files                                                                                         │
│ 5. (Optional) Push to Confluence                                                                                     │
│                                                                                                                      │
│ 4. Release Documentation Workflow                                                                                    │
│                                                                                                                      │
│ File: workflows/release-documentation.md                                                                             │
│ Purpose: Generate release artifacts                                                                                  │
│ Outputs:                                                                                                             │
│ - CHANGELOG entry                                                                                                    │
│ - Release notes (GitHub release)                                                                                     │
│ - Confluence page update                                                                                             │
│                                                                                                                      │
│ 5. Confluence Publishing Prompt                                                                                      │
│                                                                                                                      │
│ File: prompts/confluence-publish.md                                                                                  │
│ Purpose: Transform markdown docs to Confluence format                                                                │
│ Uses: Atlassian MCP                                                                                                  │
│ Actions:                                                                                                             │
│ - Convert markdown to Confluence storage format                                                                      │
│ - Create/update pages in correct space                                                                               │
│ - Link related pages                                                                                                 │
│                                                                                                                      │
│ 6. Complete SDLC Role Playbooks                                                                                      │
│                                                                                                                      │
│ Directory: prompts/role-playbooks/                                                                                   │
│                                                                                                                      │
│ Product & Planning Roles                                                                                             │
│ ┌─────────────────────┬──────────────────┬───────────────────────────────────────────────────────┐                   │
│ │        File         │       Role       │                         Focus                         │                   │
│ ├─────────────────────┼──────────────────┼───────────────────────────────────────────────────────┤                   │
│ │ product-owner.md    │ Product Owner    │ Backlog analysis, story prioritization, value mapping │                   │
│ ├─────────────────────┼──────────────────┼───────────────────────────────────────────────────────┤                   │
│ │ business-analyst.md │ Business Analyst │ Requirements elicitation, process flows, gap analysis │                   │
│ ├─────────────────────┼──────────────────┼───────────────────────────────────────────────────────┤                   │
│ │ ux-designer.md      │ UX Designer      │ UI inventory, accessibility audit, component patterns │                   │
│ └─────────────────────┴──────────────────┴───────────────────────────────────────────────────────┘                   │
│ Development Roles                                                                                                    │
│ ┌──────────────────┬──────────────────────┬──────────────────────────────────────────────────────┐                   │
│ │       File       │         Role         │                        Focus                         │                   │
│ ├──────────────────┼──────────────────────┼──────────────────────────────────────────────────────┤                   │
│ │ frontend-dev.md  │ Frontend Developer   │ Component patterns, UI conventions, state management │                   │
│ ├──────────────────┼──────────────────────┼──────────────────────────────────────────────────────┤                   │
│ │ backend-dev.md   │ Backend Developer    │ API patterns, service conventions, data access       │                   │
│ ├──────────────────┼──────────────────────┼──────────────────────────────────────────────────────┤                   │
│ │ fullstack-dev.md │ Full-Stack Developer │ End-to-end patterns, integration points              │                   │
│ └──────────────────┴──────────────────────┴──────────────────────────────────────────────────────┘                   │
│ Quality Roles                                                                                                        │
│ ┌──────────────────┬───────────────┬────────────────────────────────────────────────────┐                            │
│ │       File       │     Role      │                       Focus                        │                            │
│ ├──────────────────┼───────────────┼────────────────────────────────────────────────────┤                            │
│ │ qa-engineer.md   │ QA Engineer   │ Test gaps, AC validation, E2E generation, coverage │                            │
│ ├──────────────────┼───────────────┼────────────────────────────────────────────────────┤                            │
│ │ qa-automation.md │ QA Automation │ Test framework setup, CI test integration          │                            │
│ └──────────────────┴───────────────┴────────────────────────────────────────────────────┘                            │
│ Operations Roles                                                                                                     │
│ ┌──────────────────────┬───────────────────┬─────────────────────────────────────────────────────┐                   │
│ │         File         │       Role        │                        Focus                        │                   │
│ ├──────────────────────┼───────────────────┼─────────────────────────────────────────────────────┤                   │
│ │ devops-engineer.md   │ DevOps Engineer   │ CI/CD analysis, deployment patterns, infrastructure │                   │
│ ├──────────────────────┼───────────────────┼─────────────────────────────────────────────────────┤                   │
│ │ sre.md               │ SRE               │ Observability, SLOs, incident patterns, runbooks    │                   │
│ ├──────────────────────┼───────────────────┼─────────────────────────────────────────────────────┤                   │
│ │ security-engineer.md │ Security Engineer │ Security scan, OWASP checklist, auth/authz review   │                   │
│ └──────────────────────┴───────────────────┴─────────────────────────────────────────────────────┘                   │
│ Architecture & Leadership Roles                                                                                      │
│ ┌────────────────────────┬─────────────────────┬─────────────────────────────────────────────────────────────┐       │
│ │          File          │        Role         │                            Focus                            │       │
│ ├────────────────────────┼─────────────────────┼─────────────────────────────────────────────────────────────┤       │
│ │ architect.md           │ Architect           │ C4 diagrams, risk hotspots, tech debt, ADRs                 │       │
│ ├────────────────────────┼─────────────────────┼─────────────────────────────────────────────────────────────┤       │
│ │ tech-lead.md           │ Tech Lead           │ Code review checklist, PR analysis, team conventions        │       │
│ ├────────────────────────┼─────────────────────┼─────────────────────────────────────────────────────────────┤       │
│ │ engineering-manager.md │ Engineering Manager │ Health metrics, velocity patterns, tech debt prioritization │       │
│ └────────────────────────┴─────────────────────┴─────────────────────────────────────────────────────────────┘       │
│ Support Roles                                                                                                        │
│ ┌─────────────────────┬──────────────────┬──────────────────────────────────────────────────────┐                    │
│ │        File         │       Role       │                        Focus                         │                    │
│ ├─────────────────────┼──────────────────┼──────────────────────────────────────────────────────┤                    │
│ │ dba.md              │ DBA              │ Schema analysis, query patterns, migration review    │                    │
│ ├─────────────────────┼──────────────────┼──────────────────────────────────────────────────────┤                    │
│ │ technical-writer.md │ Technical Writer │ Doc audit, API docs, user guides                     │                    │
│ ├─────────────────────┼──────────────────┼──────────────────────────────────────────────────────┤                    │
│ │ release-manager.md  │ Release Manager  │ Release checklist, changelog, version strategy       │                    │
│ ├─────────────────────┼──────────────────┼──────────────────────────────────────────────────────┤                    │
│ │ support-engineer.md │ Support Engineer │ Troubleshooting guides, FAQ generation, known issues │                    │
│ └─────────────────────┴──────────────────┴──────────────────────────────────────────────────────┘                    │
│ 7. GitHub Actions Workflow                                                                                           │
│                                                                                                                      │
│ File: ci-templates/documentation-automation.yml                                                                      │
│ Triggers:                                                                                                            │
│ - pull_request: Run delta analysis, comment on PR                                                                    │
│ - push to main: Update affected docs                                                                                 │
│ - tag (v*): Generate release notes                                                                                   │
│                                                                                                                      │
│ Jobs:                                                                                                                │
│ 1. detect-changes: Categorize changed files                                                                          │
│ 2. run-playbook: Execute appropriate prompt via Claude CLI                                                           │
│ 3. update-docs: Commit doc changes or comment results                                                                │
│ 4. publish-confluence: (optional) Push to Confluence                                                                 │
│                                                                                                                      │
│ 8. MCP Configuration                                                                                                 │
│                                                                                                                      │
│ File: mcp-configs/atlassian-mcp.json                                                                                 │
│ {                                                                                                                    │
│   "mcpServers": {                                                                                                    │
│     "atlassian": {                                                                                                   │
│       "command": "npx",                                                                                              │
│       "args": ["-y", "mcp-atlassian"],                                                                               │
│       "env": {                                                                                                       │
│         "CONFLUENCE_URL": "${CONFLUENCE_URL}",                                                                       │
│         "ATLASSIAN_EMAIL": "${ATLASSIAN_EMAIL}",                                                                     │
│         "ATLASSIAN_API_TOKEN": "${ATLASSIAN_API_TOKEN}"                                                              │
│       }                                                                                                              │
│     }                                                                                                                │
│   }                                                                                                                  │
│ }                                                                                                                    │
│                                                                                                                      │
│ ---                                                                                                                  │
│ Decision Tree: Which Playbook to Run                                                                                 │
│                                                                                                                      │
│ START                                                                                                                │
│   │                                                                                                                  │
│   ├─► Is this a NEW repository or major refactor?                                                                    │
│   │     YES → Run FULL 4-PASS BROWNFIELD ANALYSIS                                                                    │
│   │                                                                                                                  │
│   ├─► Is this triggered by a PR?                                                                                     │
│   │     YES → Run DELTA ANALYSIS                                                                                     │
│   │           │                                                                                                      │
│   │           ├─► Architecture changes? → Architect Playbook                                                         │
│   │           ├─► Test file changes? → QA Playbook                                                                   │
│   │           ├─► API/Schema changes? → Full Pass 2 on affected service                                              │
│   │           └─► Minor changes? → Comment summary only                                                              │
│   │                                                                                                                  │
│   ├─► Is this triggered by a release tag?                                                                            │
│   │     YES → Run RELEASE DOCUMENTATION workflow                                                                     │
│   │                                                                                                                  │
│   ├─► Is this a manual request?                                                                                      │
│   │     YES → Which role?                                                                                            │
│   │           ├─► QA → qa-playbook.md                                                                                │
│   │           ├─► Dev → dev-playbook.md                                                                              │
│   │           ├─► PM → pm-playbook.md                                                                                │
│   │           ├─► Architect → architect-playbook.md                                                                  │
│   │           └─► Tech Lead → tech-lead-playbook.md                                                                  │
│   │                                                                                                                  │
│   └─► Scheduled maintenance?                                                                                         │
│         YES → Run TEST GAP ANALYSIS + doc freshness check                                                            │
│                                                                                                                      │
│ ---                                                                                                                  │
│ File Change → Playbook Mapping                                                                                       │
│ ┌───────────────────────────┬─────────────────────────────────┬───────────────────────┐                              │
│ │   Changed Files Pattern   │            Playbook             │         Scope         │                              │
│ ├───────────────────────────┼─────────────────────────────────┼───────────────────────┤                              │
│ │ src/services/*            │ Delta Analysis → Pass 2 (Infer) │ Affected service only │                              │
│ ├───────────────────────────┼─────────────────────────────────┼───────────────────────┤                              │
│ │ src/api/*, *.proto        │ Delta + Architect Playbook      │ API contracts         │                              │
│ ├───────────────────────────┼─────────────────────────────────┼───────────────────────┤                              │
│ │ tests/*, *.spec.*         │ QA Playbook                     │ Test inventory update │                              │
│ ├───────────────────────────┼─────────────────────────────────┼───────────────────────┤                              │
│ │ docker*, k8s/*, .github/* │ Architect Playbook              │ Deployment section    │                              │
│ ├───────────────────────────┼─────────────────────────────────┼───────────────────────┤                              │
│ │ package.json, *.csproj    │ Delta Analysis                  │ Dependencies section  │                              │
│ ├───────────────────────────┼─────────────────────────────────┼───────────────────────┤                              │
│ │ README*, docs/*           │ Skip (already docs)             │ -                     │                              │
│ ├───────────────────────────┼─────────────────────────────────┼───────────────────────┤                              │
│ │ migrations/*, schema/*    │ Delta + Pass 2                  │ Data model section    │                              │
│ └───────────────────────────┴─────────────────────────────────┴───────────────────────┘                              │
│ ---                                                                                                                  │
│ GitHub Actions Integration (DEFERRED)                                                                                │
│                                                                                                                      │
│ Will be implemented in a future phase. Reference pattern:                                                            │
│ - Existing workflows in acst/mono/.github/workflows/main.yaml                                                        │
│                                                                                                                      │
│ ---                                                                                                                  │
│ Proposed Directory Structure                                                                                         │
│                                                                                                                      │
│ GenDD-Flow/                                                                                                           │
│ ├── playbooks/                      # NEW: Playbook orchestration                                                    │
│ │   ├── PLAYBOOK-GUIDE.md          # Decision tree, when to use what                                                 │
│ │   ├── initial-discovery.md       # Links to existing 4-pass                                                        │
│ │   └── incremental-update.md      # Delta-based updates                                                             │
│ │                                                                                                                    │
│ ├── prompts/                                                                                                         │
│ │   ├── (existing prompts...)                                                                                        │
│ │   ├── delta-analysis.md          # NEW: Change impact analysis                                                     │
│ │   │                                                                                                                │
│ │   └── role-playbooks/            # NEW: Complete SDLC coverage                                                     │
│ │       │                                                                                                            │
│ │       ├── # Product & Planning                                                                                     │
│ │       ├── product-owner.md                                                                                         │
│ │       ├── business-analyst.md                                                                                      │
│ │       ├── ux-designer.md                                                                                           │
│ │       │                                                                                                            │
│ │       ├── # Development                                                                                            │
│ │       ├── frontend-dev.md                                                                                          │
│ │       ├── backend-dev.md                                                                                           │
│ │       ├── fullstack-dev.md                                                                                         │
│ │       │                                                                                                            │
│ │       ├── # Quality                                                                                                │
│ │       ├── qa-engineer.md                                                                                           │
│ │       ├── qa-automation.md                                                                                         │
│ │       │                                                                                                            │
│ │       ├── # Operations                                                                                             │
│ │       ├── devops-engineer.md                                                                                       │
│ │       ├── sre.md                                                                                                   │
│ │       ├── security-engineer.md                                                                                     │
│ │       │                                                                                                            │
│ │       ├── # Architecture & Leadership                                                                              │
│ │       ├── architect.md                                                                                             │
│ │       ├── tech-lead.md                                                                                             │
│ │       ├── engineering-manager.md                                                                                   │
│ │       │                                                                                                            │
│ │       └── # Support                                                                                                │
│ │           ├── dba.md                                                                                               │
│ │           ├── technical-writer.md                                                                                  │
│ │           ├── release-manager.md                                                                                   │
│ │           └── support-engineer.md                                                                                  │
│ │                                                                                                                    │
│ ├── workflows/                                                                                                       │
│ │   ├── (existing workflows...)                                                                                      │
│ │   └── incremental-doc-update.md  # NEW: Selective updates                                                          │
│ │                                                                                                                    │
│ └── templates/                                                                                                       │
│     └── (existing templates...)                                                                                      │
│                                                                                                                      │
│ ---                                                                                                                  │
│ Implementation Phases (Adjusted)                                                                                     │
│                                                                                                                      │
│ Phase 1: Core Playbook Infrastructure                                                                                │
│                                                                                                                      │
│ 1. Create playbooks/PLAYBOOK-GUIDE.md with decision tree                                                             │
│ 2. Create prompts/delta-analysis.md                                                                                  │
│ 3. Create workflows/incremental-doc-update.md                                                                        │
│ 4. Update WORKFLOW-INDEX.md with new playbook section                                                                │
│                                                                                                                      │
│ Phase 2: Complete SDLC Role Playbooks                                                                                │
│                                                                                                                      │
│ 1. Create prompts/role-playbooks/ directory                                                                          │
│ 2. Create playbooks for ALL SDLC roles:                                                                              │
│                                                                                                                      │
│ Product & Planning Roles:                                                                                            │
│ - product-owner.md - Backlog analysis, story prioritization, value mapping                                           │
│ - business-analyst.md - Requirements elicitation, process flows, gap analysis                                        │
│ - ux-designer.md - UI inventory, accessibility audit, component patterns                                             │
│                                                                                                                      │
│ Development Roles:                                                                                                   │
│ - frontend-dev.md - Component patterns, UI conventions, state management                                             │
│ - backend-dev.md - API patterns, service conventions, data access                                                    │
│ - fullstack-dev.md - End-to-end patterns, integration points                                                         │
│                                                                                                                      │
│ Quality Roles:                                                                                                       │
│ - qa-engineer.md - Test gaps, AC validation, E2E generation, coverage matrix                                         │
│ - qa-automation.md - Test framework setup, CI test integration                                                       │
│                                                                                                                      │
│ Operations Roles:                                                                                                    │
│ - devops-engineer.md - CI/CD analysis, deployment patterns, infrastructure                                           │
│ - sre.md - Observability, SLOs, incident patterns, runbooks                                                          │
│ - security-engineer.md - Security scan, OWASP checklist, auth/authz review                                           │
│                                                                                                                      │
│ Architecture & Leadership Roles:                                                                                     │
│ - architect.md - C4 diagrams, risk hotspots, tech debt, ADRs                                                         │
│ - tech-lead.md - Code review checklist, PR analysis, team conventions                                                │
│ - engineering-manager.md - Health metrics, velocity patterns, tech debt prioritization                               │
│                                                                                                                      │
│ Support Roles:                                                                                                       │
│ - dba.md - Schema analysis, query patterns, migration review                                                         │
│ - technical-writer.md - Doc audit, API docs, user guides                                                             │
│ - release-manager.md - Release checklist, changelog, version strategy                                                │
│ - support-engineer.md - Troubleshooting guides, FAQ generation, known issues                                         │
│                                                                                                                      │
│ 3. Update QUICK-START.md with role-specific examples                                                                 │
│                                                                                                                      │
│ Phase 3: DEFERRED - CI/CD Integration                                                                                │
│                                                                                                                      │
│ - GitHub Actions workflow                                                                                            │
│ - Claude CLI integration pattern                                                                                     │
│ - To be implemented in future iteration                                                                              │
│                                                                                                                      │
│ Phase 4: DEFERRED - Atlassian MCP Integration                                                                        │
│                                                                                                                      │
│ - Confluence publishing workflow                                                                                     │
│ - Release documentation automation                                                                                   │
│ - To be implemented in future iteration                                                                              │
│                                                                                                                      │
│ ---                                                                                                                  │
│ Verification Plan                                                                                                    │
│                                                                                                                      │
│ 1. Test Playbook Guide:                                                                                              │
│   - Walk through decision tree with sample scenarios                                                                 │
│   - Verify all roles map to correct playbook                                                                         │
│ 2. Test Delta Analysis:                                                                                              │
│   - Run delta-analysis.md against a sample git diff                                                                  │
│   - Verify it identifies affected documentation sections                                                             │
│ 3. Test Role Playbooks:                                                                                              │
│   - Run each of the 18 role playbooks against GenDD-Flow itself or a test repo                                        │
│   - Verify outputs are actionable and role-appropriate                                                               │
│   - Sample test order:                                                                                               │
│       - architect.md → Should produce C4 insights, risk hotspots                                                     │
│     - qa-engineer.md → Should produce test gap matrix                                                                │
│     - devops-engineer.md → Should produce CI/CD analysis                                                             │
│     - (Continue for remaining 15 playbooks)                                                                          │
│                                                                                                                      │
│ ---                                                                                                                  │
│ Critical Files to Modify                                                                                             │
│ ┌───────────────────┬─────────────────────────────────┐                                                              │
│ │       File        │             Change              │                                                              │
│ ├───────────────────┼─────────────────────────────────┤                                                              │
│ │ WORKFLOW-INDEX.md │ Add Playbooks section           │                                                              │
│ ├───────────────────┼─────────────────────────────────┤                                                              │
│ │ QUICK-START.md    │ Add role-specific quick prompts │                                                              │
│ ├───────────────────┼─────────────────────────────────┤                                                              │
│ │ README.md         │ Add playbook overview section   │                                                              │
│ ├───────────────────┼─────────────────────────────────┤                                                              │
│ │ .cursorrules.md   │ Add playbook triggers           │                                                              │
│ └───────────────────┴─────────────────────────────────┘                                                              │
│ ---                                                                                                                  │
│ User Decisions                                                                                                       │
│ ┌────────────────┬───────────────────────────────┐                                                                   │
│ │    Question    │           Decision            │                                                                   │
│ ├────────────────┼───────────────────────────────┤                                                                   │
│ │ CI/CD Platform │ Deferred (skip for now)       │                                                                   │
│ ├────────────────┼───────────────────────────────┤                                                                   │
│ │ Role Playbooks │ ALL SDLC roles (18 playbooks) │                                                                   │
│ ├────────────────┼───────────────────────────────┤                                                                   │
│ │ PR Automation  │ Deferred                      │                                                                   │
│ ├────────────────┼───────────────────────────────┤                                                                   │
│ │ Confluence MCP │ Deferred                      │                                                                   │
│ └────────────────┴───────────────────────────────┘                                                                   │
│ ---                                                                                                                  │
│ Adjusted Scope (This Implementation)                                                                                 │
│                                                                                                                      │
│ IN SCOPE:                                                                                                            │
│ - Playbook guide with decision tree                                                                                  │
│ - Delta analysis prompt                                                                                              │
│ - Incremental doc update workflow                                                                                    │
│ - 18 role-specific playbooks covering full SDLC:                                                                     │
│   - Product & Planning: Product Owner, Business Analyst, UX Designer                                                 │
│   - Development: Frontend Dev, Backend Dev, Full-Stack Dev                                                           │
│   - Quality: QA Engineer, QA Automation                                                                              │
│   - Operations: DevOps Engineer, SRE, Security Engineer                                                              │
│   - Architecture & Leadership: Architect, Tech Lead, Engineering Manager                                             │
│   - Support: DBA, Technical Writer, Release Manager, Support Engineer                                                │
│                                                                                                                      │
│ DEFERRED:                                                                                                            │
│ - GitHub Actions / CI/CD integration                                                                                 │
│ - Atlassian MCP / Confluence publishing                                                                              │
│ - Auto-commit documentation changes                                                                                  │
│ - Release documentation workflow  
