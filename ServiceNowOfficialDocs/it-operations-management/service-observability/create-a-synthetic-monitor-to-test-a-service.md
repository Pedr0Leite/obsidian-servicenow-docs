---
title: Create a synthetic monitor to test a service
description: Install and configure synthetic monitoring and then create a monitor for your service.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-operations-management/service-observability/create-a-synthetic-monitor-to-test-a-service.html
release: australia
product: Service Observability
classification: service-observability
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use synthetic monitoring with Service Observability, Customize dashboard templates, Configuring Service Observability, Service Observability, ITOM AIOps, IT Operations Management]
tags:
  - it-operations-management
  - observability
  - slo
  - health
  - itom
  - type-task
---

# Create a synthetic monitor to test a service

Install and configure [[synthetic-monitoring-landing-page|synthetic monitoring]] and then create a monitor for your service.

## Before you begin

Your service must have an HTTP-reachable endpoint, configured as a CI in the HTTP\(S\) Endpoints \[cmdb\_ci\_endpoint\_http\] table of the Configuration Management Database \(CMDB\).

Role required: n\_sow\_svcobs.admin, sn\_sow\_synthetics.synthetics\_admin

## Procedure

1.  Install synthetic monitoring.

    See [[install-synthetic-monitoring|Install synthetic monitoring]] for more information.

2.  If needed, create a location to run the monitor from.

    Monitors can be run locally from a ServiceNow Glide instance or from your environment using either a cluster of [[acc-landing-page|Agent Client Collector]] \(ACC\) agents or from a MID Server. If you choose to run them from your environment, you must create a location. See [[create-synthetic-monitoring-locations|Create synthetic monitoring locations]] for more information.

3.  Create the monitor.

    Follow the steps in [[create-synthetic-monitor|Create and edit a synthetic monitor]]. Be sure to select the service you want to monitor as the **Related service CI**.


## What to do next

Once you create the monitor, it begins running tests. View the results of those tests to verify the results before embedding synthetic monitoring into a [[service-observability|Service Observability]] dashboard. For more information about viewing monitor test results, see [[identifying-system-issues|Identifying system issues with synthetic monitoring]].

Once you have expected results, move on to [Add synthetic monitor results to a Service Observability dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/service-observability/add-synthetic-monitor-results-to-a-service-observability-dashboard.md).

## Related

- [[install-synthetic-monitoring|Install synthetic monitoring]]
- [[create-synthetic-monitoring-locations|Create synthetic monitoring locations]]
- [[create-synthetic-monitor|Create and edit a synthetic monitor]]
- [[identifying-system-issues|Identifying system issues with synthetic monitoring]]
- [[synthetic-monitoring-landing-page|Synthetic monitoring]]
- [[acc-landing-page|Agent Client Collector]]
- [[service-observability|Service Observability]]
