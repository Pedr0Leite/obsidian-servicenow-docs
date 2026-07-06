---
title: "Discovery to Windows server didn't detect port 135 in Shazzam input payload"
aliases:
  - KB0686260
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686260
kb_number: KB0686260
last_modified: 2024-04-07
---

## Discovery to Windows server didn't detect port 135 in Shazzam input payload

  

### Issue

# Symptoms

* * *

Windows server has port 22 and 135 open but Shazzam input payload show port 22 open only and didn't detect port 135. This cause the discovery fail (classification stage) as unable to login to server with credential provided (ie: It use SSH credential to access windows server) 

# Release

* * *

Jakarta but not limited to Jakarta version

# Cause

* * *

Suspect it could be due to Network delay and need more time to wait for connection.

# Resolution

* * *

Modified Shazzam probe parameter "GenericTCP\_waitForConnectMS" by increase the value from default (1000) to higher value (ie: 5000)

GenericTCP\_waitForConnectMS

Sets the number of milliseconds the GenericTCP scanner waits for a connection.  
Default: 1000
