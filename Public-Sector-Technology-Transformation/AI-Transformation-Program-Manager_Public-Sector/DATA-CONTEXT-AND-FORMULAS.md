# Data Context, Formulas & Code | AI Transformation Program Manager

## Data Story
The portfolio dataset represents AI use cases from idea through production. Each record captures business value, sponsor, data readiness, feasibility, risk, expected savings, evaluation results, human-review requirements, cost, adoption, and production status.

## Formulas
Priority Score = Value×30% + Data Readiness×20% + Feasibility×20% + Inverse Risk×15% + Adoption Readiness×15%

Realized Value % = Realized Benefit / Projected Benefit

Automation Yield = Transactions completed without human intervention / Eligible transactions

Human Review Rate = Reviewed transactions / AI transactions

Cost per Successful Transaction = AI operating cost / accepted AI transactions

## Python
    def priority(value,data,feasibility,risk,adoption):
        return round(value*.30 + data*.20 + feasibility*.20 + (5-risk)*.15 + adoption*.15,2)

## SQL
    SELECT UseCaseName, ProjectedHoursSaved, RealizedHoursSaved,
           RealizedHoursSaved*1.0/NULLIF(ProjectedHoursSaved,0) AS RealizationRate
    FROM AIUseCases
    WHERE ProductionStatus='Live';

## Context
I would use this data to prevent the AI portfolio from being driven by the most impressive demo. A use case advances because its data, controls, owner, evaluation, adoption path, and measurable value support production.

## Decisions Supported
Advance pilot • hold for data readiness • require additional control • terminate low-value pilot • scale production use case • change human-review threshold.
