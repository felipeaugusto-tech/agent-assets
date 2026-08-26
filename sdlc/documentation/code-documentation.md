---
id: DOC-001
title: Code Documentation Standards
phase: documentation
extends: null
tech: null
summary: Rules for inline docs, docstrings, and writing self-documenting code.
tags: [documentation, docstrings, inline-docs, code, self-documenting]
applies_to: ["**/*.{js,ts,jsx,tsx,py,java,go,rb,cs,cpp,c,rs,kt,swift,php}"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Code Documentation Standards (DOC-001)

## Purpose

Public interfaces are consumed by people who may not have access to the implementation context. These standards ensure code is self-describing at the documentation level — covering public APIs, modules, and non-obvious decisions.

See [`sdlc/development/code-comments.md`](../development/code-comments.md) for inline comment standards.

---

## MUST

- **DOC-001-01** All public functions, methods, classes, and exported types have documentation comments describing purpose, parameters, return values, and exceptions/errors.

## MUST NOT

- **DOC-001-02** Write comments that restate what the code does — comments explain *why*, not *what*.

## SHOULD

- **DOC-001-03** Each module or package has a top-level documentation comment describing its purpose, responsibilities, and key abstractions, using the language's conventional mechanism (e.g. Python `__init__.py` docstring, Go package doc comment, Java `package-info.java`).
- **DOC-001-04** Code that implements a decision documented in an ADR includes a reference to that ADR near the relevant code (e.g. `// See docs/adr/ADR-NNN-title.md`).

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| Java | [`../development/java/coding-standards.md`](../development/java/coding-standards.md) | `**/*.java` |
