---
title: "Field changes to a table are not getting captured in the audit table during imports, even though auditing has been enabled for that table"
aliases:
  - KB0791674
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791674
kb_number: KB0791674
last_modified: 2025-01-22
---

## Issue

You followed the steps in [Enable Auditing for a Table](https://docs.servicenow.com/csh?topicname=t_EnableAuditingForATable.html&version=latest "Enable Auditing for a Table") and field changes are captured in the system audit for any changes done through the UI. However, any changes during imports are not captured in the system audit. 

## Resolution

The changes in the fields will be captured in the audit when "Run Business Rules" is checked.
