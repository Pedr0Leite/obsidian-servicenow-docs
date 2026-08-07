---
title: "All Custom license metrics are not displayed in entitlement"
aliases:
  - KB0997804
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997804
kb_number: KB0997804
last_modified: 2026-04-22
---

## All Custom license metrics are not displayed in entitlement

  

### Issue

-   When creating an entitlement , Not all custom License metric can be displayed.
-   Example : There are more than 20 custom license metric define in samp\_sw\_license\_metric\_custom.
-   However when creating an entitlement , you can only view 14 or less

### Release

-   Paris or later

### Cause

-   Due to less number set in glide.xmlhttp.max\_choices property

### Resolution

-   Navigate to Sys\_properties.LIST
-   Search for glide.xmlhttp.max\_choices
-   Check the count and increase to 50 . 
-   Now navigate to alm\_license.LIST
-   Click new 
-   select metric group as custom
-   All license metric will be showing now
