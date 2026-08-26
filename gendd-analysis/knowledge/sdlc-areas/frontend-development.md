# Frontend Development -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Frontend Development lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Frontend framework config | HIGH | `next.config.js`, `nuxt.config.ts`, `angular.json`, `vite.config.ts`, `svelte.config.js` |
| Component files | HIGH | `*.tsx`, `*.vue`, `*.svelte`, `*.component.ts`, `src/components/` |
| Package manager with frontend deps | HIGH | `package.json` with React/Vue/Angular/Svelte |
| State management config | MEDIUM | `store/`, `redux/`, `*Store.ts`, Zustand/MobX/Pinia imports |
| CSS/styling framework files | MEDIUM | `tailwind.config.js`, `*.module.css`, `styled-components`, `*.scss` |
| Build tool configuration | MEDIUM | `webpack.config.js`, `vite.config.ts`, `next.config.js` |
| Static assets directory | LOW | `public/`, `assets/`, `static/` |
| E2E test config for UI | LOW | `playwright.config.ts`, `cypress.config.ts` |

## What to Analyze

### Project Structure
- Look for: Directory layout for components, pages, hooks, stores, styles, utilities, and API layer
- Assess: Whether structure follows framework conventions or custom patterns
- Assess: Feature-based vs. type-based organization
- Document: Directory map with purpose and naming patterns per directory

### Component Patterns
- Look for: Component naming conventions (PascalCase, kebab-case)
- Look for: Props definition approach (TypeScript interfaces, PropTypes, inline)
- Look for: State management within components (hooks, class state, composition API)
- Look for: Side effect handling patterns (useEffect cleanup, lifecycle hooks)
- Look for: Composition patterns (children, render props, slots, compound components)
- Assess: Consistency of component structure across the codebase
- Document: Component pattern reference with naming, props, state, and composition conventions

### State Management
- Look for: Global state management library and configuration
- Look for: Store/slice structure and naming
- Look for: Action and selector patterns
- Look for: State normalization approach
- Assess: State architecture clarity and separation of concerns
- Document: State management approach with store inventory, action patterns, and data flow

### API Integration
- Look for: HTTP client library (axios, fetch, ky, got)
- Look for: API client abstraction patterns (hooks, services, generated clients)
- Look for: Request/response interceptors and error handling
- Look for: Caching strategy (React Query, SWR, Apollo Cache)
- Look for: Auth header injection (interceptors, middleware)
- Assess: Consistency of API integration patterns across features
- Document: API integration architecture with client pattern, caching, and error handling

### Styling Approach
- Look for: CSS methodology (BEM, Atomic, utility-first, CSS-in-JS)
- Look for: Design token and variable management (CSS custom properties, SCSS variables, theme config)
- Look for: Responsive design approach (mobile-first, desktop-first, breakpoint definitions)
- Look for: Theme support (light/dark modes, theme switching)
- Look for: Component style scoping (CSS modules, scoped styles, styled-components)
- Assess: Consistency of styling patterns and design token usage
- Document: Styling convention reference with methodology, variables, responsive approach, and theming

### Build and Development
- Look for: Dev server configuration (port, proxy, hot reload)
- Look for: Build output configuration (output directory, code splitting)
- Look for: Environment variable handling (prefix requirements like `VITE_*`, `NEXT_PUBLIC_*`)
- Look for: Code splitting and lazy loading patterns
- Look for: Bundle analysis configuration
- Document: Build tooling summary with dev/build commands, env var patterns, and optimization strategies

### Testing Patterns
- Look for: Unit test framework (Jest, Vitest) and component testing library (RTL, Vue Test Utils)
- Look for: E2E test framework (Playwright, Cypress) and test file patterns
- Look for: Test utilities, custom render functions, mock providers
- Assess: Coverage across component, hook, utility, and integration layers
- Document: Test pattern summary with frameworks, conventions, and coverage

### Conventions and Linting
- Look for: ESLint configuration and rules
- Look for: Prettier configuration
- Look for: Import ordering conventions (absolute vs relative, path aliases)
- Look for: File naming patterns and export conventions (named vs default)
- Assess: Whether conventions are enforced by tooling or only documented
- Document: Convention reference with linting rules, formatting, and import patterns

## Key Questions to Answer

1. What frontend framework and version is used?
2. How is the project structured (feature-based, type-based, hybrid)?
3. What component patterns and conventions are followed?
4. How is state managed and what is the store architecture?
5. How does the frontend communicate with the backend?
6. What styling approach and design system is used?
7. What build tool is used and how is code splitting configured?
8. What testing frameworks are used and what is covered?
9. What conventions should a new frontend developer follow?
10. What accessibility patterns are implemented?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Container/Presentational | Separate data-fetching and display components | Good separation of concerns |
| Compound Components | Provider + Consumer pattern, shared context | Complex but flexible API surface |
| Custom Hook Abstraction | `use*` hooks encapsulating logic | Reusable logic, testable in isolation |
| Render Props | Components accepting render functions | Flexible but can lead to nesting |
| Higher-Order Components | `with*` wrapper functions | Legacy pattern, may indicate older codebase |
| Atomic Design | Atoms, molecules, organisms, templates, pages | Structured component hierarchy |
| Feature Slices | Feature folders with co-located components, state, tests | Good modularity, clear ownership |
| Barrel Exports | `index.ts` re-exporting from folder | Clean imports but can cause circular deps |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No TypeScript or type checking | Missing `tsconfig.json`, all `.js`/`.jsx` files | MEDIUM |
| Unsafe innerHTML usage | Raw HTML injection without sanitization, `v-html` with user input | HIGH |
| No code splitting | Single large bundle, no lazy() or dynamic import() | MEDIUM |
| Missing error boundaries | No ErrorBoundary components, unhandled render errors | MEDIUM |
| No accessibility patterns | Missing ARIA attributes, no semantic HTML, no focus management | MEDIUM |
| Prop drilling through many levels | Props passed 3+ levels deep without context/store | LOW |
| Outdated dependencies | React <18, Vue 2, Angular <14, unmaintained packages | MEDIUM |
| No environment variable validation | Missing runtime checks for required env vars | LOW |
| Inconsistent component patterns | Mixed class/functional, inconsistent file structure | LOW |

## Output Guidance

### Must Include
- Framework, version, and build tool
- Project structure map with directory purposes
- Component patterns and conventions (naming, props, state, composition)
- State management architecture and store inventory
- API integration patterns with client library and error handling
- Styling approach with methodology and design tokens

### Should Include (if detected)
- Build optimization configuration (code splitting, lazy loading)
- Testing patterns and coverage by component type
- Accessibility implementation status
- Design system analysis with consistency assessment
- Convention reference for new developers

### Related Areas
- [architecture](./architecture.md) -- frontend architecture within overall system context
- [fullstack-development](./fullstack-development.md) -- frontend-backend contract and data flow
- [user-experience](./user-experience.md) -- component inventory, user flows, accessibility
- [quality-assurance](./quality-assurance.md) -- frontend testing patterns and E2E coverage
- [backend-development](./backend-development.md) -- API design that frontend consumes
