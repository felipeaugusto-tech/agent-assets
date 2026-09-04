# Packet Structure

1. Section-by-section contents
2. The evidence manifest schema
3. Document order, and why

---

## 1. Section-by-section contents

Each section exists to prevent a specific failure. When a section has nothing to say,
mark it not applicable **with a reason** — an empty section and an absent one look
identical to a reviewer, and neither prompts a question.

This is a commit-only packet: it reads commit metadata and diffs, and does not
execute anything or reach an external system for evidence. Only two things feed it —
the commit(s) themselves, and acceptance criteria if the requester supplies them. A
packet can cover one commit or several; nothing about the structure changes, except
that "commit identity" and "change content" repeat per commit.

### Commit identity

One entry per commit: SHA, author, committer timestamp, parent(s), and any tag or
branch it's reachable from. Version, release name, and target environment are
recorded once at the packet level, if the requester named them.

*Prevents:* describing something other than what was actually asked about. Every
other section is checked against the exact commit set named here, so it comes first
and it is not optional — and with multiple commits, "exact set" matters even more,
since AC data or a stray reference can quietly apply to only part of it.

### Scope of this packet

A short statement that evidence is limited to these commits' own diffs and metadata,
plus any acceptance criteria supplied, and that anything not derivable from those is
out of scope.

*Prevents:* the packet's boundary reading as an oversight rather than as a deliberate
choice. State it before anyone has a chance to assume the packet covers more than it
does.

### Integrity

The result of `verify_evidence.py`: provenance agreement between the commit set and
any supplied AC data, freshness of that data, completeness.

*Prevents:* a packet whose parts describe a different set of commits than intended —
including the partial-overlap case, where AC data covers three of five commits and
silently reads as covering all five.

### Change content

The diff each commit introduces, evidenced **separately per commit**: files touched,
insertion/deletion counts, anything structural (migrations, config changes,
dependency-manifest changes, feature flags), ticket references pulled from that
commit's message, and the rationale as evidenced by the message and the diff itself.

*Prevents:* a reader who does not know what a commit actually did, or why — and,
specific to a multi-commit packet, losing track of which commit introduced which
change. Call out migrations explicitly; they are the changes hardest to undo.
Enumerate files the way a reviewer would; a loose summary invites a skim, and a
blended summary across commits actively hides information.

### Acceptance criteria

Only present if the requester supplied AC data. Each item is checked against the
combined diff across all commits for whether a file or hunk in any of them plausibly
addresses it, and which commit. If nothing was supplied, this section is
`{"not_applicable": true, "reason": "..."}`.

*Prevents:* a claim this packet has no basis to make. "The diff touches this area, in
commit X" is a narrower, more honest statement than "this criterion is satisfied,"
and conflating the two is the easiest way to overclaim.

### Unclear

Commits whose rationale the message and diff don't actually support — a bare "fix"
with no context, a diff touching files unrelated to what the message describes, no
ticket reference to check against.

*Prevents:* a guessed rationale being presented as established fact. "Intent not
evidenced by this commit" is a legitimate and useful finding, and it's the honest
alternative to inventing a plausible-sounding reason.

---

## 2. Evidence manifest schema

Input to `verify_evidence.py`. The commit set is the anchor: `commits` is a list, one
entry per commit, each with its own identity and its own `change_content`. Anything
else supplied (right now, that's only acceptance-criteria data) names which commit(s)
it describes and when it was produced — those fields are the entire basis of the
provenance and freshness checks, and supplied data without them cannot be verified at
all.

```json
{
  "release": {
    "name": "Release 42",
    "version": "42.0.0",
    "environment": "production"
  },
  "commits": [
    { "commit": "a1b2c3d4e5f6",
      "committed_at": "2026-08-09T18:00:00Z",
      "author": "J. Alvarez <j.alvarez@co>",
      "parents": ["9f8e7d6"],
      "reachable_from": ["main"],
      "change_content": {
        "files_changed": 4, "insertions": 102, "deletions": 30,
        "migrations": ["1720-add-tenant-id"], "tickets": ["PROJ-448"],
        "rationale": "Commit message references PROJ-448 (\"add tenant isolation to session lookup\"); the migration and the scoping change both support that stated intent.",
        "files": [
          { "path": "db/migrations/1720-add-tenant-id.sql",
            "change": "new migration, adds tenant_id column" },
          { "path": "services/auth/session.py",
            "change": "tenant scoping added to session lookup" }
        ]
      } },
    { "commit": "77e2f1099999",
      "committed_at": "2026-08-11T09:00:00Z",
      "author": "M. Singh <m.singh@co>",
      "parents": ["a1b2c3d4e5f6"],
      "reachable_from": ["main", "v42.0.0"],
      "change_content": {
        "files_changed": 2, "insertions": 40, "deletions": 8,
        "migrations": [], "tickets": ["PROJ-455"],
        "rationale": "Follows directly from a1b2c3d4e5f6 — closes a gap in the same scoping logic; message and diff agree.",
        "files": [
          { "path": "services/auth/session_scope.py",
            "change": "new helper extracting the tenant-scope predicate" },
          { "path": "services/auth/session.py",
            "change": "follow-up fix to the tenant-scoping check" }
        ]
      } }
  ],
  "artifacts": [
    { "name": "Acceptance criteria matrix", "path": "docs/traceability/release-42.md",
      "commits": ["a1b2c3d", "77e2f10"], "produced_at": "2026-08-12T14:10:00Z" }
  ],
  "acceptance_criteria": {
    "supplied": 2,
    "items": [
      { "id": "PROJ-448-AC-1", "diff_touches_claimed_area": true,
        "commits": ["a1b2c3d"], "files": ["services/auth/session.py"] },
      { "id": "PROJ-448-AC-2", "diff_touches_claimed_area": false }
    ]
  },
  "unclear": [
    { "commit": "9f8e7d6",
      "reason": "No message beyond \"fix\"; diff touches files unrelated to any stated intent." }
  ]
}
```

For a single-commit packet, `commits` is just a one-element list — the shape doesn't
change, there's simply one entry instead of several.

An artifact may name one commit with `"commit": "..."` or several with
`"commits": [...]`; both are accepted. Every commit an artifact names must appear in
the packet's own `commits` list, or it's a provenance mismatch — including the
partial-coverage case, where an artifact should cover all the packet's commits but
only names some of them.

When no acceptance criteria are supplied, use:

```json
"acceptance_criteria": { "not_applicable": true,
                         "reason": "no acceptance criteria provided with the request" },
"artifacts": []
```

Short and long SHAs compare equal, so `a1b2c3d` matches `a1b2c3d4e5f6`. A section may
be `{"not_applicable": true, "reason": "..."}` — the reason is required, because "N/A"
with no explanation is indistinguishable from an oversight.

The schema has no keys for evidence a commit cannot establish on its own. Anything
that would require executing something or reaching an external system is outside this
packet by design. If a requester hands over that kind of evidence anyway, treat it as
an explicit expansion of scope and say so — don't fold it in silently under
`change_content` or `acceptance_criteria`.

---

## 3. Document order, and why

```
1. Commit identity (one entry per commit)
2. Scope of this packet
3. Integrity result
4. Change content, with rationale (one entry per commit)
5. Acceptance criteria (or not applicable, with reason)
6. Unclear
```

Readers read the top of a document and skim the rest. A commit-only packet has to
earn its narrower scope by stating it early — put the boundary and the integrity
result where they will actually be seen, before the diff content that might
otherwise read as more complete than it is. With multiple commits, keep each one's
change content as its own subsection rather than merging them; a merged view is
exactly the kind of blending this packet exists to avoid.
