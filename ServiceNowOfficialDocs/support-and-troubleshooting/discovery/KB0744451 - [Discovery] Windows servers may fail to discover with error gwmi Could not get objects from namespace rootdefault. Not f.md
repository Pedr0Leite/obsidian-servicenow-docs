---
title: "[Discovery] Windows servers may fail to discover with error \"gwmi : Could not get objects from namespace root\default. Not foundAt **PATH**\""
aliases:
  - KB0744451
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744451
kb_number: KB0744451
last_modified: 2024-04-07
---

## \[Discovery\] Windows servers may fail to discover with error "gwmi : Could not get objects from namespace root\\default. Not foundAt \*\*PATH\*\*"

  

### Issue

# Symptoms

Sometimes the windows servers may fail to discover with below error message:

""

gwmi : Could not get objects from namespace root\\default. Not foundAt <<MID\_Server\_Agent\_Folder\_Path>>\\agent\\scripts\\PowerShell\\WMIFetch.psm1:363char:20+ $reg = gwmi -list -computer $computer -credential $cred-namespace r ...+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ CategoryInfo : ObjectNotFound: (:) \[Get-WmiObject\], ManagementException+ FullyQualifiedErrorId : INVALID\_NAMESPACE\_IDENTIFIER,Microsoft.PowerShell.Commands.GetWmiObjectCommandYou cannot call a method on a null-valued expression. 

""

# Release

All.

# Cause

The issue is because the namespace "root\\default" is not available on the target devices when we run PS commands. You can get this exact namespace on the related input ECC queue.

# Resolution

Request the customer to log in to the target device with the credentials same as in credentials tables and then run the below sample PS script in PS editor.

""

Get-WmiObject -Namespace "root/default" -List 

""

-   Make sure the intended namespace is returned. If not work with their admin team why the namespaces are not returned.
-   One of the other issues might be related to PowerShell version 2.0. So, please try to use a higher version of less than 6.
