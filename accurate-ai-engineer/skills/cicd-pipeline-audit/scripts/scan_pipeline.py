#!/usr/bin/env python3
"""
scan_pipeline.py — deterministic first-pass scanner for GitHub Actions workflows,
Jenkinsfiles, and related Dockerfiles.

This script does the mechanical part of a pipeline security audit: it greps for
the well-known vulnerability patterns documented in
references/cicd-security-checklist.md and emits structured JSON findings.

It is intentionally a *first pass*, not the whole audit:
- It is pattern-based, so it will produce some false positives (e.g. a "hardcoded
  secret" pattern matching an obviously-fake placeholder like "CHANGEME") and can
  miss issues that only show up from understanding control/data flow (e.g. a
  Groovy `if` branch that only takes the unsafe path under certain params).
- Several checks depend on context this script cannot see (is the repo public?,
  what's the org's default GITHUB_TOKEN permission?). Those are emitted with
  "needs_verification": true so the report can call them out rather than assert
  a severity with false confidence.

Read every finding against the actual file before writing it up — the `id` field
maps directly to a numbered section in references/cicd-security-checklist.md
(e.g. "4.1" -> "Part 4, section 4.1"), which has the full rationale, severity
justification, and a fix snippet to adapt.

Usage:
    python3 scan_pipeline.py <path> [<path> ...]
    python3 scan_pipeline.py --json <path>   # (default) machine-readable output
    python3 scan_pipeline.py --pretty <path> # human-readable grouped output

<path> can be a single file (Jenkinsfile, a workflow .yml, a Dockerfile) or a
directory, which is walked recursively.
"""

import argparse
import json
import os
import re
import sys

FORTY_HEX = re.compile(r"^[0-9a-fA-F]{40}$")

# ---------------------------------------------------------------------------
# File classification
# ---------------------------------------------------------------------------

def classify_file(path):
    name = os.path.basename(path)
    lower = name.lower()
    parts = [p.lower() for p in path.split(os.sep)]

    if lower.startswith("jenkinsfile"):
        return "jenkins"
    if lower.endswith(".jenkinsfile"):
        return "jenkins"
    if lower == "plugins.txt":
        return "jenkins_plugins"
    if lower.startswith("dockerfile"):
        return "dockerfile"
    if lower.endswith((".yml", ".yaml")) and ("workflows" in parts or ".github" in parts):
        return "github_actions"
    if lower.endswith((".yml", ".yaml")):
        # Could still be a GitHub Actions workflow pasted/saved outside .github/workflows/
        # (common when a user uploads a single workflow file). Sniff content instead.
        try:
            with open(path, "r", errors="ignore") as f:
                head = f.read(4000)
            if re.search(r"^\s*(on|jobs)\s*:", head, re.MULTILINE):
                return "github_actions"
        except OSError:
            pass
    return None


def discover_files(paths):
    found = []
    for p in paths:
        if os.path.isfile(p):
            ftype = classify_file(p)
            if ftype:
                found.append((p, ftype))
            else:
                # Unknown single file explicitly passed — still try to sniff it as
                # either a Jenkinsfile-like Groovy script or a YAML workflow.
                try:
                    with open(p, "r", errors="ignore") as f:
                        head = f.read(4000)
                except OSError:
                    head = ""
                if re.search(r"\bpipeline\s*\{|\bnode\s*\(|\bstage\s*\(", head):
                    found.append((p, "jenkins"))
                elif re.search(r"^\s*(on|jobs)\s*:", head, re.MULTILINE):
                    found.append((p, "github_actions"))
        elif os.path.isdir(p):
            for root, _dirs, files in os.walk(p):
                if "/.git/" in root + "/" or root.endswith("/.git"):
                    continue
                for fn in files:
                    fp = os.path.join(root, fn)
                    ftype = classify_file(fp)
                    if ftype:
                        found.append((fp, ftype))
    return found


# ---------------------------------------------------------------------------
# Finding helper
# ---------------------------------------------------------------------------

def finding(id_, title, severity, cicd_sec, file_, line_no, evidence, needs_verification=False):
    return {
        "id": id_,
        "title": title,
        "severity": severity,
        "owasp_cicd_sec": cicd_sec,
        "file": file_,
        "line": line_no,
        "evidence": evidence.strip(),
        "needs_verification": needs_verification,
    }


def lines_of(path):
    try:
        with open(path, "r", errors="ignore") as f:
            return f.readlines()
    except OSError:
        return []


