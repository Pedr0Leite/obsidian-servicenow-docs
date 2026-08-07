---
title: "Unique Key violation detected by database while trying to insert the record in the Enhancement table"
aliases:
  - KB0696074
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696074
kb_number: KB0696074
last_modified: 2024-04-07
---

## Unique Key violation detected by database while trying to insert the record in the Enhancement table

  

### Issue

# Symptoms

* * *

Unique Key violation detected by database while trying to insert the record in the Enhancement table

# Release

* * *

Kingston and earlier

# Cause

* * *

The issue is caused due to the business rule that runs on the Approval table

# Resolution

* * *

There is a business rule that runs on the Approval table, which is creating a new record on the "Internal Systems Request" (custom table) table (when approval records are added from the workflow) and therefore the "sys\_id" that was allocated to the "Enhancement request" record gets assigned to the "Internal Systems Request" record.

Therefore when we try to insert the "Enhancement Request" record with the same sys\_id (which has been assigned to Internal systems request record), we get the "Unique key violation" error.
