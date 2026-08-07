---
title: Configure signals for breakdown elements
description: Configure signal detection and assign responsibility for multiple breakdowns and breakdown elements on one indicator.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/configure-signals-multi-breakdowns.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure, KPI Signals, Platform Analytics experience, Platform Analytics]
tags:
  - now-intelligence
  - type-task
---

# Configure signals for breakdown elements

Configure signal detection and assign responsibility for multiple breakdowns and breakdown elements on one indicator.

## Before you begin

An administrator must activate [[process-behavior-charts-for-kpis|KPI Signals]] for the indicator. For more information, see [[activate-signals-monitor|Activate KPI Signals monitoring for an indicator \(KPI\)]].

Role required: responsible user for the indicator or admin.

## About this task

For example, KPI Signals could simultaneously monitor the following indicators and breakdowns:

-   Number of open incidents \(no breakdown\)
-   Number of open incidents, Priority = 1-Critical
-   Number of open incidents, Priority = 2-High
-   Number of open incidents, Category = Software

However, KPI Signals could not monitor "Number of open incidents, Priority = 1-Critical, Category = Software."

## Procedure

1.  Open KPI Signals for the indicator, without first selecting a filtering breakdown in [[kpi-details|KPI Details]].

2.  Click the cogwheel to open the Configuration options.

    \[Omitted image "kpi-signals-open-settings.png"\] Alt text: KPI Signals panel showing the cogwheel button for opening configuration settings

3.  Click **Add breakdowns**.

    The **Add Breakdowns** dialog opens.

4.  Click in the Breakdowns field and select a breakdown.

    A list of elements for the breakdown appears.\[Omitted image "kpi-signals-add-breakdown.gif"\] Alt text: Animation showing a breakdown being selected.

5.  Click **Filter** and use the condition builder to build a filter for the elements.

6.  Select at least one element and click **Add**

7.  To monitor signals on elements of another breakdown, click **Add breakdowns** again and repeat the steps.

8.  In the Signal Detection tab, activate monitoring for the KPIs and set the baseline start and number of scores required to calculate the baseline.

    For more information about the settings on the Signal Detection tab, see [[configure-signal-detection|Configure signal detection]].

9.  Open the Responsibility tab and assign a responsible user to each KPI.

    For more information about responsible users and the settings on the Responsibility tab, see [[kpi-signals-responsible-users|Configure responsibility for KPI Signals]].

10. Open the Notifications tab and set how often the responsible user should get an email notification for an unresolved signal.

    You can also set the total number of reminders the responsible user gets for an unresolved signal. Also set the anti-signal factor, which is used to calculate how many scores without a signal result in an anti-signal. For more information about anti-signals, see [[signal-no-signal-anti-signal|Signal, no signal, and anti-signal]]. For more information about the settings on the Notifications tab, see [[configure-signal-notifications|Configure signal notifications]].


**Parent Topic:**[[configuring-kpi-signals|Configuring KPI Signals for an indicator]]

## Related

- [[activate-signals-monitor|Activate KPI Signals monitoring for an indicator \(KPI\)]]
- [[configure-signal-detection|Configure signal detection]]
- [[kpi-signals-responsible-users|Configure responsibility for KPI Signals]]
- [[signal-no-signal-anti-signal|Signal, no signal, and anti-signal]]
- [[configure-signal-notifications|Configure signal notifications]]
- [[configuring-kpi-signals|Configuring KPI Signals for an indicator]]
- [[process-behavior-charts-for-kpis|KPI Signals]]
- [[kpi-details|KPI Details]]
