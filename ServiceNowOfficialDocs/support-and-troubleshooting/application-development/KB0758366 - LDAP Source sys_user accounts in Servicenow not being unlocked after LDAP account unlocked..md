---
title: "LDAP Source sys_user accounts in Servicenow not being unlocked after LDAP account unlocked."
aliases:
  - KB0758366
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758366
kb_number: KB0758366
last_modified: 2024-04-07
---

## LDAP Source sys\_user accounts in Servicenow not being unlocked after LDAP account unlocked.

  

### Issue

Behavior: Configured LDAP server account unlocked.  LDAP Source account in sys\_user table not being unlocked after sync from configured LDAP Server.

### Cause

Out of the box User onBefore Transform Script is commented out:

"...   
//Optional: Reactivate and unlock the user account   
// target.active = true;   
//target.locked\_out = ctrl.substr(-2, 1) == "1";   
..." 

### Resolution

Need to uncomment out of the box User onBefore transform script,  onBefore Transform Script:   
  
  
"...   
//Optional: Reactivate and unlock the user account   
target.active = true;   
target.locked\_out = ctrl.substr(-2, 1) == "1";   
..."
