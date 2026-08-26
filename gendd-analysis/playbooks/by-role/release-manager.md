# Role Playbook: Release Manager

**Role:** Release Manager
**Focus:** Release checklist, changelog, version strategy, release readiness, DoD verification
**Time:** 30-45 minutes

---

## Purpose

Analyze a codebase from a Release Manager perspective to understand:
- Release readiness and blockers
- Version management strategy
- Changelog maintenance
- Release process and automation
- Definition of Done compliance for release items

---

## {ORGANIZATION} Release Standards

> **Reference:** This playbook aligns with {ORGANIZATION}'s **Story Templates** and **Definition of Done** standards.

### Definition of Done Requirements for Release

Before release, verify all included stories meet DoD:

| DoD Criterion | Release Gate | Verification |
|---------------|--------------|--------------|
| All ACs validated | Required | QA sign-off |
| No critical defects remain | Required | Bug triage |
| Security concerns addressed | Required | Security sign-off |
| Integration behavior verified | Required | Integration tests pass |
| Test evidence exists | Required | Test reports |
| User-visible changes documented | Required | Release notes |

### Release Notes from Story Templates

Stories should include Release Notes (optional field) for user-visible behavior changes. Aggregate these for release:

| Story | User-Visible Change | Release Note |
|-------|---------------------|--------------|
| [Story ID] | [Description] | [User-facing summary] |

### Common Release Failure Modes

| Failure Mode | Root Cause | Prevention |
|--------------|------------|------------|
| Reverts after release | Undocumented integration behavior | Verify Integration Impact flag addressed |
| Security blocks release | Security discovered late | Verify Security flag addressed in DoD |
| Incomplete release notes | Stories lack Release Notes field | Collect during DoD verification |
| QA discovers issues post-release | ACs not properly validated | Verify test evidence exists |

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/release-manager.md
Analyze @TargetRepo for release readiness.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/release-manager.md

Analyze @TargetRepo from a Release Manager perspective:

## Context
- Versioning: [SemVer | CalVer | Custom]
- Release Cadence: [Weekly | Bi-weekly | Monthly | On-demand]
- Environments: [Dev → Staging → Prod]
- Current Version: [X.Y.Z]

## Phase 1: Version Management

### Versioning Strategy
| Aspect | Implementation | Status |
|--------|----------------|--------|
| Version scheme | [SemVer/CalVer] | Consistent/Inconsistent |
| Version location | [package.json/etc] | [files] |
| Auto-bumping | Yes/No | [tool] |
| Pre-release tags | [alpha/beta/rc] | [pattern] |

### Version Consistency
| Location | Version | In Sync |
|----------|---------|---------|
| [package.json] | [version] | Yes/No |
| [pyproject.toml] | [version] | Yes/No |
| [VERSION file] | [version] | Yes/No |

## Phase 2: Changelog Analysis

### Changelog Status
| Aspect | Status | Quality |
|--------|--------|---------|
| CHANGELOG.md exists | Yes/No | - |
| Format | [Keep a Changelog/Custom] | Good/Fair/Poor |
| Up to date | Yes/No | [last entry date] |
| Categorized | Yes/No | [categories used] |

### Recent Changes (Unreleased)
| Category | Count | Examples |
|----------|-------|----------|
| Added | [n] | [features] |
| Changed | [n] | [changes] |
| Fixed | [n] | [fixes] |
| Deprecated | [n] | [items] |
| Removed | [n] | [items] |
| Security | [n] | [fixes] |

### Changelog Quality
| Check | Status | Issues |
|-------|--------|--------|
| User-focused language | Yes/No | [examples] |
| Links to issues/PRs | Yes/No | [coverage] |
| Breaking changes highlighted | Yes/No | [issues] |
| Migration notes included | Yes/No | [issues] |

## Phase 3: Release Process

### Current Process
| Step | Automated | Tool | Documentation |
|------|-----------|------|---------------|
| Version bump | Yes/No | [tool] | [link] |
| Changelog update | Yes/No | [tool] | [link] |
| Build | Yes/No | [CI] | [link] |
| Test | Yes/No | [CI] | [link] |
| Tag | Yes/No | [tool] | [link] |
| Deploy | Yes/No | [tool] | [link] |
| Announce | Yes/No | [tool] | [link] |

