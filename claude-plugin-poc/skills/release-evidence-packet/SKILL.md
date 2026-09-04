---
name: release-evidence-packet
description: >-
  Assemble a change-evidence packet from one or more commits — each one's diff, its
  metadata, and (if the requester supplies it) an acceptance-criteria mapping — into
  one dated artifact, then check its integrity. The integrity pass is the point: it
  cross-checks that whatever was supplied describes commits that are actually in this
  packet, and that no required section is silently absent. Its evidence is limited to
  what the named commits themselves show, plus whatever the requester hands over
  directly — it reads commits, it does not execute anything and does not reach
  external systems for evidence. Use it whenever someone says "put together the
  release evidence," "what changed in these commits," "summarize this commit (or this
  batch of commits)," "why was this changed," or wants a rigorous, commit-grounded
  account of a change, local or remote. It never renders a judgment on the change —
  it states what the commits show, why, and where the intent behind them is unclear.
  Do NOT use for reviewing code quality line by line, or when the requester wants
  evidence that cannot be derived from a commit's own diff and metadata.
---

# Release Evidence Packet

Assemble the artifact that documents exactly what a set of commits changed and why —
and nothing this skill invents on its own.

The assembly is the easy half. The half that matters is **integrity**, and it fails
in ways that look like success:

- **Evidence claimed beyond the commits.** A packet that implies more than the diff
  itself shows. The packet's whole authority rests on never overclaiming what a set
  of commits alone can prove.
- **Acceptance criteria supplied for commits that aren't in scope.** The requester
  hands over an AC list or traceability matrix generated against a different SHA (or
  against only some of the commits), and it quietly rides along as if it covers all
  of them.
- **A guessed rationale presented as fact.** The commit message says nothing useful,
  so a plausible-sounding reason gets written in and reads as established.
- **Sections quietly absent.** Nobody notices the missing part; a reviewer confirms
  what is in front of them.

So this skill treats the packet as evidence to be verified, not a document to be
formatted. If integrity cannot be established, that is the headline finding.

## What this skill takes as input

1. **One or more commits — required.** Local or remote, as long as each can be read
   (see Step 0). If none are named explicitly, infer which commits are relevant from
   whatever context the request gives — a time window, a path or module, a ticket
   reference, a branch, "the last N commits" — and say what was inferred and how.
   Everything about "what changed" comes from these commits alone: each one's diff
   against its own parent, its message, its metadata. There's no upper or lower bound
   — one commit and twenty commits are handled the same way, just repeated per
   commit.
2. **Acceptance criteria — optional.** If the requester supplies an AC list, a ticket,
   or a traceability matrix, the packet maps it against the combined diff. If nothing
   is supplied, the section is marked not applicable — never filled with a guess.

Evidence comes from the commits themselves and from whatever the requester hands over
directly. This skill reads commit metadata and diffs; it does not execute anything and
does not reach external systems to gather evidence. If the requester expects something
a diff and a commit message cannot establish, say so plainly rather than filling a
section from thin air.

## Step 0 — Resolve the commit(s)

**Parse commit ids liberally.** The requester may give one commit or several, in any
format — comma-separated, whitespace-separated, newline-separated, bulleted, or mixed
("`a1b2c3d, 77e2f10 9f8e7d6`", "these three: abc123, def456 and 789abc0"). Split on
commas, whitespace, and common list punctuation, then treat each surviving token that
looks like a commit reference (a hex-ish string, or something resolvable by `git
rev-parse`) as a candidate. Don't require a particular separator or a specific
sentence pattern — the point is to recover every id the requester meant, not to match
a format.

**If no explicit commit is named, infer the relevant set from context** rather than
asking by default:

```bash
git log --since="<inferred window>" --oneline              # a time reference ("this week", "since Monday")
git log --oneline -- <path>                                 # a module or area named in the request
git log --grep="<term>" --oneline                            # a ticket id or keyword
git log -n <N> --oneline                                     # "the last N commits"
git log <tag-or-branch>..HEAD --oneline                       # "since v41", "what's new on this branch"
```

State plainly which commits were inferred and how, so the requester can correct scope
before reading further. Only ask directly when the request gives no usable signal at
all — no commit, no time window, no path, no branch, nothing to query against.

**For each candidate, resolve it independently** — a failure on one commit doesn't
invalidate the others, but does need to be reported:

**Local repo:**

```bash
git cat-file -e <commit>^{commit} 2>/dev/null && echo present
git show -s --format='%H%n%an <%ae>%n%cI%n%P%n%s' <commit>   # SHA, author, date, parent(s), subject
git branch --contains <commit> --all                          # branches it's reachable from
git describe --tags --always <commit>                          # tag or version, if any
```

