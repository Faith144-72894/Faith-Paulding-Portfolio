# Architecture Decision Brief | Fictional

**Decision:** Select authoritative transactional data layer.

**Options:** SharePoint Lists, Dataverse, SQL.

**Selected:** Dataverse for transaction state; SharePoint for evidence documents.

**Reason:** Relational structure, role-based security, solution-aware deployment, and workflow integration.

**Cost consideration:** Premium licensing must be validated against user population and app access pattern before production commitment.

**Continuity:** Scheduled export of critical operational data and documented manual intake path during service interruption.
