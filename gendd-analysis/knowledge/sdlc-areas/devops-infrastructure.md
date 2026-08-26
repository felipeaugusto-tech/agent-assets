# DevOps & Infrastructure -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the DevOps & Infrastructure lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| CI/CD pipeline configuration | HIGH | `.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`, `.circleci/config.yml` |
| Container configuration | HIGH | `Dockerfile`, `docker-compose.yml`, `.dockerignore` |
| Infrastructure as Code files | HIGH | `*.tf`, `*.tfvars`, `pulumi/`, `cloudformation/`, `bicep/`, `cdk/` |
| Kubernetes manifests | HIGH | `k8s/`, `helm/`, `kustomize/`, `*.yaml` with `apiVersion` |
| Deployment scripts | MEDIUM | `scripts/deploy*`, `Makefile` with deploy targets |
| Environment configuration files | MEDIUM | `.env.example`, `config/`, environment-specific configs |
| Cloud provider SDK configuration | MEDIUM | AWS SDK config, Azure SDK config, GCP credentials setup |
| Monitoring/observability config | LOW | Prometheus config, Datadog agent config, Grafana dashboards |
| Build automation | LOW | `Makefile`, `Taskfile.yml`, `justfile`, `build.sh` |

## What to Analyze

### Repository DevOps Structure
- Look for: CI/CD config files and their location
- Look for: Container files (Dockerfile, docker-compose)
- Look for: Kubernetes manifests or Helm charts
- Look for: IaC files (Terraform, Pulumi, CloudFormation)
- Look for: Deployment and build scripts
- Look for: Environment configuration files
- Document: DevOps file map with category, location, and purpose

### CI/CD Pipeline Analysis
- Look for: Pipeline triggers (PR open, merge to main, tag, schedule)
- Look for: Pipeline stages (lint, test, build, security scan, deploy)
- Look for: Stage duration and pass rates (from config or workflow history)
- Look for: Dependency caching configuration
- Look for: Test parallelization in pipeline
- Look for: Deployment stages across environments
- Assess: Pipeline completeness, speed, and reliability
- Document: Pipeline overview with triggers, stages, duration, and pass rates

### Container Strategy
- Look for: Base image selection (minimal, alpine, distroless, or full OS)
- Look for: Multi-stage build patterns
- Look for: Layer caching optimization (dependency install before code copy)
- Look for: Security scanning integration (Trivy, Snyk, Grype)
- Look for: Image size and optimization
- Look for: Non-root user configuration
- Assess: Container security and efficiency best practices
- Document: Container assessment with base image, build pattern, security, and size

### Deployment Strategy
- Look for: Deployment method (rolling update, blue-green, canary, recreate)
- Look for: Rollback mechanism (automatic, manual, feature flags)
- Look for: Health check endpoints and configuration
- Look for: Graceful shutdown implementation
- Look for: Zero-downtime deployment support
- Document: Deployment strategy with method, rollback plan, and health check approach

### Environment Management
- Look for: Environment definitions (dev, staging, production)
- Look for: Configuration source per environment (env vars, ConfigMaps, Vault, Parameter Store)
- Look for: Secret management approach (Vault, AWS Secrets Manager, K8s Secrets, env files)
- Look for: Environment parity (how similar are staging and production?)
- Document: Environment matrix with deployment method, config source, and secret management per environment

### Infrastructure as Code
- Look for: IaC tool and coverage (what resources are managed by code?)
- Look for: State management approach (remote state, locking, workspaces)
- Look for: Resource types managed (compute, network, database, storage, monitoring)
- Look for: Drift detection mechanism
- Assess: IaC maturity and coverage completeness
- Document: IaC coverage table with resource type, tool, files, and drift detection status

### Security and Compliance
- Look for: Secret management implementation
- Look for: Image scanning in CI
- Look for: Static Application Security Testing (SAST) in pipeline
- Look for: Dependency vulnerability scanning
- Look for: Compliance automation (policy as code, OPA, Kyverno)
- Assess: DevSecOps maturity
- Document: Security tooling inventory with implementation status per category

### Observability Hooks
- Look for: Deploy notification configuration (Slack, Teams, email)
- Look for: Metrics push on deploy (Datadog, Prometheus, CloudWatch)
- Look for: Log forwarding configuration (sidecar, agent, direct)
- Look for: Trace injection (automatic instrumentation, manual)
- Document: Observability integration points with tools and trigger mechanisms

## Key Questions to Answer

1. What CI/CD platform is used and what does the pipeline look like?
2. How is the application containerized and what is the image strategy?
3. What deployment strategy is used and how are rollbacks handled?
4. How are environments managed and how do they differ?
5. What Infrastructure as Code approach is used and what does it cover?
6. How are secrets managed across environments?
7. What security scanning is integrated into the pipeline?
8. What monitoring and observability hooks exist in the deployment process?
9. What are the DORA metrics indicators (deploy frequency, lead time, change failure rate, MTTR)?
10. What are the biggest gaps in the current DevOps setup?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| GitOps | ArgoCD, Flux, declarative config in git, environment branches | Auditable, reproducible deployments |
| Infrastructure as Code | Terraform, Pulumi, CloudFormation, CDK files | Reproducible infrastructure, version controlled |
| Container Orchestration | Kubernetes manifests, Helm charts, ECS task definitions | Production-grade container management |
| Feature Flags | LaunchDarkly, Unleash, custom flag service | Safe progressive rollouts, decoupled deploy/release |
| Immutable Infrastructure | No SSH access, image-based deploys, no in-place updates | Reliable, reproducible environments |
| CI/CD as Code | Pipeline defined in repo (not UI-configured) | Version controlled, reviewable pipeline |
| Environment per PR | Dynamic environment creation on PR, cleanup on merge | Fast feedback, isolated testing |
| Trunk-Based Development | Short-lived branches, frequent merges to main, feature flags | Fast feedback, reduced merge conflicts |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No CI/CD pipeline | Missing pipeline config files | HIGH |
| Secrets in source code | API keys, passwords in config files, `.env` committed | HIGH |
| No rollback mechanism | Missing rollback scripts, no deployment versioning | HIGH |
| No container security scanning | Missing Trivy/Snyk/Grype in pipeline | MEDIUM |
| Manual deployment process | No deployment automation, SSH-based deploys | MEDIUM |
| No IaC for infrastructure | Resources created manually in cloud console | MEDIUM |
| Single environment | No staging environment, deploy directly to production | HIGH |
| No monitoring on deploy | No deploy notifications, no post-deploy health checks | MEDIUM |
| Large Docker images | Base images >500MB, no multi-stage build | LOW |
| No dependency caching in CI | Long pipeline times, repeated dependency downloads | LOW |

## Output Guidance

### Must Include
- CI/CD pipeline overview with stages, triggers, and estimated duration
- Container strategy assessment (base image, multi-stage, security)
- Deployment strategy with rollback mechanism
- Environment matrix with configuration and secret management per environment
- IaC coverage summary

### Should Include (if detected)
- Security scanning inventory (SAST, image scan, dependency scan)
- Observability hooks at deployment time
- DORA metrics indicators
- Pipeline optimization recommendations
- Infrastructure drift detection assessment

### Related Areas
- [architecture](./architecture.md) -- deployment architecture within system design
- [site-reliability](./site-reliability.md) -- observability, SLOs, incident response
- [security](./security.md) -- DevSecOps, secret management, vulnerability scanning
- [release-management](./release-management.md) -- release process, versioning, changelog
- [quality-assurance](./quality-assurance.md) -- CI test integration and pipeline test stages
