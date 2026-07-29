---
title: "Syntax Error (Unknown column 'sys_user0.email' in 'where clause') appearing when trying to search in a reference field on a record producer"
aliases:
  - KB0687606
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687606
kb_number: KB0687606
last_modified: 2024-04-07
---

## Syntax Error (Unknown column 'sys\_user0.email' in 'where clause') appearing when trying to search in a reference field on a record producer

  

### Issue

# Symptoms

* * *

Syntax Error (Unknown column 'sys\_user0.email' in 'where clause') appearing when trying to search in a reference field on a record producer.

# Release

* * *

Jakarta Patch 6a+

# Cause

* * *

Syntax-related search errors can be caused by improper table references.

If a variable of <type\_x> references a field of <type\_y>, there is a large chance that the search will result in an error.

# Resolution

* * *

The attributes on the variable must reference valid columns on the referenced table.

Failure to do so will yield the aforementioned syntax errors.

#
