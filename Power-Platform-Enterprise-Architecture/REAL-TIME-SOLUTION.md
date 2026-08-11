# Real-Time Power Platform Enterprise Modernization

## Role Alignment
Power Platform Solution Architect • Enterprise Power Platform Architect • Senior Power Platform Developer • Workflow Automation Lead • Power Platform Governance Lead

## Common Government Problem
Requests arrive through email, spreadsheets, shared drives, and disconnected forms. Staff manually determine ownership, update trackers, request approvals, and communicate status.

## Modernization Pattern
**Fragmented / Siloed** → email + spreadsheet + manual approval + separate reporting

**Modernized** → Power Apps intake + governed data + Power Automate orchestration + audit history + Power BI monitoring

## Software Stack
| Software | Use in Solution | Required Access / Permission |
|---|---|---|
| Power Apps | Intake, review, management UI | Maker role for developers; app share/run permission for users; environment access |
| Power Automate | Routing, approvals, audit history, alerts | Flow owner/co-owner for developers; connector permissions; run-only access where applicable |
| SharePoint Online | Lists, documents, evidence | Site/List/Library permissions based on role; least-privilege contributor/read access |
| Dataverse | Relational production data when premium architecture is required | Environment access plus Dataverse security roles; table privileges scoped by job function |
| Power BI | Operational and executive analytics | Workspace Contributor/Member for developers; Viewer/app access for consumers; dataset permissions as required |
| Microsoft Entra ID | Identity and security groups | Group membership; tenant/admin changes restricted to authorized administrators |
| Power Platform Admin Center | Environment, DLP, capacity, governance | Power Platform Administrator or delegated Environment Administrator for administrative functions |

## Permission Model
```text
Tenant / Power Platform Admin
  → environment + DLP + capacity governance

Solution Architect / Developer
  → maker access in DEV
  → controlled deployment rights to TEST
  → no unrestricted production data administration

Business Reviewer / Approver
  → application access
  → scoped Dataverse/SharePoint records
  → approval actions

End User
  → application run permission
  → least-privilege record access

BI Consumer
  → report/app Viewer access
```

## License Structure & Estimated Commercial List Cost
| Component | Example Licensing Approach | Estimated Public List Price* |
|---|---|---:|
| Power Apps Developer Plan | Individual development/testing | $0 |
| Power Apps Premium | Production premium apps, Dataverse, premium/custom connectors | $20/user/month |
| Power Apps Premium — 2,000+ seats | Large-scale deployment, qualifying minimum | $12/user/month |
| Power Automate Premium | User-based premium cloud/attended automation | $15/user/month |
| Power Automate Process | Core enterprise process or unattended automation | $150/bot/month |
| Power Automate Hosted Process | Process license plus Microsoft-hosted VM | $215/bot/month |
| Power BI Pro | Shared BI authoring/collaboration | $14/user/month |
| Power BI Premium Per User | Pro plus most Premium features per user | $24/user/month |
| Dataverse Database Capacity add-on | Additional relational storage | $40/GB/month |

*Public commercial USD reference pricing; government, GCC/GCC High/DoD, enterprise agreements, volume licensing, contract vehicles, region, taxes, and negotiated terms can change actual pricing. Architecture must be validated against the customer's tenant and licensing agreement before deployment.

## Example Cost Scenario
For a small premium solution with 5 makers/power users on Power Apps Premium, 2 automation developers on Power Automate Premium, and 10 Power BI Pro users:

```text
Power Apps:      5 × $20 = $100/month
Power Automate:  2 × $15 =  $30/month
Power BI Pro:   10 × $14 = $140/month
-------------------------------------
Illustrative total          $270/month
Illustrative annual       $3,240/year
```

This excludes Microsoft 365 base licensing, Azure consumption, extra Dataverse capacity, AI services, taxes, government-specific licensing, and enterprise discounts.

## Licensing Decision Logic
```text
IF app uses only Microsoft 365 standard capabilities
   THEN validate included M365 use rights before buying premium licensing
ELSE IF app uses Dataverse, premium connectors, or custom connectors
   THEN evaluate Power Apps Premium for each production user

IF premium automated flow has one/few licensed owners
   THEN evaluate Power Automate Premium user licensing
ELSE IF core process is invoked by many users or uses unattended RPA
   THEN evaluate Power Automate Process licensing

IF BI workspace uses shared capacity
   THEN authors/consumers generally require Pro as applicable
ELSE IF Premium/Fabric capacity is used
   THEN evaluate capacity-based consumer access rules
```

## Power Fx Example
```powerfx
If(
    IsBlank(txtTitle.Text) || IsBlank(dpDueDate.SelectedDate),
    Notify("Required fields are missing", NotificationType.Error),
    Patch(
        Requests,
        Defaults(Requests),
        {
            Title: txtTitle.Text,
            DueDate: dpDueDate.SelectedDate,
            Status: {Value:"Submitted"},
            SubmittedOn: Now()
        }
    )
)
```

## Real-Time Automation
```text
When request is created or modified:
1. Validate workflow state
2. Capture previous/new status
3. Write audit-history record
4. Route to responsible reviewer
5. Evaluate SLA / due-date threshold
6. Send exception notification when threshold is breached
7. Refresh operational reporting
```

## Projection
```DAX
Projected SLA Breaches =
CALCULATE(
    [Open Requests],
    Requests[SLADueDate] <= NOW() + 3,
    Requests[PercentComplete] < 0.80
)
```

## Capability Demonstrated
Power Apps • Power Fx • Power Automate • SharePoint/Dataverse • workflow architecture • ALM • governance • licensing analysis • permissions design • cost estimation • validation • auditability • operational analytics

## Pricing References
- Microsoft Power Apps pricing: https://www.microsoft.com/en-us/power-platform/products/power-apps/pricing/
- Microsoft Power Automate pricing: https://www.microsoft.com/en-us/power-platform/products/power-automate/pricing
- Microsoft Power BI licensing: https://learn.microsoft.com/en-us/power-bi/fundamentals/service-features-license-type
