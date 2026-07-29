---
title: "How to remove the Mid Server Service."
aliases:
  - KB0781466
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781466
kb_number: KB0781466
last_modified: 2024-04-07
---

## How to remove the Mid Server Service.

  

### Issue

How to remove the Mid Server Service from Services on Windows Host

### Release

When we have a mid sever on the Window's Environment

### Resolution

1.  Login to the windows machine where the mid server is installed.
2.  Go to "Services" and look for the "MidServer Service".
3.  Double-click the service, under the "General" tab look for the "Service name" and copy it.
4.  Open Terminal as administrator and run the below command

                 **sc delete "Service Name"**

![](sys_attachment.do?sys_id=f9ae87b8dbc434d0471f9c41ba96198e)

You will see the below confirmation.

![](sys_attachment.do?sys_id=b5aec7b8dbc434d0471f9c41ba961925)
