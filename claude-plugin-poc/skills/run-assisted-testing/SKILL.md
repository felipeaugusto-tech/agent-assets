---
name: run-assisted-testing
description: Discover a running application's pages and elements with Playwright MCP, then generate Page Objects, an E2E test suite, and test data fixtures from what was actually found. Manual invocation only.
disable-model-invocation: true
---

# Run Playwright Assisted Testing

Builds a Playwright test suite from real application discovery rather than assumptions about the UI. This skill **requires Playwright MCP** — the one exception to this plugin's usual "no MCP tools" limit.

## 1. Fix the target and gather inputs

The target is **the user's application**, running at an accessible URL — never this plugin or the GenDD corpus.

Collect before starting: the application base URL, login credentials if needed, and which pages/features need coverage.

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/run-assisted-testing/run-assisted-testing.md` | **Primary task flow** — discovery, selector inventory, Page Objects, test generation, fixtures, in order. |
| `${CLAUDE_PLUGIN_ROOT}/references/run-assisted-testing/testing-standards.md` | Selector-naming rules and implementation-specific conventions. |
| `${CLAUDE_PLUGIN_ROOT}/references/run-assisted-testing/testing.md` | Foundational testing principles (naming, AAA structure) — modern replacement for the deprecated Context Pack testing section the primary flow references. |

Reading these as they are: verbatim corpus copies, `@GenDD-Flow/...` and `@TargetRepo/.cursor/...` links (the latter deprecated) don't resolve here.

## 3. Run the process

1. **Discover** — navigate the application, screenshot pages, inventory interactive elements (buttons, form inputs, links), prioritizing `data-testid` attributes as selectors. Map header/nav/main/sidebar/footer structure.
2. **Multi-page crawl** — visit each key page plus the authentication flow, extracting all `data-testid` attributes and the navigation map.
3. **Selector inventory** — organize by page: primary (`data-testid`), fallback (when missing), and a list of elements that *should* have a `data-testid` but don't.
4. **Page Objects** — one TypeScript class per logical page, `data-testid` selectors only, helper methods for common actions.
5. **E2E test suite** — happy path, validation (invalid/boundary inputs), error handling (mocked API/network failures), accessibility (keyboard nav, focus, ARIA), responsive (mobile/tablet/desktop breakpoints), sensitive-field masking, usability. Assertions via `expect`/`waitForSelector`, never `waitForTimeout`; each test independent via `beforeEach`.
6. **Test data fixtures** — structured JSON covering the scenarios generated above.

## 4. Never invent

A selector, page structure, or Page Object method not actually observed during discovery is a guess that will fail on first run. Every selector in the generated tests must trace back to something the discovery step actually found — if an element the user expects isn't there, say so as a finding, don't fabricate a plausible one.

## 5. Hard limits

- **Playwright MCP is required and expected** for this skill — the one exception to the plugin's usual no-MCP-tools default.
- Writes only under `e2e/` (`pages/`, `tests/`, `fixtures/`) in the target repository.
- No other MCP tools.
- No changes to application source code.
- Does not run the generated tests as part of this skill — generation only.
