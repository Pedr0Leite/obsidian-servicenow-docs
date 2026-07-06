---
title: "Service mapping error on creation of any business service:  Failed to match endpoint of type: cmdb_ci_endpoint_http, please check the relevant identifier rules"
aliases:
  - KB0720802
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720802
kb_number: KB0720802
last_modified: 2024-04-07
---

## Issue

Service mapping error on creation of any business service of any entry point type.: Failed to match endpoint of type: cmdb\_ci\_endpoint\_http, please check the relevant identifier rules.

![](/sys_attachment.do?sys_id=f58da4e2db82b450e515c2230596193e)

## Resolution

Import the missing Service watch discovery data source from another OOTB instance into the choice list.  
To check the list of data sources, navigate to System Definition > Choice Lists. Filter the table by Element=discovery\_source and Table=cmdb\_ci.   
Make sure that the Service Watch data source exists in the list, and that its Inactive value is set to false.
