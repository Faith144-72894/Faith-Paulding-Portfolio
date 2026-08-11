# Federal Financial Management Analytics | Financial Systems & Decision Support Portfolio

## Role Alignment
Financial Management Business Analyst • Financial Systems Analyst • Financial Data / BI Analyst • Financial Management Modernization Consultant • Business Financial Manager • Resource Management Analyst • Program Financial Analyst • Financial Reporting Analyst

## Common Government Problem
Budget authority, commitments, obligations, expenditures, forecasts, requirements, and program status may be maintained in separate systems and spreadsheets. Financial and program teams reconcile the same information repeatedly before leadership can evaluate execution or projected funding pressure.

## Fragmented State → Modernized State

```text
Budget File ─┐
Commitment ──┤
Obligation ──┤                    ┌→ Execution Rate
Expenditure ─┼→ Governed Model ──┼→ Forecast Variance
Forecast ────┤                    ├→ Funding Gap
Requirements ┤                    ├→ Threshold Exception
Program Data ┘                    └→ Owner / Decision
```

## Portfolio Data
[Full FY2026 fictional financial execution dataset](financial_execution_sample.csv)

The dataset includes program, appropriation, budget authority, commitments, obligations, expenditures, forecast-at-completion, validated requirements, ownership, and execution status. It is intentionally structured so the same data can support financial analysis, program analysis, PPBE/resource analysis, BI development, systems analysis, and modernization design.

## Data → Decision Translation
[See the complete field-to-calculation-to-role breakout](DATA-TO-DECISION.md).

Example: `PRG-003` contains $6.4M in fictional budget authority and $4.3M in obligations, producing a 67.2% execution rate. Its $6.7M forecast-at-completion creates $0.3M in projected pressure, while its $6.9M validated requirement creates a $0.5M requirement-to-authority gap. One governed row therefore supports execution monitoring, forecast analysis, resource analysis, and exception management.

## Plan
1. Standardize Program, Fiscal Year, Funding, Transaction, Forecast, Requirement, Milestone, Risk, and Owner keys.
2. Validate incoming records before they enter the reporting model.
3. Relate financial execution to program and requirement data.
4. Calculate execution, balance, forecast, and funding-gap measures.
5. Apply threshold rules to identify exceptions.
6. Route exceptions to accountable owners.
7. Publish current and projected conditions to leadership reporting.

## Execution
Power Query/SQL → validation → governed financial model → DAX measures → threshold logic → Power BI decision view → owner action.

## Code / Calculations / Projections
[Real-time DAX, projection logic, and automation example](REAL-TIME-SOLUTION.md)

Core measures demonstrated:
- Execution Rate
- Unobligated Balance
- Forecast Variance
- Funding Risk
- Projected Year-End Obligations
- Projected Unobligated Balance

## Result Measures
Refresh success • data-quality exceptions • execution rate • unobligated balance • forecast variance • requirement gap • time to identify variance • unresolved exceptions • 30/60/90-day funding exposure

## What This Demonstrates to a Hiring Manager
| Target Role | Evidence in This Folder |
|---|---|
| Financial Management Business Analyst | Requirements, source mapping, calculations, decision rules |
| Financial Systems Analyst | Source integration, data structure, validation, governed model |
| Financial Data / BI Analyst | Dataset, DAX, variance analysis, projections, reporting |
| Business Financial Manager | Execution, forecast, requirement/funding position |
| Resource Management / PPBE Analyst | Validated requirement, funding gap, resource decision support |
| Financial Modernization Consultant | Fragmented-to-modernized operating model |
| Program Financial Analyst | Program-level execution, forecast, exception analysis |

## Portfolio Files
- [financial_execution_sample.csv](financial_execution_sample.csv) — full fictional working dataset
- [DATA-TO-DECISION.md](DATA-TO-DECISION.md) — how fields translate to calculations, decisions, and roles
- [REAL-TIME-SOLUTION.md](REAL-TIME-SOLUTION.md) — DAX, projections, automation, and controls

> All programs and financial values are fictional portfolio data. They do not represent an actual agency, appropriation, program, or government financial record.
