---
title: "\"sn_hr_core.admin\" Role not getting assigned to a non-hr admin user"
aliases:
  - KB0777739
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0777739
kb_number: KB0777739
last_modified: 2024-04-07
---

## Issue

"sn\_hr\_core.admin" Role not getting assigned to a non-hr admin user.

There is a user "HR Admin" which has the admin, security admin, and the HR Admin role, but still, he is not able to give the "sn\_hr\_core.admin" role to any other user.

#### Steps to Reproduce

1.  Log in with a user having "sn\_hr\_core.admin" Role.
2.  Select any other non-hr admin user.
3.  Scroll down to the roles related list and select edit.
4.  Add the hr admin \[sn\_hr\_core.admin\] role
5.  The role is not given to the user

## Resolution

Recommend to remove and reassign the "sn\_hr\_core.admin" role to the user.
