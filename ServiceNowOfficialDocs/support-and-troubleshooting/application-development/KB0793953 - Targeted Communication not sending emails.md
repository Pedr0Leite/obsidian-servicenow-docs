---
title: "Targeted Communication not sending emails"
aliases:
  - KB0793953
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793953
kb_number: KB0793953
last_modified: 2025-04-01
---

## Issue

When sending a targeted communication, the user receives the notification via publication, but does not get an email with the notification.

## Resolution

To add bcc's to a custom emails scripts and include the bcc list, add these mail scripts at the bottom of the Message HTML:  
  
${mail\_script:sn\_publications\_host\_url}sn\_publications\_publications.do?sysparm\_pub\_id=${sys\_id}"  
${mail\_script:publication\_attach\_links}  
${mail\_script:publication\_content}  
${mail\_script:add\_users\_to\_bcc\_list}
