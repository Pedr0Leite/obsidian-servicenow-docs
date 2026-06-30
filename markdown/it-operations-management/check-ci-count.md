---
title: Check CI count used for ITOM subscriptions
description: View daily CI counts or the average of the last 90 daily counts.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-operations-management/check-ci-count.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Using ITOM/OT SU Licensing, ITOM/OT SU Licensing and subscriptions, IT Operations Management]
---

# Check CI count used for ITOM subscriptions

View daily CI counts or the average of the last 90 daily counts.

## Before you begin

Ensure that your organization has purchased ITOM subscriptions. You cannot view the information in the **ITOM License** module without subscriptions.

Role required: sn\_itom\_license.reader

## About this task

ITOM applications, such as [[itom-visibility-landing-page|ITOM Visibility]], ITOM [[r-discovery|Discovery]], [[itom-health-landing-page|ITOM AIOps]], [[hla-landing-page|Health Log Analytics]], [[itom-cloud-accelerate-landing-page|ITOM Cloud Accelerate]], and [[itom-optimization-landing-page|ITOM Optimization]] provide information on the resources they handle. These resources, called configuration items \(CIs\), are what ITOM applications find, monitor, and store in the CMDB. The ITOM/OT SU Licensing module combines this CI data with the subscription information of your organization to produce statistics on the subscription usage and consumption of the ITOM applications. For more information about the licensing workflow process, see [[data-collection-aggregation-licensing-process|Data collection and aggregation for licensing process]].

This information does not include any statistics on subscriptions purchased in bundles. For complete information on subscriptions, [[view-itom-license-statistics|view subscription statistics for IT Operations Management]].

## Procedure

1.  Navigate to **ITOM License** &gt; **License Report**.

    \[Omitted image "itom-license-report.png"\] Alt text: The License Report window showing subscription statistics for the [[r_ITOMApplications|IT Operations Management]] applications a la carte.

    To know more about the fields in the Licence Report window, see [[license-report-form|License Report form]].

2.  In the **Total Count** column, view the average daily CI counts for the last 90 days.

3.  View the daily CI count in one of the following ways.

    -   Set the **Aggregated** filter condition to **\[Aggregated\] \[is\] \[false\]** and select **Run**.
    -   Navigate to **ITOM License** &gt; **License Daily Usage Count**.

## Related

- [[data-collection-aggregation-licensing-process|Data collection and aggregation for licensing process]]
- [[view-itom-license-statistics|View subscription statistics for ITOM]]
- [[license-report-form|License Report form]]
- [[itom-visibility-landing-page|ITOM Visibility]]
- [[r-discovery|Discovery]]
- [[itom-health-landing-page|ITOM AIOps]]
- [[hla-landing-page|Health Log Analytics]]
- [[itom-cloud-accelerate-landing-page|ITOM Cloud Accelerate]]
- [[itom-optimization-landing-page|ITOM Optimization]]
- [[r_ITOMApplications|IT Operations Management]]
