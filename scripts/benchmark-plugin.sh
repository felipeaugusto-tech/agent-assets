#!/usr/bin/env bash
# benchmark-plugin.sh — Measures the token and cost impact of a Claude Code plugin
# by running three arms: plugin disabled, plugin enabled but idle, and skill invoked.
# Writes one CSV row per run plus a per-arm summary CSV.
#
# Exit code 0 = benchmark completed and CSVs written.
# Exit code 1 = a precondition failed, or one or more runs errored.
#
# Usage:
#   ./scripts/benchmark-plugin.sh [options]
#
#   --runs N            Runs per idle arm (default 5)
#   --invoke-runs N     Runs for the invocation arm (default 3)
#   --plugin ID         Plugin to benchmark (default gendd@hatchworks)
#   --skill CMD         Slash command for arm C (default /gendd:enhance-requirements)
#   --requirement TEXT  Requirement passed to the skill in arm C
#   --out DIR           Output directory (default <repo>/benchmarks)
#   --cwd DIR           Directory to run claude from (default $HOME). The prompt
#                       size depends on it: a project directory adds repo context,
#                       so keep it fixed for runs you intend to compare.
#   --keep-raw          Keep the raw per-run JSON alongside the CSVs
#   --dry-run           Print the plan and exit without spending anything
#   --yes               Skip the cost confirmation prompt
#   -h, --help          Show this usage text
#
# Requires: claude CLI, and python3 or python (used only to parse JSON — the repo
# has no jq dependency and bash cannot parse the CLI's JSON output unaided).
#
# WARNING: this script temporarily disables the plugin, which writes an override
# into ~/.claude/settings.json. The original settings file and plugin state are
# snapshotted and restored on exit, including on interrupt or failure.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

RUNS=5
INVOKE_RUNS=3
PLUGIN="gendd@hatchworks"
SKILL="/gendd:enhance-requirements"
REQUIREMENT="let users export their report as a PDF"
OUT_DIR="$REPO_ROOT/benchmarks"
KEEP_RAW=false
DRY_RUN=false
ASSUME_YES=false
IDLE_PROMPT="Reply with exactly: OK"
WORK_DIR="$HOME"

# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --runs)         RUNS="$2"; shift 2 ;;
    --invoke-runs)  INVOKE_RUNS="$2"; shift 2 ;;
    --plugin)       PLUGIN="$2"; shift 2 ;;
    --skill)        SKILL="$2"; shift 2 ;;
    --requirement)  REQUIREMENT="$2"; shift 2 ;;
    --out)          OUT_DIR="$2"; shift 2 ;;
    --cwd)          WORK_DIR="$2"; shift 2 ;;
    --keep-raw)     KEEP_RAW=true; shift ;;
    --dry-run)      DRY_RUN=true; shift ;;
    --yes)          ASSUME_YES=true; shift ;;
    -h|--help)      sed -n '2,31p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)              echo "benchmark-plugin: unknown option: $1" >&2; exit 1 ;;
  esac
done

# ---------------------------------------------------------------------------
# Preconditions
# ---------------------------------------------------------------------------
command -v claude >/dev/null 2>&1 || {
  echo "benchmark-plugin: claude CLI not found on PATH" >&2; exit 1; }

PY=""
for candidate in python3 python; do
  if command -v "$candidate" >/dev/null 2>&1; then PY="$candidate"; break; fi
done
[[ -n "$PY" ]] || {
  echo "benchmark-plugin: neither python3 nor python found; needed to parse JSON" >&2; exit 1; }

# Git Bash hands out MSYS paths (/tmp/..., /d/...) that a native Windows python
# cannot open. Translate anything passed to python; identity elsewhere.
topath() {
  if command -v cygpath >/dev/null 2>&1; then cygpath -w "$1"; else printf '%s' "$1"; fi
}

