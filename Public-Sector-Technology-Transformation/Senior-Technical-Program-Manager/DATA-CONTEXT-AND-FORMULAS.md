# Data Context, Formulas & Code | Senior Technical Program Manager

## What the Data Represents
This dataset is the integrated operating picture for a multi-workstream public-sector technology program. Each row represents a delivery object that can affect release readiness: milestone, dependency, decision, risk, defect, UAT gate, or recovery action.

## Grain
One row per delivery object per reporting period.

## Primary Sources
Jira/Azure DevOps work items • delivery schedule • customer decision log • UAT tracker • security review tracker • vendor status • release-readiness checklist.

## Core Fields
WorkstreamID • DeliverableID • Owner • PlannedDate • ForecastDate • ActualDate • Status • DependencyID • DecisionID • RiskLevel • UATStatus • RecoveryAction • ContinuityMethod • LastUpdated.

## Relationships
Workstream 1:M Milestones
Workstream 1:M Risks
Milestone M:M Dependencies through a bridge
Decision 1:M impacted milestones
Release 1:M readiness gates

## Why the Data Matters
This structure lets me answer the questions that matter operationally: what is late, why it is late, who owns the blocker, what decision is required, whether release readiness is improving, and whether the current business process remains protected if the release slips.

## Formulas
Schedule Variance Days = ForecastDate - PlannedDate

Decision Aging Days = Today - DecisionOpenDate

Dependency Closure Rate = Closed Critical Dependencies / Total Critical Dependencies

UAT Pass Rate = Passed Test Cases / Executed Test Cases

Release Readiness Score = Security×20% + Data×20% + Integration×20% + UAT×25% + Continuity×15%

Go/No-Go Rule = No-Go if any critical gate = 0 OR Readiness Score < 85%

## DAX
    Schedule Variance Days =
    AVERAGEX(
        FILTER(Milestones, Milestones[Status] <> "Complete"),
        DATEDIFF(Milestones[PlannedDate], Milestones[ForecastDate], DAY)
    )

    Critical Dependency Closure % =
    DIVIDE(
        CALCULATE(COUNTROWS(Dependencies), Dependencies[Criticality] = "Critical", Dependencies[Status] = "Closed"),
        CALCULATE(COUNTROWS(Dependencies), Dependencies[Criticality] = "Critical"),
        0
    )

## SQL
    SELECT WorkstreamID,
           COUNT(*) AS OpenItems,
           SUM(CASE WHEN ForecastDate > PlannedDate THEN 1 ELSE 0 END) AS LateItems,
           SUM(CASE WHEN RiskLevel IN ('High','Critical') THEN 1 ELSE 0 END) AS HighRiskItems
    FROM DeliveryObjects
    WHERE Status <> 'Closed'
    GROUP BY WorkstreamID;

## Python
    def release_decision(gates):
        weights = {"security":.20,"data":.20,"integration":.20,"uat":.25,"continuity":.15}
        score = sum(gates[k] * weights[k] for k in weights)
        critical_failure = any(gates[k] == 0 for k in weights)
        return {"score": round(score,3), "decision":"NO-GO" if critical_failure or score < .85 else "GO"}

## Data Quality Rules
No milestone without an owner • no critical dependency without a due date • no closed risk without mitigation evidence • no release gate without status • decision owner required for every open decision • stale records >3 business days flagged.

## Day-to-Day Use
Morning: review late/at-risk items and new dependencies. Midday: resolve owners and customer decisions. Afternoon: reconcile technical status against release-readiness data. Before executive review: validate that every Red/Amber condition has cause, owner, action, and expected recovery date.

## Business Decisions Supported
Move release date • approve temporary workaround • resequence scope • escalate customer decision • add UAT capacity • hold cutover • retire or retain legacy process.
