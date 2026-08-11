# PPBE & Resource Analytics Code Page

Pairs with REAL-TIME-SOLUTION.md. The logic below connects requirements, resources, execution, schedule, and projected program position.

## Core Measures
| Purpose | Formula / Logic |
|---|---|
| Validated Requirement | SUM Requirements[ValidatedAmount] |
| Approved Funding | SUM Funding[ApprovedAmount] |
| Obligations | SUM Execution[Obligations] |
| Funding Gap | [Validated Requirement] - [Approved Funding] |
| Execution Rate | DIVIDE([Obligations], [Approved Funding], 0) |
| Unfunded Requirement | MAX(0, [Validated Requirement] - [Approved Funding]) |
| Remaining Funding | [Approved Funding] - [Obligations] |

## Projection Logic
| Projection | Formula / Logic |
|---|---|
| Monthly Run Rate | DIVIDE([Obligations], [Fiscal Months Elapsed], 0) |
| Projected Year-End Execution | [Monthly Run Rate] * 12 |
| Projected Funding Position | [Approved Funding] - [Projected Year-End Execution] |
| 30-Day Requirement Exposure | Sum unfunded requirements with required date <= today + 30 |
| 60-Day Requirement Exposure | Sum unfunded requirements with required date <= today + 60 |
| 90-Day Requirement Exposure | Sum unfunded requirements with required date <= today + 90 |

## Decision Rules
| Condition | Decision Signal |
|---|---|
| Projected Funding Position < 0 | Projected shortfall |
| Required milestone <= 60 days and funding unavailable | Execution dependency |
| Unfunded Requirement > 0 and mission priority = Critical | Leadership decision required |
| Execution materially below planned curve | Execution review |

## SQL / Relationship Logic
| Relationship | Implementation Pattern |
|---|---|
| Requirement to Program | Requirements.ProgramID = Programs.ProgramID |
| Funding to Requirement | Funding.RequirementID = Requirements.RequirementID |
| Milestone to Program | Milestones.ProgramID = Programs.ProgramID |
| Risk to Requirement | Risks.RequirementID = Requirements.RequirementID |
| Decision package | Join requirement + funding + milestone + risk + owner by governed keys |

## Automation
1. Import approved requirement and execution updates.
2. Validate program and requirement keys.
3. Calculate funding gap and execution rate.
4. Recalculate 30/60/90 exposure.
5. Detect milestone/resource dependencies.
6. Assign decision owner.
7. Publish exception to leadership view.

## Role Evidence
PPBE Analyst • Business Financial Manager • Resource Management Analyst • PPBE Data Analyst • Budget/Program Analytics Consultant
