---
title: "Windows - Active Connections probe returns error: Exception calling \".ctor\" with \"2\" argument(s): \"Cannot process argument because the value of argument \"userName\" is not valid."
aliases:
  - KB0753501
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753501
kb_number: KB0753501
last_modified: 2024-04-07
---

## Windows - Active Connections probe returns error: Exception calling ".ctor" with "2" argument(s): "Cannot process argument because the value of argument "userName" is not valid.

  

### Issue

# Symptoms

Windows - Active Connections probe returns error: Exception calling ".ctor" with "2" argument(s): "Cannot process argument because the value of argument "userName" is not valid.

# Release

Post Madrid

# Cause

This issue normally happens when remoteExecution is on for "Windows - Active Connections" probe, and 

MID Server parameter mid.powershell.use\_credentials is set to false.

# Resolution

Either do:  
navigate to Discovery Definition > Probes > Windows - Active Connections > uncheck "Execute script remotely".

or:  
navigate to MID Server > Servers > open record "DPWDEV", check property: mid.powershell.use\_credentials, either delete this property, or set this to true
