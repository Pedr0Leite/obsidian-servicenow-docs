---
title: "How to configure country/region-specific holidays for SLAs"
aliases:
  - KB0758427
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758427
kb_number: KB0758427
last_modified: 2024-04-07
---

## How to configure country/region-specific holidays for SLAs

  

### Issue

The user has callers from various regions and countries. With this in mind, the user wanted to know how to apply holidays in their associated schedules to only certain regions (as not every region/country share the same holidays).

### Resolution

After much deliberation and testing, it was found that the best method for applying region-specific holidays is to create region-specific SLA Definitions.  
  
As an example, on a SLA Definition for the country of France, the user could write an initial discriminatory Start condition saying something like "Caller.Country code -- is -- France".'

Thereafter, the user would build out their subsequent conditions. In this way, only callers with the "Country code" of "France" would have the SLA Definition (and the associated Schedule with those region-specific holidays) apply.   
  
While the above may initially take some time to flesh out, this would wholly fulfill the requirement of having region-specific holidays apply properly per region. Perhaps also there could be some mainstreaming of the definitions to reduce the amount of SLA Definitions required per region.
