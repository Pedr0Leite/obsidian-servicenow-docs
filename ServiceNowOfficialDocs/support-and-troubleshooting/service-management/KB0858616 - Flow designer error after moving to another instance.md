---
title: "Flow designer error after moving to another instance"
aliases:
  - KB0858616
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858616
kb_number: KB0858616
last_modified: 2025-03-17
---

## Flow designer error after moving to another instance

  

### Issue

After the flow is migrated from one instance to another through update sets, on opening the flow below error message is received on the destination instance:

  

![](sys_attachment.do?sys_id=88187881db04b4d0b55f0b55ca961920)

### Cause

The sys\_id mentioned in the error message, This is of a custom action created in the source instance and the action was not migrated to the destination beforehand and the flow was migrated directly.

For the error message "Action Type Definition with Id of <sys\_id> is missing (order: 2)", the issue is with the action not present in the table sys\_hub\_action\_type\_snapshot and sys\_hub\_action\_instance\_list in destination instance.

https://<instance\_name>/sys\_hub\_action\_type\_snapshot\_list.do

https://<instance\_name>/sys\_hub\_action\_instance\_list.do

### Resolution

The issue is with the custom action not captured in the update set to migrate because of which the error is received. Please recreate the action and capture it on a update set and then migrate it.

While migrating the flow please keep in mind that all the relevant details of the flow are migrated in the single update set so there is no discrepancy of any configuration on the flow.
