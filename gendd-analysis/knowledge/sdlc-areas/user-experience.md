# User Experience -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the User Experience lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| UI component library or directory | HIGH | `src/components/`, component files (`.tsx`, `.vue`, `.svelte`) |
| Design system or theme configuration | HIGH | `tailwind.config.js`, theme files, design token definitions, `styles/theme.ts` |
| Page/route definitions | HIGH | `pages/`, `views/`, route config files |
| Accessibility-related attributes | MEDIUM | `aria-*` attributes, `role` attributes, `alt` text in templates |
| Form components with validation | MEDIUM | Form libraries, validation schemas, form components |
| Responsive design breakpoints | MEDIUM | Media queries, responsive utility classes, breakpoint config |
| Animation or transition config | LOW | Framer Motion, GSAP, CSS transition definitions |
| Icon or asset libraries | LOW | Icon sets, SVG sprite sheets, image optimization config |
| i18n/localization files | LOW | Locale files, translation functions, i18n config |

## What to Analyze

### Component Inventory
- Look for: All UI components with their location, variants, and reuse count
- Look for: Component categorization (buttons, forms, navigation, layout, feedback, data display)
- Assess: Whether components are reusable or duplicated across features
- Assess: Component consistency (do similar components follow the same patterns?)
- Document: Component inventory with name, location, variants, usage count, and reusability

### Page/Screen Inventory
- Look for: All user-facing pages with their routes and purposes
- Look for: Page composition (which components are used on each page)
- Look for: Navigation structure and information architecture
- Assess: Whether page structure matches user mental models
- Document: Page inventory with route, purpose, and components used

### User Flow Analysis
- Look for: Key user journeys (onboarding, main task, checkout, settings)
- Look for: Entry points, decision points, and exit points in each flow
- Look for: Error states and recovery paths
- Look for: Friction points (excessive steps, confusing navigation, dead ends)
- Assess: Flow completeness and user experience quality
- Document: User flow map per key journey with steps, friction points, and improvement opportunities

### Accessibility Audit
- Look for: Semantic HTML usage (proper heading hierarchy, landmark elements)
- Look for: ARIA labels on interactive elements
- Look for: Color contrast indicators (CSS custom properties, theme colors)
- Look for: Keyboard navigation support (focus management, tab order)
- Look for: Focus indicators (visible focus states on interactive elements)
- Look for: Image alt text presence
- Look for: Form label associations
- Assess: WCAG 2.1 AA compliance indicators from code analysis
- Document: Accessibility checklist with pass/fail/partial per WCAG principle

### Design System Analysis
- Look for: Color palette consistency (number of unique colors, deviation from tokens)
- Look for: Typography consistency (font families, sizes, weights used)
- Look for: Spacing system (consistent spacing scale or ad-hoc values)
- Look for: Icon consistency (single icon set or mixed sources)
- Look for: Component visual consistency (do buttons, inputs, cards look consistent?)
- Assess: Design system maturity and adherence
- Document: Design system audit with consistency scores per element type

### Responsive Design
- Look for: Breakpoint definitions and where they are used
- Look for: Mobile-first vs. desktop-first approach
- Look for: Components that handle responsive layout changes
- Look for: Touch target sizing for mobile (minimum 44x44px)
- Assess: Whether responsive design covers all target device categories
- Document: Responsive design summary with breakpoints, approach, and device coverage

### Interaction Patterns
- Look for: Loading states and skeleton screens
- Look for: Error state presentations (inline errors, toast notifications, error pages)
- Look for: Empty state handling (no data scenarios)
- Look for: Form interaction patterns (inline validation, submit handling, success feedback)
- Look for: Navigation patterns (breadcrumbs, back navigation, deep linking)
- Assess: Whether interaction patterns are consistent and user-friendly
- Document: Interaction pattern inventory with implementation status and consistency

## Key Questions to Answer

1. What UI components exist and how reusable are they?
2. What pages/screens exist and how are they organized?
3. What are the key user journeys and where are the friction points?
4. How does the application perform against WCAG 2.1 AA accessibility standards?
5. Is there a consistent design system and how well is it followed?
6. How does the application handle responsive design across devices?
7. Are interaction patterns (loading, error, empty states) consistently handled?
8. What component patterns should new features follow?
9. Are there accessibility issues that need immediate attention?
10. What UX improvements would have the highest user impact?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Design System in Place | Theme config, token files, consistent component library | Mature UI, consistent experience |
| Component Library Without System | Many components but no design tokens or theme | Components exist but may be inconsistent |
| Accessibility-First Development | ARIA attributes, semantic HTML, focus management | Inclusive design, WCAG compliance |
| Accessibility Gaps | Missing alt text, no ARIA labels, div-soup | Accessibility debt, compliance risk |
| Responsive-First Design | Mobile-first media queries, fluid layouts | Good mobile experience |
| Desktop-Only Design | No media queries, fixed widths | Mobile users underserved |
| Component Duplication | Similar components in different locations | Design system opportunity |
| Pattern Library | Documented component examples, Storybook | Scalable UI development |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No semantic HTML | `div` and `span` for everything, missing heading hierarchy | HIGH |
| Missing ARIA labels on interactive elements | Buttons, links, inputs without accessible names | HIGH |
| No keyboard navigation | Missing focus styles, no keyboard event handlers | HIGH |
| No responsive design | Fixed pixel widths, no media queries or responsive utilities | MEDIUM |
| Inconsistent component patterns | Similar UI elements implemented differently | MEDIUM |
| No loading state handling | No skeleton screens, no loading indicators | MEDIUM |
| No error state UI | Errors fail silently or show generic messages | MEDIUM |
| No form validation feedback | Missing inline errors, no validation messages | MEDIUM |
| Color-only information encoding | Status conveyed only by color without text/icon alternative | MEDIUM |
| Missing focus indicators | No visible focus styles on interactive elements | MEDIUM |

## Output Guidance

### Must Include
- Component inventory with reusability assessment
- Page/screen inventory with routes and purposes
- Key user flow maps with friction points identified
- Accessibility assessment against WCAG 2.1 AA principles
- Design system consistency evaluation

### Should Include (if detected)
- Responsive design analysis with breakpoint coverage
- Interaction pattern inventory (loading, error, empty states)
- Design token and theme analysis
- Component duplication opportunities
- UX improvement recommendations prioritized by user impact

### Related Areas
- [frontend-development](./frontend-development.md) -- component architecture, styling approach, build tools
- [product-management](./product-management.md) -- user journeys, feature inventory, business value
- [quality-assurance](./quality-assurance.md) -- E2E testing of user flows, accessibility testing
- [technical-writing](./technical-writing.md) -- user-facing documentation, help content
- [support-engineering](./support-engineering.md) -- error messages, troubleshooting flows
