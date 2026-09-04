# Spec: {COMPONENT_OR_INTERFACE_NAME}

> Status: {Draft / Reviewed / Final}
> Author: {NAME} | Date: {DATE}
> Implements: {link to ADR or requirement}
> Spike input: {link to spike doc, if any — omit section if none}

## Scope

{What this spec covers, and explicitly what it does not. One boundary, precisely stated.}

## Interface / Contract

{The API, function signature, schema, or event payload being defined. Precise enough to implement without a follow-up question. Use file references for existing patterns being followed.}

```
{signature, schema, or contract definition}
```

## Behavior

### Happy Path
{The expected, successful flow.}

### Edge Cases
| Case | Behavior |
|------|----------|
| {empty input / not found / unauthorized / concurrent modification / etc.} | {what happens} |

## Data Model

{Any new or changed data shapes. Reference existing models rather than repeating them where unchanged.}

## Settled by Spike

{If a spike resolved an unknown feeding this spec, state the conclusion here as fact and link the spike doc for the reasoning. Omit this section if no spike preceded this spec.}

## Open Questions

- {Anything genuinely undecided — do not guess an answer here.}

## Review

- [ ] Reviewed by: {name/role}
- [ ] Date: {date}
