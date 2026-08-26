---
id: GOV-AUTHORING
title: Rule Authoring Guidelines
phase: governance
summary: How to write, ID, structure, and maintain rules and standards in this repository.
tags: [governance, authoring, rule-ids, template, severity]
applies_to: ["**/*"]
tech: null
extends: null
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Rule Authoring Guidelines

## Purpose

This document defines how to create, update, and retire standards in this repository so that all rules are consistent, traceable, and maintainable.

---

## When to write a new standard

Write a new standard when:

- A recurring class of engineering mistake has no existing rule.
- A new SDLC phase, technology overlay, or regulatory requirement needs coverage.
- An existing rule has grown too large and needs splitting by topic.

Do not write a new standard when:

- An existing rule can be extended with a new tech overlay.
- An existing rule already covers the case and only needs a clarification.

---

## File naming

| Type | Pattern | Example |
|---|---|---|
| Agnostic phase standard | `sdlc/<phase>/<topic>.md` | `sdlc/development/coding-standards.md` |
| Phase index | `sdlc/<phase>/README.md` | `sdlc/development/README.md` |
| Tech overlay standard | `sdlc/<phase>/<tech>/<topic>.md` | `sdlc/development/java/coding-standards.md` |
| Tech overlay index | `sdlc/<phase>/<tech>/README.md` | `sdlc/development/java/README.md` |
| Governance meta doc | `governance/<topic>.md` | `governance/enforcement.md` |

Use lowercase kebab-case for all filenames. No spaces, no uppercase.

---

## Rule ID scheme

### Agnostic rules

```
<PREFIX>-<NNN>
```

- `PREFIX` is the two-to-four character phase prefix defined in [`README.md`](../README.md).
- `NNN` is a zero-padded three-digit sequence number starting at `001`.
- IDs are assigned sequentially and are **never reused**, even after deprecation.

### Tech overlay rules

```
<PREFIX>-<TECH>-<NNN>
```

- `TECH` is an uppercase abbreviation of the technology name, e.g. `JAVA`, `POSTGRESQL`, `GHA`.
- Numbering restarts at `001` within each technology namespace.

### Directive IDs within a file

Each individual directive inside a standard file carries an extended ID that includes a suffix:

```
<RULE-ID>-<NN>
```

Example: `DEV-001-02` is the second directive in the DEV-001 standard. These IDs are stable and never reused.

---

## Required frontmatter fields

Every standard file MUST include YAML frontmatter with these fields:

| Field | Description |
|---|---|
| `id` | Stable rule-set ID, e.g. `DEV-001` |
| `title` | Short, human-readable title |
| `phase` | SDLC phase name |
| `extends` | For tech overlays: path to the agnostic file being extended. `null` otherwise. |
| `tech` | Technology name for overlays. `null` for agnostic standards. |
| `summary` | One sentence describing what this standard governs |
| `tags` | List of topic tags for routing |
| `applies_to` | Glob pattern(s) for file types this rule governs |
| `version` | Semantic version of this document |
| `last_reviewed` | ISO date of last review |

The `severity` field is not used. Severity is expressed by section structure, not frontmatter.

---

## Standard file structure

Every standard file MUST use [`templates/standard-template.md`](../templates/standard-template.md) as its skeleton.

### Required sections (in order)

1. **Frontmatter** — YAML metadata block as above.
2. **Title** — matches the `title` frontmatter field.
3. **Purpose** — 1–2 sentences on why this standard exists.
4. **Scope** — what files, roles, and environments this covers. State explicit exclusions. (Omit only if fully covered by Purpose.)
5. **Directive sections** — one or more of `## MUST`, `## MUST NOT`, `## SHOULD`, `## SHOULD NOT`, `## MAY`. Include only the sections that have directives; omit empty sections.
6. **Tech-Specific Standards** — table of overlays (agnostic files only; omit from overlays).
7. **References** — external links (omit if none).

### Prohibited sections

Do not include `## Quick Reference`, `## Agent Directives`, `## Definition of Done / Checklist`, `## Exceptions`, or per-rule `**Severity:**` blocks. These are legacy structures superseded by the section model.

