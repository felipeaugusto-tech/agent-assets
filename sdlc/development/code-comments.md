---
id: DEV-005
title: Code Comment Standards
phase: development
extends: null
tech: null
summary: Rules for when and how to write comments and documentation strings.
tags: [development, comments, docstrings, documentation, self-documenting]
applies_to: ["**/*.{js,ts,jsx,tsx,py,java,go,rb,cs,cpp,c,rs,kt,swift,php}"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Code Comment Standards (DEV-005)

## Purpose

Good comments explain *why* code exists, not *what* it does. Over-commenting and narrative comments produce noise that obscures the code; under-commenting public APIs makes integration harder.

---

## MUST

- **DEV-005-01** All public functions, methods, classes, and exported types have a documentation comment (docstring, JSDoc, JavaDoc, or equivalent) describing: what the function/type does (one sentence), each parameter (name, type if not inferred, and purpose), the return value, and any exceptions or error conditions callers should handle.

## MUST NOT

- **DEV-005-02** Write comments that restate what the code does (e.g. `# Increment the counter` above `count += 1`). Comments explain *why*, not *what*.
- **DEV-005-03** Commit `TODO` or `FIXME` comments without a reference to a tracked issue or ticket (format: `// TODO(PROJ-1234): description`).

## SHOULD

- **DEV-005-04** Comments explain: why a non-obvious algorithm was chosen, why an apparently incorrect-looking value is intentional, why a workaround exists (with a link to the issue), or business rules not obvious from the domain model.
- **DEV-005-05** Before adding an explanatory comment, consider whether the code can be made self-documenting by extracting a well-named function, using a named constant instead of a magic value, or renaming a variable to reveal its purpose.
