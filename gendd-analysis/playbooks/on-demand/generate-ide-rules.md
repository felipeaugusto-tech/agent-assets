# Generate IDE Rules

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Prerequisites** | `docs/context/` must exist in the target repository (run full analysis first if not) |
| **Inputs** | Path to the target repository (`@TargetRepo`), target IDE name |
| **Outputs** | IDE-specific agent rule files in the appropriate location |

## When to Use

- Switching to a different IDE and need rules in that IDE's format
- Your IDE updated its rule format and existing rules are outdated
- You want to refresh IDE rules after updating context or standards
- Setting up a new team member's IDE with the correct rules
- Adding a second IDE alongside an existing one

## Supported IDEs

| IDE | Rule Location | Format |
|-----|--------------|--------|
| Cursor | `.cursor/rules.md` | Markdown |
| Claude Code | `.claude/` | Markdown |
| Antigravity | `.antigravity/` | Markdown |
| GitHub Copilot | `.github/copilot/` | YAML/Markdown |
| Other | Varies | Varies |

## Before You Start

- [ ] Target repository has `docs/context/` with context area files
- [ ] (Optional) Target repository has `docs/standards/` with standards files
- [ ] You know which IDE to generate rules for
- [ ] GenDD-Flow repo is available at a known path

> **Missing context?** Run [Full Analysis](../onboarding/run-full-analysis.md) first, or at minimum Phases 2-3 to generate context areas.

## Steps

### Step 1: Verify context exists

- Do: Confirm that context documents are available
- How: Check that `@TargetRepo/docs/context/` contains area files
- Expect: One or more `.md` files in the context directory

### Step 2: Generate IDE rules

- Do: Transform context and standards into IDE-specific rule files
- How: Use the following prompt:
  ```
  Read @GenDD-Flow/workflows/generate-ide-rules.md

  Using the context at @TargetRepo/docs/context/
  and standards at @TargetRepo/docs/standards/ (if available),
  generate IDE-specific rules for: [YOUR IDE]

  Target IDE: [Cursor / Claude Code / Antigravity / Copilot / Other]

  The rules should:
  1. Reference context areas for domain knowledge
  2. Enforce coding standards and conventions
  3. Include security and compliance constraints
  4. Follow the IDE's native rule format
  5. Be concise enough for the IDE's context window

  Save to the appropriate location for the target IDE.
  ```
- Expect: Rule files in the correct IDE-specific location

### Step 3: Validate rules

- Do: Test that the IDE picks up the rules correctly
- How: Open the target IDE, start a new conversation, and ask it to generate code. Verify it follows the rules.
- Expect: AI-generated code that reflects the conventions and constraints from the rules

### Step 4: Generate for additional IDEs (optional)

- Do: Repeat Step 2 for any other IDEs your team uses
- How: Run the same prompt with a different target IDE
- Expect: Each IDE has its own rule files in the correct location

## Expected Output

```
TargetRepo/
├── .cursor/              # If targeting Cursor
│   └── rules.md
├── .claude/              # If targeting Claude Code
│   └── rules.md
├── .antigravity/         # If targeting Antigravity
│   └── rules.md
└── .github/copilot/      # If targeting Copilot
    └── rules.md
```

**Save to:** IDE-specific directory in `@TargetRepo/`

## What's Next

- [ ] [Refresh Context Areas](../recurring/refresh-context-areas.md) when context becomes outdated
- [ ] [Generate Standards](generate-standards.md) if standards are missing
- [ ] Share the IDE rule location with team members

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Generate IDE Rules Workflow | `workflows/generate-ide-rules.md` | Detailed workflow for rule generation |
| Full Analysis Playbook | `playbooks/onboarding/run-full-analysis.md` | Generates the context that rules depend on |
| Context Area Template | `templates/context-area.md` | Template for context documents |
