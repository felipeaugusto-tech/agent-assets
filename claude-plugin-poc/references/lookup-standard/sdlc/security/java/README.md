# Security Phase — Java Overlay

**Tech:** Java
**Rule-ID prefix:** `SEC-JAVA`
**Applies to:** `**/*.java`
**Extends:** [`sdlc/security/`](../README.md)

## Purpose

This overlay extends the agnostic security standards with rules specific to Java applications. It covers Java-specific injection prevention patterns, encoding libraries, and secure-coding practices.

## Files in this overlay

| File | Rule IDs | Summary |
|---|---|---|
| [`input-validation-output-encoding.md`](input-validation-output-encoding.md) | SEC-JAVA-001 | Java-specific injection prevention and encoding rules |

## How to use

Read `sdlc/security/input-validation-output-encoding.md` first (agnostic rules), then read this file for Java-specific rules.
