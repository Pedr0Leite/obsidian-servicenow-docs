---
title: "[SAMP] \"End of Life\" not showing up for Software Models specifically for Microsoft publisher"
aliases:
  - KB0953882
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953882
kb_number: KB0953882
last_modified: 2025-01-03
---

## \[SAMP\] "End of Life" not showing up for Software Models specifically for Microsoft publisher

  

### Summary

-   We noticed most of the Software Models are not showing up the "End of Life". Even when looked up in the "Software Model Lifecycle Definitions " (samp\_lifecycle\_definition) table most of them doesn't have "End of life info"not available. i.e. End of Life "Active" = "false".
-   Only a few numbers of Software Model from Microsoft publisher is having this info. 

![](sys_attachment.do?sys_id=f4c044441be2ac900b8a9979b04bcba8)

### Release

-   Instance with Software Asset Management Professional plugin enabled.

### Instructions

-   Microsoft is not publishing the "End of Life" information and hence we (ServiceNow) did not add the same i.e. the "End of Life" is set "Active" = "false" as this is being the restriction from Microsoft. Please refer to the attached snip from Microsoft portal.

![](sys_attachment.do?sys_id=4d328c481be2ac900b8a9979b04bcbfa)
