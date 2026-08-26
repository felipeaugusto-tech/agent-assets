# Documentation Generation Guidelines

## Purpose
Guidelines for generating documentation that stays current, avoids redundancy, and scales to large projects.

---

## Core Principles

### 1. Code as Source of Truth

Documentation should **point to code**, not duplicate it.

| ❌ Don't: Embed Code Snippets | ✅ Do: Reference Files |
|------------------------------|------------------------|
| Code snippets get stale | File references stay current |
| Requires manual updates | Developers find live code |
| Creates two sources of truth | Single source of truth |

#### Example

**❌ Wrong: Code snippet (gets stale)**
```markdown
## Payment Processing

```csharp
public class PaymentService
{
    public async Task<PaymentResult> ProcessPayment(string token, int amount)
    {
        var charge = new StripeChargeCreateOptions
        {
            Amount = amount,
            Currency = "usd",
            SourceTokenOrExistingSourceId = token
        };
        // ... 50 more lines
    }
}
```

**✅ Right: File reference (always current)**
```markdown
## Payment Processing

**File:** `Services/PaymentService.cs`  
**Method:** `ProcessPayment()` (lines 21-58)

**Purpose:** Processes Stripe charges and updates user balance

**Key Behaviors:**
- Validates token before charging
- Creates Stripe charge with USD currency
- Updates user balance on success only
- Returns PaymentResult with success/failure status

**Related Files:**
- `Models/PaymentFormData.cs` - Request DTO
- `Controllers/PaymentController.cs` - API endpoint
```

---

### 2. Single Source of Truth (No Redundancy)

Each concept appears in **ONE file only**. Other files link to it.

| Concept | Lives In | Other Files Do |
|---------|----------|----------------|
| System purpose | `overview/system-summary.md` | Link: "See [Overview](../overview/...)" |
| Tech stack | `tech-stack.md` | Link, don't repeat |
| Risk hotspots | `risk-hotspots.md` | Link, don't repeat |
| Test gaps | `test-gaps.md` | Link, don't repeat |
| Architecture | `architecture.md` | Link, don't repeat |

#### Cross-Reference Format
```markdown
## Related Information
- **Tech Stack:** See [Tech Stack](../overview/tech-stack.md)
- **Risks:** See [Risk Hotspots](../risks/risk-hotspots.md)
- **Tests:** See [Test Gaps](../risks/test-gaps.md)
```

---

### 3. Avoid Hard-Coded Counts

Numbers become stale immediately. Use patterns instead.

| ❌ Hard-coded (stale) | ✅ Pattern-based (current) |
|-----------------------|---------------------------|
| "15 service modules" | "Services matching `*Service.cs`" |
| "4 API controllers" | "Controllers in `/Controllers/`" |
| "27 total files" | Run: `find . -name "*.cs" \| wc -l` |

#### Example

**❌ Wrong:**
```markdown
| Directory | Files |
|-----------|-------|
| src/services/ | 15 service modules |
| src/controllers/ | 4 controllers |
```

**✅ Right:**
```markdown
| Directory | Pattern | Purpose |
|-----------|---------|---------|
| `Services/` | `*Service.cs` | Business logic |
| `Controllers/` | `*Controller.cs` | API endpoints |

**To get current counts:**
```bash
find Services -name "*Service.cs" | wc -l
find Controllers -name "*Controller.cs" | wc -l
```
```

---

## Documentation Structure

### Small Projects (< 20 files)

```
docs/
├── README.md              # Navigation (50 lines max)
├── overview/system-summary.md  # Everything in one file (200-300 lines)
└── diagrams/
    └── architecture.mermaid
```

### Medium Projects (20-100 files)

```
docs/
├── README.md              # Navigation only
├── overview/
│   ├── system-summary.md      # What it does
│   └── tech-stack.md          # Technologies
├── architecture/
│   ├── components.md          # Service catalog
│   └── data-ownership.md      # Data map
├── risks/
│   ├── risk-hotspots.md       # Prioritized risks
│   └── test-gaps.md           # Testing needs
└── diagrams/
    ├── context.mermaid
    └── containers.mermaid
```

### Large Projects (100+ files)

```
docs/
├── README.md              # Navigation only (~50 lines)
├── overview/
│   ├── system-summary.md
│   ├── tech-stack.md
│   └── glossary.md
├── architecture/
│   ├── overview.md
│   ├── components/            # One file per major component
│   │   ├── payment-service.md
│   │   ├── auth-service.md
│   │   └── ...
│   └── data-ownership.md
├── flows/                     # One file per major flow
│   ├── payment-flow.md
│   ├── authentication-flow.md
│   └── ...
├── integrations/              # One file per external system
│   ├── stripe.md
│   ├── twilio.md
│   └── ...
├── risks/
│   ├── risk-hotspots.md
│   └── test-gaps.md
└── diagrams/
    ├── README.md              # How to view diagrams
    ├── context.mermaid
    ├── containers.mermaid
    └── flows/
        ├── payment-flow.mermaid
        └── auth-flow.mermaid
