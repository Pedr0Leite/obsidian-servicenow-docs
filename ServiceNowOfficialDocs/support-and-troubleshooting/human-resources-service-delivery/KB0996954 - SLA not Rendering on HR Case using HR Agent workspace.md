---
title: "SLA not Rendering on HR Case using HR Agent workspace"
aliases:
  - KB0996954
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996954
kb_number: KB0996954
last_modified: 2024-08-28
---

## SLA not Rendering on HR Case using HR Agent workspace

  

### Issue

HR TASK SLA are not getting display on HR Case records using HR agent workspace.  
  
  

### Resolution

Looking at **sys\_ui\_list** table in OOB instance, we have observed there are three records for "task\_sla" table with "Workspace" view. Two of which have "incident" and "change\_request" set as parent respectively. Third has parent field empty.

On your instance, we noticed only two records, both of the records had parent field set ("incident" and "change\_request"). A third record with empty parent field, similar to OOB instance, was missing.

Creating a new list with table field set to "task\_sla", view field set to "Workspace", and parent field set to empty value, and adding List Elements to the newly created list seems to have fixed the issue. The list elements added to the list show up in the Task SLAs related list in the agent workspace.
