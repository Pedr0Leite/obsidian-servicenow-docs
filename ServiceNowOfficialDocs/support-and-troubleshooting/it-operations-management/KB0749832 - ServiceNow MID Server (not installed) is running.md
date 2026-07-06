---
title: "ServiceNow MID Server (not installed) is running"
aliases:
  - KB0749832
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749832
kb_number: KB0749832
last_modified: 2024-04-07
---

## ServiceNow MID Server (not installed) is running

  

### Issue

# Symptoms

ServiceNow MID Server status shows (not installed).

Executing bin/mid.sh status results following:

"ServiceNow MID Server (**not installed**) is running: PID:59954, Wrapper:STARTED, Java:Started"

# Release

Madrid, London

# Environment

Red Hat Linux Server release 7.3 (Maipo)

# Cause

Observed the MID wrapper was upgraded from London with systemd instead of init.d which is causing the output as not-installed.

# Resolution

To run the MID server on the linux machine run following commands.

**sudo ./mid.sh install**

**sudo ./mid.sh start**

**sudo ./mid.sh status**

# Result

**$sudo ./mid.sh install**

Installing the ServiceNow MID Server daemon using systemd...  
creating default service file...  
Created symlink from /etc/systemd/system/multi-user.target.wants/mid.service to /etc/systemd/system/mid.service.

**sudo ./mid.sh start**

Starting ServiceNow MID Server with systemd...  
Waiting for ServiceNow MID Server...  
running: PID:6096

**sudo ./mid.sh status**

ServiceNow MID Server (**installed with systemd**) is running: PID:6096, Wrapper:STARTED, Java:STARTED
