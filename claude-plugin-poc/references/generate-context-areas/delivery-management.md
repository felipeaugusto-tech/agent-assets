# Delivery Management -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Delivery Management lens.
> This area combines Scrum Master and Engineering Manager perspectives focused on delivery flow, team health, and process effectiveness.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| PR/commit history with velocity indicators | HIGH | Merge frequency, PR size patterns, revert rate in git history |
| CI/CD pipeline with deployment stages | HIGH | `.github/workflows/`, deploy stages, environment promotion |
| Test coverage configuration and reports | MEDIUM | Coverage thresholds, test result artifacts in CI |
| Issue/project management integration | MEDIUM | Jira references in commits, GitHub Issues, linear.app links |
| Branch protection and review rules | MEDIUM | `CODEOWNERS`, branch protection config, required reviewers |
| Release tags and versioning | MEDIUM | Git tags, CHANGELOG.md, version files |
| Code ownership patterns | LOW | CODEOWNERS file, consistent contributors per module |
| Documentation maintenance signals | LOW | Doc updates frequency, README freshness |
| Tech debt tracking | LOW | TODO comments, tech debt labels in issues, refactoring commits |

## What to Analyze

### Codebase Health Metrics
- Look for: Code coverage percentage and threshold configuration
- Look for: Tech debt ratio indicators (TODO count, complexity scores, dependency freshness)
- Look for: Build and test execution times
- Look for: Linting error counts and quality gate configuration
- Assess: Whether health metrics are trending positive, stable, or declining
- Document: Health metrics dashboard with current values, benchmarks, and trend indicators

### Development Velocity Indicators
- Look for: PR size patterns (average lines changed)
- Look for: PR review and merge times
- Look for: PR rejection and revert rates
- Look for: Deployment frequency from CI/CD history
- Look for: Lead time for changes (commit to deploy)
- Look for: Change failure rate indicators
- Assess: DORA metrics approximation from available data
- Document: Velocity indicator summary with DORA metrics where measurable

### Complexity and Risk Analysis
- Look for: Files with high change frequency (hotspots)
- Look for: Modules with high complexity scores
- Look for: Bus factor assessment (contributor count per module)
- Assess: Risk score combining change frequency, complexity, and contributor count
- Document: Hotspot analysis with risk scores and cross-training recommendations

### Technical Debt Impact
- Look for: Debt categories (architecture, code quality, test, documentation, infrastructure)
- Look for: Debt item count and estimated effort per category
- Look for: Velocity impact of debt (rework percentage, workaround frequency)
- Look for: Debt interest calculation (ongoing monthly cost of not addressing)
- Assess: Which debt items have the highest ROI if addressed
- Document: Debt inventory with category, effort, velocity impact, and ROI ranking

### Team Allocation Indicators
- Look for: Commit patterns by type (feature, fix, refactor, infra, docs)
- Look for: Bug fix vs. feature development ratio
- Look for: Time spent on tech debt vs. new features
- Look for: Infrastructure and tooling investment signals
- Assess: Whether allocation matches stated priorities
- Document: Allocation analysis with estimated percentages per activity type

### Quality Indicators
- Look for: Bug rate patterns (bugs per release, trend over time)
- Look for: Critical bug frequency in recent history
- Look for: Flaky test rate and test maintenance burden
- Look for: Missing critical test coverage areas
- Assess: Quality trend and whether it supports sustainable delivery
- Document: Quality indicator summary with values, trends, and concerning patterns

### Definition of Ready Compliance
- Look for: Whether stories have clear problem statements
- Look for: Acceptance criteria presence and format (Gherkin in dedicated field)
- Look for: Scope boundary definitions
- Look for: Integration impact identification
- Look for: Security review need identification
- Look for: Documented unknowns and assumptions
- Assess: DoR compliance rate and common failure modes
- Document: DoR compliance assessment with gap frequency and rework cost

### Definition of Done Compliance
- Look for: Acceptance criteria validation evidence
- Look for: Expected behavior verification (not just "it works")
- Look for: Security concern resolution for flagged items
- Look for: Integration behavior verification
- Look for: Test evidence (manual or automated)
- Look for: User-visible change documentation
- Look for: Automation coverage or documented deferral reason
- Assess: DoD compliance rate and common shortcuts
- Document: DoD compliance assessment with enforcement gaps

### Delivery Flow and Bottlenecks
- Look for: Handoff points between roles (product to dev, dev to QA, QA to release)
- Look for: Queue depth at each stage (PRs waiting review, items waiting QA)
- Look for: Blocking patterns and resolution time
- Look for: Reopen and rework patterns
- Assess: Where work stalls and what causes it
- Document: Bottleneck analysis with severity, root cause, and distinction between process vs. structural issues

