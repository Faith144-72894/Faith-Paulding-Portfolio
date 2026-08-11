# Software, Permissions & Licensing Architecture Matrix

Use this matrix with each real-time solution to show the implementation dependencies a solution architect, technical program manager, developer, analyst, or modernization lead must account for before deployment.

> Pricing below is illustrative public commercial USD list pricing. Government cloud, GCC/GCC High/DoD, enterprise agreements, contract vehicles, volume commitments, Azure consumption, taxes, and negotiated pricing can materially change cost. Always validate against the customer's tenant and current agreement.

## Microsoft Power Platform / BI
| Software | Solution Use | Typical Permissions | Example Public List Cost |
|---|---|---|---:|
| Power Apps Developer Plan | Build/test individual solutions | Developer environment / maker access | $0 |
| Power Apps Premium | Premium apps, Dataverse, premium/custom connectors | Environment access + app permission + Dataverse security role | $20/user/month |
| Power Apps Premium 2,000+ seats | Large-scale qualifying deployments | Same functional access; enterprise administration required | $12/user/month |
| Power Automate Premium | Premium cloud flows / attended automation | Flow owner/co-owner; connector permissions | $15/user/month |
| Power Automate Process | Core process / unattended automation | Process ownership + connection/service-account permissions | $150/bot/month |
| Power Automate Hosted Process | Hosted unattended automation | Process permissions + hosted machine administration | $215/bot/month |
| Power BI Pro | Publish/share/collaborate in shared BI | Workspace role + report/app access | $14/user/month |
| Power BI Premium Per User | Advanced per-user BI | Workspace/report access + PPU license | $24/user/month |
| Dataverse database add-on | Additional relational capacity | Environment/admin capacity management | $40/GB/month |
| SharePoint Online | Lists/documents/evidence | Site/List/Library read/contribute/admin based on role | Often part of Microsoft 365; verify tenant plan |
| Microsoft Entra ID | Identity/groups/access | User/group membership; admin roles only for authorized admins | Tenant-dependent |

## Data / Analytics Software
| Software | Solution Use | Permissions / Access | Cost Treatment |
|---|---|---|---|
| SQL Server / Azure SQL | Relational analytics and source integration | Database login/Entra identity; least-privilege SELECT/EXECUTE/WRITE as required | Deployment/edition/consumption dependent |
| Python | Analytics, projections, AI/risk calculations | Approved development/runtime environment; package and data-source access | Open-source language; hosting/compute may cost |
| Excel / Power Query | Source analysis, reconciliation, prototypes | File/library permissions and Microsoft 365 application rights | Microsoft 365 plan dependent |
| GitHub | Portfolio/source/version control | Repository read/write/admin based on responsibility | Plan dependent |

## AI Solution Dependencies
| Software / Service | Use | Required Permission | Cost Treatment |
|---|---|---|---|
| Approved AI model endpoint | Generation/inference | Authorized endpoint identity/API access | Consumption/model dependent |
| Retrieval/index service | Grounding approved content | Index/data-source read permissions | Service/consumption dependent |
| Azure / cloud monitoring | Telemetry and alerts | Monitoring Reader/Contributor as appropriate | Consumption dependent |
| Key/secret management | Credentials/secrets | Least-privilege secret/key access | Cloud service dependent |

## Permission Design Standard
1. Separate development, test, and production access.
2. Use Microsoft Entra groups/security roles instead of individual grants where practical.
3. Apply least privilege to data, connectors, environments, repositories, and reports.
4. Separate maker/developer permissions from tenant administration.
5. Restrict production write/admin access.
6. Use service accounts/service principals only where architecture and organizational policy permit them.
7. Document every premium connector, data source, identity dependency, and license dependency before release.
8. Revalidate licensing when user count, automation pattern, environment, or architecture changes.

## Cost Estimation Formula
```text
Estimated Monthly Software Cost =
(user-based licenses × licensed users)
+ (process/bot licenses × processes/bots)
+ capacity/storage add-ons
+ cloud/AI consumption
+ other required platform licensing
```

## Architecture Deliverable
Each solution folder should identify:
- software used;
- purpose of each component;
- required user/developer/admin permissions;
- premium connectors or premium platform dependencies;
- user/process/capacity licensing model;
- illustrative monthly/annual cost;
- assumptions and exclusions;
- government-cloud validation requirement.

## Official Microsoft References
- Power Apps pricing: https://www.microsoft.com/en-us/power-platform/products/power-apps/pricing/
- Power Automate pricing: https://www.microsoft.com/en-us/power-platform/products/power-automate/pricing
- Power BI licensing: https://learn.microsoft.com/en-us/power-bi/fundamentals/service-features-license-type
