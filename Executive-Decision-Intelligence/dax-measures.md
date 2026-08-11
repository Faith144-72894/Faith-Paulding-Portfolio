# Executive Decision Intelligence | DAX Measures

This capability translates operational records into leadership-level performance, risk, workload, SLA, forecast, and decision measures. Power BI and DAX are the implementation tools; executive decision intelligence is the business capability.

## Audit & Corrective Action Measures

Total Deficiencies = DISTINCTCOUNT(Deficiencies[Deficiency ID])

Open Deficiencies = CALCULATE([Total Deficiencies], Deficiencies[Status] <> "Closed")

Closed Deficiencies = CALCULATE([Total Deficiencies], Deficiencies[Status] = "Closed")

Deficiency Closure Rate = DIVIDE([Closed Deficiencies], [Total Deficiencies], 0)

Overdue Deficiencies = CALCULATE([Total Deficiencies], Deficiencies[ECD] < TODAY(), Deficiencies[Status] <> "Closed")

High-Severity Open Deficiencies = CALCULATE([Total Deficiencies], Deficiencies[Severity] IN {"High", "Critical"}, Deficiencies[Status] <> "Closed")

Average Days Open = AVERAGEX(FILTER(Deficiencies, Deficiencies[Status] <> "Closed"), DATEDIFF(Deficiencies[Created Date], TODAY(), DAY))

Total Recommendations = DISTINCTCOUNT(Recommendations[Recommendation ID])

Open Recommendations = CALCULATE([Total Recommendations], Recommendations[Status] <> "Closed")

Overdue Recommendations = CALCULATE([Total Recommendations], Recommendations[ECD] < TODAY(), Recommendations[Status] <> "Closed")

Total Corrective Actions = DISTINCTCOUNT(CorrectiveActions[Action ID])

Completed Corrective Actions = CALCULATE([Total Corrective Actions], CorrectiveActions[Status] = "Completed")

Corrective-Action Completion Rate = DIVIDE([Completed Corrective Actions], [Total Corrective Actions], 0)

Overdue Corrective Actions = CALCULATE([Total Corrective Actions], CorrectiveActions[Current Due Date] < TODAY(), CorrectiveActions[Status] <> "Completed")

Total Milestones = DISTINCTCOUNT(Milestones[Milestone ID])

Milestone Completion Rate = DIVIDE(CALCULATE([Total Milestones], Milestones[Status] = "Completed"), [Total Milestones], 0)

Overdue Milestones = CALCULATE([Total Milestones], Milestones[Current Due Date] < TODAY(), Milestones[Status] <> "Completed")

Upcoming 30-Day Deadlines = CALCULATE([Total Deficiencies], Deficiencies[ECD] >= TODAY(), Deficiencies[ECD] <= TODAY() + 30, Deficiencies[Status] <> "Closed")

Upcoming 60-Day Deadlines = CALCULATE([Total Deficiencies], Deficiencies[ECD] > TODAY() + 30, Deficiencies[ECD] <= TODAY() + 60, Deficiencies[Status] <> "Closed")

Upcoming 90-Day Deadlines = CALCULATE([Total Deficiencies], Deficiencies[ECD] > TODAY() + 60, Deficiencies[ECD] <= TODAY() + 90, Deficiencies[Status] <> "Closed")

## Service Delivery & SLA Measures

Total Requests = DISTINCTCOUNT(ServiceRequests[Request ID])

Open Requests = CALCULATE([Total Requests], NOT(ServiceRequests[Current Status] IN {"Completed", "Closed", "Rejected", "Cancelled"}))

Completed Requests = CALCULATE([Total Requests], ServiceRequests[Current Status] IN {"Completed", "Closed"})

Request Completion Rate = DIVIDE([Completed Requests], [Total Requests], 0)

Critical Open Requests = CALCULATE([Total Requests], ServiceRequests[Priority] = "Critical", NOT(ServiceRequests[Current Status] IN {"Completed", "Closed", "Rejected", "Cancelled"}))

Overdue Requests = CALCULATE([Total Requests], ServiceRequests[SLA Due Date] < NOW(), NOT(ServiceRequests[Current Status] IN {"Completed", "Closed", "Rejected", "Cancelled"}))

Requests Completed Within SLA = CALCULATE([Total Requests], FILTER(ServiceRequests, NOT ISBLANK(ServiceRequests[Completed Date]) && ServiceRequests[Completed Date] <= ServiceRequests[SLA Due Date]))

Completed Requests With SLA = CALCULATE([Total Requests], FILTER(ServiceRequests, NOT ISBLANK(ServiceRequests[Completed Date]) && NOT ISBLANK(ServiceRequests[SLA Due Date])))

SLA Compliance Rate = DIVIDE([Requests Completed Within SLA], [Completed Requests With SLA], 0)

Average Resolution Hours = AVERAGEX(FILTER(ServiceRequests, NOT ISBLANK(ServiceRequests[Completed Date])), DATEDIFF(ServiceRequests[Submitted Date], ServiceRequests[Completed Date], HOUR))

SLA Due Within 24 Hours = CALCULATE([Total Requests], ServiceRequests[SLA Due Date] >= NOW(), ServiceRequests[SLA Due Date] <= NOW() + 1, NOT(ServiceRequests[Current Status] IN {"Completed", "Closed", "Rejected", "Cancelled"}))

SLA Due Within Three Days = CALCULATE([Total Requests], ServiceRequests[SLA Due Date] > NOW() + 1, ServiceRequests[SLA Due Date] <= NOW() + 3, NOT(ServiceRequests[Current Status] IN {"Completed", "Closed", "Rejected", "Cancelled"}))

Unassigned Requests = CALCULATE([Total Requests], ISBLANK(ServiceRequests[Assigned User ID]), ServiceRequests[Current Status] <> "Draft", NOT(ServiceRequests[Current Status] IN {"Completed", "Closed", "Rejected", "Cancelled"}))

## Approval & Workflow Measures

Total Approval Decisions = DISTINCTCOUNT(ApprovalDecisions[Decision ID])

Pending Approvals = CALCULATE([Total Approval Decisions], ApprovalDecisions[Decision] = "Pending")

Approved Decisions = CALCULATE([Total Approval Decisions], ApprovalDecisions[Decision] = "Approved")

Returned Decisions = CALCULATE([Total Approval Decisions], ApprovalDecisions[Decision] = "Returned")

Approval Rate = DIVIDE([Approved Decisions], CALCULATE([Total Approval Decisions], ApprovalDecisions[Decision] IN {"Approved", "Rejected", "Returned"}), 0)

Average Approval Hours = AVERAGEX(FILTER(ApprovalDecisions, NOT ISBLANK(ApprovalDecisions[Decision Date])), DATEDIFF(RELATED(ServiceRequests[Submitted Date]), ApprovalDecisions[Decision Date], HOUR))

Overdue Approval Decisions = CALCULATE([Total Approval Decisions], ApprovalDecisions[Decision] = "Pending", ApprovalDecisions[Due Date] < NOW())

## Decision Use

These measures support executive views for portfolio health, overdue exposure, corrective-action progress, workload, SLA performance, approval bottlenecks, data quality, and 30/60/90-day decision windows.

Role alignment: Executive Decision Support Analyst • BI/Data Analytics Lead • Senior BI Developer • Power BI Lead • Performance Management Analyst • Technical Program Manager
