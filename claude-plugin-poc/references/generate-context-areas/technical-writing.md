# Technical Writing -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Technical Writing lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Documentation directories | HIGH | `docs/`, `documentation/`, `wiki/`, `guides/` |
| README files | HIGH | `README.md`, `README.rst` at root and in subdirectories |
| API documentation files | HIGH | `openapi.yaml`, `swagger.json`, Redoc config, API doc directories |
| Doc build system config | MEDIUM | `docusaurus.config.js`, `mkdocs.yml`, `_config.yml`, `.readthedocs.yml` |
| Changelog files | MEDIUM | `CHANGELOG.md`, `HISTORY.md`, `RELEASES.md` |
| Contributing guide | MEDIUM | `CONTRIBUTING.md`, `CONTRIBUTING.rst` |
| Inline doc comment conventions | LOW | JSDoc, TSDoc, GoDoc, Python docstrings in source files |
| Architecture decision records | LOW | `docs/adr/`, `ADR-*.md`, decision record files |
| Diagram source files | LOW | `.puml`, `.mmd`, `.drawio` files in docs |

## What to Analyze

### Documentation Inventory
- Look for: All existing documentation files with their type, location, and last update date
- Look for: Documentation categories present (getting started, installation, configuration, API reference, tutorials, troubleshooting, contributing, changelog)
- Assess: Whether documentation covers the essential categories for the project type
- Document: Documentation inventory with type, location, last updated, and quality rating

### API Documentation Analysis
- Look for: Endpoint documentation coverage (how many endpoints are documented?)
- Look for: Request/response examples for documented endpoints
- Look for: Error code documentation
- Look for: Authentication documentation
- Look for: Rate limit documentation
- Look for: OpenAPI/Swagger spec file presence and freshness
- Look for: Interactive API documentation (Swagger UI, Redoc)
- Assess: API documentation completeness and usefulness for consumers
- Document: API doc coverage table with endpoint count, documented count, and quality per section

### Code Documentation
- Look for: Public function/method documentation coverage
- Look for: Class/module documentation presence
- Look for: Complex logic documentation (comments explaining "why")
- Look for: Configuration documentation (env vars, feature flags, settings)
- Look for: Doc comment style consistency (JSDoc, TSDoc, GoDoc, docstrings)
- Assess: Whether code documentation aids understanding or is outdated/misleading
- Document: Code documentation coverage by element type with quality assessment

### User-Facing Documentation
- Look for: End user guides and their target audience
- Look for: Tutorial coverage for key features
- Look for: Onboarding flow documentation
- Look for: FAQ or troubleshooting sections
- Assess: Whether user documentation matches actual product behavior
- Document: User documentation inventory with audience, purpose, and quality

### Documentation Quality Assessment
- Look for: Readability and appropriate technical level for target audience
- Look for: Outdated content (references to deprecated features, old screenshots)
- Look for: Broken links (internal and external)
- Look for: Missing examples (code samples, configuration examples)
- Look for: Undefined jargon or assumed knowledge
- Look for: Inconsistent formatting (heading styles, code block styles, link patterns)
- Assess: Overall documentation quality and maintainability
- Document: Quality issues inventory with type, count, severity, and examples

### Documentation Gaps
- Look for: Missing critical documentation (README, getting started, API reference)
- Look for: Outdated documentation that may mislead
- Look for: Features without any documentation
- Look for: Setup/installation gaps (undocumented prerequisites, environment setup)
- Assess: Impact of each gap on different audiences (developers, end users, admins)
- Document: Gap inventory prioritized by audience impact and effort to fill

### Documentation Infrastructure
- Look for: Static site generator for documentation (Docusaurus, MkDocs, GitBook, VitePress)
- Look for: Version-controlled documentation (docs alongside code)
- Look for: Documentation search capability
- Look for: CI/CD pipeline for documentation builds
- Look for: Contribution process for documentation updates
- Look for: Documentation templates
- Assess: Whether documentation infrastructure supports sustainable maintenance
- Document: Infrastructure summary with tools, publishing process, and contribution workflow

### Style Consistency
- Look for: Consistent heading hierarchy
- Look for: Code block formatting and language tags
- Look for: Link style consistency (relative vs absolute, anchor patterns)
- Look for: Image handling (alt text, sizing, location)
- Look for: Terminology consistency across documents
- Assess: Whether a style guide is followed (explicitly or implicitly)
- Document: Style consistency audit with issues and recommendations

## Key Questions to Answer

1. What documentation exists and what categories are covered?
2. How complete is the API documentation (endpoints, examples, errors)?
3. What is the code documentation coverage for public functions and classes?
4. Is there adequate user-facing documentation for the target audience?
5. What documentation quality issues exist (outdated, broken links, missing examples)?
6. What are the most critical documentation gaps?
7. What documentation infrastructure is in place for building and publishing?
8. Is there a documentation contribution process?
9. Does documentation keep pace with code changes?
10. What documentation improvements would have the highest impact?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Docs-as-Code | Docs in repo, Markdown, CI builds docs | Sustainable, version-controlled |
| Generated API Docs | OpenAPI spec, auto-generated reference | Up-to-date API docs, may lack context |
| Wiki-Based Docs | External wiki links, Confluence references | May be out of sync with code |
| README-Only | Only root README, no dedicated docs | Minimal documentation, scaling issues |
| Stale Documentation | Last updated months ago while code changed | Misleading, worse than no docs |
| Comprehensive Docs | Multiple categories, recent updates, good structure | Mature documentation practice |
| Doc-Comment Driven | Rich inline comments, auto-generated from code | Good for API reference, may lack guides |
| No Documentation | Missing README or one-liner README | Documentation debt, onboarding barrier |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No README or empty README | Missing or stub README.md at root | HIGH |
| No API documentation | Missing OpenAPI spec, no endpoint docs | HIGH |
| Outdated getting started guide | Setup instructions that do not match current tooling | HIGH |
| Broken links in documentation | References to moved/deleted pages or external dead links | MEDIUM |
| No code comments on public API | Public functions/classes without doc comments | MEDIUM |
| Documentation not in version control | Docs in external wiki, no change tracking | MEDIUM |
| Missing changelog | No CHANGELOG.md, no release notes | MEDIUM |
| No contributing guide | No CONTRIBUTING.md, undocumented development process | LOW |
| Inconsistent terminology | Same concept referred to by different names | LOW |
| No documentation build pipeline | Docs require manual publishing | LOW |

## Output Guidance

### Must Include
- Documentation inventory with categories, locations, and quality ratings
- API documentation coverage assessment
- Critical documentation gaps prioritized by impact
- Documentation quality issues (outdated content, broken links, missing examples)
- Recommendations for highest-impact improvements

### Should Include (if detected)
- Code documentation coverage by element type
- User-facing documentation analysis for target audience
- Documentation infrastructure assessment
- Style consistency audit
- Documentation roadmap with phased improvement plan

### Related Areas
- [backend-development](./backend-development.md) -- API patterns that need documentation
- [frontend-development](./frontend-development.md) -- component documentation, Storybook
- [architecture](./architecture.md) -- architecture documentation, ADRs, C4 diagrams
- [product-management](./product-management.md) -- feature documentation for users
- [support-engineering](./support-engineering.md) -- troubleshooting guides, FAQ, known issues
- [user-experience](./user-experience.md) -- user-facing help content, onboarding guides
