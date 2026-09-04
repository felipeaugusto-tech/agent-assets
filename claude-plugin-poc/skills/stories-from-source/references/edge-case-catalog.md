# Edge Case Catalog

Prompts per category, for the Step 6 edge-case sweep. Walk the categories; take
only what genuinely applies to the story in hand.

**Four to six real edge cases beat twelve generic ones.** An edge case earns its
place when a reasonable engineer could implement the story two different ways
and only one of them handles it. If the answer is obvious from the happy-path
AC, it is padding.

## Contents

- [Empty and null](#empty-and-null)
- [Boundary values](#boundary-values)
- [Permissions and roles](#permissions-and-roles)
- [Concurrency](#concurrency)
- [Integration failure](#integration-failure)
- [Duplicate and repeat actions](#duplicate-and-repeat-actions)
- [State already changed](#state-already-changed)
- [Multi-tenancy](#multi-tenancy)
- [Time and timezone](#time-and-timezone)
- [Volume and scale](#volume-and-scale)
- [Input format and encoding](#input-format-and-encoding)
- [Session and interruption](#session-and-interruption)

---

## Empty and null

- First-run state — the user has zero of the thing. What does the screen say?
- A required field submitted blank, or containing only whitespace.
- An optional field omitted entirely versus sent as an empty string.
- A collection that becomes empty after the last item is removed.
- A search or filter that matches nothing.

## Boundary values

- One below, exactly at, and one above every stated limit.
- Zero, negative, and the maximum representable value for a numeric field.
- Minimum and maximum field lengths, and one character past each.
- A date at the start and end of a range, and the range boundaries themselves.
- Currency at the smallest unit, and at a value with more decimal places than
  the currency supports.

## Permissions and roles

- Each role the system defines attempting the action.
- A signed-out user hitting an authenticated path directly.
- A user whose permission was revoked mid-session.
- A user acting on a resource they do not own.
- Distinguish *not permitted* from *does not exist* — the choice between 403 and
  404 leaks information and should be a stated decision, not an accident.

## Concurrency

- Two users editing the same record simultaneously — last write wins, or
  conflict surfaced?
- The same user acting from two tabs or two devices.
- A double-click or double-submit on a costly action.
- A background job touching a record while a user edits it.
- An action taken against a record deleted a moment earlier.

## Integration failure

For every external call the story makes:

- Timeout — how long, and what does the user see?
- Service unavailable (5xx).
- Service returns an unexpected shape or an error code not in the contract.
- Partial success — the call succeeded but a follow-up did not.
- Retry policy: how many, what backoff, and is the operation idempotent?

**State whether the flow degrades gracefully or fails hard.** Leaving this open
is one of the most common causes of rework, and it costs nothing to settle here.

## Duplicate and repeat actions

- The same request submitted twice — is it idempotent?
- Creating a record identical to one that exists.
- Re-running an import or upload with overlapping data.
- Clicking a one-time action link a second time.

## State already changed

- The action was already performed by someone else.
- The target moved to a state where the action no longer applies (already
  cancelled, already approved, already shipped).
- A precondition was true when the page loaded and false at submit.

## Multi-tenancy

Where the system is multi-tenant, treat isolation as required, not optional:

- A user requesting a resource ID belonging to another tenant.
- Search, list, and export scoped correctly to the tenant.
- Tenant-level configuration differing between tenants for the same behavior.
- A user who belongs to more than one tenant.

## Time and timezone

- An action spanning midnight, month end, or year end.
- Daylight-saving transitions in both directions.
- A user in a different timezone from the server or from another user.
- An expiry or deadline hit exactly at the boundary second.
- A clock skew between systems that both stamp the same record.

## Volume and scale

- A list long enough to require pagination, and the last page.
- The largest realistic input — file size, row count, batch length.
- Bulk operations where some rows succeed and others fail: is it all-or-nothing
  or partial, and what does the user get back?

## Input format and encoding

- Unicode, emoji, and right-to-left text in free-text fields.
- Leading and trailing whitespace.
- Characters with meaning in the storage or display layer, handled safely.
- A file with the right extension but the wrong content.
- Very long single-token input with no spaces.

## Session and interruption

- Session expires mid-flow.
- The browser is closed and the flow is resumed later.
- The back button is pressed after a submit.
- Network drops between request and response — did it commit?
- The page is refreshed on a confirmation screen.
