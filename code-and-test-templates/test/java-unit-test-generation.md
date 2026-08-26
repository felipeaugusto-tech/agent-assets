# Java Unit Test Generation Playbook

| Field | Value |
|---|---|
| **Category** | on-demand (Generate Unit Tests) |
| **Target roles** | Backend Developer, Fullstack Developer, QA Automation Engineer |
| **Prerequisites** | `docs/playbooks/_repo-context.md` (if present), `docs/context/quality-assurance.md`, `docs/standards/testing.md`, one reference test file from the same or a structurally similar package |
| **Inputs** | Path to the class under test, reference test file, specific methods to focus on (optional) |
| **Outputs** | Complete test class(es) covering success, edge cases, and error conditions, with untestable seams flagged |
| **Save to** | The test directory mirroring the package of the class under test, in the same module |
| **Related playbook** | [Java Code Generation](../code/java-code-generation.md) — write the testability seam in at code-gen time, not after |

## What Is This Playbook?

A repeatable procedure for asking an AI coding assistant to generate JUnit tests for an Accurate Java service that match that service's actual test framework, structure, and coverage expectations — not a generic template. This is the Java-specific version of the generic "Generate Unit Tests" on-demand playbook GenDD produces by default.

## When to Use This Playbook

- Writing tests for new code produced by the [Java Code Generation Playbook](../code/java-code-generation.md).
- Adding coverage to an existing class identified as high-risk.
- After a test coverage review flags a class or endpoint with zero tests.

## Before You Start

- [ ] `docs/playbooks/_repo-context.md` exists and has been read, if the target repo has one.
- [ ] `docs/context/quality-assurance.md` and `docs/standards/testing.md` are loaded into the assistant's context.
- [ ] You know the test framework and version actually in use (JUnit 3, 4, or 5; Mockito version; whether `MockMvc` is used for controller-layer tests).
- [ ] You have identified one existing test in the same package as a style reference.
- [ ] You have confirmed the module builds and its existing test suite passes before you add to it.
- [ ] You've checked `docs/brownfield/gendd/risks/risk-hotspots.md` (or the repo's equivalent brownfield risk doc) — if the class under test is a listed hotspot, prioritize it and cover its failure modes more thoroughly, not just the standard scenario list.

## Typical Conventions a Testing Standard Should Capture

**Requirement levels used in the tables below — `MUST`:** required; a change should not be considered done, or merged, without it. **`SHOULD`:** the strong default; follow it unless there's a specific, stated reason to deviate. **`MUST NOT`:** never do this.

Framework and structure, expressed the way a formal `docs/standards/testing.md` should:

