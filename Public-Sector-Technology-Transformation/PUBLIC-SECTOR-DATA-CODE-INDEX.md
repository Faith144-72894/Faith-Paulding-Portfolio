# Public Sector Data & Code Architecture Index

This section shows how each public-sector role moves from business problem to governed data to executable logic.

| Role | Data Context | Code Structure | Primary Operational Question |
|---|---|---|---|
| Senior Technical Program Manager | Workstreams, milestones, dependencies, decisions, risks, UAT | readiness scoring, overdue-decision query, milestone measures | Can the next release actually ship? |
| Solutions Architect | systems, interfaces, identities, decisions, environments, costs | integration queue, retry policy, architecture rules | How should the fragmented environment connect safely? |
| Customer Solutions Manager | target users, active users, blockers, usage, value | adoption cohort query, recovery prioritization | Is the customer realizing value after launch? |
| Data & AI Lead | data products, freshness, quality, permissions, AI use, review | AI release gate, freshness exceptions, telemetry controls | Is the data safe and current enough for analytics/AI? |
| Cloud Transformation PM | workloads, dependencies, waves, rollback, criticality | cutover gate, readiness query | Can this workload move without interrupting operations? |
| Technology Delivery Lead | RAID, impact, age, owner, recovery | escalation rules, blocker-aging query | What is blocking delivery and what is the recovery path? |
| Decision Intelligence Lead | KPI registry, thresholds, source, owner, forecast | DAX measures, freshness query, exception model | What requires leadership action now or next? |
| AI Transformation PM | use cases, value, readiness, risk, owner, outcome | prioritization engine, production gate | Which AI use cases deserve production investment? |
| Power Platform Architect | requests, users, roles, workflow states, audit history | Power Fx, automation expressions, DAX | How does the end-to-end workflow operate and recover? |
| Financial Systems Modernization Manager | budget, obligations, expenditures, forecast, milestone impact | SQL execution model, pressure classifier, DAX | Where will financial pressure affect delivery? |

Every sample dataset is fictional and designed to demonstrate operating logic, not represent a real customer or agency.
