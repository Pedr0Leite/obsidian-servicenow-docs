---
title: "Powershell custom activity script is executing on MID server instead target server"
aliases:
  - KB0753188
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753188
kb_number: KB0753188
last_modified: 2024-04-07
---

## Issue

You might want to run commands like: ipconfig, hostname on the target machine and expect target machine's hostname and IP Address. But the output returned will be of MID Server's, which means that the commands are executing on MID server and not on the target machine.

![](sys_attachment.do?sys_id=cd6c686edb42b450e515c2230596190c)

  

![](sys_attachment.do?sys_id=816c686edb42b450e515c22305961912)

  

## Resolution

By making use of the $computer variable which stores the Target provided in the custom activity, the command can be modified as follows:

**invoke-command -Computername $computer -Credential $cred -ScriptBlock { ipconfig }**

![](sys_attachment.do?sys_id=156c686edb42b450e515c22305961917)

  

![](sys_attachment.do?sys_id=956c686edb42b450e515c2230596191c)

Get-WMIObject can also be used to run commands targeting remote machines. For example, the below command can be used to get basic computer information:

**Get-wmiobject win32\_computersystem -Computername $computer -Credential $cred**
