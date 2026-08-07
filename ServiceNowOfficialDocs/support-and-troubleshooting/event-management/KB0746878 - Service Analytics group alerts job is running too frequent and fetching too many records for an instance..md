---
title: "\"Service Analytics group alerts\" job is running too frequent and fetching too many records for an instance."
aliases:
  - KB0746878
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746878
kb_number: KB0746878
last_modified: 2024-05-21
---

## "Service Analytics group alerts" job is running too frequent and fetching too many records for an instance.

  

### Issue

# Symptoms

"Service Analytics group alerts" job is running too frequent and fetching too many records for an instance

# Release

All Versions.

# Explanation

Alerts in em\_agg\_group\_alert table would get deleted when the alert is closed and passed 90 days.

If the alert rate is high(i.e if a huge number of alerts are getting created in your environment) and you see slowness in the queries, reduce the time of the flush(Deleting records).

To do this, follow the below steps:

-   Go to sys\_auto\_flush table
-   Search for the em\_agg\_group\_alert table name.
-   Decrease the number of seconds to what you want to keep the groups, for example, 30 days (and in seconds, it should be 30 \* 24 \* 60 \* 60)

Also, please verify in event management --> properties the following property "Auto close interval (in hours), within which open alerts will be automatically closed. Setting the property to 0 will disable this feature but it is not recommended. It should be a week (168) or less because if alerts are not closed, the groups are still kept open.
