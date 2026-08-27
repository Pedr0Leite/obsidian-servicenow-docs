---
title: "Survey Issue : Order for the questions are not working as expected"
aliases:
  - KB0957927
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957927
kb_number: KB0957927
last_modified: 2026-06-24
---

## Survey Issue : Order for the questions are not working as expected

  

### Issue

You have configured a survey 'Request Fulfillment Satisfaction Survey' and order is such that Q1 and Q2 show first and additional follow-up questions should be displayed after Q2. However, this is not working as expected in the portal. You have checked and noticed that this issue is with OOTB portal page as well.

### Release

All

### Cause

Development have confirmed that as per OOB behaviour the dependent question comes right after the question it is dependent on.  
The reason for this behaviour is because when a Q depends on another, to preserve the context we'd show all the dependent Qs immediately.  
You can change the order among the dependent Qs if there are more than 1.  
This is a feature and not a bug and unfortunately there is no workaround that could alter the standard behavior.

### Resolution

  
The behavior reported is the standard design.  
  
As a suggestion please consider raising an Enhancement/Idea if you would like to suggest this to our Product Management team to implement this in a future release.  
Idea Management for customer enhancement requests  
https://support.servicenow.com/kb?id=kb\_article\_view\_popup&sysparm\_article=KB0755878
