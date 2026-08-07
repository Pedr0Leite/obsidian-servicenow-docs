---
title: "Credential-less discovery installs npcap loopback adapter that breaks DNS resolution."
aliases:
  - KB0761174
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761174
kb_number: KB0761174
last_modified: 2024-04-08
---

## Credential-less discovery installs npcap loopback adapter that breaks DNS resolution.

  

### Issue

Enabling Credential-less discovery installs nmap and npcap on the MID Server host.  

### Release

All

### Cause

When npcap is installed, by default it creates a virtual loopback interface on the MID Server host.   
There are instances where the installation of this virtual loopback adapter by nmap tends to create DNS resolution conflicts on the host machine. Though this is a control from nmap as a tool, we do have a means of disabling the loopback adapter from being created.

### Resolution

1\. Head into the ecc\_agent\_script\_file table  
https://<INSTANCE-NAME>.service-now.com/ecc\_agent\_script\_file\_list.do

2\. In the name field filter for the keyword "NmapInstallation.ps1"  
Open the script NmapInstallation.ps1

3\. In the script NmapInstallation.ps1, in line 67 we have  
$nmap\_installer\_params = "/S /REGISTERPATH=NO /ZENMAP=NO "  
This needs to change to  
$nmap\_installer\_params = "/S /REGISTERPATH=NO /ZENMAP=NO /LOOPBACK\_SUPPORT=NO"  
  
Please note:

-   As soon as we change the script on the instance all active MID Servers will sync to this version and if we enable credential-less discovery following this on the MID Server, it will utilize the new script
-   Using /LOOPBACK\_SUPPORT=NO, we install npcap but we don't create any virtual loop back interface
-   Please be aware that if NPCAP was already installed on the host machine we don't re-intsall npcap, but we use the existing one. In the case that npcap was installed on the host machine with default (lookback\_support = true) , we will need to disable the adapters manually
-   Test if discovery runs without issues
