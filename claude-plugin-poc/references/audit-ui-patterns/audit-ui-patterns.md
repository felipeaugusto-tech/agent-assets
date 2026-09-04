# Audit UI Patterns and Accessibility

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | UX Designer, Frontend Dev |
| **Prerequisites** | Repository cloned, frontend code accessible |
| **Inputs** | Path to the target repository |
| **Outputs** | UI inventory, accessibility audit, component pattern analysis |

## When to Use

- Onboarding as a UX designer and need to understand the existing UI landscape
- Preparing for a design system consolidation or component library effort
- Running an accessibility compliance audit

## Before You Start

- [ ] Repository is cloned and accessible
- [ ] You can identify the frontend framework and component structure
- [ ] You know the target accessibility standard (WCAG 2.1 AA, etc.)

## Steps

1. **Identify frontend structure**
   - Do: Locate all UI components, pages, and styling configuration
   - How: Search for component directories, design tokens, theme files, and shared UI libraries
   - Expect: A map of the frontend architecture and component hierarchy

2. **Run the UX Designer role-playbook analysis**
   - Do: Perform a role-specific deep analysis of UI patterns and accessibility
   - How: Use the following prompt:
     ```
     Read @GenDD-Flow/playbooks/by-role/ux-designer.md

     Analyze @TargetRepo focusing on UI patterns and accessibility.

     Generate:
     1. Component inventory (shared components, one-off components, duplicates)
     2. Design token / theming analysis
     3. Accessibility audit (ARIA usage, contrast, keyboard navigation, screen reader support)
     4. User flow inventory (key paths through the application)
     5. Inconsistency report (divergent patterns, mixed conventions)
     6. Improvement recommendations (prioritized)
     ```
   - Expect: A comprehensive UI and accessibility audit

3. **Document findings**
   - Do: Save the audit as a structured report
   - How: Save to `@TargetRepo/docs/ui-audit.md`
   - Expect: Actionable UI improvement plan

## Expected Output

```
TargetRepo/docs/
└── ui-audit.md
```

**Save to:** `@TargetRepo/docs/ui-audit.md`

## What's Next

- [ ] [Run Brownfield Analysis](../onboarding/run-brownfield-analysis.md) if full codebase analysis is needed
- [ ] [Generate Unit Tests](generate-unit-tests.md) for UI components

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| UX Designer Role Playbook | `playbooks/by-role/ux-designer.md` | Deep-dive UX analysis prompt |
| Frontend Dev Role Playbook | `playbooks/by-role/frontend-dev.md` | Frontend code analysis prompt |
