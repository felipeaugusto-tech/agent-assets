---
name: generate-support-documentation
description: Generate troubleshooting guides, an FAQ, and a known-issues document for a support team, grounded in existing system documentation. Manual invocation only.
disable-model-invocation: true
---

# Generate Support Documentation

For a support team onboarding onto a product, or after a release that changes behavior, or when recurring tickets reveal missing documentation.

## 1. Fix the target and check prerequisites

The target is **the user's current repository**, never this plugin or the GenDD corpus.

This skill works best with existing system documentation. Check for `docs/brownfield/gendd/` (start with `overview/system-summary.md`); if it doesn't exist, proceed with whatever documentation does exist, or suggest `/gendd:run-brownfield-analysis` first for a stronger foundation.

## 2. Load the reference (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-support-documentation/generate-support-documentation.md` | **Primary task flow.** |
| `${CLAUDE_PLUGIN_ROOT}/references/generate-support-documentation/support-engineer.md` | **The actual analysis method** the primary flow delegates to. |

Reading these as they are: verbatim corpus copies, `@GenDD-Flow/...`/`@TargetRepo` links don't resolve here.

## 3. Run the process

1. **Gather context** — identify user-facing components, entry points, error handling patterns, and user-facing flows from existing system documentation.
2. **Apply the Support Engineer analysis method** from `support-engineer.md` to produce:
   - Troubleshooting guide (common error scenarios with resolution steps)
   - FAQ (based on actual system behavior and edge cases)
   - Known issues and workarounds
   - Error code / message reference
   - Escalation path recommendations
3. **Save outputs** to `docs/support/` (`troubleshooting-guide.md`, `faq.md`, `known-issues.md`).

## 4. Never invent

A troubleshooting step or FAQ answer not grounded in actual observed error handling or documented behavior is a guess a support engineer will pass on to a confused customer. Where the system's behavior for a scenario isn't clear from the code or docs, flag it as needing SME input rather than inventing a plausible-sounding resolution.

## 5. Hard limits

- Writes only under `docs/support/` in the target repository.
- No code or configuration changes.
- No MCP tools.
- No tests, builds, deploys, or benchmarks.
