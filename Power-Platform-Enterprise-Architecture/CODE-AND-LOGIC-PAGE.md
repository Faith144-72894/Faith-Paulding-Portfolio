# Power Platform | Full Build Code

This is the working-code companion to the real-time solution. The formulas are written in the form I would enter into Power Apps and Power BI. They are intentionally displayed as plain text rather than fenced Markdown code blocks.

## Power Apps — Screen OnVisible

    Set(varSubmissionAction, Blank());
    Set(varCurrentUserEmail, Lower(User().Email));
    Set(varIsReviewer, !IsBlank(LookUp(ReviewerSecurity, Lower(Email) = varCurrentUserEmail)));
    Set(varToday, Today());
    Refresh(Requests);
    Refresh(AuditHistory);

## Power Apps — Save Draft Button OnSelect

    Set(varSubmissionAction, "Draft");
    If(
        IsBlank(Trim(txtTitle.Text)),
        Notify("Enter a title before saving the draft.", NotificationType.Error),
        If(
            IsBlank(varCurrentRecord),
            Set(
                varCurrentRecord,
                Patch(
                    Requests,
                    Defaults(Requests),
                    {
                        Title: Trim(txtTitle.Text),
                        Description: Trim(txtDescription.Text),
                        DueDate: dpDueDate.SelectedDate,
                        Status: {Value: "Draft"},
                        SubmittedByEmail: Lower(User().Email),
                        SubmittedByName: User().FullName,
                        DraftSavedOn: Now(),
                        LastModifiedOn: Now()
                    }
                )
            ),
            Set(
                varCurrentRecord,
                Patch(
                    Requests,
                    varCurrentRecord,
                    {
                        Title: Trim(txtTitle.Text),
                        Description: Trim(txtDescription.Text),
                        DueDate: dpDueDate.SelectedDate,
                        Status: {Value: "Draft"},
                        DraftSavedOn: Now(),
                        LastModifiedOn: Now()
                    }
                )
            )
        );
        Notify("Draft saved.", NotificationType.Success)
    )

## Power Apps — Review & Submit Button OnSelect

    Set(varSubmissionAction, "Submit");
    Set(varDuplicateCount, CountRows(Filter(Requests, Lower(Title) = Lower(Trim(txtTitle.Text)) && ID <> Coalesce(varCurrentRecord.ID, -1))));

    If(
        IsBlank(Trim(txtTitle.Text)),
        Notify("Title is required.", NotificationType.Error),
        IsBlank(Trim(txtDescription.Text)),
        Notify("Description is required.", NotificationType.Error),
        IsBlank(dpDueDate.SelectedDate),
        Notify("Due date is required.", NotificationType.Error),
        dpDueDate.SelectedDate < Today(),
        Notify("Due date cannot be earlier than today.", NotificationType.Error),
        varDuplicateCount > 0,
        Notify("A possible duplicate record already exists. Review before submitting.", NotificationType.Error),
        Set(
            varCurrentRecord,
            Patch(
                Requests,
                Coalesce(varCurrentRecord, Defaults(Requests)),
                {
                    Title: Trim(txtTitle.Text),
                    Description: Trim(txtDescription.Text),
                    DueDate: dpDueDate.SelectedDate,
                    Status: {Value: "Pending Review"},
                    SubmittedByEmail: Lower(User().Email),
                    SubmittedByName: User().FullName,
                    SubmittedOn: Now(),
                    LastModifiedOn: Now()
                }
            )
        );
        Patch(
            AuditHistory,
            Defaults(AuditHistory),
            {
                RequestID: varCurrentRecord.ID,
                Action: "Submitted",
                PreviousStatus: "Draft",
                NewStatus: "Pending Review",
                ActionByEmail: Lower(User().Email),
                ActionByName: User().FullName,
                ActionDateTime: Now()
            }
        );
        Notify("Request submitted for review.", NotificationType.Success)
    )

## Power Apps — Reviewer Approve Button OnSelect

    If(
        !varIsReviewer,
        Notify("You do not have reviewer permission.", NotificationType.Error),
        Set(varPreviousStatus, varCurrentRecord.Status.Value);
        Set(
            varCurrentRecord,
            Patch(
                Requests,
                varCurrentRecord,
                {
                    Status: {Value: "Approved"},
                    ReviewedByEmail: Lower(User().Email),
                    ReviewedByName: User().FullName,
                    ReviewedOn: Now(),
                    ReviewComments: Trim(txtReviewerComments.Text),
                    LastModifiedOn: Now()
                }
            )
        );
        Patch(
            AuditHistory,
            Defaults(AuditHistory),
            {
                RequestID: varCurrentRecord.ID,
                Action: "Approved",
                PreviousStatus: varPreviousStatus,
                NewStatus: "Approved",
                Comments: Trim(txtReviewerComments.Text),
                ActionByEmail: Lower(User().Email),
                ActionByName: User().FullName,
                ActionDateTime: Now()
            }
        );
        Notify("Request approved.", NotificationType.Success)
    )

