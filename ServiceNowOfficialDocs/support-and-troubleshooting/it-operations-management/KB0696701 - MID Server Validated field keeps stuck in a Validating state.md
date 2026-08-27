---
title: "MID Server \"Validated\" field keeps stuck in a \"Validating\" state"
aliases:
  - KB0696701
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696701
kb_number: KB0696701
last_modified: 2025-09-30
---

## MID Server "Validated" field keeps stuck in a "Validating" state

  

### Issue

MID Server "Validated" field keeps stuck in a "Validating" state.  
This might occur especially after an upgrade or install.

![Mid Server list showing Validated status as Validating](sys_attachment.do?sys_id=117765354714fa18f64de825126d4356 "Mid Server list showing Validated status as Validating")

### Release

All

### Cause

This occurs when the time/date set on the MID Server server is not sync'd or it's different from the Time Zone configured on the same server.  
Example: The MID Server is running in a Windows Server with a Time Zone configured to Amsterdam Time Zone. However, the actual time/date is not sync'd or is different.

### Resolution

Make sure the time and date are correctly configured to the Server time zone.