SETTINGS="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json"
CLAUDE_VERSION="$(claude --version 2>/dev/null | head -1)"
STAMP_FILE="$(date -u +%Y%m%d-%H%M%S)"
STAMP_ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Reads the enabled/disabled state of $PLUGIN from `claude plugin list`.
plugin_state() {
  claude plugin list 2>/dev/null | awk -v id="$PLUGIN" '
    index($0, id) { found = 1; next }
    found && /Status:/ { print (index($0, "enabled") ? "enabled" : "disabled"); exit }
  '
}

ORIGINAL_STATE="$(plugin_state)"
[[ -n "$ORIGINAL_STATE" ]] || {
  echo "benchmark-plugin: plugin '$PLUGIN' is not installed" >&2; exit 1; }

# ---------------------------------------------------------------------------
# Plugin composition snapshot
#
# Recorded on every row so results stay comparable as the plugin grows. An idle
# measurement is meaningless on its own: it matters whether the plugin held one
# skill or twelve, and whether it carried agents, hooks or MCP servers, at the
# moment the number was taken.
# ---------------------------------------------------------------------------
DETAILS="$(claude plugin details "${PLUGIN%%@*}" 2>/dev/null || true)"
count_of() { printf '%s\n' "$DETAILS" | sed -n "s/^  $1 (\([0-9]\{1,\}\)).*/\1/p" | head -1; }

PLUGIN_VERSION="$(printf '%s\n' "$DETAILS" | head -1 | awk '{print $2}')"
SKILLS_COUNT="$(count_of 'Skills')"
SKILLS_LIST="$(printf '%s\n' "$DETAILS" | sed -n 's/^  Skills ([0-9]\{1,\})  *//p' | head -1 \
               | sed 's/[[:space:]]\{1,\}/;/g; s/;$//')"
AGENTS_COUNT="$(count_of 'Agents')"
HOOKS_COUNT="$(count_of 'Hooks')"
MCP_COUNT="$(count_of 'MCP servers')"
LSP_COUNT="$(count_of 'LSP servers')"
PROJECTED_ALWAYS_ON="$(printf '%s\n' "$DETAILS" | sed -n 's/^  Always-on: *~\([0-9]\{1,\}\).*/\1/p' | head -1)"
REPO_COMMIT="$(git -C "$REPO_ROOT" rev-parse --short HEAD 2>/dev/null || true)"

# ---------------------------------------------------------------------------
# Plan and cost estimate
# ---------------------------------------------------------------------------
TOTAL_CALLS=$(( RUNS * 2 + INVOKE_RUNS ))
EST_COST="$("$PY" -c "print(f'{$RUNS*2*0.015 + $INVOKE_RUNS*0.25:.2f}')")"

cat <<PLAN
benchmark-plugin: plan
  plugin              $PLUGIN  (currently $ORIGINAL_STATE)
  claude              $CLAUDE_VERSION
  arm A (disabled)    $RUNS runs   prompt: "$IDLE_PROMPT"
  arm B (idle)        $RUNS runs   prompt: "$IDLE_PROMPT"
  arm C (invoked)     $INVOKE_RUNS runs   prompt: "$SKILL $REQUIREMENT"
  total calls         $TOTAL_CALLS
  estimated cost      ~\$$EST_COST at list price
  working directory   $WORK_DIR
  composition         v$PLUGIN_VERSION — skills $SKILLS_COUNT, agents $AGENTS_COUNT, hooks $HOOKS_COUNT, mcp $MCP_COUNT, lsp $LSP_COUNT
  skills              $SKILLS_LIST
  output              $OUT_DIR/$STAMP_FILE-{runs,summary}.csv
PLAN

if [[ "$DRY_RUN" == true ]]; then
  echo "benchmark-plugin: dry run — nothing executed"
  exit 0
fi

