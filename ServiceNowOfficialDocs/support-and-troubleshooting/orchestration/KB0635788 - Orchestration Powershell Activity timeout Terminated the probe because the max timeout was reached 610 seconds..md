---
title: "Orchestration Powershell Activity timeout: \"Terminated the probe because the max timeout was reached: 610 seconds\". "
aliases:
  - KB0635788
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635788
kb_number: KB0635788
last_modified: 2024-04-07
---

## Orchestration Powershell Activity timeout: "Terminated the probe because the max timeout was reached: 610 seconds".

  

### Issue

Orchestration Powershell Activity timeout: "Terminated the probe because the max timeout was reached: 610 seconds"

  
  

# Issue

* * *

Some custom Orchestration Powershell Activities take longer to execute. If the response takes more than 610 seconds, the activity will fail and the following error appears in the activity log "Terminated the probe because the max timeout was reached: 610 seconds".

# Solution

* * *

Increase the probe timeout by adding mid.windows.probe\_timeout parameter in the MID Server Configuration Parameters.

1.  Navigate to **MID Server > Servers**.
2.  From the list of MID Servers, select a MID Server to configure.
3.  Select the **Configuration Parameters** related list and click **New**.
4.  Add the mid.windows.probe\_timeout, set a value greater than 610, and click **Save**.
5.  Restart the MID Server.
