---
title: "User Allocations are missing under Software entitlement"
aliases:
  - KB0830240
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830240
kb_number: KB0830240
last_modified: 2024-04-08
---

## User Allocations are missing under Software entitlement

  

### Issue

Under Software entitlement, there is no “User Allocation” related tab and it seems like this information is missing.  
But the same is present for Adobe whose License type = Subscription. 

### Release

All Versions.

### Resolution

1.  For the combination of Metric Group: Subscription and License Metric: User Subscription, user allocation is hidden by default.
2.  Adobe entitlements have the Metric group as "Adobe" and hence, the user allocations are available.  
    
3.  Also, if "User Subscriptions' are expected, the missing of user subscription might be because of failed imports for Abode or Office 365
4.  Verify the correctness of "Profile Configuration" and check system logs for any errors related to imports.
5.  Import job results can be viewed by following the below link:
    
    https://<instance\_name>.service-now.com/samp\_job\_log\_list.do?sysparm\_query=nameLIKEimport%5Ename%3DSAM%20-%20Import%20User%20Subscriptions&sysparm\_view=
    
    6\. Here is the job which imports user subscriptions:

https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_trigger.do?sys\_id=97c1b4721b460010f54042ebbc4bcb7c
