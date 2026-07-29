---
title: "How to customize \"group by\" on list for a table"
aliases:
  - KB0787117
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787117
kb_number: KB0787117
last_modified: 2024-01-28
---

## How to customize "group by" on list for a table

  

### Issue

User need to remove some of the options from the "group by" in List view action.

[![](/sys_attachment.do?sys_id=beb7ed1e1b6660103013751f034bcb63)](https://docs.servicenow.com/csh?topicname=t_CreateAContextMenu.html&version=latest)

### Resolution

Role required : admin

**Procedure:**

1.  Please try to replicate the same steps to remove the required fields from "Group by" - List view  
      
    
2.  Open sys\_dictionary.list in Native UI
3.  Filter with required Table Name and Column Name that you want to restrict.  
      
    For example, Opened Dictionary entries page, filtered table name = Incident, and Column Name = Created by  
      
    
4.  In the Created by Dictionary Entry page, below you can find Attributes sections.
5.  Click **New** -> Dictionary Attribute page opens
6.  Under Field name: "Attribute" update as 'Can group' and set the Value as 'false'
7.  Click **submit**.

**Expected Behaviour:**

  
Now if you go to the list view under "Group By" you will not find the field "Created by" and under Personalize list column the "Group by" will be set disabled.

[Customize List V2 context menus](https://docs.servicenow.com/csh?topicname=t_CreateAContextMenu.html&version=latest "Customize List V2 context menus")
