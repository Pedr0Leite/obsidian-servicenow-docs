---
title: "When trying to select a walk-up location as the Walk-up user, the location box infinitely loads. Why?"
aliases:
  - KB0794090
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794090
kb_number: KB0794090
last_modified: 2024-10-21
---

## When trying to select a walk-up location as the Walk-up user, the location box infinitely loads. Why?

  

### Issue

When impersonating the Walk-up user in the walk-up portal and trying to click the locations reference field, it is stuck loading infinitely. The user wanted to know why this is happening.

### Resolution

It was found that the customer had activated this Table API ACL which is inactive by default:

-   /nav\_to.do?uri=sys\_security\_acl.do?sys\_id=9ef8bc918733320025fbd1a936cb0bdd

This ACL they enabled exists for a specific use case of rolling back the REST framework's security behavior to the Fuji release. If a customer is not trying to address this specific use case then it should not be enabled. This ACL requires that _**all**_ users calling the Table API have the role snc\_platform\_rest\_api\_access. **There is no workaround to this requirement other than deactivating the ACL.**

When this ACL is active the walk-up user will fail the role check on that ACL unless they are assigned the snc\_platform\_rest\_api\_access role. This will cause the location reference field to load infinitely.  
  
Reverting the ACL back to OOB (active = false), and clearing the cache (a crucial step to make this work, as ACLs cache), allows the walk-up user to see all locations almost immediately.
