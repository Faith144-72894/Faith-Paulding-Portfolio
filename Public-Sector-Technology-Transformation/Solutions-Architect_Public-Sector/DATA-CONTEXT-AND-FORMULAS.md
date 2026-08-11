# Data Context, Formulas & Code | Public Sector Solutions Architect

## Data Story
The architecture dataset represents the technical estate behind a customer capability. Each record identifies an application, data store, interface, identity boundary, environment, license dependency, security classification, or architecture decision.

## Grain & Sources
One row per architecture component or integration. Sources include application inventory, API catalog, Entra groups, environment inventory, licensing records, data catalog, architecture decision records, and security review outputs.

## Key Relationships
Application 1:M Interfaces • Application M:M Data Products • Environment 1:M Components • Architecture Decision 1:M affected components • Role M:M Application through access mapping.

## Calculations
Integration Risk Score = Criticality × Failure Probability × Dependency Count

Architecture Debt % = Components with temporary/unapproved patterns / Total components

Premium License Exposure = Premium users × estimated unit cost

Interface Availability = Successful transactions / Total transactions

## SQL
    SELECT SourceSystem, TargetSystem,
           COUNT(*) AS TransactionCount,
           SUM(CASE WHEN Status='Failed' THEN 1 ELSE 0 END) AS Failures,
           CAST(SUM(CASE WHEN Status='Failed' THEN 1 ELSE 0 END) AS decimal(12,4))/NULLIF(COUNT(*),0) AS FailureRate
    FROM IntegrationTelemetry
    GROUP BY SourceSystem, TargetSystem;

## Python
    def architecture_risk(criticality, failure_probability, downstream_dependencies):
        return round(criticality * failure_probability * max(downstream_dependencies,1), 2)

## Design Rule
A component cannot move to production unless ownership, identity, environment, data classification, integration dependency, support path, license requirement, and fallback method are documented.

## Decisions Supported
Dataverse vs SharePoint vs SQL • API vs batch • premium vs standard capability • synchronous vs queued integration • production environment placement • identity model • AI grounding architecture • resilience pattern.
