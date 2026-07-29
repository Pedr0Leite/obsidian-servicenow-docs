---
title: "Is it possible for Forwarded emails to be treated as a reply Email and look up an existing record ?"
aliases:
  - KB0779404
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779404
kb_number: KB0779404
last_modified: 2024-04-07
---

## Is it possible for Forwarded emails to be treated as a reply Email and look up an existing record ?

  

### Issue

When a user replies to a notification and sends it to an instance, the inbound action updates an existing record based on a watermark or a record number in the subject.

When a user forwards a notification and sends it to an instance, the inbound action ignores the watermark or record number and creates a new record .

Is there a way to change the default behaviour, where forwarded emails also update the existing record using a watermark or a record number in the subject or body ?

### Cause

This is expected behaviour since the mail type will determine if a new record should get inserted or else if the code should attempt to look up an existing record.

See docs:

[Inbound Actions](https://docs.servicenow.com/csh?topicname=r_InboundActionTypeCriteria.html&version=latest "Inbound Actions")

  

### Resolution

1 - Go to Email properties

2 - Go to field "Identify email as a forward by these subject prefixes"

3 - Clear values like 'fw:fwd:' Put a string like 'xxx' in the forward prefixes field (otherwise the system will take the default values as coded)

4 - Set values 'fw: and fwd:' in the field : "Identify email as a reply by these subject prefixes" as follows:

re:,aw:,r:,Accepted:,Tentative:,Declined:,fw:,fwd:

\-> All forwarded Emails will be treated as Replies  
  

  

![](sys_attachment.do?sys_id=8e6e4778dbc434d0471f9c41ba961937)
