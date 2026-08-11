# Power Platform Code & Workflow Logic Page

Pairs with REAL-TIME-SOLUTION.md. This page shows the Power Fx, automation, validation, security, and workflow logic behind the solution without fenced code blocks.

## Power Fx — Intake Validation
| Requirement | Power Fx Logic |
|---|---|
| Required Title | IsBlank(txtTitle.Text) |
| Required Due Date | IsBlank(dpDueDate.SelectedDate) |
| Due Date cannot be historical | dpDueDate.SelectedDate < Today() |
| Submit error | Notify("Required information is missing", NotificationType.Error) |
| New record | Patch(Requests, Defaults(Requests), {...}) |
| Submission timestamp | SubmittedOn: Now() |
| Submitted status | Status: {Value: "Submitted"} |

## Save Draft Logic
| Condition | Action |
|---|---|
| User selects Save Draft | Set(varSubmissionAction, "Draft") |
| Draft validation | Validate only fields required to identify/save record |
| Record status | Draft |
| Visibility | Restrict draft to submitter and authorized support roles |
| Resume | Load existing draft into form by record ID / submitter |

## Submit Logic
| Condition | Action |
|---|---|
| User selects Review & Submit | Set(varSubmissionAction, "Submit") |
| Missing required submission field | Stop + notification |
| Duplicate governed identifier | Stop + duplicate warning |
| Valid submission | Patch/SubmitForm |
| Successful submit | Status = Pending Review |

## Review Workflow
| Reviewer Action | System Logic |
|---|---|
| Approve | Set approved state; capture reviewer/date; route forward |
| Return | Require comments; return to submitter; log action |
| Reject | Require disposition; lock record according to policy |
| Field changed | Capture previous value + new value in audit history |

## Power Automate Logic
1. Trigger on record creation or modification.
2. Read current workflow state.
3. Compare current values with prior governed state.
4. Write audit-history record.
5. Determine next owner from status and role mapping.
6. Send notification or approval.
7. Evaluate due date / SLA.
8. Create escalation when threshold is breached.
9. Update reporting timestamp.

## DAX Operational Measures
| Measure | Logic |
|---|---|
| Open Requests | Count records where Status not Closed/Rejected |
| Overdue Requests | Open records with DueDate < TODAY() |
| Average Review Time | Average Submitted-to-Review duration |
| Return Rate | Returned submissions ÷ submitted records |
| Projected SLA Breaches | Open requests due within threshold with completion below target |

## Security Logic
| User Type | Access Pattern |
|---|---|
| Submitter | Create + read own draft/submission as policy allows |
| Reviewer | Read assigned records + approved review actions |
| Program Owner | Read/manage scoped program records |
| Developer | DEV maker; controlled TEST deployment |
| Administrator | Environment/DLP/capacity administration only where authorized |
| BI Consumer | Read published reporting |

## Role Evidence
Power Platform Solution Architect • Senior Power Platform Developer • Power Apps Developer • Power Automate Developer • Workflow Automation Lead • Power Platform Governance Lead
