# Public Sector Technology & Transformation

## Role Targets, Market Alignment & Portfolio Evidence

This section is built around roles inside technology companies, cloud/platform providers, consulting organizations, systems integrators, regulated enterprises, and organizations delivering technology to public-sector customers. The portfolio is structured so a hiring manager can move from the **role I am targeting** to the **operating challenge**, then directly into the **dataset, formula, code, architecture, controls, and decision logic** I would use to solve it.

The salary ranges below are **base-salary targeting ranges for U.S. senior-level opportunities**, not guarantees. Actual compensation varies by company, geography, level, clearance/customer requirements, equity, bonus, and scope. My target is to compete in the senior market where the role expects both technical depth and program/business ownership.

## Target Roles & Compensation Expectations

| Target Role | Target Base Salary | Market Positioning | Portfolio Evidence |
|---|---:|---|---|
| Senior Technical Program Manager — Public Sector | $165K–$200K+ | Senior technical delivery / cross-functional program leadership | [Role Case](Senior-Technical-Program-Manager_Public-Sector/) |
| Solutions Architect — Public Sector | $170K–$220K+ | Enterprise/cloud/platform architecture | [Role Case](Solutions-Architect_Public-Sector/) |
| Customer Solutions Manager — Public Sector | $155K–$190K+ | Customer transformation, adoption and value realization | [Role Case](Customer-Solutions-Manager_Public-Sector/) |
| Data & AI Lead — Public Sector | $175K–$225K+ | Data strategy, AI delivery and governed analytics | [Role Case](Data-AI-Lead_Public-Sector/) |
| Cloud Transformation Program Manager — Public Sector | $165K–$205K+ | Cloud migration and modernization program leadership | [Role Case](Cloud-Transformation-Program-Manager_Public-Sector/) |
| Technology Delivery Lead — Public Sector | $160K–$195K+ | Technical delivery, recovery and dependency leadership | [Role Case](Technology-Delivery-Lead_Public-Sector/) |
| BI & Decision Intelligence Lead — Public Sector | $160K–$200K+ | Enterprise analytics, semantic models and executive decision intelligence | [Role Case](BI-Decision-Intelligence-Lead_Public-Sector/) |
| AI Transformation Program Manager — Public Sector | $175K–$220K+ | AI portfolio, production readiness and value realization | [Role Case](AI-Transformation-Program-Manager_Public-Sector/) |
| Power Platform Solution Architect — Public Sector | $160K–$200K+ | Enterprise Power Platform architecture and workflow modernization | [Role Case](Power-Platform-Solution-Architect_Public-Sector/) |
| Financial Systems Modernization / Transformation Manager | $155K–$195K+ | Financial systems, analytics and modernization leadership | Portfolio expansion target |