if [[ "$ASSUME_YES" != true ]]; then
  # Distinguish "declined" from "could not ask". Without a controlling terminal —
  # a CI job, or a call through another tool — a silent abort looks like a broken
  # script rather than a spending guard, so fail loudly and say what to do.
  # Test that /dev/tty can actually be OPENED, not merely that the node exists:
  # under Git Bash with stdin redirected the node is readable but the open fails.
  if { true < /dev/tty; } 2>/dev/null; then
    read -r -p "benchmark-plugin: this spends real money (~\$$EST_COST). Continue? [y/N] " reply < /dev/tty
    case "$reply" in [yY]*) ;; *) echo "benchmark-plugin: aborted by user"; exit 0 ;; esac
  else
    echo "benchmark-plugin: no terminal available to confirm the ~\$$EST_COST spend." >&2
    echo "benchmark-plugin: re-run with --yes to proceed, or --dry-run to see the plan." >&2
    exit 1
  fi
fi

# ---------------------------------------------------------------------------
# State snapshot and restore
# ---------------------------------------------------------------------------
RAW_DIR="$(mktemp -d)"
SETTINGS_BACKUP=""
if [[ -f "$SETTINGS" ]]; then
  SETTINGS_BACKUP="$RAW_DIR/settings.json.bak"
  cp "$SETTINGS" "$SETTINGS_BACKUP"
fi

