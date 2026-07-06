---
title: "Client Software Distribution - SCCM - Unable to Discover"
aliases:
  - KB0759363
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759363
kb_number: KB0759363
last_modified: 2026-03-30
---

## Client Software Distribution - SCCM - Unable to Discover

  

### Issue

We are trying to discover the SCCM applications and collections using the "Client Software Distribution - SCCM Server Instances" but has not been successful. 

Test credential return credential validated.

Workflow context return following error for user "svc.servicecmdb" 

@@@

New-PSSession : \[sscm.local\] Connecting to remote server 

sscm.local failed with the following error message : Access is 

denied. For more information, see the about\_Remote\_Troubleshooting Help topic. 

At line:1 char:1 

\+ New-PSSession -ComputerName sscm.local -Credential $Cred ... 

\+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

\+ CategoryInfo : OpenError: (System.Manageme....RemoteRunspace:Re 

moteRunspace) \[New-PSSession\], PSRemotingTransportException 

\+ FullyQualifiedErrorId : AccessDenied,PSSessionOpenFailed 

Authentication failure with the user DOMAIN\\svc.servicecmdb 

@@@@@

### Release

All releases

### Cause

User doesn't has right to access "CMSite" drive of SCCM. 

Approach to verify:

1\. Run following command in SCCM server Powershell command return nothing.

Import-Module -Name “$(split-path $Env:SMS\_UI\_ADMIN\_PATH)\\ConfigurationManager.psd1”  
Get-PSDrive -psprovider “CMSite”

![](sys_attachment.do?sys_id=94ad4e4493488b9c057c7de86cba103c)

### Resolution

Grant the user "CMSite" drive access.

When user has the "CMSite" drive access, we will see

![](sys_attachment.do?sys_id=14adce4493488b9c057c7de86cba1027)
