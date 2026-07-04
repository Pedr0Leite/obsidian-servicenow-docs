---
title: "Deprecated Script Include \"SoftwareEntitlementAllocationFilter\" for Asset Management"
aliases:
  - KB0962482
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0962482
kb_number: KB0962482
last_modified: 2024-04-20
---

## Deprecated Script Include "SoftwareEntitlementAllocationFilter" for Asset Management

  

### Issue

During upgrade to Quebec of our sub-production environments we found that the "SoftwareEntitlementAllocationFilter" Script Include was "Deprecated" during the upgrade. However, no guidance or Skipped Record notification was given to us to review the script include and determine if it should be retained. Upon checking, we found that the Script Include is called by an OOB field called "allocated\_model" which is used on our Device Allocations. The field auto-populates the Software Model from the Software Entitlement when a new Device Allocation is added.  
  
Even though the script was deprecated/deleted, the OOB field was still trying to call the Script Include, we were able to find the Script Include in our Prod instance and copy it downward but would like to know if this was a bug on ServiceNow's part or how we can be notified of scripts being deleted when active fields are using them.

### Cause

1\. OOTB the column "allocated model" on allocation table should be hidden. It is showing up in the customer instance because there may be some customizations on that form.  
2\. This column "allocated model" is no longer relevant and not used in our backend reconciliation code. It's ok to keep the reference and the script include "SoftwareEntitlementAllocationFilter", or delete the script include. It doesn't matter.  

### Resolution

**Short-term:**

Revert the form layout on alm\_entitlement table back to OOTB.

The "allocated model" will be auto defaulted by the script "javascript: current.licensed\_by.model", which will use the entitlement's software model as "allocated model".

  

Here is the related doc:  
[https://docs.servicenow.com/bundle/quebec-it-service-management/page/product/software-asset-management2/task/t\_AddAnEntitlementAllocationSAMF.html](https://docs.servicenow.com/bundle/quebec-it-service-management/page/product/software-asset-management2/task/t_AddAnEntitlementAllocationSAMF.html)  

  

  

**Long-term:**

We created the DEF0207326 to remove the reference to SoftwareEntitlementAllocationFilter for upgrading customers.
