# Claude Code Plugins — Overview

**A plugin is a versioned, shareable bundle of capabilities that Claude Code loads on demand — this document explains what that means and how the `gendd` plugin is built.**

| Field | Value |
|-------|-------|
| **Audience** | Engineers, tech leads, anyone evaluating or building an internal plugin |
| **Prerequisites** | Claude Code installed |
| **Reading time** | ~8 minutes |
| **Related** | [2-distribution-guide.md](2-distribution-guide.md) · [3-token-benchmarks.md](3-token-benchmarks.md) |

## How to read the source markers

Every claim about Claude Code behavior in this document carries one of two markers:

| Marker | Meaning |
|--------|---------|
| **[docs]** | Stated in official Anthropic documentation, with a link |
| **[verified]** | Not documented; observed on our machines, with the command that showed it |

---

## Table of Contents

- [What a plugin is](#what-a-plugin-is)
- [Why a plugin beats pasting instructions](#why-a-plugin-beats-pasting-instructions)
- [Anatomy of a plugin](#anatomy-of-a-plugin)
- [Who decides when a skill runs](#who-decides-when-a-skill-runs)
- [How the gendd plugin is built](#how-the-gendd-plugin-is-built)
- [Related Resources](#related-resources)

---

## What a plugin is

A plugin extends Claude Code with any combination of **skills, agents, hooks, MCP servers, and LSP servers**, installed as one unit from a marketplace. **[docs]** — [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)

A **skill** is the piece that matters most here. It is a `SKILL.md` file holding instructions Claude follows. Claude can use a skill when it judges it relevant, or you can invoke it directly with `/skill-name`. **[docs]** — [Extend Claude with skills](https://code.claude.com/docs/en/skills)

Skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools. Claude Code extends that standard with invocation control, subagent execution, and dynamic context injection. **[docs]** — [Extend Claude with skills](https://code.claude.com/docs/en/skills)

Plugin skills are **namespaced by the plugin name**, so a plugin named `gendd` providing a skill named `enhance-requirements` yields `/gendd:enhance-requirements`. **[docs]** — [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)

---

## Why a plugin beats pasting instructions

The three GenDD requirements documents already existed in this repository before the plugin did. Anyone could open them and paste them into a chat. The plugin changes four things:

| Problem with pasting | What the plugin does |
|---|---|
| You must know the documents exist and where they live | One command, discoverable in `/plugin` |
| You paste ~1,100 lines of methodology every time | Content loads only when the skill runs |
| Everyone's copy drifts | One source of truth, versioned in git |
| Sharing means sending links and hoping | Distributed org-wide automatically |

The cost argument is not hypothetical — see [3-token-benchmarks.md](3-token-benchmarks.md) for measured numbers.

---

## Anatomy of a plugin

```text
claude-plugin-poc/                        <- the plugin root
├── .claude-plugin/
│   └── plugin.json                       <- manifest: name, description, version
├── skills/
│   └── enhance-requirements/
│       └── SKILL.md                      <- the skill: frontmatter + instructions
└── references/
    └── enhance-requirements/             <- supporting files, loaded on demand
        ├── enhance-requirements.md
        ├── enhance-acceptance-criteria.md
        └── requirements-enhancement.md
```

One file lives outside the plugin, at the repository root, and turns the repo into a **marketplace**:

```text
.claude-plugin/marketplace.json           <- lists the plugins this repo offers
```

| File | Required | Purpose |
|---|---|---|
| `.claude-plugin/plugin.json` | Yes | Identifies the plugin. `name` sets the command namespace |
| `skills/<name>/SKILL.md` | — | A skill. A plugin may have many, or none |
| `references/` | No | Any supporting files the skill reads at runtime |
| `.claude-plugin/marketplace.json` | For sharing | Catalog entry so others can install it |

Validate any plugin or marketplace manifest before shipping. **[docs]** — [Plugins reference](https://code.claude.com/docs/en/plugins-reference)

```bash
claude plugin validate ./claude-plugin-poc --strict
```

Reference files are addressed from `SKILL.md` with `${CLAUDE_PLUGIN_ROOT}`, which resolves to the installed plugin's directory wherever it lands on disk.

---

## Who decides when a skill runs

**This is the most reusable decision in the whole plugin, and the direct cause of its token profile.**

Every skill answers one question: when the moment arrives, who starts it — Claude, or you?

| Mode | Frontmatter | Behavior |
|---|---|---|
| **Claude decides** | default (`disable-model-invocation: false`) | Claude loads the skill whenever it judges it relevant |
| **You decide** | `disable-model-invocation: true` | Only a typed `/name` starts it |

The official guidance frames this as a control question, not an optimization. **[docs]** — [Control who invokes a skill](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill)

> "Only you can invoke the skill. Use this for workflows with side effects or that you want to control timing, like `/commit`, `/deploy`, or `/send-slack-message`. You don't want Claude deciding to deploy because your code looks ready."

### What setting it costs you

Do not apply this reflexively. Turning it on gives up four things. **[docs]** — [Extend Claude with skills](https://code.claude.com/docs/en/skills)

- Claude can never invoke the skill on its own, however well a request matches it.
- The skill will not be preloaded into subagents.
- As of Claude Code v2.1.196, a scheduled task that fires with the skill as its prompt will not run it.
- Anything else that reaches a skill through model invocation, including `/loop` re-entry, is blocked too.

If you want the behavior without editing the file, `skillOverrides: "user-invocable-only"` in settings does the same thing. **[docs]** — [Extend Claude with skills](https://code.claude.com/docs/en/skills)

### Why it is right for this skill

`enhance-requirements` is human-initiated and human-in-the-loop. Someone has a requirement in hand and decides to refine it; there is no scenario where Claude should start writing acceptance criteria unprompted. Losing automation costs nothing here.

For a skill meant to run unattended — a nightly report, a CI check — this flag would be the wrong call.

### What it actually saves

Be precise about the claim. The flag does **not** make the skill free. What it defers is the skill body and everything the skill reads:

| Item | Size |
|---|---|
| `SKILL.md` | 62 lines / 3,646 bytes |
| Bundled reference files | 1,126 lines / 37,906 bytes |
| **Total deferred payload** | **1,188 lines / 41,552 bytes** |

The measured cost of that deferral is in [3-token-benchmarks.md](3-token-benchmarks.md).

---

## How the gendd plugin is built

| Decision | Choice | Reason |
|---|---|---|
| Plugin name | `gendd` | Sets the namespace, giving `/gendd:enhance-requirements` |
| Skills | Exactly one | Proof of concept; scope kept deliberately small |
| Invocation | `disable-model-invocation: true` | Human-initiated task; see above |
| Methodology | Three verbatim copies under `references/` | Plugin stays self-contained anywhere it is installed |
| Agents / hooks / MCP | None | Not needed; every component added is context cost |

### The bundled references, and their broken links

The three files under `references/enhance-requirements/` are **byte-identical copies** of documents in `gendd-analysis/`, verified with `cmp`. Copying them verbatim keeps the plugin self-contained, but it carries a wrinkle worth knowing: their internal cross-links (`workflows/...`, `templates/...`, `@GenDD-Flow/...`) were written relative to `gendd-analysis/` and **do not resolve inside the plugin**. One of them, `templates/architecture-decision-record.md`, is a dead link even in the original repository.

Rather than edit the copies and lose byte-fidelity with the source, `SKILL.md` instructs the agent to ignore those cross-references and treat the three copied files as the complete input.

### The skill's contract

`SKILL.md` requires the agent to ask for a requirement if none was supplied, target the user's own project rather than the plugin source, label every inference as an assumption, and return results in chat only — no code changes, no files written, no MCP, no tests.

---

## Related Resources

| Resource | Path | Description |
|---|---|---|
| Distribution guide | [2-distribution-guide.md](2-distribution-guide.md) | How this plugin reaches teams, and the two mechanisms involved |
| Token benchmarks | [3-token-benchmarks.md](3-token-benchmarks.md) | Measured cost of installing and invoking the plugin |
| Install instructions | [README.md](README.md) | Local install and invocation |
| The skill itself | `skills/enhance-requirements/SKILL.md` | Frontmatter and instructions |
| Official: skills | https://code.claude.com/docs/en/skills | Skills, frontmatter, invocation control |
| Official: plugins | https://code.claude.com/docs/en/plugins | Building plugins |
| Official: plugins reference | https://code.claude.com/docs/en/plugins-reference | Complete technical specification |
| Agent Skills standard | https://agentskills.io | The open standard skills follow |

---

*This is tooling documentation, not a standard. It carries no standards frontmatter and is intentionally not registered in `rules-manifest.yaml` — a deliberate choice, not an omission.*
