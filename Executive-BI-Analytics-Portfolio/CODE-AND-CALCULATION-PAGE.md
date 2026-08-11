# Executive Analytics Code & Measure Page

Pairs with REAL-TIME-SOLUTION.md and shows the analytical logic behind the executive performance model.

## DAX Measures
| Purpose | Formula / Logic |
|---|---|
| Total Items | COUNTROWS(FactPerformance) |
| Open Items | Count rows where Status <> Closed |
| Completed Items | Count rows where Status = Closed |
| Completion Rate | DIVIDE([Completed Items], [Total Items], 0) |
| Overdue Items | Count open rows where DueDate < TODAY() |
| Average Aging Days | Average DATEDIFF(CreatedDate, TODAY(), DAY) for open items |
| Critical Issues | Count open issues where Severity = Critical |
| Corrective Action Completion | Completed Corrective Actions ÷ Total Corrective Actions |

## Forecast Measures
| Purpose | Formula / Logic |
|---|---|
| Projected 30-Day Closures | Open records with ForecastCloseDate <= TODAY() + 30 |
| Expected New Items | Rolling historical intake average projected into next period |
| Projected Backlog | [Open Items] + [Expected New Items] - [Projected 30-Day Closures] |
| 30/60/90 Exposure | Count open items by forecast/due-date window |

## Data Quality Logic
| Test | Rule |
|---|---|
| Missing Owner | Active item has no accountable owner |
| Missing Due Date | Open action requiring deadline has no due date |
| Invalid Status | Status not in governed status dimension |
| Orphan Record | Fact key does not resolve to required dimension |
| Stale Update | LastUpdated exceeds approved reporting threshold |

## SQL Pattern
| Need | Logic |
|---|---|
| Open portfolio | WHERE Status <> 'Closed' |
| Overdue queue | WHERE DueDate < CURRENT_DATE AND Status <> 'Closed' |
| Owner summary | GROUP BY OwnerID with open, overdue, critical counts |
| Trend | GROUP BY reporting period and status/health |

## Refresh / Exception Flow
1. Load source records.
2. Apply data-quality checks.
3. Update dimensional relationships.
4. Calculate KPI layer.
5. Recalculate forecast measures.
6. Surface exceptions before summary totals.
7. Refresh executive view.
8. Preserve drill-through to source record and accountable owner.

## Role Evidence
BI/Data Analytics Lead • Senior BI Developer • Lead Data Analyst • Power BI Lead • Executive Decision Support Analyst • Performance Management Analyst
