---
title: "Using a Group Managed Service Account (gMSA) for Windows discovery"
aliases:
  - KB0750818
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750818
kb_number: KB0750818
last_modified: 2025-12-17
---

## Using a Group Managed Service Account (gMSA) for Windows discovery

  

### Issue

Group Managed Service Accounts (gMSA) are a specific type of Active Directory account that provide automatic password management, simplified service principal name (SPN) management, and the ability to delegate the management to other administrators across multiple servers. They can be configured for use in ServiceNow.

### Release

All

### Resolution

ServiceNow side configuration:

1.Discovery > Credentials 

2.New > Windows Credentials

3\. Enter the gMSA Windows credentials in the **<domain>\\<gmsa>$** legacy format or in **UPN** format.

You can configure your Windows users in Active Directory.

### Related Links

[Group Managed Service Accounts overview](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview "Group Managed Service Accounts overview")
