# Government Sector | Full Code & Logic

This page pairs with the government real-time mission solution. Code is presented directly on the white GitHub page with no fenced gray code panels.

## Power Fx | Closure Readiness

<samp>Set(<br>&nbsp;&nbsp;&nbsp;&nbsp;varOpenRecommendations,<br>&nbsp;&nbsp;&nbsp;&nbsp;CountRows(Filter(Recommendations, DeficiencyNumber = varDeficiency.DeficiencyNumber && Status.Value &lt;&gt; "Closed"))<br>);<br>Set(<br>&nbsp;&nbsp;&nbsp;&nbsp;varOpenActions,<br>&nbsp;&nbsp;&nbsp;&nbsp;CountRows(Filter(CorrectiveActions, DeficiencyNumber = varDeficiency.DeficiencyNumber && Status.Value &lt;&gt; "Completed"))<br>);<br>Set(<br>&nbsp;&nbsp;&nbsp;&nbsp;varOpenMilestones,<br>&nbsp;&nbsp;&nbsp;&nbsp;CountRows(Filter(Milestones, DeficiencyNumber = varDeficiency.DeficiencyNumber && Status.Value &lt;&gt; "Completed"))<br>);<br>Set(<br>&nbsp;&nbsp;&nbsp;&nbsp;varMissingEvidence,<br>&nbsp;&nbsp;&nbsp;&nbsp;CountRows(Filter(Evidence, DeficiencyNumber = varDeficiency.DeficiencyNumber && Required = true && IsBlank(DocumentLink)))<br>);<br><br>If(<br>&nbsp;&nbsp;&nbsp;&nbsp;varOpenRecommendations + varOpenActions + varOpenMilestones + varMissingEvidence &gt; 0,<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Closure requirements remain incomplete.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;Patch(Deficiencies, varDeficiency, {Status: {Value: "Pending Closure"}, ClosureRequestedOn: Now(), ClosureRequestedBy: Lower(User().Email)})<br>)</samp>

## Power Fx | Revised ECD Validation

<samp>If(<br>&nbsp;&nbsp;&nbsp;&nbsp;dpCurrentECD.SelectedDate &lt; dpOriginalECD.SelectedDate,<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Current ECD cannot be earlier than the original ECD without approved exception logic.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;dpCurrentECD.SelectedDate &lt;&gt; dpOriginalECD.SelectedDate && IsBlank(Trim(txtECDJustification.Text)),<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("ECD revision justification is required.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;Patch(CorrectiveActions, varAction, {CurrentECD: dpCurrentECD.SelectedDate, ECDJustification: Trim(txtECDJustification.Text), ECDRevisedOn: Now(), ECDRevisedBy: Lower(User().Email)})<br>)</samp>

## SQL | Mission Exposure Queue

<samp>SELECT<br>&nbsp;&nbsp;&nbsp;&nbsp;d.ReportNumber,<br>&nbsp;&nbsp;&nbsp;&nbsp;d.DeficiencyNumber,<br>&nbsp;&nbsp;&nbsp;&nbsp;r.RecommendationNumber,<br>&nbsp;&nbsp;&nbsp;&nbsp;ca.ActionID,<br>&nbsp;&nbsp;&nbsp;&nbsp;ca.Owner,<br>&nbsp;&nbsp;&nbsp;&nbsp;ca.Status,<br>&nbsp;&nbsp;&nbsp;&nbsp;ca.CurrentECD,<br>&nbsp;&nbsp;&nbsp;&nbsp;DATEDIFF(day, GETDATE(), ca.CurrentECD) AS DaysToECD,<br>&nbsp;&nbsp;&nbsp;&nbsp;CASE<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHEN ca.CurrentECD &lt; GETDATE() AND ca.Status &lt;&gt; 'Completed' THEN 'OVERDUE'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHEN DATEDIFF(day, GETDATE(), ca.CurrentECD) &lt;= 30 THEN '30 DAY'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHEN DATEDIFF(day, GETDATE(), ca.CurrentECD) &lt;= 60 THEN '60 DAY'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHEN DATEDIFF(day, GETDATE(), ca.CurrentECD) &lt;= 90 THEN '90 DAY'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE 'MONITOR'<br>&nbsp;&nbsp;&nbsp;&nbsp;END AS ExposureWindow<br>FROM Deficiencies d<br>JOIN Recommendations r ON r.DeficiencyNumber = d.DeficiencyNumber<br>JOIN CorrectiveActions ca ON ca.RecommendationNumber = r.RecommendationNumber<br>WHERE d.Status &lt;&gt; 'Closed';</samp>

## Python | Program Health Engine

<samp>def calculate_program_health(overdue_actions, open_critical, milestone_completion, days_to_ecd):<br>&nbsp;&nbsp;&nbsp;&nbsp;if open_critical &gt; 0 or overdue_actions &gt;= 3 or days_to_ecd &lt; 0:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return "RED"<br><br>&nbsp;&nbsp;&nbsp;&nbsp;if overdue_actions &gt; 0 or milestone_completion &lt; 0.80 or days_to_ecd &lt;= 30:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return "AMBER"<br><br>&nbsp;&nbsp;&nbsp;&nbsp;return "GREEN"</samp>

## DAX | Overdue Corrective Actions

<samp>Overdue Corrective Actions =<br>CALCULATE(<br>&nbsp;&nbsp;&nbsp;&nbsp;COUNTROWS(CorrectiveActions),<br>&nbsp;&nbsp;&nbsp;&nbsp;CorrectiveActions[CurrentECD] &lt; TODAY(),<br>&nbsp;&nbsp;&nbsp;&nbsp;CorrectiveActions[Status] &lt;&gt; "Completed"<br>)</samp>

## DAX | Corrective Action Completion Rate

<samp>Corrective Action Completion Rate =<br>DIVIDE(<br>&nbsp;&nbsp;&nbsp;&nbsp;CALCULATE(COUNTROWS(CorrectiveActions), CorrectiveActions[Status] = "Completed"),<br>&nbsp;&nbsp;&nbsp;&nbsp;COUNTROWS(CorrectiveActions),<br>&nbsp;&nbsp;&nbsp;&nbsp;0<br>)</samp>

## DAX | 30-Day Exposure

<samp>30 Day Exposure =<br>CALCULATE(<br>&nbsp;&nbsp;&nbsp;&nbsp;COUNTROWS(CorrectiveActions),<br>&nbsp;&nbsp;&nbsp;&nbsp;CorrectiveActions[CurrentECD] &gt;= TODAY(),<br>&nbsp;&nbsp;&nbsp;&nbsp;CorrectiveActions[CurrentECD] &lt;= TODAY() + 30,<br>&nbsp;&nbsp;&nbsp;&nbsp;CorrectiveActions[Status] &lt;&gt; "Completed"<br>)</samp>

## Audit History | Required Write

<samp>RecordID = governed record identifier<br>RecordType = Deficiency | Recommendation | Corrective Action | Milestone<br>Action = Create | Submit | Approve | Return | Reject | Status Change | ECD Change | Closure<br>PreviousValue = value before material change<br>NewValue = value after material change<br>ActionBy = authenticated user<br>ActionDateTime = UTC timestamp<br>Comments = required justification or review comments when applicable</samp>
