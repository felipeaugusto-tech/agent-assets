# Engagement Context — TEMPLATE (fill in per engagement, or delete)

> **This file is optional and secondary.** The primary source of project truth is
> the GenDD Context Pack in the repository `docs` folder — `context.md`,
> `architecture.md`, `conventions.md`, `testing.md`, `agents.md`. Read that first.
>
> This file exists for facts that are not in the client repo, or not there yet:
> engagement scope, decisions made in meetings, an open-contradiction log, Jira
> conventions, and who owns which open question.
>
> **Precedence:** the repo Context Pack wins on technical reality. This file wins
> on engagement reality — what was decided, by whom, and what is in scope. Where
> they conflict on the same fact, the engine surfaces both rather than choosing.
>
> Leaving placeholders unfilled is worse than deleting a section — an unfilled
> `[...]` reads as a real value. If a section does not apply, remove it.
>
> **Engagement:** [client / project name]
> **Repo(s) in scope:** [repo — or "none; generic mode"]
> **Context version:** [v1 — date]
> **Maintainer:** [name]

---

## 1. Product & scope boundaries

| Product / area | In scope? | Notes |
|---|---|---|
| [name] | [in / out / conditional] | [notes] |

**Out-of-scope rule:** a requirement landing in an out-of-scope area gets
surfaced, not expanded. A conditional area proceeds with every AC flagged as an
assumption.

---

## 2. System facts not in the repo Context Pack

Fill only what the repo does not already say. Do not duplicate — duplication goes
stale and then contradicts.

- **Multi-tenant:** [yes / no] — [isolation model, and what a cross-tenant request should return]
- **Compliance scope:** [PCI / HIPAA / FedRAMP / GDPR / CCPA / none] — [what it constrains]
- **Tech stack:** [languages, frameworks — informs realistic verification lines]
- **Third-party integrations:** [service — what it does — is its failure contract defined?]
- **Known brownfield surprises:** [places the system contradicts reasonable assumptions]

---

## 3. Personas

| Persona | Role / permissions | Relevant flows |
|---|---|---|
| [name] | [role, entitlements] | [flows] |

---

## 4. Confirmed decisions (cite these; do not re-ask)

| # | Decision | Source | Date |
|---|---|---|---|
| [D1] | [what was decided] | [meeting / doc / ticket] | [date] |

---

## 5. Open contradictions

The engine flags stories touching these and routes them to the owner. It never
resolves one itself.

| # | Contradiction | Areas affected | Owner | Status |
|---|---|---|---|---|
| [C1] | [what conflicts with what] | [area] | [name] | open |

---

## 6. Story conventions

- **Jira project key / issue types:** [key, and which issue type stories vs. follow-ups use]
- **Acceptance-criteria field:** [dedicated field, or description? drives Step 5 mapping]
- **Definition of Ready additions:** [anything this team requires beyond the skill's checklist]
- **Standing NFR baselines:** [performance / accessibility / security defaults that apply to every story]
- **Follow-up handling:** [file immediately, or list in the story for grooming?]
- **Question routing:** [who answers product questions vs. technical ones]

---

## 7. Maintenance triggers

Update this file — not `SKILL.md` — when any of these fire:

- A decision is confirmed, or a logged contradiction is resolved.
- Scope changes, or a new product area comes in.
- A new integration lands, or an integration's failure contract gets defined.
- Jira conventions or Definition of Ready change.
- New personas or standing NFR baselines.

Bump the context version when you update, so a session can tell what it ran against.
