# Role Playbook: DevOps Engineer

**Role:** DevOps Engineer
**Focus:** CI/CD analysis, deployment patterns, infrastructure review
**Time:** 45-60 minutes

---

## Purpose

Analyze a codebase from a DevOps Engineer perspective to understand:
- CI/CD pipeline architecture
- Deployment strategies and patterns
- Infrastructure as code
- Environment management
- Build and release processes

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/devops-engineer.md
Analyze @TargetRepo for CI/CD and deployment patterns.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/devops-engineer.md

Analyze @TargetRepo from a DevOps Engineer perspective:

## Context
- Cloud Provider: [AWS | Azure | GCP | On-Prem]
- Orchestration: [Kubernetes | Docker Swarm | ECS | None]
- CI Platform: [GitHub Actions | GitLab CI | Jenkins | CircleCI]
- IaC Tool: [Terraform | Pulumi | CloudFormation | ARM | None]

## Phase 1: Repository DevOps Structure

Map DevOps-related files:
| Category | Location | Files |
|----------|----------|-------|
| CI/CD Config | `.github/workflows/` | [list] |
| Docker | `./` | `Dockerfile`, `docker-compose.yml` |
| K8s Manifests | `k8s/` | [list] |
| IaC | `infra/` | [list] |
| Scripts | `scripts/` | [list] |
| Environment | `./` | `.env.example`, `config/` |

## Phase 2: CI/CD Pipeline Analysis

### Pipeline Overview
| Pipeline | Trigger | Stages | Duration | Pass Rate |
|----------|---------|--------|----------|-----------|
| PR Validation | PR open | Lint, Test, Build | [time] | [%] |
| Main Build | Merge to main | Full CI | [time] | [%] |
| Deploy Staging | Main push | Deploy | [time] | [%] |
| Deploy Prod | Manual/Tag | Deploy | [time] | [%] |

### Pipeline Stages Detail
| Stage | Purpose | Tools | Caching | Parallelism |
|-------|---------|-------|---------|-------------|
| Install | Deps | npm/go mod | Yes/No | N/A |
| Lint | Quality | ESLint/golint | N/A | Yes/No |
| Test | Verify | Jest/go test | Test deps | Yes/No |
| Build | Compile | [tool] | Build cache | N/A |
| Security | Scan | [tool] | N/A | Yes/No |
| Deploy | Release | [tool] | N/A | N/A |

## Phase 3: Container Strategy

### Docker Analysis
| Aspect | Current State | Best Practice | Status |
|--------|---------------|---------------|--------|
| Base image | [image] | Minimal (alpine/distroless) | OK/Needs work |
| Multi-stage | Yes/No | Yes | OK/Needs work |
| Layer caching | [approach] | Optimized order | OK/Needs work |
| Security scan | Yes/No | Trivy/Snyk in CI | OK/Needs work |
| Image size | [size] | <100MB | OK/Needs work |

### Container Configuration
| Config | Method | Files |
|--------|--------|-------|
| Environment | Env vars/ConfigMaps | [files] |
| Secrets | [approach] | [files] |
| Healthcheck | [type] | [location] |
| Resources | [defined?] | [location] |

## Phase 4: Deployment Strategy

### Current Approach
| Aspect | Implementation | Notes |
|--------|----------------|-------|
| Strategy | [Rolling/Blue-Green/Canary] | [details] |
| Rollback | [Automatic/Manual/None] | [process] |
| Health checks | [Type] | [endpoints] |
| Graceful shutdown | [Implemented?] | [timeout] |

### Environment Matrix
| Environment | Deployment | Config Source | Secrets |
|-------------|------------|---------------|---------|
| Development | Local Docker | `.env.dev` | Local |
| Staging | [Platform] | [Source] | [Vault/K8s/etc] |
| Production | [Platform] | [Source] | [Vault/K8s/etc] |

## Phase 5: Infrastructure as Code

