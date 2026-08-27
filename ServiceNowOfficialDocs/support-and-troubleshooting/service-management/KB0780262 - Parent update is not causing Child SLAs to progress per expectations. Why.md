---
title: "Parent update is not causing Child SLAs to progress per expectations. Why?"
aliases:
  - KB0780262
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780262
kb_number: KB0780262
last_modified: 2024-04-08
---

## Parent update is not causing Child SLAs to progress per expectations. Why?

  

### Issue

The user had a parent incident with over 150 child incidents. On about 35 of the child incidents, the task\_sla on the child incident should have progressed from a Stage value of "In progress" to "Paused", but this did not happen. The user wanted to know why.

### Resolution

After a lengthy investigation, it was found that the behavior was a direct result of two custom Business Rules' order of execution.

Both custom Business Rules were running at Order value "100". The user was instructed to change custom Business Rule 'A' to an Order of "200", and custom Business Rule 'B' to an Order of "100".  
  
Making the above change solved the issue for the user.
