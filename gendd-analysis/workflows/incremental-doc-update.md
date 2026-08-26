# Workflow: Incremental Documentation Update

**Purpose:** Update only affected documentation sections after code changes, avoiding full brownfield re-analysis.

---

## When to Use

- After a PR is merged
- After a release
- When documentation drift is detected
- During regular maintenance cycles

**Do NOT use when:**
- Repository has no existing documentation (use full brownfield instead)
- Major architectural changes occurred (use full brownfield instead)
- More than 30% of codebase changed (use full brownfield instead)

---

## Workflow Overview

```
┌─────────────────┐
│ 1. Delta        │
│    Analysis     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. Map Changes  │
│    to Docs      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. Targeted     │
│    Pass 1/2     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. Update       │
│    Specific Docs│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 5. Validate     │
│    Changes      │
└─────────────────┘
```

---

## Step 1: Run Delta Analysis

```
Read @GenDD-Flow/playbooks/on-demand/run-delta-analysis.md

Analyze @TargetRepo for changes since [LAST_DOCUMENTED_STATE]:
- Base: [main | last release tag | commit SHA]
- Head: [current | feature branch]

Generate:
1. Changed files categorized by type
2. Impact assessment per change
3. Documentation sections affected
```

**Output:** `@TargetRepo/docs/updates/delta-[date].md`

---

## Step 2: Map Changes to Documentation Sections

Using delta analysis output, create mapping:

```
Read the delta analysis at @TargetRepo/docs/updates/delta-[date].md

Create documentation update mapping:

| Changed Component | Existing Doc File | Section | Update Type |
|-------------------|-------------------|---------|-------------|
| [Component] | [doc file path] | [section] | Add/Modify/Remove |

Categorize updates:
- **Critical:** Breaking changes, removed features, security updates
- **Important:** New features, significant changes
- **Minor:** Typos, small corrections, clarifications
```

---

## Step 3: Run Targeted Pass 1/2 on Affected Areas

Only analyze changed components, not entire repository:

### For Service Changes
```
Read @GenDD-Flow/agents/pass2-infer-agent.md

Analyze ONLY these changed services in @TargetRepo:
- @TargetRepo/src/services/[ChangedService1]
- @TargetRepo/src/services/[ChangedService2]

Using existing documentation at @TargetRepo/docs/brownfield/ as baseline,
generate updated:
1. Service descriptions
2. Dependency changes
3. Flow modifications
4. Risk assessment for changes
```

### For API Changes
```
Read @GenDD-Flow/agents/pass2-infer-agent.md

Analyze ONLY these changed APIs in @TargetRepo:
- @TargetRepo/src/api/[ChangedEndpoint]

Generate updated:
1. Endpoint documentation
2. Request/response changes
3. Breaking change notes
```

### For Data Model Changes
```
Read @GenDD-Flow/agents/pass2-infer-agent.md

Analyze ONLY these schema changes in @TargetRepo:
- @TargetRepo/migrations/[NewMigration]
- @TargetRepo/models/[ChangedModel]

Generate updated:
1. Entity relationship changes
2. Data ownership updates
3. Migration notes
```

---

## Step 4: Update Specific Documentation Files

### Update Pattern

For each affected documentation file:

```
Read @GenDD-Flow/templates/documentation-guidelines.md

Update @TargetRepo/docs/[affected-file].md:

## Changes from Delta Analysis
[Reference delta analysis findings]

## Specific Updates

### Section: [Section Name]
**Previous:** [Brief description of what was documented]
**Now:** [Updated description based on code changes]
**Changed Files:** [File references]

### Section: [Another Section]
...

## Validation
- [ ] All file references are current
- [ ] No stale code snippets (use file refs instead)
- [ ] Patterns used instead of hard-coded counts
- [ ] Cross-references updated
```

### File-Specific Update Templates

#### Architecture Documentation
```
Update @TargetRepo/docs/architecture/components.md:

Component: [Component Name]
- Description: [Updated based on changes]
- Dependencies: [Updated list]
- Key files: `src/services/[Service].cs`, `src/models/[Model].cs`
- Changed in: [PR/commit reference]
```

#### Flow Documentation
```
Update @TargetRepo/docs/flows/[flow-name].md:

## Flow: [Flow Name]

### Steps (Updated)
1. [Step] - See `[file:function]`
2. [Step] - See `[file:function]`
...

### Changes from Previous
- Added: [new steps]
- Modified: [changed steps]
- Removed: [deprecated steps]
```

#### Risk Documentation
```
Update @TargetRepo/docs/risks/risk-hotspots.md:

### New Risks Identified
| Risk | Location | Severity | Mitigation |
|------|----------|----------|------------|
| [Risk] | `[file]` | High/Med/Low | [Action] |

### Resolved Risks
- [Risk] - Addressed in [PR/commit]
```

---

## Step 5: Validate Documentation Updates

```
Read @GenDD-Flow/templates/documentation-guidelines.md

Validate updates to @TargetRepo/docs/:

## Checklist

### Content Accuracy
- [ ] All file references exist and are correct
- [ ] No outdated code snippets embedded
- [ ] Patterns match actual file structure
- [ ] Cross-references point to valid sections

### Completeness
- [ ] All critical changes documented
- [ ] Breaking changes highlighted
- [ ] Migration steps included if needed
- [ ] New features have examples

### Format Compliance
- [ ] Files under size limits
- [ ] One concept per file
- [ ] Proper markdown formatting
- [ ] Consistent heading structure
```

---

## Quick Incremental Update Prompt

For simple updates, use this single prompt:

```
Read @GenDD-Flow/workflows/incremental-doc-update.md
Read @GenDD-Flow/playbooks/on-demand/run-delta-analysis.md

Perform incremental documentation update for @TargetRepo:

Changes since: [BASELINE - commit/tag/branch]

1. Run delta analysis to identify changes
2. Map changes to existing documentation
3. Update only affected sections
4. Validate updates follow documentation guidelines

Existing docs location: @TargetRepo/docs/
Output changes to: @TargetRepo/docs/updates/
```

---

## Output Structure

After incremental update:

```
TargetRepo/docs/
├── updates/
│   └── delta-[date].md           # Delta analysis record
│
├── brownfield/                   # Updated files (if needed)
│   ├── ...existing files...
│   └── CHANGELOG.md              # Update history
│
├── architecture/                 # Updated architecture docs
├── flows/                        # Updated flow docs
└── risks/                        # Updated risk docs
```

---

## Automation Hooks

### Git Hook (post-merge)
```bash
#!/bin/bash
# .git/hooks/post-merge

# Check if significant code changes
CHANGED=$(git diff --name-only HEAD~1 HEAD | grep -E '\.(ts|js|py|go|cs|java)$' | wc -l)

if [ "$CHANGED" -gt 5 ]; then
  echo "Significant code changes detected. Consider running:"
  echo "Read @GenDD-Flow/workflows/incremental-doc-update.md"
fi
```

### PR Template Addition
```markdown
## Documentation Impact

<!-- Run delta analysis if significant changes -->
- [ ] Ran `@GenDD-Flow/playbooks/on-demand/run-delta-analysis.md`
- [ ] Updated affected documentation
- [ ] No documentation changes needed (explain why)
```

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| `playbooks/on-demand/run-delta-analysis.md` | Change impact analysis |
| `playbooks/onboarding/run-brownfield-analysis.md` | Full repository analysis |
| `templates/documentation-guidelines.md` | Output formatting rules |
| `playbooks/PLAYBOOK-GUIDE.md` | When to use which playbook |
