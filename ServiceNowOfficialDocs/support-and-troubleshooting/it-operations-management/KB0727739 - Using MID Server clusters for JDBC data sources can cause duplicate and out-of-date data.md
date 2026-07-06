---
title: "Using MID Server clusters for JDBC data sources can cause duplicate and out-of-date data"
aliases:
  - KB0727739
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727739
kb_number: KB0727739
last_modified: 2026-02-11
---

## Using MID Server clusters for JDBC data sources can cause duplicate and out-of-date data

  

### Issue

The JDBC probe is usually used for large data imports. Because of this, the probe does not return all the data in a single payload but rather batches a fixed number of rows at a time into many payloads (chunks). Dedicated MID servers allow for the collection of accurate data when a payload is chunked.  MID Server clusters cannot guarantee the accuracy of the chunked data.

### MID Server clusters and JDBC data sources

Load balancing includes fail-over, initially load balancing to healthy MID Servers but if the MID server fails, we assign probes on the failed MID to other MIDs.  If in the middle of a JDBC probe execution the MID Server goes down and chunks have already been committed to the instance, there is no simple way for another MID Server to pick up where the failed MID left off. So, the new MID server reruns the same query and reimports the same records. This can result in duplicate data. 

If the failed MID Server has partial data that was queued before it went down, it sends this data chunk to the instance when it comes back up. The fail-over MID Server may have already sent the same chunk back to the instance. Because the data chunks do not have timestamps, there is no way for the integration to resolve the out-of-order data.
