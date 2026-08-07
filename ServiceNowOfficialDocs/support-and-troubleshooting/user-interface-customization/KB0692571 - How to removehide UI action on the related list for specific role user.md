---
title: "How to remove/hide UI action on the related list for specific role user"
aliases:
  - KB0692571
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692571
kb_number: KB0692571
last_modified: 2025-01-03
---

## How to remove/hide UI action on the related list for specific role user

  

### Issue

# Description

* * *

How to remove/hide UI action on the related list for specific role user

For Example:

Remove/Hide right click "Approve" option (List context menu option) for the users with "itil" role on the table "Requested Item(sc\_req\_item)".

![](/sys_attachment.do?sys_id=729a24a6db42b450e515c223059619f1)

As shown in the image above, we want to remove/hide the "Approve" option for the itil users.

# Procedure

* * *

1.  Navigate to the sc\_req\_item.LIST (table on which the user can perform "approve" UI action)
2.  Notice that the List contect menu UI action "Approve" belongs to the table "sysapproval\_approver"
3.  Navigate to UI action and apply filters: table is "sysapproval\_approver" AND List Contest Menu is "True"
4.  Open the UI action with Name "Approve" and change the condition to "!gs.hasRole('itil')" to restrict this Ui action from users with itil role

By following the above steps, we are modifying the UI action condition to make it visible to only the users with the required roles.

# Applicable Versions

* * *

All

# Additional Information

* * *

To learn more about the UI actions, please refer the below document:

[https://docs.servicenow.com/csh?topicname=c\_UIActions.html&version=latest](https://docs.servicenow.com/csh?topicname=c_UIActions.html&version=latest)
