---
title: "Cannot select emal [sys_email] and other system tables in Flow Designer"
aliases:
  - KB0953503
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953503
kb_number: KB0953503
last_modified: 2025-07-22
---

## Cannot select emal \[sys\_email\] and other system tables in Flow Designer

  

### Issue

Cannot select emal \[sys\_email\] and other system tables in Flow Designer

### Cause

Table is not in the allowed tables 

### Resolution

1\. Go to All Properties

2\. Search for the property sn\_flow\_designer.allowed\_system\_tables

3\. Add the system table you want to select in Flow Designer

4\. Save and relaunch or re-login if you still cannot see the tables

### Related Links

Note: Even though the table has been added to the property, it can only be utilized in an action and not in a trigger.
