---
title: Manage TRM technical debt
description: Manage the TRM technical debts that are created for the products that aren’t approved for the usage.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-manage-trm-technical-debt.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Manage the Technology Reference Model in Enterprise Architecture Workspace, Exploring Technology Portfolio view, Exploring Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Manage TRM technical debt

Manage the TRM technical debts that are created for the products that aren’t approved for the usage.

A scheduled job **Populate TRM technical debts in the EA Workspace** runs and creates an entry in the TRM Technical Debt \[sn\_apm\_trm\_standards\_technical\_debt\] table for EA Workspace. The table shows a reference to the software in any business application that is not aligned with the TRM software phases. The table shows a reference to the software in any business application that either isn’t defined in TRM or has TRM product lifecycles that restrict the usage of the software. To know how the technical debts are calculated, see [[eaw-trm-technical-debt-calc|TRM Technical Debt calculation in Enterprise Architecture Workspace]].

**Note:** The **Populate TRM technical debts in the EA Workspace** scheduled job is available only when the Software Asset Management \(SAM\) Foundation or Software Asset Management \(SAM\) Professional plugin is installed.

**Parent Topic:**[[eaw-managing-the-technology-portfolio|Manage the Technology Reference Model in Enterprise Architecture Workspace]]

**Related topics**  


[TRM Technical Debt calculation in Enterprise Architecture Workspace](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/eaw-trm-technical-debt-calc.md)

[[view-trm-tech-debt|View TRM technical debts]]

[[eaw-run-job-trm-tech-debts|Run a scheduled job to update TRM technical debt data in EA Workspace]]

## Related

- [[eaw-trm-technical-debt-calc|TRM Technical Debt calculation in Enterprise Architecture Workspace]]
- [[eaw-managing-the-technology-portfolio|Manage the Technology Reference Model in Enterprise Architecture Workspace]]
- [[view-trm-tech-debt|View TRM technical debts]]
- [[eaw-run-job-trm-tech-debts|Run a scheduled job to update TRM technical debt data in EA Workspace]]
