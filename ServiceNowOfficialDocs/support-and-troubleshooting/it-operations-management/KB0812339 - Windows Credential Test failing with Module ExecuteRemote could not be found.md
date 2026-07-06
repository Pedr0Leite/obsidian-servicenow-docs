---
title: "Windows Credential Test failing with \"Module ExecuteRemote could not be found\""
aliases:
  - KB0812339
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812339
kb_number: KB0812339
last_modified: 2025-04-08
---

## Windows Credential Test failing with "Module ExecuteRemote could not be found"

  

### Issue

While testing the credential, i.e. Windows Credentials, the following issue might appear.

![](/sys_attachment.do?sys_id=db5169bcdb0d741022e0fb2439961929)

### Release

Any Release

### Cause

There might be various reasons why this issue arises. The manner to troubleshoot this issue would be to follow each point mentioned in the resolution section.

### Resolution

-   Enter inside the MID Server folder looking for the **ExecuteRemote.psm1** file and confirm that this is OOTB.  - [KB0791120](https://support.servicenow.com/kb_view.do?sysparm_article=KB0791120)
-   Windows Discovery Probes that use Remote Execution framework may be blocked by Antivirus software or ExecutionPolicy  - [KB0727945](https://support.servicenow.com/kb_view.do?sysparm_article=KB0727945)
-   The MID Server service might be running using a **Local System account**. The MID Server log with debugging indicates that the test it's failing when performing the check to see if "ExecuteRemote" existed using Get-Module -List command.  If missing it means that the user account probably did not have enough privileges to list the modules. Please see below:

```
Worker-Interactive:CommandPipeline-e196a9fcdbd00810c339b04ffe961963 DEBUG: execute($env:PSModulePath = $env:PSModulePath + "C:\MID_SERVER\mid.madrid-12-18-2018__patch5-06-26-2019_07-01-2019_1425.windows.x86-32\agent/scripts/Powershell/WinRMAPI")Worker-Interactive:CommandPipeline-e196a9fcdbd00810c339b04ffe961963 DEBUG: execute($SNC_modList = Get-Module -List; $SNC_modExists = $false; forEach($SNC_module in $SNC_modList) { if ($SNC_module.Name -eq "ExecuteRemote") { $SNC_modExists = $true } } if (!$SNC_modExists) { Write-Host MI8D_COMMAND_FAILURE })
```

-   If the path has a special character for instance: _"MID Server für DEV"_ you might experience this issue. The solution is to create a new MID Server folder without any special character, for instance: "_MidServerDev_".
