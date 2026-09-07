# Claude Code Plugins — Overview

**A plugin is a versioned, shareable bundle of capabilities that Claude Code loads on demand — this document explains what that means and how the `accurate-ai-product` and `accurate-ai-engineer` plugins are built.**

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
- [How the two plugins are built](#how-the-two-plugins-are-built)
- [Related Resources](#related-resources)

---

## What a plugin is

A plugin extends Claude Code with any combination of **skills, agents, hooks, MCP servers, and LSP servers**, installed as one unit from a marketplace. **[docs]** — [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)

A **skill** is the piece that matters most here. It is a `SKILL.md` file holding instructions Claude follows. Claude can use a skill when it judges it relevant, or you can invoke it directly with `/skill-name`. **[docs]** — [Extend Claude with skills](https://code.claude.com/docs/en/skills)

Skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools. Claude Code extends that standard with invocation control, subagent execution, and dynamic context injection. **[docs]** — [Extend Claude with skills](https://code.claude.com/docs/en/skills)

Plugin skills are **namespaced by the plugin name**, so a plugin named `accurate-ai-product` providing a skill named `prd-writer` yields `/accurate-ai-product:prd-writer`. **[docs]** — [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)

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
accurate-ai-engineer/                     <- one plugin root (accurate-ai-product is the same shape)
├── .claude-plugin/
│   └── plugin.json                       <- manifest: name, description, version
└── skills/
    └── adr-writer/
        ├── SKILL.md                      <- the skill: frontmatter + instructions
        └── references/                   <- supporting files, loaded on demand
            └── adr-template.md
```

Each skill folder carries its own `references/` (and, where needed, `scripts/`) alongside its `SKILL.md` — there is no repo-wide `references/` tree; every skill is self-contained.

One file lives outside any plugin, at the repository root, and turns the repo into a **marketplace**:

```text
.claude-plugin/marketplace.json           <- lists the plugins this repo offers
```

| File | Required | Purpose |
|---|---|---|
| `.claude-plugin/plugin.json` | Yes | Identifies the plugin. `name` sets the command namespace |
| `skills/<name>/SKILL.md` | — | A skill. A plugin may have many, or none |
| `skills/<name>/references/`, `skills/<name>/scripts/` | No | Supporting files that skill reads at runtime |
| `.claude-plugin/marketplace.json` | For sharing | Catalog entry so others can install it |

Validate any plugin or marketplace manifest before shipping. **[docs]** — [Plugins reference](https://code.claude.com/docs/en/plugins-reference)

```bash
claude plugin validate ./accurate-ai-product --strict
claude plugin validate ./accurate-ai-engineer --strict
```

Reference files are addressed from `SKILL.md` with `${CLAUDE_PLUGIN_ROOT}`, which resolves to the installed plugin's directory wherever it lands on disk.

---

## Who decides when a skill runs

*The worked example in this section (`enhance-requirements`) is kept from the original single-skill `gendd` POC as illustrative methodology — it predates the split into `accurate-ai-product` and `accurate-ai-engineer` and isn't one of the skills either plugin ships today. The underlying control question and its trade-offs still apply to every skill in both plugins.*

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

## How the two plugins are built

The original `gendd` proof of concept has been split by audience into two
plugins, each installed and versioned independently:

| Plugin | Namespace | Skills |
|---|---|---|
| `accurate-ai-product` | `/accurate-ai-product:<skill>` | `prd-writer`, `stories-from-source`, `jira-story-estimator` |
| `accurate-ai-engineer` | `/accurate-ai-engineer:<skill>` | `adr-writer`, `architecture-diagram-generator`, `cicd-pipeline-audit`, `qa-test-case-writer`, `release-evidence-packet`, `test-automation-implementer`, `test-gap-analyzer`, `testrail-publisher` |

| Decision | Choice | Reason |
|---|---|---|
| Two plugins, not one | Split by audience (product vs. engineering/QA) | Each team installs only the skills relevant to their work; namespaces stay meaningful |
| Invocation | Default (model-invocable) for every skill in both plugins | Each skill's own `description` frontmatter carries the trigger conditions Claude uses to decide relevance — see [Who decides when a skill runs](#who-decides-when-a-skill-runs) for the underlying control question |
| Supporting files | Per-skill `references/`/`scripts/`, not a shared tree | Every skill folder is self-contained and portable on its own |
| Agents / hooks / MCP | None | Not needed; every component added is context cost |

---

## Related Resources

| Resource | Path | Description |
|---|---|---|
| Distribution guide | [2-distribution-guide.md](2-distribution-guide.md) | How this plugin reaches teams, and the two mechanisms involved |
| Token benchmarks | [3-token-benchmarks.md](3-token-benchmarks.md) | Measured cost of installing and invoking the plugin |
| The plugins' manifest | [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) | Catalog entry for both plugins |
| The skills themselves | `accurate-ai-product/skills/`, `accurate-ai-engineer/skills/` | Frontmatter and instructions, one `SKILL.md` per skill |
| Official: skills | https://code.claude.com/docs/en/skills | Skills, frontmatter, invocation control |
| Official: plugins | https://code.claude.com/docs/en/plugins | Building plugins |
| Official: plugins reference | https://code.claude.com/docs/en/plugins-reference | Complete technical specification |
| Agent Skills standard | https://agentskills.io | The open standard skills follow |

---

*This is tooling documentation, not a standard. It carries no standards frontmatter and is intentionally not registered in `rules-manifest.yaml` — a deliberate choice, not an omission.*
