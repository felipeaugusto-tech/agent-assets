# Role Playbook: Technical Writer

**Role:** Technical Writer
**Focus:** Doc audit, API docs, user guides, documentation quality
**Time:** 30-45 minutes

---

## Purpose

Analyze a codebase from a Technical Writer perspective to understand:
- Documentation coverage and quality
- API documentation completeness
- User guide requirements
- Documentation maintenance needs

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/technical-writer.md
Analyze @TargetRepo for documentation gaps.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/technical-writer.md

Analyze @TargetRepo from a Technical Writer perspective:

## Context
- Product Type: [API | Web App | Library | CLI | Mixed]
- Audiences: [Developers | End Users | Admins | All]
- Doc Platform: [Markdown | Docusaurus | GitBook | Confluence | Other]
- Current Doc Location: [docs/ | wiki | external]

## Phase 1: Documentation Inventory

### Existing Documentation
| Document | Location | Type | Last Updated | Quality |
|----------|----------|------|--------------|---------|
| README.md | Root | Overview | [date] | Good/Fair/Poor |
| API docs | docs/api/ | Reference | [date] | Good/Fair/Poor |
| User guide | docs/guide/ | Tutorial | [date] | Good/Fair/Poor |
| Architecture | docs/arch/ | Concept | [date] | Good/Fair/Poor |

### Documentation Types Present
| Type | Present | Location | Completeness |
|------|---------|----------|--------------|
| Getting started | Yes/No | [path] | [%] |
| Installation | Yes/No | [path] | [%] |
| Configuration | Yes/No | [path] | [%] |
| API reference | Yes/No | [path] | [%] |
| Tutorials | Yes/No | [path] | [%] |
| Troubleshooting | Yes/No | [path] | [%] |
| Contributing | Yes/No | [path] | [%] |
| Changelog | Yes/No | [path] | [%] |

## Phase 2: API Documentation Analysis

### Coverage
| API Area | Endpoints | Documented | Examples | Status |
|----------|-----------|------------|----------|--------|
| [Auth] | [n] | [n] | [n] | Complete/Partial/Missing |
| [Users] | [n] | [n] | [n] | Complete/Partial/Missing |

### API Doc Quality
| Check | Status | Issues |
|-------|--------|--------|
| Request/response examples | Present/Missing | [gaps] |
| Error codes documented | Present/Missing | [gaps] |
| Authentication explained | Present/Missing | [gaps] |
| Rate limits documented | Present/Missing | [gaps] |
| Versioning explained | Present/Missing | [gaps] |

### OpenAPI/Swagger
| Aspect | Status |
|--------|--------|
| Spec file present | Yes/No |
| Spec up to date | Yes/No |
| Generated from code | Yes/No |
| Interactive docs | Yes/No |

## Phase 3: Code Documentation

### Inline Documentation
| Element | Coverage | Quality |
|---------|----------|---------|
| Public functions | [%] | Good/Fair/Poor |
| Classes | [%] | Good/Fair/Poor |
| Complex logic | [%] | Good/Fair/Poor |
| Configuration | [%] | Good/Fair/Poor |

### Doc Comments Style
| Language | Style Used | Consistent |
|----------|------------|------------|
| [TypeScript] | JSDoc/TSDoc | Yes/No |
| [Go] | GoDoc | Yes/No |
| [Python] | Docstrings | Yes/No |

## Phase 4: User-Facing Documentation

### End User Docs
| Document | Audience | Purpose | Quality |
|----------|----------|---------|---------|
| [Doc] | [Audience] | [Purpose] | Good/Fair/Poor/Missing |

### Tutorial Coverage
| Feature | Tutorial | Up to Date |
|---------|----------|------------|
| [Feature] | Yes/No | Yes/No |

### Onboarding Flow
| Step | Documented | Clear | Tested |
|------|------------|-------|--------|
| Installation | Yes/No | Yes/No | Yes/No |
| First use | Yes/No | Yes/No | Yes/No |
| Common tasks | Yes/No | Yes/No | Yes/No |

