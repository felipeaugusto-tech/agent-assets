# LikeC4 Reference

Verified against likec4.dev (docs current as of LikeC4 1.59.x). LikeC4 is
architecture-as-code: one model, many views, validated.

Contents:
1. Why it is the recommended path
2. Project layout and file extensions
3. `specification` — declaring element kinds
4. `model` — elements and relationships
5. `views` — projecting C4 levels
6. `deployment` — the physical layer
7. CLI commands that matter here
8. Mapping C4 levels onto views
9. Getting Mermaid out anyway

---

## 1. Why it is the recommended path

Not aesthetics — three concrete properties that address the failure modes of
hand-written diagram files:

- **One model, many views.** Elements and relationships are declared once; each
  diagram is a projection. Levels therefore cannot contradict each other, which is
  the standard fate of five separately maintained `.mmd` files.
- **Real validation.** `likec4 validate` fails on syntax errors and broken
  references. In Mermaid, an arrow pointing at a misspelled alias renders happily
  as a new empty box — the diagram looks fine and is wrong.
- **Nothing is forfeited.** `likec4 gen mermaid` emits Mermaid from the model, so
  choosing LikeC4 still yields Mermaid for a README or Confluence page.

Additional practical wins: interactive drill-down navigation, a first-class
deployment layer with `instanceOf`, `.c4` files that diff well in review, and an
MCP server for exposing the model to AI tooling.

The cost is honest: a new DSL for the team to learn, and a dependency. When the
team says no, the Mermaid path is fully supported — say so once and move on.

---

## 2. Project layout and file extensions

Sources use `.c4` or `.likec4`. **All source files merge into a single model**, so
they can be split however suits the repo:

```
docs/architecture/
├── specs.c4         # element and relationship kinds
├── model.c4         # elements, hierarchy, relationships
├── deployment.c4    # deployment nodes and instances
└── views.c4         # the views (C4 levels)
```

Every file holds at least one top-level block: `specification`, `model`, `views`,
`global`, or `deployment`. Multiple blocks of the same type are allowed.

---

## 3. `specification` — declaring element kinds

Kinds must be declared before use. Declare only what the model needs; do not copy
a generic taxonomy.

```
specification {
  element actor {
    style {
      shape person
    }
  }
  element system
  element container
  element component
  element database {
    style {
      shape storage
    }
  }
  relationship async

  deploymentNode environment
  deploymentNode region
  deploymentNode cloudRun {
    technology 'Google Cloud Run'
  }
}
```

---

## 4. `model` — elements and relationships

Nesting expresses containment. `=` binds a name; the string is the title.

```
model {
  dispatcher = actor 'Dispatcher' {
    description 'Assigns Jobs to crews within their region'
  }

  fieldwork = system 'Fieldwork Ops Platform' {
    description 'Scheduling and dispatch for utility field crews'

    web = container 'Dispatcher Console' {
      technology 'React 18, Vite'
      description 'Job assignment and monitoring UI'
    }

    api = container 'dispatch-api' {
      technology 'Node.js, Express'
      description 'Owns Job and Dispatch Run lifecycle'

      assignSvc = component 'Assignment Service' {
        technology 'TypeScript'
        description 'Validates region and crew availability'
      }
    }

    db = database 'Operational Store' {
      technology 'PostgreSQL 15'
    }

    web -> api 'makes API calls to' {
      technology 'HTTPS/JSON'
    }
    api -> db 'reads from and writes to' {
      technology 'SQL/TCP'
    }
  }

  twilio = system 'Twilio' {
    description 'Third-party SMS and push delivery'
    style {
      color muted
    }
  }

  dispatcher -> web 'assigns Jobs using'
  fieldwork.api -> twilio 'sends crew notifications via' {
    technology 'HTTPS/REST'
  }
}
```

Relationships may be declared inside an element (relative references) or at the
top level (fully qualified). Kinded relationships use `-[async]->`.

---

## 5. `views` — projecting C4 levels

LikeC4 does not impose a level count — the C4 discipline comes from how the views
are defined. `index` is the default view.

```
views {
  view index {
    title 'System Context — Fieldwork Ops Platform'
    include dispatcher, crewLead, fieldwork, twilio
  }

  view containers of fieldwork {
    title 'Container Diagram — Fieldwork Ops Platform'
    include *
    include dispatcher, twilio
  }

  view apiComponents of fieldwork.api {
    title 'Component Diagram — dispatch-api'
    include *
    include fieldwork.web, fieldwork.db
  }
}
```

