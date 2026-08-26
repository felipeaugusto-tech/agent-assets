---
id: DEV-JAVA-001
title: Coding Standards — Java
phase: development
extends: sdlc/development/coding-standards.md
tech: java
summary: Extends DEV-001 with Java-specific naming, formatting, and structure rules.
tags: [development, coding, java, naming, formatting, conventions]
applies_to: ["**/*.java"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Coding Standards — Java (DEV-JAVA-001)

> This overlay extends [`sdlc/development/coding-standards.md`](../coding-standards.md). All directives in DEV-001 remain in full effect. Only Java-specific directives appear here.

## Purpose

Java has well-established naming and structural conventions expected by all tooling, IDEs, and developers in the ecosystem. Deviating from them increases friction and reduces readability.

---

## MUST

- **DEV-JAVA-001-01** Classes, interfaces, enums, and annotations use `PascalCase` (e.g. `UserAccountService`).
- **DEV-JAVA-001-02** Methods, fields, local variables, and parameters use `camelCase` (e.g. `findActiveUsers()`, `userId`).
- **DEV-JAVA-001-03** Constants (`static final`) use `UPPER_SNAKE_CASE` (e.g. `MAX_RETRY_COUNT`).
- **DEV-JAVA-001-04** Packages use all-lowercase with no underscores (e.g. `com.example.userservice`).
- **DEV-JAVA-001-05** Test classes are suffixed with `Test` or `Tests` (e.g. `UserServiceTest`).
- **DEV-JAVA-001-06** Fields that are not reassigned after construction are declared `final`.

## MUST NOT

- **DEV-JAVA-001-07** Use raw generic types — always provide type parameters (e.g. `List<String>`, not `List`).
- **DEV-JAVA-001-08** Use field injection (`@Autowired` on a field) in new code.

## SHOULD

- **DEV-JAVA-001-09** Dependencies are injected via constructor rather than setter injection.
- **DEV-JAVA-001-10** Methods that may return a value or nothing return `Optional<T>` instead of a nullable `T`.

## SHOULD NOT

- **DEV-JAVA-001-11** Use `Optional` as a field type or method parameter.