---

## How to write directives

Each directive is a single bullet under the appropriate severity section:

```markdown
## MUST
- **DEV-001-02** A function does one thing and is no longer than 50 lines.

## MUST NOT
- **DEV-001-05** Use unnamed magic numbers or strings in logic.

## SHOULD
- **DEV-001-07** Prefer immutable data structures unless mutation is explicitly required.
```

Rules for directive text:

- Write in plain imperative voice.
- Do NOT include RFC 2119 keywords (MUST, SHOULD, MAY, etc.) inside the directive text. The section heading carries the severity.
- Be specific and actionable. Avoid vague language like "consider", "be careful", or "try to".
- One directive = one statement. If two separate requirements have different severities, they are two separate directives with two separate IDs.

---

## Severity section usage

| Section | Use when |
|---|---|
| `## MUST` | The behaviour is an absolute requirement, followed as written. |
| `## MUST NOT` | The behaviour is an absolute prohibition, followed as written. |
| `## SHOULD` | The behaviour is the strong default. Deviation is allowed with documented justification. |
| `## SHOULD NOT` | The behaviour is strongly discouraged. Including it requires documented justification. |
| `## MAY` | The behaviour is optional. Include when it genuinely helps to state the option. |

When in doubt between MUST and SHOULD: if a violation would always be a defect or a security/compliance risk, use MUST. If a violation might sometimes be intentional and reasonable, use SHOULD.

---

## Tech overlay authoring

When adding a technology-specific overlay:

1. Create the directory `sdlc/<phase>/<tech>/`.
2. Write a `README.md` index stating the overlay's scope.
3. Create one file per agnostic topic being extended — using the same filename as the agnostic file.
4. Frontmatter MUST include `extends: sdlc/<phase>/<topic>.md` and `tech: <name>`.
5. Write only directives that are **additive** (new rules for this tech) or **tightening** (raising a SHOULD to a MUST for this tech). Never repeat agnostic directives verbatim.
6. An overlay MUST NOT weaken or remove a directive from the agnostic file it extends. If an overlay needs to do this, raise a rule-change proposal on the agnostic file instead.
7. Use namespaced rule IDs: `<PREFIX>-<TECH>-<NNN>`.
8. Add a manifest entry for each new file.
9. Add a link to the overlay in the parent phase `README.md`.

---

## Deprecating a rule

To deprecate a standard:

1. Add `deprecated: true`, `deprecated_date`, and `superseded_by` (if applicable) to frontmatter.
2. Add a deprecation notice at the top of the document body pointing to the replacement.
3. Update `rules-manifest.yaml` to mark the entry as deprecated.
4. Do not delete the file or reuse the rule ID.
5. Record a changelog entry in `CHANGELOG.md`.

---

## Lint requirements

A CI check enforces the following on every standard file:

- No RFC 2119 keyword token (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) appears inside a directive statement (only permitted in section headings).
- No `severity:` field appears in frontmatter.
- Section headings are limited to the allowed set (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`, `Purpose`, `Scope`, `Tech-Specific Standards`, `References`).

---

## Review checklist

Before a new or updated standard can be merged:

- [ ] Frontmatter is complete with all required fields. No `severity:` field present.
- [ ] File follows the required section structure from the template.
- [ ] All directives have stable IDs in the `<PREFIX>-<NNN>-<NN>` format.
- [ ] Directive text uses plain imperative voice with no RFC 2119 keywords.
- [ ] All directives are placed under the correct severity section.
- [ ] No Quick Reference, Agent Directives, Definition of Done, or Exceptions sections present.
- [ ] A `rules-manifest.yaml` entry exists for the file.
- [ ] No directive duplicates or weakens an existing directive from a higher-authority file.
- [ ] At least one Tech Lead or Governance Owner has approved the PR.

---

## Rules-manifest update requirement

Every new or renamed standard file MUST have a corresponding entry in [`rules-manifest.yaml`](../rules-manifest.yaml). The entry MUST include accurate `applies_to` globs, `tags`, and `summary`. A pull request adding a new standard without a manifest entry MUST NOT be merged.
