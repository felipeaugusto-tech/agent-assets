# Java Code Generation Playbook

| Field | Value |
|---|---|
| **Category** | on-demand (Code Generation) |
| **Target roles** | Backend Developer, Fullstack Developer, Tech Lead |
| **Prerequisites** | `docs/playbooks/_repo-context.md` (if present), `docs/context/backend-development.md`, `docs/standards/coding.md`, 2-3 reference files of the same class kind |
| **Inputs** | Task description, target package, reference file paths |
| **Outputs** | New production class(es) matching the target repo's conventions, with a testable seam on any new external collaborator |
| **Save to** | The module matching the change, following the target repo's existing layout |
| **Related playbook** | [Java Unit Test Generation](../test/java-unit-test-generation.md) — test the class this playbook produces |

## What Is This Playbook?

A repeatable procedure for asking an AI coding assistant to write new production Java code for an Accurate service so the result matches that service's real conventions on the first pass. Accurate's Java estate spans both older Spring monoliths wired via XML and modern annotation-driven Spring Boot services — this playbook asks the assistant to detect which shape applies before writing anything, rather than assuming one universally.

## When to Use This Playbook

- Adding a new outbound integration to an external microservice or vendor API.
- Adding a new REST endpoint or controller.
- Adding a new data-access class or repository.
- Extending an existing service class with a new use case.

## Before You Start

- [ ] `docs/playbooks/_repo-context.md` exists and has been read, if the target repo has one — it carries repo identity, key paths, and risk hotspots that the deeper context files below assume you already know.
- [ ] `docs/context/backend-development.md` has been generated for the target repo.
- [ ] `docs/standards/coding.md` is loaded into the assistant's context.
- [ ] You know which existing class(es) in the target repo are the closest structural match to what you're building — the assistant should read those, not guess conventions from general framework knowledge.
- [ ] You know whether the target repo wires beans via annotations (constructor injection, `@Service`/`@Component`) or via XML — this changes how testable new code is by default.
- [ ] You've checked whether the target class/package is a known dangerous change zone in `docs/brownfield/gendd/risks/risk-hotspots.md` (or the repo's equivalent brownfield risk doc) — if so, extra care and review are warranted, not just the standard pass.
- [ ] Any "existing convention" you're relying on from brownfield/context docs is either marked CONFIRMED, or you've verified it against the actual reference files rather than trusting an INFERRED-and-unvalidated claim.

## Typical Conventions a Coding Standard Should Capture

**Requirement levels used in the tables below — `MUST`:** required; a change should not be considered done, or merged, without it. **`SHOULD`:** the strong default; follow it unless there's a specific, stated reason to deviate.

Core principles common to a well-formed Java coding standard at Accurate:

1. Follow layered architecture: Controller/REST endpoint → Service → Client/Repository → persistence. No business logic in controllers or repositories.
2. Isolate every outbound integration behind a dedicated `*Client` class with a paired exception type, called from the service layer — the service is where any logic applied to the response belongs. Never call an HTTP client directly from a controller.
3. Centralize HTTP error-to-status mapping in one place (a shared base controller or a global exception-handler component) rather than duplicating try/catch blocks per endpoint.
4. Match the dependency-injection style already used (annotation-driven constructor injection, or XML bean wiring) — do not introduce a second style.
5. Confirm which persistence layer already owns a given entity (an ORM repository or a legacy DAO/JDBC class) before adding a read or write.
6. Never build SQL by concatenating or interpolating untrusted input; use parameterized queries, bound parameters, or the ORM's safe APIs.
7. Authorization is not authentication: verify role/tenant/scope on every sensitive endpoint, and scope returned data to what the caller owns or is assigned.
8. Prefer small, single-purpose methods with guard clauses and early returns over deep nesting; keep the happy path last and readable.
9. Leave no temporary scaffolding in the final diff: no `TODO`/`FIXME` standing in for unfinished work, no large commented-out blocks, no ad-hoc debug `System.out.println`/print statements.
10. Never commit a sensitive configuration value in plaintext — encrypt it (e.g. prefix the value with `{cipher}`) before it lands in a committed YAML file. Some repos instead keep such values in an uncommitted local-override file (e.g. `application-local.yml`) so they never reach the main repository.

