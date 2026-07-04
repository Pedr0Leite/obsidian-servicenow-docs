---
title: "'snc_internal' role is not added to users although CSM plugin and Explicit roles plugin are activated"
aliases:
  - KB0779846
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779846
kb_number: KB0779846
last_modified: 2024-01-28
---

## Issue

When we insert a user record in sys\_user table, immediately 'snc\_internal 'role should be added to the sys\_user record.  
This usually happens when you have either Customer Service \[or\] Explicit Roles plugin activated. Refer below product documentation to know more information on these roles:

-   [Explicit Roles](https://docs.servicenow.com/csh?topicname=explicit-roles.html&version=latest "Explicit Roles")
-   [Explicit Roles in CSM](https://docs.servicenow.com/csh?topicname=access-control-rules.html&version=latest "Explicit Roles in CSM")

But the 'snc\_internal' is only added to a sys\_user record based on the following criteria:

1.   'Last login time' for the sys\_user record should not be empty
2.  The UI action named "View Calendar" is present on the instance which forces loading the user record and adds snc\_internal role.

## Resolution

The explicit role snc\_internal role will be added to every user only if the "Last login time" is not empty.

If "Last login time" is empty/null, then it means that the user never logged-in, so it is expected that snc\_internal role is not added to the user until the user logs in.  
If this field is empty/blank, please log in as that user and after successful login, the role should be automatically.

However, if there is a UI action named "View Calendar" present in the instance, it forces loading the user and that triggers adding the snc\_internal role to the user.  
/sys\_ui\_action.do?sys\_id=c948277093210200ea933007f67ffbe9

In this case, system automatically populates last login time and there is no need for the user to login to see the role. The role gets added automatically.  
  
Hence, if the role is not added automatically, there are two(2) ways in which the issue can be fixed:

1.  Import the 'View Calendar' UI action onto the affected instance.
2.  Users have to be logged into the instance using their username and password to get the snc\_internal role automatically added.
