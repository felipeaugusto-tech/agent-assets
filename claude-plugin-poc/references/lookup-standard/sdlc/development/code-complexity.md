---
id: DEV-003
title: Code Complexity Standards
phase: development
extends: null
tech: null
summary: Limits on cyclomatic complexity, duplication, and rules for dead-code removal.
tags: [development, complexity, cyclomatic-complexity, duplication, dead-code, maintainability]
applies_to: ["**/*.{js,ts,jsx,tsx,py,java,go,rb,cs,cpp,c,rs,kt,swift,php}"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Code Complexity Standards (DEV-003)

## Purpose

High-complexity code has more defects, is harder to test, and is more expensive to change. These standards provide measurable targets that keep code maintainable over its lifetime.

---

## MUST

- **DEV-003-01** The cyclomatic complexity of any single function or method does not exceed 10. Functions exceeding this limit are refactored before the PR is merged, using: guard clauses (early returns) to eliminate nesting, extraction of sub-functions for distinct logical steps, or replacement of complex conditionals with polymorphism or a strategy pattern.
- **DEV-003-02** Commented-out code is not committed. Code that is no longer needed is deleted. If the code may be needed in the future, a ticket is created to track that work.
- **DEV-003-03** Dead code is removed before merging: unreachable code blocks, unused private functions or methods, unused variables or imports, and unused feature flags that have been fully rolled out.

## SHOULD

- **DEV-003-04** Code duplication is kept below 3% of the codebase as measured by the project's configured duplication checker. A block of three or more lines duplicated two or more times is extracted into a shared function or module.
- **DEV-003-05** Code is not nested more than three levels deep. Guard clauses, function extraction, and async/await flattening are used to reduce nesting.
