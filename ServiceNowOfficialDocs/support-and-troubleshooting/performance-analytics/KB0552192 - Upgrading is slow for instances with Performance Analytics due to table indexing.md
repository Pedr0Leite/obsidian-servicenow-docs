---
title: "Upgrading is slow for instances with Performance Analytics due to table indexing"
aliases:
  - KB0552192
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552192
kb_number: KB0552192
last_modified: 2024-04-07
---

## Upgrading is slow for instances with Performance Analytics due to table indexing

  

### Issue

Upgrading is slow for instances with Performance Analytics due to table indexing

Problem

* * *

If Performance Analytics is enabled on an instance, and there are a very large number of records on the Scores \[pa\_scores\] and Snapshots \[pa\_snapshots\] tables, upgrading to Fuji Patch 7, Eureka Patch 12, or later, or from Geneva Patch 1, 2, or 3, upgrading takes a very long time.

Symptoms

* * *

When upgrading from a version prior to Fuji Patch 7 or Eureka Patch 12 or from Geneva Patch 1, 2 or 3, the upgrade takes an excessively long time to complete. Your system may take more or less time to complete the operation and it is not possible to predict how long it will take for your system to add the indexes. However, we have seen examples of 25 million records taking 34 hours to add the indexes, 5 million records taking 3 hours, etc.

Cause

* * *

With Fuji Patch 7, Eureka Patch 12 and Geneva Patch 4, the Scores \[pa\_scores\] and Snapshots \[pa\_snapshots\] tables are indexed. Adding an index to these tables when there are a large number of records may take a long time to complete.

  
Resolution

* * *

Before upgrading, add the following indexes to the Scores \[pa\_scores\] and Snapshots \[pa\_snapshots\] tables during non-business hours to avoid performance impact:

-   pa\_snapshots(sys\_created\_on,start\_at)
-   pa\_scores(sys created on, start\_at)

For instances on Fuji or later, see [Create a table index](https://docs.servicenow.com/csh?topicname=t_CreateCustomIndex.html&version=latest "Create a table index") in the product documentation. For instances on a release prior to Fuji, you can contact ServiceNow customer support to request the indexes.
