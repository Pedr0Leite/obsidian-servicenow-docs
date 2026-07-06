---
title: "Role based multi-factor authentication will not be enforced when the role name has upper case letters"
aliases:
  - KB0788899
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788899
kb_number: KB0788899
last_modified: 2024-04-08
---

## Role based multi-factor authentication will not be enforced when the role name has upper case letters

  

### Issue

Role-based multi-factor authentication can be configured to administrate MFA for many users based on their roles instead of enabling MFA for them at a per-user level.

You can add the roles under Multi-factor Authentication > Multi-factor Criteria > Multi-factor Roles. In case the role that you add has Upper case character like "TestRole", MFA will not be enforced for the

users who has this role.

### Cause

This is identified as a bug and documented in PRB1377942

### Resolution

Roles that are added to the "Multi-factor Roles" should NOT have any upper case character in the name.
