# Analyze Database Schema

| Field | Value |
|-------|-------|
| **Category** | on-demand |
| **Target Roles** | DBA, Backend Dev, Architect |
| **Prerequisites** | Repository cloned, database schema files or ORM models accessible |
| **Inputs** | Path to the target repository, database type (SQL Server, PostgreSQL, etc.) |
| **Outputs** | Schema analysis report covering structure, relationships, migration health, and optimization opportunities |

## When to Use

- Onboarding onto a project and need to understand the data model
- Reviewing schema changes before a migration
- Auditing data health, naming conventions, and index usage

## Before You Start

- [ ] Repository is cloned and accessible
- [ ] You can identify where schema definitions live (migrations, ORM models, SQL files)
- [ ] You know the database engine in use

## Steps

1. **Identify schema sources**
   - Do: Locate all database-related files in the repository
   - How: Search for migration files, ORM model definitions, SQL scripts, and seed data
   - Expect: A list of all schema source files and their locations

2. **Run the DBA role-playbook analysis**
   - Do: Perform a role-specific deep analysis of the data layer
   - How: Use the following prompt:
     ```
     Read @GenDD-Flow/playbooks/by-role/dba.md

     Analyze @TargetRepo focusing on the database layer.

     Generate:
     1. Schema inventory (tables, views, stored procedures)
     2. Relationship map (foreign keys, join patterns)
     3. Migration history and health
     4. Naming convention audit
     5. Index usage and optimization opportunities
     6. Data ownership boundaries
     7. Risk areas (missing constraints, orphan tables, N+1 patterns)
     ```
   - Expect: A comprehensive data layer analysis

3. **Document findings**
   - Do: Save the analysis as a structured report
   - How: Save to `@TargetRepo/docs/database-analysis.md`
   - Expect: A reference document for the team's data layer understanding

## Expected Output

```
TargetRepo/docs/
└── database-analysis.md
```

**Save to:** `@TargetRepo/docs/database-analysis.md`

## What's Next

- [ ] [Run Brownfield Analysis](../onboarding/run-brownfield-analysis.md) if full codebase analysis is needed
- [ ] [Run Delta Analysis](run-delta-analysis.md) after schema changes to assess impact

## Related Resources

| Resource | Path | Description |
|----------|------|-------------|
| DBA Role Playbook | `playbooks/by-role/dba.md` | Deep-dive DBA analysis prompt |
