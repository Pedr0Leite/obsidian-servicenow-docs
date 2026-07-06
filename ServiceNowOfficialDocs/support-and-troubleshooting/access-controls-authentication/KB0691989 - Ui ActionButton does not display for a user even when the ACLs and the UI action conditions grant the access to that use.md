---
title: "Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user"
aliases:
  - KB0691989
tags:
  - servicenow
  - support-kb
  - ui-actions
  - acl
  - access-control
  - roles
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691989
kb_number: KB0691989
last_modified: 2024-01-28
---

## Issue

# Symptoms

* * *

Absence of a UI action/Button even when the user meets the UI action condition and the associated ACLs.

# Release

* * *

All

# Cause

* * *

There is a UI section called "Requires role" on the UI action.

If there is a role specified for "requires role" and the user does not have that role, the UI action will not be made visible to that user.

# Resolution

* * *

1.  Navigate to the UI action that is not being displayed for the user eg: Global Delete UI action
2.  On the UI action form, notice that there is a section called "Requires role"
3.  Check if there is any role specified for "requires role"
4.  Make sure the user has the role specified in "requires role" to ensure the UI action visibility.

![](sys_attachment.do?sys_id=d12d2c62db82b450e515c22305961902)

Note: In the above example, even if the user meets the UI action condition and ACLs, he/she will not see the UI action unless he/she is an admin.

# Additional Information

* * *

Learn more about UI action:

[https://docs.servicenow.com/csh?topicname=c\_UIActions.html&version=latest](https://docs.servicenow.com/csh?topicname=c_UIActions.html&version=latest)

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]]
- [[KB0685046 -  How the Admin overrides option works in an access control (ACL) rule]]
