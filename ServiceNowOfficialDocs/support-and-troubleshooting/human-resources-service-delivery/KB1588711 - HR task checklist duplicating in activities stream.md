---
title: "HR task checklist duplicating in activities stream"
aliases:
  - KB1588711
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1588711
kb_number: KB1588711
last_modified: 2024-01-24
---

## Issue

When a checklist on a particular task is generated, it is duplicating the initial "Checklist created" and "Checklist item added" in the activities stream, which then gets added to the HR case in the same way. This is complicating the activities stream for users.

## Resolution

\- As a potential solution, we have the option to either deactivate the business rule or modify the field being updated. To make this modification, we can change line 23 from \`grTask.work\_notes\` by substituting your desired field for \`work\_notes\` inside the "Add worknote for checklist item CRUD" Business Rule.  
  
PLEASE NOTE: Since this is an out-of-the-box (OOB) business rule, any modifications made to this rule may be overwritten during an upgrade.
