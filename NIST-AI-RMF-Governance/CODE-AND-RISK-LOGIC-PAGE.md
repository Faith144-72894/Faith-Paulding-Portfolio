# AI Governance Risk Logic Page

Pairs with REAL-TIME-SOLUTION.md and translates AI governance into measurable logic, controls, thresholds, and reassessment actions.

## Risk Scoring
| Measure | Formula / Logic |
|---|---|
| Inherent Risk | Impact × Likelihood |
| Control Reduction | Inherent Risk × Control Effectiveness |
| Residual Risk | Inherent Risk × (1 - Control Effectiveness) |
| Example | Impact 5 × Likelihood 4 = 20; 70% effective controls → residual risk 6.0 |

## Risk Thresholds
| Residual Risk | Action |
|---|---|
| 8 or higher | Critical review |
| 4 to 7.99 | Mitigation required |
| Below 4 | Monitor |

## Continuous Control Logic
| Signal | Trigger |
|---|---|
| Grounding Rate | < 90% → evaluation |
| Access Exceptions | Above approved tolerance → security review |
| Safety Exceptions | Above approved tolerance → governance review |
| Model Version Change | Reassessment |
| Material Data Change | Reassessment |
| New Use Case | Map + Measure review before expansion |

## Python-Style Calculation Logic
| Function Element | Logic |
|---|---|
| Inputs | impact, likelihood, control_effectiveness |
| inherent | impact * likelihood |
| residual | inherent * (1 - control_effectiveness) |
| returned value | round residual risk to approved precision |

## 30/60/90 Trend Logic
| Window | Evaluation |
|---|---|
| 30 Day | New exceptions, mitigations opened/closed, immediate threshold changes |
| 60 Day | Direction of residual-risk and control-effectiveness trends |
| 90 Day | Persistent risk, recurring controls failures, reassessment requirement |

## Evidence Record
AI System ID • Use Case • Owner • Risk Category • Impact • Likelihood • Control • Control Effectiveness • Residual Risk • Evidence Link • Last Assessment • Next Review • Status

## Role Evidence
AI Governance Lead • Responsible AI Lead • AI Risk Consultant • Cybersecurity Governance Analyst • Cyber Risk & Controls Analyst
