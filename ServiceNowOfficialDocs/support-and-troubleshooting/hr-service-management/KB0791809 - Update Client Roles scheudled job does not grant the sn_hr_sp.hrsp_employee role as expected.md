---
title: "Update Client Roles scheudled job does not grant the sn_hr_sp.hrsp_employee role as expected"
aliases:
  - KB0791809
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791809
kb_number: KB0791809
last_modified: 2024-04-08
---

## Update Client Roles scheudled job does not grant the sn\_hr\_sp.hrsp\_employee role as expected

  

### Issue

The Client Role Assignment Rules are not granting the sn\_hr\_sp.hrsp\_employee role as expected when a new HR Profile is created.

### Cause

The 'Update Client Roles' sysauto\_script is responsible granting the expected roles. Based on the query that runs in the script we should process HR Profiles where employment start date is today, after today or employment end date was yesterday. The sysauto\_script runs daily; however, the Workday integration runs daily after the update client roles which causes the HR Profile query to not find newly created HR Profiles if the employee start date was the same as the import date.

### Resolution

Ensure that the workday integration runs prior to the 'Update Client Roles' sysauto\_script and that they run on the same calendar day.