## Power Apps — Reviewer Return Button OnSelect

    If(
        IsBlank(Trim(txtReviewerComments.Text)),
        Notify("Return comments are required.", NotificationType.Error),
        Set(varPreviousStatus, varCurrentRecord.Status.Value);
        Set(
            varCurrentRecord,
            Patch(
                Requests,
                varCurrentRecord,
                {
                    Status: {Value: "Returned"},
                    ReviewComments: Trim(txtReviewerComments.Text),
                    ReviewedByEmail: Lower(User().Email),
                    ReviewedByName: User().FullName,
                    ReviewedOn: Now(),
                    LastModifiedOn: Now()
                }
            )
        );
        Patch(
            AuditHistory,
            Defaults(AuditHistory),
            {
                RequestID: varCurrentRecord.ID,
                Action: "Returned",
                PreviousStatus: varPreviousStatus,
                NewStatus: "Returned",
                Comments: Trim(txtReviewerComments.Text),
                ActionByEmail: Lower(User().Email),
                ActionByName: User().FullName,
                ActionDateTime: Now()
            }
        );
        Notify("Request returned to the submitter.", NotificationType.Success)
    )

## Power Apps — My Drafts Gallery Items

    SortByColumns(
        Filter(
            Requests,
            Lower(SubmittedByEmail) = Lower(User().Email) &&
            Status.Value = "Draft"
        ),
        "LastModifiedOn",
        SortOrder.Descending
    )

## Power Apps — Reviewer Queue Gallery Items

    SortByColumns(
        Filter(
            Requests,
            Status.Value = "Pending Review"
        ),
        "SubmittedOn",
        SortOrder.Ascending
    )

## Power Apps — Status Display Formula

    Switch(
        ThisItem.Status.Value,
        "Draft", "Draft",
        "Pending Review", "Pending Review",
        "Returned", "Returned for Revision",
        "Approved", "Approved",
        "Rejected", "Rejected",
        "Unknown"
    )

## Power Automate — Trigger Condition

    @or(
        equals(triggerOutputs()?['body/Status/Value'], 'Pending Review'),
        equals(triggerOutputs()?['body/Status/Value'], 'Approved'),
        equals(triggerOutputs()?['body/Status/Value'], 'Returned')
    )

## Power Automate — Days Until Due Expression

    div(
        sub(
            ticks(triggerOutputs()?['body/DueDate']),
            ticks(utcNow())
        ),
        864000000000
    )

## Power Automate — Escalation Condition

    @and(
        lessOrEquals(outputs('Days_Until_Due'), 3),
        not(equals(triggerOutputs()?['body/Status/Value'], 'Approved')),
        not(equals(triggerOutputs()?['body/Status/Value'], 'Closed'))
    )

## Power Automate — Audit History Payload

    RequestID = triggerOutputs()?['body/ID']
    Action = triggerOutputs()?['body/Status/Value']
    PreviousStatus = variables('PreviousStatus')
    NewStatus = triggerOutputs()?['body/Status/Value']
    ActionByEmail = triggerOutputs()?['body/Editor/Email']
    ActionDateTime = utcNow()
    Comments = coalesce(triggerOutputs()?['body/ReviewComments'], '')

## Power BI — Open Requests

    Open Requests =
    CALCULATE(
        COUNTROWS(Requests),
        NOT(Requests[Status] IN {"Closed", "Rejected"})
    )

## Power BI — Overdue Requests

    Overdue Requests =
    CALCULATE(
        COUNTROWS(Requests),
        Requests[DueDate] < TODAY(),
        NOT(Requests[Status] IN {"Closed", "Rejected"})
    )

## Power BI — Average Review Time

    Average Review Time Days =
    AVERAGEX(
        FILTER(
            Requests,
            NOT(ISBLANK(Requests[SubmittedOn])) &&
            NOT(ISBLANK(Requests[ReviewedOn]))
        ),
        DATEDIFF(Requests[SubmittedOn], Requests[ReviewedOn], DAY)
    )

## Power BI — Return Rate

    Return Rate =
    DIVIDE(
        CALCULATE(COUNTROWS(Requests), Requests[Status] = "Returned"),
        CALCULATE(COUNTROWS(Requests), NOT(ISBLANK(Requests[SubmittedOn]))),
        0
    )

## Power BI — Projected SLA Breaches

    Projected SLA Breaches =
    CALCULATE(
        COUNTROWS(Requests),
        Requests[Status] <> "Closed",
        Requests[SLADueDate] >= NOW(),
        Requests[SLADueDate] <= NOW() + 3,
        Requests[PercentComplete] < 0.80
    )

## What This Code Demonstrates

This is not pseudocode standing in for the build. The page shows the Power Fx formulas, Power Automate expressions, DAX measures, validation sequence, status transitions, audit-history writes, reviewer permissions, queue filtering, SLA logic, and projection measures that would sit behind the real-time solution.

Role alignment: Power Platform Solution Architect • Senior Power Platform Developer • Power Apps Developer • Power Automate Developer • Workflow Automation Lead • Power Platform Governance Lead
