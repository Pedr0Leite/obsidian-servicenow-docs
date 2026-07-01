---
title: UI Action Bar
description: Learn how the Workspace UI Actions component functions with Configurable Workspace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/migration-form-ui-actions.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Migrate to CSM Configurable Workspace, Migrating to Configurable Workspace, CSM Configurable Workspace, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# UI Action Bar

Learn how the Workspace UI Actions component functions with Configurable Workspace.

UI actions include custom buttons, menu items, and limiting access to [[migration-forms|forms]] based on user role. The UI Action Bar component replaces the UI Actions component in Workspace.

|Legacy table name|UIB table name|
|-----------------|--------------|
|sys\_ui\_action|sys\_ux\_form\_action|

To migrate UI actions, each UI action must have a corresponding form action to use UI actions in Configurable Workspace.

For more information, see [[config-csm-config-ws-form-action|Set up a form action in Configurable Workspace]].

## Related

- [[config-csm-config-ws-form-action|Set up a form action in CSM Configurable Workspace]]
- [[migration-forms|Forms]]
