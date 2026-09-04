---
name: generate-unit-tests
description: Generate comprehensive unit tests for an existing code file (Java, Angular/TypeScript, or other), following AAA structure, naming conventions, and required scenario coverage. Manual invocation only.
disable-model-invocation: true
---

# Generate Unit Tests

For a specific code file that needs test coverage — not a gap analysis (`/gendd:review-test-coverage` does that), a generator that produces the tests once you know what needs them.

## 1. Fix the target

The target is **the user's current project's code file(s)**, never this plugin or the GenDD corpus. Identify the file to test and its language/stack before generating — the testing conventions differ by stack (see §2).

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-unit-tests/generate-unit-tests.md` | **Primary task flow** — the generic process, framework-agnostic. |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-unit-tests/testing-standards.md` | MUST/SHOULD/MAY requirement levels, coverage targets. |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-unit-tests/testing.md` | Foundational naming/AAA/mocking principles — modern replacement for the deprecated Context Pack testing section the primary flow references. |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-unit-tests/java-unit-test-generation.md` | Load if the target is Java — framework conventions (JUnit/Mockito) and worked patterns. |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-unit-tests/angular-unit-test-generation.md` | Load if the target is Angular/TypeScript — framework conventions and worked patterns. |

Load only the stack-specific file that matches the target; for another stack, apply the generic primary flow plus `testing-standards.md`/`testing.md` directly.

Reading these as they are: verbatim corpus copies, `@GenDD-Flow/...`/`@TargetRepo/.cursor/...` links (the latter deprecated) don't resolve here — use the bundled `testing.md` in place of the old Context Pack reference.

## 3. Run the process

1. **Read the target file** and understand its business logic and dependencies.
2. **Generate tests** covering, at minimum: happy path, edge cases (null/empty/boundary values), error conditions, and — when the code actually handles them — multi-tenant scenarios, integration-failure scenarios (mocked), and domain-specific scenarios (payment, notification, auth).
3. **Follow conventions**: `{Method}_{Scenario}_{ExpectedResult}` naming (or the stack's equivalent), Arrange-Act-Assert structure, mocking at boundaries (interfaces, external services) rather than internal classes, test isolation (no shared state between tests).
4. **Self-check** against the review checklist: naming convention followed, AAA used, dependencies properly mocked, tests isolated, all public methods covered, error scenarios present.

## 4. Never invent

A test for behavior the code doesn't actually have is worse than a missing test — it creates false confidence. Every scenario generated must trace to actual logic in the target file; don't add a "payment scenario" test to code that has nothing to do with payments just because the reference mentions it as an example domain.

## 5. Hard limits

- Writes only test files, alongside or co-located with the target per the project's existing convention.
- Does not modify the code under test.
- No MCP tools.
- Does not run the generated tests or check coverage itself — hand that back to the user (`dotnet test`, `mvn test`, `ng test`, etc., per stack) rather than assuming a runner exists.
- No builds, deploys, or benchmarks.
