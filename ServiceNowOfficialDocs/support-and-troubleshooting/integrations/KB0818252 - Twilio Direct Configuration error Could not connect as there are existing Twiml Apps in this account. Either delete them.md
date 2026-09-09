---
title: "Twilio Direct Configuration error : \"Could not connect as there are existing Twiml Apps in this account. Either delete them manually by logging into Twilio or disconnect them from the instance which added them.\""
aliases:
  - KB0818252
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818252
kb_number: KB0818252
last_modified: 2025-08-19
---

## Twilio Direct Configuration error : "Could not connect as there are existing Twiml Apps in this account. Either delete them manually by logging into Twilio or disconnect them from the instance which added them."

  

### Issue

While trying to configure a Twilio Direct configuration on `xxxxx.service-now.com` ServiceNow instance with the correct **Account SID** and **Auth Token**, you experience this error message:

<table style="border-collapse: collapse; width: 100%; height: 13px;" border="1"><tbody><tr style="height: 13px;"><td style="width: 100%; height: 13px; padding: 10px; border: 1px solid #c83c36; background-color: #ffdadc;">Could not connect as there are existing Twiml Apps in this account. Either delete them manually by logging into Twilio or disconnect them from the instance which added them.<br><br>- ServiceNowTwilioDirect - Twiml app's voice url seems to be bound to instance yyyyy.service-now.com</td></tr></tbody></table>

### Cause

This error message may be caused by a stale Twilio configuration which was bound to `yyyyy` ServiceNow instance. This warning message informs that the Account SID and Auth Token will not work on the `xxxxx` instance unless the Twilio Configuration is reset/deleted.

### Resolution

-   If you still have access to `yyyyy` instance, and if the configuration is still valid, disconnect with Twilio configuration. You can try configuring on `xxxxx` instance.
-   If you don't have access to `yyyyy` instance, or if the yyyyy instance is ZBooted/cloned over before the configuration was disconnected, then please delete the configuration on Twilio website to make the API keys available for the `xxxxx` instance.
