---
title: "Events from the NNMi connector show \"State\" as \"Error\" and the \"Time of Event\" field would be \"empty\" or \"Invalid_value\"."
aliases:
  - KB0743765
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743765
kb_number: KB0743765
last_modified: 2024-04-07
---

## Events from the NNMi connector show "State" as "Error" and the "Time of Event" field would be "empty" or "Invalid\_value".

  

### Issue

Events from the NNMi connector show "State" as "Error" out and the "Time of Event" filed would be empty.

### Release

Kingston, London

### Cause

For a few events, they may not have milliseconds information in the time of the event field, as this value is missing we see the following error and the state of the event will be in "error".

time\_of\_event: Invalid value.

### Resolution

-   From the Navigation Filter go to Event Management -> Connector Definitions.
-   Open "NNMi" connector -> Open NNMIEvents\_JS script.
-   Replace line 398
-   `var msec = parseFloat(m[9]);      with      var msec = parseFloat(m[9])|0;   `

  
With this change, if the milliseconds in the time of event is empty it will consider that as a "Zero".
