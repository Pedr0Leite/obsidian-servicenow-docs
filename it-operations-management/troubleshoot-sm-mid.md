---
title: Upgrade issues
description: What to do when monitors don't work after upgrading synthetic monitoring.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-operations-management/troubleshoot-sm-mid.html
release: australia
topic_type: topic
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Troubleshoot synthetic monitors, Synthetic monitoring reference, Synthetic monitoring, ITOM AIOps, IT Operations Management]
---

# Upgrade issues

What to do when monitors don't work after upgrading [[synthetic-monitoring-landing-page|synthetic monitoring]].

## Condition

After upgrading synthetic monitoring, monitors remain in unknown state.

## Cause

After upgrading synthetic monitoring, if the monitor is hosted on a MID Server, the server must be restarted to re-recognize the hosted monitors.

## Remedy

Restart the MID Server. See [Manually start, stop, and restart a MID Server](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/t_InstallMIDServerAsWinService.md).

**Parent Topic:**[[troubleshoot-synthetic-monitors|Troubleshoot synthetic monitors]]

## Related

- [[troubleshoot-synthetic-monitors|Troubleshoot synthetic monitors]]
- [[synthetic-monitoring-landing-page|Synthetic monitoring]]