| Standard | Requirement Level | Notes |
|---|---|---|
| Use the JUnit version and runner already in the target module (3, 4 with `@RunWith`, or 5 with `@ExtendWith`) | MUST | Confirm before assuming a newer version is available |
| Mockito for boundary mocks (HTTP clients, repositories, other services) | MUST | |
| `MockMvc` (or the framework's equivalent) for controller/REST-layer tests | MUST | Verifies routing, status codes, and response shape without a running server |
| Request/response fixtures as JSON files under a test-resources directory, where the module already does this | SHOULD | Keeps large payloads out of Java string literals |
| One test class per REST-client operation or per controller endpoint, where the module already does this | SHOULD | Check existing test granularity before deciding your own |
| Shared factories, builders, and large fixtures live in a dedicated test-utilities module/package | SHOULD | Promote to it only once reused across multiple test classes; keep tiny one-off helpers next to the test that needs them |
| No production data or real PII in any test fixture | MUST | Use synthetic values even when copying the shape of a real payload |

Required scenarios, generalized from a representative service's actual contract:

| Scenario | Typical HTTP / behavior | Covered by |
|---|---|---|
| Success | 200 | Service test + controller test |
| Not found | 404 | Service test + controller test |
| Conflicting / duplicate state | 409 or 429, whichever the API intentionally contracts | Controller test |
| Validation failure | 400 | Service or controller test, depending on where validation lives |
| Downstream/external service failure | Mapped to the client's exception type | REST-client test |

Anti-patterns worth stating explicitly as MUST NOT:

| Anti-pattern | Requirement level |
|---|---|
| Tests calling live or production endpoints | MUST NOT |
| Tests depending on execution order or shared mutable static state | MUST NOT |
| Deleting a test fixture without updating every test that references it | MUST NOT |
| Skipping the paired client-library test when a REST endpoint's contract changes | MUST NOT |
| Weakening an assertion, changing an expected value, or deleting coverage just to make a failing test pass | MUST NOT |
| Silently rewriting a test that looks wrong instead of flagging it for human review | MUST NOT |

## The Prompt Template (Full)

Copy this into your AI coding assistant, fill in the bracketed placeholders, and attach the production class under test plus one existing test class from the same package as a style reference.

```
Read @docs/playbooks/_repo-context.md (if present)
Read @docs/context/quality-assurance.md
Read @docs/standards/testing.md
Read @docs/brownfield/gendd/risks/risk-hotspots.md (if present) — if the
class under test is listed, cover its failure modes more thoroughly

You are generating unit tests for [TARGET REPO].

## Class(es) under test
[Paste or reference the production class(es)]

## Reference test style
[Paste or reference an existing test class from the same package, or a
structurally similar one, so the assistant matches the JUnit version,
runner, and mocking style already in use — not a generic style.]

## Test framework
- Match the JUnit version and runner already in use (3, 4 with
  @RunWith(SpringRunner.class), or 5 with @ExtendWith) — do not introduce a
  newer framework the target repo doesn't already depend on.
- Use MockMvc (or the equivalent) for controller/REST-layer tests rather
  than starting a real server.
- Mock collaborators with Mockito. If the class under test takes its
  collaborators as constructor parameters, use @InjectMocks to wire mocked
  @Mock fields in automatically. If a collaborator is constructed directly
  inside the method under test and has no injection seam, say so
  explicitly rather than reaching for reflection-based mocking tricks.

## Naming & structure
- Test class: {ClassUnderTest}Test.
- Test method: {method}_{scenario}_{expectedResult} for new tests; match
  the file's existing legacy naming only if every other test in that file
  already uses it.
- Arrange-Act-Assert structure in every test method.

## Coverage to include
1. Success path, asserting both the returned value and the HTTP status
   (for controller tests).
2. Not-found / missing-resource path.
3. Conflicting or duplicate-state path, if the endpoint has one.
4. Validation failure.
5. Downstream/external service failure, mapped to the correct exception
   type and HTTP status.

## Mocking guidance
- Mock: HTTP clients, repositories/DAOs, other services, mail senders,
  async messaging side effects.
- Do not mock: the class under test, or simple DTOs/value objects.
- If a collaborator is constructed directly inside the method under test
  and has no injection seam, do not attempt to test the call it makes —
  test the reachable parts (validation, mapping, exception wrapping) and
  note the untestable seam as a follow-up.

## Assertions
- For service tests: assert on returned values, thrown exception types,
  and Mockito verify() calls that reflect real behavior.
- For controller tests: assert on HTTP status and response body shape
  (e.g. via jsonPath), matching the exception-to-status contract from the
  centralized error handler.
- Change production code to satisfy an existing test's intent, not the
  other way around. Do not weaken an assertion, change an expected value,
  skip a case, or delete coverage just to make a test pass. If an existing
  test is genuinely wrong or obsolete, flag it for human review instead of
  silently rewriting it.

## Test data and fixtures
- Use synthetic values in every fixture — no production data or real PII,
  even when copying the shape of a real payload.
- Put reusable factories, builders, or large fixtures in the module's
  existing test-utilities location; keep one-off helpers next to the test
  that needs them.

## Output
- Complete, compilable test class including imports and any setup method.
- No test should depend on execution order or shared mutable static state.
- Note in a one-line comment which coverage items could not be tested and
  why (e.g. no injection seam on the collaborator).
```

## Illustrative Example

### Service-layer test — constructor injection makes this simple

Because `OrderIntakeService` (from the [Code Generation Playbook](../code/java-code-generation.md)) takes its REST client as a constructor parameter, `@InjectMocks` wires a mocked client straight in — no manual wiring, no reflection, no mocking the class under test:

```java
@RunWith(MockitoJUnitRunner.class)
public class OrderIntakeServiceTest {

    @Mock
    private OrderIntakeRestClient orderIntakeRestClient;

    @InjectMocks
    private OrderIntakeService orderIntakeService;

    @Test
    public void submitOrder_success_returnsResponseFromClient() throws Exception {
        // Arrange
        OrderRequestDto request = new OrderRequestDto();
        OrderResponseDto expected = new OrderResponseDto("ACCEPTED");
        when(orderIntakeRestClient.submit(request)).thenReturn(expected);

        // Act
        OrderResponseDto actual = orderIntakeService.submitOrder(request);

        // Assert
        assertEquals("ACCEPTED", actual.getStatus());
    }

    @Test(expected = OrderIntakeServiceException.class)
    public void submitOrder_clientThrows_wrapsInOrderIntakeServiceException() {
        // Arrange
        OrderRequestDto request = new OrderRequestDto();
        when(orderIntakeRestClient.submit(request)).thenThrow(new RestClientException("timeout"));

        // Act: expected exception declared on @Test above
        orderIntakeService.submitOrder(request);
    }
}
```

### Controller-layer test — verifying the exception-to-status contract

`MockMvc` exercises the controller and centralized exception handler together, proving that each domain exception really does produce the HTTP status the API promises:

```java
@RunWith(SpringRunner.class)
@WebMvcTest(OrderIntakeController.class)
public class OrderIntakeControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private OrderIntakeService orderIntakeService;

    @Test
    public void submitOrder_success_returns200WithAcceptedStatus() throws Exception {
        when(orderIntakeService.submitOrder(any(OrderRequestDto.class)))
                .thenReturn(new OrderResponseDto("ACCEPTED"));

        mockMvc.perform(post("/v1/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"customerId\":\"C-1\"}"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.status", is("ACCEPTED")));
    }

    @Test
    public void submitOrder_orderNotFound_returns404() throws Exception {
        when(orderIntakeService.submitOrder(any(OrderRequestDto.class)))
                .thenThrow(new OrderNotFoundException("no such order"));

        mockMvc.perform(post("/v1/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"customerId\":\"C-1\"}"))
            .andExpect(status().isNotFound());
    }
}
```

Together, these two tests cover the layering from the Code Generation Playbook end to end: the service test proves the business logic and exception-wrapping behavior in isolation, and the controller test proves the centralized handler maps that exception to the HTTP status the API contract promises. Testing a REST client (`OrderIntakeRestClient`) follows the same collaborator-mocking shape as the service test above — mock the injected `RestTemplate` and assert on the translated exception type.

### Common anti-pattern — do not imitate

```java
// A "test" that is really a manual script:
public class LegacyManualCheck {
    public static void main(String[] args) {
        System.out.println(buildDebugUrl("Y3140991"));
    }
}

// A "test" that hits a live external system and asserts nothing:
@Test
public void checkLookup() {
    SomeApiClient client = new SomeApiClient();
    Result result = client.lookup("some-id");
    System.out.println(result.toString());
}
```

The first has a `main()` method, not a `@Test` method — it runs under the build's test target as a no-op and asserts nothing. The second is `@Test`-annotated but calls a live external system and only prints the result — no assertion anywhere, and no mocking, so it is a network-dependent manual smoke script wearing a test annotation. Both shapes still turn up in older suites; when asked to add tests near either one, generate a real assertion-based test alongside it rather than extending the pattern.

## Review Checklist

- [ ] Naming follows `{method}_{scenario}_{expectedResult}` (or the file's existing legacy style, consistently).
- [ ] Arrange-Act-Assert structure used in every test method.
- [ ] `@InjectMocks`/constructor mocking used where the class under test is constructor-injected; a documented seam used otherwise.
- [ ] Controller-layer tests use `MockMvc` and assert on HTTP status, not just the return value.
- [ ] Success, not-found, conflicting-state, validation, and downstream-failure scenarios are all covered where applicable.
- [ ] No live network, database, or mail calls in a test that isn't explicitly an integration test.
- [ ] No production data or PII in test fixtures.
- [ ] Untestable seams are called out as a follow-up, not silently skipped.
- [ ] No existing assertion was weakened, no expected value changed, and no coverage deleted just to make a test pass.
- [ ] Any existing test that looked genuinely wrong or obsolete was flagged for human review, not silently rewritten.
- [ ] Reusable fixtures/factories were placed in the module's test-utilities location rather than duplicated across test files.
- [ ] If the class under test is a known risk hotspot, its failure modes got deeper coverage, not just the standard scenario checklist.

## Related Resources

- [README — how this fits GenDD scaffolding](../README.md)
- [Java Code Generation Playbook](../code/java-code-generation.md)
- `docs/playbooks/_repo-context.md` — shared repo context, read before the deeper context/standards files
- `docs/brownfield/gendd/risks/risk-hotspots.md` — informs which classes deserve deeper test coverage
