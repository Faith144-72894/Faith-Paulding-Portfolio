# Public Sector Dataset → Formula → Decision Crosswalk

This page ties the fictional sample datasets directly to the formulas and decisions used in each public-sector role case. The goal is to show exactly **which columns feed each metric, how the calculation works, and what decision the result supports**.

## 1. Senior Technical Program Manager | delivery_control.csv

**Columns used:** `workstream`, `owner`, `planned_finish`, `percent_complete`, `health`, `dependency`, `decision_due`, `uat_pass_rate`, `continuity_ready`.

### Portfolio Completion
Excel structured formula:

    =AVERAGE(delivery_control[percent_complete])/100

DAX:

    Portfolio Completion % = DIVIDE(AVERAGE(delivery_control[percent_complete]),100,0)

**Meaning:** average completion across the active workstreams.

**Decision:** whether the portfolio is progressing evenly or one workstream is materially behind.

### Decision Aging / Overdue Decision

    =MAX(0,TODAY()-[@decision_due])

SQL:

    CASE WHEN decision_due < CAST(GETDATE() AS date)
         THEN DATEDIFF(day, decision_due, GETDATE())
         ELSE 0 END AS decision_days_overdue

**Decision:** escalate overdue customer or leadership decisions before they affect the release path.

### UAT Readiness

    =AVERAGE(delivery_control[uat_pass_rate])/100

**Decision:** whether testing evidence is mature enough to support release readiness.

### Continuity Coverage

    =COUNTIF(delivery_control[continuity_ready],"Yes")/ROWS(delivery_control[continuity_ready])

**Decision:** whether the current operating method can remain available if release activity slips or fails.

### Composite Release Readiness
Health is converted to Green=1, Amber=.5, Red=0.

    Release Readiness =
    (Average percent_complete/100 * 0.30)
    + (Average uat_pass_rate/100 * 0.30)
    + (Continuity Coverage * 0.20)
    + (Average Health Score * 0.20)

**Decision rule:** No-Go if `continuity_ready = No` on a critical workstream or if composite readiness is below the agreed release threshold.

---

## 2. Solutions Architect | architecture_inventory.csv

**Columns used:** `component`, `current_state`, `target_pattern`, `data_owner`, `identity_pattern`, `integration`, `criticality`, `estimated_monthly_cost`, `continuity_method`.

### Estimated Monthly Architecture Run Rate

    =SUM(architecture_inventory[estimated_monthly_cost])

SQL:

    SELECT SUM(estimated_monthly_cost) AS monthly_run_rate
    FROM architecture_inventory;

**Decision:** compare target-state architecture cost with available budget and expected value.

### High-Criticality Component Share

    =COUNTIF(architecture_inventory[criticality],"High")/COUNTA(architecture_inventory[component])

**Decision:** determine where resilience, security, testing, and continuity controls require the strongest design.

### Continuity Coverage

    =COUNTIF(architecture_inventory[continuity_method],"<>")/COUNTA(architecture_inventory[component])

**Decision:** identify architecture components that have no defined fallback method.

### Modernization Coverage

    =COUNTIF(architecture_inventory[target_pattern],"<>")/COUNTA(architecture_inventory[component])

**Decision:** confirm that each known current-state component has an intentional target-state disposition.

---

## 3. Customer Solutions Manager | adoption_telemetry.csv

**Columns used:** `user_group`, `target_users`, `active_users_30d`, `transactions_30d`, `legacy_transactions`, `open_blockers`, `avg_cycle_minutes`, `hours_saved_monthly`.

### Adoption Rate

    =[@active_users_30d]/[@target_users]

Overall:

    =SUM(adoption_telemetry[active_users_30d])/SUM(adoption_telemetry[target_users])

**Decision:** identify user groups requiring adoption recovery before legacy methods are retired.

### Legacy Reliance Rate

    =[@legacy_transactions]/([@transactions_30d]+[@legacy_transactions])

