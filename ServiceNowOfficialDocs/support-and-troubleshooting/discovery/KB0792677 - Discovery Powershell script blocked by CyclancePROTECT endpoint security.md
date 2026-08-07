---
title: "Discovery Powershell script blocked by CyclancePROTECT endpoint security"
aliases:
  - KB0792677
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792677
kb_number: KB0792677
last_modified: 2023-12-08
---

## Discovery Powershell script blocked by CyclancePROTECT endpoint security

  

### Issue

The Windows classification input payload contains the message **CylancePROTECT Script Control has blocked access to this PowerShell script** in the output tag. Test credentials of windows server is fails with below error: 

PowerConsole session was lost while executing command: function SNC-Decode-Command { param( \[Parameter(Mandatory=$true)\] \[string\]$encodedCommand ); return \[System.Text.Encoding\]::UTF8.GetString(\[System.Convert\]::FromBase64String($encodedCommand)) }

### Cause

The CylancePROTECT is an endpoint security software which is blocking Powershell script to run. Depending on the policy set for script control (alert or block), the CylancePROTECT agent will allow or block the execution of the script.

### Resolution

Please engage your endpoint security team and ask them to unblock PowerShell script control in CylancePROTECT.
