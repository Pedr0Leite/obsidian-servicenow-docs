---
title: "When Drill down to a Business Service on Event Management Dashboard, alerts are not shown for the Business Service eventhough there are open alerts for users without evt_mgmt_admin role"
aliases:
  - KB0692652
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692652
kb_number: KB0692652
last_modified: 2024-04-07
---

## When Drill down to a Business Service on Event Management Dashboard, alerts are not shown for the Business Service eventhough there are open alerts for users without evt\_mgmt\_admin role

  

### Issue

# Symptoms

* * *

There are open alerts for a Business Service but they're not loaded on the Event Management Dashboard when drilling into the Business Service. The alert list is loaded if user stays on the Dashboard and selects the Business service. This affects users without 'evt\_mgmt\_admin' role.

# Release

* * *

Jakarta and newer releases.

# Cause

* * *

-   Loading of the alerts should be sufficient for users with 'evt\_mgmt\_operator' role.
-   The Business Service Map when drilled down from Event Management Dashboard, is making calls 'ImpactAdminActionsProcessor' processor. This processor is limited to users with 'evt\_mgmt\_admin' role by 'ImpactAdminActionsProcessor' ACL.

# Resolution

* * *

This is fixed in PRB1253418, which is targeted for London release. 

# Additional Information

* * *

For older releases (Jakarta and Kingston), the use the following workaround:

1.  Navigate to System Security > Access Control (ACL)   
    2\. Search for Name = ImpactAdminActionsProcessor   
    3\. Open the ACL and add "evt\_mgmt\_operator" and/or "evt\_mgmt\_user" role
