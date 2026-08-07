---
title: "Software Asset Workspace - Content Lookup - Software PPNs not displayed when filtering by Publisher using contains or starts with"
aliases:
  - KB2977789
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2977789
kb_number: KB2977789
last_modified: 2026-04-23
---

## Software Asset Workspace - Content Lookup - Software PPNs not displayed when filtering by Publisher using contains or starts with

  

 

## Issue

In the Software Asset Workspace, the Content Lookup tool does not return Software Product Part Numbers (PPNs) when filtering the Publisher field using **contains** or **starts with** operators.

## Symptoms

-   Navigating to **Software Asset Workspace > Content Lookup** and searching for software PPNs returns no results when filtering the Publisher field with **contains** or **starts with**.
-   The following error appears in App Node logs:  
      
    `Part of the query on samp_sw_product_definition has been ignored because of insufficient access for 'query_range' on samp_sw_product_definition.entitlement_definition.`
-   The Access Analyzer confirms that the user is blocked by `query_range` ACLs on the `samp_sw_product_definition` table.
-   No `query_range` ACL rules exist for `samp_sw_product_definition` or `samp_sw_product_definition.*` on the instance.

## Facts

-   Applies to the **Software Asset Workspace** Content Lookup feature.
-   The affected table is `samp_sw_product_definition`.
-   The issue is caused by missing `query_range` ACL rules for the table and its dot-walked fields (`samp_sw_product_definition.*`).
-   This condition can occur on instances where the required `query_range` ACLs were not generated automatically, such as after a new plugin or Store App installation, or following an upgrade where the write-audit process did not create the rules for this table.
-   On instances where the ACLs were previously auto-generated, the rules carry the following attributes:
    -   **Decision Type:** Allow If
    -   **Admin Overrides:** false
    -   **Conditions:** _UserIsAuthenticated_ is true AND _HasRightsToReadIsTrue_ is true (via the `UserIsAuthenticatedAndHasRightsToRead` security attribute), scoped to users with the **public** role

## Release

Xanadu, Yokohama, Zurich

## Cause

The `query_range` ACL rules for the `samp_sw_product_definition` table and its dot-walked field references (`samp_sw_product_definition.*`) are absent from the instance. When these ACLs are missing, the platform's access control evaluation drops parts of the query that reference dot-walked fields — such as the `entitlement_definition` reference — resulting in the Publisher filter returning no matches and the error being logged in App Node logs.

## Resolution

Create the missing `query_range` ACL rules for the `samp_sw_product_definition` table. Two rules are required: one for the table itself and one for its dot-walked fields.

**Note:** Verify that these ACL rules do not already exist on the instance before proceeding. Navigate to **System Security > Access Control (ACL)** and filter by Type = _query\_range_ and Name = _samp\_sw\_product\_definition_.

To create the ACL rules, navigate to **System Security > Access Control (ACL)** and create two new records using the attributes below.

**Rule 1 — Table-level query\_range ACL**

| Field | Value |
| --- | --- |
| Type | query\_range |
| Name | samp\_sw\_product\_definition |
| Decision Type | Allow If |
| Admin Overrides | false |
| Roles | public |
| Security Attribute | UserIsAuthenticatedAndHasRightsToRead |

**Rule 2 — Dot-walked fields query\_range ACL**

| Field | Value |
| --- | --- |
| Type | query\_range |
| Name | samp\_sw\_product\_definition.\* |
| Decision Type | Allow If |
| Admin Overrides | false |
| Roles | public |
| Security Attribute | UserIsAuthenticatedAndHasRightsToRead |

**Important:** The `UserIsAuthenticatedAndHasRightsToRead` security attribute evaluates two conditions: _UserIsAuthenticated_ is true AND _HasRightsToReadIsTrue_ is true. Confirm that this security attribute is available on the instance before saving the ACL records.

1.  Navigate to **System Security > Access Control (ACL)** and click **New**.
    
2.  Set **Type** to `query_range` and enter `samp_sw_product_definition` in the **Name** field.
    
3.  Set **Decision Type** to **Allow If** and ensure **Admin Overrides** is set to **false**.
    
4.  In the **Roles** related list, add the **public** role.
    
5.  In the **Security Attribute** field, select `UserIsAuthenticatedAndHasRightsToRead`.
    
6.  Click **Submit** to save Rule 1.
    
7.  Repeat steps 1–6 for Rule 2, entering `samp_sw_product_definition.*` as the **Name**.
    
8.  Once both rules are saved, return to **Software Asset Workspace > Content Lookup** and verify that filtering the Publisher field with **contains** or **starts with** now returns PPN results as expected.
    

## Related Links

[Create query range ACLs — ServiceNow Documentation](https://docs.servicenow.com/bundle/latest/page/product/software-asset-management2/task/create-query-range-acl.html)

[Software Asset Management — Content Lookup](https://docs.servicenow.com/bundle/latest/page/product/software-asset-management2/concept/sam-pro-content-lookup.html)
