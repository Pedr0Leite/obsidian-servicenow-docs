---
title: Creating Platform Analytics pages in your own workspace
description: You can either create a new workspace with preconfigured Platform Analytics pages in App Engine Studio, or add Platform Analytics pages to your own workspace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/adding-analytics-center-to-ws.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Platform Analytics experience, Platform Analytics]
---

# Creating Platform Analytics pages in your own workspace

You can either create a new workspace with preconfigured [[c_performanceAnalyticsAndReporting|Platform Analytics]] pages in App Engine Studio, or add Platform Analytics pages to your own workspace.

Choose from the following ways to add Platform Analytics to your workspace. These approaches differ in the degree of customization they provide:

-   Add an entire pre-built workspace from App Engine Studio.
-   Use the page templates that are provided in the UI Builder. You can re-create all of Platform Analytics experience, or you can add only selected parts.

-   **[[create-analytics-ws-aes|Create a Platform Analytics workspace from App Engine Studio]]**  
The App Engine Studio includes a prebuilt workspace that you can add to an application. This workspace includes an Analytics Center page, along with the pages that the Analytics Center links to.
-   **[[add-analytics-center-to-experience|Add Platform Analytics pages to a configurable workspace]]**  
Add an Analytics Overview and its related pages to your own workspace/experience through page templates.
-   **[[add-dashboard-to-workspace|Add a dashboard to a Dashboards page]]**  
You can add either a technical dashboard or one made in the inline editor to a page you built from the Dashboards page template. Configure the dashboard component on that page.
-   **[[config-custom-redirection-from-db|Configure custom redirection from a dashboard component]]**  
If you have created a page in your workspace from the Dashboard page template, you can customize the on-click redirection from the dashboard component on that page. The inline dashboard that this component displays will follow the custom redirection.
-   **[[dashboard-url-parameter-delegation|Dashboard URL parameter delegation]]**  
The Delegate URL params property enables UIB pages containing dashboard components to control how URL parameter updates are handled. Doing so enables custom navigation logic for embedded or workspace scenarios.
-   **[[pass-global-filters-to-db|Pass global filters to the dashboard page template]]**  
Global filters are sent to the dashboard to serve as filters for the visualizations within the dashboard. These filters are merged with existing filters in the dashboard.
-   **[[configure-dashboard-data-broker|Configure dashboard data broker]]**  
Activate the Dashboard data broker preset and configure the data broker to potentially speed the loading of dashboards by prefetching some data.

**Parent Topic:**[[par-workspace|Platform Analytics experience]]

## Related

- [[create-analytics-ws-aes|Create a Platform Analytics workspace from App Engine Studio]]
- [[add-analytics-center-to-experience|Add Platform Analytics pages to a configurable workspace]]
- [[add-dashboard-to-workspace|Add a dashboard to a Dashboards page]]
- [[config-custom-redirection-from-db|Configure custom redirection from a dashboard component]]
- [[dashboard-url-parameter-delegation|Dashboard URL parameter delegation]]
- [[pass-global-filters-to-db|Pass global filters to the dashboard page template]]
- [[configure-dashboard-data-broker|Configure dashboard data broker]]
- [[par-workspace|Platform Analytics experience]]
- [[c_performanceAnalyticsAndReporting|Platform Analytics]]