```

---

## File Size Limits

| File Type | Max Lines | If Exceeded |
|-----------|-----------|-------------|
| README/Index | 50-100 | Keep as navigation only |
| Overview files | 150-200 | Split by topic |
| Component docs | 100-150 | One component per file |
| Flow docs | 100-150 | One flow per file |
| Risk/Test docs | 150-200 | Split by category |

---

## Diagram Guidelines

### Size Limits

| Diagram Type | Max Nodes | If Exceeded |
|--------------|-----------|-------------|
| Context (L1) | 6 | Split by boundary |
| Container (L2) | 10 | Split by subsystem |
| Component (L3) | 12 | One service per diagram |
| Flow | 12 steps | Split into phases |

### One Concept Per Diagram

**❌ Wrong:** Everything in one diagram
**✅ Right:** Separate diagrams for:
- System context (external actors)
- Containers (major components)
- Each major flow
- Each service's internals

---

## Multi-Phase Approach for Large Projects

When context window is limited, split documentation into phases:

### Phase 1: Scan (Separate Chat)
**Goal:** Inventory only  
**Output:** `pass1-scan.md`  
**Context Usage:** ~20%

```
Scan @TargetRepo and create inventory:
- File types and counts
- Directory structure
- Dependencies detected
- Entry points found

Output ONLY inventory, no analysis.
```

### Phase 2: Infer (Separate Chat)
**Goal:** Architecture analysis  
**Input:** Read pass1-scan.md  
**Output:** `pass2-infer.md`  
**Context Usage:** ~30%

```
Read @docs/pass1-scan.md

Analyze architecture:
- Component responsibilities
- Core flows (top 3-5)
- Data ownership
- Risk hotspots

Output analysis, reference scan findings.
```

### Phase 3: Document (Separate Chat)
**Goal:** Final documentation  
**Input:** Read pass1 + pass2  
**Output:** Split files per structure above  
**Context Usage:** ~40%

```
Read @docs/pass1-scan.md and @docs/pass2-infer.md

Generate documentation:
- Split into files per structure guidelines
- One file per major component/flow
- Reference files, don't embed code
```

### Continuation Prompt

If generation stops mid-way:
```
Continue generating from where you left off.

Previous outputs are in @docs/
Already completed: [list completed files]
Still needed: [list remaining files]

Continue with: [next file name]
```

---

## Quality Checklist

### Before Publishing Documentation

- [ ] No code snippets embedded (file references only)
- [ ] No hard-coded counts (patterns/commands instead)
- [ ] Each concept in ONE file only
- [ ] Cross-references used (not duplication)
- [ ] Files under size limits
- [ ] Diagrams have free viewer links
- [ ] README is navigation only

### Maintenance

- [ ] Review quarterly
- [ ] Update when architecture changes
- [ ] Run count commands to verify patterns
- [ ] Check diagram viewer links work

---

## Template: Component Documentation

```markdown
# {Component Name}

## Purpose
{One sentence description}

## Files

| File | Purpose |
|------|---------|
| `path/to/main.cs` | Main implementation |
| `path/to/interface.cs` | Public interface |
| `path/to/tests.cs` | Test coverage |

## Key Behaviors
- {Behavior 1}
- {Behavior 2}
- {Behavior 3}

## Dependencies
- **Uses:** {List services this depends on}
- **Used By:** {List services that depend on this}

## Related Documentation
- Architecture: See [Components Overview](../architecture/components.md)
- Risks: See [Risk Hotspots](../risks/risk-hotspots.md#component-name)
- Tests: See [Test Gaps](../risks/test-gaps.md#component-name)
```

---

## Template: Flow Documentation

```markdown
# {Flow Name}

## Trigger
{What initiates this flow}

## Steps

1. **{Step 1}** - `path/to/file.cs:methodName()`
2. **{Step 2}** - `path/to/file2.cs:methodName()`
3. **{Step 3}** - `path/to/file3.cs:methodName()`

## Diagram
See: [Flow Diagram](../diagrams/flows/{flow-name}.mermaid)

## Error Handling
| Error | Handled In | User Sees |
|-------|------------|-----------|
| {Error 1} | `file.cs` | {Message} |

## Related
- Component: See [{Component}](../architecture/components/{name}.md)
- Tests: See [Test Scenarios](../risks/test-gaps.md#{flow-name})
```

