---
title: "Microsoft CIS License Misassignment on Nutanix Clusters Due to Non-Virtualization Relationships"
aliases:
  - KB3023576
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3023576
kb_number: KB3023576
last_modified: 2026-05-15
---

## Microsoft CIS License Misassignment on Nutanix Clusters Due to Non-Virtualization Relationships

  

### Issue

Software Asset Management (SAM) reconciliation may not correctly assign Microsoft Core Infrastructure Suite (CIS) Datacenter and Standard licenses for virtual machines (VMs) running on Nutanix clusters. This occurs when Nutanix VMs have a "registered:registered on" CMDB relationship instead of "hosted:hosted on" or "virtualized:virtualized by." The SAM reconciliation engine does not interpret "registered:registered on" as a virtualization relationship, causing the system to default to Standard edition licensing rather than Datacenter, even for high-density clusters.

### Release

Not applicable.

### Cause

The SAM reconciliation engine requires a "hosted:hosted on" or "virtualized:virtualized by" relationship to recognize VMs as virtualized for license optimization purposes. When VMs are discovered with a "registered:registered on" relationship, the engine cannot apply Datacenter edition licensing logic, and Standard licenses are assigned by default.

Additionally, missing or misconfigured downgrade rights and install or inference conditions on the CIS software models can prevent correct license assignment across related products such as System Center.

### Resolution

To resolve this issue, follow these steps:

1.  In the CMDB, verify the relationship type for your Nutanix VMs. Confirm whether VMs are using "registered:registered on" instead of "hosted:hosted on" or "virtualized:virtualized by."
2.  Update the CMDB relationships for Nutanix VMs to use "hosted:hosted on" or "virtualized:virtualized by" so the SAM reconciliation engine can correctly identify them as virtualized.
3.  Navigate to the Microsoft CIS Datacenter entitlement record in SAM and add downgrade rights from Datacenter to Standard.
4.  Review the inference and install conditions on the CIS Datacenter and CIS Standard software models. Ensure that all relevant System Center installs can be inferred to the CIS suite.
5.  Run reconciliation and review the Microsoft Core License Optimization Report to confirm that Datacenter licenses are now assigned to high-density clusters as expected.

Verification:  
After completing the steps above, verify that the reconciliation results show correct license assignment logic, with Datacenter licenses applied to qualifying clusters and Standard licenses applied where appropriate.
