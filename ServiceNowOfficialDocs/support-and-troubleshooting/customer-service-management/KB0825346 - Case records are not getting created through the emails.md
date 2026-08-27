---
title: "Case records are not getting created through the emails"
aliases:
  - KB0825346
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0825346
kb_number: KB0825346
last_modified: 2025-07-01
---

## Case records are not getting created through the emails

  

### Issue

From the email log, the Case records are not getting created in the Instance through emails-  
https://<your-instance>.service-now.com/sys\_email\_list.do

#### Steps to reproduce:

1.  Hop into the instance.
2.  Navigate to https://<your-instance>.service-now.com/sys\_email\_list.do
3.  In the email log, you will see the case number present like - "Processed 'IS: Create/Update Customer Case', created sn\_customerservice\_case :CS#####"
4.  Search for the case in the sn\_customerservice\_case table.
5.  The case is not found

### Release

New York

### Cause

 The out of the box Business Rule - **'Prevent Invalid Case Creation'** is preventing the Case creation due to the custom Script Include which is used in the Email Inbound Action.

### Resolution

Advised fixing the customized Script Include while leaving the out of the box Business Rule "Prevent Invalid Case Creation" alone.

### Related Links

[Troubleshooting email notification failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538135)
