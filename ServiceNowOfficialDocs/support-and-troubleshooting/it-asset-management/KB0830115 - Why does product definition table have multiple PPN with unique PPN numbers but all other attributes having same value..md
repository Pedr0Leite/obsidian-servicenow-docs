---
title: "Why does product definition table have multiple PPN with unique PPN numbers but all other attributes having same value."
aliases:
  - KB0830115
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830115
kb_number: KB0830115
last_modified: 2025-01-02
---

## Why does product definition table have multiple PPN with unique PPN numbers but all other attributes having same value.

  

### Summary

-   PPN/SKU is a combination of entitlement like Publisher+Product+Edition+Version+Langauge+Platform+Volume+Location+Prod/Non Prod+ could be many other things
-   In the current data model for part numbers, the system\[Content Code\] only captures Publisher+Product+Edition+Version and hence, these might look the same.

  
![](sys_attachment.do?sys_id=a8b638c5dbc478d0fec4fb2439961919)  

  

-   All these PPNs are valid PPNs by Microsoft Corporations and none of the PPN is duplicate.
-   Every end customer buys a particular PPN and that can be used for the requirement.
-   if the PPN which you has is unavailable in Content Library, then kindly raise a case with Servicenow to add the same to Content Library.
