# Role Playbook: Frontend Developer

**Role:** Frontend Developer
**Focus:** Component patterns, UI conventions, state management, styling
**Time:** 30-45 minutes

---

## Purpose

Analyze a codebase from a Frontend Developer perspective to understand:
- Component architecture and patterns
- State management approach
- Styling conventions
- Build and bundling setup
- Testing patterns for frontend code

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/frontend-dev.md
Analyze @TargetRepo for frontend patterns and conventions.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/frontend-dev.md

Analyze @TargetRepo from a Frontend Developer perspective:

## Context
- Frontend Framework: [React | Vue | Angular | Svelte | Other]
- Styling: [CSS | SCSS | Tailwind | Styled-components | CSS Modules]
- State Management: [Redux | Zustand | MobX | Context | Pinia | Other]
- Build Tool: [Vite | Webpack | Next.js | Nuxt | Other]

## Phase 1: Project Structure

Map the frontend architecture:
| Directory | Purpose | Key Files |
|-----------|---------|-----------|
| `src/components/` | UI components | [patterns] |
| `src/pages/` | Page components | [patterns] |
| `src/hooks/` | Custom hooks | [patterns] |
| `src/store/` | State management | [patterns] |
| `src/styles/` | Styling | [patterns] |
| `src/utils/` | Utilities | [patterns] |
| `src/api/` | API layer | [patterns] |

## Phase 2: Component Patterns

Analyze component structure:
| Pattern | Example | Convention | Notes |
|---------|---------|------------|-------|
| Naming | [PascalCase/kebab] | `Button.tsx` | |
| Props | [TypeScript/PropTypes] | Interface defined | |
| State | [useState/class] | Functional + hooks | |
| Side effects | [useEffect pattern] | Cleanup handled | |
| Composition | [children/render props] | Slots pattern | |

## Phase 3: State Management

Document state architecture:
| Store/Slice | Purpose | Actions | Selectors |
|-------------|---------|---------|-----------|
| [auth] | Authentication state | login, logout | isAuthenticated |
| [user] | User data | fetch, update | currentUser |

State flow: [Diagram description]

## Phase 4: API Integration

How frontend talks to backend:
| Pattern | Implementation | Files |
|---------|----------------|-------|
| HTTP Client | [axios/fetch/ky] | `api/client.ts` |
| Request handling | [hooks/services] | `hooks/useApi.ts` |
| Error handling | [pattern] | [files] |
| Caching | [react-query/SWR/none] | [files] |
| Auth headers | [interceptor/manual] | [files] |

## Phase 5: Styling Approach

| Aspect | Convention | Example |
|--------|------------|---------|
| Methodology | [BEM/Atomic/Utility] | `.btn--primary` |
| Variables | [CSS vars/SCSS vars] | `--color-primary` |
| Responsive | [Mobile-first/Desktop-first] | `@media (min-width)` |
| Theme | [Light/Dark/Both] | `data-theme="dark"` |
| Component styles | [Scoped/Global] | `.module.css` |

## Phase 6: Build & Development

| Aspect | Tool/Config | Notes |
|--------|-------------|-------|
| Dev server | [command] | Port, hot reload |
| Build | [command] | Output dir |
| Env vars | [pattern] | `VITE_*` prefix |
| Code splitting | [method] | Lazy routes |
| Bundle analysis | [tool] | [if configured] |

## Phase 7: Testing

| Test Type | Framework | Pattern | Coverage |
|-----------|-----------|---------|----------|
| Unit | [Jest/Vitest] | `*.test.ts` | [%] |
| Component | [RTL/Vue Test Utils] | `*.spec.tsx` | [%] |
| E2E | [Playwright/Cypress] | `e2e/*.spec.ts` | [flows] |

## Phase 8: Conventions & Patterns

| Convention | Rule | Enforcement |
|------------|------|-------------|
| Linting | [ESLint config] | [rules] |
| Formatting | [Prettier config] | [rules] |
| Imports | [absolute/relative] | [alias pattern] |
| File naming | [pattern] | [example] |
| Component exports | [named/default] | [pattern] |
```

---

## Output: Frontend Developer Guide

```markdown
# Frontend Developer Guide: [Project Name]
Generated: [Date]
Analyzed by: Frontend Dev Playbook

## Quick Start for Frontend Devs

### Setup
```bash
[npm/yarn/pnpm] install
[npm/yarn/pnpm] run dev
```

### Key Directories
- Components: `src/components/`
- Pages: `src/pages/`
- State: `src/store/`
- API: `src/api/`

## Architecture Overview

### Component Tree
```
App
├── Layout
│   ├── Header
│   ├── Sidebar
│   └── Main
└── Routes
    ├── Home
    ├── Dashboard
    └── Settings
```

### State Flow
```
[Diagram of state management]
```

## Conventions

### Creating a New Component
```tsx
// src/components/MyComponent/MyComponent.tsx
// [Example following project conventions]
```
See `[example file path]` for reference implementation.

### API Calls
```tsx
// Pattern for API calls
// [Example following project conventions]
```
See `[example file path]` for reference implementation.

### Styling
```css
/* Pattern for styles */
/* [Example following project conventions] */
```
See `[example file path]` for reference implementation.

## Common Tasks

| Task | How To |
|------|--------|
| Add component | [steps] |
| Add page/route | [steps] |
| Add API endpoint | [steps] |
| Add state slice | [steps] |

## Testing

### Running Tests
```bash
[test command]
```

### Writing Tests
See `[example test file]` for pattern.

## Gotchas & Tips
1. [Important gotcha]
2. [Helpful tip]
3. [Common mistake to avoid]
```

---

## Reference Templates

This playbook's analysis areas align with the universal principles in the Context Pack template. Reference them for baseline expectations:

| Template | Relevant Sections |
|----------|-------------------|
| `templates/context-pack.md` (conventions.md section) | Naming conventions, SRP, component organization, formatting/linting, logging (environment-aware, levels, what never to log) |
| `templates/context-pack.md` (testing.md section) | AAA pattern, test naming, frontend/UI test scenarios |
| `templates/context-pack.md` (agents.md section) | Input validation, secure error handling, no hardcoded secrets |

---

## Follow-Up Actions

- For AI context setup: [Create Context Pack](../../workflows/create-context-pack.md) — so AI tools follow your frontend conventions and patterns
- For architecture overview: [Generate Architecture Diagrams](../../workflows/generate-architecture-diagrams.md) — understand system context and container relationships
- For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
