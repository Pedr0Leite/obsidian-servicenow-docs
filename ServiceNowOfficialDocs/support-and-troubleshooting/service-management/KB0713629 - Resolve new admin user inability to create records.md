---
title: "Resolve new admin user inability to create records"
aliases:
  - KB0713629
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713629
kb_number: KB0713629
last_modified: 2025-10-01
---

## Resolve new admin user inability to create records

  

### Issue

A newly created admin user may be unable to create records, such as incident records (incident.do). They may also notice that the New UI action is missing on a table and all fields appear as read-only. This issue typically occurs because the role required for the UI action is set to read-only. 

### Release

Any supported releases

### Cause

If the user has been assigned the snc\_read\_only role it restricts them to read-only across the platform.

**Note:** Assign snc\_read\_only role only to users. Do not assign this role to other resources in the system, such as applications and access control lists (ACL).

  

### Resolution

To remove the snc\_read\_only role from the user's profile:

1.  Log in to the instance with an admin or user\_admin account.
2.  Go to **User Administration** > **Users**.
3.  Filter the user list to locate the specific user.
4.  To open the user account record, select the **Information** icon to the left of the row corresponding to the user.
5.  Scroll to the **Roles List**, and select **Edit**. 
6.  In the list on the right, find the snc\_read\_only role.
7.  Select the left arrow to move the role to the list on the left. This removes the read-only role from the user.
8.  Select **Save**. 

### Related Links

[How to Read-only role](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/user-administration/concept/c_ReadOnlyRole.html)

[The read-only role and how to use it](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748343)
