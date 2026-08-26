---
id: DEV-001
title: Coding Standards
phase: development
extends: null
tech: null
summary: Rules for naming, formatting, structure, function size, and immutability in application code.
tags: [development, coding, naming, formatting, structure, function-size, immutability]
applies_to: ["**/*.{js,ts,jsx,tsx,py,java,go,rb,cs,cpp,c,rs,kt,swift,php}"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Coding Standards (DEV-001)

## Purpose

Consistent code style reduces cognitive load during review, speeds up onboarding, and prevents a class of bugs caused by unclear naming and oversized functions.

## Scope

Applies to all production, test, and configuration code written in any programming language. Technology-specific rules are in the relevant tech overlay.

---

## MUST

- **DEV-001-01** Names describe purpose or content, not type or implementation (e.g. `userEmail` not `string1`, `findActiveAccounts` not `doQuery`).
- **DEV-001-02** Names are pronounceable, searchable, and consistent with the domain's ubiquitous language.
- **DEV-001-03** Functions and methods do one thing and are no longer than 50 lines (blank lines and comment lines excluded).
- **DEV-001-04** Functions and methods accept no more than five parameters.
- **DEV-001-05** Every project has a formatter or linter configuration committed to the repository that enforces consistent formatting, applied automatically via pre-commit hook or CI check.

## MUST NOT

- **DEV-001-06** Use single-letter identifiers except for short-lived loop indices (`i`, `j`) or established mathematical conventions.
- **DEV-001-07** Use abbreviations that are not universally understood within the team's domain.
- **DEV-001-08** Use misleading names (e.g. a collection named `userList` that returns a map).
- **DEV-001-09** Use unnamed literal numeric or string constants in logic — all domain constants are declared as named constants. Exception: `0`, `1`, `-1`, `true`, `false`, and empty string `""` when their meaning is unambiguous in context.
- **DEV-001-10** Merge code that fails the project's formatter check.

## SHOULD

- **DEV-001-11** Functions with more than five parameters use a parameter object instead.
- **DEV-001-12** Variables and data structures are immutable by default — prefer `const` / `final` / `val` over mutable equivalents where the language supports it.
- **DEV-001-13** Functions avoid mutating their arguments and return new values instead.
- **DEV-001-14** Files are organised by domain concept rather than technical layer.
- **DEV-001-15** A single file contains no more than one public type (class, interface, or equivalent).
- **DEV-001-16** Import and dependency ordering is consistent and enforced by the project's linter.

---

## Tech-Specific Standards

| Technology | Overlay file | Applies to |
|---|---|---|
| Java | [`java/coding-standards.md`](java/coding-standards.md) | `**/*.java` |
