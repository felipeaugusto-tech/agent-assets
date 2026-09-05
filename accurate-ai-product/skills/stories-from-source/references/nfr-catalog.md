# NFR Catalog

Trigger-to-NFR mapping for the Step 6 NFR sweep, with verification methods.

**NFRs are triggered by what a story touches, not applied uniformly.** A blanket
NFR table on every story trains reviewers to skip it. Three NFRs that genuinely
apply are worth more than nine boilerplate rows.

**Only carry an NFR the source or the Context Pack supports.** An invented
latency budget or a fabricated compliance regime is worse than a flagged gap,
because it reads as agreed and propagates into tickets and tests. Where a number
is needed and none exists, propose a defensible default, label it as an
assumption, and put it in Open Questions.

**Every NFR needs a verification method.** "Must be performant" is not a
requirement; it is a wish. If nobody can say how it would be checked, it is not
ready to ship in a story.

## Contents

- [Trigger table](#trigger-table)
- [Performance](#performance)
- [Security](#security)
- [Accessibility](#accessibility)
- [Compliance and data protection](#compliance-and-data-protection)
- [Reliability and resilience](#reliability-and-resilience)
- [Observability](#observability)
- [Usability and localization](#usability-and-localization)
- [Maintainability and operability](#maintainability-and-operability)

---

## Trigger table

| If the story touches | Consider |
|---|---|
| Personal, health, or payment data | Encryption in transit and at rest, retention, access control, applicable regime |
| Authentication, roles, or permissions | Session handling, privilege boundaries, audit logging, lockout policy |
| A user-facing screen | WCAG 2.1 AA, responsive behavior, browser support, error-state clarity |
| A list, search, or report | Pagination, response time at realistic volume, index strategy |
| An external service or third-party API | Timeout, retry, fallback, rate limits, contract-version handling |
| File upload or download | Size limits, type validation, malware scanning, storage location and residency |
| Bulk, batch, or scheduled work | Throughput, partial-failure behavior, idempotency, restart safety |
| Money movement | Idempotency, reconciliation, audit trail, rounding and currency rules |
| Notifications or messaging | Delivery guarantees, opt-out handling, rate limiting, template localization |
| Anything multi-tenant | Isolation, per-tenant configuration, noisy-neighbor limits |
| A public or partner-facing API | Versioning, deprecation policy, rate limiting, documented error contract |
| Anything user-visible in more than one market | Localization, date and number formats, timezone handling |

## Performance

Express as a percentile against a stated load, never as an adjective.

| Requirement shape | Verification |
|---|---|
| Endpoint responds within N ms at p95 under M concurrent users | Load test in a representative environment |
| A page is interactive within N seconds on a stated network profile | Front-end timing in CI or synthetic monitoring |
| A batch of N records completes within a stated window | Timed run against production-scale data |
| Degradation is graceful past a stated threshold | Soak or spike test |

Anchor the load figure to something real — current traffic, a Context Pack
baseline, a client SLA. If none exists, that is an Open Question.

## Security

| Requirement shape | Verification |
|---|---|
| Authorization is enforced server-side for every affected operation | Test with a token lacking the permission |
| A user cannot access another user's or tenant's resource by ID | Cross-account authorization test |
| Input is validated and output encoded on the affected paths | Automated scan plus targeted test |
| Secrets and tokens are never logged | Log inspection under a failure path |
| Sensitive fields are masked in UI, logs, and support tooling | Manual review plus log inspection |
| Rate limiting protects the affected endpoint from abuse | Burst test against the limit |

## Accessibility

Name the standard and the check. WCAG 2.1 AA is the usual baseline.

| Requirement shape | Verification |
|---|---|
| New interactive elements meet WCAG 2.1 AA | Automated scan (axe, Lighthouse) plus manual keyboard walkthrough |
| The flow is completable using keyboard alone | Keyboard-only run-through |
| Errors are announced to assistive technology, not conveyed by color alone | Screen-reader test |
| Focus order is logical and focus is visible | Manual review |
| Text and interactive elements meet contrast minimums | Contrast checker |

## Compliance and data protection

Only cite a regime the Context Pack or the source establishes. Naming the wrong
one is worse than naming none.

| Regime | Common story-level obligations |
|---|---|
| PCI DSS | Cardholder data never transits or persists in scope; tokenization; restricted access |
| HIPAA | PHI encrypted at rest and in transit; access logged; minimum necessary |
| GDPR / UK GDPR | Lawful basis; data subject access, export, and erasure; retention period; residency |
| SOC 2 | Change control, access review, audit trail on the affected operation |
| FedRAMP | Boundary controls, approved cryptography, logging and retention per baseline |
| CCPA / CPRA | Disclosure, deletion, and opt-out of sale or sharing |

Verification is usually a documented control plus evidence: configuration
review, log inspection, or a test proving the restricted path is blocked.

## Reliability and resilience

| Requirement shape | Verification |
|---|---|
| The operation is idempotent under retry | Replay the same request; assert a single effect |
| The flow degrades gracefully when a stated dependency is unavailable | Fault injection or dependency stub |
| No data loss on interruption mid-operation | Kill-and-resume test |
| Partial failures in a batch are reported, not silently swallowed | Batch run with seeded failures |
| Recovery meets a stated RTO or RPO | Failover exercise |

## Observability

Frequently omitted, and the reason incidents take hours instead of minutes.

| Requirement shape | Verification |
|---|---|
| Failures on the affected path emit a structured, alertable log event | Trigger the failure; confirm the event |
| A stated business metric is emitted for the new behavior | Dashboard or query check |
| Requests are traceable end to end via a correlation ID | Trace inspection across services |
| An alert fires when the failure rate exceeds a stated threshold | Alert rule test |

## Usability and localization

| Requirement shape | Verification |
|---|---|
| Error messages state what happened and what to do next | Copy review against failure states |
| All new user-facing strings are externalized for translation | Source inspection; pseudo-locale run |
| Dates, numbers, and currency respect the user's locale | Locale-switch test |
| Timezone-sensitive values display in the user's timezone with the zone shown | Multi-timezone test |
| The flow works on the browsers and viewports the project supports | Cross-browser and responsive check |

## Maintainability and operability

| Requirement shape | Verification |
|---|---|
| The behavior is toggleable behind a feature flag | Flag off and on; confirm both states |
| Configuration is environment-driven, not hard-coded | Configuration review |
| Migrations are reversible, or the forward-only decision is recorded | Rollback rehearsal |
| The change is deployable without downtime | Deployment rehearsal |
| Runbook or operational note exists for the new failure modes | Document review |