### Delivery Metrics That Drive Action
- Look for: Metrics that trigger real decisions (defect leakage, reopen rate, velocity, release failures)
- Look for: Metrics that are reported but not acted upon
- Assess: Whether metrics are signal or noise
- Document: Actionable metrics inventory with review cadence and decision triggers

### Rework Signals
- Look for: Story reopen rate (target <5%, warning 5-15%, critical >15%)
- Look for: QA-discovered requirements rate (target <10%)
- Look for: Security-blocked release frequency
- Look for: Reverts from integration issues
- Look for: Late scope changes within sprints
- Assess: Whether rework is driven by upstream quality (input) or downstream execution
- Document: Rework signal analysis with root causes and prevention recommendations

### AI and Automation Readiness
- Look for: Consistency of AI tool usage patterns
- Look for: Context quality provided to AI tools
- Look for: Prompt/template reuse across team
- Look for: Human-in-the-loop verification checkpoints
- Assess: Whether AI guardrails exist and who owns them
- Document: AI readiness assessment with governance gaps

## Key Questions to Answer

1. What are the DORA metrics (deploy frequency, lead time, change failure rate, MTTR)?
2. Where are the delivery bottlenecks and what causes them?
3. What is the tech debt ROI ranking (which items to address first)?
4. What is the team allocation split (features vs. bugs vs. debt vs. infra)?
5. Are stories meeting Definition of Ready before entering sprints?
6. Are stories meeting Definition of Done before release?
7. What rework signals exist and what is their root cause?
8. What is the bus factor risk for critical modules?
9. Are quality metrics trending in the right direction?
10. What delivery improvements would have the highest impact?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Healthy Delivery Flow | Regular deploys, low revert rate, balanced pyramid | Sustainable velocity |
| Input Quality Problem | High rework, QA finding requirements, reopens | DoR not enforced, upstream quality gaps |
| Tech Debt Spiral | Increasing bug rate, slowing velocity, growing fix-to-feature ratio | Debt interest exceeding capacity |
| Bus Factor Risk | Single contributor to critical modules, no documentation | Knowledge silos, team fragility |
| Metric Theater | Many dashboards, no action taken on signals | Process compliance without substance |
| Shift-Left Success | Low rework, testable ACs, early security flags | Effective upstream quality |
| Release Train | Regular cadence, predictable deployments | Sustainable delivery rhythm |
| Continuous Deployment | Every merge triggers production deploy | Fast feedback, requires strong testing |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| Story reopen rate >15% | Git history showing frequent reopens/reverts | HIGH |
| No Definition of Ready enforcement | Stories entering sprints without ACs or scope | HIGH |
| Bus factor of 1 on critical modules | Single contributor per module in git history | HIGH |
| Increasing bug-to-feature ratio | Commit pattern analysis showing growing fix percentage | MEDIUM |
| PR review time >48 hours average | Git PR history showing slow review cycles | MEDIUM |
| No DORA metrics visibility | Missing deploy frequency, lead time, failure rate tracking | MEDIUM |
| Tech debt >20% of velocity | Significant time spent on workarounds and rework | MEDIUM |
| Missing automation deferral tracking | Tests deferred without documented reason | LOW |
| No retrospective action tracking | Improvement actions not followed through | LOW |

## Output Guidance

### Must Include
- DORA metrics approximation (deploy frequency, lead time, change failure rate, MTTR)
- Delivery bottleneck analysis with root causes
- Tech debt impact assessment with ROI ranking
- Codebase health metrics dashboard (coverage, complexity, freshness)
- Rework signal analysis with upstream vs. downstream root causes

### Should Include (if detected)
- DoR/DoD compliance assessment with gap frequency
- Bus factor risk map with cross-training recommendations
- Team allocation analysis (features vs. fixes vs. debt)
- Quality trend indicators (bug rate, flaky tests, critical bugs)
- Actionable metrics inventory with decision triggers
- AI readiness assessment with governance recommendations

### Related Areas
- [quality-assurance](./quality-assurance.md) -- test coverage, test quality, gap analysis
- [architecture](./architecture.md) -- tech debt inventory, complexity analysis
- [release-management](./release-management.md) -- release process, deployment frequency
- [product-management](./product-management.md) -- story/epic quality, backlog readiness
- [devops-infrastructure](./devops-infrastructure.md) -- CI/CD pipeline, deployment automation
- [technical-leadership](./technical-leadership.md) -- code quality, conventions, PR standards
