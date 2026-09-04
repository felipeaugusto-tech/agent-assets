# Technical Leadership -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Technical Leadership lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Linting and formatting configuration | HIGH | `.eslintrc`, `.prettierrc`, `golangci-lint.yml`, `.editorconfig` |
| PR template and review configuration | HIGH | `.github/pull_request_template.md`, `CODEOWNERS`, branch protection rules |
| Code quality tooling | HIGH | SonarQube config, CodeClimate, quality gate definitions |
| Architecture documentation | MEDIUM | `docs/architecture/`, ADR files, architecture diagrams |
| Coding standards documentation | MEDIUM | `CONTRIBUTING.md`, `CODING_STANDARDS.md`, `CONVENTIONS.md` |
| CI pipeline with quality gates | MEDIUM | Lint, type-check, test, coverage threshold in CI config |
| Onboarding documentation | LOW | `docs/onboarding/`, `GETTING_STARTED.md`, setup guides |
| Development workflow config | LOW | Git hooks (husky, pre-commit), commit message linting |

## What to Analyze

### Code Quality Assessment
- Look for: Code coverage percentage and configured thresholds
- Look for: Cyclomatic complexity indicators (average and maximum)
- Look for: Code duplication percentage
- Look for: Linting error count and severity
- Look for: Type coverage (for TypeScript or typed languages)
- Assess: Whether quality metrics meet team standards
- Document: Quality metrics dashboard with values, thresholds, and pass/fail status

### Code Smells Inventory
- Look for: Long methods (>50 lines)
- Look for: God classes (>500 lines, multiple responsibilities)
- Look for: Feature envy (methods using other class data more than their own)
- Look for: Dead code (unreachable code, unused exports, commented-out blocks)
- Look for: Magic numbers and hardcoded strings
- Assess: Severity and refactoring priority for each smell category
- Document: Code smell inventory with occurrences, severity, and example locations

### Conventions Analysis
- Look for: Naming conventions for files, classes, functions, variables, and constants
- Look for: Code organization patterns (file structure, import order, export style)
- Look for: Test file location conventions (co-located, separate directory)
- Look for: Whether conventions are documented or only implicit
- Assess: Consistency of convention adherence across the codebase
- Document: Convention reference table with rules, consistency rating, and examples

### PR and Code Review Standards
- Look for: PR template presence and content
- Look for: Required reviewer count and CODEOWNERS configuration
- Look for: CI checks required before merge
- Look for: PR size guidelines and enforcement
- Look for: Review SLA (time to review)
- Look for: DoD-aligned review checklist (AC verification, security, tests, integration)
- Assess: Review process maturity and enforcement
- Document: Code review standards summary with current state and gaps

### Development Workflow
- Look for: Branching strategy (trunk-based, GitFlow, feature branches)
- Look for: Branch naming conventions
- Look for: Commit message standards (conventional commits, commit linting)
- Look for: Merge strategy (squash, rebase, merge commit)
- Look for: Automated formatting and linting (pre-commit hooks)
- Assess: Workflow maturity and automation level
- Document: Development workflow summary with branching, commit, and merge patterns

### Documentation Assessment
- Look for: README quality and completeness
- Look for: API documentation coverage
- Look for: Inline code comments quality and coverage
- Look for: Architecture documentation presence
- Look for: Onboarding guide existence and quality
- Assess: Whether documentation enables new developer productivity
- Document: Documentation inventory with type, quality, and priority gaps

### Team Productivity Indicators
- Look for: PR merge time patterns
- Look for: Average PR size (lines changed)
- Look for: Revert and hotfix frequency
- Look for: Build and test execution time
- Look for: Development environment setup complexity
- Assess: Whether tooling and process support fast feedback loops
- Document: Productivity indicators with values, trends, and improvement opportunities

### Onboarding Readiness
- Look for: Setup guide completeness and accuracy
- Look for: Architecture overview availability
- Look for: Coding standards documentation
- Look for: Common tasks guide
- Look for: Debugging guide
- Assess: How quickly a new developer can become productive
- Document: Onboarding checklist with existence, quality, and priority for each item

### DoD Technical Verification
- Look for: Whether code review confirms implementation matches acceptance criteria
- Look for: Whether security-flagged items are resolved before merge
- Look for: Whether integration points have test coverage
- Look for: Whether adequate test coverage is added for new behavior
- Look for: Whether automation deferral is documented with reason
- Assess: DoD enforcement in the review process
- Document: DoD verification checklist with enforcement status per criterion

## Key Questions to Answer

1. What are the code quality metrics and do they meet thresholds?
2. What coding conventions are followed and are they enforced?
3. What does the code review process look like and is it effective?
4. What branching and merge strategy is used?
5. What code smells exist and which should be prioritized?
6. Is documentation sufficient for new developer onboarding?
7. What quality gates exist in the CI pipeline?
8. Are PR sizes manageable and review times reasonable?
9. Is the Development Environment easy to set up?
10. Is DoD verified during code review?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Strong Quality Culture | Enforced linting, high coverage, fast reviews | Sustainable code quality |
| Convention-Driven Development | Documented standards, automated enforcement, consistent codebase | Low friction, predictable code |
| Review Bottleneck | Long PR review times, few reviewers, large PRs | Slow feedback, merge conflicts |
| Documentation Deficit | Missing README, no onboarding guide, outdated architecture docs | Slow onboarding, tribal knowledge |
| Automated Quality Gates | Pre-commit hooks, CI quality checks, required coverage | Shift-left quality enforcement |
| Technical Excellence | Low complexity, high cohesion, clean abstractions | Maintainable, extensible codebase |
| Knowledge Silos | Single contributor areas, no code ownership documentation | Bus factor risk |
| Tooling Investment | Fast builds, automated formatting, developer productivity tools | Efficient development workflow |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No linting or formatting enforcement | Missing ESLint/Prettier config, no pre-commit hooks | MEDIUM |
| No PR review process | No required reviewers, no PR template | HIGH |
| No coding standards documentation | Missing CONTRIBUTING.md, no convention docs | MEDIUM |
| Average PR size >800 lines | Large PRs that are hard to review effectively | MEDIUM |
| PR review time >72 hours | Slow feedback loop causing context switching | MEDIUM |
| No onboarding documentation | New developers cannot self-serve setup | MEDIUM |
| Code coverage below configured threshold | Declining quality trend | MEDIUM |
| High revert rate (>5%) | Quality issues getting through review | HIGH |
| No quality gates in CI | Broken code can merge without checks | HIGH |
| No DoD verification in review | Implementation may not match acceptance criteria | MEDIUM |

## Output Guidance

### Must Include
- Code quality metrics dashboard (coverage, complexity, duplication, linting)
- Convention reference with naming, structure, and consistency assessment
- Code review process summary with PR template, reviewers, and CI checks
- Development workflow (branching, commits, merging)
- Top code smells with prioritized refactoring recommendations

### Should Include (if detected)
- Documentation inventory with quality and gap assessment
- Onboarding readiness checklist
- Team productivity indicators (PR size, review time, revert rate)
- DoD verification enforcement status
- Build and test time optimization opportunities

### Related Areas
- [architecture](./architecture.md) -- architectural conventions, ADRs, system design
- [backend-development](./backend-development.md) -- backend-specific conventions and patterns
- [frontend-development](./frontend-development.md) -- frontend-specific conventions and patterns
- [quality-assurance](./quality-assurance.md) -- test quality, coverage, naming conventions
- [delivery-management](./delivery-management.md) -- velocity indicators, DORA metrics
- [technical-writing](./technical-writing.md) -- documentation quality and coverage
