---
title: "How to check of the Mid Sever is up using a Flow"
aliases:
  - KB0831557
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831557
kb_number: KB0831557
last_modified: 2025-01-02
---

## How to check of the Mid Sever is up using a Flow

  

### Summary

How can you use Flow Designer to determine if the Mid Server is up and running?

### Instructions

To determine if the Mid Server is up you can use the table ecc\_agent. If you want to use this in Flow Designer you can define a Record Updated trigger based on this table with a condition: Status changes from Up AND Status changes to Down OR Status changes to Paused. 

Make sure to set the Run Trigger to 'For each unique change'. The default value (Once) will only trigger it initially and any subsequent changes will not be recorded.
