# Public Sector | Full Code & Logic

This page pairs directly with the real-time customer modernization solution. The code is displayed on the white GitHub page rather than in fenced gray code blocks.

## Python | Transaction Risk and Routing

<samp>from datetime import datetime, timezone<br><br>def evaluate_transaction(record):<br>&nbsp;&nbsp;&nbsp;&nbsp;risk_score = 0<br>&nbsp;&nbsp;&nbsp;&nbsp;reasons = []<br><br>&nbsp;&nbsp;&nbsp;&nbsp;if not record.get("owner"):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;risk_score += 25<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reasons.append("Missing accountable owner")<br><br>&nbsp;&nbsp;&nbsp;&nbsp;if record.get("days_to_sla", 999) &lt;= 3:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;risk_score += 30<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reasons.append("SLA due within three days")<br><br>&nbsp;&nbsp;&nbsp;&nbsp;if record.get("approval_state") == "Pending" and record.get("days_in_state", 0) &gt; 5:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;risk_score += 20<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reasons.append("Approval aging threshold exceeded")<br><br>&nbsp;&nbsp;&nbsp;&nbsp;if record.get("data_quality_exception"):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;risk_score += 25<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reasons.append("Data quality exception")<br><br>&nbsp;&nbsp;&nbsp;&nbsp;route = "Escalation Queue" if risk_score &gt;= 50 else "Standard Queue"<br><br>&nbsp;&nbsp;&nbsp;&nbsp;return {<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"transaction_id": record["transaction_id"],<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"risk_score": risk_score,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"route": route,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"reasons": reasons,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"evaluated_at": datetime.now(timezone.utc).isoformat()<br>&nbsp;&nbsp;&nbsp;&nbsp;}</samp>

## SQL | Operating Exception Queue

<samp>SELECT<br>&nbsp;&nbsp;&nbsp;&nbsp;t.TransactionID,<br>&nbsp;&nbsp;&nbsp;&nbsp;t.ProgramID,<br>&nbsp;&nbsp;&nbsp;&nbsp;t.OwnerID,<br>&nbsp;&nbsp;&nbsp;&nbsp;t.Status,<br>&nbsp;&nbsp;&nbsp;&nbsp;t.Priority,<br>&nbsp;&nbsp;&nbsp;&nbsp;t.SLADueDate,<br>&nbsp;&nbsp;&nbsp;&nbsp;DATEDIFF(day, GETUTCDATE(), t.SLADueDate) AS DaysToSLA,<br>&nbsp;&nbsp;&nbsp;&nbsp;CASE<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHEN t.OwnerID IS NULL THEN 'MISSING OWNER'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHEN t.SLADueDate &lt; GETUTCDATE() THEN 'OVERDUE'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WHEN DATEDIFF(day, GETUTCDATE(), t.SLADueDate) &lt;= 3 THEN 'SLA RISK'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE 'MONITOR'<br>&nbsp;&nbsp;&nbsp;&nbsp;END AS ExceptionState<br>FROM Transactions t<br>WHERE t.Status NOT IN ('Closed','Cancelled','Rejected');</samp>

## Power Fx | Customer Intake Submission

<samp>Set(varAction, "Submit");<br>If(<br>&nbsp;&nbsp;&nbsp;&nbsp;IsBlank(Trim(txtRequestTitle.Text)),<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Request title is required.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;IsBlank(cmbProgram.Selected.ProgramID),<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Select a program.", NotificationType.Error),<br>&nbsp;&nbsp;&nbsp;&nbsp;Set(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;varRecord,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Patch(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transactions,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Defaults(Transactions),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{Title: Trim(txtRequestTitle.Text), ProgramID: cmbProgram.Selected.ProgramID, Status: {Value: "Submitted"}, SubmittedBy: Lower(User().Email), SubmittedOn: Now()}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;);<br>&nbsp;&nbsp;&nbsp;&nbsp;Notify("Request submitted.", NotificationType.Success)<br>)</samp>

## DAX | Customer Operating Measures

<samp>Open Work =<br>CALCULATE(<br>&nbsp;&nbsp;&nbsp;&nbsp;COUNTROWS(Transactions),<br>&nbsp;&nbsp;&nbsp;&nbsp;NOT(Transactions[Status] IN {"Closed", "Cancelled", "Rejected"})<br>)</samp>

<samp>SLA Exposure =<br>CALCULATE(<br>&nbsp;&nbsp;&nbsp;&nbsp;COUNTROWS(Transactions),<br>&nbsp;&nbsp;&nbsp;&nbsp;Transactions[SLADueDate] &gt;= NOW(),<br>&nbsp;&nbsp;&nbsp;&nbsp;Transactions[SLADueDate] &lt;= NOW() + 3,<br>&nbsp;&nbsp;&nbsp;&nbsp;NOT(Transactions[Status] IN {"Closed", "Cancelled", "Rejected"})<br>)</samp>

<samp>Automation Rate =<br>DIVIDE(<br>&nbsp;&nbsp;&nbsp;&nbsp;CALCULATE(COUNTROWS(Transactions), Transactions[ProcessingMode] = "Automated"),<br>&nbsp;&nbsp;&nbsp;&nbsp;CALCULATE(COUNTROWS(Transactions), Transactions[AutomationEligible] = TRUE()),<br>&nbsp;&nbsp;&nbsp;&nbsp;0<br>)</samp>

<samp>Projected Backlog =<br>[Open Work] + [Forecast Intake Next 30 Days] - [Forecast Closures Next 30 Days]</samp>

## Automation | Event Sequence

<samp>Trigger: transaction created or materially modified<br>01 Validate required data and governed identifiers<br>02 Resolve identity, role, and permitted scope<br>03 Calculate SLA and transaction risk<br>04 Assign owner from routing matrix<br>05 Create audit-history event<br>06 Send approval when approval state is required<br>07 Escalate records crossing risk threshold<br>08 Refresh operational semantic model<br>09 Surface 30/60/90-day exposure<br>10 Preserve transaction, evidence, decision, and timestamp for auditability</samp>
