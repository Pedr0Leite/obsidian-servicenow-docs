---
title: "Including a MID Server in multiple MID Server load-balancing clusters may cause Discovery authentication or timeout errors"
aliases:
  - KB0635604
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635604
kb_number: KB0635604
last_modified: 2024-04-07
---

## Including a MID Server in multiple MID Server load-balancing clusters may cause Discovery authentication or timeout errors

  

### Issue

Including a MID Server in multiple MID Server load-balancing clusters may cause Discovery authentication or timeout errors

  
  

# Issue

* * *

MID server included in multiple MID server load-balancing clusters. When launching Discovery with any of those MID server clusters or MID servers, intermittent Discovery errors occur and some CIs are not being discovered completely.

Example error: "SNMP probe timed out. Target is either unreachable or there are no valid credentials for it".

# Cause

* * *

When any of the MID servers in the clusters is used by Discovery, Discovery automatically uses all the MID servers in the cluster to load balance discovery jobs. This means that no matter which MID server or MID server cluster is chosen, one cluster can get another cluster's MID servers involved in Discovery. If those clusters have different credentials or capabilities configured for their MID servers, errors regarding credentials or capabilities can occur.

# Solution

* * *

One MID server included in multiple load-balancing clusters can cause multiple MID clusters to be involved in one Discovery.

To fix this issue, do not include MID servers in multiple MID server load-balancing clusters. Best practice is that one MID server should appear in only one load-balancing MID server cluster. Also, ensure that each MID server in a cluster has the same credentials and capabilities.