# ---------------------------------------------------------------------------
# GitHub Actions checks (references/cicd-security-checklist.md Parts 1-5)
# ---------------------------------------------------------------------------

SECRET_SHAPE = re.compile(
    r"(AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|gh[a-z]_[A-Za-z0-9]{30,}|xox[baprs]-[0-9A-Za-z-]+|"
    r"-----BEGIN (RSA|EC|OPENSSH|PGP) PRIVATE KEY-----)"
)
GENERIC_SECRET_ASSIGNMENT = re.compile(
    r"(?i)(password|passwd|token|apikey|api[_-]?key|secret|access[_-]?key)['\"]?\s*[:=]\s*['\"][^'\"$]{6,}['\"]"
)
PLACEHOLDER_HINTS = re.compile(r"(?i)(changeme|your[_-]?(token|key|secret)|xxxx+|<[a-z_-]+>|\$\{|example|dummy|placeholder|redacted|fake)")


def check_github_actions(path):
    findings = []
    text_lines = lines_of(path)
    full_text = "".join(text_lines)

    has_pull_request_target = bool(re.search(r"pull_request_target", full_text))
    has_top_level_permissions = bool(re.search(r"^permissions\s*:", full_text, re.MULTILINE))

    for i, line in enumerate(text_lines, start=1):
        # 1.1 hardcoded secrets
        if SECRET_SHAPE.search(line):
            findings.append(finding("1.1", "Hardcoded secret/token in workflow", "Critical",
                                     "CICD-SEC-6", path, i, line))
        elif GENERIC_SECRET_ASSIGNMENT.search(line) and "secrets." not in line and "vars." not in line:
            sev = "Medium" if PLACEHOLDER_HINTS.search(line) else "Critical"
            findings.append(finding("1.1", "Possible hardcoded credential (verify it isn't a placeholder)",
                                     sev, "CICD-SEC-6", path, i, line))

        # 1.2 secrets echoed to logs
        if re.search(r'echo\s+\$\{\{\s*secrets\.|echo\s+"?\$\{?[A-Z_]*(TOKEN|SECRET|KEY|PASSWORD)|printenv\b', line):
            findings.append(finding("1.2", "Secret-bound value may be printed to logs", "High",
                                     "CICD-SEC-6", path, i, line))
        if re.search(r"^\s*run:\s*env\s*$|^\s*-\s*run:\s*env\s*$", line):
            findings.append(finding("1.2", "'run: env' dumps all environment variables to the log", "High",
                                     "CICD-SEC-6", path, i, line))

        # 2.1 / 2.2 unpinned actions
        m = re.search(r"uses:\s*([A-Za-z0-9._-]+/[A-Za-z0-9._-]+)@([A-Za-z0-9._\-/]+)", line)
        if m and not line.strip().startswith("#"):
            ref = m.group(2)
            if not FORTY_HEX.match(ref):
                sev = "High" if ref in ("main", "master", "latest", "develop") else "High"
                findings.append(finding("2.1", f"Action '{m.group(1)}' pinned to mutable ref '@{ref}' instead of a commit SHA",
                                         sev, "CICD-SEC-3", path, i, line))

        # 3.2 write-all
        if re.search(r"permissions:\s*write-all", line):
            findings.append(finding("3.2", "'permissions: write-all' grants the GITHUB_TOKEN broad write access", "High",
                                     "CICD-SEC-5", path, i, line))

        # 4.1 script injection: untrusted context spliced into a run: line (not an env: assignment)
        if re.search(r"\$\{\{\s*(github\.event\.(issue|pull_request|comment|review|commits|head_commit|discussion)\.[A-Za-z_.\[\]0-9]+|github\.head_ref)\s*\}\}", line):
            looks_like_env_assignment = bool(re.match(r"^\s*[A-Za-z_][A-Za-z0-9_]*\s*:\s*\$\{\{", line))
            if not looks_like_env_assignment:
                findings.append(finding("4.1", "Untrusted GitHub context value spliced directly into a shell/script line (script injection)",
                                         "Critical", "CICD-SEC-4", path, i, line))

        # 4.3 github-script with untrusted interpolation
        if re.search(r"\$\{\{\s*github\.event\.", line) and i > 1 and "script:" in "".join(text_lines[max(0, i-6):i]):
            if re.search(r"actions/github-script", "".join(text_lines[max(0, i-10):i])):
                findings.append(finding("4.3", "Untrusted context value spliced into a github-script JS block", "Critical",
                                         "CICD-SEC-4", path, i, line))

        # 5.5 self-hosted runners
        if re.search(r"runs-on:.*self-hosted", line):
            findings.append(finding("5.5", "Self-hosted runner referenced — confirm this repo is NOT public",
                                     "Critical", "CICD-SEC-7", path, i, line, needs_verification=True))

        # 5.6 deprecated workflow commands (CVE-2020-15228)
        if re.search(r"::(set-output|save-state|set-env|add-path)\b", line):
            findings.append(finding("5.6", "Deprecated stdout-parsed workflow command (env-injection risk, CVE-2020-15228)",
                                     "High", "CICD-SEC-7", path, i, line))

    # 1.5 pull_request_target + untrusted checkout
    if has_pull_request_target:
        for i, line in enumerate(text_lines, start=1):
            if re.search(r"ref:\s*\$\{\{\s*github\.event\.pull_request\.head\.(sha|ref)", line):
                findings.append(finding("1.5", "pull_request_target checks out untrusted PR head — secrets/write token may be exposed to attacker-controlled code",
                                         "Critical", "CICD-SEC-4", path, i, line))

    # 3.1 missing top-level permissions block (file-level finding, reported once at line 1)
    if not has_top_level_permissions:
        findings.append(finding("3.1", "No top-level 'permissions:' block — GITHUB_TOKEN scope depends on org/repo defaults rather than an explicit, auditable grant",
                                 "Medium", "CICD-SEC-5", path, 1, "(no 'permissions:' key found in file)",
                                 needs_verification=True))

    # 5.1 missing timeout-minutes (file-level, only if the file defines jobs)
    if re.search(r"^jobs\s*:", full_text, re.MULTILINE) and "timeout-minutes" not in full_text:
        findings.append(finding("5.1", "No 'timeout-minutes' set on any job — defaults to GitHub's 360-minute cap",
                                 "Low", "CICD-SEC-7", path, 1, "(no 'timeout-minutes' found in file)"))

    # 5.7 checkout without persist-credentials: false
    for i, line in enumerate(text_lines, start=1):
        if re.search(r"uses:\s*actions/checkout", line):
            window = "".join(text_lines[i:i+5])
            if "persist-credentials: false" not in window and "persist-credentials:false" not in window:
                findings.append(finding("5.7", "actions/checkout leaves GITHUB_TOKEN in git config for the rest of the job (persist-credentials defaults to true)",
                                         "Medium", "CICD-SEC-6", path, i, line))

    return findings


