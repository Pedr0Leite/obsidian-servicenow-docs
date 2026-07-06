---
title: "Finding uptime for Windows servers. "
aliases:
  - KB0752908
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752908
kb_number: KB0752908
last_modified: 2024-04-07
---

## Finding uptime for Windows servers. 

  

### Issue

Finding uptime for Windows servers. 

  

### Release

J and above. 

  

### Resolution

As of now, only the linux discovery supports the fetching of the server uptime using the standard linux command, "uptime". There is no feature for doing the same for Windows computers currently on the OOB platform. However, you can either use the command "net stats svr" on your Windows computer probe or use the Uptime.exe tool. As this is a customization, it is out of scope for ServiceNow support to completely assist you with the new probe/pattern you are creating, however, you can use the command stated above in your custom pattern.
