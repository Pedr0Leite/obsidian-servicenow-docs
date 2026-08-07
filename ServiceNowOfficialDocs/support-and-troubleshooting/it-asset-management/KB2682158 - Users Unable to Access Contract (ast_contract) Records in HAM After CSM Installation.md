---
title: "Users Unable to Access Contract (ast_contract) Records in HAM After CSM Installation"
aliases:
  - KB2682158
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2682158
kb_number: KB2682158
last_modified: 2025-12-15
---

## Users Unable to Access Contract (ast\_contract) Records in HAM After CSM Installation

  

### Issue

Users are unable to view certain Contract (ast\_contract) records after enabling the Customer Service Management (CSM) plugin, even though the records exist and the users have the CSM Agent role. Only a subset of Contract records—specifically those with the Account field populated—are visible to the affected users.

### Release

All

### Cause

-   This issue is occurring due to the Business Rule: “Contract query rules.”

               https://<instance>.service-now.com/now/nav/ui/classic/params/target/sys\_script.do%3Fsys\_id%3D710e182f0fb210103ff81b41ff767e2d

-   This behavior is triggered because the system property sn\_cs\_queryrules.use\_query\_rules is set to true.

               https://<instance>.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=931020e1b3521010700b4d43c6a8dcb6

-   When this property is enabled, access to records in the Contract table is controlled by Query Rules.
-   For a contract record to be accessible, it must match at least one applicable Query Rule.
-   In addition, the user must have the required roles defined in the matching Query Rule.

               https://<instance>.service-now.com/sn\_query\_rule\_list.do?sysparm\_query=tableSTARTSWITHast\_contract&sysparm\_first\_row=1&sysparm\_view=&sysparm\_choice\_query\_raw=&sysparm\_list\_header\_search=true

-   If the record does not satisfy any Query Rule or the required roles are missing, the contract record will not be accessible.

### Resolution

One of the following actions is required to resolve the issue:

1.  Assign additional appropriate CSM roles to the user so they match a less restrictive Query Rule.
2.  Modify existing Query Rules to allow broader access (customization).
3.  Disable Query Rules enforcement by setting the system property  
    sn\_cs\_queryrules.use\_query\_rules = false  
    _(Not recommended without proper impact analysis, as this affects record-level access controls across CSM.)_
