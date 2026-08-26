# Changelog

All notable changes to the SDLC AI Governance Standards are documented in this file.

This changelog follows Keep a Changelog conventions.
Versions follow Semantic Versioning 2.0.0.

---

## [Unreleased]

### Added

- `sdlc/quality-assurance/mocking.md` (QA-007) — Mocking standards: where mocking belongs, what must never be mocked, and contract fidelity for mocked dependencies. Closes the "mocking" AC gap in the testing-standards rule domain (WS2).
- `sdlc/quality-assurance/ai-generated-test-review.md` (QA-008) — Human-review and validation requirements for AI-authored or AI-assisted tests, including a fail-first check before trusting an AI-generated test as a regression guard. Closes the "AI-generated-test review" AC gap in the testing-standards rule domain (WS2).
- `sdlc/quality-assurance/README.md` — indexed QA-007 and QA-008.
- `rules-manifest.yaml` — added QA-007 and QA-008 entries.
- `gendd-analysis/` — New GenDD-Flow analysis module with brownfield and greenfield analysis support.
- `gendd-analysis/workflows/brownfield-repository-analysis.md` — Brownfield analysis workflow for existing repositories.
- `gendd-analysis/workflows/greenfield-analysis.md` — Greenfield analysis workflow for planned/new projects.
- `gendd-analysis/agents/pass1-scan-agent.md`, `gendd-analysis/agents/pass2-infer-agent.md`, `gendd-analysis/agents/pass3-validate-hitl-agent.md`, `gendd-analysis/agents/pass4-document-agent.md`, and `gendd-analysis/agents/pass5-role-detector-agent.md` — Multi-pass analysis agents for scanning, inference, validation, documentation, and SDLC area detection.

## [2.0.0] — 2026-07-13

### Summary

This major version adopts a **section-based severity model** across the entire repository, eliminates the exception/waiver framework, and introduces automated lint validation. Every standard file has been converted and version-bumped to 2.0.0.

### Added

- `scripts/lint-standards.sh` — CI-ready bash script that validates every standard file for required frontmatter, prohibited sections, no inline RFC 2119 keywords in directive text, valid semver version field, and `last_reviewed` age.
- `governance/versioning-and-change.md` (GOV-VERSIONING) — new document governing the rule-change process that replaces the former exception/waiver path.

### Changed

**Severity model migration — all 65 standard files**

All standard files have been converted to the section-based severity model:
- Severity section headings (`## MUST`, `## MUST NOT`, `## SHOULD`, `## SHOULD NOT`, `## MAY`) now carry all obligation information.
- RFC 2119 keywords removed from directive text; directives use plain imperative voice.
- `severity:` field removed from all frontmatter.
- `## Quick Reference`, `## Agent Directives`, `## Definition of Done / Checklist`, and `## Exceptions` sections removed from all files.

**Governance meta layer**

- `AGENTS.md` — updated authority tier table, severity explanation, and agent behaviour to reflect section-based model; removed exception links; added versioning-and-change link.
- `README.md` — updated severity model description; replaced "Request an exception" navigation link with "Propose a rule change".
- `templates/standard-template.md` — rebuilt to match new section structure; removed `severity:` frontmatter field, legacy sections, and Exceptions section.
- `rules-manifest.yaml` — removed `GOV-EXCEPTIONS` entry.
- `governance/rule-authoring.md` (GOV-AUTHORING) — updated to mandate section model; added prohibited-section list; updated lint requirements and review checklist.
- `governance/enforcement.md` (GOV-ENFORCEMENT) — reworked conformance levels, escalation section, and audit section to remove exception/waiver framework.
- `governance/charter.md` (GOV-CHARTER) — RACI updated: replaced "Granting exceptions" row with "Proposing rule changes"; guiding principle #4 updated.
- `governance/glossary.md` (GOV-GLOSSARY) — replaced "Exception / Waiver" entry with "Rule change"; updated "Compensating control" definition.
- `governance/agent-guardrails.md` (GOV-GUARDRAILS) — removed exception waiver language; last guardrail updated to direct agents to the rule-change process.
- `governance/human-in-the-loop.md` (GOV-HITL) — version bumped.

### Removed

- `governance/exceptions.md` (GOV-EXCEPTIONS) — exception/waiver request process. Rules are followed as written or changed through `governance/versioning-and-change.md`.
- `governance/exception-register.md` — active and historical exceptions register.

### Migration guide

**If you have in-flight exception requests:** Convert them to rule-change proposals using the process in `governance/versioning-and-change.md`. Document the rationale and open a PR against the relevant standard file.

**If you reference `governance/exceptions.md` in tooling or documentation:** Update references to `governance/versioning-and-change.md`.

**If you consume standard files programmatically:** Update any parser that reads `severity:` frontmatter or looks for `## Quick Reference` / `## Agent Directives` / `## Exceptions` sections. Directives are now found under `## MUST`, `## MUST NOT`, `## SHOULD`, `## SHOULD NOT`, and `## MAY` headings.