**Not present locally, but a remote is configured:**

```bash
git fetch origin <commit>                # works if the host allows fetching by SHA
git show -s --format='%H%n%an <%ae>%n%cI%n%P%n%s' <commit>
```

**Remote only, no local clone** (a hosted repo Claude can reach via API/CLI or a
connected git-hosting tool): use whatever access is available — `gh api
repos/<org>/<repo>/commits/<sha>`, a GitLab equivalent, or an MCP connector — to pull
the same fields: SHA, author, timestamp, parent(s), message, and the diff/patch.

**If a commit cannot be resolved by any of these, say so immediately** for that
commit specifically. An unresolvable commit means nothing downstream can be
evidenced for it — there is no fallback identity to check anything against. Continue
with whichever commits did resolve, and list the unresolved one(s) as a finding, not
a silent omission.

For each resolved commit, record: full SHA, author, committer timestamp, parent
commit(s), subject/message, and any tag or branch it's reachable from. If the
requester also gave an overall release name, version, or target environment, record
those once at the packet level — they don't change what's checked, only what the
packet is labeled.

## Step 1 — Gather the evidence, from the commits only

**Change content — the diff each commit introduces, evidenced separately:**

```bash
git show <commit> --stat                       # files touched, at a glance
git show <commit>                              # full patch
git log -1 <commit> --format=%B                # full commit message, for ticket refs
```

If `<commit>` is a merge commit, a plain `git show` mostly shows conflict resolution,
not the incoming change. Diff it against its first parent instead, and say in the
packet that this is what was done:

```bash
git diff <commit>^1 <commit>
```

Do this **per commit**, not once for the whole batch — even if two commits are
adjacent on the same branch, each is recorded as its own evidence item with its own
diff, its own files-touched list, and its own tickets. Don't collapse multiple
commits into a single aggregate diff; that's exactly the kind of quiet merging that
makes it impossible to tell which commit actually introduced a given change.

From each commit's diff, record: files touched, insertion/deletion counts, anything
structural (migration files, config changes, dependency-manifest changes,
feature-flag definitions), and any ticket references found in the commit message
(e.g. `PROJ-123` patterns). This is the rigorous part — do not summarize any commit's
diff loosely; enumerate what actually changed, file by file, the same way a reviewer
would.

**Explain why, not just what.** For each commit, state the rationale as evidenced by
the commit message and the shape of the diff — what problem it appears to address,
and what in the message or code supports that reading. When the message and the diff
don't make the intent clear (a bare "fix", a diff touching files unrelated to what
the message describes, no ticket reference at all), say so explicitly as an unclear
finding rather than inferring a plausible-sounding reason. A guessed rationale
presented as fact is worse than an honest "intent not evidenced by this commit."

**Acceptance criteria — only if supplied:**

If the requester hands over an AC list, ticket, or traceability matrix, map each item
against the combined diff across all the commits: does a file or hunk in *any* of
them plausibly address it, and if so, which commit? Record it as "diff touches the
claimed area (commit X)" or "no related change found in any of these commits." Also
record which commit(s) the supplied AC data itself claims to describe; if it names a
commit that isn't part of this packet — or covers only some of the commits while
implying it covers all of them — that's a provenance mismatch. Step 2 catches it, but
flag it here too.

If no AC data is supplied, mark the section `{"not_applicable": true, "reason": "no
acceptance criteria provided with the request"}` — never leave it silently blank and
never infer criteria from the diff.

**Anything the commits cannot show is not in this packet.** If the requester expects
evidence that a diff and a commit message cannot establish, that's an explicit ask
for a different, broader packet — say so rather than writing a section around it.

**Do not fill a gap with a claim.** Missing evidence is a finding, and it is more
useful in the packet than a plausible sentence.

## Step 2 — Verify integrity

```bash
python3 scripts/verify_evidence.py --manifest evidence.json
```

The script checks what's actually checkable with only a set of commits and,
optionally, supplied AC data:

1. **Provenance agreement.** If AC data was supplied, does every commit it names
   actually belong to this packet's commit set? A mismatch here — a commit named that
   isn't in scope — is the single most consequential defect a commit-only packet can
   have, because it means the AC claims apply to code that isn't (or isn't entirely)
   what's being evidenced.
2. **Freshness.** If AC data carries its own timestamp, was it produced at or after
   the most recent of the commits it claims to cover? Data produced before that
   commit existed can't describe it.
3. **Completeness.** Every commit has its own change-content recorded, and
   acceptance criteria is either populated or explicitly marked not applicable with a
   reason.

Report each check as passed, failed, or not verifiable. **A packet that fails
integrity still gets produced** — with the failure at the top.

## Step 3 — Assemble the packet

