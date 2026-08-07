---
title: "Configure Indicators in Batch"
aliases:
  - Configure Indicators in Batch
tags:
  - servicenow-dev-program
  - code-snippet
  - configure-indicators-in-batch
  - performance-analytics
---

# Configure Performance Analytics in Batch

## Problem it solves

When dealing with many PA indicators, it can become cumbersome to manually configure each of them. Typical things to configure are:
* Excluded statistics (for example the SUM stats are not applicable to percentage units)
* Precision
* Direction
* Visibility settings
* Whether the indicator is key or not
* Value when nil
* Data retention periods
* Some data aggregations (can consume lots of calculation time for nothing if they're not required)

I realised that more than often, I want the same baseline config for all the indicators of a given domain or application. 

## Solution

This code snippet loops through all the indicators that match a query, and configure them one by one. Here, this is an example of how I configure them, but each use case might require different properties. The code of the script can remain the same though, and adapted to change the values, or even update more properties.

## Possible Improvements

Extend this code snippet to:
* Add breakdowns
* Add indicator groups
* Add/create data collection job

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0689652 - Troubleshooting users unable to access responsive dashboards|Troubleshooting users unable to access responsive dashboards]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715670 - Does not have access to performance_dashboards_main.do blank|Does not have access to performance_dashboards_main.do blank]]
