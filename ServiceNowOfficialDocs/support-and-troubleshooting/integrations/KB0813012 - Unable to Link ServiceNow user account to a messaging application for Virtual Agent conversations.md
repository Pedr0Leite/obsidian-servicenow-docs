---
title: "Unable to Link ServiceNow user account to a messaging application for Virtual Agent conversations"
aliases:
  - KB0813012
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813012
kb_number: KB0813012
last_modified: 2024-04-08
---

## Unable to Link ServiceNow user account to a messaging application for Virtual Agent conversations

  

### Issue

Unable to Link ServiceNow user account to a messaging application for Virtual Agent conversations.

### Cause

ServiceNow currently supports the instance URL <instance-name>.service-now.com when linking the accounts.

### Resolution

Currently ServiceNow platform supports only instance URL while linking ServiceNow user account to a messaging application for Virtual Agent conversations. Custom URLs or Proxy URLs while linking from the Messaging Application is not supported.

### Related Links

Example link URL in the messaging application:

https://<instance-name>.service-now.com/challenge.do?sysparm\_provider\_app\_auth\_id=a8a8da5a1b9ac8103a4dbb39cd4bcb7e&sysparm\_provider\_user\_id=c2xhY2s6VDRZTldLWTBaOlVMODlRS0U4Tg&sysparm\_request\_id=RFNOMk1FM&sysparm\_token=Rpe-L\_Y-xo&sysparm\_provider\_user\_name=\_MZ5G\_wFKtoe2Hpg
