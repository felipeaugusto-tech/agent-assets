---
id: DEV-JAVA-002
title: Error Handling Standards — Java
phase: development
extends: sdlc/development/error-handling.md
tech: java
summary: Extends DEV-002 with Java exception hierarchy and handling rules.
tags: [development, error-handling, java, exceptions, checked, unchecked]
applies_to: ["**/*.java"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Error Handling Standards — Java (DEV-JAVA-002)

> This overlay extends [`sdlc/development/error-handling.md`](../error-handling.md). All directives in DEV-002 remain in full effect. Only Java-specific directives appear here.

## Purpose

Java's exception hierarchy (checked vs unchecked) requires explicit conventions to prevent catch-all blocks, lost causes, and generic JDK exceptions leaking through domain boundaries.

---

## MUST NOT

- **DEV-JAVA-002-01** Use `catch (Exception e)`, `catch (Throwable t)`, or `catch (Error e)` except at system boundaries (top-level HTTP handlers, scheduled job entry points) where the full stack trace is explicitly logged.
- **DEV-JAVA-002-02** Wrap a caught exception without including it as the `cause` argument. Correct: `throw new ServiceException("Failed to load user", e)`. Incorrect: `throw new ServiceException("Failed to load user")` inside a catch block that has `e`.

## SHOULD

- **DEV-JAVA-002-03** Use unchecked exceptions (`RuntimeException` subclasses) for programming errors (invalid arguments, contract violations) that callers cannot reasonably recover from. Use checked exceptions only for recoverable conditions where the caller is expected to handle the specific failure mode.
- **DEV-JAVA-002-04** Projects define a base exception class (e.g. `ApplicationException`) with a hierarchy of domain-specific subclasses, rather than throwing generic JDK exceptions (e.g. `IllegalArgumentException`, `IllegalStateException`) from domain or service layers.
