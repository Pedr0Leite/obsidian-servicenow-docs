---
title: "Approval Coordinator not working when manual approvals for users and groups are added."
aliases:
  - KB0780999
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780999
kb_number: KB0780999
last_modified: 2024-04-08
---

## Approval Coordinator not working when manual approvals for users and groups are added.

  

### Issue

The user's Approval Coordinator workflow activity is not working correctly when manual approvals for users and groups are inserted. The user wanted to know why.

### Resolution

After an in-depth investigation, it was found that the behavior experienced is expected.  
  
As the user is adding the Manual approvals (u\_m2m\_change\_requests\_users) and Manual group approvals (u\_m2m\_change\_requests\_groups) on some custom tables, these approvals will not be displayed in the Approvals related list.  
  
The Out of Box (OOB) behavior is as follows:

-   Once a user adds a Group approval (sysapproval\_group) on a record (change\_request), the Business rule "SNC - Create user approvals for group" will fetch all the members from the group and create individual approvals.  
      
    -   Business rule: "SNC - Create user approvals for group"
        -   /nav\_to.do?uri=sys\_script.do?sys\_id=de16b5dfc0a80164001bc97ffed71f12

With these things in mind, the user was counseled that if they want to have an OOB-like behavior with those custom tables, they should create a Business Rule similar to "SNC - Create user approvals for group" which can fetch the group members and drop approvals in the "sysapproval\_approver" table.

If the user does this, everything will be displayed under the Approvals related list per their expectations.
