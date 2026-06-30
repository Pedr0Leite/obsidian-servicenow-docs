---
title: View TRM technical debts
description: You can view the Technology Reference Model \(TRM\) technical debts that are created for the products that aren’t aligned with the TRM phases and standards.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/view-trm-tech-debt.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Working with Technology Reference Model \(TRM\) in EA Workspace, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# View TRM technical debts

You can view the Technology Reference Model \(TRM\) technical debts that are created for the products that aren’t aligned with the TRM phases and standards.

## Before you begin

Role required: sn\_apm.apm\_analyst

## About this task

A scheduled job **Populate TRM technical debts in the EA Workspace** runs and creates an entry in the TRM Technical Debt \[sn\_apm\_trm\_standards\_technical\_debt\] table for EA Workspace. The table shows a reference to the software in any business application that is not aligned with the TRM software phases. The table shows a reference to the software in any business application that either isn’t defined in TRM or has TRM product lifecycles that restrict the usage of the software. To know how the technical debts are calculated, see [[eaw-trm-technical-debt-calc|TRM Technical Debt calculation in Enterprise Architecture Workspace]].

**Note:** The **Populate TRM technical debts in the EA Workspace** scheduled job is available only when the Software Asset Management \(SAM\) Foundation or Software Asset Management \(SAM\) Professional plugin is installed.

## Procedure

1.  Navigate to **Workspace** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Technology Portfolio page by selecting the Technology Portfolio icon \[Omitted image "technology-portfolio-icon.png"\] Alt text: Technology portfolio icon.

3.  Select **Technical Debt**.

4.  View the TRM technical debts.

    For field information, see [[eaw-trm-technical-debt-form|TRM technical debt form]].


## Result

Review the list of TRM products and associated business applications details. You can also view the reason for the technical debt.

**Parent Topic:**[[eaw-work-with-trm|Working with Technology Reference Model \(TRM\) in EA Workspace]]

**Related topics**  


[[eaw-view-all-trm-phases|View all TRM phases]]

[[eaw-create-trm-prod-lifecycle|Add a TRM product in Enterprise Architecture Workspace]]

[[view-all-trm-categories|View all TRM categories]]

[[eaw-view-all-trm-products|View all TRM products]]

[[eaw-run-job-trm-tech-debts|Run a scheduled job to update TRM technical debt data in EA Workspace]]

[[eaw-request-a-trm-products|Request a TRM product]]

[[eaw-view-all-trm-products-grouped-by-product-category|View all TRM products grouped by product category]]

[[eaw-request-a-trm-product-lifecycle|Request a TRM product lifecycle]]

[[eaw-assoicate-artifact-trm-prod|Associate an Architectural Artifact to a TRM product]]

[[eaw-create-trm-prod-lifecycle-req|Add a TRM product lifecycle]]

[[eaw-managing-the-technology-portfolio|Manage the Technology Reference Model in Enterprise Architecture Workspace]]

[[eaw-view-update-trm-requests|View or update your TRM requests]]

## Related

- [[eaw-trm-technical-debt-calc|TRM Technical Debt calculation in Enterprise Architecture Workspace]]
- [[eaw-trm-technical-debt-form|TRM technical debt form]]
- [[eaw-work-with-trm|Working with Technology Reference Model \(TRM\) in EA Workspace]]
- [[eaw-view-all-trm-phases|View all TRM phases]]
- [[eaw-create-trm-prod-lifecycle|Add a TRM product in Enterprise Architecture Workspace]]
- [[view-all-trm-categories|View all TRM categories]]
- [[eaw-view-all-trm-products|View all TRM products]]
- [[eaw-run-job-trm-tech-debts|Run a scheduled job to update TRM technical debt data in EA Workspace]]
- [[eaw-request-a-trm-products|Request a TRM product]]
- [[eaw-view-all-trm-products-grouped-by-product-category|View all TRM products grouped by product category]]
- [[eaw-request-a-trm-product-lifecycle|Request a TRM product lifecycle]]
- [[eaw-assoicate-artifact-trm-prod|Associate an Architectural Artifact to a TRM product]]
- [[eaw-create-trm-prod-lifecycle-req|Add a TRM product lifecycle]]
- [[eaw-managing-the-technology-portfolio|Manage the Technology Reference Model in Enterprise Architecture Workspace]]
- [[eaw-view-update-trm-requests|View or update your TRM requests]]
- [[ea-workspace|Enterprise Architecture Workspace]]
