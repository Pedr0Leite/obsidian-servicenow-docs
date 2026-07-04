---
title: "sys_wizard_answer type button doesn't work in change interceptor"
aliases:
  - KB0783543
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783543
kb_number: KB0783543
last_modified: 2024-04-08
---

## sys\_wizard\_answer type button doesn't work in change interceptor

  

### Issue

The sys\_wizard\_answer type button doesn't work in change interceptor, since only one button is created

Go to Madrid or newest release  
Go to Interceptor > Change > Change Request  
[https://xxx.service-now.com/nav\_to.do?uri=sys\_wizard.do?sys\_id=8db4a378c611227401b96457a060e0f4](https://xxx.service-now.com/nav_to.do?uri=sys_wizard.do?sys_id=8db4a378c611227401b96457a060e0f4)  
Go to Answers (sys\_wizard\_answer\_list filter Question name contains Change  
[https://xxx.service-now.com/sys\_wizard\_answer\_list.do?sysparm\_query=question!%3Dd9fce091c61122b701df02c95197cf36%5EORquestion%3DNULL%5EGOTOquestion.nameLIKEchange](https://xxx.service-now.com/sys_wizard_answer_list.do?sysparm_query=question!%3Dd9fce091c61122b701df02c95197cf36%5EORquestion%3DNULL%5EGOTOquestion.nameLIKEchange)  
You can see Direct to Standard Change, Direct to Normal Change and Direct to Emergency Change  
Open each one and changed the Type to Button and Fill the name with the same name.  
Clear the cache  
Go to Interceptor > Change > Change Request  
[https://xxx.service-now.com/nav\_to.do?uri=sys\_wizard.do?sys\_id=8db4a378c611227401b96457a060e0f4](https://xxx.service-now.com/nav_to.do?uri=sys_wizard.do?sys_id=8db4a378c611227401b96457a060e0f4)  
Direct to Normal Change has disappeared  
Go to Change > Create

Only Direct to Emergency Change shows as button, and this is the designed behavior, since a wizard can only have one button, it's typically the execution action of a wizard like "submit".  
  

### Resolution

The problem ticket PRB1369387 was raised for this behavior, but was closed since it's working by design.

However a wizard can only have one button, it's typically the execution action of a wizard like "submit".
