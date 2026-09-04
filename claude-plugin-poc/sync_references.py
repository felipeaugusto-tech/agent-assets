#!/usr/bin/env python3
"""Keep the gendd plugin's generated content in sync with its sources.

WHY THIS EXISTS
    A Claude Code plugin cannot read files outside its own directory, so anything
    a skill needs has to be COPIED into the plugin. Copies go stale silently:
    someone improves a workflow in gendd-analysis/ and the plugin keeps shipping
    the old text forever, with nothing to say so.

    This script is the record of where every copy came from, and `--check` is what
    notices when a source moves without the plugin. Claude Code neither runs nor
    reads this file. It is ours.

THREE KINDS OF GENERATED CONTENT

    1. REFS -- corpus documents copied into references/<skill>/<basename>.
       For skills whose SKILL.md we author ourselves. The body addresses them as
       ${CLAUDE_PLUGIN_ROOT}/references/<skill>/<file>.

       The map cannot be inferred from filenames: create-context-pack.md, for
       example, exists in BOTH workflows/ and playbooks/on-demand/.

    2. VENDORED -- .skill packages under vendor/, unpacked into skills/<name>/.
       Every .skill in the Claude Skills library uses RELATIVE paths internally
       (references/foo.md, scripts/bar.py) and none uses ${CLAUDE_PLUGIN_ROOT}, so
       mirroring the package's own tree means it needs no editing at all. The
       package stays the source of truth and the unpacked copy stays disposable.

    3. TREES -- whole corpus subtrees mirrored path-for-path into
       references/<skill>/<dir>/. Only for a skill that must preserve the
       corpus's own relative paths (lookup-standard resolves rules-manifest.yaml's
       `file:` column directly against these paths) -- REFS's flat one-file-per-
       line copy would collide on basenames like README.md that repeat across
       every tech-overlay subdirectory of sdlc/.

    A skill in none of these maps is hand-written, and this script never touches it.

USAGE
    python sync_references.py            regenerate everything from the sources
    python sync_references.py --check    verify the committed copies match their
                                         sources, change nothing. Exit 0 = in sync,
                                         exit 1 = stale. Use this in CI.

Runs the same on PowerShell, Git Bash, macOS and Linux. Python 3.8+, stdlib only.
"""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

# =====================================================================
#  MAP 1 -- corpus documents.  (skill name, path relative to agent-assets/)
#  Adding a corpus-wrapped skill means adding its entries here and nothing else.
# =====================================================================

