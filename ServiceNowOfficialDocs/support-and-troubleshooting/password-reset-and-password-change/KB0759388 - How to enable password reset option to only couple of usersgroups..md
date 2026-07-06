---
title: "How to enable password reset option to only couple of users/groups."
aliases:
  - KB0759388
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759388
kb_number: KB0759388
last_modified: 2024-04-07
---

## How to enable password reset option to only couple of users/groups.

  

### Issue

-   It is possible to enable password reset feature to a set of users/groups.

### Release

-   All Versions.

### Resolution

1.  Navigate to Password Reset -> Processes
    -   https://<instance\_name>.service-now.com/pwd\_process\_list.do?sysparm\_query=
2.  Open any of the password reset processes you want to enable for a set of users.
3.  Disable "Apply to all users" checkbox.
4.  Group options will be enabled under the related lists tab.
5.  Provide the desired "groups" here.
6.  Users only in these groups will be able to use the "Password Reset" option.

![](sys_attachment.do?sys_id=43dc8c70db48b0d0fec4fb2439961929)
