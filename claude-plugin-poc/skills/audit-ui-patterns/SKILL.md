---
name: audit-ui-patterns
description: Inventory UI components, design tokens, and user flows, then audit accessibility (ARIA, contrast, keyboard nav, screen reader support) and flag inconsistent patterns. Manual invocation only.
disable-model-invocation: true
---

# Audit UI Patterns and Accessibility

For onboarding as a UX designer onto an unfamiliar frontend, prepping a design-system consolidation, or running an accessibility compliance pass. Produces one audit report, read-only against the codebase.

## 1. Fix the target

The target is **the user's current repository's frontend code**, never this plugin or the GenDD corpus.

Before analysis, confirm the target accessibility standard if it matters to the request (e.g. WCAG 2.1 AA) — don't assume one silently if the user cares about a specific bar.

## 2. Load the reference (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/audit-ui-patterns/audit-ui-patterns.md` | **Primary task flow.** |
| `${CLAUDE_PLUGIN_ROOT}/references/audit-ui-patterns/ux-designer.md` | **The actual analysis method** the primary flow delegates to — component inventory, theming analysis, accessibility audit, flow inventory, inconsistency report, prioritized recommendations. |

Reading these as they are: verbatim corpus copies, `@GenDD-Flow/...` and `@TargetRepo` links don't resolve here, describe a Cursor Chat workflow — adapt intent, ignore tool mechanics.

## 3. Run the process

1. **Map the frontend structure** — component directories, design tokens, theme files, shared UI libraries.
2. **Apply the UX designer analysis method** from `ux-designer.md` to produce:
   - Component inventory (shared, one-off, and duplicate components)
   - Design token / theming analysis
   - Accessibility audit (ARIA usage, color contrast, keyboard navigation, screen reader support)
   - Key user-flow inventory
   - Inconsistency report (divergent patterns, mixed conventions across the codebase)
   - Prioritized improvement recommendations
3. **Save the report** to `docs/ui-audit.md`.

## 4. Never invent

An accessibility finding not backed by an actual inspected component (ARIA attribute present/absent, contrast ratio computed, focus order traced) is a guess. If something can't be verified from the code alone (e.g. actual screen-reader behavior), say so as a limitation rather than asserting pass/fail.

## 5. Hard limits

- Writes only `docs/ui-audit.md` in the target repository.
- No code or configuration changes — this is an audit, not a fix.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
- Read-only against the codebase throughout.
