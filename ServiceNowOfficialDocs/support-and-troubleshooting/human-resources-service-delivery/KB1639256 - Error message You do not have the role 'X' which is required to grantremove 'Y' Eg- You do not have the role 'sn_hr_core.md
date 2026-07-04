---
title: "Error message \"You do not have the role 'X' which is required to grant/remove 'Y' Eg:-  You do not have the role 'sn_hr_core.admin' which is required to grant/remove 'sn_esign.config_manager"
aliases:
  - KB1639256
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1639256
kb_number: KB1639256
last_modified: 2025-10-27
---

## Error message "You do not have the role 'X' which is required to grant/remove 'Y' Eg:- You do not have the role 'sn\_hr\_core.admin' which is required to grant/remove 'sn\_esign.config\_manager

  

Error message "You do not have the role ‘X’ which is required to grant/remove ‘Y’

Eg:-  You do not have the role 'sn\_hr\_core.admin' which is required to grant/remove 'sn\_esign.config\_manager

Anything we do with the role (if the user doesn't have the assignable by role) will surface this error (e.g. assigning the role to a user, adding a user to a group which contains this role, assigning this role to a group,).  

While updating assignable by of role, pls make sure it should not affect other places.

Soltution:- User need to have a assignable by role in order to perform these operations.

If the error show up  on just opening a group record  then check if “glide.security.scoped\_administration.role.show\_error” is set to true or not (It is expected to show the error message if "glide.security.scoped\_administration.role.show\_error" is set to true. Now This property is not shipped OOB.)
