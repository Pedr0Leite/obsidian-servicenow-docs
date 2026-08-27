---
title: "How to check when was the last cache flush happened in the instance?"
aliases:
  - KB0815772
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815772
kb_number: KB0815772
last_modified: 2025-01-03
---

## How to check when was the last cache flush happened in the instance?

  

### Summary

Cache is flushed automatically when update sets are committed or when plugins are installed.

This article describes how to check when the cache is cleared in the instance.

### Instructions

The cache.flush date can be seen in the 'ServiceNow Performance' dashboard.

Steps:  
1\. Log in to the instance as an Admin user  
2\. On the home page, select "ServiceNow Performance" dashboard  
3\. Select the Timespan as 30 days  
You can see the Cache.flush events for the instance under "Diagnostic Events"

### Related Links

[https://community.servicenow.com/community?id=community\_blog&sys\_id=81ada2a9dbd0dbc01dcaf3231f961913](https://community.servicenow.com/community?id=community_blog&sys_id=81ada2a9dbd0dbc01dcaf3231f961913)
