# Angular Unit Test Generation Playbook

| Field | Value |
|---|---|
| **Category** | on-demand (Generate Unit Tests) |
| **Target roles** | Frontend Developer, Fullstack Developer, QA Automation Engineer |
| **Prerequisites** | `docs/playbooks/_repo-context.md` (if present), `docs/context/quality-assurance.md`, `docs/standards/testing.md`, one reference spec file from the same or a structurally similar feature area |
| **Inputs** | Path to the component/service under test, reference spec file |
| **Outputs** | Complete spec file(s) covering creation, inputs/outputs, branches, and success/error paths |
| **Save to** | Co-located with the unit under test, in the same feature area |
| **Related playbook** | [Angular Code Generation](../code/angular-code-generation.md) — write testable, DI-friendly code at code-gen time, not after |

## What Is This Playbook?

A repeatable procedure for asking an AI coding assistant to generate unit tests for an Accurate Angular application that match that app's actual test framework and mocking style — not a generic template borrowed from a different testing ecosystem.

## When to Use This Playbook

- Writing tests for new code produced by the [Angular Code Generation Playbook](../code/angular-code-generation.md).
- Adding coverage to an existing component or service identified as high-risk.
- After a test coverage review flags a component or service with zero tests.

## Before You Start

- [ ] `docs/playbooks/_repo-context.md` exists and has been read, if the target repo has one.
- [ ] `docs/context/quality-assurance.md` and `docs/standards/testing.md` are loaded into the assistant's context.
- [ ] You know the test framework actually in use (Karma + Jasmine, or Jest, if the app has migrated) and how HTTP is mocked in existing tests.
- [ ] You have identified one existing spec file in the same feature area as a style reference.
- [ ] You've checked `docs/brownfield/gendd/risks/risk-hotspots.md` (or the repo's equivalent brownfield risk doc) — if the component/service under test is a listed hotspot, prioritize it and cover its failure modes more thoroughly, not just the standard scenario list.

## Typical Conventions a Testing Standard Should Capture

**Requirement levels used in the table below — `MUST`:** required; a change should not be considered done, or merged, without it. **`SHOULD`:** the strong default; follow it unless there's a specific, stated reason to deviate.

| Standard | Requirement Level | Notes |
|---|---|---|
| Co-locate spec files with the unit under test | MUST | `name.component.spec.ts`, `name.service.spec.ts` |
| Use `TestBed` with a minimal set of declared providers/imports | MUST | Only what the specific unit needs |
| Mock HTTP via the framework's testing utilities rather than a real backend | MUST | E.g. `HttpTestingController`, or the app's existing HTTP-mocking convention |
| Mock injected services with a spy/stub rather than instantiating the real collaborator | SHOULD | Keeps component tests fast and isolated |
| Assert on rendered output, emitted values, or Observable results — not private component state | MUST | |
| Shared factories, builders, and large fixtures live in a dedicated test-utilities directory | SHOULD | Promote to it only once reused across multiple spec files; keep tiny one-off helpers next to the spec that needs them |
| No production data or real PII in any test fixture | MUST | Use synthetic values even when copying the shape of a real payload |

Typical coverage priorities:

- Component creation ("should be created").
- Each `@Input`/`@Output` behavior variation.
- Each conditional template branch (empty list, single item, error state).
- Service methods: success and error path for each Observable-returning method.
- Route guard allow/deny cases, if the app uses guards.
- Form validation edge cases, if the component has a form.

## The Prompt Template (Full)

Copy this into your AI coding assistant, fill in the bracketed placeholders, and attach the component/service under test plus one existing spec file from the same feature area as a style reference.

```
Read @docs/playbooks/_repo-context.md (if present)
Read @docs/context/quality-assurance.md
Read @docs/standards/testing.md
Read @docs/brownfield/gendd/risks/risk-hotspots.md (if present) — if the
unit under test is listed, cover its failure modes more thoroughly

You are generating unit tests for [TARGET REPO].

## Unit(s) under test
[Paste or reference the component/service]

## Reference test style
[Paste or reference an existing spec file from the same feature area, or a
structurally similar one, so the assistant matches TestBed setup, mocking
style, and assertion style already in use.]

## Test framework
- Match the test framework already used in this app (Karma + Jasmine, or
  Jest if migrated) — do not introduce a different one.
- Use TestBed to construct the fixture; declare only the providers/imports
  this specific unit needs.
- Mock HTTP with the framework's testing utilities (e.g.
  HttpTestingController), not a real backend.
- Mock injected services with a spy/stub, matching the reference spec's
  convention.

## Naming & structure
- File: name.component.spec.ts / name.service.spec.ts, co-located with the
  unit under test.
- Top-level describe named after the class.

## Coverage to include
- Component creation.
- Each @Input rendering/behavior variation and each @Output emission.
- Each conditional template branch.
- Service methods: success path and error path for each Observable-
  returning method.
- Route guard allow/deny cases, if testing a guard.
- Form validation: valid/invalid/edge values, if testing a form component.

## Assertions
- Assert on rendered DOM, emitted values, or returned Observable results —
  not on private component fields.
- Change production code to satisfy an existing test's intent, not the
  other way around. Do not weaken, skip, or delete an existing test to
  make a change pass. If an existing test is genuinely wrong or obsolete,
  flag it for human review instead of silently rewriting it; if its
  expectation must change due to a genuine behavior change, call that out
  explicitly.

## Test data and fixtures
- Use synthetic values in every fixture — no production data or real PII,
  even when copying the shape of a real payload.
- Put reusable factories, builders, or large fixtures in the app's
  existing test-utilities location; keep one-off helpers next to the spec
  that needs them.

## Output
- Complete, compilable spec file including imports and TestBed
  configuration.
- No test should depend on execution order or leak state between tests.
```

