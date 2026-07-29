---
title: "MID Server issue: Unable to subscribe to AMB channel: /mid/server/c10a30efdb3f7f0094ababf34a9619bf"
aliases:
  - KB0779124
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779124
kb_number: KB0779124
last_modified: 2024-04-08
---

## MID Server issue: Unable to subscribe to AMB channel: /mid/server/c10a30efdb3f7f0094ababf34a9619bf

  

### Issue

MID Server Issue : Unable to subscribe to AMB channel: /mid/server/c10a30efdb3f7f0094ababf34a9619bf

Under the MID Server -> MID Server Issues

We will see the following entry with the count increasing.

MID Server Issue : Unable to subscribe to AMB channel: /mid/server/c10a30efdb3f7f0094ababf34a9619bf

From the Agent Log.

09/18/19 00:38:36 (095) AMBClientProvider WARNING \*\*\* WARNING \*\*\* Unable to subscribe to AMB channel: /mid/server/c10a30efdb3f7f0094ababf34a9619bf&#13;

### Release

Madrid

### Cause

This could be caused by different reasons related to Proxy or it may just be due to missed configuration of instance URL in the config.xml

### Resolution

Check to make sure that the "config.xml" has URL configured with "HTTPS" instead of "HTTP"

Also If Proxy is configured, make sure it is configured with an "IP" address only.  i.e it should be just IP "10.10.10.10"  instead of "http://10.10.10.10"
