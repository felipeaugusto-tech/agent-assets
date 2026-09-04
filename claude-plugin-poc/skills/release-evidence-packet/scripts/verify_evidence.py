#!/usr/bin/env python3
"""
verify_evidence.py — check that a release-evidence packet is internally trustworthy.

The packet covers one or more commits, and nothing beyond what those commits and the
requester's own input show. Three checks a reviewer will not reliably catch by eye:

  1. Provenance   — does every supplied artifact (e.g. an AC matrix) name commits
                     that are actually part of this packet?
  2. Freshness    — was it produced after the commits it claims to cover, and
                     recently enough?
  3. Completeness — is every required section present for every commit, or
                     explicitly N/A with a reason?

    python3 verify_evidence.py --manifest evidence.json

Exit 0 when integrity holds, 1 when it does not, 2 on bad input. A failure here does
not mean stop assembling the packet — it means the finding goes at the top of it.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SHA_RX = re.compile(r"^[0-9a-f]{7,40}$", re.I)


def parse_dt(value):
    if not value:
        return None
    v = str(value).strip().replace("Z", "+00:00")
    for fmt in (None, "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"):
        try:
            dt = datetime.fromisoformat(v) if fmt is None else datetime.strptime(v, fmt)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def same_commit(a, b):
    """Short and long SHAs of the same commit must compare equal."""
    if not a or not b:
        return None
    a, b = a.strip().lower(), b.strip().lower()
    if not (SHA_RX.match(a) and SHA_RX.match(b)):
        return a == b
    n = min(len(a), len(b))
    return a[:n] == b[:n]


def artifact_commits(art):
    """An artifact may name one commit ('commit') or several ('commits')."""
    if art.get("commits"):
        return [c for c in art["commits"] if c]
    if art.get("commit"):
        return [art["commit"]]
    return []


def check_provenance(m):
    findings = []
    commits = m.get("commits") or []
    if not commits:
        findings.append(("FAIL", "provenance",
                         "No commits pinned. Nothing can be checked against a packet "
                         "identity that does not exist."))
        return findings, []

    resolved = []
    for i, c in enumerate(commits):
        sha = (c.get("commit") or "").strip()
        if not sha:
            findings.append(("FAIL", "provenance",
                             f"commits[{i}]: no SHA recorded — an entry in the commit "
                             f"set with no identity can't be checked against anything."))
            continue
        if not SHA_RX.match(sha):
            findings.append(("WARN", "provenance",
                             f"Commit {sha!r} is not a git SHA — provenance comparison "
                             f"for it will be string equality only."))
        resolved.append(sha)

    # In a commit-only packet, "artifacts" holds whatever the requester supplied
    # directly (e.g. an acceptance-criteria matrix) — never CI-produced evidence.
    # Each one still has to name commits that are actually in this packet's set.
    for art in m.get("artifacts", []):
        name = art.get("name", "unnamed artifact")
        claimed = artifact_commits(art)
        if not claimed:
            findings.append(("FAIL", "provenance",
                             f"{name}: no commit(s) recorded — cannot be tied to this "
                             f"packet, so it is not evidence for it."))
            continue
        for claim in claimed:
            if not any(same_commit(claim, sha) for sha in resolved):
                findings.append(("FAIL", "provenance",
                                 f"{name}: describes commit {claim} — that is not one of "
                                 f"this packet's commits ({', '.join(resolved) or '—'}). "
                                 f"This is evidence for a different commit."))
    return findings, resolved


def check_freshness(m, max_age_days):
    findings = []
    now = datetime.now(timezone.utc)
    commit_dates = {}
    for c in m.get("commits") or []:
        sha = (c.get("commit") or "").strip()
        dt = parse_dt(c.get("committed_at"))
        if sha and dt:
            commit_dates[sha.lower()] = dt

    for art in m.get("artifacts", []):
        name = art.get("name", "unnamed artifact")
        produced = parse_dt(art.get("produced_at"))
        if not produced:
            findings.append(("WARN", "freshness",
                             f"{name}: no production timestamp — freshness unverifiable."))
            continue

        # Evidence has to postdate every commit it claims to cover — the latest one,
        # specifically, since that's the last point the evidence could be true as of.
        claimed = artifact_commits(art)
        relevant = [dt for sha in claimed
                    for known, dt in commit_dates.items() if same_commit(sha, known)]
        if relevant:
            latest = max(relevant)
            if produced < latest:
                findings.append(("FAIL", "freshness",
                                 f"{name}: produced {produced.date()}, before the most "
                                 f"recent commit it claims to cover ({latest.date()}). "
                                 f"It cannot describe code that did not exist yet."))

        age = (now - produced).days
        if age > max_age_days:
            findings.append(("WARN", "freshness",
                             f"{name}: {age} days old (threshold {max_age_days})."))
    return findings


def check_completeness(m):
    findings = []

    commits = m.get("commits")
    if commits is None:
        findings.append(("FAIL", "completeness",
                         "Missing 'commits' — the list of commits this packet covers. "
                         "Absence is invisible to a reviewer, who confirms what is in "
                         "front of them."))
    elif len(commits) == 0:
        findings.append(("FAIL", "completeness",
                         "'commits' is present but empty — a packet needs at least one "
                         "commit to evidence anything."))
    else:
        for i, c in enumerate(commits):
            label = c.get("commit", f"commits[{i}]")
            if c.get("change_content") is None:
                findings.append(("FAIL", "completeness",
                                 f"{label}: missing 'change_content' — what this "
                                 f"commit's own diff changed."))
            elif isinstance(c["change_content"], dict) and len(c["change_content"]) == 0:
                findings.append(("WARN", "completeness",
                                 f"{label}: 'change_content' is present but empty."))

    val = m.get("acceptance_criteria")
    label = "AC-to-diff mapping, or an explicit not_applicable with reason"
    if val is None:
        findings.append(("FAIL", "completeness",
                         f"Missing section 'acceptance_criteria' ({label}). Absence is "
                         f"invisible to a reviewer, who confirms what is in front of "
                         f"them."))
    elif isinstance(val, dict) and val.get("not_applicable"):
        if not (val.get("reason") or "").strip():
            findings.append(("FAIL", "completeness",
                             "'acceptance_criteria' marked not applicable with no reason."))
        else:
            findings.append(("INFO", "completeness",
                             f"'acceptance_criteria' not applicable: {val['reason']}"))
    elif isinstance(val, (list, dict, str)) and len(val) == 0:
        findings.append(("WARN", "completeness",
                         "'acceptance_criteria' is present but empty — populate it or "
                         "mark it not applicable with a reason."))
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--max-age-days", type=int, default=14)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    try:
        m = json.loads(Path(a.manifest).read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"Cannot read manifest: {e}")
        return 2

    findings, commits = check_provenance(m)
    findings += check_freshness(m, a.max_age_days)
    findings += check_completeness(m)

    fails = [f for f in findings if f[0] == "FAIL"]
    warns = [f for f in findings if f[0] == "WARN"]
    infos = [f for f in findings if f[0] == "INFO"]

    if a.json:
        print(json.dumps({"integrity": "FAIL" if fails else "PASS",
                          "release": m.get("release"),
                          "commits": [c.get("commit") for c in (m.get("commits") or [])],
                          "findings": [{"severity": s, "check": c, "detail": d}
                                       for s, c, d in findings]}, indent=2))
        return 1 if fails else 0

    rel = m.get("release") or {}
    commit_list = m.get("commits") or []
    shas = [c.get("commit", "—") for c in commit_list]
    print(f"\nEvidence integrity — {rel.get('name', 'unnamed packet')}")
    if len(shas) == 1:
        c0 = commit_list[0]
        print(f"Commit {c0.get('commit','—')} · "
              f"Author {c0.get('author','—')} · "
              f"Committed {c0.get('committed_at','—')}")
    else:
        print(f"Commits ({len(shas)}): {', '.join(shas) if shas else '—'}")
    print("=" * 74)

    print(f"\nINTEGRITY: {'FAIL' if fails else 'PASS'}"
          f" — {len(fails)} failure(s), {len(warns)} warning(s)")

    if fails:
        print("\nFAILURES — these belong at the top of the packet")
        print("-" * 74)
        for _, check, detail in fails:
            print(f"  ✗ [{check}] {detail}")
    if warns:
        print("\nWARNINGS")
        print("-" * 74)
        for _, check, detail in warns:
            print(f"  ! [{check}] {detail}")
    if infos:
        print("\nNOTES")
        print("-" * 74)
        for _, check, detail in infos:
            print(f"  · [{check}] {detail}")

    print("\nSUMMARY BY CHECK")
    print("-" * 74)
    for check in ("provenance", "freshness", "completeness"):
        n = sum(1 for s, c, _ in findings if c == check and s == "FAIL")
        print(f"  {'✗' if n else '✓'} {check}: {n} failure(s)")

    print("\n" + "-" * 74)
    if fails:
        print("Assemble the packet anyway — with these failures stated first. Omitting")
        print("them would leave someone reading a document whose parts disagree.")
    else:
        print("Integrity holds. This says the evidence is internally consistent and")
        print("about these commits — not any judgment on the change itself.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