---

## [1.0.0] — 2026-07-09

### Added

**Repository scaffolding**
- `README.md` — repository overview, navigation guide, rule ID scheme, and severity keyword reference.
- `AGENTS.md` — AI agent entrypoint with global non-negotiables, routing table, and layered loading protocol.
- `rules-manifest.yaml` — compact routing manifest for all standards with IDs, summaries, tags, and `applies_to` globs.
- `templates/standard-template.md` — canonical document skeleton for all standard files.
- `templates/adr-template.md` — Architecture Decision Record template.
- `templates/user-story-template.md` — User story template.
- `templates/pull-request-template.md` — Pull request description template.

**Governance meta layer**
- `governance/charter.md` (GOV-CHARTER) — purpose, scope, RACI, and guiding principles.
- `governance/rule-authoring.md` (GOV-AUTHORING) — rule ID scheme, template usage, tech overlay authoring.
- `governance/versioning-and-change.md` (GOV-VERSIONING) — semver, changelog, deprecation lifecycle.
- `governance/enforcement.md` (GOV-ENFORCEMENT) — severity tiers, enforcement layers, conformance levels.
- `governance/exceptions.md` (GOV-EXCEPTIONS) — exception request process and template.
- `governance/exception-register.md` — active and historical exceptions register.
- `governance/human-in-the-loop.md` (GOV-HITL) — autonomy levels, mandatory approval gates.
- `governance/agent-guardrails.md` (GOV-GUARDRAILS) — global agent do/never-do list.
- `governance/glossary.md` (GOV-GLOSSARY) — shared terminology.

**Product phase** (`sdlc/product/`, prefix `PRD`)
- `user-stories.md` (PRD-001) — INVEST criteria, story format, splitting.
- `acceptance-criteria.md` (PRD-002) — Given/When/Then format, testability, unhappy paths.
- `definition-of-ready.md` (PRD-003) — DoR checklist.
- `product-requirements-doc.md` (PRD-004) — PRD structure standard.
- `jira/user-stories.md` (PRD-JIRA-001) — Jira field mapping for stories.
- `jira/acceptance-criteria.md` (PRD-JIRA-002) — Jira acceptance criteria conventions.

**Architecture phase** (`sdlc/architecture/`, prefix `ARC`)
- `decision-records.md` (ARC-001) — ADR triggers, format, immutability.
- `design-documents.md` (ARC-002) — Technical design doc triggers and sections.
- `api-design.md` (ARC-003) — Versioning, backward compatibility, error model, pagination.
- `non-functional-requirements.md` (ARC-004) — NFR categories, measurable format.
- `diagramming.md` (ARC-005) — C4 model, version-controlled diagrams.
- `openapi/api-design.md` (ARC-OPENAPI-001) — OpenAPI specification quality rules.

**Development phase** (`sdlc/development/`, prefix `DEV`)
- `coding-standards.md` (DEV-001) — Naming, function size, formatting, immutability.
- `error-handling.md` (DEV-002) — Exception handling, fail-safe, no internal details to callers.
- `code-complexity.md` (DEV-003) — Cyclomatic complexity, duplication, dead code.
- `dependency-management.md` (DEV-004) — Version pinning, vulnerability scanning, licensing.
- `code-comments.md` (DEV-005) — Docstrings, no narrative comments, no orphaned TODOs.
- `definition-of-done.md` (DEV-006) — Full DoD checklist.
- `java/coding-standards.md` (DEV-JAVA-001) — Java naming, `final` fields, no raw generics.
- `java/error-handling.md` (DEV-JAVA-002) — Java exception hierarchy rules.

**Security phase** (`sdlc/security/`, prefix `SEC`)
- `authentication-authorization.md` (SEC-001) — Authn/z, least privilege, no custom crypto.
- `input-validation-output-encoding.md` (SEC-002) — Validation, parameterised queries, encoding.
- `secrets-management.md` (SEC-003) — No hardcoded secrets, vault usage, rotation, no secrets in logs.
- `data-protection.md` (SEC-004) — TLS, encryption at rest, no deprecated algorithms.
- `data-privacy.md` (SEC-005) — Privacy-by-design, data minimisation, data-subject rights.
- `threat-modeling.md` (SEC-006) — STRIDE, triggers, documented findings.
- `vulnerability-management.md` (SEC-007) — CVE scanning, patch SLAs, responsible disclosure.
- `java/input-validation-output-encoding.md` (SEC-JAVA-001) — PreparedStatement, OWASP Java Encoder.

