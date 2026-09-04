---
name: spike-doc
description: Record a time-boxed investigation -- what was tried, what was found, and a recommendation -- so the finding survives past the person who ran it. Manual invocation only.
disable-model-invocation: true
---

# Spike Doc

For a genuinely uncertain question worth investigating before committing to an approach in a spec or implementation plan — which library actually supports what's needed, whether an approach performs acceptably, whether an assumption holds.

## 1. Fix the target and get the question

The target is **the user's current project**, never this plugin or the GenDD corpus.

Get a precise question before starting — "investigate caching" isn't a spike question; "can Redis Cluster handle our write pattern without cross-slot errors" is. If the question given is too vague to have a clear answer, help narrow it first rather than running an unfocused investigation.

Also get the time-box — how long this gets before a decision is made with whatever's known at that point.

## 2. Load the references (now, not before)

| File | Role |
| --- | --- |
| `${CLAUDE_PLUGIN_ROOT}/references/spike-doc/spike-doc.md` | **Primary task flow.** |
| `${CLAUDE_PLUGIN_ROOT}/references/spike-doc/spike-template.md` | **Output template.** |

## 3. Run the process

1. **Do the investigation** — read docs, run a prototype, benchmark — whatever actually answers the question, within the time-box.
2. **Record what was tried**, not just the conclusion — enough detail that a skeptical reader could see why the conclusion follows, without redoing the spike themselves.
3. **State a recommendation** — proceed, proceed with named caveats, pick a different approach, or spend one more time-boxed round on a narrower question. "More research needed" alone means the time-box ran out without producing the spike's value — say that plainly if it happened.
4. **Name what this feeds** — the spec or implementation plan whose design depends on this answer.

Fill `spike-template.md` and save to `docs/spikes/{topic-slug}.md`.

## 4. Never invent

A finding not actually produced by the investigation isn't a finding. If the time-box ran out before a clear answer emerged, say that rather than writing a confident conclusion the investigation didn't support.

## 5. Hard limits

- Writes only `docs/spikes/{topic-slug}.md`.
- Respects the stated time-box — flag when it's reached rather than continuing indefinitely.
- No MCP tools beyond what's needed to actually investigate (e.g. reading docs, running code the user has in the repo) — this isn't a blanket exception like `generate-ide-rules`' web search; stay within what the investigation actually requires.
- No production code changes — a spike's prototype code, if any, stays out of the main change until a spec or plan formalizes it.
