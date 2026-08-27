# Token Benchmarks — What This Plugin Costs

**Installed and idle, the plugin costs zero measured tokens; invoked, it costs 45,450 prompt tokens and roughly 17× the money — which is exactly the behavior `disable-model-invocation: true` is meant to produce.**

| Field | Value |
|-------|-------|
| **Audience** | Anyone weighing whether to install or build an internal plugin |
| **Method** | Measured A/B, repeated runs — not estimates |
| **Date** | 2026-08-27 |
| **Related** | [1-plugin-overview.md](1-plugin-overview.md) · [2-distribution-guide.md](2-distribution-guide.md) |

## How to read the source markers

Unlike the companion documents, **every number on this page is measured on our own machines** — marked **[verified]** where it matters most. The one figure we did *not* measure is called out explicitly as Anthropic's projection in [What this method cannot measure](#what-this-method-cannot-measure). Nothing here is an estimate unless it says so.

---

## Table of Contents

- [Headline results](#headline-results)
- [Environment](#environment)
- [Method](#method)
- [Results](#results)
- [What this method cannot measure](#what-this-method-cannot-measure)
- [Interpretation](#interpretation)
- [Reproduce it yourself](#reproduce-it-yourself)
- [Related Resources](#related-resources)

---

## Headline results

| Scenario | Prompt tokens | Turns | Cost (USD) |
|---|---:|---:|---:|
| No plugin | 27,404 | 1 | $0.0148 |
| Plugin installed, skill **not** invoked | 27,404 | 1 | $0.0148 |
| Plugin installed, skill **invoked** | 72,854 | 4 | $0.2530 |

| Delta | Value |
|---|---|
| Cost of having the plugin installed | **0 tokens** |
| Cost of actually using it | **+45,450 prompt tokens** (2.66×) |
| Cost multiple when used | **~17×** ($0.0148 → $0.2530) |

The middle row is the point. A plugin you are not using should be free, and this one measurably is.

---

## Environment

| Item | Value |
|---|---|
| Claude Code | v2.1.247 |
| Model | `claude-opus-5` |
| OS | Windows 11 |
| Plugin | `gendd@hatchworks` v0.1.0, `Scope: managed` |
| Marketplace repo | public GitHub repository |
| Working directory | `$HOME` — see [Working directory changes the baseline](#working-directory-changes-the-baseline) |
| Date | 2026-08-27 |
| Raw results | [`../benchmarks/`](../benchmarks/) |

Cost figures come from the CLI's own `total_cost_usd`, reported on a list-price basis. On a Team or Enterprise plan your actual billing differs — treat costs as **relative** measures, and the token counts as the primary result.

---

## Method

Three arms, identical prompt (`Reply with exactly: OK`), five runs each for the idle arms and three for the invocation arm:

| Arm | Setup | Answers |
|---|---|---|
| **A** | Plugin disabled | Baseline session cost |
| **B** | Plugin enabled, skill not invoked | Always-on cost of having it installed |
| **C** | Skill invoked with a fixed requirement | Full cost when actually used |

Arm A was isolated with `claude plugin disable gendd@hatchworks`, which succeeds even on a managed-scope plugin by writing a local override. The plugin was re-enabled and the override removed afterwards.

### The metric

**Total prompt tokens** = `inputTokens + cacheCreationInputTokens + cacheReadInputTokens`, read from `modelUsage` in `--output-format json`.

Summing all three fields is essential. Cache warmth moves tokens between *creation* and *read* between runs, so either field alone swings wildly while the sum stays stable. Our runs bore this out: **zero variance across every arm** (range = 0 tokens).

### Two traps worth documenting

**Read the right model.** `modelUsage` can contain more than one model. Arms A and B included an auxiliary `claude-haiku-4-5` call of 897 tokens alongside the main `claude-opus-5` session. Taking the *first* entry rather than the main-session model produced 897 tokens for every arm and an apparent difference of zero — a measurement artifact that looked like a finding. The figures here use the primary session model; all-model totals were 28,301 for arms A and B, and 72,854 for arm C, which makes no Haiku call.

**Restrict the toolset and you measure a stub.** An early attempt passed `--allowed-tools "Read"` and produced an 897-token prompt, far below a real session. The published runs use the default toolset.

---

## Results

### Arms A and B — installed versus not

```text
--- Arm A: plugin disabled (n=5) ---
  prompt=27404  out=4  turns=1  $0.0148   (all 5 runs identical)
  spread: min=27404 max=27404 range=0

--- Arm B: plugin enabled, not invoked (n=5) ---
  prompt=27404  out=4  turns=1  $0.0148   (all 5 runs identical)
  spread: min=27404 max=27404 range=0
```

**Difference: 0 tokens.** Not "within noise" — identical, with zero variance across ten runs.

### Control — is the measurement sensitive at all?

A zero result is only meaningful if the method could have detected a non-zero one. We ran the **same plugin with only the flag removed** from `SKILL.md`, loaded via `--plugin-dir`:

| Variant | Prompt tokens |
|---|---:|
| `disable-model-invocation: true` (shipped) | 27,404 |
| Flag removed (model-invocable) | 27,404 |

Both identical. This control **failed to demonstrate sensitivity** — see the next section, which is the honest reading of it.

### Arm C — invoking the skill

```text
--- Arm C: /gendd:enhance-requirements <requirement> (n=3) ---
  run 1:  prompt=72854  out=13579  turns=4  $0.5635
  run 2:  prompt=72854  out= 7375  turns=4  $0.2208
  run 3:  prompt=72854  out= 8661  turns=4  $0.2530
  MEDIAN: prompt=72854  out= 8661  turns=4  $0.2530
  spread(prompt): range=0
```

Prompt tokens are all but deterministic; output varies 7,375–13,579 because the length of the generated specification varies with the requirement and the model's choices.

A later scripted run of the same three arms reproduced 27,404 / 27,404 / 72,854 exactly, with one arm C run landing on 72,853 — a spread of 1 token in 72,854, or 0.001%. Treat arm C's prompt size as stable rather than literally fixed; the idle arms have shown a spread of exactly 0 across every run to date.

---

## What this method cannot measure

**Headless sessions do not advertise skills to the model.** This is the most important caveat on the page, and it limits the "0 tokens" result.

Evidence: **[verified]**

- The control above — a *model-invocable* skill — added 0 tokens too. If skill descriptions were in the headless prompt, that arm would have grown.
- Asked directly in a `-p` run whether `/gendd:enhance-requirements` was available, the model answered `MISSING`, even with the plugin loaded and working. Invoking the command in the same configuration succeeded.

Together these say the slash command is resolved client-side and expanded into the user message, without the skill being listed in the model's context.

**What follows from that:**

| Claim | Status |
|---|---|
| In headless (`-p` / CI) runs, this plugin adds 0 tokens when idle | **Measured** |
| In interactive sessions, a manual-only skill adds ~59 tokens | **Not measured here.** This is Anthropic's own projection from `claude plugin details gendd` |
| Invoking the skill costs +45,450 prompt tokens | **Measured** |

Do not quote "zero always-on cost" for interactive use on the strength of these runs. To measure that, run `/context` in an interactive session with the plugin enabled and again with it disabled, and compare.

For reference, the projection we did not confirm:

```text
Projected token cost
  Always-on:   ~59 tok   added to every session
  component             always-on  on-invoke
  enhance-requirements        ~60      ~1.2k
```

---

## Interpretation

### Why idle is free, and invocation is not

The plugin bundles 1,188 lines / 41,552 bytes of methodology — `SKILL.md` plus three reference documents. None of it reaches the model until you type the command. That is `disable-model-invocation: true` doing its job; see [Who decides when a skill runs](1-plugin-overview.md#who-decides-when-a-skill-runs) for what the flag costs you in exchange.

### Read the 45,450 correctly

That figure is **cumulative across 4 turns**, not 45,450 tokens of new content. Each turn resends the accumulated context, so a 4-turn agentic loop that reads three reference files compounds. The underlying payload is ~41.5 KB of markdown; the rest is the conversation carrying it forward.

It is a **per-invocation** cost, not per-session. Two invocations in one session cost roughly twice.

### Is it worth it?

That is a judgment about the work, not the tokens. The comparison is not "$0.25 versus free" — it is $0.25 versus a person assembling the same structured specification by hand, or pasting 1,100 lines of methodology into a chat and getting a less consistent result. What the benchmark establishes is narrower and still useful: **you are not paying for it the rest of the time.**

### What this says about building plugins

| Guidance | Basis |
|---|---|
| Add only components you need | Every component is potential context cost |
| For human-initiated workflows, prefer manual-only invocation | Measured: 0 idle cost in headless |
| Keep heavy material in `references/`, not `SKILL.md` | `SKILL.md` loads on invocation; references load only if read |
| Measure rather than assume | Our first two measurement attempts were both wrong |

---

## Reproduce it yourself

The method is scripted. From the repository root:

```bash
./scripts/benchmark-plugin.sh              # full run: 5 + 5 + 3 calls, ~$0.90 at list price
./scripts/benchmark-plugin.sh --dry-run    # print the plan, spend nothing
./scripts/benchmark-plugin.sh --help       # all options
```

Inside a Claude Code session in this repository, `/benchmark` wraps the same script — `/benchmark --dry-run`, and so on. That command is project-level, deliberately not a skill inside `gendd`: a benchmark living in the plugin it measures would raise the inventory to two skills and inflate the very idle cost it reports.

It writes a dated pair of CSVs to `benchmarks/` and prints a ready-to-paste markdown table. It temporarily disables the plugin to isolate arm A, and restores your original plugin state and `settings.json` on exit — including on interrupt or failure.

The script encodes all four traps below, so you do not have to remember them.

### What the script does, and why each detail matters

```bash
# Arm A - disable the plugin, 5 runs
claude plugin disable gendd@hatchworks
for i in 1 2 3 4 5; do
  claude -p "Reply with exactly: OK" --output-format json < /dev/null > armA-$i.json
done

# Arm B - re-enable, 5 runs
claude plugin enable gendd@hatchworks
for i in 1 2 3 4 5; do
  claude -p "Reply with exactly: OK" --output-format json < /dev/null > armB-$i.json
done

# Arm C - invoke the skill, 3 runs
for i in 1 2 3; do
  claude -p "/gendd:enhance-requirements let users export their report as a PDF" \
    --output-format json < /dev/null > armC-$i.json
done
```

Extract the metric from each file:

```bash
python -c "
import json,sys
j=json.load(open(sys.argv[1],encoding='utf-8',errors='replace'))
mu=j['modelUsage']
k,m=max(mu.items(), key=lambda kv: kv[1].get('contextWindow',0))
print(k, m['inputTokens']+m['cacheCreationInputTokens']+m['cacheReadInputTokens'],
      m['outputTokens'], j['num_turns'], j['total_cost_usd'])
" armA-1.json
```

| Trap | Consequence if you get it wrong |
|---|---|
| Select the model by largest `contextWindow` | Taking the first entry picks up an auxiliary Haiku call, identical across arms, that masks any real difference |
| Redirect `< /dev/null` | A stdin warning is prepended to stdout and the JSON will not parse |
| Never pass `--allowed-tools` | You measure an 897-token stub instead of a real session |
| Keep the working directory fixed | Prompt size depends on it — see below |

### Working directory changes the baseline

Run from a project directory instead of `$HOME` and the baseline rises measurably — 27,698 rather than 27,404 tokens, since repository context enters the prompt. That is a real difference, not noise. The script pins the directory to `$HOME` by default and reports the choice; use `--cwd` to change it, and keep it constant across any runs you intend to compare.

Compare against the projection with `claude plugin details gendd`.

---

## Related Resources

| Resource | Path | Description |
|---|---|---|
| Plugin overview | [1-plugin-overview.md](1-plugin-overview.md) | What a plugin is; the invocation-control decision |
| Distribution guide | [2-distribution-guide.md](2-distribution-guide.md) | How the plugin reaches teams |
| Official: skills | https://code.claude.com/docs/en/skills | Skill frontmatter and invocation control |
| Official: plugins reference | https://code.claude.com/docs/en/plugins-reference | Debugging and development tools |
| Official: discover plugins | https://code.claude.com/docs/en/discover-plugins | Context cost shown in the plugin UI |

---

*This is tooling documentation, not a standard. It carries no standards frontmatter and is intentionally not registered in `rules-manifest.yaml` — a deliberate choice, not an omission.*
