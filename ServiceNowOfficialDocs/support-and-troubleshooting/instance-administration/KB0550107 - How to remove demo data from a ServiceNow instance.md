---
title: "How to remove demo data from a ServiceNow instance"
aliases:
  - KB0550107
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550107
kb_number: KB0550107
last_modified: 2026-04-08
---

## How to remove demo data from a ServiceNow instance

  

### Issue

Demo data is typically included when an instance is created and is commonly removed prior to using the instance in a production environment.  

**Important:** Demo data removal on production should be successfully tested and verified on a non-production instance before requesting that demo data be deleted.

ServiceNow engineers with the sn\_customerservice\_agent role can request demo data removal on behalf of customers via the service catalog, provided the request is raised by a customer with the customer\_admin role.

### Release

All supported releases

### Resolution

To request deletion of demo data:

1.  Go to [Now Support.](https://support.servicenow.com/now "Now Support")
2.  Create a case using the instructions in [How to create a case on Now Support](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960058 "How to create a case on Now Support"). 
3.  Enter the following case details: 
    -   **Case type**: Service request
    -   **Subject**: Delete demo data
    -   **Instance(s) impacted**: Select the instances from which demo data should be removed
4.  Provide the following information to describe the issue:

-   -   If the instance selected is production:
        -   Specify whether the removal of demo data has been tested in a non-production instance
        -   Whether the production instance is live, or
        -   Whether the request is to remove demo data in a live production instance without testing

**Note**: Demo data removal on production should be successfully verified on a non-production instance that is a recent clone of the production instance.

1.  1.  -   Requested date and time to remove demo data (actual date and time will be based on resource availability).

If you have questions about demo data removal, see [Demo Data Removal FAQ](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743670).

### Related Links

  
[How to create a case on Now Support](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960058 "How to create a case on Now Support")
