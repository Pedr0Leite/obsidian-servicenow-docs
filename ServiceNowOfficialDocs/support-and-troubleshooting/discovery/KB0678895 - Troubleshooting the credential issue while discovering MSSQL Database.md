---
title: "Troubleshooting the credential issue while discovering MSSQL Database"
aliases:
  - KB0678895
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0678895
kb_number: KB0678895
last_modified: 2024-04-07
---

## Troubleshooting the credential issue while discovering MSSQL Database

  

### Issue

Troubleshooting the credential issue while discovering MSSQL Database

# Issue

* * *

When attempting to discover an MSSQL server, the MSSQL Probe will fail with Error: _Authentication failure with the local MID server service credential._

In this scenario, you can run the following PowerShell script from the MID Server to verify the credentials.

If the credentials are successful, it should list the databases available on the SQL server.

# Solution

* * *

   

 
script start ###### 
\[reflection.assembly\]::LoadWithPartialName('Microsoft.SqlServer.Smo');\[reflection.assembly\]::LoadWithPartialName('Microsoft.SqlServer.SqlWmiManagement'); 
 
#Please change password below with password for "<username@domain.com>" 
$password = "" 
 
$dbinstance = "\\," 
$server = New-Object Microsoft.SqlServer.Management.Smo.Server($dbinstance) 
$server.ConnectionContext.LoginSecure = $true 
$server.ConnectionContext.ConnectAsUser = $true 
$server.ConnectionContext.ConnectAsUsername = "<username@domain.com>" 
$server.ConnectionContext.ConnectAsUserPassword = $password 
$server.Databases | select name 
script End ######
