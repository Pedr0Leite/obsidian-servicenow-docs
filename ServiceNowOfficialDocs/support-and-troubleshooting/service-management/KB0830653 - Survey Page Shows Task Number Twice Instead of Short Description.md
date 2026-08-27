---
title: "Survey Page Shows Task Number Twice Instead of Short Description"
aliases:
  - KB0830653
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830653
kb_number: KB0830653
last_modified: 2025-05-13
---

## Survey Page Shows Task Number Twice Instead of Short Description

  

### Issue

Surveys generated display the task (REQ, incident, case etc.) number twice. The requirement is to show the number and the short description.

### Resolution

There needs to be an entry in the sys\_ui\_title table. Add an entry for the table you are generating surveys on and the short description field. If the table doesn't have an entry for the trigger table and the field that should be used as the title, it will return the record number instead.