**Compensation research:** These targets are intentionally presented as ranges rather than a single “market salary.” Current postings for senior technical program, solutions architecture, cloud/data/AI, and Power Platform architecture roles show wide ranges depending on employer and level. Use current postings and compensation databases when negotiating a specific opportunity. [AWS Careers](https://www.amazon.jobs/) • [Microsoft Careers](https://jobs.careers.microsoft.com/) • [Google Careers](https://www.google.com/about/careers/applications/jobs/results/) • [Levels.fyi](https://www.levels.fyi/) • [Glassdoor](https://www.glassdoor.com/Salaries/index.htm)

---

## How to Read the Data in This Portfolio

The sample CSV files are not decorative. Each dataset represents the operating information I would need in that role. The calculations are deliberately tied to the actual columns in those files.

**Dataset field → business rule → formula → code → threshold → decision → action.**

[Open the full Dataset → Formula → Decision Crosswalk](DATASET-FORMULA-CROSSWALK.md)

Examples:

- In the **Senior Technical Program Manager** dataset, `decision_due` feeds decision-aging logic, `uat_pass_rate` feeds release readiness, and `continuity_ready` becomes a go/no-go control.
- In the **Customer Solutions Manager** dataset, `active_users_30d / target_users` calculates adoption, while `legacy_transactions / total transactions` exposes whether teams are still relying on the old process.
- In the **Data & AI Lead** dataset, `actual_freshness_hours` is tested against `freshness_sla_hours`, while `quality_score` and `grounding_score` determine whether automated output can proceed or requires human review.
- In the **Cloud Transformation PM** dataset, readiness is not a date. `identity_ready`, `data_validated`, `integration_ready`, `rollback_ready`, and `support_ready` must pass before a workload becomes cutover-eligible.
- In the **AI Transformation PM** dataset, business value, data readiness, feasibility, inverse risk, and adoption readiness combine into a weighted priority score used to decide which AI use cases deserve investment.
- In the **Power Platform Architect** dataset, submission/review dates calculate cycle time, ECD drives risk, and duplicate flags expose intake/data-quality problems.

The crosswalk includes Excel-style formulas plus SQL, Python, DAX, or Power Fx patterns where the role and implementation layer call for them.

---

## 1. Senior Technical Program Manager — Public Sector

**Business condition:** A customer modernization program has multiple workstreams, vendors, technical dependencies, decision gates, security reviews, testing activities, and leadership commitments. Status exists, but no single view explains what is blocking delivery or what decision is required next.

**Dataset:** `data/delivery_control.csv` inside the role case.

**Fields driving decisions:** workstream • owner • planned finish • percent complete • health • dependency • decision due • UAT pass rate • continuity ready.

**What I calculate:** portfolio completion • overdue decision days • UAT readiness • continuity coverage • composite release readiness.

**What I decide from it:** escalate a decision • resequence a dependency • add testing capacity • hold release • maintain fallback • approve go-live.

[Open Role Case](Senior-Technical-Program-Manager_Public-Sector/)

---

## 2. Solutions Architect — Public Sector

**Business condition:** A customer has applications, spreadsheets, shared repositories, analytics, identity requirements, security controls, and new AI capabilities but no documented target architecture connecting them.

**Dataset:** `data/architecture_inventory.csv`.

**Fields driving decisions:** component • current state • target pattern • data owner • identity pattern • integration • criticality • estimated monthly cost • continuity method.

**What I calculate:** monthly architecture run rate • high-criticality share • continuity coverage • modernization coverage.

**What I decide from it:** target platform • integration pattern • resilience requirement • identity pattern • modernization sequence • cost tradeoff.

[Open Role Case](Solutions-Architect_Public-Sector/)

---

## 3. Customer Solutions Manager — Public Sector

**Business condition:** A solution has technically launched, but user adoption is uneven. Leadership sees implementation as complete while operational teams continue using spreadsheets and manual workarounds.

**Dataset:** `data/adoption_telemetry.csv`.

**Fields driving decisions:** target users • active users • transactions • legacy transactions • blockers • cycle time • hours saved.

**What I calculate:** adoption rate • legacy reliance • blocker density • monthly productivity benefit.

**What I decide from it:** where to intervene • which user group needs training • which blocker requires product escalation • whether legacy retirement is premature.

[Open Role Case](Customer-Solutions-Manager_Public-Sector/)

---

## 4. Data & AI Lead — Public Sector

**Business condition:** Operational data is distributed across systems with different refresh schedules, quality levels, owners, and permissions. AI use cases are being proposed on top of that environment.

**Dataset:** `data/data_product_registry.csv`.

**Fields driving decisions:** source • freshness SLA • actual freshness • quality score • AI use • grounding score • human-review rule.

**What I calculate:** freshness compliance • quality pass • grounding review trigger • trusted data-product rate.

**What I decide from it:** allow automated use • block stale data • correct quality defects • require human review • suspend an AI output path.

[Open Role Case](Data-AI-Lead_Public-Sector/)

---

## 5. Cloud Transformation Program Manager — Public Sector

**Business condition:** Workloads need to move from legacy or fragmented infrastructure while the organization must continue operating throughout migration.

**Dataset:** `data/migration_inventory.csv`.

**Fields driving decisions:** workload • criticality • wave • readiness • identity • data validation • integration • rollback • support • cutover window.

**What I calculate:** technical gate pass • cutover eligibility • wave readiness • critical blocked workloads.

**What I decide from it:** move • hold • split wave • resequence • remediate dependency • activate rollback.

[Open Role Case](Cloud-Transformation-Program-Manager_Public-Sector/)

---

## 6. Technology Delivery Lead — Public Sector

**Business condition:** Risks, assumptions, issues, dependencies, customer decisions, and technical recovery actions exist across different tools and meetings.

**Dataset:** `data/raid_register.csv`.

**Fields driving decisions:** type • impact • owner • opened date • due date • status • recovery action • affected process.

**What I calculate:** item age • days overdue • high-impact open blockers • recovery coverage • escalation trigger.

**What I decide from it:** escalate • assign recovery • change delivery sequence • invoke fallback • close or continue monitoring.

[Open Role Case](Technology-Delivery-Lead_Public-Sector/)

---

## 7. BI & Decision Intelligence Lead — Public Sector

**Business condition:** Leadership receives multiple reports with different definitions for performance, finance, risk, adoption, and delivery.

**Dataset:** `data/kpi_registry.csv`.

**Fields driving decisions:** KPI • definition • source • refresh SLA • actual age • threshold • current value • owner • decision trigger.

**What I calculate:** freshness variance • stale-KPI flag • threshold exception • action requirement.

**What I decide from it:** whether the metric is trustworthy enough to use and which owner/action is triggered when performance crosses its threshold.

[Open Role Case](BI-Decision-Intelligence-Lead_Public-Sector/)

---

## 8. AI Transformation Program Manager — Public Sector

**Business condition:** Teams have many AI ideas but no shared mechanism for determining which use cases should progress from idea to production.

**Dataset:** `data/ai_use_case_portfolio.csv`.

**Fields driving decisions:** business value • data readiness • technical feasibility • risk • adoption readiness • projected hours saved • owner • status.

**What I calculate:** weighted priority score • production-candidate flag • portfolio productivity potential.

**What I decide from it:** fund • pilot • hold • improve data • add controls • scale • terminate.

[Open Role Case](AI-Transformation-Program-Manager_Public-Sector/)

---

## 9. Power Platform Solution Architect — Public Sector

**Business condition:** Departmental forms and spreadsheets have expanded into business-critical workflows without a scalable application, data, automation, security, or support model.

**Dataset:** `data/requests.csv` plus workflow/audit structures in the role case.

**Fields driving decisions:** request ID • type • status • submitted/review dates • reviewer • priority • ECD • duplicate flag.

**What I calculate:** review cycle days • pending-review age • duplicate rate • ECD risk • approval/return rate.

**What I decide from it:** routing • reviewer capacity • duplicate handling • escalation • workflow redesign • production support requirements.

[Open Role Case](Power-Platform-Solution-Architect_Public-Sector/)

---

## 10. Financial Systems Modernization Manager — Public Sector

**Business condition:** Budget, obligations, expenditures, forecast, program delivery, and leadership reporting are maintained through separate reconciliation processes.

**Target dataset structure:** program/workstream • available authority • obligations • expenditures • forecast • milestone • ECD • risk • owner.

**Core formulas:**

    Execution Rate = Obligations / Available Authority
    Forecast Variance = Forecast - Budget
    Remaining Balance = Budget - Obligations
    Projected Pressure = Forecast - Available Authority

**What I decide from it:** rephase work • change scope • escalate resource pressure • reconcile forecast • protect critical milestones.

---

## Fragmented Process → Modernized Operating Model

| Fragmented Condition | Modernized Control | Business Result |
|---|---|---|
| Requests in email | Structured digital intake | Complete, traceable submissions |
| Separate spreadsheets | Governed data model | One operational record |
| Manual follow-up | Workflow automation | Reduced handoff delay |
| Decisions in meetings | Decision register | Traceable accountability |
| Static status decks | Live decision intelligence | Faster intervention |
| Finance separate from delivery | Integrated financial/program view | Earlier resource decisions |
| Untracked architecture choices | Architecture decision records | Reduced rework |
| AI pilots without controls | Governed AI lifecycle | Deployable, monitored AI |
| Adoption measured informally | Adoption/value tracker | Measurable realized value |
| Single-person workflow ownership | Service ownership + fallback | Operational continuity |

## Technology & Operating Stack

**Application and workflow:** Power Apps • Power Automate • SharePoint • Dataverse

**Analytics and data:** Power BI • DAX • Power Query • SQL • Python • APIs • governed semantic models

**Identity and governance:** Microsoft Entra ID • role-based access • DLP • environment controls • service accounts • audit history

**AI:** grounded retrieval • source-permission filtering • human review • telemetry • risk thresholds • use-case governance

**Program operations:** integrated schedules • RAID • decision logs • dependency management • UAT • release readiness • adoption • value realization

**Financial operations:** budget • obligations • expenditures • forecasts • variance • resource pressure • program-to-finance alignment

## Evidence in This Section

[Dataset → Formula → Decision Crosswalk](DATASET-FORMULA-CROSSWALK.md) shows how the actual CSV columns feed the calculations and operating decisions.

[Public Sector Data & Code Index](PUBLIC-SECTOR-DATA-CODE-INDEX.md) maps each role to its primary operational question and code structure.

[Real-Time Solution](REAL-TIME-SOLUTION.md) demonstrates a fragmented-to-modernized scenario.

[Code & Logic](CODE-AND-LOGIC.md) provides implementation-level SQL, Python, DAX, Power Fx, workflow, validation, risk, routing, SLA, financial, and projection logic.

## Portfolio Standard

The sample data is fictional and designed to demonstrate operating logic. The standard is that a reader should be able to trace a business condition into the source fields, reproduce the calculation, inspect the code, understand the threshold, and see the decision or action the result is intended to drive.
