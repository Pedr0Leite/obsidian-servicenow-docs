---
title: "Connector instance stuck in running state for 2 hours."
aliases:
  - KB0785101
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785101
kb_number: KB0785101
last_modified: 2024-04-08
---

## Connector instance stuck in running state for 2 hours.

  

### Issue

Customer reported that one of the connector instance is stuck in running state for two hours before being erred out.

### Cause

-   OOB, when a connector instance is executed, a ConnectorProbe is created for the targeted MID Server.
-   If the MID Server goes down, its corresponding record in "ecc\_agent" table is updated as "Down".
-   This triggers a Business Rule "Update connectors". The Business Rule update all executing ConnectorProbe on the problematic MID Server to "processed". It also update the connector instances being executed by the MID Server to not running. This would allow next execution of the connector instance to proceed if multiple MID Servers are configured or MID Server is in a cluster.
-   To find the executing connector instances, the Business rules queries the "em\_connector\_instance" table whose name is the same as the ConnectorProbe's source (ecc\_queue.source field). The first matching record is updated to not running.
-   Customer has several connector instances with the same name so the query pulled up multiple connector instances. Depending on the order of the list the DB returned, the first matching record could be the wrong connector instance. This was the case. The intended Connector instance was not updated leaving it in the running state.
-   Two hours later the "Event Management - Update Stuck connectors" scheduled job determined that the connector instance is stale and erred it out.

### Resolution

Correct the connector instances names and make sure they are unique.
