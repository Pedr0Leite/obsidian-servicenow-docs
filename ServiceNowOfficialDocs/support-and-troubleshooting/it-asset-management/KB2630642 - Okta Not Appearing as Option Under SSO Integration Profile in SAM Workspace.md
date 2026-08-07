---
title: "Okta Not Appearing as Option Under \"SSO Integration Profile\" in SAM Workspace"
aliases:
  - KB2630642
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2630642
kb_number: KB2630642
last_modified: 2025-11-17
---

## Okta Not Appearing as Option Under "SSO Integration Profile" in SAM Workspace

  

### Issue

“Okta” option was missing from the Integration type dropdown while creating a new User Subscription → SSO Integration Profile in SAM Workspace.

### Symptoms

Missing “Okta” option in Integration type dropdown.

Relevant plugins already installed:

_\-Software Asset Management – SaaS License Management_ 

### Release

Any release

### Cause

The option "Okta" in the SSO Integration Profile dropdown is controlled by a specific sys\_wizard\_answer record.  
If this record is missing, the option will not appear in the UI.

  
This usually occurs when a file fails to install during plugin installation or upgrade.

Missing Record:

```
sys_wizard_answer.sys_id = 22810303772011108383b0fabe5a9900
```

* * *

### Resolution

To restore the Microsoft Entra ID option:

Option 1 – Repair Plugin (Recommended)

Navigate to System Definition → Plugins.

Search for and repair the plugin:  
`Software Asset Management – SaaS License Management (sn_sam_saas_int)`

This will reinstall any missing dependent records, including the sys\_wizard\_answer entry.

Option 2 – Import the Missing Record

Export the sys\_wizard\_answer record (`sys_wizard_answer.sys_id = 22810303772011108383b0fabe5a9900`) from a working instance.

Import the XML into the affected instance.

Validate that “Okta” now appears in the dropdown.
