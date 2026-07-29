---
title: "Discovery: A Windows virtual server discovered both via IP and vCenter could have different RAM values in each CI"
aliases:
  - KB0755051
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755051
kb_number: KB0755051
last_modified: 2025-03-13
---

## Discovery: A Windows virtual server discovered both via IP and vCenter could have different RAM values in each CI

  

### Issue

If a Windows VM is being discovered as a server (cmdb\_ci\_win\_server) and, at the same time as a VMware Instance (cmdb\_ci\_vmware\_instance) because vCenter discovery is enabled, the RAM values might not match.

If you log into the VM and vCenter, both show the same amount of RAM.

### Release

All

### Cause

If RAM is added dynamically to a Windows VM through vCenter while it is running the Win32\_PhysicalMemory class isn't updated. As the ServiceNow Windows probes use this class to recover the memory information it appears incorrectly in the cmdb\_ci\_win\_server CI.

It appears correctly on the server because the Win32\_OperatingSystem class is used to retrieve the information. 

You can verify this by running the following command against the target server as per the documentation provided here: [Manage ECC Queue content](https://docs.servicenow.com/csh?topicname=ecc-queue-mid-server.html&version=latest "Manage ECC Queue content")

powershell.exe 'Get-WmiObject -Class Win32\_OperatingSystem -ComputerName <TARGET\_SERVER\_NAME\_OR\_IP> -Property FreePhysicalMemory'

**NOTE**: This is not a platform limitation, this is a consequence of how Windows WMI and dynamic memory assignment interact.

### Resolution

The correct value will show in Win32\_PhysicalMemory after the VM is next rebooted.
