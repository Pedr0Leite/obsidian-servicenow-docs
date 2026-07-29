---
title: "Write operation error message is shown when using Applications module under System Applications menu"
aliases:
  - KB0657299
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657299
kb_number: KB0657299
last_modified: 2024-04-07
---

## Write operation error message is shown when using Applications module under System Applications menu

  

### Issue

# Symptoms

* * *

The following error message always comes up when navigating to Applications Module under the System Applications Menu:  
  
![](sys_attachment.do?sys_id=989e3c62db0ab450e515c22305961993)  
  

   

# Release

* * *

ALL

# Cause

* * *

This is usually caused by custom business rules that have been implemented on the sys\_attachment table that attempts to go back and modify the parent record for the attachment. If that tries to update the app and store related tables, it causes the error. The tables in question are:

-   sys\_app
-   sys\_store\_app
-   sys\_remote\_app
-   sys\_app\_version

   

# Resolution

* * *

Try disabling any custom business rules on sys\_attachment to identify which business rule is causing the error message. Once the offending rule is identified make sure it's logic keeps it from attempting to update the following tables:

-   sys\_app
-   sys\_store\_app
-   sys\_remote\_app
-   sys\_app\_version
