---
title: "Parallel Approvals in Flow Designer"
aliases:
  - KB0964016
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0964016
kb_number: KB0964016
last_modified: 2025-07-21
---

## Parallel Approvals in Flow Designer

  

There are times when we need to do parallel approvals on the same record, but this isn't supported within Flow Designer.  The typical pattern instead is to create a subtask and create approvals on the subtask.

To do this:

1.  Add Do the following in Parallel Flow Logic
2.  Create a subtask, by adding Create Task to each branch (Create Catalog Task for Service Catalog flows)
3.  Be sure the Wait Checkbox is unchecked 
4.  Add Ask For Approval to each branch and use the Task record created in (2) as the record for approval
5.  You may want some logic to close the subtasks once approved

![Parallel Approval](sys_attachment.do?sys_id=9e2be7d89754229024a7739c1253aff3 "Parallel Approval")
