---
title: "SAM: Microsoft 365 Integration Profile Missing as a Direct Integration Option in Software Asset Workspace"
aliases:
  - KB3027084
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3027084
kb_number: KB3027084
last_modified: 2026-05-18
---

## SAM: Microsoft 365 Integration Profile Missing as a Direct Integration Option in Software Asset Workspace

  

### Issue

When creating a new Direct Integration profile in the Software Asset Workspace, the Microsoft 365 Integration Profile does not appear as an available option in the selection list.

### Symptoms

Navigating to Workspaces > Software Asset Workspace > License Operations > User Subscription > Direct Integration Profile and selecting New does not display a Microsoft 365 integration profile option.

### Facts

The Software Asset Management - SaaS License Management (`sn_sam_saas_int`) plugin is installed.

### Release

All

### Cause

The Microsoft 365 Integration Profile option also requires the `com.snc.samp.microsoft` plugin to be installed. Without it, the platform has no awareness of Microsoft 365 as a supported integration type, so the option does not appear in the Direct Integration Profile creation form. The presence of `sn_sam_saas_int` alone is not sufficient to expose this integration option.

### Resolution

1.  Navigate to System Definition > Plugins and verify whether `com.snc.samp.microsoft` (Software Asset Management Professional for Microsoft) is installed.
2.  If the plugin is not installed, submit a plugin activation request via the Now Support Portal: go to Automation Store and select the "Activate a plugin" catalog item.
3.  In the activation form, select com.snc.samp.microsoft from the plugin dropdown and submit the request.
4.  Once activation is confirmed, return to Workspaces > Software Asset Workspace > License Operations > User Subscription > Direct Integration Profile and select New. The Microsoft 365 Integration Profile option should now be present.

### Related Links

-   ServiceNow Docs: Set Up Microsoft Office 365 — [https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/set-up-microsoft-office-365.html](https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/set-up-microsoft-office-365.html)
-   Now Support KB: Plugin Activation via Automation Store — [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0695388](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695388)
