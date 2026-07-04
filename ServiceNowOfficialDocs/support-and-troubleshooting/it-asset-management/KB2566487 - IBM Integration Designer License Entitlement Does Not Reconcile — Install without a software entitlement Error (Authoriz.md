---
title: "IBM Integration Designer License Entitlement Does Not Reconcile — \"Install without a software entitlement\" Error (Authorized User Metric)"
aliases:
  - KB2566487
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2566487
kb_number: KB2566487
last_modified: 2026-05-22
---

## IBM Integration Designer License Entitlement Does Not Reconcile — "Install without a software entitlement" Error (Authorized User Metric)

  

### Issue

When you create an entitlement for IBM Integration Designer using the Authorized User metric and the Subscription publisher part number (PPN) D0INXLL, and then run a reconciliation, some installations of the product do not reconcile. The reconciliation result shows the reason: Install without a software entitlement.

### Symptoms

When you navigate to the SAM workspace and select License Usage, then search for the publisher IBM and review the product results for Integration Designer under Installs Requiring Action, the reason displayed is Install without a software entitlement.

If you try to add the entitlement for PPN D0INXLL with the license metric Authorized User, the following warning appears:

> "The license metric that you have chosen requires CAL records to be created. Please ensure that the CAL records are populated for the license metric that you have chosen."

### Release

All

### Cause

There is no corresponding client access record (CAL record) for the entitlement. The Authorized User license metric requires CAL records to be present before reconciliation can succeed.

### Resolution

To resolve this issue, add the correct client access record and associate both users and devices with installations.

1.  Navigate to the SAM workspace.
2.  Locate the entitlement for IBM Integration Designer (PPN: D0INXLL).
3.  Add a client access record for the entitlement. For instructions, see [Create a software client access record in workspace](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/create-clientaccess-workspace.html) in the ServiceNow documentation.
4.  In the client access record, add both the relevant users and the devices with installations.
5.  After you save the client access record, run reconciliation again and verify that the installations now reconcile correctly.

### Related Links

-   [Software license metrics — ServiceNow Australia IT Asset Management documentation](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/c_SAMLicenseMetrics.html): Describes the Authorized User metric — "Licenses each user who is granted access to an IBM software product."
-   [IBM user-based licenses](https://www.servicenow.com/docs/r/xanadu/it-asset-management/software-asset-management/ibm-user-based-licensing.html)
-   [Create a software client access record in workspace](https://www.servicenow.com/docs/r/xanadu/it-asset-management/software-asset-management/create-clientaccess-workspace.html)
