---
title: "On Easy import large 'Integer' values (more than 10 digits) are saved as 2,147,483,647 in the staging table"
aliases:
  - KB0745402
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745402
kb_number: KB0745402
last_modified: 2024-04-07
---

## On Easy import large 'Integer' values (more than 10 digits) are saved as 2,147,483,647 in the staging table

  

### Issue

# Symptoms

* * *

When you try to import a value (e.g.: 9999999999) more than 10 in the integer fields via Easy import, you may observe that the values is changing to 2,147,483,647  

# Cause

* * *

This is the limitation on the platform due to the limits for integers on SQL https://dev.mysql.com/doc/refman/8.0/en/integer-types.html

# Resolution

* * *

You have to change the type of the field from integer to string in staging table. Also validate the mapping in the transformation map are correct.