restore() {
  local code=$?
  # Disarm first: on INT/TERM this handler calls exit, which would otherwise
  # re-enter it through the EXIT trap and restore twice.
  trap - EXIT INT TERM
  set +e
  if [[ -n "$SETTINGS_BACKUP" && -f "$SETTINGS_BACKUP" ]]; then
    cp "$SETTINGS_BACKUP" "$SETTINGS"
  fi
  # The settings file is the source of the override, but confirm the CLI agrees.
  local now; now="$(plugin_state)"
  if [[ "$now" != "$ORIGINAL_STATE" ]]; then
    if [[ "$ORIGINAL_STATE" == "enabled" ]]; then
      claude plugin enable "$PLUGIN" >/dev/null 2>&1
    else
      claude plugin disable "$PLUGIN" >/dev/null 2>&1
    fi
    if [[ -n "$SETTINGS_BACKUP" && -f "$SETTINGS_BACKUP" ]]; then
      cp "$SETTINGS_BACKUP" "$SETTINGS"
    fi
  fi
  echo "benchmark-plugin: restored plugin state to $ORIGINAL_STATE"
  if [[ "$KEEP_RAW" == true ]]; then
    mkdir -p "$OUT_DIR/$STAMP_FILE-raw"
    cp "$RAW_DIR"/*.json "$OUT_DIR/$STAMP_FILE-raw/" 2>/dev/null
    echo "benchmark-plugin: raw JSON kept in $OUT_DIR/$STAMP_FILE-raw"
  fi
  rm -rf "$RAW_DIR"
  exit "$code"
}
trap restore EXIT INT TERM

MANIFEST="$RAW_DIR/manifest.tsv"
: > "$MANIFEST"

# Constants that apply to every row, written once for the aggregator to attach.
META="$RAW_DIR/meta.tsv"
{
  printf 'plugin\t%s\n'                     "$PLUGIN"
  printf 'plugin_version\t%s\n'             "$PLUGIN_VERSION"
  printf 'skills_count\t%s\n'               "$SKILLS_COUNT"
  printf 'skills_list\t%s\n'                "$SKILLS_LIST"
  printf 'agents_count\t%s\n'               "$AGENTS_COUNT"
  printf 'hooks_count\t%s\n'                "$HOOKS_COUNT"
  printf 'mcp_count\t%s\n'                  "$MCP_COUNT"
  printf 'lsp_count\t%s\n'                  "$LSP_COUNT"
  printf 'projected_always_on_tokens\t%s\n' "$PROJECTED_ALWAYS_ON"
  printf 'work_dir\t%s\n'                   "$WORK_DIR"
  printf 'repo_commit\t%s\n'                "$REPO_COMMIT"
} > "$META"

# Runs one arm. Never pass --allowed-tools: restricting the toolset measures a
# stub prompt rather than a real session. Always redirect stdin from /dev/null,
# or a warning is prepended to stdout and corrupts the JSON.
run_arm() {
  local arm="$1" label="$2" state="$3" n="$4" prompt="$5" skill="${6:-}" i out
  for (( i = 1; i <= n; i++ )); do
    out="$RAW_DIR/run-$arm-$i.json"
    ( cd "$WORK_DIR" && claude -p "$prompt" --output-format json ) < /dev/null > "$out" 2>/dev/null || true
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$(topath "$out")" "$arm" "$label" "$state" "$i" "$skill" "$prompt" >> "$MANIFEST"
    echo "benchmark-plugin: arm $arm run $i/$n"
  done
}

# ---------------------------------------------------------------------------
# Arm A — plugin disabled
# ---------------------------------------------------------------------------
claude plugin disable "$PLUGIN" >/dev/null 2>&1
run_arm A "plugin disabled" disabled "$RUNS" "$IDLE_PROMPT"

# ---------------------------------------------------------------------------
# Arm B — plugin enabled, skill not invoked
# ---------------------------------------------------------------------------
claude plugin enable "$PLUGIN" >/dev/null 2>&1
run_arm B "plugin idle" enabled "$RUNS" "$IDLE_PROMPT"

# ---------------------------------------------------------------------------
# Arm C — skill invoked
# ---------------------------------------------------------------------------
run_arm C "skill invoked" enabled "$INVOKE_RUNS" "$SKILL $REQUIREMENT" "$SKILL"

# ---------------------------------------------------------------------------
# Aggregate to CSV
# ---------------------------------------------------------------------------
mkdir -p "$OUT_DIR"

"$PY" - "$(topath "$MANIFEST")" "$(topath "$OUT_DIR/$STAMP_FILE-runs.csv")" \
       "$(topath "$OUT_DIR/$STAMP_FILE-summary.csv")" \
       "$STAMP_ISO" "$CLAUDE_VERSION" "$(topath "$META")" <<'PYEOF'
import csv, json, statistics as st, sys

manifest, runs_csv, summary_csv, stamp, version, meta_path = sys.argv[1:7]

# Constants describing what was measured. Without these, a row's token count
# cannot be compared against a run taken at a different plugin composition.
meta = {}
with open(meta_path, encoding="utf-8") as fh:
    for line in fh:
        if line.strip():
            k, _, v = line.rstrip("\n").partition("\t")
            meta[k] = v

META_COLS = ["plugin","plugin_version","skill_invoked","skills_count","skills_list",
             "agents_count","hooks_count","mcp_count","lsp_count",
             "projected_always_on_tokens","work_dir","repo_commit","prompt"]

RUN_COLS = ["timestamp_utc","arm","arm_label","run","plugin_state","model","prompt_tokens",
            "input_tokens","cache_creation_tokens","cache_read_tokens","output_tokens",
            "turns","cost_usd","is_error","session_id","claude_version"] + META_COLS
SUM_COLS = ["timestamp_utc","arm","arm_label","n","prompt_tokens_median","prompt_tokens_min",
            "prompt_tokens_max","output_tokens_median","turns_median","cost_usd_median",
            "claude_version"] + [c for c in META_COLS if c != "prompt"]

rows, failures = [], 0
with open(manifest, encoding="utf-8") as fh:
    for line in fh:
        if not line.strip():
            continue
        path, arm, label, state, idx, skill, prompt = line.rstrip("\n").split("\t")
        try:
            # errors="replace": arm C output contains bytes that break a naive
            # read under the default Windows codepage.
            j = json.load(open(path, encoding="utf-8", errors="replace"))
        except Exception as exc:
            print(f"benchmark-plugin: unparseable {path}: {exc}", file=sys.stderr)
            failures += 1
            continue
        mu = j.get("modelUsage") or {}
        if not mu:
            print(f"benchmark-plugin: no modelUsage in {path}", file=sys.stderr)
            failures += 1
            continue
        # Select the PRIMARY session model by largest context window. Taking the
        # first entry picks up an auxiliary Haiku call that is identical across
        # arms and silently masks any real difference.
        name, m = max(mu.items(), key=lambda kv: kv[1].get("contextWindow", 0))
        inp = m.get("inputTokens", 0)
        cc  = m.get("cacheCreationInputTokens", 0)
        cr  = m.get("cacheReadInputTokens", 0)
        if j.get("is_error"):
            failures += 1
        row = {
            "timestamp_utc": stamp, "arm": arm, "arm_label": label, "run": idx,
            "plugin_state": state, "model": name, "prompt_tokens": inp + cc + cr,
            "input_tokens": inp, "cache_creation_tokens": cc, "cache_read_tokens": cr,
            "output_tokens": m.get("outputTokens", 0), "turns": j.get("num_turns", 0),
            "cost_usd": round(j.get("total_cost_usd", 0.0), 6),
            "is_error": j.get("is_error"), "session_id": j.get("session_id", ""),
            "claude_version": version,
        }
        row.update({k: meta.get(k, "") for k in META_COLS})
        # skill_invoked is per-arm, not global: blank for the idle arms.
        row["skill_invoked"] = skill
        row["prompt"] = prompt
        rows.append(row)

if not rows:
    print("benchmark-plugin: no usable runs", file=sys.stderr)
    sys.exit(1)

with open(runs_csv, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=RUN_COLS); w.writeheader(); w.writerows(rows)

summaries = []
for arm in sorted({r["arm"] for r in rows}):
    a = [r for r in rows if r["arm"] == arm]
    p = [r["prompt_tokens"] for r in a]
    s = {
        "timestamp_utc": stamp, "arm": arm, "arm_label": a[0]["arm_label"], "n": len(a),
        "prompt_tokens_median": round(st.median(p)), "prompt_tokens_min": min(p),
        "prompt_tokens_max": max(p),
        "output_tokens_median": round(st.median([r["output_tokens"] for r in a])),
        "turns_median": round(st.median([r["turns"] for r in a])),
        "cost_usd_median": round(st.median([r["cost_usd"] for r in a]), 4),
        "claude_version": version,
    }
    s.update({k: meta.get(k, "") for k in META_COLS if k != "prompt"})
    s["skill_invoked"] = a[0]["skill_invoked"]
    summaries.append(s)

with open(summary_csv, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=SUM_COLS); w.writeheader(); w.writerows(summaries)

print()
print("Copy-paste summary:")
print()
print("| Scenario | Prompt tokens | Spread | Turns | Cost (USD) |")
print("|---|---:|---:|---:|---:|")
for s in summaries:
    spread = s["prompt_tokens_max"] - s["prompt_tokens_min"]
    print(f"| {s['arm_label']} | {s['prompt_tokens_median']:,} | {spread} | "
          f"{s['turns_median']} | ${s['cost_usd_median']:.4f} |")
print()

by_arm = {s["arm"]: s for s in summaries}
if "A" in by_arm and "B" in by_arm:
    print(f"Idle cost of the plugin: "
          f"{by_arm['B']['prompt_tokens_median'] - by_arm['A']['prompt_tokens_median']} tokens")
if "A" in by_arm and "C" in by_arm:
    d = by_arm["C"]["prompt_tokens_median"] - by_arm["A"]["prompt_tokens_median"]
    ratio = by_arm["C"]["cost_usd_median"] / by_arm["A"]["cost_usd_median"] if by_arm["A"]["cost_usd_median"] else 0
    print(f"Invocation cost: +{d:,} prompt tokens, {ratio:.1f}x cost")
print()

sys.exit(2 if failures else 0)
PYEOF
PY_STATUS=$?

echo "benchmark-plugin: wrote $OUT_DIR/$STAMP_FILE-runs.csv"
echo "benchmark-plugin: wrote $OUT_DIR/$STAMP_FILE-summary.csv"

if [[ "$PY_STATUS" -ne 0 ]]; then
  echo "benchmark-plugin: FAIL — one or more runs errored or could not be parsed"
  exit 1
fi

echo "benchmark-plugin: PASS — $TOTAL_CALLS runs completed"