## Phase 5: Documentation Quality Assessment

### Readability Scores
| Document | Readability | Tech Level | Appropriate |
|----------|-------------|------------|-------------|
| [Doc] | [Score] | [Level] | Yes/No |

### Common Issues
| Issue | Occurrences | Examples |
|-------|-------------|----------|
| Outdated content | [n] | [files] |
| Broken links | [n] | [files] |
| Missing examples | [n] | [files] |
| Jargon undefined | [n] | [terms] |
| Inconsistent formatting | [n] | [files] |

### Style Consistency
| Element | Standard | Followed |
|---------|----------|----------|
| Headings | [Style] | Yes/No |
| Code blocks | [Style] | Yes/No |
| Links | [Style] | Yes/No |
| Images | [Style] | Yes/No |

## Phase 6: Documentation Gaps

### Missing Critical Docs
| Document | Audience | Priority | Effort |
|----------|----------|----------|--------|
| [Doc] | [Who needs it] | P1/P2/P3 | [days] |

### Outdated Docs
| Document | Last Updated | Staleness | Action |
|----------|--------------|-----------|--------|
| [Doc] | [date] | Critical/Moderate/Minor | Update/Archive/Delete |

## Phase 7: Documentation Infrastructure

### Doc Build System
| Aspect | Status | Tool |
|--------|--------|------|
| Static site generator | Yes/No | [tool] |
| Version control | Yes/No | [approach] |
| Search | Yes/No | [tool] |
| CI/CD for docs | Yes/No | [pipeline] |

### Contribution Process
| Aspect | Status |
|--------|--------|
| Doc contribution guide | Present/Missing |
| Templates | Present/Missing |
| Review process | Defined/Undefined |

## Phase 8: Recommendations

### High Priority (P1)
| Document | Action | Effort | Impact |
|----------|--------|--------|--------|
| [Doc] | Create/Update | [days] | [impact] |

### Medium Priority (P2)
| Document | Action | Effort | Impact |
|----------|--------|--------|--------|

### Nice to Have (P3)
| Document | Action | Effort | Impact |
|----------|--------|--------|--------|
```

---

## Output: Documentation Audit Report

```markdown
# Documentation Audit: [Project Name]
Generated: [Date]
Analyzed by: Technical Writer Playbook

## Documentation Health Score: [X/10]

## Coverage Summary

| Category | Coverage | Quality |
|----------|----------|---------|
| Getting Started | [%] | |
| API Reference | [%] | |
| User Guides | [%] | |
| Architecture | [%] | |

## Documentation Map

```
docs/
├── README.md           [✓ Good]
├── GETTING_STARTED.md  [⚠ Needs update]
├── api/
│   ├── auth.md        [✓ Good]
│   └── users.md       [✗ Missing examples]
└── guides/
    └── ...            [✗ Missing]
```

## API Documentation

### Coverage: [X/Y] endpoints documented

### Gaps
| Endpoint | Issue |
|----------|-------|

## Quality Issues

### Critical
- [Issue 1]

### Moderate
- [Issue 2]

## Recommendations

### Create
1. [New document] - [audience], [effort]

### Update
1. [Existing document] - [what to update]

### Improve
1. [Area] - [how to improve]

## Documentation Roadmap

### Sprint 1
- [ ] [Task]

### Sprint 2
- [ ] [Task]
```

---

## Follow-Up Actions

- For AI context files: [Create Context Pack](../../workflows/create-context-pack.md) — generates `agents.md`, `context.md`, `conventions.md`, `testing.md`, `architecture.md`
- For architecture diagrams: [Generate Architecture Diagrams](../../workflows/generate-architecture-diagrams.md) — C4 diagrams stored in `docs/architecture/`
- For incremental doc updates: [Update Documentation](../recurring/update-documentation.md) — keep docs current after code changes
- For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
