---
title: "Missing \"New\" UI Action in HAM Workspace Donation Order Section"
aliases:
  - KB2468689
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2468689
kb_number: KB2468689
last_modified: 2025-09-09
---

## Missing "New" UI Action in HAM Workspace Donation Order Section

  

### Issue

Users have reported the absence of the "New" UI action in the Donation Order section of the Hardware Asset Management (HAM) Workspace. This article clarifies whether this is expected behaviour and outlines steps for resolution.

### Symptoms

-   The "New" button is missing in the Donation Order section of the HAM Workspace.
-   Confirmed to be absent in Out-of-the-Box (OOTB) lab instances

### Release

ALL

### Cause

This is expected behaviour in the current OOTB configuration. The recommended method for initiating donation requests is via the Service Catalog, not directly through the workspace UI.

The exclusion is enforced by the following system record:

-   `sys_workspace_declarative_action_exclusion_f35ea7544322111062f45ad28ab8f2b9`

This record hides the "New" button from the workspace UI to align with catalog-driven workflows.

![](/sys_attachment.do?sys_id=5b2219f647ab6e9077748d01426d4301)

### Resolution

To enable the "New" button in the HAM Workspace Donation Order section:

1.  Navigate to the system record:
    -   `sys_workspace_declarative_action_exclusion_f35ea7544322111062f45ad28ab8f2b9`
2.  Uncheck the "Exclude" checkbox to remove the exclusion.
3.  Save and verify that the "New" button is now visible in the workspace.

Note: Deactivating this exclusion may impact intended workspace behaviour. It is recommended to test changes in a non-production environment before applying them to production.
