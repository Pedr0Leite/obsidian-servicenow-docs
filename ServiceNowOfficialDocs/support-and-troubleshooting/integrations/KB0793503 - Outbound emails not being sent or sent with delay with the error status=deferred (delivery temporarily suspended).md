---
title: "Outbound emails not being sent or sent with delay with the error \"status=deferred (delivery temporarily suspended)\""
aliases:
  - KB0793503
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793503
kb_number: KB0793503
last_modified: 2026-05-01
---

## Outbound emails not being sent or sent with delay with the error "status=deferred (delivery temporarily suspended)"

  

### Issue

You may notice a delay in delivery to certain users or emails not delivered at all.

In the logs we can notice the following message: 

status=deferred (delivery temporarily suspended: host xxxx.net\[xxxxxxxxx\] refused to talk to me: 550 Error  
  
  

### Release

All

### Cause

ServiceNow IP addresses are not allow-listed in the affected customer infrastructure.

### Resolution

Follow the instructions in the article [Enabling email delivery using SPF records to allow SN mail servers](https://support.servicenow.com/kb_view.do?sysparm_article=KB0535456 "Enabling email delivery using SPF records to allow SN mail servers") to allow-list ServiceNow IPs in your mail servers.
