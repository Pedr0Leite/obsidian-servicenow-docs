---
title: "WMI-Classify fails with error \"Could not get objects from namespace root\default\"
aliases:
  - KB0713211
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713211
kb_number: KB0713211
last_modified: 2024-04-07
---

## WMI-Classify fails with error "Could not get objects from namespace root\\default"

  

### Issue

# Symptoms

* * *

"gwmi : Could not get objects from namespace root\\default. Access denied"

# Environment

* * *

All environments

# Cause

* * *

This issue occurs when the rights do not flow down if assigned at the root level, it is complaining that the credential or group does not have access to root/default

# Resolution

* * *

\-On the Start menu, click Run and type wmimgmt.msc

\-In the WMI Control pane, right-click WMI Control, choose Properties, and then select the Security tab.

\-Navigate to the namespace root/default, click Security, and then configure groups and permissions for the namespace. We would need read permissions at the root/default level.
