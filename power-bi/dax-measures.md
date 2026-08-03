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
# Executive Performance Indicators and DAX Measures

These measures support the Power BI executive dashboard for the Government Service Request & Approval Portal.

## Data Tables

The measures use the following fictional tables:

- ServiceRequests
- RequestCategories
- Assignments
- ApprovalDecisions
- RequestComments
- Documents
- SLARules
- StatusHistory
- Notifications
- Users
- SecurityRoles
- AuditHistory

## Executive Performance Indicators

| Indicator | Purpose |
|---|---|
| Total Requests | Counts all service requests |
| Open Requests | Counts requests that remain active |
| Completed Requests | Counts completed and closed requests |
| Request Completion Rate | Measures overall completion performance |
| Critical Open Requests | Highlights urgent unresolved requests |
| Overdue Requests | Counts requests that exceeded their SLA |
| SLA Compliance Rate | Measures requests completed within SLA |
| Average Resolution Time | Measures average hours required for completion |
| Pending Approvals | Counts approval decisions awaiting action |
| Returned Requests | Identifies requests requiring corrections |
| Unassigned Requests | Identifies requests without an assigned specialist |
| Upcoming SLA Deadlines | Identifies requests approaching SLA deadlines |
| Average Approval Time | Measures approval processing performance |
| Data-Quality Exceptions | Counts incomplete or inconsistent records |
| Overall Service Health | Assigns Green, Amber, or Red performance status |

## Core Request Measures

### Total Requests

