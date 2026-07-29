---
title: "Default Data Refresh rules"
aliases:
  - KB0696913
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696913
kb_number: KB0696913
last_modified: 2025-04-07
---

## Default Data Refresh rules

  

### Issue

# Overview

* * *

If there are no data refresh rules defined, the updates to (stale) CIs would be made per the existing data source precedence rules and reconciliation rules, if any. 

# \[Subject\]

* * *

Default behavior when no data refresh rules are defined explicitly. 

# Additional Information

* * *

For example, you have a datasource precedence rule for the SCCM datasource with order=100 and another datasource precedence rule for ServiceNow as datasource with order=200. For a CI, if no updates have been made to it by SCCM, say in over 20 days(by when it has met the criteria for stale CI), you can create a data refresh rule to ensure that ServiceNow datasource updates it, despite the ServiceNow data source precedence rule having a lower order(200).   
  
Therefore, you can use data refresh rules to determine if a CI is stale for a specific data source. Such CIs can then be updated by a lower-priority authorized data source(serviceNow data source from the above example). If you have no data refresh rules defined, the updates to CIs would be as per your data source precedence rules' order only.
