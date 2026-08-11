# Financial Management Code & Calculation Page

This page pairs directly with REAL-TIME-SOLUTION.md and shows the implementation logic behind the financial-management case without fenced code blocks.

## DAX Measure Logic
| Purpose | Formula / Logic |
|---|---|
| Total Budget Authority | SUM FinancialExecution[BudgetAuthority] |
| Total Commitments | SUM FinancialExecution[Commitments] |
| Total Obligations | SUM FinancialExecution[Obligations] |
| Total Expenditures | SUM FinancialExecution[Expenditures] |
| Execution Rate | DIVIDE([Total Obligations], [Total Budget Authority], 0) |
| Unobligated Balance | [Total Budget Authority] - [Total Obligations] |
| Unexpended Obligations | [Total Obligations] - [Total Expenditures] |
| Forecast Variance | [Forecast at Completion] - [Total Budget Authority] |
| Requirement Gap | [Validated Requirement] - [Total Budget Authority] |
| Commitment Conversion Rate | DIVIDE([Total Obligations], [Total Commitments], 0) |

## Forecast Logic
| Projection | Formula / Logic |
|---|---|
| Fiscal Months Elapsed | MAX Calendar[FiscalMonthNumber] |
| Average Monthly Obligation | DIVIDE([Total Obligations], [Fiscal Months Elapsed], 0) |
| Projected Year-End Obligations | [Average Monthly Obligation] * 12 |
| Projected Unobligated Balance | [Total Budget Authority] - [Projected Year-End Obligations] |
| Projected Requirement Variance | [Projected Year-End Obligations] - [Validated Requirement] |

## Risk Classification
| Condition | Result |
|---|---|
| Forecast Variance > 0 | RED |
| Execution Rate < 70% after defined fiscal threshold | AMBER |
| Requirement Gap > 0 and milestone due within 60 days | AMBER |
| No active threshold | GREEN |

## Power Query / Data Quality Logic
| Validation | Logic |
|---|---|
| Missing Program ID | Flag record when ProgramID is null or blank |
| Invalid Fiscal Year | Reject values outside approved fiscal-year list |
| Duplicate Program/FY/Appropriation | Group by ProgramID + FiscalYear + Appropriation and flag count > 1 |
| Negative Financial Amount | Flag amount fields below zero unless approved adjustment type |
| Forecast Missing | Flag active program when ForecastAtCompletion is null |

## SQL Pattern
| Need | SQL Logic |
|---|---|
| Program-level execution | SELECT ProgramID, SUM(BudgetAuthority), SUM(Obligations), SUM(Expenditures) GROUP BY ProgramID |
| High-risk variance | WHERE ForecastAtCompletion > BudgetAuthority |
| Current FY filter | WHERE FiscalYear = current approved fiscal year |
| Owner exception queue | JOIN ProgramOwner to exception records where threshold status <> GREEN |

## Automation Logic
1. Source refresh completes.
2. Validate ProgramID, FiscalYear, appropriation, and required financial amounts.
3. Reject or quarantine failed records.
4. Recalculate execution and forecast measures.
5. Evaluate Red/Amber/Green thresholds.
6. Write exception record with ProgramID, owner, reason, amount, timestamp, and status.
7. Notify accountable owner.
8. Refresh executive reporting.
9. Close exception only after explanation or corrective action is recorded.

## Example Using PRG-003
| Measure | Calculation | Result |
|---|---:|---:|
| Execution Rate | 4.3M ÷ 6.4M | 67.2% |
| Forecast Variance | 6.7M - 6.4M | +0.3M |
| Requirement Gap | 6.9M - 6.4M | 0.5M |
| Current Risk | Forecast above authority + execution below threshold | RED / AMBER review condition |

## Role Evidence
Financial Systems Analyst • Financial Data/BI Analyst • Business Financial Manager • Program Financial Analyst • Resource Management Analyst • Financial Management Modernization Consultant
