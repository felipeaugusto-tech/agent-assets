# Interview Question Bank

Ask in compact batches, not one at a time. Mine any context the user already
gave you first, and only ask about real gaps. The goal is to leave the PRD with
no silent guesses — anything you still don't know becomes an Open Decision.

## Universal core (every variant)

1. **The one-liner.** "In one or two sentences, what is this and what does it do?"
   If they struggle, offer a draft and let them correct it.
2. **Users.** "Who uses it? List the distinct user types, and tell me which one
   is primary." Push for real personas, not "users."
3. **Problem / why now.** "What problem does this solve, and what happens if we
   don't build it?"
4. **Success.** "How will we know it worked? Give me the one or two numbers that
   would make you call this a win." Push for measurable targets.
5. **Non-goals.** "What are we explicitly NOT doing in this version?" The most
   valuable question — insist on at least two or three.
6. **Constraints.** "What's fixed? Deadline, budget, existing stack, team size,
   compliance, dependencies you can't change."
7. **Status & ownership.** "Who owns this, and what stage is it at — early idea,
   for-review, or approved-for-build?"

## Technical PRD — additional

8. **Architecture shape.** "Roughly how does it hang together — frontend,
   backend, database, third-party services? Any diagram or existing system it
   plugs into?"
9. **Data.** "What are the main entities/records the system stores, and how do
   they relate? Any sensitive/PII data?"
10. **Interfaces.** "What APIs, endpoints, or integration points does it expose
    or consume?"
11. **Non-functional targets.** "Any hard numbers for performance, scale,
    availability, or latency? Security/compliance requirements (SOC 2, HIPAA,
    GDPR)?"
12. **Build phasing.** "Is this one shot, or phased? If phased, what's the rough
    order and what's the exit criterion for each phase?"
13. **Risks.** "What worries you most about building this? What's most likely to
    go wrong?"

## Business / feature PRD — additional

8. **User journey.** "Walk me through what the user does, step by step, start to
   finish."
9. **Current state.** "How do people accomplish this today, if at all? What's
   painful about it?"
10. **Value & prioritization.** "What's the must-have vs. nice-to-have? If you
    could only ship one part, which?"
11. **Metrics & instrumentation.** "Which product metrics move if this works —
    activation, retention, conversion, support tickets?"
12. **GTM / rollout.** "How does this reach users — full launch, beta, phased
    rollout, feature flag? Any dependencies on marketing/sales/support?"
13. **Design.** "Are there mockups, a design system, or brand constraints to
    follow?"

## PoC / spike PRD — additional

8. **The hypothesis.** "What exactly are you trying to prove or de-risk? What
   would a successful PoC let you decide?"
9. **The full vision.** "Is there a larger production build this is a subset of?
   If so, what does the PoC deliberately leave out?" — this drives the critical
   "what's stripped" section.
10. **What's stripped, and why it's safe.** "For each thing you're cutting
    (multi-tenancy, CI/CD, enterprise security, scale), is removing it a simple
    add-back later, or a rearchitecture?" Capture this — it's what makes a PoC
    credible.
11. **Fixture / validation data.** "What will you test it against — real data,
    synthetic fixture, a single golden path?"
12. **Time box.** "How long do you have, and what's the single demo/outcome that
    proves it?"
13. **Path to production.** "After the PoC succeeds, what's the rough plan to
    harden it?"

## Reading the room

- A user who talks in stacks, schemas, and latency wants a **technical PRD**.
- A user who talks in user journeys, funnels, and stakeholders wants a
  **business PRD**.
- A user who says "prototype," "validate," "time-boxed," or "cut scope" wants a
  **PoC PRD**.

When context is thin and the user wants to move, ask the universal core (1–7)
only, write the draft, and route every unknown to Open Decisions.
