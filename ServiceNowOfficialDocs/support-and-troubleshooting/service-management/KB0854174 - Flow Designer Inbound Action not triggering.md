---
title: "Flow Designer Inbound Action not triggering"
aliases:
  - KB0854174
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0854174
kb_number: KB0854174
last_modified: 2026-06-29
---

## Flow Designer Inbound Action not triggering

  

### Issue

You have a configuration for Inbound Email flow as in the below screenshot:

![](sys_attachment.do?sys_id=2bdb559147794fd43542f24c736d43ff)

and when an email comes in, instead of being processed by the above flow, you can notice in the logs:

Trigger xxxxxxxxxxx: Unable to access target record for table name x\_an\_projects\_projects, skipping ( x\_an\_projects\_projects can be any other table here). 

### Release

All

### Resolution

Remove the Reply Record Type value. 

If you have condition on the email flow, for example "Receive Type" is "Reply" as in below image 

![](sys_attachment.do?sys_id=2bdb959147794fd43542f24c736d4304)

this is enough to successfully run the flow.
