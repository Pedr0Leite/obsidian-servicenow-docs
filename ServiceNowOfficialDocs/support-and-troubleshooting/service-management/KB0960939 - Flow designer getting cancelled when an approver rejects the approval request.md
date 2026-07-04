---
title: "Flow designer getting cancelled when an approver rejects the approval request"
aliases:
  - KB0960939
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960939
kb_number: KB0960939
last_modified: 2026-03-05
---

## Flow designer getting cancelled when an approver rejects the approval request

  

### Issue

If a flow has an approval action in it then flows are being canceled when an approver rejects the approval request.

### Cause

When the approval is Rejected, the stage of the RITM is getting updated as "Request Cancelled".

There is an OOTB business rule "cancel flow on request cancelled" running on the sc\_req\_item table, which checks the stage of the RITM and cancels the associated flow designer if the stage of the RITM is "Request Cancelled".

https://instance\_name.service-now.com/sys\_script.do?sys\_id=062422410f2100108af26b198b767eb0

### Resolution

This is expected behavior.
