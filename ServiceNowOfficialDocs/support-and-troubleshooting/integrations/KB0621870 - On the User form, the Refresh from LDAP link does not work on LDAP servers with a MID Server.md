---
title: "On the User form, the \"Refresh from LDAP\" link does not work on LDAP servers with a MID Server"
aliases:
  - KB0621870
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621870
kb_number: KB0621870
last_modified: 2024-04-07
---

## On the User form, the "Refresh from LDAP" link does not work on LDAP servers with a MID Server

  

### Issue

On the User form, the "Refresh from LDAP" link does not work on LDAP servers with a MID Server

Problem

* * *

If your user was imported by LDAP, and the LDAP server uses a MID Server to retrieve the data, it will not update the user records.  

 ![Refresh URL](sys_attachment.do?sys_id=69f8ec6edb02b450e515c2230596191c "Refresh URL")

Symptoms

* * *

The instance system logs could show either:  

-   WARNING \*\*\* LDAP: LDAP:
-   Connection refused
-   User not found

Cause

* * *

"Refresh from LDAP"  requires direct access to the LDAP server  

  
Resolution

* * *

To update the user data, run the data source or LDAP import for the LDAP server the user belong to.  
Do not use "Refresh from LDAP" if your LDAP server has a MID Server set.
