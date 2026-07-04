---
title: "Troubleshooting purchase order integration errors between Software Asset Management and Coupa"
aliases:
  - KB2572231
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2572231
kb_number: KB2572231
last_modified: 2026-05-20
---

## Troubleshooting purchase order integration errors between Software Asset Management and Coupa

  

### Issue

Issue 1: HTTP 403 Forbidden error when submitting a purchase order to Coupa

When you create a purchase order in ServiceNow using the procurement process and select the Order button to trigger the Coupa integration, the following error appears:

`HTTP Request failure with 403 status: Method failed: (/api/requisitions/new/submit_for_approval) with code: 403 - Forbidden username/password combo`

* * *

Issue 2: Deprecated flow used for requisition creation

When a purchase order is submitted to Coupa, the transaction uses the deprecated flow _Create Requisition (Deprecated)_ instead of the current flow.

### Facts

### Release

Yokohama with SAM plugin and Coupa Spoke v4.5

### Cause

-   The OAuth connection credential alias does not have sufficient roles associated with the OAuth entity profile. The `core.requisition.write` role is required to call the requisition creation API.
-   The Coupa Spoke was updated with a new flow for requisition creation. The SAM integration was not aligned with the updated spoke version.

### Resolution

**Issue 1:**  
**Cause**

The OAuth connection credential alias does not have sufficient roles associated with the OAuth entity profile. The `core.requisition.write` role is required to call the requisition creation API.

**Resolution**

1.  Navigate to System OAuth > Application Registry Profiles and open the relevant OAuth entity profile.
2.  Add the `core.requisition.write` role to the profile.
3.  Request a new OAuth token to refresh the connection.
4.  Retry the purchase order submission.

For more information on required roles when configuring a Coupa connection, see [Create a Coupa integration profile](https://www.servicenow.com/docs/bundle/yokohama-it-service-management/page/product/procurement/task/create-coupa-int-profile.html).

* * *

**Issue 2:**   
**Cause**

The Coupa Spoke was updated with a new flow for requisition creation. The SAM integration was not aligned with the updated spoke version.

**Resolution**

This issue is tracked under problem PRB1937031. Monitor the problem record for updates and apply the fix when it becomes available.

For related setup documentation, see:

-   [Create a Coupa integration profile — Yokohama](https://www.servicenow.com/docs/bundle/yokohama-it-service-management/page/product/procurement/task/create-coupa-int-profile.html)
-   [Create a requisition on Coupa through the Procurement application — Yokohama](https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/procurement/task/create-req-coupa.html)
