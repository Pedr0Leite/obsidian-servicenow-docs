---
title: "Cornerstone Spoke Import Jobs are stuck in either \"Loaded\" or \"Running\" State"
aliases:
  - KB1705622
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1705622
kb_number: KB1705622
last_modified: 2024-10-24
---

## Issue

After implementing the Cornerstone Spoke and configuring it as per the [ServiceNow Documentation](https://docs.servicenow.com/bundle/xanadu-integrate-applications/page/administer/integrationhub-store-spokes/task/setup-cornerstone.html), you may see that the import jobs are getting classified as either in a state of "loaded" or "running", but never progress afterwards.

## Resolution

Please implement the background script recommendation found in the KB article below and noted this process the imports and transformed as expected:  
  
[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0781666](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781666)

Please ensure that in the script, the staging table name is updated to the target table and that the query for the status of the import is added as needed.
