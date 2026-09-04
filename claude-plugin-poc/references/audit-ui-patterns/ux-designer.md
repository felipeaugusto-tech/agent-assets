# Role Playbook: UX Designer

**Role:** UX Designer
**Focus:** UI inventory, accessibility audit, component patterns, user flows
**Time:** 30-45 minutes

---

## Purpose

Analyze a codebase from a UX Designer perspective to understand:
- UI component inventory and patterns
- User flow implementations
- Accessibility compliance
- Design system adherence

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/ux-designer.md
Analyze @TargetRepo for UI patterns and accessibility.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/ux-designer.md

Analyze @TargetRepo from a UX Designer perspective:

## Context
- Product: [PRODUCT NAME]
- Design System: [If known - e.g., Material, Tailwind, Custom]
- Target Users: [USER PERSONAS]
- Devices: [Web/Mobile/Desktop/All]

## Phase 1: Component Inventory

Identify all UI components:
| Component | Location | Variants | Usage Count | Reusable? |
|-----------|----------|----------|-------------|-----------|
| [Button] | `components/` | Primary, Secondary | 50+ | Yes |
| [Form] | `components/forms/` | Login, Contact | 3 | Partial |

## Phase 2: Page/Screen Inventory

Map all user-facing pages:
| Page | Route/Path | Purpose | Components Used |
|------|------------|---------|-----------------|
| [Home] | `/` | Landing | Hero, NavBar, Footer |
| [Dashboard] | `/dashboard` | User overview | Sidebar, Cards, Charts |

## Phase 3: User Flow Analysis

For key user journeys:
| Flow | Entry Point | Steps | Exit Points | Friction Points |
|------|-------------|-------|-------------|-----------------|
| [Onboarding] | `/signup` | 5 | Dashboard, Abandon | Step 3 - too many fields |

## Phase 4: Accessibility Audit

Check for WCAG compliance indicators:
| Area | Check | Status | Files |
|------|-------|--------|-------|
| Semantic HTML | Using proper elements | Pass/Fail | [files] |
| ARIA labels | Interactive elements labeled | Pass/Fail | [files] |
| Color contrast | Sufficient contrast ratios | Pass/Partial/Fail | [files] |
| Keyboard nav | All functions keyboard accessible | Pass/Fail | [files] |
| Focus indicators | Visible focus states | Pass/Fail | [files] |
| Alt text | Images have alt attributes | Pass/Fail | [files] |
| Form labels | Inputs have associated labels | Pass/Fail | [files] |

## Phase 5: Design System Analysis

Evaluate design consistency:
| Element | Variants Found | Consistent? | Recommendation |
|---------|----------------|-------------|----------------|
| Colors | [List] | Yes/No | [Action] |
| Typography | [List] | Yes/No | [Action] |
| Spacing | [List] | Yes/No | [Action] |
| Icons | [Source] | Yes/No | [Action] |

## Phase 6: Responsive Design

Check responsive patterns:
| Breakpoint | Implemented | Pattern | Issues |
|------------|-------------|---------|--------|
| Mobile (<768px) | Yes/No | [Pattern] | [Issues] |
| Tablet (768-1024px) | Yes/No | [Pattern] | [Issues] |
| Desktop (>1024px) | Yes/No | [Pattern] | [Issues] |

## Phase 7: Recommendations

| Area | Issue | Impact | Recommendation | Priority |
|------|-------|--------|----------------|----------|
| [Area] | [Issue] | High/Med/Low | [Fix] | P1/P2/P3 |
```

---

## Output: UX Analysis Report

```markdown
# UX Analysis: [Product Name]
Generated: [Date]
Analyzed by: UX Designer Playbook

## UI Overview
[Summary of UI structure and patterns]

## Component Library

### Core Components
- **Buttons:** [variants, locations]
- **Forms:** [patterns, validation]
- **Navigation:** [patterns]
- **Cards/Containers:** [patterns]

### Component Consistency Score: [X/10]

## User Flows

### Flow: [Name]
```
[Start] → [Step 1] → [Decision] → [Step 2] → [End]
                  ↓
              [Alt Path]
```

### Friction Points
1. [Issue] - Impact: [description]

## Accessibility Report

### WCAG 2.1 AA Compliance
- [ ] Perceivable: [status]
- [ ] Operable: [status]
- [ ] Understandable: [status]
- [ ] Robust: [status]

### Critical Issues
| Issue | Location | Fix |
|-------|----------|-----|

## Design System Audit
[Consistency analysis]

## Recommendations
1. [High priority fix]
2. [Medium priority improvement]
3. [Nice to have enhancement]
```

---

## Playwright MCP Integration

For live UI analysis:

```
Read @GenDD-Flow/playbooks/by-role/ux-designer.md
Read @GenDD-Flow/playbooks/on-demand/run-assisted-testing.md

Using Playwright MCP on [APP_URL]:

1. Navigate to each major page
2. Screenshot at each breakpoint (mobile, tablet, desktop)
3. List all data-testid attributes
4. Check for accessibility attributes (aria-*, role, alt)
5. Document component patterns observed
```

---

## Follow-Up Actions

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
