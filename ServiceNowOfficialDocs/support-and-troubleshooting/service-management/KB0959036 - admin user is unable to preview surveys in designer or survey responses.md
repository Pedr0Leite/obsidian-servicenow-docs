---
title: "admin user is unable to preview surveys in designer or survey responses"
aliases:
  - KB0959036
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0959036
kb_number: KB0959036
last_modified: 2024-03-10
---

## admin user is unable to preview surveys in designer or survey responses

  

### Issue

-   admin account is unable to preview surveys in designer or survey responses  
    
-   questions are not viewable

### Cause

-   in my case, there was a custom business rule on table \[asmt\_assessment\_instance\_question\] updating the source\_id with the instance.trigger\_id
-   this caused issues with the sys UI page assessment\_task2.do from reading the question data
