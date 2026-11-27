# Technical delivery — executive steering package

**Independent planning exercise.** All financial inputs, targets, roles and decisions are fictional assumptions, not actual employer outcomes.

## Decision request
Authorize a time-boxed pilot, not production rollout. Sponsor must validate the baseline, costs and acceptance criteria before committing funds.

## Options and investment
| Option | Annual cost assumption | Annual gross benefit assumption | Net benefit | Decision |
|---|---:|---:|---:|---|
| Maintain baseline | $0 incremental | $0 incremental | $0 | Comparator |
| Pilot at 50% modeled scope | $100000 | $130000 | $30000 | Conditional |
| Full modeled scope | $200000 | $260000 | $60000 | Defer pending evidence |

Full-scope simple ROI: 30.0%. At 50% benefit realization with full cost, net benefit is $-70000. These are illustrative linear assumptions, not a discounted cash-flow forecast.

## RACI
| Activity | Sponsor | Program lead | Finance | Independent reviewer | Operations |
|---|---|---|---|---|---|
| Approve scope and funding | A | R | C | C | I |
| Build and configure | I | A/R | I | C | C |
| Validate acceptance | I | R | C | A | C |
| Validate benefits | I | C | A/R | C | I |
| Authorize rollout | A | R | C | C | C |
| Operate and monitor | I | C | I | C | A/R |

## Integrated schedule
| ID | Work | Days | Predecessor | Exit evidence |
|---|---|---:|---|---|
| 1 | Baseline and scope | 5 | — | Approved baseline |
| 2 | Design and controls | 5 | 1 | Architecture decision |
| 3 | Implementation | 10 | 2 | Working pilot |
| 4 | Acceptance and readiness | 5 | 3 | Test evidence |
| 5 | Steering decision | 5 | 4 | Signed decision |

## Risk register and controls
| Risk | Likelihood / impact assumption | Owner | Trigger | Response |
|---|---|---|---|---|
| Dependency slip | Medium / High | Program lead | Acceptance threshold missed | Rebaseline |
| Benefits shortfall | Medium / High | Finance | Realized benefit below baseline plan | Reforecast and stop expansion |
| Operational readiness gap | Medium / High | Operations | Runbook or support missing | Hold production launch |

## Benefits and governance
Metric: Schedule. Target: Critical path baseline approved. Baseline: not measured; establish in week 1. Evidence owner: Program lead. Weekly pilot review; monthly sponsor review after launch. Finance signs off on actual benefits. No target is represented as achieved.

## Architecture decision record
Choose a local reference implementation for reproducible demonstration rather than claiming vendor deployment. Tradeoff: limited production fidelity; require authenticated integration, security assessment, resilience and load testing before rollout.

## Communications and readiness
Weekly delivery report to sponsor; fortnightly stakeholder demonstration; monthly investment review. Operations must approve support ownership, rollback, monitoring, incident response and access controls. Post-pilot review compares actual results against baseline and records lessons, exceptions and next decision.

## Steering meeting agenda
1. Baseline and strategic objective. 2. Demo and acceptance evidence. 3. Financial sensitivity. 4. Risks and dependencies. 5. Funding decision and accountable actions.

[Technical walkthrough](README.md)
