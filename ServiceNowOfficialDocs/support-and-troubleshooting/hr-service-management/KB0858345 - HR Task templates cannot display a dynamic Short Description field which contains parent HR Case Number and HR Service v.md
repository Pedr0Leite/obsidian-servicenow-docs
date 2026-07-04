---
title: "HR Task templates cannot display a dynamic Short Description field which contains parent HR Case Number and HR Service values"
aliases:
  - KB0858345
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858345
kb_number: KB0858345
last_modified: 2025-09-03
---

## Issue

Customer have a  requirement to have HR Task templates that should have a dynamic Short Description field which contains parent HR Case Number and HR Service values.  
To achieve this they  tried using 'javascript: current.parent.number', '${current.parent.number}' and few other options but nothing worked.   
When  checked the "sn\_hr\_core.hr\_CaseAjax().getTemplateFields()", could see that ServiceNow is avoiding  from using javascript .

For now the requirement is whenever a task is created using a template it should have dynamic short description, for non-template tasks user would manually enter the short description.  
Customer has use cases for creating tasks from both Workflow and manually.  

Is there any workaround to this?

## Resolution

  
There are two scenarios here:  
1\. Applying templates using workflows (server side)  
2\. Applying templates using manual HR task creation ( client side)  
  
Templates apply the javascript server side not client side.  
  
Applying templates using workflows (server side) :  
Below javascript will work in this scenario because gs is a server side function.  
javascript: gs.getUserID()  
  
The reason 'javascript: current.parent.number' would not work is because current does not work in templates. Basically there is no handle of current record which applying templates.  
  
Applying templates using manual HR task creation :  
The reason getTemplateFields() function (in hr\_CaseAjax script include) is ignoring fields with javascript is because g\_form does not support.  
  
Having said that, templates might not be able to help in achieving this requirement. So, you might have to do customisation to achieve this, may be using a BR.
