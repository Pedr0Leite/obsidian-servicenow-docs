---
title: "How to get Password Reset working with LDAP/AD"
aliases:
  - KB0721415
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721415
kb_number: KB0721415
last_modified: 2024-04-07
---

## How to get Password Reset working with LDAP/AD

  

### Issue

# Symptoms

* * *

Testing Windows Credentials would fail with an error message : **"Module Credentials could not be found"**.

# Cause

* * *

Installation of MID server on the unsupported Windows version. This was noticed on Windows 10 workstation, but may be applicable for any unsupported version.

# Resolution

* * *

Install the mid server on a supported version. Below is the requirements from London version, but refer the instance version for the actual mid server requirements.

MID Server supported systems :   
[https://docs.servicenow.com/csh?topicname=r\_MIDServerSystemRequirements.html&version=latest](https://docs.servicenow.com/csh?topicname=r_MIDServerSystemRequirements.html&version=latest)   
  

**Windows server:** To discover Windows-based servers, run Service Mapping patterns, or execute Orchestration commands on Windows devices, the MID Server must be installed on a Windows server. The MID Server supports all Windows Server 2008, 2012, and 2016 editions, virtual machines, and 64-bit systems.  
**  
Note:** .NET Framework version 3.5, 4.0, 4.5, 4.6, or 4.7 is required for Service Mapping support and for Windows pattern-based discovery.
