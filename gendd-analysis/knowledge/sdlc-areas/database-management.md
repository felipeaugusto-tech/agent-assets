# Database Management -- Analysis Knowledge

> This file is used by GenDD-Flow's AI during Phase 3 (Generate Context Per Area).
> It tells the AI what to look for, analyze, and document when evaluating a codebase through the Database Management lens.

## Detection Signals

| Signal | Confidence | Examples |
|--------|-----------|----------|
| Database migration files | HIGH | `migrations/`, `db/migrate/`, Flyway `V*__*.sql`, Alembic `versions/`, EF Core `Migrations/` |
| ORM model definitions | HIGH | `models/`, `entities/`, `*.entity.ts`, `*Model.cs`, `models.py` with ORM base classes |
| Database configuration | HIGH | Connection strings in config, `database.yml`, `ormconfig.ts`, `prisma/schema.prisma` |
| SQL files or stored procedures | MEDIUM | `*.sql`, `procedures/`, `views/`, `functions/` directories |
| Database seed files | MEDIUM | `seeds/`, `seeders/`, `db/seeds/`, seed scripts |
| Schema definition files | MEDIUM | `schema.prisma`, `schema.graphql` with DB directives, `*.dbml` |
| Repository pattern files | LOW | `repositories/`, `*Repository.ts`, `*_repo.go` |
| Database index definitions | LOW | Index annotations in models, migration files creating indexes |

## What to Analyze

### Schema Analysis
- Look for: All tables/collections with their purpose and estimated size
- Look for: Relationships between entities (one-to-one, one-to-many, many-to-many)
- Look for: Primary key strategy (auto-increment, UUID, composite)
- Look for: Foreign key definitions and referential integrity
- Look for: Naming conventions for tables, columns, and constraints
- Assess: Schema normalization level and appropriateness
- Assess: Whether entity relationships are properly constrained at the database level
- Document: Table inventory with purpose, relationships, and schema health assessment

### Migration Strategy
- Look for: Migration tool and version history
- Look for: Reversibility of migrations (up/down scripts)
- Look for: Data migrations (not just schema changes)
- Look for: Zero-downtime migration compatibility (additive changes, backward-compatible)
- Assess: Migration discipline and risk of each pending migration
- Document: Migration summary with tool, count, reversibility, and risk assessment

### Query Pattern Analysis
- Look for: ORM query patterns vs. raw SQL usage
- Look for: N+1 query patterns (loop-based database calls)
- Look for: SELECT * usage (over-fetching)
- Look for: Missing pagination on list queries
- Look for: Cartesian join patterns (accidental cross joins)
- Look for: Complex query locations (joins across many tables)
- Look for: Stored procedures and views
- Assess: Query efficiency and presence of anti-patterns
- Document: Query pattern inventory with anti-patterns found and their locations

### Index Analysis
- Look for: Existing index definitions (in migrations, model annotations, or dedicated files)
- Look for: Columns used in WHERE clauses, JOIN conditions, and ORDER BY without indexes
- Look for: Composite index opportunities (multi-column queries)
- Look for: Potentially unused indexes (indexes on rarely-queried columns)
- Assess: Whether indexing strategy matches query patterns
- Document: Index inventory with recommendations for missing and unused indexes

### Data Integrity
- Look for: NOT NULL constraints on required fields
- Look for: UNIQUE constraints on business keys (email, username, external IDs)
- Look for: CHECK constraints for data validation (ranges, enums, formats)
- Look for: Foreign key constraints for referential integrity
- Look for: Application-level vs. database-level validation gaps
- Assess: Whether data integrity is enforced at the database level or only in application code
- Document: Constraint coverage with gaps where database-level enforcement is missing

### Performance Considerations
- Look for: Large table indicators (audit logs, event tables, historical data)
- Look for: Partitioning configuration
- Look for: Archiving strategy for old data
- Look for: Connection pooling configuration and pool size
- Look for: Timeout handling on database connections
- Look for: Query caching or application-level caching for database data
- Assess: Whether performance-critical areas have appropriate optimization
- Document: Performance assessment with large table analysis, pooling config, and caching strategy

### Backup and Recovery
- Look for: Backup configuration (automated, scheduled, manual)
- Look for: Point-in-time recovery capability
- Look for: Backup testing evidence
- Assess: Whether backup strategy matches data criticality
- Document: Backup and recovery status with strategy, frequency, and test status

## Key Questions to Answer

1. What database engine and ORM are used?
2. How is the schema organized and what are the key entity relationships?
3. What migration strategy is used and are migrations reversible?
4. Are there query anti-patterns (N+1, SELECT *, missing pagination)?
5. Does the indexing strategy match the actual query patterns?
6. Are data integrity constraints enforced at the database level?
7. How are large tables and historical data managed?
8. What is the connection pooling and timeout configuration?
9. Is there a backup and recovery strategy that has been tested?
10. What are the highest-priority database improvements needed?

## Common Patterns to Detect

| Pattern | Indicators | Implication |
|---------|-----------|-------------|
| Repository Pattern | Interface + implementation for data access, abstracted queries | Clean separation, testable data layer |
| Active Record | Models with built-in CRUD methods, model-based queries | Simple but can couple business logic to persistence |
| Unit of Work | Transaction management wrapping multiple operations | Consistent data state, atomic operations |
| CQRS | Separate read/write models, materialized views, projections | Optimized reads, complex but scalable |
| Event Sourcing | Event tables, replay capability, projection handlers | Full audit trail, complex reconstruction |
| Soft Delete | `deleted_at` columns, global query scopes filtering deleted records | Data preservation, but query complexity |
| Multi-Tenant Data | Tenant ID columns, row-level security, schema-per-tenant | Data isolation requirements, query filtering |
| Audit Trail | Created/updated timestamps, audit log tables, change history | Compliance-ready, adds storage overhead |

## Risk Signals

| Risk | Detection Method | Severity |
|------|-----------------|----------|
| No foreign key constraints | Missing FK definitions, orphan data possible | HIGH |
| N+1 query patterns | Loop-based DB calls in service/controller code | HIGH |
| Missing indexes on filtered columns | WHERE clauses on non-indexed columns | MEDIUM |
| No migration reversibility | Missing down/rollback scripts | MEDIUM |
| SELECT * in queries | Over-fetching data from database | MEDIUM |
| No connection pooling | New connection per request, no pool config | MEDIUM |
| Missing NOT NULL constraints | Nullable columns that should be required | MEDIUM |
| No backup testing | Backups configured but never tested for restoration | HIGH |
| Hardcoded connection strings | Database credentials in source code | HIGH |
| No pagination on list queries | Unbounded result sets returned to client | MEDIUM |
| Data validation only in application | No CHECK or UNIQUE constraints at DB level | LOW |

## Output Guidance

### Must Include
- Database engine, ORM, and schema version
- Table inventory with key relationships (entity-relationship summary)
- Migration strategy summary with tool, reversibility, and discipline assessment
- Query anti-patterns found with locations and severity
- Data integrity constraint coverage assessment

### Should Include (if detected)
- Index analysis with missing and unused index recommendations
- Performance assessment for large tables (partitioning, archiving)
- Connection pooling and timeout configuration
- Backup and recovery status
- ER diagram (Mermaid format) for key entity relationships

### Related Areas
- [backend-development](./backend-development.md) -- data access patterns, repository layer, ORM usage
- [architecture](./architecture.md) -- data architecture within system design
- [security](./security.md) -- data encryption, PII storage, access control
- [site-reliability](./site-reliability.md) -- database monitoring, connection health
- [devops-infrastructure](./devops-infrastructure.md) -- database infrastructure, managed services
