# Government-Audit-Compliance-Management-System
A sanitized PL-600 portfolio solution demonstrating a government audit and compliance management system built with Power Apps, Power Automate, Power BI, SharePoint, Power Fx, and Microsoft 365. Includes automated intake, approvals, corrective-action tracking, audit trails, forecasting, and executive reporting using fictional data.
## Project Overview

This solution modernizes fragmented audit processes traditionally managed through emails, spreadsheets, manual approvals, and disconnected legacy systems. It provides a centralized platform for audit intake, internal review, corrective-action planning, milestone tracking, deficiency closure, and executive reporting.

All records, organizations, users, metrics, and examples presented in this repository are fictional.

## Business Challenge

Government organizations frequently experience:

- Disconnected audit and compliance records
- Manual intake and approval processes
- Limited visibility into overdue deficiencies
- Inconsistent naming and data standards
- Difficulty tracking corrective actions and milestones
- Time-consuming executive reporting
- Limited audit trails and accountability
- High costs associated with traditional eGRC platforms

## Proposed Solution

The solution uses Microsoft Power Platform and Microsoft 365 to provide:

- Centralized audit and deficiency intake
- Automated internal review and approval routing
- Recommendation and Corrective Action Plan management
- Milestone and Estimated Completion Date tracking
- Role-based application experiences
- Automated reminders and escalation notifications
- Historical audit trails
- 30-, 60-, and 90-day risk forecasting
- Interactive Power BI executive dashboards

## Application Workflows

### Workflow 1: External Intake

Captures new submissions, validates required information, assigns a tracking number, and allows users to save drafts before submission.

### Workflow 2: Internal Review

Routes submitted records to authorized reviewers for validation, correction, approval, rejection, or return to the submitter.

### Workflow 3: Recommendations and Corrective Actions

Connects deficiencies to recommendations, corrective actions, responsible owners, milestones, supporting documentation, and completion dates.

### Workflow 4: Deficiency Management and Closure

Tracks the complete deficiency lifecycle and verifies that all recommendations, corrective actions, milestones, documentation, and approvals are complete before closure.

## Microsoft Technology Stack

| Technology | Solution Role |
|---|---|
| Power Apps | Responsive user interface and workflow application |
| Power Fx | Validation, navigation, filtering, record creation, and business logic |
| Power Automate | Approvals, notifications, routing, audit trails, and escalation |
| SharePoint Online | Structured data storage and document management |
| Dataverse | Recommended enterprise relational data platform |
| Power BI | Executive dashboards, trends, forecasting, and compliance reporting |
| Power Query | Data transformation, standardization, and quality checks |
| DAX | Risk calculations, KPIs, overdue indicators, and forecasting |
| SQL | Data integration, validation, and scalable reporting support |
| Microsoft Teams | Collaboration, alerts, and application access |

## Solution Architecture

```mermaid
flowchart TD
    A[Power Apps] --> B[SharePoint or Dataverse]
    A --> C[Power Automate]
    C --> B
    B --> D[Power BI]
    C --> E[Teams and Outlook]
