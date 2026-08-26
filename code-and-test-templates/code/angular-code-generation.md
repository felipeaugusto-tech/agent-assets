# Angular Code Generation Playbook

| Field | Value |
|---|---|
| **Category** | on-demand (Code Generation) |
| **Target roles** | Frontend Developer, Fullstack Developer, Tech Lead |
| **Prerequisites** | `docs/playbooks/_repo-context.md` (if present), `docs/context/frontend-development.md`, `docs/standards/coding.md`, 2-3 reference files of the same kind |
| **Inputs** | Task description, target feature area, reference file paths |
| **Outputs** | New component(s)/service(s) matching the target app's conventions |
| **Save to** | The feature area matching the change, following the target app's existing layout |
| **Related playbook** | [Angular Unit Test Generation](../test/angular-unit-test-generation.md) — test the code this playbook produces |

## What Is This Playbook?

A repeatable procedure for asking an AI coding assistant to write new production Angular/TypeScript code for an Accurate application so the result matches that application's real conventions on the first pass. Accurate's Angular applications range from single standalone SPAs to micro-frontends composed at runtime — this playbook asks the assistant to detect which shape applies before generating routing or bootstrap code, rather than assuming a plain single-app default.

## When to Use This Playbook

- Adding a new component, page, or feature area.
- Adding a new data-fetching service.
- Adding a new route.
- Extending an existing component or service with a new use case.

## Before You Start

- [ ] `docs/playbooks/_repo-context.md` exists and has been read, if the target repo has one — it carries repo identity, key paths, and risk hotspots that the deeper context files below assume you already know.
- [ ] `docs/context/frontend-development.md` has been generated for the target repo.
- [ ] `docs/standards/coding.md` is loaded into the assistant's context.
- [ ] You know which existing component/service in the target repo is the closest structural match to what you're building.
- [ ] You know whether the app uses standalone components or `NgModule`s, and whether it is a single application or one piece of a micro-frontend composed at runtime — this changes how routing and bootstrap code should be written.
- [ ] You've checked whether the target feature area is a known dangerous change zone in `docs/brownfield/gendd/risks/risk-hotspots.md` (or the repo's equivalent brownfield risk doc) — if so, extra care and review are warranted, not just the standard pass.
- [ ] Any "existing convention" you're relying on from brownfield/context docs is either marked CONFIRMED, or you've verified it against the actual reference files rather than trusting an INFERRED-and-unvalidated claim.

## Typical Conventions a Coding Standard Should Capture

**Requirement levels used in the tables below — `MUST`:** required; a change should not be considered done, or merged, without it. **`SHOULD`:** the strong default; follow it unless there's a specific, stated reason to deviate.

Core principles common to a well-formed Angular coding standard at Accurate:

1. Match the component style already in use (standalone components, or `NgModule`-declared) — do not mix both in the same feature area.
2. Put HTTP calls in an injectable service using `HttpClient`; never call `HttpClient` directly from a component.
3. Default to the simplest state-management approach that fits the app's complexity — component-local signals, plus a small injectable service (RxJS `Subject`/`BehaviorSubject`) for state shared across components. Reach for a full state-management library only if the app already uses one.
4. Use Reactive Forms for new forms unless the app already standardizes on template-driven forms.
5. Match the app's existing styling system (a utility-first CSS framework, component-scoped stylesheets, or a shared internal component library) rather than introducing a second one. Where component-scoped CSS is hand-written, follow BEM naming (`block__element--modifier`) so selectors stay self-descriptive to a human reader.
6. Lazy-load new routed features rather than adding them to an eagerly-loaded root module or route.
7. If the app is a micro-frontend (host or remote), confirm what it exposes/consumes before adding new root-level routes or bootstrap logic — changes there can break the composition contract with other apps.
8. Prefer semantic HTML (`button`, `nav`, `main`, `h1`–`h6`, `label` tied to inputs) and the app's shared design-system primitives (Button, Input, Dialog, Form helpers) over raw `div`/`span` with click handlers.
9. Never place untrusted input into `innerHTML`, `[innerHTML]`, or a `bypassSecurityTrust*` call without the framework's default escaping or an explicit, vetted sanitizer.
10. Leave no temporary scaffolding in the final diff: no `TODO`/`FIXME` standing in for unfinished work, no large commented-out blocks, no ad-hoc `console.log` debugging left behind.

If the task introduces a new key dependency, a new state-management/styling pattern, or a cross-cutting change the app doesn't already use, flag this explicitly and recommend the team capture the decision in an ADR (`docs/adr/`) before or alongside the change.

A representative naming and structure standard:

