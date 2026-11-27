# Original enterprise technology implementation curriculum

Status: planned learning and implementation roadmap. No vendor deployment or certification is claimed by this document. Use synthetic data and personal sandbox environments only.

| Role | Original project | Technology |
|---|---|---|
| AI Technical Program Manager | AI delivery command center | Jira, Azure DevOps, Azure AI Foundry, Power BI |
| Principal AI Solution Architect | Knowledge assistant | Python, LangChain, LangGraph, RAG, vector search, FastAPI, React |
| Director AI & Digital Transformation | AI adoption office | Copilot Studio, Power Apps, CrewAI, Workato |
| Principal Technical Program Manager | Delivery command center | Jira, Azure DevOps, GitHub Actions, SQL |
| Enterprise AI Architect | Governed AI platform | Azure, AWS, GCP, Docker, Terraform, knowledge graphs |
| Director Business Intelligence | Executive intelligence | Fabric, Power BI, SQL, DAX, Python |
| Director Enterprise Applications | Integration hub | SAP BTP, SAP UI5, MuleSoft, Workato, Dataverse, Salesforce |
| Director Technology Programs | Investment portfolio | Project, Power BI, Power Automate, SAFe, PRINCE2 |

## Cross-platform labs
Firebase mobile and IoT telemetry; TypeScript/JavaScript front ends using React, Angular, Vue and Meteor; Java and C++ service examples; cloud ML deployment and orchestration; AI evaluation and safety. Select tools by business need rather than forcing every tool into one solution.

## Required walkthrough format
For each lab: business problem; prerequisites and licensing; architecture; numbered click-by-click instructions; genuine screenshots captured in a sandbox with secrets redacted; configuration and code; expected output; reproducible tests; troubleshooting; deployment and rollback; business value; limitations. Clearly label mockups and unverified instructions. Never claim third-party certifications as earned.

## First lab: local multi-agent workflow
1. Open the project folder in VS Code.
2. Open Terminal > New Terminal.
3. Create a virtual environment with python -m venv .venv.
4. Activate it using the command appropriate for your operating system.
5. Install the project's pinned dependencies once implemented.
6. Configure a local environment file using example variables, never commit secrets.
7. Run the workflow against synthetic requests.
8. Inspect agent outputs, approval gates and evaluation logs.
9. Run tests and capture actual output screenshots.
10. Document failures, fixes and limitations.

This is a planned lab, not a completed implementation. Vendor console steps must be verified against the current interface before publication.
