---
name: validate-acceptance-criteria
description: Validate Gherkin acceptance criteria against a running application using Playwright MCP -- check every element and outcome actually exists and is testable, then refine the ACs. Manual invocation only.
disable-model-invocation: true
---

# Validate Acceptance Criteria with Playwright

Confirms ACs are testable before sprint planning or automation, by driving the real application rather than trusting the prose. This skill **requires Playwright MCP** — the one exception to this plugin's usual "no MCP tools" limit.

## 1. Fix the target and gather inputs

The target is **the user's application**, running at an accessible URL — never this plugin or the GenDD corpus.

Before running anything, collect:
- The Gherkin acceptance criteria to validate (Given/When/Then).
- The application URL (staging or local).
- Test credentials, if the feature requires authentication.
- The feature area name.

Ask for whichever of these is missing — don't guess a URL or credentials.

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/validate-acceptance-criteria/validate-acceptance-criteria.md` | **Primary task flow** — the per-AC verification steps and the report format. |
| `${CLAUDE_PLUGIN_ROOT}/references/validate-acceptance-criteria/testing-standards.md` | Selector-naming rules (prefer `data-testid`) and implementation-specific test conventions. |
| `${CLAUDE_PLUGIN_ROOT}/references/validate-acceptance-criteria/testing.md` | Foundational testing principles (naming, structure) — the modern replacement for the deprecated Context Pack template's testing section; the primary flow references the old one, use this instead. |

Reading these as they are: verbatim corpus copies, `@GenDD-Flow/...` and `@TargetRepo/.cursor/...` links (the latter point at a deprecated context-pack format) don't resolve here — use the bundled `testing.md` in their place.

## 3. Run the process

Using Playwright MCP, for each acceptance criterion:

1. **Navigate** to the pages the AC references and screenshot each.
2. **Verify GIVEN** — confirm the precondition can actually be set up.
3. **Verify WHEN** — for each action, does the referenced element exist? What's its actual selector (`data-testid` preferred)? Is it visible/enabled in the expected state?
4. **Verify THEN** — can the outcome be asserted programmatically? What selector shows success/failure? Are error messages accessible?
5. **Classify** each AC: Fully Testable / Partially Testable / Not Testable.

Then:
- **Refine the ACs** using what was found — reference actual element names/selectors, add concrete assertion values, note discovered edge cases.
- **List action items** for anything blocking automation: missing `data-testid` attributes, test-data requirements, API mocks needed.

## 4. Never invent

A "Fully Testable" verdict without having actually navigated to the page and inspected the element is a guess, not a validation — the entire point of this skill is that it checks the live application instead of trusting the AC prose. If Playwright MCP isn't available or the app isn't reachable, say so and stop rather than producing a report that looks verified but isn't.

## 5. Hard limits

- **Playwright MCP is required and expected** for this skill — the one exception to the plugin's usual no-MCP-tools default.
- Writes only the validation report, to `docs/requirements/` or as instructed by the user (e.g. attached to a ticket) — never modifies application code.
- No other MCP tools.
- No builds, deploys, or non-Playwright test runs.
