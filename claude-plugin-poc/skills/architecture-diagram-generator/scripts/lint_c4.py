#!/usr/bin/env python3
"""
lint_c4.py — structural and C4-convention linter for Mermaid C4 diagrams.

Checks what a renderer cannot: whether the diagram obeys the C4 model. Runs with
no dependencies, no network, and no browser, which matters because mmdc needs a
Chromium download that is blocked in many sandboxes and CI images.

Usage:
    python3 lint_c4.py docs/architecture/*.mmd
    python3 lint_c4.py --strict docs/architecture/container-diagram.mmd

Exit code 0 when clean, 1 when any ERROR is found. Warnings alone exit 0.
"""

import re
import sys
from pathlib import Path

DIAGRAM_TYPES = {
    "C4Context", "C4Container", "C4Component", "C4Dynamic", "C4Deployment",
    "classDiagram", "erDiagram",
}

ELEMENT_RE = re.compile(
    r"\b(Person|Person_Ext|System|SystemDb|SystemQueue|System_Ext|SystemDb_Ext|"
    r"SystemQueue_Ext|Container|ContainerDb|ContainerQueue|Container_Ext|"
    r"ContainerDb_Ext|ContainerQueue_Ext|Component|ComponentDb|ComponentQueue|"
    r"Component_Ext|Node|Node_L|Node_R|Deployment_Node)\s*\(\s*([A-Za-z0-9_]+)\s*,(.*)$"
)
BOUNDARY_RE = re.compile(
    r"\b(Enterprise_Boundary|System_Boundary|Container_Boundary|Boundary)\s*\(\s*([A-Za-z0-9_]+)\s*,"
)
REL_RE = re.compile(
    r"\b(Rel|Rel_U|Rel_D|Rel_L|Rel_R|Rel_Up|Rel_Down|Rel_Left|Rel_Right|BiRel)\s*\((.*)$"
)

# Elements carrying a technology slot: Kind(alias, label, tech, descr)
TECH_BEARING = {
    "Container", "ContainerDb", "ContainerQueue", "Container_Ext",
    "ContainerDb_Ext", "ContainerQueue_Ext",
    "Component", "ComponentDb", "ComponentQueue", "Component_Ext",
}

VAGUE_REL_LABELS = {
    "uses", "calls", "connects", "connects to", "talks to", "communicates with",
    "interacts with", "accesses", "links to", "sends", "receives", "depends on",
    "", "-",
}

ESCAPED_QUOTE_RE = re.compile(r'\\"')
RAW_ANGLE_RE = re.compile(r"<[A-Za-z/]")

# Kinds that are boundaries/nodes rather than positioned leaf elements. Mermaid's
# C4 renderer crashes (or silently fails) when Rel() connects one of these
# directly — Rel must target a Person/System/Container/Component alias instead.
NOT_RELATABLE_KINDS = {"boundary", "Deployment_Node", "Node", "Node_L", "Node_R"}


def check_empty_boundaries(lines):
    """Flag any boundary/node whose '{' ... '}' body contains zero statements.

    Mermaid's C4 grammar rejects an empty body outright (parse error), even when
    the surrounding diagram is otherwise valid — confirmed empirically against
    mermaid-cli, since the grammar isn't documented precisely enough to infer
    this from the reference alone. A nested boundary/node with no children must
    not be given braces at all... except Deployment_Node/boundary macros always
    require braces, so the fix is to put something inside (typically a Container
    representing what that node actually hosts), not to drop the braces.
    """
    errors = []
    stack = []  # [line_no, has_content]
    is_decl_re = re.compile(
        r"^(Rel|Rel_U|Rel_D|Rel_L|Rel_R|Rel_Up|Rel_Down|Rel_Left|Rel_Right|BiRel|"
        r"UpdateElementStyle|UpdateRelStyle|UpdateLayoutConfig|Person|Person_Ext|"
        r"System|SystemDb|SystemQueue|System_Ext|SystemDb_Ext|SystemQueue_Ext|"
        r"Container|ContainerDb|ContainerQueue|Container_Ext|ContainerDb_Ext|"
        r"ContainerQueue_Ext|Component|ComponentDb|ComponentQueue|Component_Ext|"
        r"Node|Node_L|Node_R|Deployment_Node|Enterprise_Boundary|System_Boundary|"
        r"Container_Boundary|Boundary)\b"
    )
    for i, raw in enumerate(lines, 1):
        ln = raw.strip()
        if not ln or ln.startswith("%%"):
            continue
        if stack and is_decl_re.match(ln):
            stack[-1][1] = True
        for _ in range(ln.count("{")):
            stack.append([i, False])
        for _ in range(ln.count("}")):
            if stack:
                open_line, has_content = stack.pop()
                if not has_content:
                    errors.append(("ERROR", f"Line {open_line}: empty boundary/node body. "
                                            f"Mermaid's C4 grammar rejects '{{' immediately "
                                            f"followed by '}}' as a parse error — every "
                                            f"boundary or Deployment_Node needs at least one "
                                            f"statement inside it (a Container it hosts, a "
                                            f"nested node, or a Rel), not just a description."))
    return errors


