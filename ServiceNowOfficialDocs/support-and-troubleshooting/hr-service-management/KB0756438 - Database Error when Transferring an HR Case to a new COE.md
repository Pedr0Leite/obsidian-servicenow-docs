---
title: "Database Error when Transferring an HR Case to a new COE"
aliases:
  - KB0756438
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756438
kb_number: KB0756438
last_modified: 2024-04-07
---

## Database Error when Transferring an HR Case to a new COE

  

### Issue

When transferring an HR Case to a different COE, an error that is generated:  Syntax Error or Access Rule Violation detected by database (You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near...).

### Cause

A customized version of the Transfer Case UI page is causing this issue.

### Resolution

Revert to the out of box version of the 'Transfer Case' UI page to resolve the issue.
