# Audit CI/CD Pipeline

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | DevOps Engineer, SRE, Tech Lead |
| **Prerequisites** | Repository cloned, access to CI/CD configuration files |
| **Inputs** | Path to the target repository |
| **Outputs** | CI/CD audit report covering pipeline structure, deployment patterns, and improvement recommendations |

## When to Use

- Onboarding onto a project and need to understand the deployment pipeline
- Reviewing CI/CD configuration for reliability, speed, or security improvements
- Preparing for a migration to a new CI/CD platform

## Before You Start

- [ ] Repository is cloned and accessible
- [ ] You can identify CI/CD config files (GitHub Actions, Azure DevOps, Jenkins, etc.)
- [ ] You have access to deployment environment documentation (if any)

## Steps

1. **Identify CI/CD configuration**
   - Do: Locate all pipeline and deployment configuration files
   - How: Search for `.github/workflows/`, `azure-pipelines.yml`, `Jenkinsfile`, `Dockerfile`, `docker-compose.yml`, Terraform/Pulumi files, Helm charts
   - Expect: A complete inventory of CI/CD and infrastructure-as-code files

2. **Run the DevOps role-playbook analysis**
   - Do: Perform a role-specific deep analysis of the CI/CD layer
   - How: Use the following prompt:
     ```
     Read @GenDD-Flow/playbooks/by-role/devops-engineer.md

     Analyze @TargetRepo focusing on CI/CD and deployment infrastructure.

     Generate:
     1. Pipeline inventory (build, test, deploy stages)
     2. Deployment pattern (blue-green, rolling, canary, etc.)
     3. Environment map (dev, staging, prod)
     4. Secret management approach
     5. Build performance analysis (caching, parallelism)
     6. Security scan integration (SAST, DAST, dependency checks)
     7. Improvement recommendations (prioritized)
     ```
   - Expect: A structured CI/CD audit

3. **Document findings**
   - Do: Save the audit as a structured report
   - How: Save to `@TargetRepo/docs/cicd-audit.md`
   - Expect: A reference document for pipeline improvements

## Expected Output

```
TargetRepo/docs/
└── cicd-audit.md
```

**Save to:** `@TargetRepo/docs/cicd-audit.md`

## What's Next

- [ ] [Run Brownfield Analysis](../onboarding/run-brownfield-analysis.md) if full codebase analysis is needed
- [ ] [Review Test Coverage](../recurring/review-test-coverage.md) to ensure CI runs adequate tests

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| DevOps Role Playbook | `playbooks/by-role/devops-engineer.md` | Deep-dive DevOps analysis prompt |
| SRE Role Playbook | `playbooks/by-role/sre.md` | Reliability-focused analysis prompt |
