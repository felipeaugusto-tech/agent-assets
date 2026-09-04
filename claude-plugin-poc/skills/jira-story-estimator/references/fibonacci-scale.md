# Fibonacci Point Scale

Points measure **complexity and uncertainty**, not hours. Calibrate against the codebase via ADR/PRD/Context Packs. Map the sub-task mix (known / familiar / novel / exploratory) to a value:

| Points | Meaning | Sub-task profile | Typical signs |
|---|---|---|---|
| **0.5** | Trivial chore, zero uncertainty | 1 known task | Config change, label edit, flag flip. No discovery possible. |
| **1** | Tiny, fully understood | All known | One small change in a familiar area; AC obvious. |
| **2** | Small, clear path | Mostly known, maybe 1 familiar | Established pattern, minor judgment calls. |
| **3** | Moderate, well-understood | Known + familiar mix | Several steps, all on known patterns; light integration. |
| **5** | Substantial or one new area | Familiar + 1 novel | New pattern to establish, or touches multiple layers; some discovery. |
| **8** | Large or genuinely uncertain | Multiple novel, or 1 exploratory | Significant new ground, cross-cutting changes, real unknowns. |
| **13** | Too large to estimate reliably | Multiple novel/exploratory | **Stop and split.** Signals a poorly-scoped story, not a sprint commitment. |

## Rules

- **0.5** only when there is genuinely no chance of discovering complexity. Any risk of surprise → at least **1**.
- **13** is a conversation, not a size. Reaching 13 means propose a breakdown into smaller stories.
- **Uncertainty counts as complexity.** An unfamiliar integration is complex precisely because it's unknown — don't estimate that away.
- **Anchor to the codebase.** The same feature is a 2 in a clean, documented repo and a 5–8 in untested legacy.
- **The decomposition drives the number.** Points follow from the sub-task mix, not the reverse. If two values feel plausible, the complexity category of the hardest sub-task usually decides.

## Quick adjacency check

When justifying a value, state why not the value below (what would make it simpler) and why not the value above (what would make it harder). If you can't cleanly argue both edges, the story may need more clarification before estimating.
