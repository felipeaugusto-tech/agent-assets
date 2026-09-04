---
id: ARC-005
title: Diagramming Standards
phase: architecture
extends: null
tech: null
summary: Conventions for architecture diagrams including C4 model and source-control requirements.
tags: [architecture, diagrams, c4, documentation, version-control]
applies_to: ["**/*.puml", "**/*.mermaid", "**/*.drawio", "**/diagrams/**"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Diagramming Standards (ARC-005)

## Purpose

Diagrams that exist only in slide decks or wiki pages become stale and disconnected from the codebase. Version-controlled, text-based diagrams can be reviewed alongside code changes, diffed over time, and kept current.

---

## MUST

- **ARC-005-01** Architecture diagrams are stored as source files in the repository under `docs/diagrams/`. Exported image files may be co-located for convenience but are not the only representation.
- **ARC-005-02** System-level architecture diagrams use the C4 model levels: Level 1 (Context — system and external relationships), Level 2 (Container — services, databases, queues), Level 3 (Component — within a container, only for complex containers), Level 4 (Code — only when other levels are insufficient). Each diagram includes a title indicating its C4 level.

## MUST NOT

- **ARC-005-03** Reference diagrams that exist only in external tools not linked from the repository.

## SHOULD

- **ARC-005-04** Diagrams use a text-based format (PlantUML `.puml` or Mermaid `.mermaid`) to enable meaningful diffs in pull requests.
- **ARC-005-05** When a PR changes the architecture of a system, the relevant diagrams are updated in the same PR.
