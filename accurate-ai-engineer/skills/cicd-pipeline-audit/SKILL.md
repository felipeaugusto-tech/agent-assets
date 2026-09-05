---
name: cicd-pipeline-audit
description: Audits a Jenkinsfile, Jenkins pipeline, or GitHub Actions workflow (and related Dockerfiles/plugins.txt) for security vulnerabilities and misconfigurations, and produces a structured audit report with severity ratings, OWASP CI/CD Top 10 mappings, evidence, and fix snippets. Use this whenever the user shares or references a Jenkinsfile, a `.github/workflows/*.yml` file, or a CI/CD pipeline and asks for a security review, audit, vulnerability scan, hardening check, or "is this pipeline safe" — even if they just paste the YAML/Groovy and ask "does this look ok" or "what's wrong with this". Also trigger for requests like "check our CI/CD for secrets exposure", "review our GitHub Actions permissions", "audit our build pipeline", or "prep this for a security review", even when the user doesn't say the word "audit" explicitly.
---

# CI/CD Pipeline Security Audit

Security bugs in Jenkinsfiles and GitHub Actions workflows are unusually high-leverage:
a single misconfigured `pull_request_target` trigger or one unescaped `${{ github.event.* }}`
interpolation can hand an external contributor a path to secrets, a write-scoped token, or
arbitrary code execution on your build infrastructure. Because pipeline configs are code that
runs with elevated trust and rarely gets the same review rigor as application code, they're
one of the most common places real breaches start (the tj-actions/changed-files supply-chain
compromise and the "pwn request" pattern in `references/cicd-security-checklist.md` are both
real, dated incidents, not hypotheticals). Treat this audit with the same seriousness as an
app security review.

## Overview of the workflow

1. **Get the pipeline file(s).** The user may attach a file, paste inline text, or point at a
   path/repo. If they paste config inline without a file, save it to a temp file with the
   correct name/extension first (`Jenkinsfile`, or `workflow.yml` under a `workflows/`
   directory) — the scanner and your own review both work off real files, and giving the
   pipeline file a realistic name also helps you reason about it the way you would a real repo.

2. **Run the first-pass scanner.**
   ```
   python3 <skill_dir>/scripts/scan_pipeline.py <path> > /tmp/scan_results.json
   ```
   This mechanically greps for the well-documented vulnerability patterns (unpinned actions,
   `pull_request_target` + untrusted checkout, script injection via untrusted context
   interpolation, hardcoded secrets, missing permissions blocks, Jenkins credential/Groovy
   injection patterns, and more) and returns structured JSON findings, each tagged with an
   `id` like `"4.1"` that maps directly to a numbered section in
   `references/cicd-security-checklist.md`.

   The scanner is deliberately narrow: it's pattern-matching, not a parser, so it will
   occasionally flag a placeholder value as a "hardcoded secret" or miss something that only
   shows up once you trace how a variable flows between steps. Treat its output as a
   worklist, not a final answer.

3. **Read your way through every finding, and read the file yourself too.** For each finding
   the scanner surfaced, open `references/cicd-security-checklist.md` at that section number
   to pull the accurate severity rationale, the OWASP CICD-SEC mapping, and a fix snippet to
   adapt to the user's actual code (don't just copy the generic example verbatim — match their
   variable names, action versions, and structure). Then read the whole pipeline file yourself
   with the same checklist in mind — the scanner can't understand Groovy control flow, can't
   tell whether a `pull_request_target` job actually executes untrusted code versus just
   labeling a PR, and can't tell a real secret from a test fixture. Your read is what turns
   raw pattern matches into a trustworthy report, and it's also how you'll catch the class of
   issue the scanner structurally can't: logic-dependent vulnerabilities, missing
   `CODEOWNERS`/branch-protection context implied by the file, or a fix that reintroduces the
   same problem it claims to solve.