**Decision:** distinguish a technically deployed solution from one actually used in day-to-day operations.

### Blocker Density

    =[@open_blockers]/[@active_users_30d]

**Decision:** prioritize customer-success effort where adoption friction is concentrated.

### Monthly Productivity Benefit

    =SUM(adoption_telemetry[hours_saved_monthly])

**Decision:** quantify realized operational value rather than relying only on deployment completion.

---

## 4. Data & AI Lead | data_product_registry.csv

**Columns used:** `data_product`, `owner`, `source`, `freshness_sla_hours`, `actual_freshness_hours`, `quality_score`, `ai_use`, `grounding_score`, `human_review_rule`.

### Freshness Compliance

    =IF([@actual_freshness_hours]<=[@freshness_sla_hours],1,0)

Overall:

    =AVERAGE(FreshnessComplianceColumn)

**Decision:** block or flag analytics/AI use when source data is stale.

### Quality Pass
Example portfolio threshold = 0.98.

    =IF([@quality_score]>=0.98,1,0)

**Decision:** determine whether a data product is suitable for downstream decision or AI use.

### Grounding Review Trigger

    =IF([@grounding_score]<0.90,"Human Review","Allow")

**Decision:** require human review when evidence coverage is below the accepted threshold.

### Trusted Data Product Rate

    =AVERAGE(FreshnessPass * QualityPass * GroundingPass)

Python:

    trusted = (
        actual_freshness_hours <= freshness_sla_hours
        and quality_score >= .98
        and grounding_score >= .90
    )

**Decision:** identify which data products can support automated analytics/AI and which must remain gated.

---

## 5. Cloud Transformation Program Manager | migration_inventory.csv

**Columns used:** `workload`, `criticality`, `wave`, `readiness_pct`, `identity_ready`, `data_validated`, `integration_ready`, `rollback_ready`, `support_ready`, `cutover_window`.

### Technical Gate Pass

    =IF(AND([@identity_ready]="Yes",[@data_validated]="Yes",[@integration_ready]="Yes",[@rollback_ready]="Yes",[@support_ready]="Yes"),1,0)

### Cutover Eligibility

    =IF(AND([@readiness_pct]>=85,[@identity_ready]="Yes",[@data_validated]="Yes",[@integration_ready]="Yes",[@rollback_ready]="Yes",[@support_ready]="Yes"),"GO","NO-GO")

**Decision:** prevent a workload from moving simply because its planned cutover date has arrived.

### Wave Readiness

    =AVERAGEIFS(migration_inventory[readiness_pct],migration_inventory[wave],[@wave])/100

**Decision:** determine whether an entire migration wave should progress, split, or be resequenced.

### Critical Blocked Workloads

    =COUNTIFS(migration_inventory[criticality],"Critical",migration_inventory[readiness_pct],"<85")

**Decision:** escalate continuity risk before a critical workload enters cutover.

---

## 6. Technology Delivery Lead | raid_register.csv

**Columns used:** `id`, `type`, `description`, `impact`, `owner`, `opened_date`, `due_date`, `status`, `recovery_action`, `business_process`.

### Item Age

    =TODAY()-[@opened_date]

### Days Overdue

    =IF(AND([@status]<>"Closed",TODAY()>[@due_date]),TODAY()-[@due_date],0)

### High-Impact Open Blockers

    =COUNTIFS(raid_register[impact],"High",raid_register[status],"<>Closed")

### Recovery Coverage

    =COUNTIF(raid_register[recovery_action],"<>")/COUNTA(raid_register[id])

**Decision:** every high-impact issue should have a recovery action before it reaches executive reporting.

### Escalation Rule
Example:

    Critical = immediate
    High = escalate at 2 days open
    Medium = escalate at 5 days open
    Low = escalate at 10 days open

Python:

    thresholds = {"Critical":0,"High":2,"Medium":5,"Low":10}
    escalate = item_age >= thresholds[impact]

---

