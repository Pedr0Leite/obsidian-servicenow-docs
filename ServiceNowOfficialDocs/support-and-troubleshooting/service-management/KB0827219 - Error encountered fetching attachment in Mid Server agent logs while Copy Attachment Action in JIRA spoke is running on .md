---
title: "\"Error encountered fetching attachment\" in Mid Server agent logs while Copy Attachment Action in JIRA spoke is running on Flow Designer"
aliases:
  - KB0827219
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827219
kb_number: KB0827219
last_modified: 2024-04-08
---

## "Error encountered fetching attachment" in Mid Server agent logs while Copy Attachment Action in JIRA spoke is running on Flow Designer

  

### Issue

"Copy Attachment" in JIRA SPOKE in Flow Designer copies an attachment from the Attachments \[sys\_attachment\] table to a target record.

[Copy Attachment action](https://docs.servicenow.com/csh?topicname=copy-attachment-flow-designer.html&version=latest "Copy Attachment action")

MID Server is being used for communication with JIRA for Copy Attachment.

When the "Copy Attachment" action is executed , an error is being pushed:

  
"Either provided SysID of attachment record is incorrect or unknown error occurred."  

  
  
![](sys_attachment.do?sys_id=64a52c49db8c70905a959c41ba96197c)

### Cause

This issue is happening because the mid server user is not able to reach to the **"sys\_attachment"** table.  

### Resolution

When the Mid Server agent logs checked , below is seen the IPaaSActionProbe worker:

  

2020-06-02 15:18:34 (987) Worker-Expedited:IPaaSActionProbe-6491ea5bdb09d410e4d4d7795e961922 Worker starting: IPaaSActionProbe source: 80816293944d14d028880feb9b35ea37  
2020-06-02 15:18:35 (644) Worker-Expedited:IPaaSActionProbe-6491ea5bdb09d410e4d4d7795e961922 Credentials sys\_id: 7badc6a2db7898508014dd3b5e961938  
2020-06-02 15:18:36 (003) Worker-Expedited:IPaaSActionProbe-6491ea5bdb09d410e4d4d7795e961922 SEVERE \*\*\* ERROR \*\*\* Error encountered fetching Attachment : Error while parsing metadata for attachment with sysid .

  
The solution for this issue is to add READ ACL for **"sys\_attachment"** table for the mid server user **"ServiceNow MidServer user"** in sys\_user table.