REFS: list[tuple[str, str]] = [
    # --- enhance-requirements -----------------------------------------
    #     primary task flow | detailed methodology | required output format
    ("enhance-requirements", "gendd-analysis/playbooks/on-demand/enhance-requirements.md"),
    ("enhance-requirements", "gendd-analysis/workflows/enhance-acceptance-criteria.md"),
    ("enhance-requirements", "gendd-analysis/templates/requirements-enhancement.md"),

    # --- run-brownfield-analysis --------------------------------------
    #     task flow | documentation rules | detailed methodology | the four pass agents
    #     NB: create-context-pack is NOT packaged -- workflows/create-context-pack.md
    #     is marked DEPRECATED upstream, superseded by the Analyze & Generate flow.
    ("run-brownfield-analysis", "gendd-analysis/playbooks/onboarding/run-brownfield-analysis.md"),
    ("run-brownfield-analysis", "gendd-analysis/templates/documentation-guidelines.md"),
    ("run-brownfield-analysis", "gendd-analysis/workflows/brownfield-repository-analysis.md"),
    ("run-brownfield-analysis", "gendd-analysis/agents/pass1-scan-agent.md"),
    ("run-brownfield-analysis", "gendd-analysis/agents/pass2-infer-agent.md"),
    ("run-brownfield-analysis", "gendd-analysis/agents/pass3-validate-hitl-agent.md"),
    ("run-brownfield-analysis", "gendd-analysis/agents/pass4-document-agent.md"),

    # --- generate-context-areas -----------------------------------------
    #     task flow | output template | area-detection fallback | 16 area frameworks
    ("generate-context-areas", "gendd-analysis/workflows/generate-context-areas.md"),
    ("generate-context-areas", "gendd-analysis/templates/context-area.md"),
    ("generate-context-areas", "gendd-analysis/agents/pass5-role-detector-agent.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/architecture.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/backend-development.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/database-management.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/delivery-management.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/devops-infrastructure.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/frontend-development.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/fullstack-development.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/product-management.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/quality-assurance.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/release-management.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/security.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/site-reliability.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/support-engineering.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/technical-leadership.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/technical-writing.md"),
    ("generate-context-areas", "gendd-analysis/knowledge/sdlc-areas/user-experience.md"),

    # --- detect-and-generate-standards -----------------------------------
    #     task flow | generic skeleton | 7 filled worked examples
    ("detect-and-generate-standards", "gendd-analysis/workflows/detect-and-generate-standards.md"),
    ("detect-and-generate-standards", "gendd-analysis/templates/standards/_template.md"),
    ("detect-and-generate-standards", "gendd-analysis/templates/standards/architecture.md"),
    ("detect-and-generate-standards", "gendd-analysis/templates/standards/coding.md"),
    ("detect-and-generate-standards", "gendd-analysis/templates/standards/delivery.md"),
    ("detect-and-generate-standards", "gendd-analysis/templates/standards/operations.md"),
    ("detect-and-generate-standards", "gendd-analysis/templates/standards/product.md"),
    ("detect-and-generate-standards", "gendd-analysis/templates/standards/security.md"),
    ("detect-and-generate-standards", "gendd-analysis/templates/standards/testing.md"),

    # --- generate-ide-rules ------------------------------------------------
    #     task flow | 5 output templates | 6 baseline format knowledge files
    ("generate-ide-rules", "gendd-analysis/workflows/generate-ide-rules.md"),
    ("generate-ide-rules", "gendd-analysis/templates/ide-rules/cursor-rule.md"),
    ("generate-ide-rules", "gendd-analysis/templates/ide-rules/claude-code-rule.md"),
    ("generate-ide-rules", "gendd-analysis/templates/ide-rules/antigravity-rule.md"),
    ("generate-ide-rules", "gendd-analysis/templates/ide-rules/copilot-instructions.md"),
    ("generate-ide-rules", "gendd-analysis/templates/ide-rules/generic-rule.md"),
    ("generate-ide-rules", "gendd-analysis/knowledge/ide-formats/_README.md"),
    ("generate-ide-rules", "gendd-analysis/knowledge/ide-formats/cursor.md"),
    ("generate-ide-rules", "gendd-analysis/knowledge/ide-formats/claude-code.md"),
    ("generate-ide-rules", "gendd-analysis/knowledge/ide-formats/antigravity.md"),
    ("generate-ide-rules", "gendd-analysis/knowledge/ide-formats/copilot.md"),
    ("generate-ide-rules", "gendd-analysis/knowledge/ide-formats/generic.md"),

    # --- greenfield-analysis ------------------------------------------------
    ("greenfield-analysis", "gendd-analysis/workflows/greenfield-analysis.md"),

    # --- run-delta-analysis --------------------------------------------------
    ("run-delta-analysis", "gendd-analysis/playbooks/on-demand/run-delta-analysis.md"),

    # --- incremental-doc-update ----------------------------------------------
    #     task flow | targeted re-analysis method | output formatting rules
    ("incremental-doc-update", "gendd-analysis/workflows/incremental-doc-update.md"),
    ("incremental-doc-update", "gendd-analysis/agents/pass2-infer-agent.md"),
    ("incremental-doc-update", "gendd-analysis/templates/documentation-guidelines.md"),

    # --- audit-ui-patterns -----------------------------------------------
    #     task flow | the UX designer role-playbook it delegates to
    ("audit-ui-patterns", "gendd-analysis/playbooks/on-demand/audit-ui-patterns.md"),
    ("audit-ui-patterns", "gendd-analysis/playbooks/by-role/ux-designer.md"),

    # --- analyze-and-generate ----------------------------------------------
    #     the orchestration map over phases already packaged as their own skills
    ("analyze-and-generate", "gendd-analysis/workflows/analyze-and-generate.md"),

    # --- validate-acceptance-criteria ---------------------------------------
    #     task flow | selector/testing conventions | foundational testing principles
    ("validate-acceptance-criteria", "gendd-analysis/playbooks/on-demand/validate-acceptance-criteria.md"),
    ("validate-acceptance-criteria", "gendd-analysis/templates/testing-standards.md"),
    ("validate-acceptance-criteria", "gendd-analysis/templates/standards/testing.md"),

    # --- run-assisted-testing ------------------------------------------------
    ("run-assisted-testing", "gendd-analysis/playbooks/on-demand/run-assisted-testing.md"),
    ("run-assisted-testing", "gendd-analysis/templates/testing-standards.md"),
    ("run-assisted-testing", "gendd-analysis/templates/standards/testing.md"),

    # --- review-test-coverage ------------------------------------------------
    #     task flow | gap-analysis method | foundational testing principles
    ("review-test-coverage", "gendd-analysis/playbooks/recurring/review-test-coverage.md"),
    ("review-test-coverage", "gendd-analysis/playbooks/on-demand/identify-test-gaps.md"),
    ("review-test-coverage", "gendd-analysis/templates/standards/testing.md"),

    # --- generate-standards ---------------------------------------------
    ("generate-standards", "gendd-analysis/playbooks/on-demand/generate-standards.md"),

    # --- analyze-database-schema -------------------------------------------
    #     task flow | the DBA role-playbook it delegates to
    ("analyze-database-schema", "gendd-analysis/playbooks/on-demand/analyze-database-schema.md"),
    ("analyze-database-schema", "gendd-analysis/playbooks/by-role/dba.md"),

    # --- generate-unit-tests -------------------------------------------------
    #     task flow | requirement levels | foundational principles | 2 stack guides
    ("generate-unit-tests", "gendd-analysis/workflows/generate-unit-tests.md"),
    ("generate-unit-tests", "gendd-analysis/templates/testing-standards.md"),
    ("generate-unit-tests", "gendd-analysis/templates/standards/testing.md"),
    ("generate-unit-tests", "code-and-test-templates/test/java-unit-test-generation.md"),
    ("generate-unit-tests", "code-and-test-templates/test/angular-unit-test-generation.md"),

    # --- lookup-standard / compile-rules -----------------------------------
    #     the routing manifest itself (also used by compile-rules)
    ("lookup-standard", "rules-manifest.yaml"),
    ("compile-rules", "rules-manifest.yaml"),
    ("compile-rules", "gendd-analysis/templates/ide-rules/cursor-rule.md"),
    ("compile-rules", "gendd-analysis/templates/ide-rules/claude-code-rule.md"),
    ("compile-rules", "gendd-analysis/templates/ide-rules/antigravity-rule.md"),
    ("compile-rules", "gendd-analysis/templates/ide-rules/copilot-instructions.md"),
    ("compile-rules", "gendd-analysis/templates/ide-rules/generic-rule.md"),

    # --- audit-observability -------------------------------------------
    #     task flow | the SRE role-playbook it delegates to
    ("audit-observability", "gendd-analysis/playbooks/on-demand/audit-observability.md"),
    ("audit-observability", "gendd-analysis/playbooks/by-role/sre.md"),

    # --- generate-support-documentation ---------------------------------
    #     task flow | the Support Engineer role-playbook it delegates to
    ("generate-support-documentation", "gendd-analysis/playbooks/on-demand/generate-support-documentation.md"),
    ("generate-support-documentation", "gendd-analysis/playbooks/by-role/support-engineer.md"),

    # --- implementation-plan (Phase 3 -- new corpus methodology) ------------
    ("implementation-plan", "gendd-analysis/workflows/implementation-plan.md"),
    ("implementation-plan", "gendd-analysis/templates/implementation-plan-template.md"),

    # --- spec-authoring (Phase 3 -- new corpus methodology) -----------------
    ("spec-authoring", "gendd-analysis/workflows/spec-authoring.md"),
    ("spec-authoring", "gendd-analysis/templates/spec-template.md"),

    # --- spike-doc (Phase 3 -- new corpus methodology) ----------------------
    ("spike-doc", "gendd-analysis/workflows/spike-doc.md"),
    ("spike-doc", "gendd-analysis/templates/spike-template.md"),

    # --- pr-pre-review (Phase 3 -- new corpus methodology) ------------------
    #     task flow | report template | routing manifest (sdlc/governance tree reused from lookup-standard)
    ("pr-pre-review", "gendd-analysis/workflows/pr-pre-review.md"),
    ("pr-pre-review", "gendd-analysis/templates/pr-pre-review-template.md"),
    ("pr-pre-review", "rules-manifest.yaml"),
]

