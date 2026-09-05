# Evidence Sources

Where each diagram level's truth lives in a repository. Use this when a stack is
unfamiliar, or when the obvious places came up empty.

The principle throughout: **configuration and manifests describe intent; running
code describes behavior; IaC describes deployment.** When they disagree, say so —
the disagreement is usually the interesting finding.

---

## Actors (L1)

| Source | What it yields |
|---|---|
| Auth middleware, guards, decorators | Role names — a proxy for actors, not a substitute |
| Role or permission enums, RBAC config | The role taxonomy the code enforces |
| Seed data, fixtures, test users | Realistic persona names |
| `docs/context.md` or equivalent | The actual persona definitions, if the Context Pack has them |
| README, onboarding docs | Who the system is for, in prose |

Roles are not actors. Three roles may be one human job, and a "service" role is
not a person. Confirm the actor list rather than transcribing the enum.

---

## External systems (L1)

| Source | What it yields |
|---|---|
| Dependency manifests | Vendor SDKs — Stripe, Twilio, Auth0, Segment |
| Env var names and `.env.example` | Base URLs, API keys, hostnames of dependencies |
| HTTP client instantiations, base URLs | Outbound calls, and which module owns them |
| Webhook route handlers | Inbound integrations, easy to miss |
| OpenAPI or client-generation config | Contract-defined dependencies |
| Feature flags | Integrations that may be dormant |

Watch for vestigial config: an env var and an unused client are common leftovers of
an integration removed months ago. Grep for actual call sites before drawing the
arrow, and ask when it is ambiguous.

---

## Containers (L2)

| Ecosystem | Look at |
|---|---|
| Node / TypeScript | `package.json` per package, workspaces, `main`/`bin`/`scripts.start`, `Dockerfile`s |
| Python | `pyproject.toml`, `setup.py`, entry points, ASGI/WSGI app definitions, Celery workers |
| Java / Kotlin | `pom.xml` modules, Gradle subprojects, `@SpringBootApplication` classes |
| .NET | `.sln` and `.csproj` files, `Program.cs`, host builders |
| Go | `go.mod`, `main` packages under `cmd/` |
| Ruby | `Gemfile`, `config.ru`, Sidekiq workers |

Cross-cutting signals of a distinct deployable:

- Its own `Dockerfile`, or a service entry in `docker-compose.yml`
- A separate k8s `Deployment`, `StatefulSet`, `CronJob`, or `Job`
- A separate CI job that builds and publishes it
- Its own health check endpoint or port binding
- A serverless function definition

Datastores and brokers are containers too. Find them in connection strings, ORM
config, migration directories, and compose service definitions — and name the
engine and version where the evidence gives it.

---

## Components (L3)

| Source | What it yields |
|---|---|
| Route registration files | The API surface, and which module handles each path |
| DI container or module registration | The intended component seams, as the authors saw them |
| Directory structure inside the container | Feature or layer groupings |
| Service, repository, handler classes | Responsibilities worth naming |
| Interface or port definitions | Genuine boundaries, as opposed to incidental file splits |

Prefer the seams the code declares over the ones a folder tree implies. A `utils/`
directory is rarely a component; a registered module with an interface usually is.

---

## Deployment

| Source | What it yields |
|---|---|
| Terraform, Pulumi, CloudFormation, Bicep | Real infrastructure: compute, network, managed services |
| Kubernetes manifests, Helm charts | Clusters, namespaces, replica counts, resource limits |
| `docker-compose.yml` | Local topology — do not present it as production |
| CI/CD workflows | Deploy targets, regions, environment names, gating |
| Platform config (`app.yaml`, `vercel.json`, `fly.toml`, Procfile) | Hosting platform and scaling settings |
| Environment config directories | Which environments exist, and how they differ |

With no IaC in the repository, the deployment diagram is not derivable. Ask. The
CI workflow often reveals the platform and region, which makes the question much
easier to answer — offer that inference as the proposed default rather than
presenting it as fact.

---

## Cross-cutting: relationship evidence

An arrow needs a source, a target, and a mechanism. Get the mechanism from:

- Client construction and call sites (HTTP, gRPC, SDK)
- Message publish and subscribe registrations (topics, queues, consumer groups)
- Database clients and ORM configuration
- Shared datastore access — two containers on one database is worth drawing, and
  often worth flagging
- Contract tests, which name both parties explicitly and are the strongest evidence
  available

Unlabeled arrows are the most common defect in generated C4 diagrams. If the
mechanism cannot be established, that is a question, not a plain line.
