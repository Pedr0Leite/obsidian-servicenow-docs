---
title: Scan Engine for the Impact Store Application
description: Impact Platform Health uses the Impact Scan Engine to enable proactive management of instance quality, compliance, and performance. The Scan Engine is integrated with your Impact Store App to support platform health and adherence to leading practices.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/impact-healthscan-store-app.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Platform Health, Using Impact, Impact]
---

# Scan Engine for the Impact Store Application

[[impact-landing-page|Impact]] [[platform-health-idi|Platform Health]] uses the Impact Scan Engine to enable proactive management of instance quality, compliance, and [[instance-observer-performance|performance]]. The Scan Engine is integrated with your Impact Store App to support platform health and adherence to leading practices.

The Scan Engine examines ServiceNow instances for findings related to active definitions that are stored in the Scan Findings table. You can view existing or resolved findings that resulted from the instance scans or summarized and detailed scan information.

Impact Scan Engine automates your code inspections in real-time so you can identify more deficiencies, improve the quality of your instances, and speed up your development efforts. You can also monitor and control development activities to proactively improve the quality of the system and support ongoing efforts to improve it over time.

## Benefits and overview

-   Enforce leading practices and code standards in real-time.
-   Enhance platform performance, security, and [[user-experience-insights|user experience]] with role-based visibility and controls.
-   Improve maintainability, upgrades, and problem management.
-   Reduce development and maintenance costs.
-   Diminish the need for manual code reviews, which are prone to human error.
-   Calculate technical debt and estimate resolution time with scan output findings, progress percentiles, and estimated time remaining on code fixes.
-   Empower proactive code quality monitoring and detection versus reactive corrections.
-   Automate developer feedback and training through real-time, leading practice rule evaluations.

## Scan definitions

Scan Engine uses a large set of definitions to correct coding and workflow findings in real time and performs scans across your entire instance to detect existing findings. This prevents developer mistakes by blocking saving a record before issues are resolved. Nightly scans identify existing findings across the entire instance.

For more information, see [[scan-engine-definitions|Scan Engine definitions]].

## Scan types

There are different types of scans that you can run on your instances. Depending on the type of scan, the properties required during configuration vary.

Refer to the table for information on the available scan types.

<table><thead><tr><th>

Scan type

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Initial diagnostic scan \(Scheduled scan\)

</td><td>

-   Runs based on defined Scheduled Scan options or on-demand with the Execute Now option.

**Note:** The first executed instance scan is a full scan.

See [[run-scan-engine|Run your first scan with the Scan Engine]] for first time setup.

-   View existing or resolved findings that resulted from the instance scans as well as summarized and detailed scan information.

</td></tr><tr><td>

Diagnostic scans- On-demand scan \(subsequent delta scans\)

</td><td>

-   Scans for configured updates that occurred since the last scan.
-   Specifically analyzes application files that have been modified or sys\_update\_xml records.
-   Delta scans always look for definitions marked to return one row check per system property.
-   Scans for specific definitions that were identified as development issues in a previous scan.

**Note:** See [[configure-scan-engine-properties|Configure Scan Engine properties]] for on-demand scan configuration options and [[scan-engine-parallel-processing|Full and delta instance scans]] for scan information.


</td></tr><tr><td>

Update set scan

</td><td>

-   Scans individual update sets for findings.

The initial Update set scan is a full scan of all open update sets. Subsequent scans only scans records that have been modified since the last scan date \(delta scan\).

-   Child update set findings are visible from the parent update set findings summary scan record.

**Note:** See [[update-set-scanning-properties|Configure update set scanning properties]] for details.


</td></tr><tr><td>

Application scan

</td><td>

Scan applications to identify definition findings before publishing to the application repository. **Note:** See [[initiating-on-demand-scans-scan-engine|Initiate application scans]] for details.

</td></tr></tbody>
</table>## Configuration overview

For more information on configuring and running the Scan Engine, see [[using-impact-scan-engine|Running on-demand scans]], and [[scan-engine-diagnostic-dashboards|Track Platform Health trends]].

**Note:** Scan Engine findings are not transmitted to the Impact Delivery Instance through the Guided Setup integration.

## Related

- [[scan-engine-definitions|Scan Engine definitions]]
- [[run-scan-engine|Run your first scan with the Scan Engine]]
- [[configure-scan-engine-properties|Configure Scan Engine properties]]
- [[scan-engine-parallel-processing|Full and delta instance scans]]
- [[update-set-scanning-properties|Configure update set scanning properties]]
- [[initiating-on-demand-scans-scan-engine|Initiate application scans]]
- [[using-impact-scan-engine|Running on-demand scans]]
- [[scan-engine-diagnostic-dashboards|Track Platform Health trends]]
- [[impact-landing-page|Impact]]
- [[platform-health-idi|Platform Health]]
- [[instance-observer-performance|Performance]]
- [[user-experience-insights|User Experience]]
