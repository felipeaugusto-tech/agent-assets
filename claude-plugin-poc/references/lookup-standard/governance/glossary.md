---
id: GOV-GLOSSARY
title: Shared Glossary
phase: governance
summary: Definitions of terms used across all standards in this repository.
tags: [governance, glossary, terminology]
applies_to: ["**/*"]
tech: null
extends: null
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Shared Glossary

This glossary defines terms used across the standards in this repository. When a term is defined here, all standards MUST use it with this meaning and MUST NOT redefine it locally. Standards MAY add narrower, context-specific definitions that build on a glossary term, provided they do not contradict it.

---

| Term | Definition |
|---|---|
| **Acceptance Criteria** | A set of conditions that a deliverable must satisfy for it to be accepted by the stakeholder. In this repository, acceptance criteria MUST be written in Given/When/Then format and must be independently testable. |
| **Agent** / **AI Agent** | An autonomous or semi-autonomous AI system that can read, generate, modify, and execute code and configuration within a software project. |
| **Agnostic standard** | A rule or standard that applies regardless of the programming language, framework, or platform in use. The primary standard files in each SDLC phase are agnostic. |
| **Artifact** | Any output produced during the SDLC, including code, binaries, container images, configuration files, documentation, and test reports. |
| **Autonomy level** | A classification (A1 Autonomous, A2 Human-in-review, A3 Human-initiated) describing how much independent action an agent may take before requiring human involvement. See [`human-in-the-loop.md`](human-in-the-loop.md). |
| **Backward compatibility** | The property of a change that allows existing consumers of an interface (API, library, protocol) to continue working without modification. |
| **Canary deployment** | A deployment strategy where a new version is released to a small subset of users or traffic before a full rollout, allowing early detection of issues. |
| **Cardinality** (metrics) | The number of unique label/dimension combinations for a metric. High cardinality metrics consume disproportionate storage and query resources. |
| **CI/CD** | Continuous Integration / Continuous Delivery (or Deployment). The practice of automating the build, test, and release pipeline so that changes can be delivered frequently and reliably. |
| **Compensating control** | A security or process measure that reduces risk when the ideal primary control cannot be applied in a specific context. Compensating controls are documented as part of the rule-change or escalation process. |
| **Conventional Commits** | A commit message convention that uses a structured prefix (e.g. `feat:`, `fix:`, `chore:`) to make commit history machine-readable and human-navigable. |
| **Cyclomatic complexity** | A metric for the number of linearly independent paths through a piece of code. High cyclomatic complexity correlates with defect rates and reduced maintainability. |
| **Definition of Done (DoD)** | A shared checklist that must be satisfied before a piece of work is considered complete and ready to ship. |
| **Definition of Ready (DoR)** | A shared checklist that a backlog item must satisfy before it can be picked up for development. |
| **Deprecation** | The process of marking a rule or standard as no longer recommended for use, with a grace period before it is removed. |
| **Drift** | A state where the actual configuration of a system diverges from its declared-in-code configuration, typically because manual changes were made outside the IaC toolchain. |
| **Error budget** | The permitted amount of unavailability or unreliability for a service over a given period, calculated as `1 - SLO target`. When the error budget is exhausted, new feature work is paused in favour of reliability work. |
| **Rule change** | The formal process for modifying or removing a rule in this repository. Rules are followed as written or changed through the versioning process described in [`versioning-and-change.md`](versioning-and-change.md). No informal deviations or waivers are permitted. |
| **Fail-safe** | A design principle where a system defaults to a safe, restrictive state when it encounters an unexpected error, rather than failing open. |
| **Feature flag** | A runtime configuration mechanism that enables or disables a feature without a code deployment, used for canary releases, A/B testing, and controlled rollouts. |
| **Frontmatter** | Structured YAML metadata at the top of a Markdown file, delimited by `---`, used in this repository to enable routing and selection of rules without reading the full document. |
| **Given/When/Then** | A structured format for writing acceptance criteria. *Given* describes the initial state; *When* describes the action; *Then* describes the expected outcome. |
| **Human-in-the-loop** | A requirement that a human must review, approve, or trigger an action before or during its execution by an agent. |
| **IaC** | Infrastructure as Code. The practice of defining and managing infrastructure (servers, networks, databases, etc.) through machine-readable configuration files rather than manual processes. |
| **Idempotent** | An operation that produces the same result regardless of how many times it is applied. Database migrations and API operations SHOULD be idempotent. |
| **INVEST** | A mnemonic for the criteria a well-formed user story should meet: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable. |
| **Least privilege** | The principle that a user, process, or system component should have access to only the minimum resources and permissions required to perform its function. |
| **Migration** | A versioned, executable change to a database schema or data set. In this repository, migrations MUST be reversible and backward-compatible. |
| **N+1 query** | A performance anti-pattern where loading a list of N records triggers N additional individual queries, instead of one batched query. |
| **NFR** | Non-Functional Requirement. A requirement that specifies how a system performs a function (e.g. response time, availability, security level), rather than what functions it performs. |
| **Parameterised query** | A database query that uses placeholders for user-supplied values, preventing SQL injection by separating the query structure from its data. |
| **PII** | Personally Identifiable Information. Any data that can be used to identify a natural person, either directly (name, email) or indirectly in combination with other data. |
| **Postmortem** | A blameless, structured review conducted after an incident to identify root causes, contributing factors, and preventive actions. |
| **PRD** | Product Requirements Document. A document that describes the problem to be solved, the target users, the goals, success metrics, and scope of a product or feature. |
| **Provenance** | The documented origin and chain of custody of a software artifact, including its source, build inputs, and build process. |
| **RFC 2119** | An IETF standard defining the meaning of keywords such as MUST, SHOULD, and MAY in specification documents. This repository uses RFC 2119 terminology for all rule severity levels. |
| **RED method** | A metrics framework for services: **R**ate (requests per second), **E**rrors (error rate), **D**uration (latency). |
| **Rule ID** | A stable, unique identifier for a rule in this repository, of the form `PREFIX-NNN` or `PREFIX-TECH-NNN`. Rule IDs are never reused. |
| **SBOM** | Software Bill of Materials. A formal, machine-readable inventory of all components, libraries, and dependencies in a software product, used for supply-chain security and licence compliance. |
| **SDLC** | Software Development Lifecycle. The end-to-end process of planning, creating, testing, deploying, and maintaining software. |
| **SLI** | Service Level Indicator. A quantitative measure of a service's performance (e.g. request success rate). |
| **SLO** | Service Level Objective. A target value for an SLI (e.g. 99.9% success rate over 30 days). SLOs drive the error budget. |
| **Secrets** | Any value that provides access to a protected resource and must not be disclosed: passwords, API keys, tokens, private keys, certificates, connection strings. |
| **Semver** | Semantic Versioning. A versioning scheme using `MAJOR.MINOR.PATCH` where MAJOR indicates breaking changes, MINOR indicates new backward-compatible features, and PATCH indicates backward-compatible bug fixes. |
| **Tech overlay** | A technology-specific subfolder under an SDLC phase that extends the agnostic standard with rules specific to a language, framework, or tool. |
| **Threat model** | A structured analysis of a system to identify potential threats, their likelihood, impact, and mitigations. |
| **Trunk-based development** | A branching strategy where all developers commit frequently to a single main branch, with short-lived feature branches. |
| **USE method** | A metrics framework for resources: **U**tilisation, **S**aturation, **E**rrors. |
| **Zero-downtime migration** | A database migration designed to be applied without taking the application offline, typically by making changes backward-compatible before removing the old schema. |