def split_args(argstr):
    """Split a macro's arguments on top-level commas, respecting quotes and parens."""
    args, depth, in_q, cur = [], 0, False, ""
    for ch in argstr:
        if ch == '"':
            in_q = not in_q
            cur += ch
        elif ch == "(" and not in_q:
            depth += 1
            cur += ch
        elif ch == ")" and not in_q:
            if depth == 0:
                break
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0 and not in_q:
            args.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        args.append(cur.strip())
    return args


def lint(path, strict=False):
    errors, warnings = [], []
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()

    code = [
        ln for ln in lines
        if ln.strip() and not ln.strip().startswith(("%%", "#"))
    ]
    if not code:
        return [("ERROR", "File is empty")], []

    dtype = code[0].strip().split()[0]
    if dtype not in DIAGRAM_TYPES:
        errors.append(("ERROR", f"Line 1 must declare a diagram type, found {dtype!r}. "
                                f"There is no C4Code type — use classDiagram for Level 4."))
        return errors, warnings

    if not any(ln.strip().startswith("title ") for ln in code):
        errors.append(("ERROR", "No title. Every diagram states its scope in the title, "
                                "including which container or environment it covers."))

    for i, ln in enumerate(lines, 1):
        if ESCAPED_QUOTE_RE.search(ln):
            errors.append(("ERROR", f'Line {i}: backslash-escaped quote (\\") found. Mermaid\'s '
                                    f"C4/classDiagram grammar does not support escaping the "
                                    f"string delimiter — the label ends at the first quote and "
                                    f"the rest is parsed as syntax, breaking the diagram. Use a "
                                    f"single quote (') or rephrase without an embedded quote."))

    if dtype in ("classDiagram", "erDiagram"):
        if text.count("{") != text.count("}"):
            errors.append(("ERROR", "Unbalanced braces"))
        return errors, warnings

    if text.count("{") != text.count("}"):
        errors.append(("ERROR", f"Unbalanced braces: {text.count('{')} open, "
                                f"{text.count('}')} close"))
    else:
        errors.extend(check_empty_boundaries(lines))

    declared, rels = {}, []
    for i, raw in enumerate(lines, 1):
        ln = raw.strip()
        if not ln or ln.startswith("%%"):
            continue

        if RAW_ANGLE_RE.search(ln):
            errors.append(("ERROR", f"Line {i}: literal '<' followed by a letter found in a "
                                    f"label. Mermaid renders C4 labels through HTML/"
                                    f"foreignObject, so this is parsed as a tag and can silently "
                                    f"break or blank out the rendering. Avoid angle brackets in "
                                    f"labels — spell out placeholders instead (e.g. 'per-"
                                    f"environment' instead of '<env>')."))

        m = BOUNDARY_RE.search(ln)
        if m:
            declared[m.group(2)] = ("boundary", i)
            continue

        m = ELEMENT_RE.search(ln)
        if m:
            kind, alias, rest = m.group(1), m.group(2), m.group(3)
            declared[alias] = (kind, i)
            args = split_args(rest)
            if kind in TECH_BEARING:
                if len(args) < 2:
                    errors.append(("ERROR", f"Line {i}: {kind} {alias!r} has no technology. "
                                            f"Containers and components must name their "
                                            f"language, framework, or engine."))
                elif not args[1].strip(' "'):
                    errors.append(("ERROR", f"Line {i}: {kind} {alias!r} has an empty "
                                            f"technology field."))
            if dtype == "C4Context" and kind in TECH_BEARING:
                errors.append(("ERROR", f"Line {i}: {kind} in a C4Context diagram mixes "
                                        f"abstraction levels. L1 shows systems and people only."))
            if len(args) < 2 and kind not in TECH_BEARING:
                warnings.append(("WARN", f"Line {i}: {kind} {alias!r} has no description."))
            continue

        m = REL_RE.search(ln)
        if m:
            args = split_args(m.group(2))
            if len(args) < 3:
                errors.append(("ERROR", f"Line {i}: relationship has no label. Every arrow "
                                        f"reads as a verb phrase from source to target."))
                continue
            src, tgt, label = args[0], args[1], args[2].strip(' "')
            rels.append((src, tgt, label, len(args) >= 4 and bool(args[3].strip(' "')), i))
            continue

    for alias, (kind, line) in declared.items():
        if kind == "boundary":
            continue
        if not any(alias in (s, t) for s, t, *_ in rels):
            warnings.append(("WARN", f"Line {line}: {alias!r} has no relationships. "
                                     f"An unconnected element usually means a missing arrow "
                                     f"or an element that does not belong."))

    for src, tgt, label, has_tech, line in rels:
        for end, role in ((src, "source"), (tgt, "target")):
            if end not in declared:
                errors.append(("ERROR", f"Line {line}: relationship {role} {end!r} is not "
                                        f"declared anywhere."))
            elif declared[end][0] in NOT_RELATABLE_KINDS:
                errors.append(("ERROR", f"Line {line}: relationship {role} {end!r} is a "
                                        f"boundary/Deployment_Node, not a Person/System/"
                                        f"Container/Component. Mermaid's C4 renderer crashes "
                                        f"(or fails silently) when Rel connects a boundary "
                                        f"directly — point it at a leaf element inside that "
                                        f"boundary instead."))
        if label.lower().strip(".") in VAGUE_REL_LABELS:
            errors.append(("ERROR", f"Line {line}: label {label!r} is not a verb phrase — it "
                                    f"tells a reviewer nothing. Say what flows and which way."))
        if not has_tech and dtype in ("C4Container", "C4Component", "C4Deployment"):
            sev = "ERROR" if strict else "WARN"
            (errors if strict else warnings).append(
                (sev, f"Line {line}: relationship {src}→{tgt} has no protocol or mechanism "
                      f"(HTTPS/JSON, SQL, gRPC, AMQP).")
            )

    if dtype == "C4Container" and not any(
        k == "boundary" for k, _ in declared.values()
    ):
        warnings.append(("WARN", "No boundary. A container diagram normally wraps the system "
                                 "in scope in a System_Boundary so externals sit outside it."))

    if dtype == "C4Deployment" and not any(
        k in ("Node", "Node_L", "Node_R", "Deployment_Node") for k, _ in declared.values()
    ):
        errors.append(("ERROR", "A deployment diagram with no nodes is not a deployment "
                                "diagram. Ground the infrastructure in IaC or ask."))

    return errors, warnings


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    if not args:
        print(__doc__)
        return 2

    total_errors = 0
    for path in args:
        errors, warnings = lint(path, strict=strict)
        total_errors += len(errors)
        status = "FAIL" if errors else ("WARN" if warnings else "PASS")
        print(f"\n{status}  {path}")
        for sev, msg in errors + warnings:
            print(f"  [{sev}] {msg}")
        if not errors and not warnings:
            print("  Clean — structure and C4 conventions check out.")

    print(f"\n{'-' * 60}")
    print(f"{len(args)} file(s), {total_errors} error(s)")
    print("Note: this checks structure and C4 conventions, not that Mermaid renders it.")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
