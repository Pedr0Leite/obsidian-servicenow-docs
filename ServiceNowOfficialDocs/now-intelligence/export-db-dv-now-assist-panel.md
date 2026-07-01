---
title: Export dashboards and data visualizations from the Now Assist panel
description: Export or schedule the export of dashboards and data visualizations conversationally through AI instead of going through the Platform Analytics user interface.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/export-db-dv-now-assist-panel.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
keywords: [export, schedule, schedule export, Now Assist, Now Assist Panel, Platform Analytics AI]
breadcrumb: [Platform Analytics in the Now Assist panel, Now Assist in Platform Analytics, Platform Analytics]
---

# Export dashboards and data visualizations from the Now Assist panel

Export or [[schedule-export-dboards-data-viz|schedule the export of dashboards and data visualizations]] conversationally through AI instead of going through the [[c_performanceAnalyticsAndReporting|Platform Analytics]] user interface.

## Before you begin

Role required: now\_assist\_panel\_user. To schedule an export, you also need par\_scheduler. You need access to the dashboard or the data in the visualization.

## Procedure

1.  Open the Now Assist panel.

    \[Omitted image "nowass-open-nowass-panel.png"\] Alt text: Control for opening the Now Assist panel.

2.  From the options, select **Dashboard and visualization export**.

    \[Omitted image "dash-viz-export.png"\] Alt text: Now Assist panel showing Dashboard and visualization export.

3.  Engage in an iterative conversation until Now Assist produces the export you want.

    -   If you want an immediate export, specify the word "Export" in your prompt. If you want to schedule an export, specify "Schedule."
    -   Specify the name of the data visualization or dashboard.
    -   Specify the word "visualization" or "dashboard" depending on what you want to export. Specify the word multiple times for best results.
    -   Specify the desired output type.
    -   Specify whether you want to download the export or have it emailed.
    -   You can only export dashboards or data visualizations that have been saved to the library.
    -   Although you can directly export only visualizations that are in the library, if you export a dashboard, you export all visualizations on that dashboard, including those that were not saved to the library.
    For more information, see the topics linked after this procedure.


## What to do next

**Tip:** After an export request is complete, reset the conversation before beginning a new request. Otherwise, some option selections might carry over to the new request. If this happens anyway, consider clearing your browser cache.

-   **[[nowass-supported-export-output|Supported export output types]]**  
The dashboard and visualization output skill supports the same outputs for the same data visualizations as Platform Analytics generally.
-   **[[nowass-export-destinations|Export destinations]]**  
When you export a dashboard or data visualization in the Now Assist panel, you have to specify the destination.
-   **[[limitations-exporting-db-dv|Limitations for exporting dashboards and visualizations]]**  
The [[activate-db-dv-export-skill|dashboard and visualization export skill]] supports only some dashboards for export. Requests for export are not always recognized or understood correctly.
-   **[[nowass-export-guidelines-examples|Export guidelines and examples]]**  
In your prompts for the dashboard and visualization export skill, you can describe the export you want with a variable amount of detail. You are prompted for any necessary information that is missing. Before the export runs, you are asked to review the request, giving you a chance to change any options.

**Parent Topic:**[[analytics-assist-landing-page|Generate or export dashboards and data visualizations in the Now Assist panel]]

**Related topics**  


[[export-visualization-vd|Export a data visualization from the Visualization Designer]]

[[export-pae-dashboard-ppt|Export a Platform Analytics dashboard]]

[[schedule-visn-export-vd|Schedule the export of data visualizations or dashboards]]

## Related

- [[nowass-supported-export-output|Supported export output types]]
- [[nowass-export-destinations|Export destinations]]
- [[limitations-exporting-db-dv|Limitations for exporting dashboards and visualizations]]
- [[nowass-export-guidelines-examples|Export guidelines and examples]]
- [[analytics-assist-landing-page|Generate or export dashboards and data visualizations in the Now Assist panel]]
- [[export-visualization-vd|Export a data visualization from the Visualization Designer]]
- [[export-pae-dashboard-ppt|Export a Platform Analytics dashboard]]
- [[schedule-visn-export-vd|Schedule the export of data visualizations or dashboards]]
- [[schedule-export-dboards-data-viz|Schedule the export of dashboards and data visualizations]]
- [[c_performanceAnalyticsAndReporting|Platform Analytics]]
- [[activate-db-dv-export-skill|Dashboard and visualization export skill]]