### IaC Coverage
| Resource Type | Managed By | Files | Drift Detection |
|---------------|------------|-------|-----------------|
| Compute | [Tool] | [files] | Yes/No |
| Network | [Tool] | [files] | Yes/No |
| Database | [Tool] | [files] | Yes/No |
| Storage | [Tool] | [files] | Yes/No |
| Monitoring | [Tool] | [files] | Yes/No |

### State Management
| Aspect | Implementation |
|--------|----------------|
| State backend | [S3/Azure Blob/GCS/Local] |
| State locking | [DynamoDB/etc] |
| Environments | [Workspaces/Directories] |

## Phase 6: Security & Compliance

| Security Aspect | Implementation | Status |
|-----------------|----------------|--------|
| Secret management | [Vault/AWS SM/K8s Secrets] | OK/Needs work |
| Image scanning | [Tool] | OK/Missing |
| SAST | [Tool] | OK/Missing |
| Dependency scanning | [Tool] | OK/Missing |
| Compliance checks | [Tool] | OK/Missing |

## Phase 7: Observability Hooks

| Aspect | Implementation | Integration |
|--------|----------------|-------------|
| Deploy notifications | [Slack/Teams/etc] | [trigger] |
| Metrics push | [Datadog/Prometheus/etc] | [agent/push] |
| Log forwarding | [Tool] | [sidecar/agent] |
| Trace injection | [Tool] | [automatic/manual] |

## Phase 8: Recommendations

### Critical (P1)
| Issue | Impact | Recommendation | Effort |
|-------|--------|----------------|--------|

### Important (P2)
| Issue | Impact | Recommendation | Effort |
|-------|--------|----------------|--------|

### Nice to Have (P3)
| Issue | Impact | Recommendation | Effort |
|-------|--------|----------------|--------|
```

---

## Output: DevOps Analysis Report

```markdown
# DevOps Analysis: [Project Name]
Generated: [Date]
Analyzed by: DevOps Engineer Playbook

## Infrastructure Overview

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│   Dev    │───▶│ Staging  │───▶│   Prod   │
│  Local   │    │  [Cloud] │    │  [Cloud] │
└──────────┘    └──────────┘    └──────────┘
```

## CI/CD Pipeline

### Pipeline Flow
```
PR ──► Lint ──► Test ──► Build ──► Deploy
[5m]   [1m]    [3m]     [2m]      [5m]
```

### Health Metrics
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Build time | [time] | <10m | |
| Deploy time | [time] | <5m | |
| MTTR | [time] | <1h | |
| Change failure rate | [%] | <15% | |

## Container Strategy

### Dockerfile Assessment
- [ ] Using minimal base image
- [ ] Multi-stage build
- [ ] Non-root user
- [ ] Security scanning
- [ ] Optimized layer caching

## Deployment

### Current Strategy: [Strategy]
**Pros:** [list]
**Cons:** [list]

### Rollback Process
[Document current rollback procedure]

## Infrastructure as Code

### Coverage
| Resource | IaC | Drift |
|----------|-----|-------|

### Recommendations
1. [Recommendation]

## Security

### Current State
- Secret management: [status]
- Image scanning: [status]
- SAST: [status]
- Dependency scanning: [status]

### Gaps
1. [Gap]

## Recommendations

### Immediate
- [ ] [Action]

### Short-term
- [ ] [Action]

### Long-term
- [ ] [Action]
```

---

## Reference Templates

This playbook's analysis areas align with the universal principles in the Context Pack template. Reference them for baseline expectations:

| Template | Relevant Sections |
|----------|-------------------|
| `templates/context-pack.md` (conventions.md section) | Version control: branch protection, branching strategy, merge strategies, .gitignore essentials |
| `templates/context-pack.md` (agents.md section) | Secret handling, dependency security |
| `templates/context-pack.md` (testing.md section) | CI/CD integration, pipeline stages, test categories (unit/integration/E2E) |

---

## Follow-Up Actions

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