def check_dockerfile(path):
    findings = []
    for i, line in enumerate(lines_of(path), start=1):
        if re.match(r"^\s*FROM\s+\S+\s*$", line) and ("latest" in line or ":" not in line.split()[1] if len(line.split()) > 1 else True):
            findings.append(finding("2.5", "Base image not pinned to a specific version/digest (uses 'latest' or no tag)",
                                     "Medium", "CICD-SEC-3", path, i, line))
        if re.search(r"(?i)(ARG|--build-arg)\s+\S*(PASSWORD|TOKEN|SECRET|KEY)", line):
            findings.append(finding("1.7", "Secret passed via Docker build arg — persists in image history/layers",
                                     "High", "CICD-SEC-6", path, i, line))
    return findings


# ---------------------------------------------------------------------------
# Jenkins checks
# ---------------------------------------------------------------------------

def check_jenkinsfile(path):
    findings = []
    text_lines = lines_of(path)

    for i, line in enumerate(text_lines, start=1):
        if SECRET_SHAPE.search(line):
            findings.append(finding("1.1", "Hardcoded secret/token in Jenkinsfile", "Critical",
                                     "CICD-SEC-6", path, i, line))
        elif GENERIC_SECRET_ASSIGNMENT.search(line) and "credentials(" not in line:
            sev = "Medium" if PLACEHOLDER_HINTS.search(line) else "Critical"
            findings.append(finding("1.1", "Possible hardcoded credential (verify it isn't a placeholder)",
                                     sev, "CICD-SEC-6", path, i, line))

        # 1.6 double-quoted sh string interpolating what looks like a bound credential var
        if re.search(r'sh\s*\(?\s*"[^"]*\$\{?\s*(USR|PSW|USER|PASS|PASSWORD|TOKEN|SECRET|KEY|CREDENTIAL)', line, re.I):
            findings.append(finding("1.6", "Double-quoted 'sh' string interpolates a credential-like variable — defeats console-log masking and risks injection",
                                     "High", "CICD-SEC-6", path, i, line))

        # 4.6 shell injection via params./env. in double-quoted sh string
        if re.search(r'sh\s*\(?\s*"[^"]*\$\{?\s*(params|env)\.[A-Za-z_][A-Za-z0-9_]*', line):
            findings.append(finding("4.6", "Groovy double-quoted string splices params./env. value directly into a shell command (command injection)",
                                     "Critical", "CICD-SEC-4", path, i, line))

        # 3.5 / 4.5 sandbox escape patterns
        if re.search(r"(class\.forName|\.classLoader|@Grab\b|@Grapes\b|System\.getProperty)", line):
            findings.append(finding("4.5", "Reflection/dynamic-loading pattern commonly associated with Groovy sandbox escapes",
                                     "Critical", "CICD-SEC-7", path, i, line, needs_verification=True))

        # 3.4 docker agent without non-root user
        if re.search(r"agent\s*\{", line):
            window = "".join(text_lines[i-1:i+6])
            if re.search(r"docker\s*\{", window) and "image" in window and not re.search(r"args\s+['\"]-u\s", window):
                findings.append(finding("3.4", "Docker agent has no '-u' non-root user argument — build likely runs as root",
                                         "High", "CICD-SEC-7", path, i, line, needs_verification=True))

        # missing timeout (5.1 analog)
    if "timeout(" not in "".join(text_lines):
        findings.append(finding("5.1", "No 'timeout(...)' option found — a hung/runaway build has no automatic cutoff",
                                 "Low", "CICD-SEC-7", path, 1, "(no 'timeout(' found in file)"))

    return findings


