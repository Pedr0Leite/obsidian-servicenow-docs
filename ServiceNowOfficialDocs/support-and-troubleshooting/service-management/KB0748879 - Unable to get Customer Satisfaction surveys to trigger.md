---
title: "Unable to get Customer Satisfaction surveys to trigger"
aliases:
  - KB0748879
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748879
kb_number: KB0748879
last_modified: 2024-04-07
---

## Unable to get Customer Satisfaction surveys to trigger

  

### Issue

The survey are not triggered. Survey issue in the domain separated instance. 

### Cause

When a survey trigger condition is created to trigger a survey then a Business rule "Auto Assessment business rule" is created by the system.  
The Business rule is created in the same domain in which the survey is created.  
As the business rule is not accessible by other domains, so the survey is not triggered.

### Resolution

You can create the Survey and Trigger condition in Global or Top domain where all domain has access to it, this will help to trigger the survey from any lower domains.
