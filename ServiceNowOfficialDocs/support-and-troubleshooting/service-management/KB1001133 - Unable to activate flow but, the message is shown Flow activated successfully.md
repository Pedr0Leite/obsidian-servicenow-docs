---
title: "Unable to activate flow but, the message is shown: Flow activated successfully"
aliases:
  - KB1001133
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1001133
kb_number: KB1001133
last_modified: 2025-09-03
---

## Unable to activate flow but, the message is shown: Flow activated successfully

  

### Issue

Unable to activate flow using the Activate button available in the. designer but, the message is shown: Flow activated successfully and the activate button is still showing.

### Cause

It's a corner case with Error stage usage in flows. Flow designer does not allow more than one error stage inside an if block.  
But if the flow developer manages to achieve this ( say add a nested if and move the steps under inside if to outside if ) - the issue of "unable to activate flow even if flow activated successfully message shown " issue occurs.

![](sys_attachment.do?sys_id=2e534e57db1c8510fd8d2b6913961979)

### Resolution

Removing the extra error stage in the if block, resolves the issue.
