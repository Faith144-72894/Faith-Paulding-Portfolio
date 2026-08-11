SELECT
    r.RequestID,
    r.RequestType,
    r.Status,
    r.Priority,
    r.SubmittedOn,
    r.ECD,
    DATEDIFF(day, r.SubmittedOn, COALESCE(r.CompletedOn, GETDATE())) AS CycleDays,
    CASE WHEN r.ECD < CAST(GETDATE() AS date) AND r.Status NOT IN ('Complete','Closed') THEN 1 ELSE 0 END AS IsOverdue,
    a.LastAction,
    a.LastActionOn
FROM Request r
OUTER APPLY (
    SELECT TOP 1 h.Action AS LastAction, h.ActionOn AS LastActionOn
    FROM StatusHistory h
    WHERE h.RequestID=r.RequestID
    ORDER BY h.ActionOn DESC
) a;