If the task introduces a new key dependency, a new architectural pattern, or a cross-cutting change not already used in the target repo, flag this explicitly and recommend the team capture the decision in an ADR (`docs/adr/`) before or alongside the change.

A representative naming standard, expressed the way a formal `docs/standards/coding.md` should:

| Standard | Requirement Level | Notes |
|---|---|---|
| Classes: PascalCase; methods/fields: camelCase | MUST | Java convention |
| REST entry points: `*Controller` or `*Rest` suffix | MUST | Match whichever suffix the target repo already uses |
| Business services: `*Service` (optionally paired with an `I*Service` interface) | MUST | |
| Outbound HTTP clients: `*Client` suffix | MUST | |
| Data access: `*Repository` (ORM) or `*Dao`/`*DAOImpl` (legacy) | MUST | Match the existing persistence style |
| Exceptions: `*Exception`, paired per client/service | MUST | |
| Entity ↔ DTO conversion via a dedicated assembler/mapper class | SHOULD | Keeps conversion logic out of services and controllers; many services build the DTO/entity itself with Lombok's `@Builder` rather than hand-written setters |

Error handling and logging standards:

| Standard | Requirement Level | Notes |
|---|---|---|
| Centralize HTTP status mapping in one shared component (a base controller class or a global exception-handler) | MUST | Avoids duplicated try/catch per endpoint |
| Map each domain exception to a specific, intentional HTTP status rather than a blanket 500 | SHOULD | E.g. not-found → 404, conflicting state → 409/429 |
| Do not expose stack traces in API responses | MUST | |
| Every user-facing error response includes a correlation ID | MUST | Lets support and logs be tied together. Propagate it to downstream services via a request header so the full call chain is traceable in OpenSearch — the org-wide header name is still being finalized; use `X-Trace-Id` in the interim |
| Use the logging façade already in use in the target module | MUST | SLF4J, commons-logging, or log4j — match, don't mix |
| Emit structured (JSON) log entries where the module already logs structurally | SHOULD | Include timestamp, severity, correlation_id, service_name, message, context, and a business reference id where one exists (e.g. the order's Y-code); if none exists, fall back to a subject id, search id, or other identifier so the entry stays traceable instead of noise |
| Never log PII, secrets, tokens, or credentials, or dump full request/response bodies | MUST | Redact or omit sensitive fields instead |
| Log every caught error with a reference id (order/customer/subject id) before it leaves the module | MUST | Needed to correlate failures in OpenSearch |
| Give a wrapped/rethrown exception a message stating what failed, and why if known | SHOULD | E.g. `throw new OrderIntakeServiceException("Failed to submit order " + orderId, e);` — not a bare wrap |
| When wrapping or rethrowing, always pass the original exception as the cause | MUST | Never construct a new exception from the message alone; preserve the original stack trace |

API design standards (endpoints and list responses):

| Standard | Requirement Level | Notes |
|---|---|---|
| Version new endpoints from day one (`/v1/...` or the repo's existing prefix) | MUST | Don't add unversioned public surface |
| Document every new/changed endpoint in the project's API spec (OpenAPI/Swagger, or GraphQL schema) | MUST | Keep the spec in sync with the code in the same change |
| Paginate any endpoint returning a list that can grow without bound | MUST | Cursor or offset/limit, with a sensible default and upper bound |
| Design HTTP resources as RESTful nouns/verbs with intentional status codes | SHOULD | Use kebab-case for any multi-word path segment (e.g. `/order-summaries`); use a single word where one suffices |

Data-access and transaction standards (repositories, DAOs, entities):

| Standard | Requirement Level | Notes |
|---|---|---|
| Run multi-table or multi-row writes belonging to one business operation in a single transaction | MUST | Use the module's existing transaction helper; roll back all-or-nothing |
| Never call external services or perform blocking I/O while a transaction is open | MUST | Do it after commit, or via outbox/async job with its own retry story |
| Load a collection's related entities via batching, joins, or dataloaders | MUST | Avoid one query per item (N+1) |
| One schema/entity-mapping file per entity or aggregate root | SHOULD | Match the module's existing ORM schema layout |
| Use the ORM/engine's native on-conflict (upsert) semantics for insert-or-update | SHOULD | Partial unique indexes may need predicates in the conflict target |
| New tables/columns ship in a backward-compatible, reversible migration | MUST | Nullable/defaulted new columns; expand-contract for drops/renames; generate via the ORM's migration tool, don't hand-write |

Resilience and distributed-systems standards (outbound clients, webhooks, side-effecting operations):

| Standard | Requirement Level | Notes |
|---|---|---|
| Retry transient failures (timeouts, 5xx, 429) with exponential backoff and jitter | MUST | Cap max attempts and max delay; log each retry at WARN with attempt number, delay, error class, correlation id |
| Design operations that can be redelivered or retried (webhooks, payment/inventory writes, queue consumers) to be idempotent | MUST | Idempotency key, natural key, or compare-and-set |
| Do not rely on in-process memory as the sole source of authoritative state | MUST | Assume multiple instances, restarts, and concurrent workers |

## The Prompt Template (Full)

Copy this into your AI coding assistant, fill in the bracketed placeholders, and attach the reference files it names before running it.

```
Read @docs/playbooks/_repo-context.md (if present)
Read @docs/context/backend-development.md
Read @docs/standards/coding.md
Read @docs/brownfield/gendd/risks/risk-hotspots.md (if present) — flag if the
target class/package is a known dangerous change zone

You are generating production Java code for [TARGET REPO], a [brief
description of the stack, e.g. "Spring Boot / Maven service" or "Spring
XML-wired monolith"].

## Task
[Describe the feature/change: what it does, why it's needed, where it fits —
e.g. "Add an outbound REST client that notifies a vendor when a record's
status changes, following the existing order-intake integration pattern."]

## Target location
- Module/package: [target package]
- Reference files to read first (do not guess conventions — copy them):
  [list 2-3 real existing files of the same kind in the target repo]

## Architecture constraints
- Detect and match the target repo's dependency-injection style
  (annotation-driven constructor injection vs. XML bean wiring) — do not
  introduce a second style.
- If this is an external integration, isolate it in a dedicated
  `*Client` class with a paired exception type, called from the service
  layer (which owns any logic applied to the response) — never call the
  HTTP client directly from a controller.
- If this touches persistence, identify which existing layer owns the
  entity before writing to it — do not introduce a third persistence style.
- Route any new domain exception through the target repo's existing
  centralized error-handling component (base controller or global
  exception handler) with a specific, intentional HTTP status.
- Testability: if the target repo uses constructor injection, accept the
  new class's collaborators (HTTP client, etc.) as constructor parameters
  so the DI container — and tests — can supply a mock. If the target repo
  constructs collaborators directly with `new` at the call site, add an
  explicit package-private setter or constructor overload purely so tests
  can inject a double; this costs nothing in production.
- If this introduces a new pattern, key dependency, or cross-cutting
  change the target repo doesn't already use, say so explicitly and
  recommend an ADR before proceeding.

## API design (if this adds or changes an endpoint)
- Version the endpoint using the repo's existing prefix (e.g. `/v1/...`) —
  do not add unversioned public surface.
- Update the project's OpenAPI/Swagger (or GraphQL schema) for this
  endpoint in the same change.
- Paginate any response that returns a list that can grow without bound
  (cursor or offset/limit, with a default and upper bound page size).
- Verify role/tenant/scope on this route, not just that the caller is
  authenticated; scope any returned data to what the caller owns or is
  assigned.
- Use kebab-case for any multi-word path segment (e.g. `/order-summaries`);
  use a single word where one suffices.

## Data access (if this touches persistence)
- Run multi-table or multi-row writes for one business operation inside a
  single transaction using the module's existing transaction helper.
- Never call an external service or perform blocking I/O while that
  transaction is open — do it after commit, or via outbox/async job.
- Load a collection's related entities via batching/joins, not one query
  per item.
- If adding a new entity, use one schema/mapping file per entity, matching
  the module's existing layout. If this requires a migration, make it
  backward-compatible and reversible (nullable/defaulted new columns;
  expand-contract for drops/renames), generated through the ORM's
  migration tool rather than hand-written.

## Resilience (if this is an outbound integration or a side-effecting operation)
- Retry transient failures (timeouts, 5xx, 429) with exponential backoff
  and full jitter; cap the max attempts and max delay.
- If this operation can be retried or redelivered (webhook handler,
  payment/inventory write, queue consumer), design it to be idempotent
  (idempotency key, natural key, or compare-and-set).
- Never build SQL by concatenating untrusted input; use parameterized
  queries or the ORM's safe APIs.

## Naming
Match the suffix already used for this kind of class in the target
package (`*Controller`/`*Rest`, `*Service`, `*Client`, `*Repository`/`*Dao`,
`*Exception`, `*Assembler`). Mirror the reference files' package layout.

## Cross-cutting concerns
- Logging: use the same logging API as the reference files in this
  package. Prefer structured (JSON) log entries where the module already
  logs structurally, including a correlation ID and a business reference id
  (e.g. the order's Y-code; fall back to a subject/search id if no
  reference id exists). Where this code calls another internal service,
  propagate the correlation/trace id via a request header (the org-wide
  header name is still being finalized — use `X-Trace-Id` in the interim)
  so the call chain is traceable in OpenSearch. Never log PII, secrets,
  tokens, or full request/response bodies.
- Error handling: log every caught error with a reference id before
  wrapping it. Wrap failures in the module's existing exception type,
  mapped to a specific HTTP status via the existing centralized handler,
  with a message stating what failed and why if known — never construct
  the wrapping exception from the message alone, always pass the original
  exception as the cause. Include a correlation ID in every user-facing
  error response; never expose stack traces or raw dependency exception
  messages to callers.
- Configuration: read URLs/credentials from environment configuration —
  never hardcode them. Never commit a sensitive value in plaintext —
  encrypt it (e.g. prefix with `{cipher}`) before it reaches a committed
  YAML file, or place it in the repo's uncommitted local-override file
  (e.g. `application-local.yml`) if one exists. If this adds a new config
  value, update `.env.example` (or the repo's documented template) with a
  placeholder and a short description.
- Code quality: guard clauses and early returns over deep nesting; small,
  single-purpose methods and intention-revealing names over comments; no
  leftover TODOs, commented-out blocks, or debug print statements; code
  must pass the module's configured linters/formatters with no new
  violations.

## Dependencies
Use only libraries already present in the target module. Do not add a new
HTTP client, JSON library, or DI framework duplicating one already in use.

## Documentation
If this change alters an API contract, configuration, or user-facing
behavior, update the doc that already owns that topic (README section,
guide, or runbook) in the same change — do not create a duplicate doc, and
do not edit an accepted ADR to retrofit it to the new behavior.

## Output
- Production code only (tests are requested separately — see the Unit Test
  Generation Playbook).
- Include package declaration and imports.
- If you deviate from any constraint above, state why in a one-line comment
  at the top of the file.
```

## Illustrative Example

The example below shows the modern, annotation-driven shape: constructor-injected Spring beans and centralized exception-to-status mapping. Names are invented, not drawn from any specific Accurate repository.

### Controller, service, and REST client

```java
@RestController
@RequestMapping("/v1/orders")
public class OrderIntakeController {

    private final OrderIntakeService orderIntakeService;

    public OrderIntakeController(OrderIntakeService orderIntakeService) {
        this.orderIntakeService = orderIntakeService;
    }

    @PostMapping
    public ResponseEntity<OrderResponseDto> submitOrder(@RequestBody OrderRequestDto request) {
        return ResponseEntity.ok(orderIntakeService.submitOrder(request));
    }
}
```

```java
@Service
public class OrderIntakeService {

    private static final Logger log = LoggerFactory.getLogger(OrderIntakeService.class);

    private final OrderIntakeRestClient orderIntakeRestClient;

    public OrderIntakeService(OrderIntakeRestClient orderIntakeRestClient) {
        this.orderIntakeRestClient = orderIntakeRestClient;
    }

    public OrderResponseDto submitOrder(OrderRequestDto request) {
        try {
            return orderIntakeRestClient.submit(request);
        } catch (RestClientException e) {
            log.error("Failed to submit order for customerId={}", request.getCustomerId(), e);
            throw new OrderIntakeServiceException(
                "Failed to submit order for customerId=" + request.getCustomerId(), e);
        }
    }
}
```

Because `OrderIntakeRestClient` is a constructor-injected Spring bean rather than something the service constructs itself with `new`, this class is already testable — a test can simply pass a mock into the constructor. No extra seam is needed here. Contrast this with an older Spring XML-wired monolith, where collaborators are more often constructed directly inside a method body; in that shape, add an explicit package-private setter or constructor overload purely for tests, since a full dependency-injection refactor is rarely in scope for a single change.

```java
@Component
public class OrderIntakeRestClient {

    private final RestTemplate restTemplate;
    private final String orderIntakeUrl;

    public OrderIntakeRestClient(RestTemplate restTemplate,
                                  @Value("${order-intake.host}") String orderIntakeUrl) {
        this.restTemplate = restTemplate;
        this.orderIntakeUrl = orderIntakeUrl;
    }

    public OrderResponseDto submit(OrderRequestDto request) {
        return restTemplate.postForObject(orderIntakeUrl + "/orders", request, OrderResponseDto.class);
    }
}
```

### Centralized exception-to-status mapping

Rather than a try/catch in every controller, route domain exceptions through one shared component that maps each to a specific, intentional HTTP status:

```java
@RestControllerAdvice
public class ApiExceptionHandler {

    @ExceptionHandler(OrderNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ErrorResponseDto handleNotFound(OrderNotFoundException e) {
        return new ErrorResponseDto(e.getMessage());
    }

    @ExceptionHandler(DuplicateOrderException.class)
    @ResponseStatus(HttpStatus.CONFLICT)
    public ErrorResponseDto handleDuplicate(DuplicateOrderException e) {
        return new ErrorResponseDto(e.getMessage());
    }

    @ExceptionHandler(OrderIntakeServiceException.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorResponseDto handleServiceError(OrderIntakeServiceException e) {
        return new ErrorResponseDto("Unable to process order");
    }
}
```

In an older Spring XML-wired monolith, the equivalent shape is often a shared base controller class that other controllers extend, with one `@ExceptionHandler` method per domain exception — same principle (one place maps exceptions to status codes), different mechanism. Detect which mechanism the target repo already uses before adding a second one.

## Review Checklist

- [ ] Dependency-injection style matches the target repo's existing approach — no second style introduced.
- [ ] New external calls are isolated in a `*Client` class with a paired exception type, called from the service layer — not directly from a controller.
- [ ] If collaborators are constructor-injected, the new class accepts them as constructor parameters (no internal `new`); if the target repo constructs collaborators directly, a test seam was added.
- [ ] New domain exceptions are routed through the existing centralized error-handling component with a specific HTTP status.
- [ ] Persistence uses the same layer (ORM repository or legacy DAO/JDBC) as the entity's existing owner — not a new third style.
- [ ] No PII, secrets, tokens, or passwords in any log statement; logs are structured where the module already logs structurally.
- [ ] Every caught error is logged with a reference id (order/customer/subject id, or the order's Y-code where applicable); wrapped/rethrown exceptions carry a descriptive message and the original exception as cause.
- [ ] No stack traces or raw dependency exception messages exposed in API responses; user-facing errors carry a correlation ID, propagated to downstream calls via a trace header (`X-Trace-Id` in the interim).
- [ ] URLs and credentials come from configuration, never hardcoded; sensitive values are encrypted (e.g. `{cipher}`-prefixed) before being committed, or kept in an uncommitted local-override file; `.env.example` updated for any new config value.
- [ ] New/changed endpoints are versioned, documented in the API spec, paginated if they return an unbounded list, and use kebab-case for multi-word path segments.
- [ ] Sensitive routes check role/tenant/scope, not just authentication; returned data is scoped to the caller.
- [ ] SQL is parameterized or built via the ORM's safe APIs — no string-concatenated queries.
- [ ] Multi-table/multi-row writes for one operation run in a single transaction, with no external calls or blocking I/O inside it.
- [ ] Collection loads use batching/joins rather than one query per item.
- [ ] Outbound calls that can fail transiently retry with capped exponential backoff and jitter; retryable/redeliverable operations are idempotent.
- [ ] New schema changes are backward-compatible and reversible.
- [ ] No leftover TODOs, commented-out code, or debug print statements; code passes the module's linters/formatters.
- [ ] Docs that own the changed behavior (README section, guide, runbook) were updated; no accepted ADR was rewritten to match new behavior.
- [ ] If the change touches a known risk hotspot, that was called out explicitly rather than treated as a routine change.

## Related Resources

- [README — how this fits GenDD scaffolding](../README.md)
- [Java Unit Test Generation Playbook](../test/java-unit-test-generation.md)
- `docs/playbooks/_repo-context.md` — shared repo context, read before the deeper context/standards files
- `docs/brownfield/gendd/risks/risk-hotspots.md` — known dangerous change zones for the target repo
