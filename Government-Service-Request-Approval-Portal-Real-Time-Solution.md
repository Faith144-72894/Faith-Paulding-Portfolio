# Real-Time Government Service Request & Approval Modernization

## Role Alignment
Business Systems Analyst • Technical Business Analyst • Power Apps Developer • Power Automate Developer • Workflow Automation Lead

## Common Government Problem
Service requests arrive through email or forms and are copied into trackers. Ownership, approvals, documents, SLA dates, and status communications are maintained separately.

## Modernization Pattern
**Fragmented** → email → spreadsheet → approval email → manual follow-up → static report

**Modernized** → digital intake → validation → routing → approval → fulfillment → SLA monitoring → audit history → live analytics

## Power Fx
```powerfx
Patch(
    ServiceRequests,
    Defaults(ServiceRequests),
    {
        RequestTitle: txtRequest.Text,
        Status: {Value:"Submitted"},
        SubmittedDate: Now(),
        RequiredBy: dpRequired.SelectedDate
    }
)
```

## SLA Calculation
```DAX
SLA Hours Remaining =
DATEDIFF(NOW(), MAX(ServiceRequests[SLADueDate]), HOUR)

Projected SLA Breaches =
CALCULATE(
    [Open Requests],
    ServiceRequests[SLADueDate] <= NOW() + 1,
    ServiceRequests[Status] <> "Completed"
)
```

## Capability Demonstrated
Requirements • workflow design • Power Apps • Power Automate • Power Fx • SLA logic • approvals • audit history • operational reporting
