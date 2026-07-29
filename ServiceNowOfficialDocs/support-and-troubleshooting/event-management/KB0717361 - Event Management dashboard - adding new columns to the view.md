---
title: "Event Management dashboard - adding new columns to the view"
aliases:
  - KB0717361
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717361
kb_number: KB0717361
last_modified: 2025-01-03
---

## Event Management dashboard - adding new columns to the view

  

### Issue

# Description

* * *

In the event management dashboard, you can modify the columns that you see by default

![](sys_attachment.do?sys_id=895968eedb02b450e515c2230596190f)

# Procedure

* * *

You can edit the event management dashboard view, to modify the columns you view. You can only add the fields from em\_alert\_history table.   
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_db\_object.do?sys\_id=6303d710db221300ab9bf7d61d9619cb  
  
You would need to add a new record to the "List Elements" related list in the below form:   
https://<instance-name>.service-now.com/sys\_ui\_list.do?sys\_id=82d89a0097a0030091be2ffee3ac4ab4  
  
You need to make sure you are adding the exact column name from em\_alert\_history table under "Element" field. The List ID should be "em\_alert\_history". Please use an existing record as a reference 

# Applicable Versions

* * *

Any version
