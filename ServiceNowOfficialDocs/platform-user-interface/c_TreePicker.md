---
title: Tree picker
description: The tree picker is a special reference lookup that you can add as an attribute to a form. Add the tree picker to the classic environment or to workspaces.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/c\_TreePicker.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Common UI elements, Working in Core UI, Configure UIs and portals, Configure user experiences]
tags:
  - platform-user-interface
  - type-concept
---

# Tree picker

The tree picker is a special [[onboarding-modals-reference|reference]] lookup that you can add as an attribute to a form. Add the tree picker to the classic environment or to workspaces.

The tree picker is a special reference lookup for the following items.

-   Configuration Items \(CIs\) for a field that depends on another CI field.
-   Reference elements for any hierarchical table. A hierarchical table is any table that has a parent field pointing back at itself.
-   Values for a user reference that depends on the group.

-   **[[t_AddTheTreePickerAttribute|Add the tree picker attribute]]**  
A limit of 1000 has been placed on the number of nodes returned to the tree picker. This limit is configurable with the **glide.ui.group\_heirarchy.max\_nodes** property.

**Parent Topic:**[[p_CommonUIElements|Common UI elements]]

**Related topics**  


[Reference lookup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_ReferenceLookup.md)

## Related

- [[t_AddTheTreePickerAttribute|Add the tree picker attribute]]
- [[p_CommonUIElements|Common UI elements]]
- [[onboarding-modals-reference|Reference]]
