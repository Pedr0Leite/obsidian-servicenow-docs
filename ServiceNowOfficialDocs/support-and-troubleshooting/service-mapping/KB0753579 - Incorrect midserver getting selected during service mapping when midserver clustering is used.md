---
title: "Incorrect midserver getting selected during service mapping when midserver clustering is used"
aliases:
  - KB0753579
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753579
kb_number: KB0753579
last_modified: 2024-04-07
---

## Incorrect midserver getting selected during service mapping when midserver clustering is used

  

### Issue

When midservers with service mapping capabilities are placed in midserver cluster,  any random midserver is picked up during service mapping discovery instead of the ones with SM capabilities.Hence the service mapping fails .

  

  

  

  

### Cause

This is a known issue and is documented in PRB-PRB1329739.

### Resolution

As per the PRB the workaround is not use SM midsevers in a cluster. However this workaround is not a very viable solution for customers sometimes, based upon the network topology which they are trying to discover.

There is another workaround available which they use, in case the first one is not possible:

Workaround 2--> Set the business rule "MID Server Cluster Management" to inactive.   
This is a legacy business rule that changes the MID selected by SM to a random MID server in case this MID is part of a cluster.   
There is no need for this business rule any more and there is no problem to disable it.