# =====================================================================
#  MAP 2 -- .skill packages in vendor/, unpacked verbatim into skills/<name>/.
#  The archive's top-level directory name becomes the skill name.
# =====================================================================

VENDORED: list[str] = [
    "adr-writer.skill",
    "prd-writer.skill",
    "stories-from-source.skill",           # the _v2 archive, renamed -- the non-_v2 one is retired
    "jira-story-estimator.skill",          # renamed from the stray "jira-story-estimator 1.skill"
    "architecture-diagram-generator.skill",  # wins over workflows/generate-architecture-diagrams.md -- ships lint_c4.py
    "release-evidence-packet.skill",         # ships verify_evidence.py
    "cicd-pipeline-audit.skill",              # ships scan_pipeline.py
    "test-gap-analyzer.skill",                # wins over workflows/identify-test-gaps.md -- ships analyze_test_gaps.py
                                               # (re-zipped from the QA toolset's unzipped skill folder)
    "qa-test-case-writer.skill",              # re-zipped from the QA toolset's unzipped skill folder
    "test-automation-implementer.skill",      # re-zipped from the QA toolset's unzipped skill folder
    "testrail-publisher.skill",               # re-zipped; the MCP server itself stays out of this plugin
]

# =====================================================================
#  MAP 3 -- whole corpus subtrees, mirrored path-for-path into references/<skill>/.
#  Only for a skill that must preserve the corpus's own relative paths verbatim
#  (rules-manifest.yaml's `file:` column) -- a flat copy of sdlc/** would collide
#  on basenames like README.md that repeat across every tech-overlay subdirectory.
# =====================================================================