### Release Artifacts
| Artifact | Generated | Location |
|----------|-----------|----------|
| Binary/Package | Yes/No | [location] |
| Docker image | Yes/No | [registry] |
| Documentation | Yes/No | [location] |
| Release notes | Yes/No | [location] |

## Phase 4: Release Readiness Assessment

### Code Readiness
| Check | Status | Blocker |
|-------|--------|---------|
| All tests passing | Yes/No | [if No] |
| No critical bugs | Yes/No | [list] |
| Code review complete | Yes/No | [pending PRs] |
| Security scan clean | Yes/No | [issues] |
| Dependency updates | Yes/No | [outdated] |

### Documentation Readiness
| Check | Status | Blocker |
|-------|--------|---------|
| Changelog updated | Yes/No | |
| Release notes drafted | Yes/No | |
| API docs updated | Yes/No | |
| Migration guide (if needed) | Yes/No/NA | |

### Deployment Readiness
| Check | Status | Notes |
|-------|--------|-------|
| Staging deployed | Yes/No | [version] |
| Staging tested | Yes/No | [coverage] |
| Rollback tested | Yes/No | [last test] |
| Monitoring ready | Yes/No | [dashboards] |

## Phase 5: Breaking Changes Analysis

### Identified Breaking Changes
| Change | Impact | Migration | Documented |
|--------|--------|-----------|------------|
| [Change] | [Who affected] | [Steps] | Yes/No |

### Deprecations
| Item | Deprecated In | Remove In | Alternative |
|------|---------------|-----------|-------------|
| [Item] | [version] | [version] | [replacement] |

## Phase 6: Risk Assessment

### Release Risks
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Action] |

### Rollback Plan
| Aspect | Status |
|--------|--------|
| Rollback procedure documented | Yes/No |
| Rollback tested | Yes/No |
| Database rollback possible | Yes/No |
| Feature flags in place | Yes/No |

## Phase 7: Communication Plan

### Stakeholder Notification
| Stakeholder | Notification | Timing | Owner |
|-------------|--------------|--------|-------|
| Engineering | [channel] | [when] | [who] |
| Support | [channel] | [when] | [who] |
| Customers | [channel] | [when] | [who] |

## Phase 8: Recommendations

### Release Blockers (Must Fix)
| Issue | Impact | Owner | ETA |
|-------|--------|-------|-----|
| [Issue] | [Impact] | [Owner] | [Date] |

### Process Improvements
| Improvement | Benefit | Effort |
|-------------|---------|--------|
| [Improvement] | [Benefit] | [S/M/L] |
```

---

## Output: Release Readiness Report

```markdown
# Release Readiness Report: [Project Name]
Version: [X.Y.Z]
Generated: [Date]
Analyzed by: Release Manager Playbook

## Release Status: [GO / NO-GO / CONDITIONAL]

## Version Info
- **Current:** [version]
- **Proposed:** [version]
- **Type:** [Major/Minor/Patch]

## Readiness Checklist

### Code
- [x] All tests passing
- [x] No critical bugs
- [ ] Security scan clean (2 medium issues)

### Documentation
- [x] Changelog updated
- [ ] Migration guide needed

### Deployment
- [x] Staging deployed
- [x] Staging tested
- [ ] Rollback tested (last: 30 days ago)

## Changes Summary

### Added
- [Feature 1]
- [Feature 2]

### Changed
- [Change 1]

### Fixed
- [Fix 1]

### Breaking Changes
| Change | Migration |
|--------|-----------|
| [Change] | [Steps] |

## Blockers

### Must Fix Before Release
1. [Blocker 1] - Owner: [name], ETA: [date]

### Known Issues (Ship With)
1. [Issue] - Workaround: [workaround]

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | Med | High | [Action] |

## Release Checklist

### Pre-Release
- [ ] Version bump
- [ ] Changelog finalized
- [ ] Tag created
- [ ] Release notes drafted

### Release Day
- [ ] Final staging verification
- [ ] Production deploy
- [ ] Smoke tests
- [ ] Monitoring verified

### Post-Release
- [ ] Announcement sent
- [ ] Documentation published
- [ ] Support team notified

## Approval

| Role | Approver | Status |
|------|----------|--------|
| Tech Lead | [Name] | Pending/Approved |
| QA | [Name] | Pending/Approved |
| Product | [Name] | Pending/Approved |
```

---

## Follow-Up Actions

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
