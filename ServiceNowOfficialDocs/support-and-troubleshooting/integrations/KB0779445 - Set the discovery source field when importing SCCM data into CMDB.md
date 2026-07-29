---
title: "Set the discovery source field when importing SCCM data into CMDB"
aliases:
  - KB0779445
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779445
kb_number: KB0779445
last_modified: 2025-07-11
---

## Set the discovery source field when importing SCCM data into CMDB

  

### Summary

This article shows how to set the **discovery\_source** field during the one-direction import of Microsoft System Center Configuration Manager (SCCM) into the ServiceNow Configuration Management Database (CMDB). By default, SCCM data imports do not set this field in the CMDB. 

### Release

Any

### Instructions

1.  Open the SCCM 2016 Computer Identity transform map.
2.  In the Related Links, create a new field map as follows, and then submit:

-   **Map**: SCCM 2016 Computer Identity
-   **Source table**: imp\_sccm2016\_computer\_id
-   **Use source script**: ticked
-   **Choice action**: ignore
-   **Target table**: cmdb\_ci\_computer
-   **Target field**: Discovery source
-   **Source script**: answer = "MS SMS";

![Set Discovery source in Transform Map](/sys_attachment.do?sys_id=c69d3c3f936aae54f2167de86cba1038 "Set Discovery source in Transform Map")
