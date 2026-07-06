---
title: "MID Server agent log has Install name: Demo Server"
aliases:
  - KB0783175
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783175
kb_number: KB0783175
last_modified: 2025-01-03
---

## MID Server agent log has Install name: Demo Server

  

### Summary

MID Server's agent log (./agent/logs/agent0.log.0) may show the Install Name as "Demo Server", which is confusing and probably wrong for your instance.

10/24/19 11:00:03 (398) MIDServer MID Server started  
10/24/19 11:00:07 (284) StartupSequencer Successfully connected to instance:  
10/24/19 11:00:07 (284) StartupSequencer     **Install name: Demo Server**  
...

### Release

All.

### Instructions

This is nothing to worry about. Our instance provisioning scripts use "Demo Server" as a default value for all instances. You will also see that value at the top of the /stats.do page.

If you prefer some other value, then you can change the system property that defines the text:

1.  Log in an an admin.
2.  Navigate to **System Properties > All Properties**.
3.  Search and open the property named **glide.installation.name** 
4.  Change the value.
5.  Save the record.

This will have no functional effect at all for the instance, so can safely be changed to anything.
