---
title: "HR Template Checklist is not populating on sn_hr_core_task"
aliases:
  - KB0779067
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779067
kb_number: KB0779067
last_modified: 2024-04-08
---

## HR Template Checklist is not populating on sn\_hr\_core\_task

  

### Issue

Workflow is creating a new HR task but not populating the checklist

### Cause

"Populate Task Variables" under workflow activity 'Create Task'

### Resolution

For the HR Tasks being created via workflow, the template field is empty and 'template\_invoked' is false. So, the template values are not being fetched properly. When we create an HR Task manually and apply the template, the checklist gets added as expected on the task.  
  
In the 'Create Task' activity of the workflow, under Populate task variables changing the following: (please find the attached screenshot for your reference)  
\-> "Task values from' field to 'Values'  
\-> Set Values - From the dropdown select 'Template' and select the required template in the next field  
will populate the checklist on the HR Task as expected.   
  

![](sys_attachment.do?sys_id=97270849db8038d0fec4fb24399619d1)
