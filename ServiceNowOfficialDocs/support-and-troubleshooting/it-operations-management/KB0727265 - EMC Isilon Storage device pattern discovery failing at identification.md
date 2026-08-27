---
title: "EMC Isilon Storage device pattern discovery failing at identification"
aliases:
  - KB0727265
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727265
kb_number: KB0727265
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Pattern Discovery of EMC Isilon Storage Server CI fails with "Insertion failed with error identification\_engine <date/time> Error identification\_engine : MISSING\_DEPENDENCY In payload...

# Release

* * *

London Patch 4, Hot Fix 2

# Environment

* * *

EMC Isilon

# Cause

* * *

Discovery EMC Islong Storage Server CI where one of the Storage Node Elements (cmdb\_ci\_storage\_node\_element) and its IP address is not populated

# Resolution

* * *

This is avaialbe for customer who installed the EMC Isilon pattern available through ServiceNow store. It is supported by ServiceNow pattern team. Even though Storage Node Elements (cmdb\_ci\_storage\_node\_element) device ip\_address was not populated, rather than removing it, the pattern was modified to keep the device and all devices related to it (disks and network\_adapter). Look up PRB to get fixed pattern.
