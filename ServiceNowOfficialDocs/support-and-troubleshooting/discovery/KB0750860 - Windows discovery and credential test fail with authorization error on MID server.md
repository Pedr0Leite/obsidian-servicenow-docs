---
title: "Windows discovery and credential test fail with authorization error on MID server"
aliases:
  - KB0750860
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750860
kb_number: KB0750860
last_modified: 2026-06-11
---

## Windows discovery and credential test fail with authorization error on MID server

  

### Issue

Windows discovery fails and credential tests return an authorization error when the Credentials.psm1 file has been customized on the MID server. Symptoms - Credential test fails with an authorization error. - MID server logs contain the following error:

PowerConsole-<session\_id>>stderr DEBUG: STDERR: At C:\\ServiceNow\\MIDServer\\agent\\scripts\\Powershell\\WinRMAPI\\Credentials\\Credentials.psm1:70
+ $results = gwmi win32\_operatingsystem -computer $computer -credentia ...
+ CategoryInfo          : InvalidOperation: (:) \[Get-WmiObject\], COMException
+ FullyQualifiedErrorId : GetWMICOMException,Microsoft.PowerShell.Commands.GetWmiObjectCommand

\- Running the same credentials manually on the MID server using Get-WmiObject (GWMI) succeeds.

### Symptoms

\- Credential test fails with an authorization error.  
\- MID server logs contain the following error:

PowerConsole-<session\_id>>stderr DEBUG: STDERR: At C:\\ServiceNow\\MIDServer\\agent\\scripts\\Powershell\\WinRMAPI\\Credentials\\Credentials.psm1:70  
\+ $results = gwmi win32\_operatingsystem -computer $computer -credentia ...  
\+ CategoryInfo : InvalidOperation: (:) \[Get-WmiObject\], COMException  
\+ FullyQualifiedErrorId : GetWMICOMException,Microsoft.PowerShell.Commands.GetWmiObjectCommand

\- Running the same credentials manually on the MID server using Get-WmiObject (GWMI) succeeds.

### Facts

1\. Customize the **Credentials.psm1** file on the MID server.  
2\. Navigate to **MID Server** > **Credentials**.  
3\. Run a credential test against a Windows target.  
4\. Observe the authorization error in the MID server logs.

### Release

  All release

### Resolution

Prerequisites:  
\- Access to the MID server file system.  
\- Ability to stop and start the MID server service.

Step 1: Identify the customized Credentials.psm1 files

1\. Navigate to the MID server installation directory: <MIDServer\_install\_path>\\agent\\scripts\\Powershell\\WinRMAPI\\Credentials\\  
2\. Locate both Credentials.psm1 files in the directory.  
3\. Compare each file against the default version from a clean MID server installation or from the ServiceNow store package.

Step 2: Restore default files

1\. Replace any customized Credentials.psm1 file with the default version.  
2\. Save the files.

Step 3: Verify the fix

1\. Restart the MID server service.  
2\. Navigate to MID Server > Credentials and run a credential test.  
3\. Confirm the test completes without an authorization error.

### Related Links

[Configuring MID Server](https://www.servicenow.com/docs/r/servicenow-platform/mid-server/configure-mid-server.html "Configuring MID Server")
