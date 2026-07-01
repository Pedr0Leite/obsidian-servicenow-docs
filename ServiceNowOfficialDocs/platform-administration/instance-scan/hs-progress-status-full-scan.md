---
title: Monitoring a scan
description: You can check the progress status of a scan by checking the progress tracker.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/instance-scan/hs-progress-status-full-scan.html
release: australia
product: Instance Scan
classification: instance-scan
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Using Instance Scan, Instance Scan, Maintain and monitor, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - instance-scan
  - health-check
  - best-practices
  - type-task
---

# Monitoring a scan

You can check the progress status of a scan by checking the progress tracker.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **[[hs-landing-page|Instance Scan]]** &gt; **Checks**.

    A list of checks appears.

2.  Run the required scan.

    The progress tracker displays the status of the scan run. You can close the progress tracker and view it later without having to stay in the modal for the execution to complete. To see the status later, go to **[[hs-results|Results]]** in the application navigator. Select the required [[hc-scan-results|scan results]] record to review its status.

3.  To see the status of the scan, select **Go to Result**.

    If the scan completes, a list of [[hs-findings|findings]] is displayed. You can also find all the checks that ran as a part of the scan by selecting the Checks related list. If any of the checks fails, click Failures related list to review them. If the full scan takes some time to complete, you can check the status by selecting **Results** from the application navigator.


**Parent Topic:**[Using Instance Scan](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-using-scans.md)

**Related topics**  


[Create a check]()

[Create a check suite]()

[Executing a scan]()

[Schedule a full scan]()

[Schedule a suite scan]()

[Parallel scans]()

[Reviewing of scans]()

[Queue your scan]()

[Cancel a scan]()

[Using the Instance Scan dashboard]()

## Related

- [[hs-landing-page|Instance Scan]]
- [[hs-results|Results]]
- [[hc-scan-results|Scan results]]
- [[hs-findings|Findings]]