| Element | Convention | Illustrative example |
|---|---|---|
| Component/service files | kebab-case + Angular type suffix | `order-summary.component.ts`, `order-intake.service.ts` |
| Classes | PascalCase | `OrderIntakeService`, `OrderSummaryComponent` |
| Component selectors | kebab-case with the app's configured prefix | `app-order-summary` |
| Constructor injection | `private readonly <name>: <Type>` | `constructor(private readonly http: HttpClient) {}` |
| Spec files | co-located `<name>.spec.ts` | `order-intake.service.spec.ts` |
| CSS classes (hand-written, component-scoped) | BEM: `block__element--modifier` | `order-summary__title--highlighted` |

Accessibility standards every new UI component should meet:

| Standard | Requirement Level | Notes |
|---|---|---|
| Use semantic elements instead of `div`/`span` with click handlers | MUST | `button`, `nav`, `main`, headings, `label` tied to inputs |
| Give icon-only buttons and custom/composite widgets an accessible name | MUST | Visible text, `aria-label`, or `aria-labelledby` |
| Support full keyboard operation | MUST | Logical focus order, visible focus styles, Escape to dismiss, arrow-key patterns for composite widgets |
| Meet contrast requirements for text and critical states (focus, error) | MUST | Against the app's design tokens or the WCAG-aligned checks already in CI |
| Text can be resized/zoomed up to 200% without loss of content or function | MUST | Use relative units (rem/em) for font sizing; avoid fixed-height containers that clip enlarged text |

UI consistency standards:

| Standard | Requirement Level | Notes |
|---|---|---|
| UI is responsive across the app's supported breakpoints | MUST | Layouts reflow rather than requiring horizontal scrolling or breaking at mobile/tablet widths |
| Use the app's shared Button/Input/Dialog/Form primitives instead of raw HTML | MUST | Keeps focus, variants, and pointer styles consistent |
| Confirmation/destructive-action dialogs use the app's standard dialog chrome and button variants | SHOULD | Disable Cancel and the primary action while the mutation is in flight |
| Bottom action rows (dialog/sheet footers, sticky submit bars) align actions to the end with a gap utility | SHOULD | Avoid margin-only spacing between buttons |
| Client-side validation mirrors server validation; field errors are shown inline, API errors via toast/banner | MUST | Keep client and server rules in sync |
| After a successful create/update, show a success toast or inline message before navigating/refetching | SHOULD | |
| Scrollable regions use the app's scroll container primitive with a bounded height | SHOULD | Not ad hoc `overflow` on a generic `div` without a real height bound |
| Large or sortable data tables define sort, at least one meaningful filter, explicit empty/loading states, and `aria-label`s on icon-only row actions | SHOULD | Put navigation on the entity's name/title rather than a redundant "View" column |

Security standards:

| Standard | Requirement Level | Notes |
|---|---|---|
| Never place untrusted input into `innerHTML`/`bypassSecurityTrust*` without sanitization | MUST | Rely on Angular's default interpolation escaping instead |
| Never hardcode secrets or API keys in frontend source | MUST | Read from build-time environment configuration |

## The Prompt Template (Full)

Copy this into your AI coding assistant, fill in the bracketed placeholders, and attach the reference files it names before running it.

