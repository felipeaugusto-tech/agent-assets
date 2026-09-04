# Infrastructure Phase Standards

**Rule-ID prefix:** `INF`

## Purpose

Infrastructure standards govern how systems are provisioned, configured, and maintained. They prevent manual drift, enforce security defaults, and ensure infrastructure can be reproduced, version-controlled, and audited.

## Standards in this phase

| File | Rule IDs | Summary |
|---|---|---|
| [`infrastructure-as-code.md`](infrastructure-as-code.md) | INF-001 | IaC required, modularity, state management |
| [`configuration-management.md`](configuration-management.md) | INF-002 | Config vs code, per-environment config, no secrets |
| [`immutability.md`](immutability.md) | INF-003 | Immutable infrastructure and drift prevention |
| [`resource-tagging.md`](resource-tagging.md) | INF-004 | Ownership, cost, and environment tags |

## Tech overlays

| Technology | Folder | Applies to |
|---|---|---|
| Terraform | [`terraform/`](terraform/README.md) | `**/*.tf`, `**/*.tfvars` |

## Agent routing note

Load this index first. For Terraform files, also open the Terraform overlay.
