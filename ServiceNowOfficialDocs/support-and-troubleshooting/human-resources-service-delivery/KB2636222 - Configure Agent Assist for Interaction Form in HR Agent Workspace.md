---
title: "Configure Agent Assist for Interaction Form in HR Agent Workspace"
aliases:
  - KB2636222
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636222
kb_number: KB2636222
last_modified: 2026-01-03
---

## Configure Agent Assist for Interaction Form in HR Agent Workspace

  

### Issue

Agent Assist was requested for the Interaction form in HR Agent Workspace or a custom workspace. While Agent Assist worked for the Interaction form in the SOW workspace, the same configuration did not work in HR Agent Workspace. Guidance was requested to enable Agent Assist in HR Agent Workspace and custom workspaces.

### Release

Any Release

### Cause

The issue occurred due to missing configuration in the macroponent JSON for the state field. Specifically, the required entry for the interaction type was absent, preventing Agent Assist from appearing in the HR Agent Workspace Interaction form.

### Resolution

To enable Agent Assist for the Interaction form in HR Agent Workspace:

-   Verify Macroponent Configuration

-   -   Navigate to the sys\_ux\_macroponent record for the Interaction form.
    -   Check the JSON configuration for the state field.

-   Add Required Entry

-   -   Include the `"sn_hr_core_task"` entry in the macroponent JSON.
    -   Save and publish the changes.

-   Validate Functionality

-   -   Confirm that Agent Assist appears in the Interaction form within HR Agent Workspace.
    -   Test in custom workspaces if applicable.

-   Additional Guidance

-   -   Refer to documentation for configuring sys\_ux\_macroponent for custom workspaces.
    -   Ensure proper mappings for state fields and interaction types.
