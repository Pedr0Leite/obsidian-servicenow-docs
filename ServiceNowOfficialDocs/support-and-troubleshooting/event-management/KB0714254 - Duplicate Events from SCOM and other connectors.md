---
title: "Duplicate Events from SCOM and other connectors"
aliases:
  - KB0714254
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714254
kb_number: KB0714254
last_modified: 2024-04-07
---

## Duplicate Events from SCOM and other connectors

  

### Issue

# Overview

* * *

When you check the records on the em\_event table you will notice duplicates as in same Time of Event and Message Key

# Additional Information

* * *

This is an expected behaviour.

We pull the data from SCCM using the following criteria:

-   Query for 500 events order by LastModifiedDate
-   Last event's LastModifiedDate is used as cutoff datetime for next query
-   Next query is to query for next 500 events > last cutoff datetime.

Therefore if there is more than one event created on the same second we might pull it twice. This is not an issue and we process these duplicates using the threshold rules.

It doesn't affect instance performance neither overload the database as the event table gets rolled over every week.
