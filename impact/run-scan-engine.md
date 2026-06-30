---
title: Run your first scan with the Scan Engine
description: An initial full Scan Engine completion is required to set a baseline from a series of tasks performed that tune the instance environment to complete future scans quickly and efficiently.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/run-scan-engine.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Configure the Impact Store Application, Configuring Impact, Impact]
---

# Run your first scan with the Scan Engine

An initial full Scan Engine completion is required to set a baseline from a series of tasks performed that tune the instance environment to complete future scans quickly and efficiently.

## Before you begin

[[configure-initial-scan-engine-settings|Activate Scan Engine and review settings]] before beginning this task.

You can complete the configuration steps directly in the Guided Setup interface or can configure the properties using the indicated navigation path.

Refer to [[scan-engine-parallel-processing|Full and delta instance scans]] for details on the various types of scans that can be executed.

**Important:** Depending on the size of your instance, your first scan could take a few hours to complete. We suggest running your first scan overnight, especially in production instances.

Role required: [[impact-landing-page|impact]] app admin or admin

## Procedure

1.  Navigate to **All** &gt; **Impact** &gt; **[[platform-health-idi|Platform Health]]** &gt; **Scheduled Scan**.

2.  Select **Execute Now**.

    The scan progress is tracked within Platform Health.

    **Note:** Scan Engine findings are not transmitted to Impact Delivery Instance.

3.  Navigate to **All** &gt; **Impact** &gt; **Platform Health** &gt; **Scan Engine** &gt; **Scan Status**.

    See [[scan-engine-diagnostic-dashboards|Track Platform Health trends]]:

    -   View the different charts and reports available at **Impact** **Platform Health** **[[io-analytics|Analytics]] Dashboard**.
    -   Access refreshed Health Scan Engine dashboards each time a scan is completed.
    The Scan Engine results display with the status of each table that is being scanned.

4.  Integrate with your other environments running Impact and utilize Scan Engine diagnostics.

    You can connect your instances with a one-time configuration, available in both OAuth 2.0 and Basic Auth. Refer to [[instance-integration-scan-engine|Scan Engine integrations]] for details.

5.  **Mark as Complete** to progress to the next step in Guided Setup.


## What to do next

See [[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]] to further configure the Impact Store Application and import data from the Impact Delivery Instance.

-   **[Full and delta instance scans](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/scan-engine-parallel-processing.md)**  
The full and delta instance scan feature enables ServiceNow administrators and developers to initiate, monitor, and manage instance scans directly from the Scan Results list view.
-   **[[initiate-manage-scan-engine|Initiate and manage scans]]**  
Use the Scan Results list view to initiate scans, monitor scan status, and manage scan execution using the Initiate Scan and Force Full Scan buttons.
-   **[[using-impact-scan-engine|Running on-demand scans]]**  
You can initiate some scan types on-demand to run whenever they are required.
-   **[[understanding-scan-blocking-override-behavior|Scan blocking and override behavior scenarios]]**  
The Scan Engine blocks concurrent scans to protect instance [[instance-observer-performance|performance]]. Understanding these rules helps you plan scan execution efficiently and how the system handles concurrent scan requests and when Force Full Scan override is necessary.

**Parent Topic:**[[configuring-impact-platform|Configure the Impact Store Application]]

**Previous topic:**[[update-set-scanning-properties|Configure update set scanning properties]]

**Next topic:**[Full and delta instance scans](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/scan-engine-parallel-processing.md)

## Related

- [[configure-initial-scan-engine-settings|Activate Scan Engine and review settings]]
- [[scan-engine-parallel-processing|Full and delta instance scans]]
- [[scan-engine-diagnostic-dashboards|Track Platform Health trends]]
- [[instance-integration-scan-engine|Scan Engine integrations]]
- [[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]]
- [[initiate-manage-scan-engine|Initiate and manage scans]]
- [[using-impact-scan-engine|Running on-demand scans]]
- [[understanding-scan-blocking-override-behavior|Scan blocking and override behavior scenarios]]
- [[configuring-impact-platform|Configure the Impact Store Application]]
- [[update-set-scanning-properties|Configure update set scanning properties]]
- [[impact-landing-page|Impact]]
- [[platform-health-idi|Platform Health]]
- [[io-analytics|Analytics]]
- [[instance-observer-performance|Performance]]
