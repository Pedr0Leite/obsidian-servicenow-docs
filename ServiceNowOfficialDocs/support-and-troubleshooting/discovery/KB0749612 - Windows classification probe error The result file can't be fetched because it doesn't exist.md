---
title: "Windows classification probe error \"The result file can't be fetched because it doesn't exist\""
aliases:
  - KB0749612
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749612
kb_number: KB0749612
last_modified: 2025-07-07
---

## Windows classification probe error "The result file can't be fetched because it doesn't exist"

  

### Issue

Windows classification probe error "The result file can't be fetched because it doesn't exist"

### Release

Madrid Patch 3 and pre Paris release.

### Cause

Windows administrative shares are hidden server resources that Discovery uses to temporarily store the results of processes run by specific probes. The MID Server script file LaunchProc.psm1 launches the process, writes its output to the administrative share on the machine, and then retrieves the results for the MID Server. Access to administrative shares is restricted to users with administrative rights to the target, such as users, local or on the domain, who belong to the local Administrators group.

With the Madrid patch 3 release, all Windows probes that use WMI protocol call the LaunchProc.psm1 script file and use the $admin share folder as default. The "Windows - Classify" probe uses WMI protocol and thus need access to the discovered computer admin share.

The admin share was already necessary for many of the windows probes for previous releases.

### Resolution

From the MID server and with the same account used by discovery, ensure the user account used for discovery can:

1.  Access/Create files on the target host   
    \\\\<ip\_address>\\admin$\\temp\\

### Related Links

-   [Windows Discovery on Madrid Patch 3 and later - known issues and workarounds](https://support.servicenow.com/kb_view.do?sysparm_article=KB0753561 "Windows Discovery on Madrid Patch 3 and later - known issues and workarounds")

Starting in Paris the classify probe will first check if MID server has access to the $admin share. Next, if the MID server has access to the $admin share it will check if there is Powershell access. If one of the conditions fails, it will revert to legacy WMI discovery on such host. Thus, upgrading to Paris may resolve the issue in some cases.