## 7. BI & Decision Intelligence Lead | kpi_registry.csv

**Columns used:** `kpi`, `definition`, `source`, `refresh_sla_minutes`, `actual_age_minutes`, `threshold`, `current_value`, `owner`, `decision_trigger`.

### Freshness Variance

    =[@actual_age_minutes]-[@refresh_sla_minutes]

### Stale KPI Flag

    =IF([@actual_age_minutes]>[@refresh_sla_minutes],1,0)

**Decision:** prevent executives from acting on a metric that is outside its approved refresh window.

### Example Threshold Calculations
Adoption:

    =IF([@current_value]<0.80,"Action","Within Threshold")

SLA Compliance:

    =IF([@current_value]<0.90,"Action","Within Threshold")

Forecast Pressure:

    =IF([@current_value]>0,"Decision Required","Within Plan")

Data Quality:

    =IF([@current_value]<0.98,"Correct Data","Within Threshold")

**Decision model:** KPI → threshold → exception → owner → action.

---

## 8. AI Transformation Program Manager | ai_use_case_portfolio.csv

**Columns used:** `use_case`, `business_value`, `data_readiness`, `technical_feasibility`, `risk`, `adoption_readiness`, `projected_hours_saved`, `owner`, `status`.

### AI Use-Case Priority Score
All inputs are scored 1–5; risk is inverted with `6-risk`.

    =([@business_value]*0.30)+([@data_readiness]*0.20)+([@technical_feasibility]*0.20)+((6-[@risk])*0.15)+([@adoption_readiness]*0.15)

Python:

    priority = (
        business_value*.30
        + data_readiness*.20
        + technical_feasibility*.20
        + (6-risk)*.15
        + adoption_readiness*.15
    )

### Production Candidate Flag

    =IF(AND([@data_readiness]>=4,[@technical_feasibility]>=4,[@risk]<=2,[@adoption_readiness]>=4),"Production Candidate","Hold / Improve")

### Portfolio Productivity Potential

    =SUM(ai_use_case_portfolio[projected_hours_saved])

**Decision:** prioritize AI investments using readiness and value rather than demo visibility.

---

## 9. Power Platform Solution Architect | requests.csv

**Columns used:** `request_id`, `title`, `request_type`, `status`, `submitted_by`, `submitted_on`, `reviewer`, `reviewed_on`, `priority`, `ecd`, `duplicate_flag`.

### Review Cycle Days
For reviewed records:

    =IF([@reviewed_on]="","",[@reviewed_on]-[@submitted_on])

### Pending Review Age

    =IF([@status]="Pending Review",TODAY()-[@submitted_on],0)

### Duplicate Rate

    =COUNTIF(requests[duplicate_flag],"Yes")/COUNTA(requests[request_id])

### ECD Risk

    =IF(AND([@status]<>"Approved",[@status]<>"Closed",[@ecd]-TODAY()<=7),"At Risk","Normal")

### Approval/Return Rate

    Approval Rate = Approved Requests / Reviewed Requests
    Return Rate = Returned Requests / Reviewed Requests

**Decision:** identify duplicate demand, reviewer bottlenecks, aging requests, and items likely to miss expected completion dates.

---

## How the Calculations Become Code

The CSV files are intentionally simple so a reviewer can inspect the source. In a production solution, these same calculations can be implemented at the appropriate layer:

- **Excel / Power Query** for exploratory validation and analyst-controlled models.
- **SQL** for governed transformations, joins, flags, and reusable reporting views.
- **Python** for scoring, forecasting, simulation, batch controls, and AI/data-quality logic.
- **DAX** for interactive measures, time intelligence, threshold views, and executive drill-through.
- **Power Fx** for user-facing validation and workflow behavior inside Power Apps.
- **Power Automate** for event-driven routing, escalation, audit history, notifications, and recovery handling.

The calculation is not the end product. The purpose of each calculation is to expose a condition that changes an operating decision.
