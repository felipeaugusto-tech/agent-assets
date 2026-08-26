---
id: SEC-JAVA-001
title: Input Validation and Output Encoding Standards — Java
phase: security
extends: sdlc/security/input-validation-output-encoding.md
tech: java
summary: Extends SEC-002 with Java-specific injection prevention and encoding rules.
tags: [security, input-validation, java, injection, owasp-java-encoder, spring]
applies_to: ["**/*.java"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Input Validation and Output Encoding Standards — Java (SEC-JAVA-001)

> This overlay extends [`sdlc/security/input-validation-output-encoding.md`](../input-validation-output-encoding.md). All directives in SEC-002 remain in full effect. Only Java-specific directives appear here.

## Purpose

Java has specific APIs for parameterised queries, HTML encoding, and OS command execution that require explicit conventions to prevent injection vulnerabilities.

---

## MUST

- **SEC-JAVA-001-01** All database queries use one of: `PreparedStatement` with `?` placeholders; JPA `@Query` with named parameters (`:paramName`); Spring Data query method conventions; or JPQL/HQL named parameter syntax. `Statement.execute(string)`, `Statement.executeQuery(string)`, and `createNativeQuery(string)` with concatenated user input are never used.
- **SEC-JAVA-001-02** Untrusted data rendered in HTML templates (JSP, Thymeleaf, Freemarker, or plain string output) uses `Encode.forHtml()`, `Encode.forJavaScript()`, or the appropriate context method from the OWASP Java Encoder library (`org.owasp.encoder:encoder`). `th:utext` (Thymeleaf unescaped text) is not used with untrusted input.

## MUST NOT

- **SEC-JAVA-001-03** Use `Runtime.exec(String command)` with any user-supplied data. Use `ProcessBuilder` with a `List<String>` of pre-validated arguments if OS command execution with dynamic arguments is unavoidable.

## SHOULD

- **SEC-JAVA-001-04** Request DTOs use Bean Validation annotations (`@NotNull`, `@Size`, `@Pattern`, `@Email`, `@Valid`) to declare constraints. Spring controller methods include `@Valid` or `@Validated` on request body parameters to trigger validation before handler methods are invoked.
