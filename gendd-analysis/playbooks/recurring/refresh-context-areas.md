# Refresh Context Areas

| Field | Value |
|-------|-------|
| **Category** | recurring |
| **Frequency** | Quarterly or after major changes |
| **Prerequisites** | Existing `docs/context/` folder from a previous full analysis, GenDD-Flow repo available |
| **Inputs** | Path to target repository (`@TargetRepo`), list of changes since last refresh |
| **Outputs** | Updated `docs/context/` files, updated `docs/standards/` (if applicable), regenerated IDE rules |

## When to Use

- Context area documents are outdated (quarterly check)
- Major features shipped that changed architecture or patterns
- Team conventions changed (new frameworks, refactored patterns)
- New SDLC areas emerged that were not previously documented
- IDE rules are producing inaccurate suggestions due to stale context
- After a significant refactor or migration

## Before You Start

- [ ] Existing context area files are in `@TargetRepo/docs/context/`
- [ ] You know what changed since the last refresh
- [ ] You have access to the codebase to verify current patterns
- [ ] GenDD-Flow repo is available at a known path

## Steps

### Step 1: Identify stale areas

- Do: Determine which context areas need updating
- How: Review changes since last refresh and map to context files:
  ```
  Review the context area files at @TargetRepo/docs/context/
  and compare them against the current codebase.

  Identify:
  1. Areas that have changed significantly
  2. New areas that should be documented
  3. Areas that are no longer relevant
  4. Specific files/sections that are outdated

  List each finding with the affected context file and what needs to change.
  ```
- Expect: A prioritized list of areas that need attention

### Step 2: Re-detect context areas

- Do: Run area detection to catch any new or removed areas
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/analyze-and-generate.md

  Re-detect SDLC context areas for @TargetRepo.
  Compare against existing areas in @TargetRepo/docs/context/.

  Identify:
  1. New areas that should be added
  2. Existing areas that should be removed or merged
  3. Areas that need significant rewriting vs. minor updates
  ```
- Expect: Updated list of applicable context areas

### Step 3: Regenerate affected context files

- Do: Update or regenerate context documents for changed areas
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/generate-context-areas.md

  Refresh the following context areas at @TargetRepo/docs/context/:
  - [LIST AREAS TO UPDATE]

  Changes since last refresh:
  - [LIST KEY CHANGES]

  For each area:
  1. Preserve accurate existing content
  2. Update outdated information
  3. Add new patterns discovered in the codebase
  4. Remove references to deprecated code
  5. Use actual file references from the current codebase

  Save updated files to @TargetRepo/docs/context/
  ```
- Expect: Updated context files reflecting the current state of the codebase

### Step 4: Update standards (if needed)

- Do: Refresh standards documents if conventions changed
- How: If standards exist at `@TargetRepo/docs/standards/`, review and update them to match the refreshed context
  ```
  Read @GenDD-Flow/workflows/detect-and-generate-standards.md

  Review standards at @TargetRepo/docs/standards/ against
  the refreshed context at @TargetRepo/docs/context/.

  Update any standards that are now outdated or inconsistent
  with the current codebase patterns.
  ```
- Expect: Standards aligned with refreshed context

### Step 5: Regenerate IDE rules

- Do: Regenerate IDE-specific rules from the updated context and standards
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/generate-ide-rules.md

  Regenerate IDE rules using the refreshed context at @TargetRepo/docs/context/
  and standards at @TargetRepo/docs/standards/.

  Target IDE: [YOUR IDE]

  Save to the appropriate location.
  ```
- Expect: IDE rules that reflect the refreshed context

### Step 6: Validate and communicate

- Do: Test that the refreshed context produces accurate AI output
- How: Open your IDE, start a new conversation, and ask it to generate code. Verify it follows the updated conventions.
- Expect: AI-generated code that matches current patterns
- Do: Commit changes and notify the team
- How: Commit with a clear message noting what was refreshed, and inform team members of any convention changes

## Expected Output

```
@TargetRepo/
├── docs/
│   ├── context/            # Updated context area files
│   │   ├── architecture.md
│   │   ├── testing.md
│   │   └── {area}.md
│   └── standards/          # Updated standards (if applicable)
│       └── {area}.md
└── .cursor/                # Regenerated IDE rules (or IDE-specific location)
    └── rules.md
```

**Save to:** `@TargetRepo/docs/context/`, `@TargetRepo/docs/standards/`, and IDE-specific rule location

## What's Next

- [ ] [Generate IDE Rules](../on-demand/generate-ide-rules.md) for additional IDEs if needed
- [ ] [Generate Architecture Diagrams](../on-demand/generate-architecture-diagrams.md) if architecture context changed
- [ ] [Update Documentation](update-documentation.md) for broader documentation refresh
- [ ] Schedule next refresh (quarterly or after next major change)

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Full Analysis Playbook | `playbooks/onboarding/run-full-analysis.md` | Initial 5-phase analysis |
| Generate Context Areas | `workflows/generate-context-areas.md` | Context document generation workflow |
| Generate IDE Rules | `workflows/generate-ide-rules.md` | IDE rule generation workflow |
| Detect & Generate Standards | `workflows/detect-and-generate-standards.md` | Standards generation workflow |
