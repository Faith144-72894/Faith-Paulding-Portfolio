# Power Platform | Full Build Code

This page pairs with the real-time solution and presents the build formulas on the white GitHub page itself. The formulas below are written as they would be entered in Power Apps, Power Automate, and Power BI. No fenced or indented Markdown code blocks are used.

## Power Apps | Screen OnVisible

<samp>Set(varSubmissionAction, Blank());<br>Set(varCurrentUserEmail, Lower(User().Email));<br>Set(varIsReviewer, !IsBlank(LookUp(ReviewerSecurity, Lower(Email) = varCurrentUserEmail)));<br>Set(varToday, Today());<br>Refresh(Requests);<br>Refresh(AuditHistory);</samp>

## Power Apps | Save Draft Button OnSelect

<samp>Set(varSubmissionAction, "Draft");<br>If(<br>&nbsp;&nbsp;&nbsp;&nbsp;IsBlank(Trim(txtTitle.Text)),<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Enter a title before saving the draft.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;If(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IsBlank(varCurrentRecord),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;varCurrentRecord,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Patch(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Requests,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Defaults(Requests),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Title: Trim(txtTitle.Text),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Description: Trim(txtDescription.Text),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DueDate: dpDueDate.SelectedDate,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Status: {Value: "Draft"},<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SubmittedByEmail: Lower(User().Email),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SubmittedByName: User().FullName,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DraftSavedOn: Now(),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LastModifiedOn: Now()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;varCurrentRecord,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Patch(Requests, varCurrentRecord, {Title: Trim(txtTitle.Text), Description: Trim(txtDescription.Text), DueDate: dpDueDate.SelectedDate, Status: {Value: "Draft"}, DraftSavedOn: Now(), LastModifiedOn: Now()})<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;);<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Draft saved.", NotificationType.Success)<br>)</samp>

## Power Apps | Review & Submit Button OnSelect

<samp>Set(varSubmissionAction, "Submit");<br>Set(varDuplicateCount, CountRows(Filter(Requests, Lower(Title) = Lower(Trim(txtTitle.Text)) && ID &lt;&gt; Coalesce(varCurrentRecord.ID, -1))));<br><br>If(<br>&nbsp;&nbsp;&nbsp;&nbsp;IsBlank(Trim(txtTitle.Text)), Notify("Title is required.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;IsBlank(Trim(txtDescription.Text)), Notify("Description is required.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;IsBlank(dpDueDate.SelectedDate), Notify("Due date is required.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;dpDueDate.SelectedDate &lt; Today(), Notify("Due date cannot be earlier than today.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;varDuplicateCount &gt; 0, Notify("A possible duplicate record already exists. Review before submitting.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;Set(varCurrentRecord, Patch(Requests, Coalesce(varCurrentRecord, Defaults(Requests)), {Title: Trim(txtTitle.Text), Description: Trim(txtDescription.Text), DueDate: dpDueDate.SelectedDate, Status: {Value: "Pending Review"}, SubmittedByEmail: Lower(User().Email), SubmittedByName: User().FullName, SubmittedOn: Now(), LastModifiedOn: Now()}));<br>&nbsp;&nbsp;&nbsp;&nbsp;Patch(AuditHistory, Defaults(AuditHistory), {RequestID: varCurrentRecord.ID, Action: "Submitted", PreviousStatus: "Draft", NewStatus: "Pending Review", ActionByEmail: Lower(User().Email), ActionByName: User().FullName, ActionDateTime: Now()});<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Request submitted for review.", NotificationType.Success)<br>)</samp>

## Power Apps | Reviewer Approve Button OnSelect

<samp>If(<br>&nbsp;&nbsp;&nbsp;&nbsp;!varIsReviewer,<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("You do not have reviewer permission.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;Set(varPreviousStatus, varCurrentRecord.Status.Value);<br>&nbsp;&nbsp;&nbsp;&nbsp;Set(varCurrentRecord, Patch(Requests, varCurrentRecord, {Status: {Value: "Approved"}, ReviewedByEmail: Lower(User().Email), ReviewedByName: User().FullName, ReviewedOn: Now(), ReviewComments: Trim(txtReviewerComments.Text), LastModifiedOn: Now()}));<br>&nbsp;&nbsp;&nbsp;&nbsp;Patch(AuditHistory, Defaults(AuditHistory), {RequestID: varCurrentRecord.ID, Action: "Approved", PreviousStatus: varPreviousStatus, NewStatus: "Approved", Comments: Trim(txtReviewerComments.Text), ActionByEmail: Lower(User().Email), ActionByName: User().FullName, ActionDateTime: Now()});<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Request approved.", NotificationType.Success)<br>)</samp>

## Power Apps | Reviewer Return Button OnSelect

<samp>If(<br>&nbsp;&nbsp;&nbsp;&nbsp;IsBlank(Trim(txtReviewerComments.Text)),<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Return comments are required.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;Set(varPreviousStatus, varCurrentRecord.Status.Value);<br>&nbsp;&nbsp;&nbsp;&nbsp;Set(varCurrentRecord, Patch(Requests, varCurrentRecord, {Status: {Value: "Returned"}, ReviewComments: Trim(txtReviewerComments.Text), ReviewedByEmail: Lower(User().Email), ReviewedByName: User().FullName, ReviewedOn: Now(), LastModifiedOn: Now()}));<br>&nbsp;&nbsp;&nbsp;&nbsp;Patch(AuditHistory, Defaults(AuditHistory), {RequestID: varCurrentRecord.ID, Action: "Returned", PreviousStatus: varPreviousStatus, NewStatus: "Returned", Comments: Trim(txtReviewerComments.Text), ActionByEmail: Lower(User().Email), ActionByName: User().FullName, ActionDateTime: Now()});<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Request returned to the submitter.", NotificationType.Success)<br>)</samp>

## Power Apps | My Drafts Gallery Items

<samp>SortByColumns(<br>&nbsp;&nbsp;&nbsp;&nbsp;Filter(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Requests,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lower(SubmittedByEmail) = Lower(User().Email) &&<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Status.Value = "Draft"<br>&nbsp;&nbsp;&nbsp;&nbsp;),<br>&nbsp;&nbsp;&nbsp;&nbsp;"LastModifiedOn",<br>&nbsp;&nbsp;&nbsp;&nbsp;SortOrder.Descending<br>)</samp>

## Power Apps | Reviewer Queue Gallery Items

<samp>SortByColumns(<br>&nbsp;&nbsp;&nbsp;&nbsp;Filter(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Requests,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Status.Value = "Pending Review"<br>&nbsp;&nbsp;&nbsp;&nbsp;),<br>&nbsp;&nbsp;&nbsp;&nbsp;"SubmittedOn",<br>&nbsp;&nbsp;&nbsp;&nbsp;SortOrder.Ascending<br>)</samp>

## Power Apps | Status Display Formula

<samp>Switch(<br>&nbsp;&nbsp;&nbsp;&nbsp;ThisItem.Status.Value,<br>&nbsp;&nbsp;&nbsp;&nbsp;"Draft", "Draft",<br>&nbsp;&nbsp;&nbsp;&nbsp;"Pending Review", "Pending Review",<br>&nbsp;&nbsp;&nbsp;&nbsp;"Returned", "Returned for Revision",<br>&nbsp;&nbsp;&nbsp;&nbsp;"Approved", "Approved",<br>&nbsp;&nbsp;&nbsp;&nbsp;"Rejected", "Rejected",<br>&nbsp;&nbsp;&nbsp;&nbsp;"Unknown"<br>)</samp>

## Power Automate | Trigger Condition

<samp>@or(<br>&nbsp;&nbsp;&nbsp;&nbsp;equals(triggerOutputs()?['body/Status/Value'], 'Pending Review'),<br>&nbsp;&nbsp;&nbsp;&nbsp;equals(triggerOutputs()?['body/Status/Value'], 'Approved'),<br>&nbsp;&nbsp;&nbsp;&nbsp;equals(triggerOutputs()?['body/Status/Value'], 'Returned')<br>)</samp>

## Power Automate | Days Until Due Expression

<samp>div(<br>&nbsp;&nbsp;&nbsp;&nbsp;sub(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ticks(triggerOutputs()?['body/DueDate']),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ticks(utcNow())<br>&nbsp;&nbsp;&nbsp;&nbsp;),<br>&nbsp;&nbsp;&nbsp;&nbsp;864000000000<br>)</samp>

## Power Automate | Escalation Condition

<samp>@and(<br>&nbsp;&nbsp;&nbsp;&nbsp;lessOrEquals(outputs('Days_Until_Due'), 3),<br>&nbsp;&nbsp;&nbsp;&nbsp;not(equals(triggerOutputs()?['body/Status/Value'], 'Approved')),<br>&nbsp;&nbsp;&nbsp;&nbsp;not(equals(triggerOutputs()?['body/Status/Value'], 'Closed'))<br>)</samp>

## Power Automate | Audit History Payload

<samp>RequestID = triggerOutputs()?['body/ID']<br>Action = triggerOutputs()?['body/Status/Value']<br>PreviousStatus = variables('PreviousStatus')<br>NewStatus = triggerOutputs()?['body/Status/Value']<br>ActionByEmail = triggerOutputs()?['body/Editor/Email']<br>ActionDateTime = utcNow()<br>Comments = coalesce(triggerOutputs()?['body/ReviewComments'], '')</samp>

## Power BI | Open Requests

<samp>Open Requests =<br>CALCULATE(<br>&nbsp;&nbsp;&nbsp;&nbsp;COUNTROWS(Requests),<br>&nbsp;&nbsp;&nbsp;&nbsp;NOT(Requests[Status] IN {"Closed", "Rejected"})<br>)</samp>

## Power BI | Overdue Requests

<samp>Overdue Requests =<br>CALCULATE(<br>&nbsp;&nbsp;&nbsp;&nbsp;COUNTROWS(Requests),<br>&nbsp;&nbsp;&nbsp;&nbsp;Requests[DueDate] &lt; TODAY(),<br>&nbsp;&nbsp;&nbsp;&nbsp;NOT(Requests[Status] IN {"Closed", "Rejected"})<br>)</samp>

## Power BI | Average Review Time

<samp>Average Review Time Days =<br>AVERAGEX(<br>&nbsp;&nbsp;&nbsp;&nbsp;FILTER(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Requests,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NOT(ISBLANK(Requests[SubmittedOn])) &&<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NOT(ISBLANK(Requests[ReviewedOn]))<br>&nbsp;&nbsp;&nbsp;&nbsp;),<br>&nbsp;&nbsp;&nbsp;&nbsp;DATEDIFF(Requests[SubmittedOn], Requests[ReviewedOn], DAY)<br>)</samp>

## Power BI | Return Rate

<samp>Return Rate =<br>DIVIDE(<br>&nbsp;&nbsp;&nbsp;&nbsp;CALCULATE(COUNTROWS(Requests), Requests[Status] = "Returned"),<br>&nbsp;&nbsp;&nbsp;&nbsp;CALCULATE(COUNTROWS(Requests), NOT(ISBLANK(Requests[SubmittedOn]))),<br>&nbsp;&nbsp;&nbsp;&nbsp;0<br>)</samp>

## Power BI | Projected SLA Breaches

<samp>Projected SLA Breaches =<br>CALCULATE(<br>&nbsp;&nbsp;&nbsp;&nbsp;COUNTROWS(Requests),<br>&nbsp;&nbsp;&nbsp;&nbsp;Requests[Status] &lt;&gt; "Closed",<br>&nbsp;&nbsp;&nbsp;&nbsp;Requests[SLADueDate] &gt;= NOW(),<br>&nbsp;&nbsp;&nbsp;&nbsp;Requests[SLADueDate] &lt;= NOW() + 3,<br>&nbsp;&nbsp;&nbsp;&nbsp;Requests[PercentComplete] &lt; 0.80<br>)</samp>

## What This Code Demonstrates

The page contains the working Power Fx formulas, Power Automate expressions, DAX measures, validation sequence, status transitions, audit-history writes, reviewer controls, queue filtering, SLA logic, and projection measures behind the real-time solution.

Role alignment: Power Platform Solution Architect • Senior Power Platform Developer • Power Apps Developer • Power Automate Developer • Workflow Automation Lead • Power Platform Governance Lead
