# Data Context, Formulas & Code | Cloud Transformation Program Manager

## Data Story
The migration dataset connects each workload to business criticality, technical dependencies, migration wave, readiness controls, rollback, cutover, defects, and business acceptance.

## Grain
One row per workload per migration wave; separate child records for dependencies, readiness gates, cutover events, and defects.

## Formulas
Readiness % = Passed Required Gates / Required Gates

Rollback Coverage = Workloads with validated rollback / Workloads scheduled for cutover

Migration Success % = Accepted workloads / Cutover workloads

Defect Rate = Post-cutover defects / Migrated workloads

## SQL
    SELECT Wave,
           COUNT(*) AS Workloads,
           AVG(ReadinessPercent) AS AvgReadiness,
           SUM(CASE WHEN RollbackValidated=0 THEN 1 ELSE 0 END) AS RollbackGaps
    FROM WorkloadMigration
    GROUP BY Wave;

## Python
    required = ["security","data","integration","rollback","support","business_acceptance"]
    def cutover_gate(record):
        failed=[g for g in required if not record.get(g,False)]
        return "GO" if not failed else "NO-GO: " + ", ".join(failed)

## Context
A workload being technically movable does not mean it is operationally ready. I use the data to distinguish infrastructure completion from business cutover readiness.

## Decisions Supported
Move workload • hold workload • change migration wave • invoke rollback • extend stabilization • retire legacy environment.
