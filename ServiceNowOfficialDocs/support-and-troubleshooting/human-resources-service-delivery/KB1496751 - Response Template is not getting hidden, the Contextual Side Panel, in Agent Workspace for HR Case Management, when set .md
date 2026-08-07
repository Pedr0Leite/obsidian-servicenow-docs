---
title: "\"Response Template\" is not getting hidden, the Contextual Side Panel\", in \"Agent Workspace for HR Case Management\", when set to \"Inactive\" through UI Builder"
aliases:
  - KB1496751
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1496751
kb_number: KB1496751
last_modified: 2026-05-01
---

## "Response Template" is not getting hidden, the Contextual Side Panel", in "Agent Workspace for HR Case Management", when set to "Inactive" through UI Builder

  

### Issue

How to hide the Contextual Side Panel in the process of configuring the HR Configurable Agent Workspace Agent Workspace for HR Case Management).

1.  Response Templates.
2.  Fulfillment Instructions.
3.  Checklists  
      
    

### Release

Utah Patch 4

### Resolution

  
Below are the steps that needs to be performed to hide the contextual side panel :-

1.  Find the record page getting loaded. i.e. Case SRP : below:  
    [https://instancename.service-now.com/now/builder/ui/edit/experience/8ad40be90fe120102208555db4767e7b/ca1b8b0c0ff120102208555db4767e23/6103b475eb3011106eb96bf3a252282b](https://instancename.service-now.com/now/builder/ui/edit/experience/8ad40be90fe120102208555db4767e7b/ca1b8b0c0ff120102208555db4767e23/6103b475eb3011106eb96bf3a252282b)
2.  Identify the side panel tabs / components and click on the required component e.g. Response Template.
3.  Click on Go to tabs.
4.  If you have already configured a data resource based on which this component will be hidden / visible -  "!@data.hrUiCtrl.contextualSidebar.showResponseTemplates".
5.  We can click on the Hide tab > Pencil icon to use static input > and toggle to hide.

  
![](/sys_attachment.do?sys_id=f2e004da47680754b7832920326d430c "Screenshot 2023-08-03 at 8.44.01 AM.png")
