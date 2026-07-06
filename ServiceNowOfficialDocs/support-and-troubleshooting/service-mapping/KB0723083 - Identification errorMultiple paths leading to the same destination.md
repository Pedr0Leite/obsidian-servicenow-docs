---
title: "Identification error:\"Multiple paths leading to the same destination\""
aliases:
  - KB0723083
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723083
kb_number: KB0723083
last_modified: 2024-04-07
---

## Identification error:"Multiple paths leading to the same destination"

  

### Issue

# Symptoms

* * *

Service mapping fails with the following identification error

\*\*\*

In case the discovered CI is included CI (such as Tomcat WAR) check if there are multiple records with name 'Contains::Contained by' in cmdb\_rel\_type table.

Multiple paths leading to the same destination: \[class:cmdb\_ci\_db\_db2\_instance, sys\_id:d58885badbc8e70005cb86171b961998\] -> \[class:cmdb\_ci\_aix\_server, sys\_id:67ab75b81333f6407f4abf304244b068\]

# Release

* * *

All releases

# Cause

* * *

This error is thrown when there is an application that has a duplicate relationship with the same server.

For example: Multiple paths leading to the same destination: \[class:cmdb\_ci\_db\_db2\_instance, sys\_id:d58885badbc8e70005cb86171b961998\] -> \[class:cmdb\_ci\_aix\_server, sys\_id:67ab75b81333f6407f4abf304244b068\]

In the above case, DB2 instance has multiple "Runs on::Runs" relationships with the same AIX server that is hosted on causing Identification engine to fail.

# Resolution

* * *

Navigate to cmdb\_rel\_ci table and see if there are duplicate relationships of the same type to a parent.(ex: DB2->server), Please remove duplicate relationship and re-run the discovery.
