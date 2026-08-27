---
title: "Discovery Error on Windows Machine with Powershell 1.0"
aliases:
  - KB0790930
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790930
kb_number: KB0790930
last_modified: 2024-04-08
---

## Discovery Error on Windows Machine with Powershell 1.0

  

### Issue

Discovery on a Windows target device throw -  
  

<table style="height: 38px; width: 92.9959%; border-collapse: collapse;"><tbody><tr style="height: 13px;"><td style="width: 100%; height: 13px; background-color: #dedede;">Error: <strong><span style="color: #ff0000;">Missing expression after unary operator</span></strong> '-'.At line:1 char:2+ -E &lt;&lt;&lt;&lt; xecutionPolicy ByPass -NonInteractive -WindowStyle Hidden -command .....</td></tr></tbody></table>

![](sys_attachment.do?sys_id=8d5e144ddb00b4d0471f9c41ba961906)

### Release

-   All

### Cause

-   Powershell version on Target Machine or the MID Server Host Machine is Version 1.0

### Resolution

There are two ways to resolve this issue:

1.  Avoid Using Powershell by MID Server  
      
    -   Use MID Server Property 'mid.use\_powershell'
    -   This property enables or disables PowerShell for Discovery.
    -   Default value: false
    -   When set to true, Discovery reverts to using WMIRunner Probe.
    -   This probe cannot use the credentials defined in Discovery > Credentials.
    -   In this case, the MID Server connects to the WMI providers with the account the MID Server service is running.
    -   This account is required to have access to the remote machines so that WMIRunner works.  
          
        
2.  Upgrade Powershell Version  
      
    -   Upgrade Powershell Version on the Target Machine/Host Machine.

### Related Links

**ServiceNow supports these PowerShell versions**:

-   **Version 2.0**  
      
    -   Regular Discovery  
          
        
-   **Version 3.0**  
      
    -   Regular Discovery
    -   Application Dependency Mapping (ADM)
    -   File-based Discovery
    -   PowerShell version 3.0 does not support Windows Server 2003.  
          
        
-   **Version 4.0**  
      
    -   Regular Discovery
    -   Application Dependency Mapping (ADM)
    -   File-based Discovery  
          
        
-   **Version 5.0**  
      
    -   Regular Discovery
    -   Application Dependency Mapping (ADM)
    -   File-based Discovery

**Useful documents**:

-   [MID Server parameters for PowerShell](https://docs.servicenow.com/csh?topicname=mid-server-parameter-powershell.html&version=latest "MID Server parameters for PowerShell")
-   [Add a MID Server parameter](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest "Add a MID Server parameter")
-   [PowerShell for Discovery](https://docs.servicenow.com/csh?topicname=r_PowerShellForDiscovery.html&version=latest "PowerShell for Discovery")
