---
title: "Adding a custom Assignment group Field on to Task SLA Table"
aliases:
  - KB0832190
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0832190
kb_number: KB0832190
last_modified: 2026-06-24
---

## Adding a custom Assignment group Field on to Task SLA Table

  

### Issue

You have added a custom 'assignment group' field on the task sla table that is a reference to the Group table.  
You require this to be populated by the parent incident assignment group when the Task Sla is created.  
  
Currently your custom field assignment group field on the task sla enables you to manually select a value but you require it to autopopulate with Incident assignment group.

You want to know how to fix this.

Ultimately you want to report on incident and task\_sla tables by Assignment Group.

### Release

All

### Cause

  
You have not written any script that would cause the task\_sla assignment group field to be auto-populated.  
This would not happen automatically.  
  
OOB Assignment Group does not exist on the task\_sla table and so for any implementation where you require a field on a child table to be populated by a value from the parent table a customization is required.

### Resolution

  
1\. To populate your custom 'assignment group' field on the task\_sla table you will need to create a custom business rule which sets assignment group in task\_sla table.  
  
Please note that customizations is out of scope for Technical Support, however similar requirement can be found on the community that could assist you in creating your own business rule.

Please reference the below url:  
https://community.servicenow.com/community?id=community\_question&sys\_id=683c0765db9cdbc01dcaf3231f9619e9  
  
In addition please be aware that for any additional assistance with your script you can create your own thread on the community forum so you can engage developers to assist you for your own scenario.  
  
2.  Please be aware that we provide OOB a database view 'incident\_sla' that is explicitly for reporting purposes and so would allow you to report on the fields from both tables combined. You can view this database view and test if it helps you meet your requirement.
