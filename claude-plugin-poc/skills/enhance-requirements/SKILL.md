---
name: enhance-requirements
description: Transform a vague requirement into a structured, testable specification with Given/When/Then acceptance criteria. Manual invocation only.
disable-model-invocation: true
---

# Enhance Requirements

Turn one vague requirement into a structured, testable specification. Chat output only.

## 1. Get the requirement

If the user invoked this skill without a requirement, ask for it in one short question and stop until they answer. Do not guess a requirement from the open file, the git diff, or the conversation.

## 2. Fix the target

The target is **the user's current project**. Never treat this plugin, its `references/` files, or this repository as the subject of analysis — they are methodology inputs only. Do not read, summarize, or modify plugin source as if it were the requirement.

## 3. Load the references (now, not before)

Read these three files only after invocation:

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/enhance-requirements/enhance-requirements.md` | **Primary task flow** — follow its Steps 1-6 as the order of work. |
| `${CLAUDE_PLUGIN_ROOT}/references/enhance-requirements/enhance-acceptance-criteria.md` | **Detailed methodology** — AC quality depth, NFR validation, Definition of Ready gate, worked example. |
| `${CLAUDE_PLUGIN_ROOT}/references/enhance-requirements/requirements-enhancement.md` | **Required output format** — AC rules, Example Output Structure, Quality Checklist. |

Reading these files as they are:

- They are verbatim copies of repository documents. Their internal links (`workflows/...`, `templates/...`, `@GenDD-Flow/...`, `@docs/...`) point at the original repo layout and **do not resolve here** — one is dead even upstream. Do not try to fetch them. These three files are the complete input.
- `{ORGANIZATION}` and `{PRODUCT_NAME}` are placeholders; substitute the user's context or leave generic.
- `#`/`##` lines inside fenced code blocks are output-template content, not instructions to you.
- They describe a Cursor Chat workflow. Adapt the intent, ignore the tool-specific mechanics.

## 4. Produce the specification

Follow the template's output structure. Include, in this order:

1. **Problem and goal** — what is broken or missing, and the outcome that counts as success.
2. **Actors / personas** — who acts, and the system actors involved.
3. **Assumptions and scope** — what is in, what is explicitly out.
4. **Functional requirements** — numbered, each one independently verifiable.
5. **Non-functional requirements** — only when the requirement genuinely implies them (performance, security, accessibility, availability, data retention). Omit the section rather than padding it.
6. **Ambiguities, risks, and open questions.**
7. **Acceptance criteria** — Given/When/Then, observable and testable, describing outcomes rather than implementations. Cover happy path, alternate paths, and error/edge cases.

## 5. Never invent business facts

Anything not stated by the user is an inference, and every inference belongs under **Assumptions**, labelled as such. Do not present a guessed rule, threshold, role, or integration as established fact.

Where a gap is material — it would change the acceptance criteria — ask about it. Batch those questions at the end under **Open Questions**, keep them concise, and still deliver the full specification under stated assumptions rather than withholding it.

## 6. Hard limits

- No code changes.
- No files created or modified in the user's project.
- No MCP tools.
- No tests, builds, or benchmarks.
- No subagents.

Return the result in chat.
