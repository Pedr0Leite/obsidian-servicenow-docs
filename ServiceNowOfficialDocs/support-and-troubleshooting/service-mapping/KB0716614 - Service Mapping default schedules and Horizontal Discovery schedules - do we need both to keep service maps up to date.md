---
title: "Service Mapping default schedules and Horizontal Discovery schedules - do we need both to keep service maps up to date?"
aliases:
  - KB0716614
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716614
kb_number: KB0716614
last_modified: 2024-04-07
---

## Service Mapping default schedules and Horizontal Discovery schedules - do we need both to keep service maps up to date?

  

### Issue

# Overview

* * *

There are two schedules which are active by default with Service Mapping plugin

1.  All Applications
2.  Load Balancer Services

# Subject

* * *

The above two Discovery Schedules need to be run even when you are using Horizontal Discovery on IP's to discover CI's. These two schedules trigger the ServiceDiscoveryProbe, which runs a top down discovery on the endpoints across all the business services.

So it is essential to run these schedules to keep the service maps updated along with running horizontal discovery to discover individual CI's that are part of the service maps.
