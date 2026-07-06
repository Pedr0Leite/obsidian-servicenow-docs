---
title: "Alerts processed by events do not have Task field populated"
aliases:
  - KB0756803
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756803
kb_number: KB0756803
last_modified: 2025-01-03
---

## Issue

For a valid event with working event rule, an alert gets generated and on its form, we would not be able to see a task being populated though there is an incident created by the Create Task(Legacy) workflow triggered as a result of Alert Management Rule.

![](/sys_attachment.do?sys_id=469e91f4db41b41066e0a345ca961907)

## Resolution

To identify and resolve such a scenario-

1.  Create a debug business rule that can print a stack trace against the em\_event table. The KB [KB0683765](https://support.servicenow.com/kb_view.do?sysparm_article=KB0683765 "KB0683765") can be used to do so.
2.  From a sample event that is relevant, generate an alert. 
3.  Once we reproduce the scenario, in the stack trace we would see this exception- 'Unique Key violation detected by database'
4.  Please check all the script includes that were called as a part of the session and were recorded in the stack trace and check to see if there are any 'before' business rules which have a **current.update()** included int he script. 
5.  If you find one, please suggest either removing the **current.update()** or updating the business rule to be 'after'.
6.  If the stack trace doesn't reveal the observations above, the issue has to be investigated further cause it can be a different influencer that is causing the issue.
