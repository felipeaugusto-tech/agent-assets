# Distributing a Plugin Across Your Organization

**Claude chat and Claude Code are fed by two different admin systems — using the wrong one is silent, and costs hours.**

| Field | Value |
|-------|-------|
| **Audience** | Org Owners, Primary Owners, anyone distributing an internal plugin |
| **Prerequisites** | Claude for Teams or Enterprise; Owner or Primary Owner role |
| **Reading time** | ~10 minutes |
| **Related** | [1-plugin-overview.md](1-plugin-overview.md) · [3-token-benchmarks.md](3-token-benchmarks.md) |

## How to read the source markers

| Marker | Meaning |
|--------|---------|
| **[docs]** | Stated in official Anthropic documentation, with a link |
| **[verified]** | Not documented; observed on our machines on 2026-08-26/27 with Claude Code v2.1.247, with the command that showed it |

---

## Table of Contents

- [The one thing to understand first](#the-one-thing-to-understand-first)
- [Path A — Claude chat and Cowork](#path-a--claude-chat-and-cowork)
- [Path B — Claude Code](#path-b--claude-code)
- [What we actually did](#what-we-actually-did)
- [Three corrections to a common explanation](#three-corrections-to-a-common-explanation)
- [Troubleshooting](#troubleshooting)
- [Related Resources](#related-resources)

---

## The one thing to understand first

There are two admin console pages. They look interchangeable. They are not.

| | **Organization plugins** | **Managed settings** |
|---|---|---|
| Console page | `claude.ai/admin-settings/plugins` | `claude.ai/admin-settings/claude-code` |
| Mechanism | Org plugin marketplace | Server-managed settings |
| **Reaches** | Claude chat (web and the Chat tab in Claude Desktop) and Claude Cowork | **Claude Code** |
| Plugin source | Uploaded `.zip`, or GitHub sync | Git repo, via `extraKnownMarketplaces` |
| Repo visibility | Private or internal **required** | Public or private both work |
| Updates | Manual re-upload | Automatic with `autoUpdate: true` |

The support article states where org-distributed plugins appear, and Claude Code is not among them. **[docs]** — [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)

> "Plugins you distribute appear in both chat (on the web and the Chat tab in Claude Desktop) and Claude Cowork."

Note the precision required here. The documentation does **not** say Claude Code is excluded; it simply names three surfaces and never mentions Claude Code either way. What makes the conclusion firm is the second half of the evidence, from our own machines. **[verified]**

- After uploading the plugin and setting it to *Available to install*, `claude plugin marketplace list` never showed the marketplace, across repeated restarts.
- A full startup debug capture (`claude --debug --debug-file <path> -p "hi"`) showed **no server call** capable of delivering an org marketplace.

Documented absence plus measured absence. If you only need Claude chat, use Path A. If you need Claude Code, you must use Path B.

---

## Path A — Claude chat and Cowork

Use `claude.ai/admin-settings/plugins`. Requires Owner or Primary Owner, and both Cowork and Skills enabled for the organization first. **[docs]** — [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)

Two ways to load plugins, with these limits: **[docs]**

| Method | Limits |
|---|---|
| Manual `.zip` upload | Under 50 MB; up to 100 plugins per marketplace |
| GitHub sync | Repository must be **private or internal**; public repos are rejected. Up to 500 plugins |

Per plugin you choose an access level: *Installed by default*, *Available for install*, *Not available*, or *Required*. Group-level overrides are Enterprise-only. **[docs]**

If you upload a `.zip`, note that the plugin contents must sit at the **archive root** — `.claude-plugin/plugin.json` at the top level, not nested inside a wrapper folder. **[verified]** An archive wrapped in a containing folder fails to load, reporting `Unknown command`, while the same files zipped from the root work.

---

## Path B — Claude Code

For Claude Code, a **git repository acts as the marketplace**. There is no zip-upload path.

### Step 1 — Make the repo a marketplace

Add `.claude-plugin/marketplace.json` at the repository root. **[docs]** — [Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "hatchworks",
  "description": "Internal Claude Code plugins for Hatchworks / GenDD workflows",
  "owner": { "name": "Felipe Augusto" },
  "plugins": [
    {
      "name": "accurate-ai-product",
      "description": "Product & planning skills for Accurate AI: write PRDs, turn source material into traceable user stories, and estimate Jira story points.",
      "source": "./accurate-ai-product"
    },
    {
      "name": "accurate-ai-engineer",
      "description": "Engineering & QA skills for Accurate AI: ADRs, C4 architecture diagrams, CI/CD pipeline security audits, QA test-case authoring, TestRail publishing, test-gap analysis, test-automation implementation, and release-evidence packets.",
      "source": "./accurate-ai-engineer"
    }
  ]
}
```

Validate and push:

```bash
claude plugin validate . --strict
git add .claude-plugin/marketplace.json && git commit && git push
```

### Step 2 — Choose how it reaches people

Two options, and the difference matters.

| | **Option B1 — project settings** | **Option B2 — managed settings** |
|---|---|---|
| Where | `.claude/settings.json` in a repo | `claude.ai/admin-settings/claude-code` |
| Scope | Only people working in that repo | Everyone in the organization |
| User action | Must trust the project folder | None |
| Who configures | Any developer | Owner or Primary Owner only |
| Best for | A tool tied to one codebase | An organization-wide capability |

**Option B1** — commit to the project's `.claude/settings.json`. Claude Code adds the marketplace once a team member trusts the repository folder. **[docs]** — [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)

```json
{
  "extraKnownMarketplaces": {
    "hatchworks": { "source": { "source": "github", "repo": "your-org/your-repo" } }
  },
  "enabledPlugins": {
    "accurate-ai-product@hatchworks": true,
    "accurate-ai-engineer@hatchworks": true
  }
}
```

**Option B2 — recommended for org-wide distribution.** Server-managed settings are delivered from Anthropic's servers, fetched at startup and polled hourly. **[docs]** — [Configure server-managed settings](https://code.claude.com/docs/en/server-managed-settings)

Requirements: **[docs]**

- Claude for Teams or Claude for Enterprise
- Owner or Primary Owner role
- Network access to `api.anthropic.com`
- Not using a third-party provider (Bedrock, Vertex, Foundry) or a custom `ANTHROPIC_BASE_URL`

---

## What we actually did

*This section documents the original rollout of the single-plugin `gendd` POC, kept as-is for historical/verified record. The plugin has since been split into `accurate-ai-product` and `accurate-ai-engineer` (see the Step 1 sample above); a re-publish of managed settings under the new plugin names hasn't been re-verified on our machines yet.*

Path B, Option B2. Published at `claude.ai/admin-settings/claude-code` → Managed settings:

```json
{
  "extraKnownMarketplaces": {
    "hatchworks": {
      "source": { "source": "github", "repo": "felipeaugusto-tech/agent-assets" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": { "gendd@hatchworks": true }
}
```

### What happens on a teammate's machine

**[verified]** Nothing is required of them. On the first launch after publication, Claude Code registers the marketplace and installs the plugin **in the background**; it is available from the next launch. A first invocation attempted immediately after publication returned `Unknown command`, and the same command succeeded on the following run.

Confirm the end state:

```bash
claude plugin list
```

```text
❯ gendd@hatchworks
  Version: 0.1.0
  Scope: managed
  Status: ✔ enabled
```

`Scope: managed` is the marker that it came from the organization rather than from anything local.

### Shipping an update

Commit and push to the repository. With `autoUpdate: true`, the change reaches everyone without touching the console. **[docs]** — [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)

### Before you publish managed settings

- **Managed settings apply to the entire organization uniformly.** Per-group configuration is not supported. **[docs]** — [Configure server-managed settings](https://code.claude.com/docs/en/server-managed-settings)
- They occupy the highest tier in the settings hierarchy, overriding user, project, and local values for any key they contain. **[docs]** — [Deploy managed settings](https://code.claude.com/docs/en/managed-settings) — so keep the payload to the two plugin keys unless you intend broader policy.
- Clearing the console does not take effect instantly; cached settings persist on each client until its next successful fetch. **[docs]**

---

## Three corrections to a common explanation

A widely circulated summary of this topic gets three things wrong in ways that will cost you time.

**1. "For Claude Code, commit to your project's `.claude/settings.json`."**

That is Option B1 — correct, but per-repository, and it requires each teammate to trust the folder. For organization-wide delivery, Option B2 (managed settings) needs nothing from the user and is not tied to a repo. Both work; pick deliberately.

**2. "GitHub sync requires a private or internal repo — public repos aren't allowed."**

True **only** for Path A, the org plugins console. **[docs]** The Claude Code path places no such restriction: our marketplace runs from a **public** repository and installs without any GitHub authentication. **[verified]** Conflating the two sends you hunting for a private-repo requirement that does not apply.

**3. "Teammates run `/plugin marketplace add owner/repo`."**

Required for Option B1 and for ad-hoc sharing. **Not** required under managed settings, where registration and installation are automatic. **[verified]**

---

## Troubleshooting

### The marketplace never appears in Claude Code

Check whether your organization has ever published managed settings:

```bash
cat ~/.claude/remote-settings.json
```

If it prints `{}`, no managed settings exist. Confirm with a startup capture:

```bash
claude --debug --debug-file /tmp/cc.log -p "hi"
grep -i "remote settings" /tmp/cc.log
```

```text
[DEBUG] Remote settings: No settings found (404)
[DEBUG] Remote settings: Saved empty sentinel (404 response)
```

**[verified]** This means the organization has no Claude Code settings document — nothing to do with your plugin. Publish at `claude.ai/admin-settings/claude-code`, restart, and confirm `remote-settings.json` is no longer `{}`.

A useful contrast in the same log: `Policy limits: Fetched successfully` alongside the settings 404 proves authentication and organization lookup are fine, and isolates the problem to the settings document itself.

### Confirming which source is in play

Run `/status` in an interactive session and read the `Setting sources` line. `Enterprise managed settings (remote)` means server-managed settings are active. **[docs]** — [Deploy managed settings](https://code.claude.com/docs/en/managed-settings)

### Avoiding a false positive

If you previously ran `claude plugin marketplace add` yourself, remove it before testing org delivery:

```bash
claude plugin marketplace remove hatchworks
```

Otherwise you cannot tell whether the marketplace arrived from the organization or from your own earlier command.

---

## Related Resources

| Resource | Path | Description |
|---|---|---|
| Plugin overview | [1-plugin-overview.md](1-plugin-overview.md) | What a plugin is and how this one is built |
| Token benchmarks | [3-token-benchmarks.md](3-token-benchmarks.md) | Measured cost of installing and invoking |
| Marketplace manifest | `../.claude-plugin/marketplace.json` | The file that makes this repo a marketplace |
| Official: org plugins | https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization | Path A — chat and Cowork |
| Official: server-managed settings | https://code.claude.com/docs/en/server-managed-settings | Path B, Option B2 |
| Official: managed settings | https://code.claude.com/docs/en/managed-settings | Delivery mechanisms and precedence |
| Official: marketplaces | https://code.claude.com/docs/en/plugin-marketplaces | Creating and distributing a marketplace |
| Official: settings reference | https://code.claude.com/docs/en/settings-reference | `extraKnownMarketplaces`, `enabledPlugins` |

Console pages (require an Owner login; not publicly reachable): `claude.ai/admin-settings/plugins` and `claude.ai/admin-settings/claude-code`.

---

*This is tooling documentation, not a standard. It carries no standards frontmatter and is intentionally not registered in `rules-manifest.yaml` — a deliberate choice, not an omission.*
