---
title: "Transfer Type Dropdown Not Populating in HR Agent Workspace"
aliases:
  - KB2657082
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657082
kb_number: KB2657082
last_modified: 2025-12-17
---

## Transfer Type Dropdown Not Populating in HR Agent Workspace

  

### Issue

In the HR Agent Workspace, the Transfer type dropdown does not display any options, even though active records exist in the HR Transfer Case Configurations table (`sn_hr_core_transfer_case_config`). The issue is specific to HR Agent Workspace; functionality works in the Native UI.

### Release

Any

### Cause

A bug in the UX Client Script “Update available transfer types for HR case SRP” caused incorrect mapping of transfer types using `output.map(type => ...)` instead of `output.methods.map(type => ...)`.

### Resolution

To resolve the issue:

-   Navigate to UX Client Scripts and locate Update available transfer types for HR case SRP.
-   Update the script logic to use:

JavaScript

output.methods.map(type => ...)

instead of

JavaScript

output.map(type => ...)

-   Test the fix in a development instance and validate that the Transfer type dropdown populates correctly.
-   Apply the fix to higher environments following change management.
-   Refer to PRB1859289 for tracking the permanent fix from ServiceNow.
