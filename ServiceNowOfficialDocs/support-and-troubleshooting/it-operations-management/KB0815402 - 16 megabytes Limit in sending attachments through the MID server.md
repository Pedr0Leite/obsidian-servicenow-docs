---
title: "16 megabytes Limit in sending attachments through the MID server"
aliases:
  - KB0815402
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815402
kb_number: KB0815402
last_modified: 2025-01-22
---

## Issue

1\. The ECC queue payload field is of type string.  
  
2\. From the documentation below we can see that ServiceNow String data type corresponds MYSQL MEDIUMTEXT type. See  documentation here [KB0765460](https://support.servicenow.com/kb_view.do?sysparm_article=KB0765460 "KB0765460").

## Resolution

Since the limit on the ECC queue payload field is 16MB, the customer needs to explore other options of sending attachments such as using the attachment API.

For more information on attachment API see documentation here [KB0773993](https://support.servicenow.com/kb_view.do?sysparm_article=KB0773993 "KB0773993").