## Illustrative Example

Continuing the [Angular Code Generation Playbook](../code/angular-code-generation.md) example — testing `OrderIntakeService` and `OrderSummaryComponent`. Names are invented, not drawn from any specific Accurate repository.

### Service test — mocking HTTP

```typescript
describe('OrderIntakeService', () => {
  let service: OrderIntakeService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideHttpClient(), provideHttpClientTesting(), OrderIntakeService],
    });
    service = TestBed.inject(OrderIntakeService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => httpMock.verify());

  it('submitOrder_success_returnsResponse', () => {
    const request: OrderRequest = { customerId: 'C-1' };
    let actual: OrderResponse | undefined;

    service.submitOrder(request).subscribe((response) => (actual = response));

    const req = httpMock.expectOne('/api/v1/orders');
    expect(req.request.method).toBe('POST');
    req.flush({ status: 'ACCEPTED' });

    expect(actual?.status).toBe('ACCEPTED');
  });

  it('submitOrder_serverError_propagatesError', () => {
    const request: OrderRequest = { customerId: 'C-1' };
    let actualError: unknown;

    service.submitOrder(request).subscribe({
      error: (err) => (actualError = err),
    });

    const req = httpMock.expectOne('/api/v1/orders');
    req.flush('server error', { status: 500, statusText: 'Server Error' });

    expect(actualError).toBeTruthy();
  });
});
```

### Component test — mocking the injected service

```typescript
describe('OrderSummaryComponent', () => {
  let fixture: ComponentFixture<OrderSummaryComponent>;
  let component: OrderSummaryComponent;
  let orderIntakeServiceSpy: jasmine.SpyObj<OrderIntakeService>;

  beforeEach(() => {
    orderIntakeServiceSpy = jasmine.createSpyObj('OrderIntakeService', ['submitOrder']);

    TestBed.configureTestingModule({
      imports: [OrderSummaryComponent],
      providers: [{ provide: OrderIntakeService, useValue: orderIntakeServiceSpy }],
    });

    fixture = TestBed.createComponent(OrderSummaryComponent);
    component = fixture.componentInstance;
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });

  it('submit_serviceSucceeds_clearsSubmittingFlag', () => {
    orderIntakeServiceSpy.submitOrder.and.returnValue(of({ status: 'ACCEPTED' }));

    component.submit({ customerId: 'C-1' });

    expect(component.isSubmitting()).toBeFalse();
    expect(component.errorMessage()).toBeNull();
  });

  it('submit_serviceErrors_setsErrorMessage', () => {
    orderIntakeServiceSpy.submitOrder.and.returnValue(throwError(() => new Error('boom')));

    component.submit({ customerId: 'C-1' });

    expect(component.isSubmitting()).toBeFalse();
    expect(component.errorMessage()).toBe('Unable to submit order');
  });
});
```

Because `OrderIntakeService` is injected rather than instantiated inside the component, the component test never needs a real `HttpClient` — it substitutes a Jasmine spy via Angular's dependency-injection configuration. This is the same testability payoff described in the Code Generation Playbook: match the target app's DI style and tests come naturally, without needing to bolt on a separate seam.

### Common anti-pattern — do not imitate

```typescript
describe('OrderSummaryComponent', () => {
  it('should be created', () => {
    expect(component).toBeTruthy();
  });
  // ...no other tests in the entire file, despite the component having
  // a form, a submit handler, and two error states.
});
```

A spec file with only a creation test gives the appearance of coverage — the file exists, the suite is green — without exercising any of the component's actual behavior. When asked to add tests to a component like this, treat the existing "should be created" test as a floor, not a ceiling, and add the missing input/output, branch, and error-path coverage described above.

## Review Checklist

- [ ] Spec file is co-located with the unit under test.
- [ ] `TestBed` declares only the providers/imports this unit needs.
- [ ] HTTP is mocked via the framework's testing utilities, never a real backend.
- [ ] Injected services are mocked with a spy/stub, matching the app's existing convention.
- [ ] Component creation, each `@Input`/`@Output`, each conditional template branch, and each Observable success/error path are covered.
- [ ] Assertions target rendered output, emitted values, or Observable results — not private state.
- [ ] No test depends on execution order or leaks state between tests.
- [ ] Existing tests are not weakened or deleted to make a new test pass; any test that looked genuinely wrong was flagged for human review, not silently rewritten.
- [ ] No production data or PII in test fixtures.
- [ ] Reusable fixtures/factories were placed in the app's test-utilities location rather than duplicated across spec files.
- [ ] If the unit under test is a known risk hotspot, its failure modes got deeper coverage, not just the standard scenario checklist.

## Related Resources

- [README — how this fits GenDD scaffolding](../README.md)
- [Angular Code Generation Playbook](../code/angular-code-generation.md)
- `docs/playbooks/_repo-context.md` — shared repo context, read before the deeper context/standards files
- `docs/brownfield/gendd/risks/risk-hotspots.md` — informs which units deserve deeper test coverage