TREES: list[tuple[str, str]] = [
    ("lookup-standard", "sdlc"),
    ("lookup-standard", "governance"),
]

# =====================================================================

PLUGIN_DIR = Path(__file__).resolve().parent      # claude-plugin-poc/
CORPUS = PLUGIN_DIR.parent                        # agent-assets/
VENDOR = PLUGIN_DIR / "vendor"


def _fail(lines: list[str]) -> "None":
    for line in lines:
        print(line, file=sys.stderr)
    sys.exit(1)


def vendored_skill_name(archive: Path) -> str:
    """The single top-level directory inside a .skill archive."""
    with zipfile.ZipFile(archive) as z:
        roots = {Path(n).parts[0] for n in z.namelist() if n.strip()}
    if len(roots) != 1:
        _fail([f"{archive.name}: expected one top-level directory, found {sorted(roots)}"])
    return roots.pop()


def build(dest: Path) -> tuple[int, int, int]:
    """Generate everything under dest. Returns (corpus files, vendored files, tree files)."""
    missing = [src for _, src in REFS if not (CORPUS / src).is_file()]
    missing += [f"vendor/{a}" for a in VENDORED if not (VENDOR / a).is_file()]
    missing += [d for _, d in TREES if not (CORPUS / d).is_dir()]
    if missing:
        _fail([f"missing source: {m}" for m in missing])

    # --- map 1: corpus -> references/
    refs_root = dest / "references"
    if refs_root.exists():
        shutil.rmtree(refs_root)          # so a removed entry actually disappears
    for skill, src in REFS:
        target = refs_root / skill
        target.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(CORPUS / src, target / Path(src).name)

    # --- map 3: whole corpus subtrees -> references/<skill>/<dir>/, mirrored
    tree_count = 0
    for skill, d in TREES:
        target = refs_root / skill / d
        shutil.copytree(CORPUS / d, target, dirs_exist_ok=True)
        tree_count += sum(1 for p in target.rglob("*") if p.is_file())

    # --- map 2: vendor/*.skill -> skills/<name>/
    vendored_count = 0
    for archive_name in VENDORED:
        archive = VENDOR / archive_name
        name = vendored_skill_name(archive)
        target = dest / "skills" / name
        if target.exists():
            shutil.rmtree(target)
        with zipfile.ZipFile(archive) as z:
            for info in z.infolist():
                if info.is_dir():
                    continue
                rel = Path(*Path(info.filename).parts[1:])   # strip the archive root
                out = target / rel
                out.parent.mkdir(parents=True, exist_ok=True)
                with z.open(info) as fh, open(out, "wb") as dst:
                    shutil.copyfileobj(fh, dst)
                vendored_count += 1

    return len(REFS), vendored_count, tree_count


