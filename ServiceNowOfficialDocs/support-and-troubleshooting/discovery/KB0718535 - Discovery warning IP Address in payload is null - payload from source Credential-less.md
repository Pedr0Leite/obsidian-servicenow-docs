---
title: "Discovery warning \"IP Address in payload is null - payload:\"  from source \"Credential-less\"
aliases:
  - KB0718535
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718535
kb_number: KB0718535
last_modified: 2026-05-29
---

## Discovery warning "IP Address in payload is null - payload:" from source "Credential-less"

  

### Issue

The following error is seen when an input payload contains a CI of a class which extends the cmdb\_ci\_harware class and field ip\_address is empty, the source is set to Credential-less:

IP Address in payload is null - payload:

### Release

ALL

### Cause

"Horizontal Discovery Sensor" is responsible in logging these warnings. Before the identification process, this sensor will check if the CI needs to be reconciled with any credential-less discovery created CIs. As part of this process, one preliminary check is to validate if IP Address is not null. If the IP Address is null, discovery would log a warning like "IP Address in payload is null - payload: <Actual Payload>" with discovery source as "Credential-less". 

### Resolution

This is to show useful information that the IP Address is missing in the payload. To resolve the issue:

1.  Review the payload items in the error
2.  Check for CIs that class extends cmdb\_ci\_harware but the IP address field is empty
3.  Is it ok for the ip\_address field to be empty:
    1.  Yes: Disregard the error
    2.  No: Update pattern so that the ip\_address field for the CI is populated
