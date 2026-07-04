---
title: "HR Create Case throwing {{errorMessage}}"
aliases:
  - KB0862330
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0862330
kb_number: KB0862330
last_modified: 2025-09-03
---

## HR Create Case throwing {{errorMessage}}

  

### Issue

**When creating a New HR Case, the following error is seen.**

![](sys_attachment.do?sys_id=10cb340ddb80f8d066e0a345ca961977)

### Cause

1) After enabling debug and trying to create the case, the following error is seen in debug logs:  
\======  
10:44:50.912 Evaluator: org.mozilla.javascript.EcmaError: Cannot find function setInitialCaseFields in object \[object Object\]. Caused by error in ftp://gsft\_database\_form/sys\_ui\_page.3433fb86eb533200a9e7e26ac106fef2.html.28 at line 15 12: var taskCreateTable = evConfig.taskCreateTable; 13: var taskCreateRecord = new GlideRecord(evConfig.taskCreateTable); 14: taskCreateRecord.initialize(); ==> 15: evConfig.setInitialCaseFields(taskCreateRecord); 16: var taskFields = {}; 17: for (var key in evConfig.taskFields) 18: taskFields\[key\] = evConfig.getFieldObjects(taskCreateRecord, evConfig.taskFields\[key\], true);  
\======

  
2) When the Create Case link from the menu it clicked, it calls the UI Page (case\_Creation):  
https://instancename.service-now.com/nav\_to.do?uri=sys\_ui\_page.do?sys\_id=3433fb86eb533200a9e7e26ac106fef2  
  
Which then calls script includes (hr\_CaseCreation), checked the script includes(hr\_CaseCreation) and the function (**setInitialCaseFields**) seems to be missing as the file has been customised:  
https://instancename.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=687d7d8deb6f3200a9e7e26ac106fee0

### Resolution

  
  
Revert the script and rollback to OOB.
