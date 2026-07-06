---
title: "Unable to add roles, Insert new a row does not exist."
aliases:
  - KB0749023
tags:
  - servicenow
  - support-kb
  - sys_user_preference
  - list-edit
  - roles
  - acl
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749023
kb_number: KB0749023
last_modified: 2024-04-20
---

## Issue

# Symptoms

Unable to add roles, Insert new a row does not exist.

# Release

All

# Environment

Admin or any users who should be able to create ACL's.

# Cause

User Preference - \[list\_edit\_enable\] set to False 

In the sys\_user\_preference table, for that particular user, **list\_edit\_enable** preference set to **false**

# Resolution

Set this User Preference - \[list\_edit\_enable\] to True or delete.

## Related

- [[KB0743902 - Unable to view all sys_user_preferences records as an Admin, seeing security constraints message]]
- [[KB0749174 - Customization considerations for Access Controls (ACLs)]]
