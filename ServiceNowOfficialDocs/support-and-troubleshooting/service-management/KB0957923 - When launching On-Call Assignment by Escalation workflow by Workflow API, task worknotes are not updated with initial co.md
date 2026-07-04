---
title: "When launching On-Call: Assignment by Escalation workflow by Workflow API, task worknotes are not updated with initial communication or escalation path"
aliases:
  - KB0957923
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957923
kb_number: KB0957923
last_modified: 2026-06-24
---

## When launching On-Call: Assignment by Escalation workflow by Workflow API, task worknotes are not updated with initial communication or escalation path

  

### Issue

When launching "On-Call: Assign by Remediation Task" workflow by Workflow API, task worknotes are not updated with initial communication or escalation path.  
Expected behavior is for task worknotes to be updated initially with the entire escalation path from the On-call schedule of the group and also with each notify communication. While the initial worknotes are not updated with the Escalation path or initial communication, subsequent communications ARE added to the worknotes.  
  
for e.g. on Incident record INC5505034 where it works you see the below worknote entry  
Sent communication to User A (by Voice)  
  
This incident escalation is in progress using the following escalation plan:  
Escalate in 0 minutes to User A  
Escalate in 1 minutes to User A  
Escalate in 2 minutes to User B  
Escalate in 3 minutes to User B

  
On Remediation Task TASK0040803, you see only the reminder worknote entries.

### Release

All

### Cause

This occurs because the Custom Code which triggers the Workflow is running **after** update of the Record which prevents the updates being made as expected by the Workflow.

### Resolution

To resolve this issue update the logic of the custom code to ensure the Workflow is being triggered **before update** of the record.
