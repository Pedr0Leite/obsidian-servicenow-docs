---
title: "Flow is being triggered multiple times on RITM"
aliases:
  - KB0965066
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0965066
kb_number: KB0965066
last_modified: 2024-05-21
---

## Flow is being triggered multiple times on RITM

  

### Issue

-   flow is executing multiple times on the RITM (requested item) 

### Cause

Could be caused by the following:

-   the business rule "Start FlowDesigner Flow" has been customized, passing another GlideRecord into method fireCatalogTrigger
-   In Quebec, if the very first thing the SC flow is doing is setting the stage to "Request Approved" this will update the RITM to set the stage and trigger the business rule "Start FlowDesigner Flow" again
-   In the transaction where RITM was approved if there is a business rule where a GlideRecord query was done to obtain the RITM and then updated, this will trigger the business rule "Start FlowDesigner Flow" again. Set business rule to after or use getRefRecord() to obtain the GR object of RITM.
