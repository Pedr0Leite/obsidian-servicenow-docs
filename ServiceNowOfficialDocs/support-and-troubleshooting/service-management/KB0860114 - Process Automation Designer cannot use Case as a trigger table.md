---
title: "Process Automation Designer cannot use Case as a trigger table"
aliases:
  - KB0860114
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860114
kb_number: KB0860114
last_modified: 2024-04-08
---

## Issue

Process Automation Designer cannot use Case as a trigger table

**Steps to Reproduce:**

1.  Switch to Customer Service scope
2.  Open Process automation designer
3.  Create new process
4.  Select a trigger: Define your own conditions for when your process runs  / Record create or update
5.  Set your trigger conditions
6.  Only Incident and Incident Task tables are available

## Resolution

Our product development team have confirmed:  
This is by design. The case table (sn\_customerservice\_case) is available as part of the Playbooks for Customer Service Management plugin.  
  
If you install the above mentioned plugin then you should be able to create process definitions on case.
