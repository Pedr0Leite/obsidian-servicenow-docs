---
title: "Variable values are empty after submission in RITM records"
aliases:
  - KB0714206
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714206
kb_number: KB0714206
last_modified: 2024-04-07
---

## Variable values are empty after submission in RITM records

  

### Issue

# Symptoms

* * *

Mandatory variable values are empty

# Release

* * *

London and before

# Cause

* * *

The service portal UI formatter that renders the widget which displays the variables in portal view is customized and it has the old code. 

# Resolution

* * *

The service portal UI formatter that renders the widget which displays the variable editor in the portal view is customized and is using an older code.   
  
When replaced the widget with the OOB widget, the issue is resolved.   
  
The Service Portal UI Formatters table can be reached at [/sp\_ui\_formatter\_list.do](https://instancename.service-now.com/sp_ui_formatter_list.do)   
  
  
To resolve the issue, kindly verify the code in the customized widget (with OOB widget "sp-variable-editor" as the reference) or the OOB widget can be used.