def check_jenkins_plugins(path):
    findings = []
    for i, line in enumerate(lines_of(path), start=1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if ":" not in s:
            findings.append(finding("2.4", "Plugin has no version pin — will always resolve to latest",
                                     "Medium", "CICD-SEC-3", path, i, line))
    return findings


def check_bootstrap_flags(path):
    """Applies to any file — Dockerfiles, IaC, shell scripts, groovy init scripts —
    since these flags can show up in any provisioning artifact."""
    findings = []
    for i, line in enumerate(lines_of(path), start=1):
        if "DISABLE_CSRF_PROTECTION" in line:
            findings.append(finding("5.9", "Jenkins CSRF protection explicitly disabled", "Critical",
                                     "CICD-SEC-7", path, i, line))
        if "runSetupWizard=false" in line:
            findings.append(finding("5.10", "Jenkins setup wizard skipped — verify a real securityRealm/authorizationStrategy is configured before the controller is network-reachable",
                                     "High", "CICD-SEC-7", path, i, line, needs_verification=True))
    return findings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

SEVERITY_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="File(s) or directory/directories to scan")
    ap.add_argument("--pretty", action="store_true", help="Print human-readable grouped output instead of JSON")
    args = ap.parse_args()

    files = discover_files(args.paths)
    if not files:
        print(json.dumps({"error": "No Jenkinsfile, GitHub Actions workflow, Dockerfile, or plugins.txt found",
                           "searched": args.paths}), file=sys.stdout)
        sys.exit(0)

    all_findings = []
    for path, ftype in files:
        if ftype == "github_actions":
            all_findings.extend(check_github_actions(path))
        elif ftype == "jenkins":
            all_findings.extend(check_jenkinsfile(path))
            all_findings.extend(check_bootstrap_flags(path))
        elif ftype == "jenkins_plugins":
            all_findings.extend(check_jenkins_plugins(path))
        elif ftype == "dockerfile":
            all_findings.extend(check_dockerfile(path))
            all_findings.extend(check_bootstrap_flags(path))

    all_findings.sort(key=lambda f: (SEVERITY_ORDER.get(f["severity"], 9), f["file"], f["line"]))

    if args.pretty:
        by_sev = {}
        for f in all_findings:
            by_sev.setdefault(f["severity"], []).append(f)
        for sev in ["Critical", "High", "Medium", "Low"]:
            if sev not in by_sev:
                continue
            print(f"\n=== {sev} ({len(by_sev[sev])}) ===")
            for f in by_sev[sev]:
                verify = " [NEEDS VERIFICATION]" if f["needs_verification"] else ""
                print(f"  [{f['id']}] {f['title']}{verify}")
                print(f"      {f['file']}:{f['line']}")
                print(f"      {f['evidence']}")
        print(f"\nScanned {len(files)} file(s), {len(all_findings)} raw finding(s) before manual review/dedup.")
    else:
        print(json.dumps({
            "files_scanned": [{"path": p, "type": t} for p, t in files],
            "findings": all_findings,
        }, indent=2))


if __name__ == "__main__":
    main()