4. **Filter and prioritize.** Drop clear false positives (a `TOKEN = "CHANGEME"` placeholder in
   a documented example isn't a Critical finding — though it's still worth a Low/Info note that
   it should never be replaced with a real value the same way). Merge duplicate findings that
   point at the same root cause. Where a check genuinely depends on information a static file
   can't provide (is this repo public? what's the org's default `GITHUB_TOKEN` permission?),
   say so explicitly rather than asserting a severity you can't back up — flag it as
   "needs verification" instead of guessing.

5. **Write the report** using the exact structure below, then deliver it as a file.

## Report structure

Always use this exact template for the report (as a Markdown file):

```markdown
# CI/CD Pipeline Security Audit Report

**Target:** [file name(s)/repo audited]
**Date:** [today's date]
**Pipeline type:** [GitHub Actions / Jenkins / both]

## Executive Summary
[2-4 sentences, written for someone who won't read past this section: what was audited,
how many findings at each severity, and the single most important thing to fix first.]

## Findings Summary

| Severity | Count |
|---|---|
| Critical | N |
| High | N |
| Medium | N |
| Low | N |

## Detailed Findings

Group by severity (Critical first, then High, Medium, Low). For each finding:

### [Severity] — [Short title]
- **Location:** `path/to/file:line`
- **OWASP CI/CD Top 10:** CICD-SEC-N — [name]
- **Description:** [what the issue is and why it matters, in plain language]
- **Evidence:**
  ```
  [the actual matched line(s) from the file]
  ```
- **Remediation:**
  ```
  [a corrected snippet adapted to this file's actual code, not a generic template]
  ```

## Needs Manual/Organizational Verification
[Checks that depend on context outside the file itself — repo visibility for self-hosted
runners, org-level default token permissions, branch protection settings, whether Script
Security sandbox approvals are being rubber-stamped, etc. State what to check and why it
matters, rather than omitting these just because they can't be resolved from the file alone.]

## Appendix: Methodology
[One line: which files were scanned, and that findings were cross-checked against the
OWASP CI/CD Top 10 / GitHub's and Jenkins' own security hardening documentation.]
```

Notes on filling this in well:
- Order findings within a severity tier by how directly exploitable they are, not by file order.
- A report with zero Critical/High findings is a legitimate, good outcome — don't manufacture
  severity to make the report feel more substantial. If the pipeline is genuinely solid, say so
  and note what it's already doing right (e.g. "actions are already SHA-pinned" is worth calling
  out as a positive, not just an absence of a finding).
- If both a Jenkinsfile and a GitHub Actions workflow were audited together, keep them in one
  report but make it easy to scan per-system (either two Detailed Findings subsections, or a
  "System" column if using a table).

## Delivering the report

Save the report as a `.md` file and send it to the user — this is a document they'll want to
keep, share with a security team, or attach to a ticket, so a real file beats a wall of chat
text. If they asked for a different format (Word doc, PDF, HTML), build the Markdown content
first exactly as above, then convert using the appropriate skill (docx/pdf) rather than
reinventing the structure in that format from scratch.

## Reference material

`references/cicd-security-checklist.md` is the full technical reference this skill is built
on: every check the scanner runs, organized by category (Secrets & Credential Exposure, Supply
Chain & Pinning, Permissions & Least Privilege, Injection & Untrusted Input, General Hardening),
each with severity rationale, detection patterns, before/after fix code, and a citation to a
named primary source (OWASP CI/CD Top 10, GitHub's own Security Hardening guide, GitHub
Security Lab writeups, Jenkins Security Advisories, SLSA.dev). It also documents the OWASP
Top 10 CI/CD Security Risks framework used to classify findings, and closes with a quick-
reference grep cheat sheet if you want to double-check a pattern by hand. Read the specific
sections relevant to what you found — you don't need to read the whole thing for every audit,
but do look up every category that produced a finding, since the "why it matters" and the fix
snippet are usually more precise than what you'd write from memory.
