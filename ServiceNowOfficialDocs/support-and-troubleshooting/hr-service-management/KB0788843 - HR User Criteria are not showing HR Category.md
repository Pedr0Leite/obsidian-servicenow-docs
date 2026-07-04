---
title: "HR User Criteria are not showing HR Category"
aliases:
  - KB0788843
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788843
kb_number: KB0788843
last_modified: 2024-04-08
---

## HR User Criteria are not showing HR Category

  

### Issue

User criteria is not allowing HR category to be visible for users.

### Cause

The script within the user criteria uses a function called 'answer' which is not advisable as this is a predefined variable in user criteria.

### Resolution

Change the function name to something other than 'answer' and clearing the instance cache.