```DAX
Total Requests =
DISTINCTCOUNT(ServiceRequests[Request ID])
Draft Requests =
CALCULATE(
    [Total Requests],
    ServiceRequests[Current Status] = "Draft"
)
Submitted Requests =
CALCULATE(
    [Total Requests],
    ServiceRequests[Current Status] = "Submitted"
)
Open Requests =
CALCULATE(
    [Total Requests],
    NOT(
        ServiceRequests[Current Status]
            IN {"Completed", "Closed", "Rejected", "Cancelled"}
    )
)
Completed Requests =
CALCULATE(
    [Total Requests],
    ServiceRequests[Current Status]
        IN {"Completed", "Closed"}
)
Request Completion Rate =
DIVIDE(
    [Completed Requests],
    [Total Requests],
    0
)
Critical Open Requests =
CALCULATE(
    [Total Requests],
    ServiceRequests[Priority] = "Critical",
    NOT(
        ServiceRequests[Current Status]
            IN {"Completed", "Closed", "Rejected", "Cancelled"}
    )
)
High-Priority Open Requests =
CALCULATE(
    [Total Requests],
    ServiceRequests[Priority] IN {"High", "Critical"},
    NOT(
        ServiceRequests[Current Status]
            IN {"Completed", "Closed", "Rejected", "Cancelled"}
    )
)
Overdue Requests =
CALCULATE(
    [Total Requests],
    ServiceRequests[SLA Due Date] < NOW(),
    NOT(
        ServiceRequests[Current Status]
            IN {"Completed", "Closed", "Rejected", "Cancelled"}
    )
)
Requests Completed Within SLA =
CALCULATE(
    [Total Requests],
    FILTER(
        ServiceRequests,
        NOT ISBLANK(ServiceRequests[Completed Date])
            && ServiceRequests[Completed Date]
                <= ServiceRequests[SLA Due Date]
    )
)
Completed Requests With SLA =
CALCULATE(
    [Total Requests],
    FILTER(
        ServiceRequests,
        NOT ISBLANK(ServiceRequests[Completed Date])
            && NOT ISBLANK(ServiceRequests[SLA Due Date])
    )
)
SLA Compliance Rate =
DIVIDE(
    [Requests Completed Within SLA],
    [Completed Requests With SLA],
    0
)
SLA Compliance Rate =
DIVIDE(
    [Requests Completed Within SLA],
    [Completed Requests With SLA],
    0
)
Average Resolution Hours =
AVERAGEX(
    FILTER(
        ServiceRequests,
        NOT ISBLANK(ServiceRequests[Completed Date])
    ),
    DATEDIFF(
        ServiceRequests[Submitted Date],
        ServiceRequests[Completed Date],
        HOUR
    )
)
Average Resolution Days =
DIVIDE(
    [Average Resolution Hours],
    24,
    0
)
SLA Due Within 24 Hours =
CALCULATE(
    [Total Requests],
    ServiceRequests[SLA Due Date] >= NOW(),
    ServiceRequests[SLA Due Date] <= NOW() + 1,
    NOT(
        ServiceRequests[Current Status]
            IN {"Completed", "Closed", "Rejected", "Cancelled"}
    )
)
SLA Due Within Three Days =
CALCULATE(
    [Total Requests],
    ServiceRequests[SLA Due Date] > NOW() + 1,
    ServiceRequests[SLA Due Date] <= NOW() + 3,
    NOT(
        ServiceRequests[Current Status]
            IN {"Completed", "Closed", "Rejected", "Cancelled"}
    )
)
SLA Due Within Seven Days =
CALCULATE(
    [Total Requests],
    ServiceRequests[SLA Due Date] > NOW() + 3,
    ServiceRequests[SLA Due Date] <= NOW() + 7,
    NOT(
        ServiceRequests[Current Status]
            IN {"Completed", "Closed", "Rejected", "Cancelled"}
    )
)
Assigned Requests =
CALCULATE(
    [Total Requests],
    NOT ISBLANK(ServiceRequests[Assigned User ID])
)
Unassigned Requests =
CALCULATE(
    [Total Requests],
    ISBLANK(ServiceRequests[Assigned User ID]),
    ServiceRequests[Current Status] <> "Draft",
    NOT(
        ServiceRequests[Current Status]
            IN {"Completed", "Closed", "Rejected", "Cancelled"}
    )
)
Active Assignments =
CALCULATE(
    DISTINCTCOUNT(Assignments[Assignment ID]),
    Assignments[Assignment Status] = "Active"
)
Pending Assignment Acceptance =
CALCULATE(
    DISTINCTCOUNT(Assignments[Assignment ID]),
    Assignments[Assignment Status] = "Pending Acceptance"
)
Average Assignment Acceptance Hours =
AVERAGEX(
    FILTER(
        Assignments,
        NOT ISBLANK(Assignments[Accepted Date])
    ),
    DATEDIFF(
        Assignments[Assigned Date],
        Assignments[Accepted Date],
        HOUR
    )
)
Total Approval Decisions =
DISTINCTCOUNT(ApprovalDecisions[Decision ID])
Total Approval Decisions =
DISTINCTCOUNT(ApprovalDecisions[Decision ID])
Pending Approvals =
CALCULATE(
    [Total Approval Decisions],
    ApprovalDecisions[Decision] = "Pending"
)
Pending Approvals =
CALCULATE(
    [Total Approval Decisions],
    ApprovalDecisions[Decision] = "Pending"
)
Approved Decisions =
CALCULATE(
    [Total Approval Decisions],
    ApprovalDecisions[Decision] = "Approved"
)
Returned Decisions =
CALCULATE(
    [Total Approval Decisions],
    ApprovalDecisions[Decision] = "Returned"
)
Approval Rate =
DIVIDE(
    [Approved Decisions],
    CALCULATE(
        [Total Approval Decisions],
        ApprovalDecisions[Decision]
            IN {"Approved", "Rejected", "Returned"}
    ),
    0
)
Average Approval Hours =
AVERAGEX(
    FILTER(
        ApprovalDecisions,
        NOT ISBLANK(ApprovalDecisions[Decision Date])
    ),
    DATEDIFF(
        RELATED(ServiceRequests[Submitted Date]),
        ApprovalDecisions[Decision Date],
        HOUR
    )
)
Overdue Approval Decisions =
CALCULATE(
    [Total Approval Decisions],
    ApprovalDecisions[Decision] = "Pending",
    ApprovalDecisions[Due Date] < NOW()
)
Returned Requests =
CALCULATE(
    [Total Requests],
    ServiceRequests[Current Status] = "Returned for Correction"
)
Returned Requests =
CALCULATE(
    [Total Requests],
    ServiceRequests[Current Status] = "Returned for Correction"
)
Return Rate =
DIVIDE(
    [Returned Requests],
    [Total Requests],
    0
)
Total Notifications =
DISTINCTCOUNT(Notifications[Notification ID])
Failed Notifications =
CALCULATE(
    [Total Notifications],
    Notifications[Delivery Status] <> "Delivered"
)
Escalation Notifications =
CALCULATE(
    [Total Notifications],
    Notifications[Escalation Level] > 0
)
Notification Delivery Rate =
DIVIDE(
    CALCULATE(
        [Total Notifications],
        Notifications[Delivery Status] = "Delivered"
    ),
    [Total Notifications],
    0
)
Total Documents =
DISTINCTCOUNT(Documents[Document ID])
Required Documents Returned =
CALCULATE(
    [Total Documents],
    Documents[Required] = TRUE(),
    Documents[Review Status] = "Returned"
)
Required Documents Pending Review =
CALCULATE(
    [Total Documents],
    Documents[Required] = TRUE(),
    Documents[Review Status] = "In Review"
)
Requests Missing Assigned Team =
CALCULATE(
    [Total Requests],
    ISBLANK(ServiceRequests[Assigned Team]),
    ServiceRequests[Current Status] <> "Draft"
)
Requests Missing Assigned Team =
CALCULATE(
    [Total Requests],
    ISBLANK(ServiceRequests[Assigned Team]),
    ServiceRequests[Current Status] <> "Draft"
)
Requests Missing SLA Due Date =
CALCULATE(
    [Total Requests],
    ISBLANK(ServiceRequests[SLA Due Date]),
    ServiceRequests[Current Status] <> "Draft"
)
Requests Missing Required Date =
CALCULATE(
    [Total Requests],
    ISBLANK(ServiceRequests[Required By Date]),
    ServiceRequests[Current Status] <> "Draft"
)
Data-Quality Exceptions =
[Requests Missing Assigned Team]
    + [Requests Missing SLA Due Date]
    + [Requests Missing Required Date]
Overall Service Health =
VAR HealthScore = [Service Health Score]
VAR ComplianceRate = [SLA Compliance Rate]

RETURN
    SWITCH(
        TRUE(),
        HealthScore >= 12
            || ComplianceRate < 0.75, "Red",

        HealthScore >= 4
            || ComplianceRate < 0.90, "Amber",

        "Green"
    )
Service Health Color =
SWITCH(
    [Overall Service Health],
    "Green", "#2E7D32",
    "Amber", "#F9A825",
    "Red", "#C62828",
    "#607D8B"
)
# Executive Performance Indicators and DAX Measures

These measures support the Power BI executive dashboard for the Federal Program Performance Command Center.

## Data Tables

The measures use the following fictional tables:

- Programs
- Projects
- Milestones
- Deliverables
- Risks
- Issues
- CorrectiveActions
- FundingCosts
- StatusUpdates
- PerformanceMeasures
- Users
- SecurityRoles
- AuditHistory

## Executive Performance Indicators

| Indicator | Purpose |
|---|---|
| Total Programs | Counts programs in the portfolio |
| Active Programs | Counts currently active programs |
| Total Projects | Counts all projects |
| Overall Program Health | Assigns Green, Amber, or Red health |
| Approved Budget | Calculates total approved funding |
| Actual Cost | Calculates total recorded expenditures |
| Forecast at Completion | Estimates final portfolio cost |
| Cost Variance | Measures budget compared with forecast cost |
| Schedule Variance | Measures project and milestone delay |
| Milestone Completion Rate | Measures milestone-delivery performance |
| Overdue Milestones | Identifies missed milestone deadlines |
| Open Risk Exposure | Measures unresolved risk severity |
| Critical Issue Count | Counts open critical issues |
| Corrective-Action Completion Rate | Measures remediation progress |
| Upcoming 30-Day Deadlines | Identifies immediate deadlines |
| Upcoming 60-Day Deadlines | Supports medium-range planning |
| Upcoming 90-Day Deadlines | Supports forward-looking risk management |
| Data-Quality Exception Count | Identifies incomplete or inconsistent records |

## Reporting Date

Because this repository uses a fictional historical dataset, dashboard calculations should use the latest available reporting date instead of the current system date.

```DAX
Reporting As Of Date =
MAX(FundingCosts[As of Date])
Live Reporting Date =
TODAY()
Total Programs =
DISTINCTCOUNT(Programs[Program ID])
Active Programs =
CALCULATE(
    [Total Programs],
    Programs[Lifecycle Status] = "Active"
)
Total Projects =
DISTINCTCOUNT(Projects[Project ID])
Active Projects =
CALCULATE(
    [Total Projects],
    NOT(
        Projects[Status]
            IN {"Completed", "Closed", "Cancelled"}
    )
)
Completed Projects =
CALCULATE(
    [Total Projects],
    Projects[Status]
        IN {"Completed", "Closed"}
)
Projects at Risk =
CALCULATE(
    [Total Projects],
    Projects[Status]
        IN {"At Risk", "Delayed"}
)
Project Completion Rate =
DIVIDE(
    [Completed Projects],
    [Total Projects],
    0
)
Average Project Progress =
AVERAGE(Projects[Percent Complete])
Total Approved Budget =
SUM(FundingCosts[Approved Budget])
Total Obligated Amount =
SUM(FundingCosts[Obligated Amount])
Total Actual Cost =
SUM(FundingCosts[Actual Cost])
Forecast at Completion =
SUM(FundingCosts[Forecast at Completion])

