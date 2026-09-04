# Workflow: Spike Doc

## Overview

A spike is a time-boxed investigation into something unknown enough that planning around a guess would be worse than spending an hour finding out — which library actually supports the needed feature, whether a proposed approach performs acceptably, whether an assumption in a spec actually holds. A spike doc records what was tried, what was found, and what it means for the work that depends on the answer. It is not the design itself; it feeds one.

**The failure mode this guards against:** an investigation that happens in someone's head (or a throwaway branch) and evaporates the moment the person moves on, leaving the next reader to redo the work or trust an unstated conclusion. Writing it down is what makes the finding reusable.

## When to Use

- Before committing to an approach in a spec or implementation plan, when the viability of that approach is genuinely uncertain — not when the answer is already known and the "spike" would just be busywork to produce a document.
- When choosing between libraries, frameworks, or architectural approaches where the trade-offs aren't clear from documentation alone.
- When validating a risky assumption before it becomes load-bearing in a plan (e.g. "can this API actually handle our expected volume").

**Time-box it.** State the time budget before starting, and stop at it — a spike that runs long without a decision point is no longer a spike, it's unplanned implementation work wearing a different name.

## Prerequisites

- A specific question the spike is meant to answer. "Investigate caching" is not a spike question; "can Redis Cluster handle our write pattern without cross-slot errors" is.

## Process

### Step 1: State the question precisely

Write the question the spike answers before starting the investigation. If the question can't be stated precisely, that's a sign the real work is narrowing the question, not running the spike yet.

### Step 2: State the time-box

How long this investigation gets before a decision is made with whatever's known at that point.

### Step 3: Do the investigation

Try the thing. Read the docs, run the prototype, benchmark the approach — whatever actually answers the question, not what's most interesting to explore.

### Step 4: Record what was tried, not just the conclusion

Enough detail that someone doubting the conclusion could see why it was reached, without having to redo the spike themselves: what was tested, against what, with what result.

### Step 5: State the recommendation

A spike that ends in "it's complicated, more research needed" without a recommendation has usually run out of time-box without producing its value. Even an inconclusive spike should recommend what to do given the uncertainty — proceed with caveats, pick a different approach, or spend a second time-boxed round on a narrower question.

### Step 6: Name what depends on this

Point at the spec or implementation plan this spike's answer feeds into, so the connection isn't lost.

## Never Invent

A finding not actually produced by the investigation is not a finding — if the time-box ran out before a clear answer emerged, say that plainly rather than writing a confident-sounding conclusion the investigation didn't actually support.

## Output Artifacts

Save to `docs/spikes/{topic-slug}.md` in the target repository, using `templates/spike-template.md`.

## Verification Checklist

- [ ] The question is specific enough to have a clear answer
- [ ] A time-box was stated before starting
- [ ] What was actually tried is recorded, not just the conclusion
- [ ] A recommendation is given, even if the answer is "proceed with caveats"
- [ ] The downstream spec or plan this feeds is named

## Related Resources

> **Feeds:** `workflows/spec-authoring.md` — a spike's conclusion becomes settled fact in the spec it informs.
> **Feeds:** `workflows/implementation-plan.md` — when the spike de-risks a specific task rather than the overall design.
> **Template:** `templates/spike-template.md`.
