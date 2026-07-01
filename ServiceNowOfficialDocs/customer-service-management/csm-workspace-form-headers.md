---
title: CSM Configurable Workspace form headers
description: Form headers in CSM Configurable Workspace provide a quick glance of case, account, or contact information.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/csm-workspace-form-headers.html
release: australia
topic_type: reference
last_updated: "2026-03-24"
reading_time_minutes: 1
breadcrumb: [Form features, CSM Configurable Workspace features, CSM Configurable Workspace, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-reference
---

# CSM Configurable Workspace form headers

[[migration-form-headers|Form headers]] in [[csm-workspaces-configure|CSM Configurable Workspace]] provide a quick glance of case, account, or contact information.

Form headers typically include the case short description. They can also include the action bar, record tags, and the [[csm-front-line-case-page|record presence component]].

\[Omitted image "csm-config-workspace-case-form-header.png"\] Alt text: [[r_CustomerServiceCaseForm|Case form]] header that shows the short description, record tags, and action buttons such as Close Case, Save, and Assign to me

For more information, see [[config-csm-config-ws-form-header|Set up a form header in CSM Configurable Workspace]]

**Note:** One form header configuration, **CSM/FSM Configurable Workspace Header Config**, is included with CSM Configurable Workspace.

## Record Information tab

The record information tab in the contextual side panel displays record details including the account and contact or consumer, the case state, and the case priority.

The Record Information tab in the contextual side panel can include the following cards depending on the record page configuration:

-   Overview: Displays relevant information about the case including the account and contact, the case priority, and the state.
-   Active SLA: Displays active SLAs for the case, including time remaining, the SLA state, and any breaches.

The cards that appear in the Record Information tab can be configured in the ribbon configuration. For more information, see [[config-csm-config-ws-ribbon|Set up a ribbon configuration in CSM Configurable Workspace]].

\[Omitted image "csm-config-workspace-case-form-header-sidebar.png"\] Alt text: The overview card shows the customer information, the case priority, and case state.

## Form header components

For CSM Configurable Workspace, the form header is made up of individual components that can be configured with [UI Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/using-ui-builder.md).

Individual components provide customers with flexible and granular configuration options. Customers can control the placement, size and spacing of these components, giving them the ability to show additional information that agents may need.

The Data Value Block component is used to display secondary values in the form header and the Contextual side panel. .

## Related

- [[csm-front-line-case-page|Front-line case page]]
- [[config-csm-config-ws-form-header|Set up a form header in CSM Configurable Workspace]]
- [[config-csm-config-ws-ribbon|Set up a ribbon configuration in CSM Configurable Workspace]]
- [[migration-form-headers|Form headers]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[r_CustomerServiceCaseForm|Case form]]