def managed_paths() -> list[Path]:
    """Every path this script owns, relative to the plugin directory."""
    paths = [Path("references")]
    paths += [Path("skills") / vendored_skill_name(VENDOR / a) for a in VENDORED]
    return paths


def differences(live_root: Path, expected_root: Path, rel: Path) -> list[str]:
    """Where the committed tree and a fresh build disagree, under one managed path."""
    live, expected = live_root / rel, expected_root / rel
    if not live.exists():
        return [f"missing entirely, run without --check: {rel}"]

    out: list[str] = []

    def walk(sub: Path) -> None:
        cmp = filecmp.dircmp(live / sub, expected / sub)
        for name in sorted(cmp.left_only):
            out.append(f"committed but not in any source:  {rel / sub / name}")
        for name in sorted(cmp.right_only):
            out.append(f"in the source but not committed:  {rel / sub / name}")
        for name in sorted(cmp.diff_files):
            out.append(f"content differs from its source:  {rel / sub / name}")
        for name in sorted(cmp.common_dirs):
            walk(sub / name)

    walk(Path("."))
    return [line.replace("/./", "/") for line in out]


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the committed copies match their sources; write nothing",
    )
    args = parser.parse_args()

    if not args.check:
        n_refs, n_vendored, n_tree = build(PLUGIN_DIR)
        print(f"synced {n_refs} corpus file(s) into references/")
        print(f"unpacked {n_vendored} file(s) from {len(VENDORED)} vendored .skill package(s)")
        print(f"mirrored {n_tree} file(s) from {len(TREES)} corpus subtree(s)")
        for rel in managed_paths():
            print(f"  managed: {rel.as_posix()}")
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        expected = Path(tmp)
        n_refs, n_vendored, n_tree = build(expected)
        diffs: list[str] = []
        for rel in managed_paths():
            diffs += differences(PLUGIN_DIR, expected, rel)

    if not diffs:
        print(f"in sync -- {n_refs} corpus file(s), {n_vendored} vendored file(s), "
              f"and {n_tree} mirrored tree file(s) match their sources")
        return 0

    print("STALE: generated content no longer matches its sources.", file=sys.stderr)
    for line in diffs:
        print(f"  {line}", file=sys.stderr)
    print(f"\n  Fix by running: python {Path(__file__).name}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
