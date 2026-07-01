---
title: Playbook pages
description: Use playbook pages in CSM Configurable Workspace so that your agents can view the stages and activities in a playbook, work on activities, and have quick access to in-context information.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/csm-playbook-pages.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 8
breadcrumb: [Playbooks in Customer Service Management, Agent tools, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Playbook pages

Use playbook pages in [[csm-workspaces-configure|CSM Configurable Workspace]] so that your agents can view the stages and activities in a playbook, work on activities, and have quick access to in-context information.

## Overview of templates, pages, and page variants

Pages provide the base structure for how the system displays record information in CSM Configurable Workspace. You can create and customize pages with [UI Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/ui-builder-overview.md), a web user interface builder.

A page template is a pre-defined page configuration. When you create a page in UI Builder, you can select a page template as a starting point. You can also create a page from scratch or by copying another page and then customizing the page to meet your needs.

A page variant is a version of a page that includes unique settings such as the audience, conditions, and page order. For more information about templates, pages, and page variants, see [[config-csm-ws-create-page-variant|Creating pages and page variants]].

Pages and page variants can also include playbooks, which are created in Workflow Studio. A playbook provides step-by-step guidance for resolving a specific type of case. The workflows that are associated with a specific type of case and the activities that need to be completed to resolve cases of this type are detailed in the playbook.

## Playbook pages

The Playbooks for [[c_CustomerServiceManagement|Customer Service Management]] plugin provides the following playbook pages:

-   [[csm-playbook-horizontal-stages|Case playbook: horizontal stages]] page
-   [[csm-playbook-vertical-stages|Case playbook: vertical stages]] page

Additional CSM [[csm-playbook-apps|playbook applications]] provide playbook pages that you can activate and use with case types in CSM Configurable Workspace.

|Application|Page variant|Description|
|-----------|------------|-----------|
|Case Playbook for Complaints v5.0|Complaint case process page|Includes a horizontal stage picker that provides an end-to-end view of the complaint process.|
|Case Playbook for Onboarding v5.0|Onboarding case process page|This playbook page includes a horizontal stage picker at the top of the record that provides an end-to-end view of the onboarding process.|
|Case Playbook for Product Support v4.0|Product Support process page|This playbook page includes a horizontal stage picker at the top of the record that provides an end-to-end view of the product support process.|

For more information, see [[setting-up-csm-playbooks|Playbook plugins]].

**Note:** By default, playbook pages are read-only. To use a playbook page, [[activate-process-based-page|activate the page]] and set the page order.

## Benefits of using playbook pages

Resolving customer issues or requests often involves the execution of tasks across multiple users, departments, and systems. Different users are responsible for different tasks within the overall resolution process. Using playbooks provides the following benefits:

-   An experience that is tailored to customer service agents and other users.
-   Visibility into the overall resolution process, the current stage in the process, and the activities that need to be completed within that stage.
-   Access to in-context information.

## Configuring playbook pages

The following table includes configuration tasks for playbook pages.

<table id="table_sth_yrb_dxb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[Activate a playbook page or page variant](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/activate-process-based-page.md)

</td><td>

Activate a playbook page or page variant and set the page order.**Note:** Some playbook pages and page variants are not active by default.

</td></tr><tr><td>

[[customize-process-form-header|Customize the page header for a playbook page]]

</td><td>

Configure the page header for a playbook page. The page header includes a primary value and several secondary values. These fields can provide case, account, and contact information at a glance.

</td></tr><tr><td>

[[customize-process-ui-actions-bar|Customize UI actions for a playbook page]]

</td><td>

Configure the UI actions to display in the action bar for a playbook page.

</td></tr><tr><td>

[[customize-content-left-side-panel|Customize content in the left side panel for a playbook page]]

</td><td>

Add custom components in the side panel. By default, this panel includes the Customer 360, Timeline, and Active SLA components.

</td></tr><tr><td>

[[customize-process-tabs-in-side-panel|Customize tabs in the contextual side panel for a playbook page]]

</td><td>

Add or remove the tabs from the contextual side panel. Agents can use these tabs to perform tasks such as adding attachments and viewing recommendations.

</td></tr><tr><td>

[[customize-dynamic-related-records|Customize the dynamic related records for a playbook page]]

</td><td>

Configure the Dynamic Related Records feature to display the related records in the contextual side panel.

</td></tr><tr><td>

[[configure-app-route-for-subpage|Configure the app route to use an existing subpage]]

</td><td>

Create an app route to make an existing page a part of the page collection.

</td></tr><tr><td>

[[configure-optional-activity-for-a-case-type-playbook|Configure an optional activity for a playbook]]

</td><td>

Configure an optional activity in  Workflow Studio at various stages in a playbook so that agents and fulfillers can insert an activity when they are using the playbook.

</td></tr><tr><td>

[[setup-record-generator-for-case-type|Set up a record generator for case type]]

</td><td>

Create a record for a case type as the first step in a playbook by using a playbook record generator.

</td></tr><tr><td>

[Configure an email template](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/configure-email-templates.md)

</td><td>

Configure new email templates to enable agents to create emails for common issues.

</td></tr></tbody>
</table>## Using playbook pages

Playbooks enable your agents to view and complete their tasks more efficiently.

<table id="table_l2b_p5g_2xb"><thead><tr><th>

User task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[csm-playbook-create-record|Create a record using a playbook]]

