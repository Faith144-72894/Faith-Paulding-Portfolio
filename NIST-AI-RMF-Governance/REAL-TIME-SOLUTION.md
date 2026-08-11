# Continuous AI Risk Monitoring

## Role Alignment
AI Governance Lead • Responsible AI Lead • AI Risk Consultant • Cybersecurity Governance Analyst • Cyber Risk & Controls Analyst

## Common Government Problem
Governance is often performed at approval points while the operating risk changes after deployment: data changes, user behavior changes, model behavior changes, and new exceptions appear.

## Modernization Pattern
**Fragmented / Point-in-Time** → approval document + separate risk register + manual reassessment

**Modernized** → AI inventory + control mapping + continuous metrics + threshold alerts + evidence + reassessment workflow

## Risk Calculation
```python
def ai_risk_score(impact, likelihood, control_effectiveness):
    inherent = impact * likelihood
    residual = inherent * (1 - control_effectiveness)
    return round(residual, 2)

risk = ai_risk_score(impact=5, likelihood=4, control_effectiveness=0.70)
```

## Threshold Logic
```text
Residual risk >= 8  -> Critical review
Residual risk >= 4  -> Mitigation required
Residual risk < 4   -> Monitor

Grounding rate < 90% -> evaluation trigger
Access exception > threshold -> security review
Material model/data change -> reassessment
```

## Projection
Rolling 30/60/90-day risk trends identify increasing exception rates before they become control failures.

## Capability Demonstrated
NIST AI RMF concepts • risk scoring • controls • continuous monitoring • governance workflow • evidence • escalation • cybersecurity-aware AI delivery
