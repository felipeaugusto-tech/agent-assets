# Pull Request: [Short title]

**Type:** Feature | Bug Fix | Refactor | Chore | Docs | Security | Performance
**Ticket / Issue:** [Link to the ticket or issue this PR closes]
**Breaking change:** Yes / No

---

## Summary

[2–4 sentences describing what this PR does and why. Focus on the "why" — the business or technical reason — not just the "what".]

---

## Changes Made

[A concise bullet list of the significant changes. Group by area if the PR touches multiple components.]

- [ ] [Change 1]
- [ ] [Change 2]
- [ ] [Change 3]

---

## How to Test

[Step-by-step instructions for a reviewer to verify the changes work correctly. Include any required environment setup, seed data, or feature flags.]

1. [Step 1]
2. [Step 2]
3. Expected result: [What the reviewer should observe]

---

## Checklist

The author MUST confirm all applicable items before requesting review.

### Code quality
- [ ] Code follows the standards in [`sdlc/development/coding-standards.md`](../sdlc/development/coding-standards.md).
- [ ] No commented-out code, debug statements, or TODO comments left in the diff (unless tracked in a ticket).
- [ ] Error handling follows [`sdlc/development/error-handling.md`](../sdlc/development/error-handling.md).

### Testing
- [ ] New functionality is covered by automated tests.
- [ ] All existing tests pass.
- [ ] No new flaky tests introduced.

### Security
- [ ] No secrets, credentials, or PII are present in the diff.
- [ ] Input validation and output encoding follow [`sdlc/security/input-validation-output-encoding.md`](../sdlc/security/input-validation-output-encoding.md).
- [ ] Dependencies added or upgraded have been reviewed for known vulnerabilities.

### Documentation
- [ ] Public-facing API changes are reflected in the API documentation.
- [ ] CHANGELOG updated (if this change is user-visible or changes behaviour).
- [ ] README or onboarding docs updated if setup steps changed.

### Database (if applicable)
- [ ] Migration is reversible and tested locally.
- [ ] No N+1 queries introduced.

---

## Screenshots / Recordings

[Attach screenshots, screen recordings, or links to a staging environment for UI changes. Remove this section if not applicable.]

---

_This PR follows the standard defined in [`sdlc/version-control/pull-requests.md`](../sdlc/version-control/pull-requests.md)._
