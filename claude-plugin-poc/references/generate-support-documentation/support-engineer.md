# Role Playbook: Support Engineer

**Role:** Support Engineer / Customer Support Engineer
**Focus:** Troubleshooting guides, FAQ generation, known issues, supportability
**Time:** 30-45 minutes

---

## Purpose

Analyze a codebase from a Support Engineer perspective to understand:
- How to troubleshoot common issues
- Error messages and their meanings
- Configuration options and their effects
- Known issues and workarounds

---

## Quick Prompt

```
Read @GenDD-Flow/playbooks/by-role/support-engineer.md
Analyze @TargetRepo for supportability and troubleshooting.
```

---

## Full Analysis Prompt

```
Read @GenDD-Flow/playbooks/by-role/support-engineer.md

Analyze @TargetRepo from a Support Engineer perspective:

## Context
- Product Type: [SaaS | Self-hosted | Library | API]
- Support Channels: [Ticket | Chat | Email | Community]
- Common Issues: [Known problem areas if any]
- User Technical Level: [Developer | Technical | Non-technical]

## Phase 1: Error & Message Inventory

### User-Facing Error Messages
| Error Code/Message | Location | Meaning | User Action |
|--------------------|----------|---------|-------------|
| [ERROR_CODE] | `[file:line]` | [What happened] | [What user should do] |

### Error Categories
| Category | Count | Examples | Severity |
|----------|-------|----------|----------|
| Authentication | [n] | Login failed, Token expired | High |
| Validation | [n] | Invalid input, Missing field | Medium |
| Permission | [n] | Access denied, Forbidden | High |
| Server | [n] | Internal error, Timeout | Critical |
| Integration | [n] | API unavailable, Rate limit | High |

## Phase 2: Configuration Analysis

### User-Configurable Settings
| Setting | Location | Default | Description | Impact |
|---------|----------|---------|-------------|--------|
| [Setting] | [env/config] | [value] | [What it does] | [Effect of change] |

### Environment Variables
| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| [VAR_NAME] | Yes/No | [default] | [Purpose] |

### Configuration Pitfalls
| Misconfiguration | Symptom | Resolution |
|------------------|---------|------------|
| [Config issue] | [What user sees] | [How to fix] |

## Phase 3: Logging & Diagnostics

### Log Locations
| Log Type | Location | Format | Retention |
|----------|----------|--------|-----------|
| Application | [path] | [JSON/Text] | [duration] |
| Access | [path] | [format] | [duration] |
| Error | [path] | [format] | [duration] |

### Log Levels
| Level | When Used | Examples |
|-------|-----------|----------|
| ERROR | Critical failures | [examples] |
| WARN | Recoverable issues | [examples] |
| INFO | Normal operations | [examples] |
| DEBUG | Troubleshooting | [examples] |

### Key Log Patterns
| Pattern | Meaning | Action |
|---------|---------|--------|
| `[pattern]` | [What it indicates] | [What to do] |

## Phase 4: Common Issues Analysis

### Inferred Common Issues
| Issue | Evidence | Symptoms | Resolution |
|-------|----------|----------|------------|
| [Issue] | [Code patterns] | [User sees] | [Fix] |

### Error Handling Patterns
| Scenario | How Handled | User Message | Support Action |
|----------|-------------|--------------|----------------|
| [Scenario] | [Code pattern] | [Message] | [What support does] |

## Phase 5: Health Check & Status

### Health Endpoints
| Endpoint | Purpose | Expected Response |
|----------|---------|-------------------|
| /health | Liveness | 200 OK |
| /ready | Readiness | 200 OK + status |

### Status Indicators
| Indicator | Location | Meaning | Troubleshooting |
|-----------|----------|---------|-----------------|
| [Indicator] | [Where visible] | [What it means] | [Steps] |

## Phase 6: Integration Points

### External Dependencies
| Dependency | Purpose | Failure Symptoms | Workaround |
|------------|---------|------------------|------------|
| [Service] | [Why needed] | [What user sees] | [Temporary fix] |

### API Integrations
| Integration | Endpoint | Common Errors | Resolution |
|-------------|----------|---------------|------------|
| [Integration] | [URL pattern] | [Errors] | [Fixes] |

## Phase 7: Troubleshooting Flows

### Issue: [Common Issue 1]
```
Symptom: [What user reports]
│
├─► Check: [First thing to check]
│     │
│     ├─► If [condition]: [Resolution A]
│     │
│     └─► If not: Continue ↓
│
├─► Check: [Second thing to check]
│     │
│     └─► [Resolution B]
│
└─► Escalate to: [Team/Level]
```

### Issue: [Common Issue 2]
```
[Similar flow]
```

## Phase 8: Support Documentation Gaps

### Missing Documentation
| Document | Need | Priority |
|----------|------|----------|
| Troubleshooting guide | [Why needed] | High/Med/Low |
| FAQ | [Why needed] | High/Med/Low |
| Known issues list | [Why needed] | High/Med/Low |

### Incomplete Documentation
| Document | Gap | Impact |
|----------|-----|--------|
| [Doc] | [What's missing] | [Impact on support] |

## Phase 9: Recommendations

### Supportability Improvements
| Improvement | Benefit | Effort |
|-------------|---------|--------|
| [Better error messages] | [Fewer tickets] | [S/M/L] |
| [Add diagnostic endpoint] | [Faster resolution] | [S/M/L] |

### Documentation Needs
| Document | Content | Priority |
|----------|---------|----------|
| [Doc] | [What to include] | P1/P2/P3 |
```

---

## Output: Support Guide

```markdown
# Support Guide: [Project Name]
Generated: [Date]
Analyzed by: Support Engineer Playbook

## Quick Reference

### Health Check
```bash
curl [base-url]/health
```

### Logs Location
- Application: `[path]`
- Error: `[path]`

### Key Configuration
| Setting | Location | Default |
|---------|----------|---------|
| [Key setting] | [where] | [value] |

## Error Code Reference

| Code | Meaning | User Action | Support Action |
|------|---------|-------------|----------------|
| [CODE] | [Meaning] | [What to tell user] | [What to check] |

## Troubleshooting Guides

### Issue: [Issue 1]
**Symptoms:** [What user reports]

**Resolution Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**If unresolved:** [Escalation path]

### Issue: [Issue 2]
[Similar format]

## FAQ

### Q: [Common question 1]
A: [Answer]

### Q: [Common question 2]
A: [Answer]

## Known Issues

| Issue | Workaround | Status | ETA |
|-------|------------|--------|-----|
| [Issue] | [Workaround] | Open/In Progress | [Date] |

## Configuration Guide

### Required Settings
| Setting | Purpose | Example |
|---------|---------|---------|
| [Setting] | [Purpose] | [Example value] |

### Common Misconfigurations
| Mistake | Symptom | Fix |
|---------|---------|-----|
| [Mistake] | [What happens] | [How to fix] |

## Escalation Matrix

| Issue Type | Level 1 | Level 2 | Level 3 |
|------------|---------|---------|---------|
| [Type] | Support | [Team] | Engineering |

## Useful Commands

```bash
# Check application status
[command]

# View recent errors
[command]

# Restart service
[command]
```
```

---

## Follow-Up Actions

For playbook selection guidance, see `playbooks/PLAYBOOK-GUIDE.md`.
