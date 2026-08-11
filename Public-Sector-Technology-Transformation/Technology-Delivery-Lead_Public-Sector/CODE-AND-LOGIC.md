# Code & Logic

## SQL | Blocker Aging

    SELECT IssueID, Impact, Owner, OpenedDate,
           DATEDIFF(day, OpenedDate, GETDATE()) AS AgeDays,
           RecoveryAction
    FROM RAID
    WHERE Status <> 'Closed'
    ORDER BY CASE Impact WHEN 'Critical' THEN 1 WHEN 'High' THEN 2 ELSE 3 END, AgeDays DESC;

## Python | Escalation

    def escalation(impact, age):
        thresholds = {"Critical":0, "High":2, "Medium":5, "Low":10}
        return age >= thresholds[impact]

    print(escalation("High", 3))
