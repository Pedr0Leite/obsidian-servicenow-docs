---
title: "HR 'Create Case' is not available for some users"
aliases:
  - KB2305222
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2305222
kb_number: KB2305222
last_modified: 2025-09-03
---

## HR 'Create Case' is not available for some users

  

### Issue

Users are encountering an issue where the 'Create Case' button is greyed out and non-functional in the HR Agent workspace.   
  

![HR case create](/sys_attachment.do?sys_id=876741dd473eaad0f64de825126d435a "HR case create")

### Symptoms

'Create case' button is grey or not clickable.

### Release

Yokohama

### Cause

Users default view does not contain work\_notes field. This is configured in the Case creation configuration record out of box.

### Resolution

1\. Identify the affected users and the type of cases they are unable to create.  
2\. Check the current view settings for the users (ex: in platform view), specifically for the HR case and COE tables related to the issue.  
3\. Change the view setting for the affected users from 'Service Portal' to 'Default view' for the relevant case tables (sn\_hr\_core\_case for HR cases and sn\_hr\_er\_case for ER cases). Alternatively, the work\_notes field can be added to the view they are using.  
4\. Verify that the 'Work notes' field is now visible on the form when attempting to create a case in the HR workspace.  
5\. Test the creation of both HR and ER cases to ensure the issue has been resolved.