</td><td>

If a playbook is configured to use the playbook record generator feature, an agent can create a record by using a playbook activity. Creating a record opens the playbook and initiates the first activity, which is to guide an agent through the record creation process.After saving the case, an agent moves to the next activity in the current stage or to the first activity in the next stage.

</td></tr><tr><td>

[[csm-playbooks-using|Resolve a case using a playbook]]

</td><td>

Opening a case takes the agent to the first open assigned activity. An agent can do the following actions while working on the activities in a playbook:

-   View the entire playbook process in the [[csm-playbook-templates|horizontal stage picker]].
-   View the activities for each stage in the stacked [[csm-playbook-layout|playbook activity view]].
-   [[csm-playbooks-using-activity-stream|Use the activity stream in the contextual side panel]]
-   [[csm-playbook-filter-activities|Filter activity cards]].
-   Select an activity and perform the work required in the main work area.
-   View and update the case details by using the **View Details** button.
-   View the persistent contextual information in the left side panel, such as the account and contact.
-   View the related list tabs in the [[csm-contextual-related-records|Dynamic related records]] component in the contextual side panel.
-   Access information in the contextual side panel, including the [[csm-config-ws-activity-stream|activity stream]], form ribbon, [[migration-agent-assist|Agent Assist]], Dynamic related records, attachments, and templates.
-   Create tasks, compose email, and add worknotes.
-   Open reference fields in subtabs under the session tab.

</td></tr><tr><td>

[Add an activity to a playbook](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/playbook-add-optional-activity.md)

</td><td>

Add optional activities to a playbook stage as needed.

</td></tr><tr><td>

[[case-summarization-in-process-page|Summarize case details]]

</td><td>

Use the Now Assist for CSM case summarization skill to summarize the case details and display this information on the case record.

</td></tr><tr><td>

[[compose-email-from-email-template|Compose an email from an email template]]

</td><td>

Quickly compose emails for common issues by selecting an email template in the Compose Email page instead of manually drafting an email.

</td></tr></tbody>
</table>**Note:** For tasks that an agent completes outside of a playbook, the system automatically updates the playbook activities.

## Related

- [[config-csm-ws-create-page-variant|Creating pages and page variants]]
- [[csm-playbook-horizontal-stages|csm playbook horizontal stages]]
- [[csm-playbook-vertical-stages|csm playbook vertical stages]]
- [[setting-up-csm-playbooks|Playbooks in Customer Service Management]]
- [[activate-process-based-page|Activate a playbook page or page variant]]
- [[customize-process-form-header|Customize the page header for a playbook page]]
- [[customize-process-ui-actions-bar|Customize UI actions for a playbook page]]
- [[customize-content-left-side-panel|Customize content in the left side panel for a playbook page]]
- [[customize-process-tabs-in-side-panel|Customize tabs in the contextual side panel for a playbook page]]
- [[customize-dynamic-related-records|Customize the dynamic related records for a playbook page]]
- [[configure-app-route-for-subpage|Configure the app route to use an existing subpage]]
- [[configure-optional-activity-for-a-case-type-playbook|Configure an optional activity for a playbook]]
- [[setup-record-generator-for-case-type|Set up a record generator for case type]]
- [[csm-playbook-create-record|Create a record using a playbook]]
- [[csm-playbooks-using|Using Playbooks for Customer Service Management]]
- [[csm-playbook-templates|Playbook page templates]]
- [[csm-playbook-layout|Playbook layout and features]]
- [[csm-playbooks-using-activity-stream|Using the activity stream in the contextual side panel]]
- [[csm-playbook-filter-activities|Filter playbook activities]]
- [[csm-contextual-related-records|Dynamic related records]]
- [[case-summarization-in-process-page|Summarize a case]]
- [[compose-email-from-email-template|Compose an email from an email template]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[csm-playbook-apps|Playbook applications]]
- [[csm-config-ws-activity-stream|Activity stream]]
- [[migration-agent-assist|Agent assist]]
