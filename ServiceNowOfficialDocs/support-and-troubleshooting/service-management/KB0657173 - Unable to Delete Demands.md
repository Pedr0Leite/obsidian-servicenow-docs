---
title: "Unable to Delete Demands"
aliases:
  - KB0657173
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657173
kb_number: KB0657173
last_modified: 2024-04-07
---

## Unable to Delete Demands

  

### Issue

 Unable to delete project requests

### Cause

There are associated Metric and Category Results attached to the Project Request

### Resolution

-   Remove the associated Metric Results in the related list for table: "asmt\_metric\_results"
-   Remove the Category Results in the related list for table: "asmt\_category\_result"
-   Then you can delete the Project Request Demand (dmn\_demand)
