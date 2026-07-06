---
title: "Delivery Controller pattern fails at step 5 with a PermissionDenied error"
aliases:
  - KB0745150
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745150
kb_number: KB0745150
last_modified: 2024-04-07
---

## Delivery Controller pattern fails at step 5 with a PermissionDenied error

  

### Issue

# Symptoms

When running the **Delivery Controller** pattern it fails at step 5 with a **PermissionDenied** error:

Get-XDSite : You do not have the required permissions to perform this operation.  
At line:1 char:37  
\+ Add-PSSnapin Citrix.Broker.Admin.V2;Get-XDSite  
\+ ~~~~~~~~~~  
\+ CategoryInfo : PermissionDenied: (:) \[Get-XDSite\], PermissionDeniedException  
\+ FullyQualifiedErrorId : Citrix.XDPowerShell.PermissionDenied,Citrix.XenDesktopPowerShellSdk.Sdk.Configuration.GetXDSiteCommand

# Cause

This is due to the Windows Discovery account not having access to Citrix Studio.

# Resolution

Make sure the Windows account used for discovering that specific device has permission to access Citrix Studio and then re-run the discovery.