```
Read @docs/playbooks/_repo-context.md (if present)
Read @docs/context/frontend-development.md
Read @docs/standards/coding.md
Read @docs/brownfield/gendd/risks/risk-hotspots.md (if present) — flag if the
target feature area is a known dangerous change zone

You are generating production Angular/TypeScript code for [TARGET REPO].

## Task
[Describe the feature/change: what it does, why it's needed, where it fits —
e.g. "Add a component that lets a user review and submit an order,
following the existing order-intake feature pattern."]

## Target location
- Feature area: [e.g. src/app/features/<feature>/]
- Reference files to read first (do not guess conventions — copy them):
  [list 2-3 real existing files of the same kind in the target repo — a
  sibling component, its service, and its spec file]

## Structure constraints
- Match the component style already in use (standalone vs. NgModule-
  declared) — do not mix both in the same feature area.
- Put HTTP calls in an injectable service using HttpClient, returning an
  Observable (or wrapped in a signal, matching the app's existing style).
  Never call HttpClient directly from a component.
- Lazy-load this feature if it is newly routed — do not add it to an
  eagerly-loaded root module or route.
- If the app is a micro-frontend (host or remote), do not change what it
  exposes/consumes, its root bootstrap sequence, or its base-href handling
  unless the task explicitly calls for it — these changes can break the
  composition contract with other apps.

## State management
- Use the app's existing lightweight pattern (component-local signals,
  plus an injectable service with an RxJS Subject for cross-component
  state) unless the app already uses a dedicated state-management library
  — in that case, follow its existing store pattern instead.

## Styling
- Match the app's existing styling system (utility classes, component-
  scoped stylesheets, or a shared internal component library). Do not
  introduce a second design system or a new UI component library.
- If writing component-scoped CSS by hand, follow BEM naming
  (`block__element--modifier`) rather than ad hoc class names.

## Forms (if applicable)
- Use Reactive Forms unless the app already standardizes on template-
  driven forms — match whichever the sibling components use.
- Client-side validation mirrors server validation. Surface field errors
  inline via the form field wrappers already in use; surface API errors
  through a toast/banner rather than only a root-level form error. Show a
  success toast/message after a successful create/update before
  navigating or refetching.

## Accessibility
- Use semantic elements (`button`, `nav`, `main`, headings, `label` tied to
  inputs) instead of `div`/`span` with click handlers.
- Give icon-only buttons and custom/composite widgets an accessible name
  (visible text, `aria-label`, or `aria-labelledby`).
- Support full keyboard operation: logical focus order, visible focus
  styles, Escape to dismiss, arrow-key patterns for composite widgets.
- Meet contrast requirements for text and critical states (focus, error)
  against the app's design tokens.
- Text can be resized/zoomed to 200% without breaking layout or losing
  content/function — use relative units (rem/em), not fixed-height
  containers that clip text.

## UI consistency (if applicable)
- The UI is responsive across the app's supported breakpoints
  (mobile/tablet/desktop) — layouts reflow rather than break or require
  horizontal scrolling.
- Use the app's shared Button/Input/Dialog/Form primitives instead of raw
  HTML where an equivalent exists.
- Confirmation/destructive-action dialogs use the app's standard dialog
  chrome; disable Cancel and the primary action while the mutation is in
  flight.
- Bottom action rows align to the end using a gap utility, not
  margin-only spacing.
- Scrollable regions use the app's scroll container primitive with a
  bounded height, not ad hoc `overflow` without a real height bound.
- Data tables/lists define sort, at least one meaningful filter (if the
  list is large), explicit empty/loading states, and `aria-label`s on
  icon-only row actions; put navigation on the entity's name/title rather
  than a redundant "View" column.

## Security
- Never place untrusted input into `innerHTML`, `[innerHTML]`, or a
  `bypassSecurityTrust*` call without the framework's default escaping or
  an explicit, vetted sanitizer.
- Never hardcode secrets or API keys in frontend source; read them from
  build-time environment configuration.

## Naming conventions
- Files: kebab-case with the Angular type suffix (`.component.ts`,
  `.service.ts`).
- Classes: PascalCase. Constructor injection: `private readonly <name>:
  <Type>`.
- Component selectors: kebab-case with the app's configured prefix.

## Dependencies
Use only libraries already present in the app's package.json. Do not add a
new UI, date, or state-management library duplicating one already in use.

## Code quality
Guard clauses and early returns over deep nesting; small, single-purpose
functions and intention-revealing names over comments; no leftover TODOs,
commented-out blocks, or `console.log` debugging. Code must pass the
project's configured linters/formatters with no new violations, and must
not loosen existing TypeScript strictness settings.

## Documentation
If this change alters a user-facing flow, a component's public API
(`@Input`/`@Output`), or configuration, update the doc that already owns
that topic (README section or guide) in the same change.

## Output
- Production code only (tests are requested separately — see the Unit Test
  Generation Playbook).
- Include all necessary imports.
- If you deviate from any constraint above, state why in a one-line comment
  at the top of the file.
```

## Illustrative Example

The example below shows a typical standalone-component feature: an injectable service for data fetching, and a component that uses signals for local state. Names are invented, not drawn from any specific Accurate repository.

```typescript
@Injectable({ providedIn: 'root' })
export class OrderIntakeService {
  constructor(private readonly http: HttpClient) {}

  submitOrder(request: OrderRequest): Observable<OrderResponse> {
    return this.http.post<OrderResponse>('/api/v1/orders', request).pipe(
      catchError((err) => {
        console.error('Error submitting order:', err);
        return throwError(() => err);
      })
    );
  }
}
```

```typescript
@Component({
  selector: 'app-order-summary',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './order-summary.component.html',
  styleUrl: './order-summary.component.css',
})
export class OrderSummaryComponent {
  protected readonly isSubmitting = signal(false);
  protected readonly errorMessage = signal<string | null>(null);

  constructor(private readonly orderIntakeService: OrderIntakeService) {}

  submit(request: OrderRequest): void {
    this.isSubmitting.set(true);
    this.errorMessage.set(null);
    this.orderIntakeService.submitOrder(request).subscribe({
      next: () => this.isSubmitting.set(false),
      error: () => {
        this.isSubmitting.set(false);
        this.errorMessage.set('Unable to submit order');
      },
    });
  }
}
```

