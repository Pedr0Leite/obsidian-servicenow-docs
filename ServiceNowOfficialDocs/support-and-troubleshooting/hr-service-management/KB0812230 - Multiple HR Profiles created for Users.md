---
title: "Multiple HR Profiles created for Users"
aliases:
  - KB0812230
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812230
kb_number: KB0812230
last_modified: 2025-09-03
---

## Multiple HR Profiles created for Users

  

### Issue

Two HR Profiles have been created for some users. A customer async business rule creates an HR profile when a user record is inserted or updated if an HR profile does not exist.

### Release

All Releases

### Cause

When a user logins in to an instance, the sys\_user record is updated twice which fires the business rule twice. The script in the business rules queries the HR profile table and if one doesn't exist, a profile is created. 

### Resolution

As the code for creating the HR profile is not intensive change the business rule to an 'after' rule.
