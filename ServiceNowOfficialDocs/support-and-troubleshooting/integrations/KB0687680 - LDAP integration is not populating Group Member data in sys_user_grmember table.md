---
title: "LDAP integration is not populating Group Member data in sys_user_grmember table"
aliases:
  - KB0687680
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687680
kb_number: KB0687680
last_modified: 2024-04-07
---

## LDAP integration is not populating Group Member data in sys\_user\_grmember table

  

### Issue

LDAP integration is not populating Group Member data in sys\_user\_grmember table

  

# Problem

* * *

We have already imported users and group via LDAP successfully. But the problem is, Group members are not getting populated in sys\_user\_grmember table.

# Cause

* * *

 In LDAP integration, populating Group Members are handled via an onAfter Transform script which includes below code:

ldapUtils.addMembers(source, target);

The **source** object in above code refers to import set table which holds the LDAP Group import data. Field **u\_member** in import set table holds Group Member(s) data. Behind the scene, platform use u\_member field value in order to find the right match in sys\_user table. When the match is found, that particular user is added as a member in sys\_user\_grmember table.

Most of the time, we found that u\_member field field length/size for import set table in dictionary is short therefore, incoming data from the LDAP is truncated which in turn causing no match in sys\_user table and this issue appears.

# Solution

* * *

Increase the field size of u\_member field in sys\_dictionary for the specific import set table and the issue is fixed.
