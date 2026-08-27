---
title: "How to execute OOTB MID Server PowerShell scripts directly on the PowerShell console"
aliases:
  - KB0717302
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717302
kb_number: KB0717302
last_modified: 2025-01-03
---

## Issue

# Description

* * *

This article describes how to execute OOTB MID Server Powershell scripts directly on the Powershell console.

Useful for identifying errors that occurred while executing Orchestration workflows.  

# Procedure

* * *

1.Login to the MID Server host and open Powershell console

2\. You will need to find the DiagnosticsUtil.psm1 module that is on the MID Server

3. perform Import-Module \[path to module\]/DiagnosticsUtil -DisableNameChecking

4\. Now copy the contents of the mid server script file that you want to execute.

5\. Hardcode the values for variables if required

6\. Execute the script

  

Note : The above steps are for scenario where you want to execute for example : UpdateADObject.ps1.  In general, if you are executing a method and the powershell log says method not found, you need to import the module that contains this method.
