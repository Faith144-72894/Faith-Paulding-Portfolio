# Financial Data → Calculation → Decision → Role Translation

## Sample Data
[financial_execution_sample.csv](financial_execution_sample.csv) contains fictional FY2026 program-level budget authority, commitments, obligations, expenditures, forecast-at-completion, validated requirements, ownership, and execution status.

## How the Data Translates

| Source Field | Calculation / Control | Decision Use | Role Capability |
|---|---|---|---|
| BudgetAuthority + Obligations | Execution Rate = Obligations / Budget Authority | Identify under/over execution | Financial Data Analyst; BFM; Resource Analyst |
| BudgetAuthority + ForecastAtCompletion | Forecast Variance = FAC - Budget Authority | Identify projected funding pressure | Program Financial Analyst; Financial Systems Analyst |
| ValidatedRequirement + BudgetAuthority | Funding Gap = Requirement - Authority | Quantify unfunded requirement | PPBE Analyst; Resource Management Analyst |
| Commitments + Obligations | Commitment-to-obligation conversion | Identify funds not progressing to obligation | Financial Management Analyst |
| Obligations + Expenditures | Disbursement/expense relationship | Identify execution lag | Financial Reporting Analyst |
| ProgramOwner + threshold result | Exception ownership | Route decision/action | Financial Modernization Consultant; Program Manager |

## Example Calculations

Using `PRG-003`:

- Budget Authority = $6.4M
- Obligations = $4.3M
- Execution Rate = 4.3 / 6.4 = **67.2%**
- Forecast at Completion = $6.7M
- Forecast Variance = 6.7 - 6.4 = **+$0.3M projected pressure**
- Validated Requirement = $6.9M
- Funding Gap = 6.9 - 6.4 = **$0.5M**

The same row supports three different decisions: current execution, projected year-end position, and requirement-to-resource gap.

## Modernization Translation

```text
BEFORE
Budget spreadsheet
+ commitment report
+ obligation report
+ expenditure report
+ program tracker
+ forecast workbook
= manual reconciliation

AFTER
Governed financial dataset
→ validated program/fiscal keys
→ calculated execution measures
→ forecast/projection logic
→ exception thresholds
→ owner assignment
→ executive decision view
```

## Portfolio Evidence
- [Real-time calculations and projection logic](REAL-TIME-SOLUTION.md)
- [Sample financial execution dataset](financial_execution_sample.csv)
- README describes the challenge, plan, execution, and role alignment.

## Data Disclaimer
All programs and values are fictional and exist solely to demonstrate financial-management analytics capability.
