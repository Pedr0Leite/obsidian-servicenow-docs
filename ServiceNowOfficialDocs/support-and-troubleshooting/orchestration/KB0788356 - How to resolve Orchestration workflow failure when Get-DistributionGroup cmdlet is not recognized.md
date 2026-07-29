---
title: "How to resolve Orchestration workflow failure when Get-DistributionGroup cmdlet is not recognized"
aliases:
  - KB0788356
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788356
kb_number: KB0788356
last_modified: 2026-01-16
---

## How to resolve Orchestration workflow failure when Get-DistributionGroup cmdlet is not recognized

  

### Issue

An Orchestration activity fails with the following error in the ECC Queue:

"The term 'Get-DistributionGroup' is not recognized as the name of a cmdlet, function, script file, or operable program."

### Release

All supported releases

### Cause

The **Get-DistributionGroup** cmdlet is not installed or configured on the MID Server. Scripts that run through Orchestration activities must be executable from the MID Server command prompt. 

### Resolution

**Get-DistributionGroup** is an Exchange cmdlet used to administer Active Directory remotely. This cmdlet is available in on-premises Exchange and in the cloud-based service.

To resolve this error, do one of the following:

-   Install the Exchange Management Tools on the MID Server
-   Connect to a management session on an Exchange server

For installation instructions, refer to the Microsoft documentation: [Install the Exchange management tools.](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/install-management-tools?view=exchserver-2019)
