---
title: "Discovery does not populate Serial number on Server records."
aliases:
  - KB0793513
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793513
kb_number: KB0793513
last_modified: 2024-04-08
---

## Issue

Discovery does not populate **Serial number** on Server records.

## Resolution

\* Remove the HP - UX Server pattern from the OOB pre sensor.  
\* https://<<instance>>.service-now.com/sa\_pattern\_prepost\_script.do?sys\_id=59e84c5b9f2322001d753758442e70f3  
\* Create a copy of presensor and add the HP pattern.  
\* Update the script line 175 in OSs - Pre Sensor to use 'related' instead of 'lookup'.

(Or)

\*  Disable Custom Identifier.