Remaining Available Budget =
[Total Approved Budget]
    - [Total Actual Cost]
Cost Variance =
[Total Approved Budget]
    - [Forecast at Completion]
Cost Variance Percentage =
DIVIDE(
    [Cost Variance],
    [Total Approved Budget],
    0
)
Obligation Rate =
DIVIDE(
    [Total Obligated Amount],
    [Total Approved Budget],
    0
)
Projects Forecast Over Budget =
CALCULATE(
    DISTINCTCOUNT(FundingCosts[Project ID]),
    FundingCosts[Forecast at Completion]
        > FundingCosts[Approved Budget]
)
Total Milestones =
DISTINCTCOUNT(Milestones[Milestone ID])
Completed Milestones =
CALCULATE(
    [Total Milestones],
    Milestones[Status] = "Completed"
)
Milestone Completion Rate =
DIVIDE(
    [Completed Milestones],
    [Total Milestones],
    0
)
Overdue Milestones =
VAR AsOfDate = [Reporting As Of Date]

RETURN
    CALCULATE(
        [Total Milestones],
        Milestones[Current Due Date] < AsOfDate,
        Milestones[Status] <> "Completed"
    )
Overdue Milestones =
VAR AsOfDate = [Reporting As Of Date]

RETURN
    CALCULATE(
        [Total Milestones],
        Milestones[Current Due Date] < AsOfDate,
        Milestones[Status] <> "Completed"
    )
