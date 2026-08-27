---
title: "Failing widget HRM Task Activity GlideRecord.setTableName - empty table name"
aliases:
  - KB0783801
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783801
kb_number: KB0783801
last_modified: 2024-12-23
---

## Failing widget HRM Task Activity GlideRecord.setTableName - empty table name

  

### Issue

When user Pepper Potts is trying to view the "to-dos" section of the Employee Service Center, she is seeing many errors:

-   org.mozilla.javascript.EvaluatorException: GlideRecord.setTableName - empty table name (sys\_script\_include.9998ae7e531322002b76da86a11c0870.script; line 155)
    -   Which references Script Include "hr\_ActivitySetAJAX":
        -   https://instance.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=9998ae7e531322002b76da86a11c0870
    -   Line 155:
        -   gr = new GlideRecord(parentTable);
-   Failing widget: 'HRM Task Activity' (be9a53ee738023002ceb31d7caf6a769) called from: 'To-dos task Line Item' (a4716c8f53d3130030f3ddeeff7b1288)
    -   Failing widget "HRM Task Activity":
        -   https://instance.service-now.com/nav\_to.do?uri=sp\_widget.do?sys\_id=be9a53ee738023002ceb31d7caf6a769
    -   Which is called from widget "To-dos task Line Item":
        -   https://instance.service-now.com/nav\_to.do?uri=sp\_widget.do?sys\_id=a4716c8f53d3130030f3ddeeff7b1288

### Resolution

The behavior described above is now a documented Problem (PRB), PRB1370325.

The workaround for this behavior is to make a small change to Script Include "hr\_ActivitySetAJAX" on line 155:

```
if (!parentTable || !parentId)return null;
```

By making the above modification to the Script Include, a validation check (which was not previously present) is put in place for when a user is assigned a task with a parent record they cannot read.
