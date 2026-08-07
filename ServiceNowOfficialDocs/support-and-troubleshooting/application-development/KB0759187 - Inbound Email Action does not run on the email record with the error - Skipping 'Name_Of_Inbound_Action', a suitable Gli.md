---
title: "Inbound Email Action does not run on the email record with the error - Skipping 'Name_Of_Inbound_Action', a suitable GlideRecord not found"
aliases:
  - KB0759187
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759187
kb_number: KB0759187
last_modified: 2026-07-02
---

## Inbound Email Action does not run on the email record with the error - Skipping 'Name\_Of\_Inbound\_Action', a suitable GlideRecord not found

  

### Issue

When an email is received, and it is expected that an inbound email action runs - it does not run against the email. The log entry in the email logs has the following message - 

Skipping 'Name\_Of\_Inbound\_Action', a suitable GlideRecord not found

### Cause

This happens when the target table field on the inbound action is blank. The inbound email action is unable to associate any GlideRecord to run the inbound email action against. If there is no target table, the inbound email action will not be able to find current object type. This will lead to the error being shown in the email logs. 

### Resolution

It is recommended that the target table field of the inbound action record should have a value.

### Related Links

[Inbound Email Action Target Table](https://support.servicenow.com/kb_view.do?sysparm_article=KB0535511 "Inbound Email Action Target Table")