Critical Overdue Milestones =
VAR AsOfDate = [Reporting As Of Date]

RETURN
    CALCULATE(
        [Total Milestones],
        Milestones[Current Due Date] < AsOfDate,
        Milestones[Status] <> "Completed",
        Milestones[Criticality] = "Critical"
    )
Average Schedule Variance Days =
AVERAGE(Milestones[Schedule Variance Days])
Maximum Schedule Variance Days =
MAX(Milestones[Schedule Variance Days])
Milestones Behind Baseline =
CALCULATE(
    [Total Milestones],
    Milestones[Current Due Date]
        > Milestones[Baseline Date],
    Milestones[Status] <> "Completed"
)
Total Deliverables =
DISTINCTCOUNT(Deliverables[Deliverable ID])

Overdue Deliverables =
VAR AsOfDate = [Reporting As Of Date]

RETURN
    CALCULATE(
        [Total Deliverables],
        Deliverables[Due Date] < AsOfDate,
        NOT(
            Deliverables[Status]
                IN {"Approved", "Completed"}
        )
    )
Deliverable Approval Rate =
DIVIDE(
    [Approved Deliverables],
    [Total Deliverables],
    0
)
Open Risks =
CALCULATE(
    [Total Risks],
    NOT(
        Risks[Status]
            IN {"Closed", "Accepted"}
    )
)
Critical Open Risks =
CALCULATE(
    [Total Risks],
    Risks[Risk Level] = "Critical",
    NOT(
        Risks[Status]
            IN {"Closed", "Accepted"}
    )
)
High and Critical Risks =
CALCULATE(
    [Total Risks],
    Risks[Risk Level] IN {"High", "Critical"},
    NOT(
        Risks[Status]
            IN {"Closed", "Accepted"}
    )
)
Open Risk Exposure =
CALCULATE(
    SUM(Risks[Risk Score]),
    NOT(
        Risks[Status]
            IN {"Closed", "Accepted"}
    )
)
Average Risk Score =
CALCULATE(
    AVERAGE(Risks[Risk Score]),
    NOT(
        Risks[Status]
            IN {"Closed", "Accepted"}
    )
)
Average Risk Score =
CALCULATE(
    AVERAGE(Risks[Risk Score]),
    NOT(
        Risks[Status]
            IN {"Closed", "Accepted"}
    )
)
Total Issues =
DISTINCTCOUNT(Issues[Issue ID])
Critical Issue Count =
CALCULATE(
    [Total Issues],
    Issues[Severity] = "Critical",
    Issues[Status] <> "Resolved"
)