```markdown
# Change Evidence — 2 commits
**Commits** `a1b2c3d4e5f6` (J. Alvarez, 2026-08-09T18:00Z), `77e2f1099999` (M. Singh, 2026-08-11T09:00Z)
**Prepared** 2026-08-19T15:40Z by AI

## Scope of this packet
Evidence is limited to these 2 commits' own diffs and metadata, plus acceptance
criteria supplied with the request. Anything not derivable from those is out of scope
and is not described here.

## Integrity
| Check | Result |
|---|---|
| Supplied AC data names only commits in this packet | **FAIL — AC matrix also names `9f8e7d6`, not in scope** |
| AC data produced at or after the most recent commit it covers | PASS |
| Every commit has change content, required sections present | PASS |

**The supplied AC matrix names a commit outside this packet's set and cannot be
counted as evidence for it as scoped. Re-supply it against exactly these two commits.**

## Change content

### `a1b2c3d4e5f6` — J. Alvarez, 2026-08-09T18:00Z
4 files changed, +102/-30 · 1 schema migration (`1720-add-tenant-id`) · tickets: PROJ-448

| File | Change |
|---|---|
| `db/migrations/1720-add-tenant-id.sql` | new migration, adds `tenant_id` column |
| `services/auth/session.py` | tenant scoping added to session lookup |

Why: commit message references PROJ-448 ("add tenant isolation to session lookup");
the migration and the scoping change in `session.py` both support that stated intent.

### `77e2f1099999` — M. Singh, 2026-08-11T09:00Z
2 files changed, +40/-8 · tickets: PROJ-455

| File | Change |
|---|---|
| `services/auth/session_scope.py` | new helper extracting the tenant-scope predicate |
| `services/auth/session.py` | follow-up fix to the tenant-scoping check |

Why: follows directly from `a1b2c3d4e5f6` — closes a gap in the same scoping logic
introduced there; message and diff agree.

## Acceptance criteria
Supplied: 2 · Diff appears to touch the claimed area: 1 · No related change found: 1

| AC | Diff touches claimed area? |
|---|---|
| PROJ-448-AC-1 (tenant isolation) | Yes — `session.py` in `a1b2c3d` |
| PROJ-448-AC-2 (audit log entry) | No related change found in either commit |

## Unclear
- Commit `9f8e7d6` (if in scope): no message beyond "fix", diff touches files
  unrelated to any stated intent — rationale could not be determined from the commit
  alone.
```

Order is deliberate: **scope statement, then integrity, then the change content and
its rationale, then what's left unclear.** A commit-only packet especially needs the
scope stated up front, so its boundary reads as deliberate rather than as an
oversight. With multiple commits, each one still gets its own change-content entry —
never a single blended diff that obscures which commit did what.

## Step 4 — Deliver

Write to `docs/release-evidence/<short-sha-or-batch-label>.md`, committed. It is an
audit artifact, so it needs to be immutable and diffable.

Then state, in the handover: the integrity result first, and which commits (if any)
had unclear rationale. Offer to post to a ticket or wiki page **only with explicit
confirmation**.

## Hard rules

1. Pin every commit in scope and check every piece of evidence against that exact
   set — no more, no fewer.
2. Take evidence only from the commits themselves and from what the requester
   supplied directly — never execute anything or reach an external system to fill a
   section, and never describe something a diff and a commit message cannot show.
3. Acceptance criteria are optional; when supplied, report only whether the diff
   plausibly touches the claimed area — never claim more than the diff itself shows.
4. Report a provenance mismatch (supplied AC data naming a commit outside the
   packet's set, or covering only some of the commits) at the top of the packet.
5. Evidence each commit separately — never blend multiple commits' diffs into one
   summary that hides which commit changed what.
6. State each commit's rationale only when the message and diff actually support it;
   otherwise, record it as unclear rather than inferring a plausible-sounding reason.
7. Missing evidence is a finding, never a gap to fill with a claim.
8. Scope, integrity, and unclear items come before the change content in the document
   order.
9. Produce the packet even when integrity fails — with the failure first.
10. Commit the packet as an immutable, diffable artifact.
11. Never post to a tracker, transition an issue, or mark anything approved without
    explicit confirmation.

## Bundled files

- `scripts/verify_evidence.py` — integrity checker: provenance agreement between the
  packet's commit set and any supplied AC data, freshness of that data against the
  most recent commit it claims to cover, and per-commit completeness. Reads an
  evidence manifest, emits findings, exits non-zero when integrity fails. No
  dependencies.
- `references/packet-structure.md` — section-by-section contents, the evidence
  manifest schema (including the multi-commit `commits` list), and the failure modes
  each section exists to prevent.