Template and stylesheet for `OrderSummaryComponent` (referenced by `templateUrl`/`styleUrl` above), using semantic form elements and BEM class names:

```html
<form class="order-summary" (ngSubmit)="submit({ customerId: customerIdInput.value })">
  <h2 class="order-summary__title">Submit order</h2>

  <label class="order-summary__label" for="customerId">Customer ID</label>
  <input
    class="order-summary__input"
    id="customerId"
    name="customerId"
    type="text"
    required
    #customerIdInput
  />

  <p class="order-summary__error" *ngIf="errorMessage() as message" role="alert">
    {{ message }}
  </p>

  <button
    class="order-summary__submit"
    type="submit"
    [disabled]="isSubmitting()"
    [attr.aria-busy]="isSubmitting()"
  >
    {{ isSubmitting() ? 'Submitting…' : 'Submit order' }}
  </button>
</form>
```

```css
.order-summary {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  max-width: 28rem;
}

.order-summary__title {
  font-size: 1.25rem;
  font-weight: 600;
}

.order-summary__label {
  font-size: 0.875rem;
}

.order-summary__input {
  padding: 0.5rem;
  border: 1px solid var(--color-border, #ccc);
  border-radius: 0.25rem;
}

.order-summary__error {
  color: var(--color-error, #b00020);
  font-size: 0.875rem;
}

.order-summary__submit {
  align-self: flex-end;
}

/* Responsive: single-column layout already holds at narrow widths since
   .order-summary is a column flex container; cap width only above mobile. */
@media (max-width: 480px) {
  .order-summary {
    max-width: 100%;
  }
}
```

Note the BEM class names (`order-summary__title`, `order-summary__label`, ...) and the semantic `label`/`input`/`button` elements rather than `div`s with click handlers — the same accessibility and naming conventions called out above, applied to markup and styles rather than TypeScript.

Lazy route registration for the new feature:

```typescript
{
  path: 'orders',
  loadComponent: () =>
    import('./order-summary.component').then((m) => m.OrderSummaryComponent),
}
```

Because `OrderIntakeService` is constructor-injected into `OrderSummaryComponent`, the component is already testable — a test can supply a mock/spy in place of the real service via Angular's dependency-injection configuration. No extra seam is needed, the same principle as the Java constructor-injection example in the [Java Code Generation Playbook](java-code-generation.md).

## Review Checklist

- [ ] Component style (standalone vs. NgModule) matches the target app — not mixed.
- [ ] All HTTP calls go through an injectable service, not directly from a component.
- [ ] New routed features are lazy-loaded.
- [ ] State management matches the app's existing approach — no new state library introduced without cause.
- [ ] Styling matches the app's existing design system — no second one introduced.
- [ ] Naming, file structure, and selector prefix match the app's existing convention.
- [ ] If the app is a micro-frontend, its composition contract (exposed/consumed modules, bootstrap sequence) is untouched unless the task requires it.
- [ ] TypeScript strictness settings already in place are satisfied, not loosened.
- [ ] Semantic HTML and the app's shared design-system primitives are used instead of raw `div`/`span` with click handlers.
- [ ] Icon-only buttons and custom widgets have an accessible name; keyboard operation and focus-visible styles work; contrast meets the app's tokens; text can be resized/zoomed to 200% without breaking layout.
- [ ] UI is responsive across the app's supported breakpoints — no horizontal scrolling or broken layout at mobile/tablet widths.
- [ ] Hand-written component-scoped CSS classes follow BEM naming (`block__element--modifier`).
- [ ] Confirmation/destructive dialogs use the app's standard chrome and disable actions while a mutation is in flight.
- [ ] Client-side validation mirrors server validation; field errors are inline and API errors surface via toast/banner; a success message shows after a successful mutation.
- [ ] Scrollable regions use the app's scroll primitive with a bounded height; large/sortable tables have sort, a filter, empty/loading states, and `aria-label`s on icon-only actions.
- [ ] No untrusted input reaches `innerHTML`/`bypassSecurityTrust*` without sanitization; no hardcoded secrets or API keys in frontend source.
- [ ] No leftover TODOs, commented-out code, or `console.log` debugging; code passes the project's linters/formatters.
- [ ] If the change alters a user-facing flow or component API, the doc that owns that topic was updated.
- [ ] If the change touches a known risk hotspot, that was called out explicitly rather than treated as a routine change.

## Related Resources

- [README — how this fits GenDD scaffolding](../README.md)
- [Angular Unit Test Generation Playbook](../test/angular-unit-test-generation.md)
- `docs/playbooks/_repo-context.md` — shared repo context, read before the deeper context/standards files
- `docs/brownfield/gendd/risks/risk-hotspots.md` — known dangerous change zones for the target repo
