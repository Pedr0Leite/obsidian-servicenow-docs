---
title: CSM Configurable Workspace landing pages
description: A landing page is an initial view of your workspace. Landing pages present content tailored to a user’s assigned role and provide the information they must get started with their work.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/csm-workspace-landing-pages.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [CSM Configurable Workspace features, CSM Configurable Workspace, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# CSM Configurable Workspace landing pages

A landing page is an initial view of your workspace. Landing pages present content tailored to a user’s assigned role and provide the information they must get started with their work.

Landing pages can include filtered [[migration-lists|lists]], KPIs, and other features that enables you to access information from one location. CSM Configurable Workspace landing pages provide customer service agents and managers with lists of assigned [[csm-cases-case-tasks-overview|cases and case tasks]] as well as agent, group, and organization metrics.

Agents use landing pages as a starting point to get into their work, where they can quickly scan and prioritize cases and case tasks, access records, and track their performance.

## CSM Configurable Workspace landing pages

Several landing pages are available for [[csm-workspaces-configure|CSM Configurable Workspace]].

-   **[[csm-ws-landing-page-original|CSM Landing Page]] and [[csm-ws-landing-page-premium|CSM Landing Page - Premium]]**

    These landing pages use components to display lists and metrics. The admin configures this information in [UI Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/using-ui-builder.md) and can create different landing pages for different audiences.

    Two versions of the landing page are available based on plugin activation. For more information, see [CSM Configurable Workspace landing page plugins](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/csm-workspace-landing-pages.md).

-   **[[csm-ws-landing-page-dashboard|CSM Dashboards]]**

    This landing page uses dashboards to display information. You can duplicate the provided dashboards and modify them as desired or create dashboards and then share these dashboards with other users.


## CSM Configurable Workspace landing page plugins

The following table describes the plugin requirements for the CSM Configurable Workspace landing pages.

<table id="table_czt_w5n_4xb"><thead><tr><th>

Landing Page

</th><th>

Plugin requirements

</th></tr></thead><tbody><tr><td>

CSM Landing Page

</td><td>

Available with the CSM Configurable Workspace plugin \(sn\_csm\_wrkspc\).

</td></tr><tr><td>

CSM Landing Page - Premium

</td><td>

Available with the following plugins:-   CSM Configurable Workspace \(sn\_csm\_wrkspc\)
-   Performance Analytics - Content Pack - [[c_CustomerServiceManagement|Customer Service Management]] - Advanced \(com.snc.pa.customer\_service\_advanced\)

</td></tr><tr><td>

CSM Dashboards

</td><td>

Available with the CSM Configurable Workspace plugin \(sn\_csm\_wrkspc\).

</td></tr></tbody>
</table>

## Related

- [[csm-ws-landing-page-original|CSM Landing Page]]
- [[csm-ws-landing-page-premium|CSM Landing Page - Premium]]
- [[csm-ws-landing-page-dashboard|Dashboard landing pages]]
- [[migration-lists|Lists]]
- [[csm-cases-case-tasks-overview|Cases and case tasks]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[c_CustomerServiceManagement|Customer Service Management]]
