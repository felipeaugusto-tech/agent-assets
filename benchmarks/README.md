# Benchmark Results

**Dated snapshots of the token and cost impact of the `gendd` Claude Code plugin, produced by `scripts/benchmark-plugin.sh`.**

| Field | Value |
|-------|-------|
| **Produced by** | [`../scripts/benchmark-plugin.sh`](../scripts/benchmark-plugin.sh) |
| **Interpretation** | [`../claude-plugin-poc/3-token-benchmarks.md`](../claude-plugin-poc/3-token-benchmarks.md) |
| **Format** | CSV, one dated pair per run |

---

## Regenerate

```bash
./scripts/benchmark-plugin.sh              # full run: 5 + 5 + 3 calls, ~$0.90 at list price
./scripts/benchmark-plugin.sh --dry-run    # print the plan, spend nothing
./scripts/benchmark-plugin.sh --help       # all options
```

Inside a Claude Code session in this repository, `/benchmark` wraps the same script — for example
`/benchmark --dry-run`. It is a project-level command, deliberately **not** a skill inside the `gendd`
plugin: adding one there would raise the plugin's inventory to two skills and the benchmark would
measure its own weight.

Each run writes a new dated pair; nothing is overwritten, so cost can be tracked as the plugin evolves.

The script asks for confirmation before spending. With no terminal available it exits 1 and tells you
to pass `--yes` rather than silently doing nothing.

---

## Files

| Pattern | Contents |
|---|---|
| `<timestamp>-runs.csv` | One row per individual run |
| `<timestamp>-summary.csv` | One row per arm, with median, min and max |

### The three arms

| Arm | Setup | Answers |
|---|---|---|
| **A** | Plugin disabled | Baseline session cost |
| **B** | Plugin enabled, skill not invoked | Always-on cost of having it installed |
| **C** | Skill invoked | Full cost when actually used |

### Measurement columns

| Column | Meaning |
|---|---|
| `prompt_tokens` | `input_tokens + cache_creation_tokens + cache_read_tokens` — the headline metric |
| `input_tokens`, `cache_creation_tokens`, `cache_read_tokens` | The three components. Cache warmth moves tokens between the last two between runs, which is why only the sum is stable |
| `output_tokens` | Tokens generated. Varies with response length, especially in arm C |
| `turns` | Agentic turns. Arm C is multi-turn because the skill reads its reference files |
| `cost_usd` | The CLI's own `total_cost_usd`, at list price |
| `model` | Primary session model, selected by largest context window |

### Provenance columns — what was measured

These are the columns that make one run comparable with another. A token count is
uninterpretable without them: the same number means something different when the plugin
carried one skill than when it carried twelve.

| Column | Meaning |
|---|---|
| `skill_invoked` | The slash command run in arm C. Blank for the idle arms, which invoke nothing |
| `plugin`, `plugin_version` | Which plugin, at which version |
| `skills_count`, `skills_list` | How many skills the plugin held, and their names |
| `agents_count`, `hooks_count`, `mcp_count`, `lsp_count` | The rest of the component inventory |
| `projected_always_on_tokens` | Anthropic's own estimate from `claude plugin details`, for comparison against the measured figure |
| `work_dir` | Where `claude` was run from. Prompt size depends on it — see below |
| `repo_commit` | Short SHA of this repository at measurement time |
| `prompt` | The exact prompt sent (`runs.csv` only) |

`summary.csv` carries the same provenance columns except `prompt`, alongside the per-arm
median, min and max.

### Tracking cost as the plugin grows

The point of the provenance columns is longitudinal comparison. To see what adding a
component cost, compare `prompt_tokens_median` for **arm B** across two snapshots with
different `skills_count` or `agents_count` — that is the always-on cost of the change.
Compare **arm C** at matching `skill_invoked` values to see whether a skill's own
invocation cost has drifted.

Two conditions must hold for such a comparison to mean anything: identical `work_dir`, and
ideally the same `claude_version`, since a CLI upgrade can move the baseline on its own.

---

## Reading the numbers

**Compare only runs with the same working directory.** Prompt size depends on it — a project directory adds repository context that the home directory does not. The script pins it to `$HOME` by default and records the choice in its plan output. A run from the repository root measures ~294 tokens higher, which is real and not noise.

**`prompt_tokens` is deterministic; `cost_usd` is not.** Across runs, prompt tokens have shown a spread of exactly 0, while cost varies with output length and with how much of the prompt was served from cache. Treat cost as a relative measure and token counts as the primary result.

**Costs are list price.** On a Team or Enterprise plan your actual billing differs.

---

## Related Resources

| Resource | Path | Description |
|---|---|---|
| The harness | [`../scripts/benchmark-plugin.sh`](../scripts/benchmark-plugin.sh) | Runner, options, and safety behavior |
| Interpretation | [`../claude-plugin-poc/3-token-benchmarks.md`](../claude-plugin-poc/3-token-benchmarks.md) | What the numbers mean, and what this method cannot measure |
| Plugin overview | [`../claude-plugin-poc/1-plugin-overview.md`](../claude-plugin-poc/1-plugin-overview.md) | The design decision these numbers measure |

---

*This is tooling output, not a standard. It carries no standards frontmatter and is intentionally not registered in `rules-manifest.yaml` — a deliberate choice, not an omission.*
