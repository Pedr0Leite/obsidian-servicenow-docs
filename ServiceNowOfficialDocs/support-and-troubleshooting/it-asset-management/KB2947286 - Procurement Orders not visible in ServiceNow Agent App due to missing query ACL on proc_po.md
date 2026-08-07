---
title: "Procurement Orders not visible in ServiceNow Agent App due to missing query ACL on proc_po"
aliases:
  - KB2947286
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2947286
kb_number: KB2947286
last_modified: 2026-05-12
---

## Procurement Orders not visible in ServiceNow Agent App due to missing query ACL on proc\_po

  

 

## Issue

Procurement Orders are not visible in the ServiceNow Agent App for non-admin users who have the required procurement roles (`procurement_user` or `procurement_admin`) and the appropriate table-level ACL permissions to view the `proc_po` table.

* * *

## Symptoms

-   Users with the `procurement_user` or `procurement_admin` role cannot see Purchase Order records when selecting **POs next 30 days** in the ServiceNow Agent App.
-   Users with the `admin` role can see Purchase Order records in the Agent App without issue.
-   Affected users can view Purchase Orders normally in the Classic UI.
-   The following message appears in **System Logs (syslog)** for the affected transaction:

Invalid query detected, please check logs for details \[Unknown field null in table proc\_po\]

-   The following warning appears in the **application node logs** for the affected transaction:

Part of the query on proc\_po has been ignored because of insufficient access for 'query\_range' operation on proc\_po.due\_by

* * *

## Facts

-   The **POs next 30 days** filter in the Agent App uses the following encoded query against the `proc_po` table:

statusINordered,pending^due\_byRELATIVELE@dayofweek@ahead@30^ORdue\_byISEMPTY^EQ^ORDERBYnumber

-   This query includes a **relative range operation** (`RELATIVELE`) on the `proc_po.due_by` field, which requires `query_range` ACL access.
-   By default, when no query ACL is defined for a table, a `*.*` (star-dot-star) ACL grants `query_range` access to all users. However, when any query ACL is explicitly defined for a table, that default behavior is overridden — all `query_range` operations then require an explicit, matching query ACL.
-   Query ACLs for `proc_po.*` are not defined out of the box, which causes the `query_range` operation on `proc_po.due_by` to be blocked for non-admin users.
-   Admin users bypass ACL enforcement and are not affected.

**Note:** This behavior is consistent with the Query ACL security model introduced to prevent data inference attacks. When explicit query ACLs exist on a table, they take precedence over the default `*.*` grant, and any `query_range` operation not covered by a matching ACL will be denied.

* * *

## Release

All Versions

* * *

## Cause

No query ACL is defined for `proc_po.*`. When a relative date range filter (such as **POs next 30 days**) is applied in the Agent App, the platform evaluates `query_range` access on the `proc_po.due_by` field. Because no explicit query ACL grants this access to non-admin users, the range portion of the query is silently dropped, and no records are returned.

* * *

## Resolution

Create a query ACL for `proc_po.*` that grants `query_range` access to the appropriate procurement roles.

1.  Navigate to **System Security > Access Control (ACL)**.
    
2.  Click **New** to create a new ACL record.
    
3.  Set the following field values:
    
    -   **Type:** `record`
    -   **Operation:** `query_range`
    -   **Name:** `proc_po.*`
    
4.  In the **Requires role** related list, add the roles that should be granted `query_range` access — at minimum, `procurement_user` and `procurement_admin`.
    
5.  Save the ACL record.
    
6.  Test by logging in as a non-admin user with the `procurement_user` or `procurement_admin` role and selecting **POs next 30 days** in the Agent App. Purchase Order records should now be returned.
    

**Warning:** Modifying ACLs can affect record visibility across the platform. Validate this change in a sub-production environment before applying it to production, in accordance with your organization's change management process.

* * *

## Related Links

[Query ACLs — ServiceNow Documentation](https://docs.servicenow.com/bundle/washingtondc-platform-security/page/administer/contextual-security/concept/query-acls.html)

[Procurement — Purchase Orders (proc\_po) table reference](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/procurement/reference/ref_proc_po.html)
