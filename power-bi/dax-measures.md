# Executive Performance Indicators and DAX Measures

These measures support the executive Power BI dashboard for the Government Audit & Compliance Management System.

The calculations use fictional data and the following proposed tables:

- Deficiencies
- Recommendations
- CorrectiveActions
- Milestones
- AuditIntake
- AuditHistory
- Calendar

## Executive KPI Summary

| Performance Indicator | Purpose |
|---|---|
| Total Deficiencies | Counts all deficiencies in the system |
| Open Deficiencies | Counts deficiencies that have not been closed |
| Overdue Deficiencies | Identifies open deficiencies past their ECD |
| High-Severity Open Deficiencies | Highlights the most serious unresolved findings |
| Deficiency Closure Rate | Measures the percentage of deficiencies closed |
| Average Days Open | Measures how long deficiencies remain unresolved |
| Open Recommendations | Counts unresolved recommendations |
| Corrective-Action Completion Rate | Measures completion of CAP actions |
| Overdue Corrective Actions | Identifies CAP actions past their due dates |
| Upcoming 30-Day Deadlines | Identifies immediate upcoming deadlines |
| Upcoming 60-Day Deadlines | Supports medium-term planning |
| Upcoming 90-Day Deadlines | Provides forward-looking audit-risk visibility |
| Pending Internal Reviews | Measures the intake-review backlog |
| Returned Submissions | Identifies submissions requiring corrections |
| Data-Quality Exceptions | Counts records failing required quality rules |
| Overall Audit Health | Assigns Green, Amber, or Red health status |

## Core Deficiency Measures

### Total Deficiencies

