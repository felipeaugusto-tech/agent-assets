---
description: Run the plugin token benchmark and report the results. Spends real money.
disable-model-invocation: true
allowed-tools: Bash(./scripts/benchmark-plugin.sh *)
---

# Run the plugin token benchmark

A thin wrapper around `scripts/benchmark-plugin.sh`. The script is the engine; do not reimplement any
part of it, and do not run the `claude -p` loop yourself.

## What to do

Run the script from the repository root, passing the user's arguments through unchanged:

```bash
./scripts/benchmark-plugin.sh <the user's arguments>
```

Add no flags the user did not ask for. `./scripts/benchmark-plugin.sh --help` lists every option.

## Confirming the spend

The script guards against unintended spending by asking for confirmation, but it cannot prompt
through the Bash tool — with no terminal it exits 1 and tells you to pass `--yes`.

So:

- If the user has already made their intent explicit — they asked to run the benchmark, or passed
  `--yes` themselves — confirm the estimated cost with them in one short question, then run with
  `--yes` added.
- If they seem to be exploring rather than committing, run `--dry-run` first. It prints the full plan,
  including the cost estimate and the plugin composition, and spends nothing.
- Never add `--yes` silently. A default run is 13 `claude` invocations and roughly $0.90 at list
  price.

## Reporting

Report the script's printed summary table **verbatim**, along with the paths of the two CSVs it wrote.
Do not recompute, round, or reinterpret the numbers — the script is the source of truth.

If the run fails, show the script's own error output rather than paraphrasing it.

## Do not

- Do not edit `claude-plugin-poc/3-token-benchmarks.md`. Updating that document from new numbers is a
  deliberate human act; offer the summary table for the user to paste instead.
- Do not commit the generated CSVs unless the user asks.
- Do not change the plugin's enabled state yourself. The script disables and re-enables it, and
  restores the original state on exit including on interrupt.
