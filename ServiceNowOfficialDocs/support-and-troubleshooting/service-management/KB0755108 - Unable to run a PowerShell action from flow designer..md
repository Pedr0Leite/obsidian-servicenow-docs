---
title: "Unable to run a PowerShell action from flow designer."
aliases:
  - KB0755108
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755108
kb_number: KB0755108
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

When attempting to run a test Connection from the Flow Designer using the PowerShell Step, we are seeing this error message:

"Operation (AzureAD Testing.4891f802db323bc0edb538ff9d961958.2cdb2086dbfef7c0edb538ff9d9619cc) failed because no valid MID is available" 

# Cause

* * *

This is due to the Connection Alias (within the PowerShell step of the Flow Designer) does not have a current online MID Server.

# Resolution

* * *

From the Connection Alias step create a new connection or select the correct field here. Also, you can go to the sys\_connection table and create a new connection as well.