```DAX
Total Deficiencies =
DISTINCTCOUNT(Deficiencies[Deficiency ID])
Open Deficiencies =
CALCULATE(
    [Total Deficiencies],
    Deficiencies[Status] <> "Closed"
)

Closed Deficiencies =
CALCULATE(
    [Total Deficiencies],
    Deficiencies[Status] = "Closed"
)
Deficiency Closure Rate =
DIVIDE(
    [Closed Deficiencies],
    [Total Deficiencies],
    0
)
Overdue Deficiencies =
CALCULATE(
    [Total Deficiencies],
    Deficiencies[ECD] < TODAY(),
    Deficiencies[Status] <> "Closed"
)
High-Severity Open Deficiencies =
CALCULATE(
    [Total Deficiencies],
    Deficiencies[Severity] IN {"High", "Critical"},
    Deficiencies[Status] <> "Closed"
)
Average Days Open =
AVERAGEX(
    FILTER(
        Deficiencies,
        Deficiencies[Status] <> "Closed"
    ),
    DATEDIFF(
        Deficiencies[Created Date],
        TODAY(),
        DAY
    )
)
Average Days to Closure =
AVERAGEX(
    FILTER(
        Deficiencies,
        Deficiencies[Status] = "Closed"
            && NOT ISBLANK(Deficiencies[Closed Date])
    ),
    DATEDIFF(
        Deficiencies[Created Date],
        Deficiencies[Closed Date],
        DAY
    )
)
Total Recommendations =
DISTINCTCOUNT(Recommendations[Recommendation ID])
Open Recommendations =
CALCULATE(
    [Total Recommendations],
    Recommendations[Status] <> "Closed"
)
Overdue Recommendations =
CALCULATE(
    [Total Recommendations],
    Recommendations[ECD] < TODAY(),
    Recommendations[Status] <> "Closed"
)
Recommendation Closure Rate =
DIVIDE(
    CALCULATE(
        [Total Recommendations],
        Recommendations[Status] = "Closed"
    ),
    [Total Recommendations],
    0
)
Total Corrective Actions =
DISTINCTCOUNT(CorrectiveActions[Action ID])
Completed Corrective Actions =
CALCULATE(
    [Total Corrective Actions],
    CorrectiveActions[Status] = "Completed"
)
Corrective-Action Completion Rate =
DIVIDE(
    [Completed Corrective Actions],
    [Total Corrective Actions],
    0
)
Overdue Corrective Actions =
CALCULATE(
    [Total Corrective Actions],
    CorrectiveActions[Current Due Date] < TODAY(),
    CorrectiveActions[Status] <> "Completed"
)
Average Corrective-Action Progress =
AVERAGE(CorrectiveActions[Percent Complete])
Total Milestones =
DISTINCTCOUNT(Milestones[Milestone ID])
Milestone Completion Rate =
DIVIDE(
    CALCULATE(
        [Total Milestones],
        Milestones[Status] = "Completed"
    ),
    [Total Milestones],
    0
)
Overdue Milestones =
CALCULATE(
    [Total Milestones],
    Milestones[Current Due Date] < TODAY(),
    Milestones[Status] <> "Completed"
)
Critical Overdue Milestones =
CALCULATE(
    [Total Milestones],
    Milestones[Current Due Date] < TODAY(),
    Milestones[Status] <> "Completed",
    Milestones[Criticality] = "Critical"
)
Upcoming 30-Day Deadlines =
CALCULATE(
    [Total Deficiencies],
    Deficiencies[ECD] >= TODAY(),
    Deficiencies[ECD] <= TODAY() + 30,
    Deficiencies[Status] <> "Closed"
)
Upcoming 60-Day Deadlines =
CALCULATE(
    [Total Deficiencies],
    Deficiencies[ECD] > TODAY() + 30,
    Deficiencies[ECD] <= TODAY() + 60,
    Deficiencies[Status] <> "Closed"
)
Upcoming 90-Day Deadlines =
CALCULATE(
    [Total Deficiencies],
    Deficiencies[ECD] > TODAY() + 60,
    Deficiencies[ECD] <= TODAY() + 90,
    Deficiencies[Status] <> "Closed"
)
Pending Internal Reviews =
CALCULATE(
    DISTINCTCOUNT(AuditIntake[Intake ID]),
    AuditIntake[Status] = "Pending Review"
)
Returned Submissions =
CALCULATE(
    DISTINCTCOUNT(AuditIntake[Intake ID]),
    AuditIntake[Status] = "Returned for Correction"
)
Average Review Processing Time =
AVERAGEX(
    FILTER(
        AuditIntake,
        NOT ISBLANK(AuditIntake[Review Completed Date])
    ),
    DATEDIFF(
        AuditIntake[Submitted Date],
        AuditIntake[Review Completed Date],
        DAY
    )
)
Data-Quality Exceptions =
CALCULATE(
    [Total Deficiencies],
    ISBLANK(Deficiencies[Deficiency Number])
        || ISBLANK(Deficiencies[Owner])
        || ISBLANK(Deficiencies[Status])
        || ISBLANK(Deficiencies[ECD])
)
Records Missing Owners =
CALCULATE(
    [Total Deficiencies],
    ISBLANK(Deficiencies[Owner])
)
Records Missing ECD =
CALCULATE(
    [Total Deficiencies],
    ISBLANK(Deficiencies[ECD]),
    Deficiencies[Status] <> "Closed"
)
Audit Health Score =
VAR OverdueCount = [Overdue Deficiencies]
VAR CriticalOpenCount = [High-Severity Open Deficiencies]
VAR OverdueCAPCount = [Overdue Corrective Actions]
VAR CriticalMilestoneCount = [Critical Overdue Milestones]
VAR QualityExceptionCount = [Data-Quality Exceptions]

RETURN
    (OverdueCount * 2)
        + (CriticalOpenCount * 3)
        + (OverdueCAPCount * 2)
        + (CriticalMilestoneCount * 3)
        + QualityExceptionCount
Overall Audit Health =
VAR HealthScore = [Audit Health Score]

RETURN
    SWITCH(
        TRUE(),
        HealthScore >= 15, "Red",
        HealthScore >= 5, "Amber",
        "Green"
    )
Health Definitions
Health	Definition
Green	Audit activity is within approved thresholds with no significant unresolved risks
Amber	Emerging deadlines, overdue actions, data-quality concerns, or elevated findings require attention
Red	Critical deficiencies, multiple overdue actions, missed milestones, or serious compliance risks require leadership intervention
Audit Health Color =
SWITCH(
    [Overall Audit Health],
    "Green", "#2E7D32",
    "Amber", "#F9A825",
    "Red", "#C62828",
    "#607D8B"
)
