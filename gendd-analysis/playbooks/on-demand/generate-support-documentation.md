# Generate Support Documentation

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | Support Engineer, Technical Writer |
| **Prerequisites** | Repository cloned, brownfield analysis or system documentation available |
| **Inputs** | Path to the target repository, existing system documentation |
| **Outputs** | Troubleshooting guides, FAQ, known issues document |

## When to Use

- Support team is onboarding onto a product and needs troubleshooting materials
- After a major release that introduces new features or changes behavior
- When recurring support tickets indicate missing documentation

## Before You Start

- [ ] Repository is cloned and accessible
- [ ] System documentation exists (brownfield analysis or equivalent)
- [ ] You have access to known issues or common support tickets (if available)

## Steps

1. **Gather existing context**
   - Do: Review system documentation and identify user-facing components
   - How: Read `@TargetRepo/docs/brownfield/gendd/` (the documentation pack — start with `gendd/overview/system-summary.md`) or equivalent. Identify entry points, error handling patterns, and user-facing flows.
   - Expect: Understanding of the system's surface area from a support perspective

2. **Run the Support Engineer role-playbook analysis**
   - Do: Generate support-oriented documentation
   - How: Use the following prompt:
     ```
     Read @GenDD-Flow/playbooks/by-role/support-engineer.md

     Analyze @TargetRepo focusing on supportability.

     Generate:
     1. Troubleshooting guide (common error scenarios with resolution steps)
     2. FAQ document (based on system behavior and edge cases)
     3. Known issues and workarounds
     4. Error code / message reference
     5. Escalation path recommendations
     ```
   - Expect: A set of support-ready documents

3. **Save and organize**
   - Do: Save outputs in a support-specific docs folder
   - How: Save to `@TargetRepo/docs/support/`
   - Expect: Organized support documentation ready for the team

## Expected Output

```
TargetRepo/docs/support/
├── troubleshooting-guide.md
├── faq.md
└── known-issues.md
```

**Save to:** `@TargetRepo/docs/support/`

## What's Next

- [ ] [Update Documentation Incrementally](../recurring/update-documentation.md) to keep support docs current
- [ ] [Run Brownfield Analysis](../onboarding/run-brownfield-analysis.md) if system docs don't exist yet

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| Support Engineer Role Playbook | `playbooks/by-role/support-engineer.md` | Deep-dive support analysis prompt |
| Technical Writer Role Playbook | `playbooks/by-role/technical-writer.md` | Documentation quality prompt |
