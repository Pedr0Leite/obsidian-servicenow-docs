---
title: "MSSQL  DB on windows pattern fails with the error \"Failed to find library by name: [sys_id_of_pattern]\"
aliases:
  - KB0716298
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716298
kb_number: KB0716298
last_modified: 2024-04-07
---

## MSSQL DB on windows pattern fails with the error "Failed to find library by name: \[sys\_id\_of\_pattern\]"

  

### Issue

# Symptoms

* * *

MSSQL DB on windows pattern fails with the error "Failed to find library by name: \[sys\_id\_of\_pattern\]"

# Release

* * *

London

# Cause

* * *

The shared library "MS SQL Enrich Attribute Library" is inactive by default in London instances.

# Resolution

* * *

1) Navigate to the Module "Discovery Patterns" and find the name "MS SQL Enrich Attribute Library"

2) Check the Active flag

3) Save the pattern
