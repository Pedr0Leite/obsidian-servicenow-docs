---
title: "Windows VM powershell execute script support for GCP"
aliases:
  - KB0756431
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756431
kb_number: KB0756431
last_modified: 2024-04-20
---

## Windows VM powershell execute script support for GCP

  

**This article is to explain how to configure and execute Windows PowerShell scripts in Google Cloud Platform**

**Prerequisites**

On a Windows MID Server, execute the attached PowerShell script ([winrmenable.ps1.zip](sys_attachment.do?sys_id=401a1cf7dbeb7fc81cd8a345ca9619f2 "winrmenable.ps1.zip")).

**Note:** Ensure that the provisioning VM has WinRM HTTP and WinRM HTTPS ports allowed in the firewall. If not, execute the following command after provisioning:

New-NetFirewallRule -DisplayName 'PSremoting Inbound' -Profile @('Domain', 'Private', 'Public') -Direction Inbound -Action Allow -Protocol TCP -LocalPort @('5985', '5986')

**Procedure**

1.  Unzip the attached file: [ModExpoExtractor.jar.zip](sys_attachment.do?sys_id=b70a1cf7dbeb7fc81cd8a345ca9619e5 "ModExpoExtractor.jar.zip")
2.  Before you add the jar file: Navigate to **System Properties > Security** and then set MIME to be inactive by selecting **No**.
3.  Create a new MID Server Jar File and attached ModExpoExtractor.jar.  
      
    ![](/sys_attachment.do?sys_id=c01a1cf7dbeb7fc81cd8a345ca9619ec)  
      
    
4.  Extract the [WindowsPowershellGCPUpdateSet.zip](sys_attachment.do?sys_id=801a1cf7dbeb7fc81cd8a345ca9619ef "WindowsPowershellGCPUpdateSet.zip")
5.  Import the update sets in the following order:  
      
                     GCPWindowsKeySupport – CAPI scope  
                     Regenerate Google Compute API – GCP scope  
                     GCPResourceBlockUpdates – GCP scope  
      
    
6.  After the import processes succeed, click **Preview Update Set**.
7.  Commit the update sets. The state changes from **Updated** to **Committed**.
8.  Provision a Windows VM using a GDM template.
9.  After provisioning, create a key or identify a key that is listed in the Cloud Management User Portal.  
      
            **Notes:**  
               -- **InfuseKey** can push only one user key.  
               -- **InfuseKey** cannot push a Management key.  
      
    
10.  Use the **Virtual Machine Store Extension Interface.****InfuseKey** Day-2 operation to add the key to the VM. 
11.  On the Cloud Admin Portal, Click **Design > Cloud Scripts**.
12.  Click **Cloud Script Template** and add the PowerShell script.
13.  Create a cloud script that should map to cloud script template.
14.  On the Cloud User Portal, test by executing the PowerShell script using the **Virtual Machine Store Extension Interface.ExecuteScript** Day-2 operation.
