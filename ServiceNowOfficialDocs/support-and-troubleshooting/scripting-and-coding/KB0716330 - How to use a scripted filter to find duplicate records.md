---
title: "How to use a scripted filter to find duplicate records"
aliases:
  - KB0716330
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716330
kb_number: KB0716330
last_modified: 2025-01-03
---

## How to use a scripted filter to find duplicate records

  

### Issue

# Description

* * *

How to use a scripted filter to find duplicate records (task table) and display in a list. 

# Procedure

* * *

1.  Download this [script include](https://support.servicenow.com/nav_to.do?uri=sys_attachment.do?sys_id=3cfa202adb42b450e515c2230596198d "script include") and import into your instance.
2.  User this url to perform the scripted filter search:  
    /incident\_list.do?sysparm\_query=number%3Djavascript%3A%20new%20SearchRec().findDup()

# Applicable Versions

* * *

All

# Additional Information

* * *

The customization described is not supported by ServiceNow Customer Support. This method is provided as-is and should be tested thoroughly before implementation. More information on scripted filters can be found in our product documentation [here](https://docs.servicenow.com/csh?topicname=t_ScriptedFilters.html&version=latest "here").