**Database phase** (`sdlc/database/`, prefix `DAT`)
- `schema-design.md` (DAT-001) — Primary keys, foreign keys, naming conventions.
- `migrations.md` (DAT-002) — Reversibility, zero-downtime, expand-contract pattern.
- `query-standards.md` (DAT-003) — Parameterised queries, no SELECT *, indexing, N+1.
- `data-lifecycle.md` (DAT-004) — Retention, backups, restore testing.
- `pii-handling.md` (DAT-005) — PII classification, masking in non-prod, field-level encryption.
- `postgresql/schema-design.md` (DAT-POSTGRESQL-001) — BIGSERIAL/UUID, TIMESTAMPTZ, JSONB.
- `postgresql/query-standards.md` (DAT-POSTGRESQL-002) — EXPLAIN ANALYZE, partial indexes, GIN, no OFFSET.

**Quality Assurance phase** (`sdlc/quality-assurance/`, prefix `QA`)
- `test-strategy.md` (QA-001) — Test pyramid, documented strategy.
- `test-automation.md` (QA-002) — AAA, descriptive names, determinism, independence.
- `coverage.md` (QA-003) — 80% line coverage minimum, meaningful assertions.
- `test-data-management.md` (QA-004) — No production data, factory pattern, no PII in fixtures.
- `flaky-tests.md` (QA-005) — Quarantine within 24h, fix within 14 days, no permanent disable.
- `non-functional-testing.md` (QA-006) — NFR validation, performance, security, accessibility.
- `junit/test-automation.md` (QA-JUNIT-001) — JUnit 5 annotations, @DisplayName, assertThrows.

**Version Control phase** (`sdlc/version-control/`, prefix `VCS`)
- `branching-strategy.md` (VCS-001) — Short-lived branches, naming conventions, no direct push to main.
- `commit-conventions.md` (VCS-002) — Conventional Commits, atomic commits, no secrets.
- `pull-requests.md` (VCS-003) — Ticket link, description, 400-line limit.
- `code-review.md` (VCS-004) — 1-day SLA, security review, no MUST rule violation approvals.
- `github/pull-requests.md` (VCS-GITHUB-001) — Branch protection, CODEOWNERS, required status checks.

**CI/CD phase** (`sdlc/cicd/`, prefix `CICD`)
- `pipeline-standards.md` (CICD-001) — Required stages, fail fast, no deploy on failure.
- `build-reproducibility.md` (CICD-002) — Deterministic builds, artefact integrity, SBOM.
- `versioning-releases.md` (CICD-003) — Semver, git tags, changelog per release.
- `deployment-strategies.md` (CICD-004) — Rollback procedures, canary/blue-green, feature flags.
- `environments.md` (CICD-005) — Staging parity, artefact promotion, no production data in staging.
- `github-actions/pipeline-standards.md` (CICD-GHA-001) — Least-privilege permissions, pinned actions, OIDC.

**Observability phase** (`sdlc/observability/`, prefix `OBS`)
- `logging.md` (OBS-001) — Structured JSON, correlation IDs, correct levels, no PII in logs.
- `metrics.md` (OBS-002) — RED/USE, naming conventions, cardinality limits.
- `tracing.md` (OBS-003) — W3C trace context propagation, span creation, no PII in spans.
- `alerting.md` (OBS-004) — Actionable alerts, runbook links, SLO-based alerting.
- `slos.md` (OBS-005) — SLI/SLO required, user-facing metrics, error budget policy.
- `incident-management.md` (OBS-006) — Severity levels, blameless postmortems, runbook updates.
- `opentelemetry/tracing.md` (OBS-OTEL-001) — TracerProvider init, auto-instrumentation, semantic conventions.
- `opentelemetry/metrics.md` (OBS-OTEL-002) — MeterProvider, instrument selection, OTLP exporter.

**Infrastructure phase** (`sdlc/infrastructure/`, prefix `INF`)
- `infrastructure-as-code.md` (INF-001) — IaC required, version-controlled, modular, CI-only apply.
- `configuration-management.md` (INF-002) — Config/code separation, no secrets in config, startup validation.
- `immutability.md` (INF-003) — Replace not modify, no direct production changes.
- `resource-tagging.md` (INF-004) — Mandatory tags, naming convention, policy enforcement.
- `terraform/infrastructure-as-code.md` (INF-TERRAFORM-001) — Remote state, separate state per env, version pinning.

**Documentation phase** (`sdlc/documentation/`, prefix `DOC`)
- `code-documentation.md` (DOC-001) — Public interface docstrings, ADR references.
- `api-documentation.md` (DOC-002) — Complete endpoint docs, examples, contract-driven generation.
- `repository-documentation.md` (DOC-003) — README required sections, CONTRIBUTING.md.
- `changelog.md` (DOC-004) — Keep a Changelog format, [Unreleased] section, no internal entries.
- `knowledge-retention.md` (DOC-005) — Decision capture, runbook post-incident updates, bus factor.
- `docusaurus/api-documentation.md` (DOC-DOCUSAURUS-001) — OpenAPI plugin, versioning, sidebar structure.
