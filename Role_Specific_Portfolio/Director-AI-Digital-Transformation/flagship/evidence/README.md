# Transformation investment: technical walkthrough and executive evidence

Independent synthetic case study, not employer work or a measured business outcome.

## Click-by-click local application
1. Clone the repository and run `python service.py` from the root.
2. Open http://127.0.0.1:8765/service-index.html; select **Transformation investment** (or open http://127.0.0.1:8765/service-demos/Director-AI-Digital-Transformation.html directly).
3. In Scenario configuration, enter 2000 hours / $60 / 0.8 adoption / $40,000 cost. See callout 1.
4. Select **Run analysis** (callout 2).
5. Read Decision scorecard (callout 3). Expected: $96,000 benefit; 140% ROI.
6. Expand Raw service response to inspect the JSON (callout 4).
7. Set adoption to 0, then Run analysis again. Expected: Negative ROI.
8. Inspect local SQLite runs table to confirm successful requests were saved. Do not use confidential data.

![Annotated local interface reconstruction](screen.svg)

Actual screenshot capture is configured in browser CI, not yet verified. This drawing is an original reconstruction of the local application, not a vendor screenshot.

## Executive leadership case
| Decision element | Proposed evidence |
|---|---|
| Accountable forum | Investment committee |
| Decision | Fund conditional pilot; validate adoption before scaling |
| Acceptance metric | Break-even adoption 33.3% |
| Risk and response | Benefit overstatement; finance validation |
| Evidence | Expected synthetic result: $96,000 benefit; 140% ROI |

### Governance and delivery
Sponsor owns funding and acceptance; technical lead owns implementation; independent reviewer validates test evidence; operations lead owns support. Proposed 30-day pilot: week 1 baseline and scope; week 2 build; week 3 acceptance and risk review; week 4 sponsor decision. No actual sponsor decision, funding, or realized outcome is claimed. Production authorization requires security, integration and operational readiness evidence.
