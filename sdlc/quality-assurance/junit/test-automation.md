---
id: QA-JUNIT-001
title: Test Automation Standards — JUnit
phase: quality-assurance
extends: sdlc/quality-assurance/test-automation.md
tech: junit
summary: Extends QA-002 with JUnit 5 annotation and test structure rules.
tags: [qa, test-automation, junit, java, annotations, parameterized]
applies_to: ["**/*Test.java", "**/*Tests.java", "**/test/**/*.java"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Test Automation Standards — JUnit (QA-JUNIT-001)

> This overlay extends [`sdlc/quality-assurance/test-automation.md`](../test-automation.md). All directives in QA-002 remain in full effect. Only JUnit 5-specific directives appear here.

## Purpose

JUnit 4 and JUnit 5 annotations are incompatible and mixing them causes tests to be silently ignored. JUnit 5 provides purpose-built APIs for parameterisation, display names, and exception assertions.

---

## MUST

- **QA-JUNIT-001-01** All new tests use JUnit 5 annotations (`org.junit.jupiter.api.*`). JUnit 4 imports (`org.junit.Test`, `org.junit.Before`, `org.junit.runner.*`) are not used in new test classes.
- **QA-JUNIT-001-02** Every test class has a `@DisplayName` annotation with a human-readable description of the class under test. Every test method has a `@DisplayName` annotation describing the scenario and expected outcome in plain English.
- **QA-JUNIT-001-03** Exception-expected scenarios use `assertThrows` to capture the thrown exception and assert its message or properties. `@Test(expected = ...)` (JUnit 4) and try/catch with `fail()` are not used in new tests.

## SHOULD

- **QA-JUNIT-001-04** When the same test logic applies to multiple input values, `@ParameterizedTest` with `@ValueSource`, `@CsvSource`, `@MethodSource`, or `@EnumSource` is used instead of duplicating the test method.
- **QA-JUNIT-001-05** `@BeforeEach` is used for mutable test dependencies (mocks, service instances) to reinitialise before every test. `@BeforeAll` is used only for truly immutable or read-only shared resources.
