# Release Management -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Release Management lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Version files | HIGH | `package.json` with version field, `VERSION`, `version.txt`, `pyproject.toml` |
| Changelog file | HIGH | `CHANGELOG.md`, `HISTORY.md`, `RELEASES.md` |
| Release CI/CD configuration | HIGH | GitHub Release workflow, deploy-to-prod pipeline, tag-triggered builds |
| Git tags following version pattern | HIGH | `v1.2.3`, `release/1.2.3`, SemVer or CalVer tags |
| Release branch pattern | MEDIUM | `release/*`, `hotfix/*` branches |
| Environment promotion config | MEDIUM | Staging to production pipeline, environment-specific deploy steps |
| Feature flag configuration | MEDIUM | LaunchDarkly, Unleash, custom feature toggle files |
| Release notes template | LOW | Release note template in `.github/`, changelog generation config |
| Deprecation notices in code | LOW | `@deprecated` annotations, deprecation warnings in logs |

## What to Analyze

### Version Management
- Look for: Versioning scheme (SemVer, CalVer, custom)
- Look for: Version source of truth (package.json, VERSION file, Git tags)
- Look for: Auto-bumping tools (semantic-release, standard-version, release-please)
- Look for: Pre-release tag conventions (alpha, beta, rc)
- Look for: Version consistency across multiple files
- Assess: Whether versioning is disciplined and consistent
- Document: Versioning strategy with scheme, source of truth, auto-bumping, and consistency status

### Changelog Analysis
- Look for: CHANGELOG.md presence and format (Keep a Changelog, conventional, custom)
- Look for: Whether changelog is up to date with latest changes
- Look for: Change categorization (Added, Changed, Fixed, Deprecated, Removed, Security)
- Look for: User-focused language vs. technical jargon
- Look for: Links to issues and PRs in changelog entries
- Look for: Breaking change highlights and migration notes
- Assess: Changelog quality and usefulness for stakeholders
- Document: Changelog assessment with format, freshness, categorization, and quality

### Release Process
- Look for: Release steps (version bump, changelog update, build, test, tag, deploy, announce)
- Look for: Which steps are automated vs. manual
- Look for: Release approval gates (manual approval, QA sign-off, security sign-off)
- Look for: Release artifacts generated (binary, Docker image, documentation, release notes)
- Assess: Release process maturity and automation level
- Document: Release process checklist with automation status per step

### Release Readiness Assessment
- Look for: All tests passing on release branch
- Look for: No critical bugs remaining open
- Look for: Code review completion for included changes
- Look for: Security scan results clean
- Look for: Dependency updates applied
- Look for: Changelog and release notes prepared
- Look for: API documentation updated
- Look for: Staging deployment and testing completed
- Look for: Rollback procedure tested
- Assess: Whether release is ready to go based on checklist
- Document: Release readiness checklist with status per item

### Breaking Changes Analysis
- Look for: API changes that break backward compatibility
- Look for: Database schema changes requiring data migration
- Look for: Configuration changes requiring updates by consumers
- Look for: Deprecation warnings for items being removed
- Assess: Impact of breaking changes on consumers and migration path
- Document: Breaking change inventory with impact, migration steps, and documentation status

### Rollback Strategy
- Look for: Rollback procedure documentation
- Look for: Whether rollback has been tested recently
- Look for: Database rollback capability (reversible migrations)
- Look for: Feature flags enabling quick rollback of behavior
- Look for: Blue-green or canary deployment enabling traffic switch
- Assess: Rollback readiness and confidence level
- Document: Rollback strategy with mechanism, test status, and database reversibility

### Risk Assessment
- Look for: High-risk changes in the release (critical path changes, integration changes)
- Look for: Known issues that ship with the release
- Look for: Monitoring readiness (dashboards, alerts for post-release)
- Assess: Release risk level and whether mitigations are in place
- Document: Risk assessment table with likelihood, impact, and mitigation per risk

### Communication Plan
- Look for: Stakeholder notification channels (engineering, support, customers)
- Look for: Release note format for different audiences
- Look for: Post-release communication process
- Assess: Whether communication is planned or ad-hoc
- Document: Communication plan with stakeholder, channel, timing, and owner

### DoD Compliance for Release Items
- Look for: Whether all included stories have ACs validated
- Look for: Whether no critical defects remain open
- Look for: Whether security concerns are addressed
- Look for: Whether integration behavior is verified
- Look for: Whether test evidence exists
- Look for: Whether user-visible changes are documented in release notes
- Assess: DoD compliance rate for items in the release
- Document: DoD compliance summary with gates and verification status

## Key Questions to Answer

1. What versioning scheme is used and is it consistently applied?
2. Is the changelog up to date and useful for stakeholders?
3. What does the release process look like and how automated is it?
4. Is the release ready based on code, documentation, and deployment criteria?
5. Are there breaking changes and is there a migration path?
6. What is the rollback strategy and has it been tested?
7. What risks does this release carry?
8. How are stakeholders notified about releases?
9. Do all included items meet Definition of Done criteria?
10. What release process improvements would reduce risk and effort?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Semantic Versioning | SemVer tags, version bumps matching change type | Clear version meaning, consumer trust |
| Automated Release | semantic-release, release-please, CI-triggered publish | Consistent, low-effort releases |
| Manual Release | Release checklist in docs, manual version bumps | Error-prone, but may suit low-frequency releases |
| Trunk-Based Release | Deploy from main, feature flags for incomplete work | Fast releases, requires strong testing |
| Release Branch Strategy | `release/*` branches, cherry-picks, parallel maintenance | Controlled releases, but complex branching |
| Continuous Deployment | Every merge deploys to production | Fast feedback, requires strong testing and monitoring |
| Scheduled Releases | Fixed cadence (weekly, bi-weekly, monthly) | Predictable, but may batch risky changes |
| Hotfix Process | `hotfix/*` branches, expedited review/deploy | Fast fixes, needs clear criteria |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No versioning strategy | No version files, no Git tags | HIGH |
| No changelog | Missing CHANGELOG.md, no release notes | MEDIUM |
| No rollback strategy | No rollback docs, no tested procedure | HIGH |
| Manual-only release process | No automation, fully manual deploy | MEDIUM |
| No staging environment | Direct deploy to production without staging test | HIGH |
| Breaking changes without migration guide | API changes without consumer migration documentation | HIGH |
| No post-release monitoring | No dashboards, no alerts watching release health | MEDIUM |
| No release approval gate | Anyone can deploy without QA/security sign-off | MEDIUM |
| Inconsistent version across files | Different versions in package.json, Docker tag, docs | LOW |
| No deprecation warning period | Features removed without deprecation notices | MEDIUM |

## Output Guidance

### Must Include
- Versioning strategy with scheme, source of truth, and consistency status
- Changelog assessment with format, freshness, and quality
- Release process overview with automation level per step
- Release readiness checklist with status per criterion
- Rollback strategy with mechanism and test status

### Should Include (if detected)
- Breaking changes inventory with migration paths
- Risk assessment for upcoming release
- DoD compliance summary for release items
- Communication plan for stakeholders
- Release process improvement recommendations

### Related Areas
- [devops-infrastructure](./devops-infrastructure.md) -- CI/CD pipeline, deployment strategy, environment management
- [delivery-management](./delivery-management.md) -- deployment frequency, change failure rate
- [security](./security.md) -- security gates before release, vulnerability status
- [quality-assurance](./quality-assurance.md) -- test readiness, coverage status
- [technical-writing](./technical-writing.md) -- changelog, release notes, migration guides
- [support-engineering](./support-engineering.md) -- known issues, post-release support preparation