Useful mechanics:

- `view of <element>` scopes the view; references resolve relative to that element,
  and the view becomes that element's default on click-through.
- `include *` pulls in the scoped element's children — the workhorse predicate.
- `include * -> some.element` includes incoming relationships.
- `exclude` removes noise after a broad include.
- `view x extends y` inherits predicates and styles.
- Properties (`title`, `description`, `tags`, `link`) come before predicates.

---

## 6. `deployment` — the physical layer

A separate hierarchy that references the logical model via `instanceOf` and
inherits its relationships. This is what the C4 Deployment diagram needs.

```
deployment {
  environment prod 'Production' {
    technology 'Terraform'

    region useast1 'us-east1' {
      cloudRun apiNode {
        instanceOf fieldwork.api
      }
      cloudRun crewNode {
        instanceOf fieldwork.crewSvc
      }
      db = instanceOf fieldwork.db {
        title 'Cloud SQL (primary)'
      }
    }
  }
}
```

Instances can override title, technology, and style. Deployment-only
relationships are allowed (`vm2.db -> vm1.db 'replicates'`) — useful for
replication that has no place in the logical model. Deploy to any level, not just
leaves. Deployment views live in `views` and are documented under Deployment views.

---

## 7. CLI commands that matter here

No install needed to try it: `npx likec4 <command>`. For a project, `npm i -D likec4`.

| Command | Use |
|---|---|
| `likec4 validate` | Syntax errors and layout drift. Non-zero exit on failure. **Run this every time.** |
| `likec4 serve` (`start`, `dev`) | Local preview with hot reload on `:5173` |
| `likec4 build -o ./dist` | Static site for sharing or embedding |
| `likec4 gen mmd` / `gen mermaid` | Emit Mermaid from the model |
| `likec4 gen dot` / `d2` / `plantuml` | Other notations |
| `likec4 export json -o dump.json` | Machine-readable model |
| `likec4 export drawio` | One `.drawio` per view, for editable handoff |
| `likec4 export png -o ./assets` | **Requires Playwright** — prompts to install if absent |
| `likec4 format --check` | CI-friendly formatting check |

`validate` and `gen` need no browser, so they work in restricted sandboxes where
`export png` will not.

---

## 8. Mapping C4 levels onto views

LikeC4 will not enforce the levels, so hold the line deliberately:

| C4 level | View |
|---|---|
| L1 Context | `view index` — actors, the system, external systems. No containers. |
| L2 Container | `view containers of <system>` with `include *`, plus actors and externals |
| L3 Component | `view <name>Components of <system>.<container>` — one container only |
| L4 Code | Out of scope for LikeC4; if genuinely needed, a Mermaid `classDiagram` alongside |
| Deployment | A view over the `deployment` model, one per environment |

The abstraction-level checks in `c4-and-mermaid.md` still apply: no containers in
the Context view, technology on every container and component, verb-phrase
relationship labels with a technology.

---

## 9. Getting Mermaid out anyway

When someone wants Mermaid in a README or Confluence page but the model lives in
LikeC4, generate rather than hand-write:

```bash
likec4 gen mmd -o docs/architecture/mermaid/
```

Generated Mermaid is downstream of the validated model, which makes it the
preferred way to produce Mermaid at all — the model stays the single source of
truth and the `.mmd` files become build output rather than a second thing to
maintain. Note this in the repo so nobody hand-edits the generated files.

**Two things to know about the output** (verified against likec4 1.59.2):

- It emits **flowchart syntax** (`graph TB` with `@{ shape: ... }` node syntax), not
  the `C4Container` macro set. So `scripts/lint_c4.py` does not apply to it — that
  linter checks C4 macros. Validate the model with `likec4 validate` instead; the
  generated file is an artifact of an already-validated model.
- It is **lossy**: node labels and relationship labels survive, but element
  technology and descriptions do not appear in the generated Mermaid. If a
  stakeholder needs technology visible in a Mermaid diagram, either hand-write that
  one diagram with C4 macros or export PNG/SVG from LikeC4 instead.

---

## Related

- Editors: a VS Code extension and JetBrains support exist — the user's choice to
  install, never something to assume.
- `likec4 lsp` provides language-server support for other editors.
- Erode, a community drift-detection tool, is worth mentioning to teams that care
  about diagrams staying true over time.
