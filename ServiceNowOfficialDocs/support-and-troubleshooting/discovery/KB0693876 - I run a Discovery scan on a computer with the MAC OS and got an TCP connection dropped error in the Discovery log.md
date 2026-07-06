---
title: "I run a Discovery scan  on a computer with the MAC OS and got an \"TCP connection dropped\" error in the Discovery log"
aliases:
  - KB0693876
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693876
kb_number: KB0693876
last_modified: 2024-04-07
---

## I run a Discovery scan on a computer with the MAC OS and got an "TCP connection dropped" error in the Discovery log

  

### Issue

# Symptoms

* * *

I run a Discovery scan  on a computer with the MAC OS and got an "TCP connection dropped" error in the Discovery log.

# Release

* * *

Any

# Environment

* * *

Discovering a MAC OS computer.

# Cause

* * *

Apple changed how SSH login responds back to bad credential requests. Bad credential requests occur in normal operation when Discovery tries different SSH credentials to determine the correct credential to use in the future for that target device.   
  
Also, you must be using sncssh library, not j2ssh library to discover Mac Sierra.

# Resolution

* * *

To enable sncssh for all MID servers, set mid.property.ssh.use\_snc = true in MID Server -> Properties.
