---
title: " AWS Config/SNS service does not integrate successfully with ServiceNow"
aliases:
  - KB0693962
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693962
kb_number: KB0693962
last_modified: 2026-05-19
---

## AWS Config/SNS service does not integrate successfully with ServiceNow

  

### Issue

On the AWS console, the SNS subscription shows "**pending confirmation**" status. 

### Release

Any

### Resolution

1.  Make sure that the required AWS SNS integration user roles **sn\_cmp.cloud\_event\_integration** and **discovery\_admin** are added to the ServiceNow user used in this integration.
2.  After creating the topic and subscription, check the **sn\_cmp\_cloud\_event** table and locate the received event about AWS subscription confirmation URL.
3.  Use the confirmation URL on AWS SNS Topic subscription '**Confirm subscription**'. ServiceNow will start to receive AWS cloud events into the **sn\_cmp\_cloud\_event** table as expected.
