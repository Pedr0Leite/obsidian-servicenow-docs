---
title: "Differences between Windows PowerShell Discovery and legacy Windows Discovery"
aliases:
  - KB0752537
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752537
kb_number: KB0752537
last_modified: 2025-07-24
---

## Issue

Beginning with Madrid Patch 3 and the New York release, as part of general Discovery performance enhancements, a new Windows Discovery method was implemented that uses PowerShell and the **admin$** share folder on remote targets. This method was already implemented and used in application dependency mapping (ADM) and enhanced application dependency mapping (ADME).

The new Windows discovery shows performance increases with speeds up to 8x times faster on the MID Server, with less CPU utilization and memory consumption. This means fewer MID Servers are now required by customers to discover their Windows infrastructure. The resources used on the target hosts have not significantly changed from the prior Discovery method.

Most customers have some Windows machines in their infrastructure, and most of these use PowerShell installed out of the box.

### Legacy Windows Discovery

Previously, to get all installed software display names, Discovery had to fetch it as a single Windows Management Instrumentation (WMI) field (which is a registry key) from the installed software probe. For example, for this registry key:

HKLM/Software/Microsoft/Windows/CurrentVersion/Installer/UserData/\*/Products/\*/InstallProperties/DisplayName

Note the two asterisks (\*)  around /Products/.

First, you had to get the values for everything where the (\*) is and then expand the information. Each value, user, and product would have to be expanded and go back and forth between the MID Server and the target host. This interchange between the MID Server and the target host caused issues with CPU and memory spikes.

![Exhibit of interchange between MID Server and a target host](sys_attachment.do?sys_id=016c4f7787fa6e1457288519dabb35e8)

### Enhanced Windows Discovery

**Beginning with Madrid Patch 3 and New York release**

Currently, the MID Server queries the target one time only with _all WMI fields_. An on-the-fly PowerShell script is built on the MID Server, and then the script runs on the target host. The target lists everything and returns the data back to the MID Server. The raw data is then parsed to an XML or a JSON output (depending on the probe used). 

There is no back and forth between the MID Server and the target, which frees up the MID Server by reducing CPU issues and memory spikes.

![Improved query between MID Server and target host](sys_attachment.do?sys_id=9d6c8f7787fa6e1457288519dabb35ef)

              ![Results of a PowerShell script](sys_attachment.do?sys_id=d56c8f7787fa6e1457288519dabb35f2)

### Requirements for Enhanced Windows Discovery

-   PowerShell versions 3.0 to 5.1 for remote Windows systems
-   File system to access from the MID Server.
    -   **Note**: The default is admin$ share (for WMI not Win RM). 
-   10 MB free disk space on the target to write the temporary file 

**Note**: All Windows probes using WMI protocol call the _LaunchProc.psm1_ script file and write to **admin$** share folder by default. In the New York release, if another network share is mounted on each Window target, the folder may be changed by updating the MID Server property to mid.powershell.target\_base\_dir**.**

**WinRM** **component, architecture, and design**

![](sys_attachment.do?sys_id=116c8f7787fa6e1457288519dabb35f5) 

**WMI component, architecture, and design**

![](sys_attachment.do?sys_id=596c8f7787fa6e1457288519dabb35f7)

## Resolution

.
