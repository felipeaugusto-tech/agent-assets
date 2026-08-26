#!/usr/bin/env bash
# lint-standards.sh — Validates that every standard file in this repository
# conforms to the section-based severity model defined in governance/rule-authoring.md.
#
# Exit code 0 = all checks pass.
# Exit code 1 = one or more violations found.
#
# Usage:
#   ./scripts/lint-standards.sh [--fix-dates] [path ...]
#
# If paths are supplied, only those files are checked. Otherwise all *.md files
# under sdlc/ and governance/ are checked (READMEs are skipped).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FIX_DATES=false
TARGETS=()
ERRORS=()

# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------
for arg in "$@"; do
  case "$arg" in
    --fix-dates) FIX_DATES=true ;;
    *) TARGETS+=("$arg") ;;
  esac
done

if [[ ${#TARGETS[@]} -eq 0 ]]; then
  mapfile -t TARGETS < <(
    find "$REPO_ROOT/sdlc" "$REPO_ROOT/governance" \
      -name "*.md" ! -name "README.md" | sort
  )
fi

# ---------------------------------------------------------------------------
# Helper: record an error
# ---------------------------------------------------------------------------
err() {
  local file="$1"
  local msg="$2"
  ERRORS+=("  ${file#"$REPO_ROOT/"}: $msg")
}

# ---------------------------------------------------------------------------
# Required frontmatter fields
# ---------------------------------------------------------------------------
REQUIRED_FIELDS=(id title phase summary tags applies_to version last_reviewed)

check_frontmatter() {
  local file="$1"
  # Extract frontmatter (between first two --- lines)
  local fm
  fm=$(awk '/^---/{c++; if(c==2) exit} c==1' "$file")

  for field in "${REQUIRED_FIELDS[@]}"; do
    if ! echo "$fm" | grep -qE "^${field}:"; then
      err "$file" "Missing required frontmatter field: $field"
    fi
  done

  # Verify 'severity' field is NOT present
  if echo "$fm" | grep -qE "^severity:"; then
    err "$file" "Prohibited frontmatter field present: severity (use section-based severity instead)"
  fi
}

# ---------------------------------------------------------------------------
# Prohibited section headings — match only exact ## headings at line start
# ---------------------------------------------------------------------------
PROHIBITED_SECTIONS=(
  "Quick Reference"
  "Agent Directives"
  "Definition of Done"
  "Checklist"
  "Exceptions"
)

check_prohibited_sections() {
  local file="$1"
  for section in "${PROHIBITED_SECTIONS[@]}"; do
    # Match the exact heading line: starts with "## <section>" with nothing else
    # (allows optional trailing whitespace). This avoids matching prose references.
    if grep -qE "^## ${section}[[:space:]]*$" "$file"; then
      err "$file" "Prohibited section present: ## $section"
    fi
  done
}

# ---------------------------------------------------------------------------
# Severity keyword check — RFC 2119 words must not appear inside directive text
# (i.e. in bullet list items under a ## MUST / ## SHOULD / ## MAY section).
# We detect lines that start with '- ' and contain a bare MUST/SHOULD/MAY
# keyword NOT inside a **bold rule ID** or a code span.
# ---------------------------------------------------------------------------
check_inline_severity_keywords() {
  local file="$1"
  local in_section=false
  local in_code_block=false
  local lineno=0

  while IFS= read -r line; do
    lineno=$((lineno + 1))

    # Toggle code fence tracking — skip everything inside fenced code blocks
    if [[ "$line" =~ ^[[:space:]]*\`\`\` ]]; then
      if $in_code_block; then
        in_code_block=false
      else
        in_code_block=true
      fi
      continue
    fi
    $in_code_block && continue

    # Detect entry into a severity section
    if [[ "$line" =~ ^##[[:space:]]+(MUST|MUST\ NOT|SHOULD|SHOULD\ NOT|MAY)[[:space:]]*$ ]]; then
      in_section=true
      continue
    fi

    # Detect exit from severity section (any other ## heading)
    if [[ "$line" =~ ^##[[:space:]] ]]; then
      in_section=false
      continue
    fi

    if $in_section && [[ "$line" =~ ^-[[:space:]] ]]; then
      # Strip bold rule IDs like **SEC-001-01** to avoid false positives
      local stripped_line
      stripped_line=$(echo "$line" | sed 's/\*\*[A-Z][A-Z0-9-]*\*\*//g')
      # Remove common noun uses: "a MUST rule", "SHOULD rule", "MUST NOT rule", etc.
      stripped_line=$(echo "$stripped_line" | sed -E 's/\b(MUST NOT|MUST|SHOULD NOT|SHOULD|MAY) rules?\b//g')
      # Check for bare RFC 2119 keywords (word boundaries) — obligation use only
      if echo "$stripped_line" | grep -qE '\b(MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\b'; then
        err "$file" "Line $lineno: Directive text contains inline RFC 2119 keyword. Move severity to section heading only."
      fi
    fi
  done < "$file"
}

# ---------------------------------------------------------------------------
# At least one severity section must exist for non-governance files
# ---------------------------------------------------------------------------
check_has_severity_section() {
  local file="$1"
  # Governance files (charter, glossary, HITL, guardrails) are narrative and
  # use their own structure. Skip them.
  if [[ "$file" == *"/governance/"* ]]; then
    return
  fi

  if ! grep -qE "^## (MUST|MUST NOT|SHOULD|SHOULD NOT|MAY)" "$file"; then
    err "$file" "No severity section (## MUST, ## SHOULD, etc.) found. Standard files must contain at least one severity section."
  fi
}

# ---------------------------------------------------------------------------
# Version field must be semver (x.y.z)
# ---------------------------------------------------------------------------
check_version_format() {
  local file="$1"
  local fm
  fm=$(awk '/^---/{c++; if(c==2) exit} c==1' "$file")
  local version
  version=$(echo "$fm" | grep -E "^version:" | head -1 | sed 's/version:[[:space:]]*//' | tr -d '"'"'" )
  if [[ -n "$version" ]] && ! [[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    err "$file" "version field '$version' is not valid semver (expected x.y.z)"
  fi
}

# ---------------------------------------------------------------------------
# last_reviewed date must not be older than 365 days from today
# ---------------------------------------------------------------------------
TODAY=$(date +%s)
check_review_date() {
  local file="$1"
  local fm
  fm=$(awk '/^---/{c++; if(c==2) exit} c==1' "$file")
  local date_str
  date_str=$(echo "$fm" | grep -E "^last_reviewed:" | head -1 | sed 's/last_reviewed:[[:space:]]*//' | tr -d '"'"'" )
  if [[ -z "$date_str" ]]; then
    return
  fi

  local epoch
  epoch=$(date -d "$date_str" +%s 2>/dev/null || echo "")
  if [[ -z "$epoch" ]]; then
    err "$file" "last_reviewed '$date_str' cannot be parsed as a date"
    return
  fi

  local diff_days=$(( (TODAY - epoch) / 86400 ))
  if [[ $diff_days -gt 365 ]]; then
    err "$file" "last_reviewed '$date_str' is more than 365 days ago ($diff_days days). Schedule a review."
  fi
}

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
checked=0
for file in "${TARGETS[@]}"; do
  # Skip non-markdown files
  [[ "$file" != *.md ]] && continue
  # Skip READMEs
  [[ "$(basename "$file")" == "README.md" ]] && continue
  # Skip AGENTS.md and top-level README.md (not standards files)
  local_path="${file#"$REPO_ROOT/"}"
  if [[ "$local_path" == "AGENTS.md" || "$local_path" == "README.md" || "$local_path" == "CHANGELOG.md" ]]; then
    continue
  fi

  checked=$((checked + 1))
  check_frontmatter "$file"
  check_prohibited_sections "$file"
  check_inline_severity_keywords "$file"
  check_has_severity_section "$file"
  check_version_format "$file"
  check_review_date "$file"
done

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
echo ""
echo "lint-standards: checked $checked files"

if [[ ${#ERRORS[@]} -eq 0 ]]; then
  echo "lint-standards: PASS — no violations found"
  exit 0
else
  echo "lint-standards: FAIL — ${#ERRORS[@]} violation(s) found:"
  for e in "${ERRORS[@]}"; do
    echo "$e"
  done
  exit 1
fi
