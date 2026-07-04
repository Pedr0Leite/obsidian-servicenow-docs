---
title: "Software model result not present for not licensable product type"
aliases:
  - KB0829843
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829843
kb_number: KB0829843
last_modified: 2024-04-08
---

## Issue

Once I run reconciliation, I do not see product google chrome listed in the results list. Why is this the case?

## Resolution

When we run reconciliation we look for those product that have type licensable. For not licensable product type we do not create reconciliation result or product result/software model result.

  

We do have a property that can help in automatic creation of software model for non licensable product type but this is just to create software model. It still does not get considered in reconciliation.

[https://docs.servicenow.com/csh?topicname=c\_SAMReconciliation.html&version=latest](https://docs.servicenow.com/csh?topicname=c_SAMReconciliation.html&version=latest)   
"You can also set the com.snc.samp.automaticsmcreation property to have a software model created automatically for not-licensable products, if desired"
